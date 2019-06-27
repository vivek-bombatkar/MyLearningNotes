
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

- Convert dataframe to pandas  
```python
from pandas.util.testing import assert_frame_equal
assert_frame_equal(csvdata, csvdata_old)

```

> ***sparktestingbase*** : https://github.com/holdenk/spark-testing-base  
```python
# 1. df_comparison.py
sparktestingbase
from sparktestingbase import sqltestcase
from pyspark.sql import SparkSession

class SparkBaseTestCase(sqltestcase.SQLTestCase):

    def setUp(self):
        super(SparkBaseTestCase, self).setUp()
        self.session = SparkSession.builder.getOrCreate()

    def read_data(self, file_name, schema):
        temp_data = self.session.read.csv('file:///{0}/tests/{1}'.format(os.getcwd(), file_name), sep=',',
                                          header='true', schema=schema)
        # we need this additional conversion in case of existence of not nullable columns in the expected schema
        # after reading from csv all columns of the schema are nullable, so comparison of dataframes fails
        return self.session.createDataFrame(temp_data.rdd.collect(), schema)

# 2. test_module_1.py

from tests import dataframes_comparison as dfcomp
from pyspark.sql.functions import *


class TestDataClean(dfcomp.SparkBaseTestCase):

    def test_module_1(self):
        schema_test = StructType([
            StructField("field_1", StringType()),
            StructField("field_2", StringType())
        ])
        schema_expected = StructType([
            StructField("field_1", StringType()),
            StructField("field_2", StringType())
            #StructField("field_1_not_applicable", BooleanType()),
            #StructField("field_2_not_applicable", BooleanType())
        ])
        expected_data = self.read_data('module_1_data/module_1expected_data.csv', schema_expected)
        test_data = self.read_data('module_1_data/module_1_test_data.csv', schema_test)
        super(TestDataClean, self).assertDataFrameEqual(module_1.function_1(test_data), expected_data)

```

## pytest-spark
> https://pypi.org/project/pytest-spark/   
> https://stackoverflow.com/questions/40975360/testing-spark-with-pytest-cannot-run-spark-in-local-mode  
> https://pypi.org/project/pytest-runner/  


## orderBy

```python
sdf.orderBy('col1', ascending = False)
```

## checkpoint()
> https://jaceklaskowski.gitbooks.io/mastering-apache-spark/spark-rdd-checkpointing.html  
- Useful for overwriting the same HIVE table which used to create DF  
```python
sc = sparkSession.sparkContext
sc.setCheckpointDir('/user/tmp/checkpoint')

sdf = sparkSession.sql("select *, "1" as new_col  from hive_table_1").checkpoint()

sdf.write.mode("overwrite").saveAsTable("hive_table_1")

```
  - withput checkpoint exception will thrown : org.apache.spark.sql.AnalysisException: Cannot overwrite table prod_gse_microwave.gsemicrowave_gb_1w_31102018t153548z that is also being read from;   


## Configuration 
> https://spark.apache.org/docs/1.5.0/configuration.html#dynamically-loading-spark-properties

- Properties set directly on the SparkConf take highest precedence, then flags passed to spark-submit or spark-shell, then options in the spark-defaults.conf file.  
1. Properties set on the SparkConf (in program).  
2. Flags passed to spark-submit or spark-shell.  
3. Options set in the spark-defaults.conf file.  


## Log handling in Spark - 2 options 
1. In the code itself while creating spark context  
```spark.sparkContext.setLogLevel("ERROR)"```

2. While spark-submit   
``` --driver-java-options "-Dlog4j.configuration=<FULL PATH>/spark_custom-log4j.properties" ```

- spark_custom-log4j.properties file :   
```
log4j.rootLogger=${root.logger}
root.logger=WARN,console
log4j.appender.console=org.apache.log4j.ConsoleAppender
log4j.appender.console.target=System.err
log4j.appender.console.layout=org.apache.log4j.PatternLayout
log4j.appender.console.layout.ConversionPattern=%d{yy/MM/dd HH:mm:ss} %p %c{2}: %m%n
shell.log.level=WARN
log4j.logger.org.eclipse.jetty=WARN
log4j.logger.org.spark-project.jetty=WARN
log4j.logger.org.spark-project.jetty.util.component.AbstractLifeCycle=ERROR
log4j.logger.org.apache.spark.repl.SparkIMain$exprTyper=ERROR
log4j.logger.org.apache.spark.repl.SparkILoop$SparkILoopInterpreter=ERROR
log4j.logger.org.apache.parquet=ERROR
log4j.logger.parquet=ERROR
log4j.logger.org.apache.hadoop.hive.metastore.RetryingHMSHandler=FATAL
log4j.logger.org.apache.hadoop.hive.ql.exec.FunctionRegistry=ERROR
log4j.logger.org.apache.spark.repl.Main=${shell.log.level}
log4j.logger.org.apache.spark.api.python.PythonGatewayServer=${shell.log.level}
```

## read files from AWS S3

```
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession, HiveContext

spark = SparkSession.builder \
.master("local[*]") \
.appName("load_aws_s3") \
.enableHiveSupport() \
.config("spark.submit.deployMode","client") \
.config("spark.hadoop.fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem") \
.config("spark.hadoop.fs.s3a.aws.credentials.provider","org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider") \
.config("spark.hadoop.com.amazonaws.services.s3.enableV4","true") \
.config("spark.hadoop.fs.s3a.endpoint","https://s3.eu-central-1.amazonaws.com") \
.config("spark.hadoop.hadoop.security.credential.provider.path","jceks://hdfs/user/myuser/pwd.jceks") \
.config("spark.jars","hdfs://myClusterName/user/myuser/spark-avro_2.11-4.0.0.jar") \
.getOrCreate()

sdf = spark.read.csv("<S3 BUCKET ADDRESS>/*csv")

sdf = spark.read.format("com.databricks.spark.avro").load(""<S3 BUCKET ADDRESS>/*.avro")
```

``` .config("spark.hadoop.hadoop.security.credential.provider.path","jceks://hdfs/user/myuser/pwd.jceks") ```
- .jceks is the strong encrypted pwd 

``` .config("spark.jars","hdfs://hadoop-supercrunch-mvp/user/myuser/spark-avro_2.11-4.0.0.jar") ```  
- Need this to read avro files in pyspark 

## renaming dataframe columnames

```python
df = spark.createDataFrame([(100, 15), (200, 10)], 
                                  ["201821_sum(abc)", "201822_mean(abc)"])
df.show()

def format_string(myString):
    return myString[:6]

df = data.withColumnRenamed(data.columns[0], format_string(data.columns[0]))\
                .withColumnRenamed(data.columns[1],format_string(data.columns[1]))

df_new.show()

+---------------+----------------+
|201821_sum(abc)|201822_mean(abc)|
+---------------+----------------+
|            100|              15|
|            200|              10|
+---------------+----------------+

+----+----+
|col1|col2|
+----+----+
| 100|  15|
| 200|  10|
+----+----+
```

## spark job conf : spark.app.name VS name

```
spark-submit --name "app_test_1" --conf "spark.app.name=app_test_2"  Untitled1.py

spark = SparkSession.builder.master("yarn").appName("app_test_2")...

#.appName() = spark.app.name

```

- name : seen in Spark History server UI list  
- spark.app.name : seen in Environment tab along with all other configs. 

## Pickle object to Hadoop , RDD 
> http://spark.apache.org/docs/latest/api/python/pyspark.html?highlight=pickle  
`
RDD.saveAsPickleFile 
sparkContext.pickleFile
`

```
from time import gmtime, strftime

TIMESTAMP = strftime("%d%m%Yt%H%M%Sz", gmtime())
DS_HDFS_DIR = '/user/hive/warehouse/abc'

spark = spark_session.get_spark_session()
sdf = spark.createDataFrame(pdf)

PICKLE_OBJ_LOCATION = "{}/test_pickle_object_{}".format(DS_HDFS_DIR,TIMESTAMP)
sdf.rdd.saveAsPickleFile(PICKLE_OBJ_LOCATION)
```
```
rdd_pickle =spark.sparkContext.pickleFile(PICKLE_OBJ_LOCATION)
sdf = rdd_pickle.toDF()

```

## Various ways to handle bad records with PySpark  
> https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/4222224209897404/1931650819888846/1920808090278788/latest.html

```python
#Reference:
#https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/DataFrameReader.html
#https://docs.databricks.com/spark/latest/spark-sql/handling-bad-records.html

from pyspark.sql import functions as F
from pyspark.sql.types import IntegerType, StringType, StructType

dbutils.fs.rm("/tmp/dataframe_sample.csv", True)
dbutils.fs.put("/tmp/dataframe_sample.csv", 
"""
1,CA-SF
2,CA-SD
three,NY-NY
4,NY-NY
five,CA-SD
""", True)

schema_test = StructType([
    StructField("id", IntegerType()),
    StructField("location", StringType())
])

# 1. Do not care for bad records
df_RAW = spark.read.schema(schema_test).csv("/tmp/dataframe_sample.csv")

# 2. Ignnore bad records from result
df_DROPMALFORMED = spark.read.schema(schema_test).option("mode","DROPMALFORMED").csv("/tmp/dataframe_sample.csv")

# 3. Ignore and collect bad records in separate location 
df_COLLECT_BAD_RECORD = spark.read.schema(schema_test).option("mode","DROPMALFORMED").option("badRecordPath","/tmp").csv("/tmp/dataframe_sample.csv")


df_RAW.show()
df_DROPMALFORMED.show()
df_COLLECT_BAD_RECORD.show()
```
```
Wrote 48 bytes.
+----+--------+
|  id|location|
+----+--------+
|   1|   CA-SF|
|   2|   CA-SD|
|null|    null|
|   4|   NY-NY|
|null|    null|
+----+--------+

+---+--------+
| id|location|
+---+--------+
|  1|   CA-SF|
|  2|   CA-SD|
|  4|   NY-NY|
+---+--------+
```

### Above solution (with badRecordPath) will not work if you are not using Databricks distribution of Spark !
Hence alternative approach will be below, 

```python
from pyspark.sql import functions as F
from pyspark.sql.types import IntegerType, StringType, StructType, StructField
from pyspark.sql.functions import col

schema_test = StructType([
    StructField("id", IntegerType()),
    StructField("location", StringType()),
    StructField("badRecords", StringType())
])


df_raw = spark.read.schema(schema_test)\
                .csv("dataframe_sample.csv",columnNameOfCorruptRecord='badRecords').cache()

df_badRecords = df_raw.filter(col("badRecords").isNotNull()).select("badRecords")
df_goodRecords = df_raw.filter(col("badRecords").isNull()).select("id","location")

df_badRecords.show()
df_goodRecords.show()
```

```
+-----------+
| badRecords|
+-----------+
|three,NY-NY|
| five,CA-SD|
+-----------+

+---+--------+
| id|location|
+---+--------+
|  1|   CA-SF|
|  2|   CA-SD|
|  4|   NY-NY|
+---+--------+
```

- Note `.cache()` is IMP because: "Since Spark 2.3, the queries from raw JSON/CSV files are disallowed when the referenced columns only include the internal corrupt record column..."   


## Spark SQL Built in functions  
> https://spark.apache.org/docs/latest/api/sql/

Could use them over Dataframe as well,
```python
from pyspark.sql.functions import expr
condition1 = expr('<SQL Built in function>')
```

## spark.task.maxFailures  
- Number of failures of any particular task before giving up on the job. The total number of failures spread across different tasks will not cause the job to fail; a particular task has to fail this number of attempts. Should be greater than or equal to 1 
- Only works for yarn-cluster mode as in client mode failure once is failure    
``` 
spark-submit --conf spark.yarn.maxAppAttempts=1 ...
```   

## .config("spark.sql.crossJoin.enabled", "true")   
> http://blog.madhukaraphatak.com/migrating-to-spark-two-part-4/  


## pySpark DF vs Pandas DF  
> https://www.kdnuggets.com/2016/01/python-data-science-pandas-spark-dataframe-differences.html  

# From Pandas to Spark

In this notebook we try to find patterns how common Pandas operations can be expressed in Spark. Since you should always avoid of switching back and forth between Spark and Pandas, you always should try to stay within a single framework. Actually the flexibility of Pandas is slightly bigger than that of Spark, but except for some specific exceptions you can do almost everything in Spark what you can do with Pandas, although the syntax and general approacj might differ.

## Fundamental Differences

Due to its inner design, Spark has some fundamental differences to Pandas. Specifically:

### Distributed processing
The huge selling point of Apache Spark is that it uses a distributed execution model running on multiple computers in a cluster, whereas Pandas is limited to a single Python process. While in Pandas your whole data set has to fit into memory, Spark can process data sets which are much bigger than the total amount of RAM of the whole compute cluster.

This non-functional high level difference has lead to a specific design of the implementation of Spark, which in turn has some very important implications when working with Spark. Some of the implications are formulated in the next items.

### Lazy evaluation
Spark does not execute any transformation when you specify it, but it chains together and optimizes all transformations whenever an action is started, for example to store or view the result of some transofrmations. This design is a very conscious decision of the Spark people (although an "eager" mode is planned for PySpark), which allows better optimizations since the execution of all transformations is delayed until the whole picture is clear to Spark. This approach allows rearranging transformations and pruning of columns thus greatly improving execution speed.

In general in Pandas you always work directly with the data, while in Spark you always transform the execution plan that will create some data for you.

### Immutable DataFrames
The whole core of Spark is developed in Scala, a object-oriented functional programming language. Again this was a very conscious design design of the founders of Spark. Functional programming in general prefers immutable objects over mutable ones. This is also true for the Spark API and helps to keep the Spark code simpler and more efficient. On the other hand, this also means that you cannot modify a data frame in place like you might be used to by Pandas. Every Spark transformation returns a new data frame (with some special exceptions, where some meta information is changed).

### No index
Pandas data frames always have an index (even if that is only the natural numbers), but Spark doesn't even have the concept of an index. Instead of an index, you might think about a primary key like you might know from relational databases.

### No single record access
By using the index, Pandas allows very efficient access to individual rows. This is completely impossible with Spark, since in Spark you primarily work with execution plans *representing* the data, but not with the data itself.


## 
