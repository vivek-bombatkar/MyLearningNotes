
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
- 1. In the code itself while creating spark context  
```spark.sparkContext.setLogLevel("ERROR)"```

- 2. While spark-submit   
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
