
- [1. BIG DATA](#10)  
- [2. HDFS Architecture  ](#20)  
- [3. Hadoop](#30)  
- [4. Hive](#40)  

## <a name="10"></a>1. big data  
***Big data --> 3 v's - IBM

Big data is a term for data sets that are so large or complex that traditional data processing applications are inadequate to deal with them.
Challenges include analysis, capture, data curation, search, sharing, storage, transfer, visualization, querying, updating and information privacy.  

1) Volume --> How many zeros in yotta bytes. --> 24 zeros.  

2) Velocity --> Speed of the data arrival.  

	--> Algo Trading  
	--> AML  
	--> Fraud Analytics  
  
3) Variety:-  
	a) Structured --> schema aware, fixed rows and cols, data types  
	b) Semi-Structured --> textual data having no schema -- emails, logs, blogs, comments, JSON  
	c) UnStructured -->   
		images -- Cheques   
		video -- CCTV, security  
		audio -- trader's call, Customer confirmation calls  

http://www.ibmbigdatahub.com/infographic/four-vs-big-data  


Analysis		v/s		Analytics  

Reporting [ historical]			Predictive  
RDBMS, BI				RDBMS,NoSQL - SPSS, SAS, R  


|  OLTP			|		OLAP   |
|  --  |  --  | 
|  Transactional	|			Analytical  |  
|  RDBMS		| 			DWH  |   
|  NoSQL		|  			Hadoop  |   


Biggest Diffentiator between RDBMS and Hadoop  
Centralized 	v/s 	Distributed	--> Storage + Processing  


ETL			v/s		ELT  
Extract Transform Load			Extract Load Transform  
Process while streaming			Hadoop  


Data going to Code		v/s 		Code going to Data  
Traditionally					Hadoop  
Centralized					Distributed  


What is Virtualization  
1) It is the ability to run a different OS within a OS. [ We will be running ubuntu inside windows ]  
What are the 4 common virtualization softwares  
1) VmWare  
2) Virtual box  
3) Hyper-V  
4) KVM  


Master --> metadata  
Slaves --> actual data  

## <a name="20"></a>2. HDFS Architecture  

HDFS --> daemons --
			NameNode		-	Master - maintains the metadata
			Data Node		-	Store the actual data - blocks
			Secondary NameNode	-	Checkpointing if there is no Passive NN
			

***Is HDFS a physical or a virtual file system? Virtual.***  
If we put a file called sample into the cluster.  

	a) Where will i see the file sample? HDFS level  
	b) Will i see the file sample at the node level? No, we will only see the blk files.  



1) Master - Slave Architecture --> Master [ Server Grade ] & Slave [ Commodity machine ]  
Commodity --> No dual power supply, No RAID, No high memory configuration, huge amount of storage.  
4PB --> 250 nodes - each node have 6 TB storage.  

2) Block size --> Unit of data that can be read / written.  
	Linux --> 4K  
	Hadoop --> 128MB [ Everything is configurable ]  

3) Redundancy:- Block Replication. The default is 3 [ 1+2 ], on different nodes. This can be changed at the file level granurality.  

All the modules in Hadoop are designed with a fundamental assumption that hardware failures are a common occurrence and should be automatically handled by the framework.  
		
### ***File Injestion Process***
Cluster --> set of machines acting like one entity.

Client A: sample - 200 MB -- put this in to the cluster.
[Not a part of the cluster ]

				Master

1	   2	3	  4	  5  	6  	7  	8  	9  	10  
128	 72			   128	72	72		  128  

1) Whom will the client talk to? Master  
2) How will the client know who the master is? via config files. Should hadoop be present on the client? YES only the extracted hadoop and the config files.  
3) What will be the master's reponse to the client request? He will give the write pipeline [ slave ips ]. How many slave ips will be give.  

	128[ 1, 5, 9 ]
	 72[ 2, 6, 7 ]

Note: The client will write only to the first node for every block.  
4) How is the first node for a block decided by the master? Based on the network proximity between the client and the slaves and then of course the avilability.  
5) How are the other nodes decided? NOT BASED ON PROXIMITY NOW. But based on the data distribution [ load balancing ]. If there are multiple nodes available, then based on random distribution.  
6) When will replication start? Immediately [at 4 k levels ]when writing happens on the first node for every block.   
7) When will the final write confirmation go from the client to the master? Once the reverse checksum information comes from 9 - 5 - 1 and then from 7 - 6 to 2 and then 1 and 2 will give it to the client.  

### File Read Architecture

					Master

1	  2	  3	  4	  5	  6	  7	  8	  9	  10  
128	72			    128	72	72		  128  

							Client B
						Read Pipeline
						[9,5,1]
						[7,6,2]

### Failure Use Cases :-

 1) While Writing  
	a) Primary Node[1,2]: Node 1 goes down after 100 MB of data is written.  

		1) Will the client be aware of the failure? YES. As he has opened socket connection to the node 1 and 2 for writing.  
		2) What should the client do now? Start the write process again. Again communicate back to the master, who will send a new write pipeline.  
		3) How much data should the client send now as a part of the write process? The complete file has to be rewritten.  
		4) What will happen to the 100MB & 72 MB data written and replicated. --> Orphaned or zombied blocks, which needs to be deleted via a cron job, which runs fsck.This has to be executed explicitly.  

				Master

1	2	3	4	5	6	7	8	9	10
128	72			128	72	72		128

	b) Replicated Nodes: Node 9 goes down after 100 MB of data is written.  
		1) Will the client be aware of the failure? No  
		2) How will the framework handle it. The master will assign a new node for the failed node. [ 8 ], and will inform 5 to write the complete block to 8.  


 2) After Writing  

	Any node goes down. Will the Admin have to do anything other then formatting the failed node? Nothing.  

	The master [ hadoop framework ]  will assign a different node in place of the failed node and request a node which has the data to copy this on to the newly assigned node.  
  The frame work will ensure that at any point of time, it adheres to the replication policy.  

	--> What will happen is the failed node comes -->  

	Less than 10 minutes --> It will automatically added back to the cluster.  

	More than 10 minutes --> all the blocks in the node is invalid.  
  
  
-------------------     
For each of the components, there is a xml file.  

There would be a XXX-default.xml file which will give you all the listing of the default properties.  

There will be a XXX-site.xml file inside etc/hadoop folder of the hadoop installation, where we will have to write the properties which needs to be overridden.  


## deamons in hadoop  

|   |  HDFS  | YARN  |
|  --  |  -- |  --  |
|  Master  |  Namenode  | ResourceManager  |
|  Slave  |  Datanode  |  NodeManager  | 
|  |  SecondaryNameNode OR Passive Namenode  |   |
			

## 4 node cluster --> on which machine will the deamons be running  

	Master	{	NN	SNN	RM	} --> 3 machines

	Slaves	{	DN+NM	DN+NM	DN+NM	DN+NM	}  


http://media.bestofmicro.com/X/8/430172/original/yarn.png


|   		|	 NN  |  SNN  |	RM  | 	Slave  | 	Client  |  
|  -- |  -- |  -- |  --  |  --  |  --  |
|  core-site.xml > fs.defaultFS | 	YES  | 	YES  | 	YES  |	 YES  |   YES  |  
|  hdfs-site.xml > dfs.replication  | 	YES  | 	No  | 	No  | 	No  | 	No  |  
|  dfs.namenode.name.dir  | 	YES  | 	No  | 	No  | 	No  | 	No  |  
|  dfs.datanode.data.dir  | 	No  | 	No  | 	No  | 	YES  | 	No  |    
|  mapred-site.xml  | 		No  | 	No  | 	YES  |   No  | 	No  |  
|  yarn-site.xml  |	 	No  | 	No  | 	YES  |	No  | 	No  |   



### How metadata is handled in HDFS  

2 things that represents the metadata of a cluster --> 
	a) fsimage --> Snap shot of the FS at a point of time
	b) edits_inprogress --> redo logs in oracle
	

For the first time, when we format the NN and start the services  

1) fsimage --> snapshot of the FS at a point of time  
2) edits_in_progress  
3) edits_XXXXXX03-XXXXXXXX40  

	--> HDFS Architecture with respect to Metadata

https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html

https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsUserGuide.html#Secondary_NameNode

Where is the meta data of the cluster stored?

1) Main memory of the NN		PLUS
2) a persisted copy will be present in fsimage and edits


### Checkpointing process

Checkpointing --> Some time interval [ 1 hour ] --> 

The SNN copies the edits_inProgress + fsimage from the NN, loads it its internal memory and applies the edits_inprogress on the fsimage and create a new fsimage and copies this fsimage to the NN also.	

1) The SNN will copy the fsimage and edits in progress to its local system, load it in to memory, apply the edits in progress and create a new fsimage  

4 clock --> fsimage_20 edits in progress  
5 clock --> SNN will copy these files, apply the image and get a new fsimage_30  
6 clock --> SNN will copy these files, apply the image and get a new fsimage_40  
6.30 --> restart my machine -->   

2) It will then copy the new fsimage to the directory in the NN also.  


==> What will be present on the Data Nodes?
	a) blocks
	b) .meta file which contains the checksum information for a block.
	
	
### Metadata of Hadoop

1) fsimage --> snapshot of the filesystem when checkpointing happened   
2) edits_in_progress --> logs of what happened on the FS after the previous checkpoint   
3) edits_XXXX-XXXX --> These are the individuals edits which have been stored so that we can roll back to a earlier point.  


## <a name="30"></a>3. Hadoop  

- core-site.xml --> IP address of your NN. --> 9000 port will be used by the datanodes for the RPC communication. This will also be used by the client.  

- hdfs-site.xml --> replication - the default is 3.  


### Zookeeper
Zookeeper is the component which ensure that the masters have a leader and when the leader goes down, it will assign another leader.

http://hadoop.apache.org/docs/current2/hadoop-project-dist/hadoop-hdfs/HDFSHighAvailabilityWithQJM.html

### Map Reduce

1) Map --> 	pick what you want from a record.
		Works parallely on each node
		The result is shuffled sorted 
--> Magic Phase of Shuffling --> Bring together all the values of the similar key together so that we can perform reducing

2) Reduce --> 	aggregation based on the map functionality

***3 aspects / faces of map reduce

1) Programming Model --> Divide & Conquer --> Can be applied to any language and any framework  
2) It is a API --> Allow developers to use the framework classes so that the functionality can be used.  
3) It is a Runtime --> Resource Manager + Node Manager  

***Pre-req information you need before processing

1) dataset  
2) result of the analysis - knowledge of the data  
3) What is a record? The default record seperator --> \n [ new line ]  


***In any Map Reduce Program, How many classes will be there?  

Map Class --> Business logic of what i should pick from a record   
Combiner  
Partitioner  
Reduce Class --> Business logic of aggregation  
Driver Class --> Build my Job and send it across to the Cluster  


### 6 Phases in Map Reduce

5 Node Cluster

sample -- 200

	1		2		3		4		5
			128 - M				72 - M

Shuffler + Reducer process can run on any of the data nodes which ever is free. Also Note by default there would be only 1 reducer per job.

					Reducing


1] Input Phase - Block

2] Splitting Phase. There are 2 types of splits in Hadoop

	a) Block Split 		--> Writing	physical
	b) Record Split
	   Logical Record	--> Reading	logical


key --> cursor position [ moves left to right like a cursor ]
value --> the record.

3] Mapping phase: Here you will write the business logic of what is needed from a record.

	1) txns  
	2) Sum of Sales across cities  
	3) record is a new line.	 
```
00000000,06-26-2011,4007024,040.33,Exercise & Fitness,Cardio Machine Accessories,Clarksville,Tennessee,credit
00000001,05-26-2011,4006742,198.44,Exercise & Fitness,Weightlifting Gloves,Long Beach,California,credit
00000002,06-01-2011,4009775,005.58,Exercise & Fitness,Weightlifting Machine Accessories,Anaheim,California,credit
00000003,06-05-2011,4002199,198.19,Gymnastics,Gymnastics Rings,Milwaukee,Wisconsin,credit
00000004,12-17-2011,4002613,098.81,Team Sports,Field Hockey,Nashville  ,Tennessee,credit
00000005,02-14-2011,4007591,193.63,Outdoor Recreation,Camping & Backpacking & Hiking,Chicago,Illinois,credit
00000006,10-28-2011,4002190,027.89,Puzzles,Jigsaw Puzzles,Charleston,South Carolina,credit
00000007,07-14-2011,4002964,096.01,Outdoor Play Equipment,Sandboxes,Columbus,Ohio,credit
00000008,01-17-2011,4007361,010.44,Winter Sports,Snowmobiling,Des Moines,Iowa,credit
00000009,05-17-2011,4004798,152.46,Jumping,Bungee Jumping,St. Petersburg,Florida,credit
```

In this example: Key will be the city and the amt will be the value.

Where is the output of the mapping phase stored? Nodes where the processing has happened. [ Node 2 and Node 4 where the blocks were present in our example]

4] Shuffling --> Controls Shuffling --> Master of the Processing Layer  

Where is shuffling done? on Any Slave which is decided by the RM.  

Can shuffling start when any blocks is finished? YES  

There are 2 parts of the Reducing  

	a) To bring the data from the mapper output locations in different nodes to the reducer JVM. This i sthe shuffling process  

5) Reducing --> We perform the aggregations  

6) Output Phase --> Were the output of reducing is stored in HDFS  


### Rules for Broken Records :-   

***1) The possibility of a broken record comes only in the last record for a block.   
2) The second block onwards will start processing from the beginning of a record only. That means if we have a broken record in the 2nd block, it will not be processed by the second block at the beginning.   
3) When the first block finds that at the end of the block, there is no recording ending, it will tell the RM to request the other block on a different node to share that record to the first block and then processing will happen.    

### hadoop jars

The dependency jar files are present in  

1) hadoop-2.7.2\share\hadoop\mapreduce --> all jars here  
2) hadoop-2.7.2\share\hadoop\mapreduce\lib --> all jars here  
3) hadoop-2.7.2\share\hadoop\common --> all jars here  

Tight Coupling v/s Loose Coupling between different classes  

1) Tight --> Using Inner classes [ Mapper and Reducer ] would be within the Driver class  

2) Loose --> Each of them as seperate java files itself.  


### Walk Through of the code  

***The access pattern in Hadoop is WORM --> Write Once Read Many  

***Hadoop does not support Updates:- SCD Type2  

> https://en.wikipedia.org/wiki/Slowly_changing_dimension  

To get a list of linux options possible in hdfs --> hdfs dfs - press enter

Speculative Execution:- http://hadoopinrealworld.com/speculative-execution/

Deep Dive in to Code:-

1) What are the life cycle methods of mapper --

	setup
	map / run
	cleanup

2) What are the Mapper and Reducer classes static? Called from the Driver class via the job class

3) What is the  < > line in the mapper class? Generics --> compile time type safefy

4) What is LongWritable, Text? Wrapper given by Hadoop Framework. This is to create Avro Style Serialization - Page No 108 of the Def Guide

5) What is context in the map function? 

6) The InputFormat class specifies the record splitting logic. The default is TextInputFormat

7) job.setMapOutputKeyClass and Value class because there is Generic Erasure at runtime


***Ex - 2 --> Location of the Sysout statement. 

Complete Flow of the Map Reduce Programme.  

1) Client submits the jar file via hadoop jar  

2) The request goes to the Resource Manager [RM ]  

3) The RM will allocate a Application Master to handle the life cycle of that particular application. This AM will be started on any data node which is available.  

The per-application ApplicationMaster is, in effect, a framework specific library and is tasked with negotiating resources from the ResourceManager and working with the NodeManager(s) to execute and monitor the tasks.  

4) The RM will communicate with the NN to get the block details of the file that is being analyzed.  

5) The RM will communicate with the Applicaton Master and give that information to him.  

6) The AM will communicate with the NM on the nodes where the blocks are and the Node Manager will start the Map containers.  

7) These NM will communicate with the DN to get the blocks and do the processing.  

8) The life cycle of the application is taken care of by AM.  


***Ex3 --> Find out the Max Temp per year.

dataset: 1901_S
Schema --> fixed position --> Year and The Temp
Purpose: Find out the max temp per year.

k1 --cursor
v1 --complete record
k2 -- year
v2 -- temp	--> Map function

shuffler: Bring together all values for the similar years

k3 - year
v3 - max temp


***Ex- 4 --> Optimization via the combiner

If we have a lot of similar keys from the mapper, then the following 2 counter values should be checked:-

1) Network IO -- Reduce Shuffled Bytes
2) Disk IO --> spilled records.

		Map Writing    - 6
		Reduce Reading - 6

1901_C dataset --> 6565 readings per year and we have 2 years of data in this file. 1901 and 1902.

Run the same jar with this new dataset and tell me

	Network IO		-> 144436
	Disk IO			-> 26260

Now let us optimize the performance by introducing the Combiner. This is like a mini reducer running on the map side. This will be called before the data is written to the disk.

Combiner takes the input from the mapper and performs aggregation. If the logic of the mapper and reducer is the same, then we can use the reducer class itself as the combiner.

	Network IO		-> 28
	Disk IO			-> 4 [ 2 unique years, 2 for map writing and 2 for reduce reading ]

If combiner is so beneficial, why was it not set to true by default in the framework?

If we use combiner in logic like median, avg, std dev --> will it work? They is why the combiner is kept optional.

======================================

***Ex 5: Sum of Transactions per product [ Sub Category ]. 

Plus we need to find out the total number of sub category items --> This info will be available from the counters. 

The schema of the txns file is 

txnid, date, custid, amount, primary_product, sub_category, City, State, Cash / Credit

00000009,05-17-2011,4004798,152.46,Jumping,Bungee Jumping,St. Petersburg,Florida,credit

Map Phase: pick the sub category and the amount

Shuffle Phase: All the values for similar sub categories will be brought together by the shuffler

Reduce Phase: Perform Aggregation.Note: The final result that i want should be of not more than 2 decimals

Imp Points: We can use the Reducer class as a combiner only if the key value of the mapper and the reducer are the same.If not it will give the ClassCastException.

If we still need to use a combiner, we will have to explicitly write a combiner class, which will extend the Reducer class itself, as there is no Combiner class in the framework.

***Ex 6: For testing the business logic of the map and reduce functions, we will have to use the MR Unit Library.

3 Drivers-->
	MapDriver<k1,v1,k2,v2>
	ReduceDriver<k2,v2,k3,v3>
	MapReduceDriver<k1,v1,k2,v2,k3,v3>
	
Junit methodology

1) @Before --> setup --> create the necessary instances
2) Unit Test Case
	Pass some input values
	Specify the expected output values
	runTest

Ex 7 --> Working with a Group By Example --> Partitioner.

4 classes here.

hdfs dfs -rm-r /input/partitiondata.txt

## <a name="40"></a>4. Hive

### Difference between Internal V/s External Table

A] Location of Data
1) Int: /user/hive/warehouse/Name.db/Tablefolder in HDFS
2) Ext: Can be present anywhere in HDFS

B] Is a load required?
1) Int: Yes
2) Ext: No as the data is already uploaded by the upstream in to a specific folder in HDFS

C] Who has permission on the data folder?
1) Int: Hive
2) Ext: Not hive, but HDFS

D] What happens when i drop a table?
1) Int: Both the structure & the data will be deleted.
2) Ext: Only the structure is deleted and the data will be present in HDFS.

E] Syntax
1) Int: Normal syntax
2) Ext: The word external should be present before the table word + folder location should be given at the time of table create itself.

 sqlContext.sql("CREATE external TABLE IF NOT EXISTS customer1 (id INT, name STRING,city STRING, state STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' location '/TempCust'")


