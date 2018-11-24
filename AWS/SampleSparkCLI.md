
```
aws emr create-cluster 
--name "Add Spark Step Cluster" 
--release-label emr-5.19.0 
--applications Name=Spark \
--ec2-attributes KeyName=myKey 
--instance-type m4.large 
--instance-count 3 \
--steps Type=Spark
,Name="Spark Program" 
,ActionOnFailure=CONTINUE ,Args=[--class,org.apache.spark.examples.SparkPi,/usr/lib/spark/lib/spark-examples.jar,10] 
--use-default-roles

aws emr create-cluster --name "Add Spark Step Cluster" --release-label emr-5.19.0 \
--applications Name=Spark --ec2-attributes KeyName=myKey --instance-type m4.large --instance-count 3 \
--steps Type=CUSTOM_JAR
,Name="Spark Program"
,Jar="command-runner.jar"
,ActionOnFailure=CONTINUE
,Args=[spark-example,SparkPi,10] 
--use-default-roles

aws emr add-steps --cluster-id j-2AXXXXXXGAPLF 
--steps Type=Spark
,Name="Spark Program"
,ActionOnFailure=CONTINUE
,Args=[--class,org.apache.spark.examples.SparkPi,/usr/lib/spark/lib/spark-examples.jar,10]

aws emr create-cluster \
     --name “Cluster” \
     --release-label emr-5.9.0 \
     --instance-type m4.large — instance-count 3 \
     --applications Name=Spark \
     --steps Type=Spark,Name=”Spark Program”,ActionOnFailure=CONTINUE,Args=[ — class,com.jeanr84.sparkjob.SparkJob,s3://my-second-emr-bucket/tutorialEMR/spark-job-0.0.1-SNAPSHOT.jar,s3://my-second-emr-bucket/tutorialEMR/input.txt,s3://my-second-emr-bucket/tutorialEMR/output] \
     --use-default-roles \
     --ec2-attributes SubnetId=subnet-e7ba9d9c \
     --auto-terminate

```
