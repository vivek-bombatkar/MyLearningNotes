
# Spark hands on practice and notes   
> Follow me on,  [LinkedIn](https://www.linkedin.com/in/vivek-bombatkar/), [Github](https://github.com/vivek-bombatkar)  

Please checkout my Spark related notes from below repos,  

> https://github.com/vivek-bombatkar/Databricks-Apache-Spark-2X-Certified-Developer  

> https://github.com/vivek-bombatkar/Spark-with-Python---My-learning-notes-  

> https://github.com/vivek-bombatkar/DataWorksSummit2018_Spark  


## Spark - HDFS partitoning 
| No partiton defined | sdf.write.partitionBy("col_1") | sdf.write.repartiton(10) |  
| -- | -- | -- |  
| spark default partition will get apply, i.e. 128 MB | files with splits based on partition column, hence default 128 MB will not apply. |  partition will be based on number given  |  


## Spark : HDFS from PySpark  
> https://diogoalexandrefranco.github.io/interacting-with-hdfs-from-pyspark/   


## unit testing with pyspark
> https://www.knowru.com/blog/how-unittest-pyspark-applications/  
> https://engblog.nextdoor.com/unit-testing-apache-spark-with-py-test-3b8970dc013b  
> https://blog.cambridgespark.com/unit-testing-with-pyspark-fb31671b1ad8  
