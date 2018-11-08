Big data --> 3 v's - IBM

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


OLTP			v/s		OLAP  

Transactional				Analytical  
RDBMS					DWH  
NoSQL					Hadoop  


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


## HDFS Architecture  

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


