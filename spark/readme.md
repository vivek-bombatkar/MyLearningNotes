
## Apache Spark

> https://github.com/vivek-bombatkar/Spark-with-Python---My-learning-notes-

> https://www.slideshare.net/cloudera/top-5-mistakes-to-avoid-when-writing-apache-spark-applications



### Databricks - Apache Spark™ Certified Developer  

> https://pages.databricks.com/rs/094-YMS-629/images/7-steps-for-a-developer-to-learn-apache-spark.pdf
> [Table of Contents](http://shop.oreilly.com/product/0636920028512.do)  


#### a. Concept  
> http://spark.apache.org/  
> https://databricks.gitbooks.io/databricks-spark-reference-applications/content/index.html  
> https://thachtranerc.wordpress.com/2017/07/10/databricks-developer-certifcation-for-apache-spark-finally-i-made-it/  
> https://www.youtube.com/watch?v=7ooZ4S7Ay6Y  
> https://www.youtube.com/watch?v=kkOG_aJ9KjQ  
> https://www.youtube.com/watch?v=dmL0N3qfSc8  
> https://www.youtube.com/watch?v=49Hr5xZyTEA  
> [Overview](https://www.youtube.com/watch?v=tFRPeU5HemU)


#### b. WEB UI / Spark UI  
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

| -- | -- | -- | -- | -- | -- |  
| JOBS | STAGES | STORAGE | ENVIRONMENT | EXECUTORS | SQL |
| The Jobs tab consists of two pages, i.e. All Jobs and Details for Job pages. | Stages tab in web UI shows the current state of all stages of all jobs in a Spark application (i.e. a SparkContext) with two optional pages for the tasks and statistics for a stage (when a stage is selected) and pool details (when the application works in FAIR scheduling mode). | When created, StorageTab creates the following pages and attaches them immediately: A. StoragePage B.RDDPage |  | Shows various details like total tasks, Input, Shuffle read & write, etc   | SQL tab in web UI shows SQLMetrics per physical operator in a structured query physical plan. By default, it displays all SQL query executions. However, after a query has been selected, the SQL tab displays the details for the structured query execution |



> EXECUTORS tab :   
    - Input - total data processed or read by the application from hadoop or spark storage  
    - Storage Memory - tatal memory used or available 
    
> STAGES tab :    
    ..- All Stages Page:  shows the task details for a stage given its id and attempt id.   
    ..- Stagev Details page / The Fair Scheduler Pool Details page :  shows information about a Schedulable pool and is only available when a Spark application uses the FAIR scheduling mode (which is controlled by spark.scheduler.mode setting).   
 
| -- |  
| ***Summary Metrics*** |  
| for Completed Tasks in Stage : The summary metrics table shows the metrics for the tasks in a given stage that have already finished with SUCCESS status and metrics available. The table consists of the following columns: Metric, Min, 25th percentile, Median, 75th percentile, Max.  |  
| The 1st row is Duration which includes the quantiles based on executorRunTime.  |  
| The 2nd row is the optional Scheduler Delay which includes the time to ship the task from the scheduler to executors, and the time to send the task result from the executors to the scheduler. It is not enabled by default and you should select Scheduler Delay checkbox under Show Additional Metrics to include it in the summary table.  |  
| Tip : If Scheduler Delay is large, consider decreasing the size of tasks or decreasing the size of task results. |  
| The 3rd row is the optional Task Deserialization Time which includes the quantiles based on executorDeserializeTime task metric. It is not enabled by default and you should select Task Deserialization Time checkbox under Show Additional Metrics to include it in the summary table.  |  
| The 4th row is GC Time which is the time that an executor spent paused for Java garbage collection while the task was running (using jvmGCTime task metric). |   
| The 5th row is the optional Result Serialization Time which is the time spent serializing the task result on a executor before sending it back to the driver (using resultSerializationTime task metric). It is not enabled by default and you should select Result Serialization Time checkbox under Show Additional Metrics to include it in the summary table.  |  
| The 6th row is the optional Getting Result Time which is the time that the driver spends fetching task results from workers. It is not enabled by default and you should select Getting Result Time checkbox under Show Additional Metrics to include it in the summary table. |    
| Tip : If Getting Result Time is large, consider decreasing the amount of data returned from each task.   |  
| If Tungsten is enabled (it is by default), the 7th row is the optional Peak Execution Memory which is the sum of the peak sizes of the internal data structures created during shuffles, aggregations and joins (using peakExecutionMemory task metric). For SQL jobs, this only tracks all unsafe operators, broadcast joins, and external sort. It is not enabled by default and you should select Peak Execution Memory checkbox under Show Additional Metrics to include it in the summary table. |  
| If the stage has an input, the 8th row is Input Size / Records which is the bytes and records read from Hadoop or from a Spark storage (using inputMetrics.bytesRead and inputMetrics.recordsRead task metrics). |  
| If the stage has an output, the 9th row is Output Size / Records which is the bytes and records written to Hadoop or to a Spark storage (using outputMetrics.bytesWritten and outputMetrics.recordsWritten task metrics). |  
| If the stage has shuffle read there will be three more rows in the table. The first row is Shuffle Read Blocked Time which is the time that tasks spent blocked waiting for shuffle data to be read from remote machines (using shuffleReadMetrics.fetchWaitTime task metric). The other row is Shuffle Read Size / Records which is the total shuffle bytes and records read (including both data read locally and data read from remote executors using shuffleReadMetrics.totalBytesRead and shuffleReadMetrics.recordsRead task metrics). And the last row is Shuffle Remote Reads which is the total shuffle bytes read from remote executors (which is a subset of the shuffle read bytes; the remaining shuffle data is read locally). It uses shuffleReadMetrics.remoteBytesRead task metric. |  
| If the stage has shuffle write, the following row is Shuffle Write Size / Records (using shuffleWriteMetrics.bytesWritten and shuffleWriteMetrics.recordsWritten task metrics). |  
| If the stage has bytes spilled, the following two rows are Shuffle spill (memory) (using memoryBytesSpilled task metric) and Shuffle spill (disk) (using diskBytesSpilled task metric). |  




#### c. RDD + DataFrame + DataSets + SparkSQL  
> http://spark.apache.org/docs/latest/rdd-programming-guide.html  
  Working with Key-Value Pairs  
  
> http://spark.apache.org/docs/latest/sql-programming-guide.html  

#### d. Streaming  
> https://spark.apache.org/docs/latest/streaming-programming-guide.html

#### e. SparkMLLib  
> https://jaceklaskowski.gitbooks.io/mastering-apache-spark/spark-mllib/spark-mllib.html


#### f. GraphLib


***Learning Spark***  notes from the book reading.  
[Introduction to Data Analysis with Spark](#1)
- Programming with RDDs  
- Working with Key-Value Pairs  
- Loading and Saving Your Data  
- Advanced Spark Programming  
- Running on a Cluster  


## <a name="1"></a>Introduction to Data Analysis with Spark    
- a cluster computing platform   
- Spark application consists of a driver program that launches various parallel operations on a cluster.   
- driver programs typically manage a number of nodes called executors
- ***SparkContext*** represents a connection to a computing cluster.  
 
<img src="https://github.com/vivek-bombatkar/MyLearningNotes/blob/master/spark/pics/componunt_distribution_spark.JPG" />

- 