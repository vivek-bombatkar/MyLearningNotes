
# Databricks - Apache Spark™ Certified Developer  
> https://databricks.com/training/certified-spark-developer

## Index  
- [1. General IMP links](#10)  
- [2. Points to consider](#20)  
- [3. Course topics](#30)  
- [4. Notes from the books / guides.](#40)  
  - [4.1 Learning Spark: Lightning‑Fast Big Data ](#41)
  - [4.2 High Performance Spark](#42)
  - [4.3 Machine Learning with Spark: Nick Pentreath ](#43)  
  - [4.4 https://databricks.gitbooks.io/databricks-spark-knowledge-base/content/ ](#44)   
  - [4.5 Programming Guides from http://spark.apache.org/docs/latest/ ](#45)  
- [5. SparkSession & pyspark.sql.functions f](#50)  


## <a name="10"></a>1. General IMP links  


### Free online Spark clusters for getting started!   
- [databricks](https://community.cloud.databricks.com/)  
- [zepl](https://www.zepl.com/)  
- [colab from google](https://colab.research.google.com/)   

> [code comments from Git](https://github.com/apache/spark)
> https://github.com/vivek-bombatkar/Spark-with-Python---My-learning-notes-  
> https://jaceklaskowski.gitbooks.io/mastering-apache-spark/content/  
> https://www.slideshare.net/cloudera/top-5-mistakes-to-avoid-when-writing-apache-spark-applications  
> https://pages.databricks.com/rs/094-YMS-629/images/7-steps-for-a-developer-to-learn-apache-spark.pdf   
> [Table of Contents](http://shop.oreilly.com/product/0636920028512.do)   
> https://docs.databricks.com/index.html  
  - practice example from databricks 
  - https://docs.databricks.com/spark/latest/gentle-introduction/index.html  
> http://www.bigdatatrunk.com/developer-certification-for-apache-spark-databricks/  
> http://spark.apache.org/docs/latest/rdd-programming-guide.html  
 



## <a name="20"></a>2. Points to consider
- 40 questions, 90 minutes  
- 70% programming Scala, Python and Java, 30% are theory.  
- Orielly learning spark : Chapter’s 3,4 and 6 for 50% ; Chapters 8,9(IMP) and 10 for 30%  
- Programming Languages (Certifications will be offered in Scala or Python)  
- Some experience developing Spark apps in production already  
- Developers must be able to recognize the code that is more parallel, and less memory constrained. They must know how to apply the best practices to avoid run time issues and performance bottlenecks.  



## <a name="30"></a>3. Course topics 
- [a. Spark Concept](#a) 
- [b. WEB UI / Spark UI  ](#b)
- [c. RDD + DataFrame + DataSets + SparkSQL  ](#c)
- [d. Streaming](#d)
- [e. SparkMLLib ](#e)
- [f. GraphLib ](#f)


### <a name="a"></a>a. Spark Concept  
> https://github.com/vivek-bombatkar/Spark-with-Python---My-learning-notes-  
> http://spark.apache.org/  
> https://databricks.gitbooks.io/databricks-spark-reference-applications/content/index.html  
> https://thachtranerc.wordpress.com/2017/07/10/databricks-developer-certifcation-for-apache-spark-finally-i-made-it/  
> https://www.youtube.com/watch?v=7ooZ4S7Ay6Y  
> [Overview](https://www.youtube.com/watch?v=tFRPeU5HemU)

- IMP:  Broadcast variables and Accumulators, Shuffles, Shuffles , Performance tuning  , Partitioning  

-  Spark Standalone Mode  
  - In addition to running on the Mesos or YARN cluster managers, Spark also provides a simple standalone deploy mode.   
```
./bin/spark-shell --master spark://IP:PORT
# URL of the master
```

- supervise flag to spark-submit    
  - In standalone cluster mode supports restarting your application automatically if it exited with non-zero exit code.  
  
- Dynamic Allocation
  - https://spark.apache.org/docs/latest/configuration.html#dynamic-allocation
  - scales the number of executors registered with this application up and down based on the workload. 
  - spark.dynamicAllocation.enabled  

- Speculative execution 
  - spark.speculation	
  - If set to "true", performs speculative execution of tasks. This means if one or more tasks are running slowly in a stage, they will be re-launched.

- locality wait
  - spark.locality.wait		
  - How long to wait to launch a data-local task before giving up and launching it on a less-local node. The same wait will be used to step through multiple locality levels (process-local, node-local, rack-local and then any). It is also possible to customize the waiting time for each level by setting spark.locality.wait.node, etc. You should increase this setting if your tasks are long and see poor locality, but the default usually works well.

- Types of RDD
  - HadoopRDD, FilterRDD, MapRDD, ShuffleRDD, 




> Performance Tunning
- http://spark.apache.org/docs/latest/tuning.html  
- when tuning a Spark application – most importantly, data serialization and memory tuning.
- CPU, network bandwidth, memory 
- a. Data Serialization:  
  - Formats that are slow to serialize objects into, or consume a large number of bytes, will greatly slow down the computation.  
  - Java serialization (default)  
  - Kryo serialization: SparkConf and calling conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer").  
- b. Memory Tuning:   
  - the amount of memory used by your objects (you may want your entire dataset to fit in memory),   
  - the cost of accessing those objects  
  - the overhead of garbage collection (if you have high turnover in terms of objects).  
- Memory Management Overview :   
  - two categories: execution and storage.  
  - Execution memory refers to that used for computation in shuffles, joins, sorts and aggregations,   
  - Storage memory refers to that used for caching and propagating internal data across the cluster.  
  - When no execution memory is used, storage can acquire all the available memory and vice versa.  
  - spark.memory.fraction  
  - spark.memory.storageFraction  
- ***How Determining Memory Consumption***  
  - create an RDD, put it into cache, and look at the “Storage” page in the web UI  
  - SizeEstimator’s estimate - consumption of a particular object  
- Tuning Data Structures  
  - avoid the Java features that add overhead, such as pointer-based data structures and wrapper objects.   
  - prefer arrays of objects, and primitive types, instead of the standard Java or Scala collection classes  
  - Avoid nested structures with a lot of small objects and pointers when possible.  
  - Consider using numeric IDs or enumeration objects instead of strings for keys.  
- Serialized RDD Storage  
  - When your objects are still too large to efficiently store despite this tuning, a much simpler way to reduce memory usage is to store them in serialized form  
  - Downside is performance hit, as it add overhead of deserialization every time  
- Garbage Collection Tuning  
- ***Level of Parallelism***  
  -  Spark automatically sets the number of 
   - “map” tasks to run on each file according to its size (though you can control it through optional parameters to SparkContext.textFile, etc),   
   - and for distributed “reduce” operations, it uses the largest parent RDD’s number of partitions.   
  - spark.default.parallelism   
  - recommend 2-3 tasks per CPU core in your cluster.  
  - You can safely increase the level of parallelism to more than the number of cores in your clusters.  
 - ***Memory Usage of Reduce Tasks***
  -  Spark’s shuffle operations (sortByKey, groupByKey, reduceByKey, join, etc) build a hash table within each task to perform the grouping, which can often be large.  
  - The simplest fix here is to increase the level of parallelism, so that each task’s input set is smaller  
 - ***Broadcasting Large Variables***
   -  in general tasks larger than about 20 KB are probably worth optimizing.  
 - ***Data Locality***  
   - If data and the code that operates on it are together then computation tends to be fast   
   - Typically it is faster to ship serialized code from place to place than a chunk of data because code size is much smaller than data. Spark builds its scheduling around this general principle of data locality.  
   - Spark prefers to schedule all tasks at the best locality level, but this is not always possible.   
   - In situations where there is no unprocessed data on any idle executor, Spark switches to lower locality levels.   
   - There are two options:   
    - a) wait until a busy CPU frees up to start a task on data on the same server, or  
    - b) immediately start a new task in a farther away place that requires moving data there.  
   - What Spark typically does is wait a bit in the hopes that a busy CPU frees up.  
   - Once that timeout expires, it starts moving the data from far away to the free CPU.  
   - You should increase these settings if your tasks are long and see poor locality, but the default usually works well.  
- For most programs, switching to Kryo serialization and persisting data in serialized form will solve most common performance issues

> Job Scheduling  
- http://spark.apache.org/docs/latest/job-scheduling.html#scheduling-within-an-application  
- 

> Spark Security  
- http://spark.apache.org/docs/latest/security.html  

> Hardware Provisioning  
- http://spark.apache.org/docs/latest/hardware-provisioning.html

> 



 

### <a name="b"></a>b. WEB UI / Spark UI  
 > [spark web ui](https://jaceklaskowski.gitbooks.io/mastering-apache-spark/spark-webui.html)
 > https://www.cloudera.com/documentation/enterprise/5-9-x/topics/operation_spark_applications.html

```
JOBS --> STAGES --> TASKS
```
```
JOBS    --> All jobs
        --> individaul jobs
```  

> A job can be in a running, succeeded, failed or unknown state.

- JOBS :  The Jobs tab consists of two pages, i.e. All Jobs and Details for Job pages.  
- STAGES :  Stages tab in web UI shows the current state of all stages of all jobs in a Spark application (i.e. a SparkContext) with two optional pages for the tasks and statistics for a stage (when a stage is selected) and pool details (when the application works in FAIR scheduling mode).  
- STORAGE : When created, StorageTab creates the following pages and attaches them immediately: A. StoragePage B.RDDPage    
- ENVIRONMENT : Shows various details like total tasks, Input, Shuffle read & write, etc  
- EXECUTORS : list all executors used  
- SQL :  SQL tab in web UI shows SQLMetrics per physical operator in a structured query physical plan. By default, it displays all SQL query executions. However, after a query has been selected, the SQL tab displays the details for the structured query execution  


> EXECUTORS tab :   
    - Input - total data processed or read by the application from hadoop or spark storage  
    - Storage Memory - tatal memory used or available 
    
> STAGES tab :    
    ..- All Stages Page:  shows the task details for a stage given its id and attempt id.   
    ..- Stagev Details page / The Fair Scheduler Pool Details page :  shows information about a Schedulable pool and is only available when a Spark application uses the FAIR scheduling mode (which is controlled by spark.scheduler.mode setting).    
 
> ***Summary Metrics***  :
- for Completed Tasks in Stage : The summary metrics table shows the metrics for the tasks in a given stage that have already finished with SUCCESS status and metrics available. The table consists of the following columns: Metric, Min, 25th percentile, Median, 75th percentile, Max.  
- The 1st row is Duration which includes the quantiles based on executorRunTime.  
- The 2nd row is the optional Scheduler Delay which includes the time to ship the task from the scheduler to executors, and the time to send the task result from the executors to the scheduler. It is not enabled by default and you should select Scheduler Delay checkbox under Show Additional Metrics to include it in the summary table.  
- Tip : If Scheduler Delay is large, consider decreasing the size of tasks or decreasing the size of task results.  
- The 3rd row is the optional Task Deserialization Time which includes the quantiles based on executorDeserializeTime task metric. It is not enabled by default and you should select Task Deserialization Time checkbox under Show Additional Metrics to include it in the summary table.    
- The 4th row is GC Time which is the time that an executor spent paused for Java garbage collection while the task was running (using jvmGCTime task metric).    
- The 5th row is the optional Result Serialization Time which is the time spent serializing the task result on a executor before sending it back to the driver (using resultSerializationTime task metric). It is not enabled by default and you should select Result Serialization Time checkbox under Show Additional Metrics to include it in the summary table.   
- The 6th row is the optional Getting Result Time which is the time that the driver spends fetching task results from workers. It is not enabled by default and you should select Getting Result Time checkbox under Show Additional Metrics to include it in the summary table. - Tip : If Getting Result Time is large, consider decreasing the amount of data returned from each task.    
- If Tungsten is enabled (it is by default), the 7th row is the optional Peak Execution Memory which is the sum of the peak sizes of the internal data structures created during shuffles, aggregations and joins (using peakExecutionMemory task metric). For SQL jobs, this only tracks all unsafe operators, broadcast joins, and external sort. It is not enabled by default and you should select Peak Execution Memory checkbox under Show Additional Metrics to include it in the summary table.   
- If the stage has an input, the 8th row is Input Size / Records which is the bytes and records read from Hadoop or from a Spark storage (using inputMetrics.bytesRead and inputMetrics.recordsRead task metrics).   
- If the stage has an output, the 9th row is Output Size / Records which is the bytes and records written to Hadoop or to a Spark storage (using outputMetrics.bytesWritten and outputMetrics.recordsWritten task metrics).   
- If the stage has shuffle read there will be three more rows in the table. The first row is Shuffle Read Blocked Time which is the time that tasks spent blocked waiting for shuffle data to be read from remote machines (using shuffleReadMetrics.fetchWaitTime task metric). The other row is Shuffle Read Size / Records which is the total shuffle bytes and records read (including both data read locally and data read from remote executors using shuffleReadMetrics.totalBytesRead and shuffleReadMetrics.recordsRead task metrics). And the last row is Shuffle Remote Reads which is the total shuffle bytes read from remote executors (which is a subset of the shuffle read bytes; the remaining shuffle data is read locally). It uses shuffleReadMetrics.remoteBytesRead task metric.   
- If the stage has shuffle write, the following row is Shuffle Write Size / Records (using shuffleWriteMetrics.bytesWritten and shuffleWriteMetrics.recordsWritten task metrics).   
- If the stage has bytes spilled, the following two rows are Shuffle spill (memory) (using memoryBytesSpilled task metric) and Shuffle spill (disk) (using diskBytesSpilled task metric).   



### <a name="c"></a>c. RDD + DataFrame + DataSets + SparkSQL  
> http://spark.apache.org/docs/latest/rdd-programming-guide.html  
  Working with Key-Value Pairs  
  
> http://spark.apache.org/docs/latest/sql-programming-guide.html  

### <a name="d"></a>d. Streaming  (50-50 hands on + theory)
> https://github.com/vivek-bombatkar/Spark-with-Python---My-learning-notes-    
> https://spark.apache.org/docs/latest/streaming-programming-guide.html   

### <a name="e"></a>e. SparkMLLib  (theory)
> https://github.com/vivek-bombatkar/DataWorksSummit2018_Spark_ML   
> https://jaceklaskowski.gitbooks.io/mastering-apache-spark/spark-mllib/spark-mllib.html  


### <a name="f"></a>f. GraphLib (theory)
> https://spark.apache.org/docs/latest/graphx-programming-guide.html  
 


## <a name="40"></a>4. Notes from the books.  
[4.1 Learning Spark: Lightning‑Fast Big Data ](#41)


## <a name="41"></a>4.1 Learning Spark: Lightning‑Fast Big Data   

- [Introduction to Data Analysis with Spark](#1)
- [Programming with RDDs](#2)  
- [Working with Key-Value Pairs](#3)  
- [Loading and Saving Your Data](#4)  
- [Advanced Spark Programming](#5)  
- [Running on a Cluster](#6)  


### <a name="1"></a>Introduction to Data Analysis with Spark    
- cluster computing platform   
- Spark application consists of a driver program that launches various parallel operations on a cluster.   
- driver programs typically manage a number of nodes called executors
- ***SparkContext*** represents a connection to a computing cluster.  
 
<img src="https://github.com/vivek-bombatkar/MyLearningNotes/blob/master/spark/pics/componunt_distribution_spark.JPG" />

### <a name="2"></a>Programming with RDDs    
- Resilient Distributed Dataset (RDD)
- an immutable distributed collection of objects
- It split into multiple partitions, which may be computed on different nodes of the cluster
- ***Transformations*** construct a new RDD from a previous one.
- ***Actions***, on the other hand, compute a result based on an RDD, and either return it to the driver program or save it to an external storage system
- lazy evaluation  - Spark only computes them in a lazy fashion
- to reuse an RDD in multiple actions, you can ask Spark to persist it using RDD.persist().
-  three options for passing functions into Spark - lambda. top level function or locally define functions
- reduce / fold

### <a name="3"></a>Working with Key-Value Pairs
- RDDs containing key-value pairs. These RDDs are called Pair RDDs. 
- Transformations one pair rdd : reduceByKey / foldByKey, combineByKey, countByValue, groupByKey, mapValues, flatMapValues, keys, values, sortByKey
- Transformations on two pair rdd : substractByKey, join, rightOuterJoin, leftOuterJoin, cogroup
- Actions : collectAsMap(), lookup()
- Most operator accept a second parameter giving the number of partitions to use when creating the grouped or aggregated RDD
- repartitioning your data is a fairly expensive operation
- Partitioning will not be helpful in all applications — for example, if a given RDD is only scanned once, there is no point in partitioning it in advance. It is only useful when a dataset is reused multiple times in key-oriented operations such as joins. 
- ***partitionBy***
- HashPartitioner

### <a name="4"></a>Loading and Saving Your Data
- Comprassion optison : gzip, lzo, bzip2, zlib, Snappy
-  

### <a name="5"></a>Advanced Spark Programming
- ***accumulators*** to aggregate information.
- One of the most common uses of accumulators is to count events that occur during job execution for debugging purposes. 
- Note that tasks on worker nodes cannot access the accumulator’s value — from the point of view of these tasks, accumulators are write-only variables.
- ***speculative execution*** Spark can preemptivley launch a “speculative” copy of the task on another node, and take its result if that finishes.
- accumulators updated in actions vs in transformations
- broadcast variables to efficiently distribute large values. allow the program to efficiently send a large, read-only value to all the worker nodes for use in one or more Spark operations.
- ***PrePartition operations***: mapPartition, foreachPartition, mapPartitionWithIndex

### <a name="6"></a>Running on a Cluster
- When running in cluster mode, Spark utilizes a master-slave architecture with one central coordinator and many distributed workers. 
- The central coordinator is called the driver. 
- The driver communicates with potentially larger number of distributed workers called executors. 
- The driver runs in its own Java process and each executor is a Java process. 
- A driver and its executors are together termed a Spark application.
- A Spark application is launched on a set of machines using an external service called a cluster manager.
- Driver program main duties : 
    - a. compiling user program into task
    - b. scheduling task on executor
- Executor 
    - a. running the tasks
    - b. in-memory storage for rdd
- Sparks Dirver & Executor VS YARNs Master & Worker
    - For instance Apache YARN runs a master daemon (called the Resource Manager) and several worker daemons called (Node Managers). 
    - Spark will run both drivers and executors on YARN worker nodes.
- spark2-submit options types :
    - The first is the location of the cluster manager along with an amount of resources you’d like to request for your job (as shown above). 
    - The second is information about the runtime dependencies of your application, such as libraries or files you want to be present on all worker machines.
    
 
 
## <a name="42"></a>4.2 High Performance Spark   


### Spark Model of Parallel Computing: RDDs
- driver (or master node) perform operations on data in parallel. 
- Spark represents large datasets as RDDs, immutable distributed collections of objects, 
- which are stored in the executors or (slave nodes). 
- The objects that comprise RDDs are called partitions 
- Partitions may be (but do not need to be) computed on different nodes of a distributed system. 
- Spark can keep an RDD loaded in memory on the executor nodes throughout the life of a Spark application for faster access 
- RDDs are immutable, so transforming an RDD returns a new RDD rather than the existing one.
-  Actions trigger the scheduler, which builds a directed acyclic graph (called the DAG), based on the dependencies between RDD transformations. 
- Then, using this series of steps called the execution plan, the scheduler computes the missing partitions for each stage until it computes the whole RDD.  

### In Memory Storage and Memory Management  
- Spark offers three options for memory management:  
  - in memory deserialized data  - higher performace but consume high memory   
  - in memory as serialized data - slower performance but low disk space  
  - on disk - slower and nothing in memory, can be more fault tolarent for long string transformations  
- The persist() function in the RDD class lets the user control how the RDD is stored. 
- By default, persist() stores an RDD as deserialized objects in memory.  

### five main properties to represent an RDD internally. 
- partitions()  
- iterator(p, parentIters)  
- dependencies()  
- partitioner()  
- preferredLocations(p)  

### Resource Allocation Across Applications  
-  static allocation  
-  dynamic allocation  

### The Anatomy of a Spark Job  
> spark application -> jobs -> stages -> tasks  
- ***jobs*** 
  - highest element of Spark’s execution hierarchy. 
  - Each Spark job corresponds to one action
- ***stages***
  - As mentioned above, a job is defined by calling an action. 
  - The action may include several transformations, which breakdown of jobs into stages.
  - Several transformations with narrow dependencies can be grouped into one stage.
  - It is possible to executed stages in parallel if they are used to compute different RDDs
  - wide transformations needed to compute one RDD have to be computed in sequence
  - one stage can be computed without moving data across the partitions. 
  - Within one stage, the tasks are the units of work done for each partition of the data.
- ***tasks***
  - A stage consists of tasks. 
  - The task is the smallest unit in the execution hierarchy
  - each can represent one local computation. 
  - One task cannot be executed on more than one executor. 
  - However, each executor has a dynamically allocated number of slots for running tasks
  - The number of tasks per stage corresponds to the number of partitions in the output RDD of that stage.
 
 > Spark SQL’s column operators are defined on the column class, so a filter containing the expression 0 >= df.col("friends") will not
compile since Scala will use the >= defined on 0. Instead you would write df.col("friend") <= 0 or convert 0 to a column literal with
lit  

- ***Transformations*** : types
  - filters
  - sql standard functions
  - 'when' - for if then else
  - Specialized DataFrame Transformations for Missing & Noisy Data
  - Beyond Row-by-Row Transformations
  - Aggregates and groupBy - agg API
  - windowing
  - sorting - orderBy
  - Multi DataFrame Transformations
  
- Tungsten  
  - Tungsten is a new Spark SQL component that provides more efficient Spark operations by working directly at the byte level.
  - Tungsten includes specialized in-memory data structures tuned for the type of operations required by Spark
  - improved code generation, and a specialized wire protocol.

- Query Optimizer  
  - Catalyst is the Spark SQL query optimizer, 
  - which is used to take the query plan and transform it into an execution plan that Spark can run. 
  - Much as our transformations on RDDs build up a DAG, Spark SQL builds up a tree representing our query plan, called a logical plan. 
  - Spark is able to apply a number of optimizations on the logical plan 
  - also choose between multiple physical plans for the same logical plan using a cost-based mode.
  
### Joins (SQL & Core) - 79
 
 ## <a name="50"></a>5. pyspark API & spark SQL functions   
 > http://spark.apache.org/docs/2.2.0/api/python/pyspark.sql.html  
 - functions could be passed to API to perform operations  
 - like aggregate functions used with 'agg' API  
 
 ```python
 from pyspark.sql import functions f
 ```
 
 ### lit() 
 Creates a Column of literal value
 ```
 df.withColumn("col1", f.when("col2") == 0, f.lit("Y")).otherwise(f.lit("N")))
 ```  
 ### monotonically_increasing_id() 
 A column that generates monotonically increasing 64-bit integers. monotonically increasing and unique, but not consecutive.
```
df.withColumn("new_id", f.monotonically_increasing_id())
```
### SparkSession.table()
Returns the specified table as a DataFrame.

### expr()
Parses the expression string into the column that it represents
'''
col_condn = f.exppr("if(col is null, 1,0)") 
df.withColumn("col1",col_condn)
'''
### JOIN 
> http://www.learnbymarketing.com/1100/pyspark-joins-by-example/
```
df_res = df_one.join(df_two,df_one.col1 == df_two.col1,"left") 
df_res = df_one.join(other=df_two,on=["col1"],how="left")
df_res = df_one.alias("a").join(df_two.alias("b"),col("a.col1") == col("b.col1"),"left") 
```
### distinct()
>https://stackoverflow.com/questions/30959955/how-does-distinct-function-work-in-spark
- shuffle data accross partition 
```

```
 
### dataFrame.checkpoint
> https://dzone.com/articles/what-are-spark-checkpoints-on-dataframes  
> https://stackoverflow.com/questions/35127720/what-is-the-difference-between-spark-checkpoint-and-persist-to-a-disk  
- Returns a checkpointed version of this dataset. 
- Checkpointing can be used to ***truncate the logical plan of this dataset***, which is especially useful in iterative algorithms where the plan may grow exponentially. 
- It will be saved to files inside the checkpoint directory set with  SparkContext#setCheckpointDir.
- types : Eager Checkpoint & Non-Eager Checkpoint
 - eager – Whether to checkpoint this DataFrame immediately
```
df.checkpoint
```

### pyspark.sql.window
> https://databricks.com/blog/2015/07/15/introducing-window-functions-in-spark-sql.html  
```python
window_condn = window \
               .partitionby(df.col_date) \               
               .rangeBetween(min_val, max_val) \
               .rowsBetween(Window.unboundedPreceding, Window.unboundedFollowing) \
               .OrderBy(df.col_date) 

df_new = df.withColumn('col1',f.sum('col2')).over(window_condn)   
```

### df.pivote
> https://databricks.com/blog/2016/02/09/reshaping-data-with-pivot-in-apache-spark.html  
- Pivots a column of the current DataFrame and perform the specified aggregation. 
- There are two versions of pivot function: one that requires the caller to specify the list of distinct values to pivot on, and one that does not. 
- The latter is more concise but less efficient, because Spark needs to first compute the list of distinct values internally.

### f.explode(col)
Returns a new row for each element in the given array or map.
```
new_df = df.select(f.explode(df.col1))
```

### df.groupBy(*cols)
Groups the DataFrame using the specified columns, so we can run aggregation on them. See GroupedData for all the available aggregate functions.
```python
df.groupBy(df.col1).count().collect()
```

### df.agg(*expr)
Aggregate on the entire DataFrame without groups (shorthand for df.groupBy.agg()).
```
df.groupBy(df.col1).agg(a.max(df.col1))
```

### pyspark.sql.types.ArrayType
```python
from pyspark.sql.functions import udf
@udf(returnType=ArrayType(StringType()))
def func_test_udf(a):
   return []
 
 new_df = df.withColumn("new_col", func_test_udf(df.col1))

An error occurred while calling None.org.apache.spark.sql.execution.python.UserDefinedPythonFunction. Trace:
class org.apache.spark.sql.types.ArrayType]) does not exist
```

### df.filter()
```
df_new = df.filter(col("col1").isNotNull & col("col1") > 100)
```

### f.first(col)
Aggregate function: returns the first value in a group.

### df.distinct()
```python
df.select("abc").distinct()
```



 
