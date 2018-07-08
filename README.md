# Because its never late to start taking notes and 'public' it...

## This file contains random technical notes, please follow individual folders for specific technology. 



### get HDFS file size 
```
$ hdfs dfs -du -s -h  hdfs://hadoop-cluster/user/hive/warehouse/hive_schema.db/table
655.2 M  1.9 G  hdfs://hadoop-cluster/user/hive/warehouse/hive_schema.db/table

[size]     [disk space consumed]
655.2 M  * 3 (replication factor)  = 1.9 G
-s : aggregate summary of file lengths
-h : human readable instead long number in bytes 
```

### find and delete HIVE tables matching pattern with beeline
```
beeline -u $BEELINE_URL --showHeader=false --outputformat=tsv2 -e "show tables from $HIVE_SCHEMA like $PATTERN ;" | xargs -I '{}' beeline -u $BEELINE_URL --showHeader=false --outputformat=tsv2 -e " drop table $HIVE_SCHEMA.{} ;" 

xargs - reads data from standard input (stdin) and executes the command (supplied to it as argument) one or more times based on the input read. Any blanks and spaces in input are treated as delimiters, while blank lines are ignored. 
```

### hdfs dfs -checksum
https://community.hortonworks.com/questions/19239/hadoop-checksum-calculation-doubts.html

```
hdfs dfs -checksum <hdfs url>
<hdfs url>        MD5-of-0MD5-of-512CRC32C        00000200000000000000000024c3cf9f64d08eaafeb25bb9776f793c

- Datanodes are responsible for verifying the data they receive before storing the data and its checksum
- When clients read data from datanodes, they verify checksums as well, comparing them with the ones stored at the datanodes
- 'get' command : HDFS computes a checksum for each block of each file. The checksums for a file are stored separately in a hidden file. When a file is read from HDFS, the checksums in that hidden file are used to verify the file’s integrity. For the get command, the -crc option will copy that hidden checksum file. The -ignorecrc option will skip the checksum checking when copying
- A separate checksum is created for every dfs.bytes-perchecksum bytes of data. The default is 512 bytes3
- Each datanode keeps a persistent log of checksum verifications, so it knows the last time each of its blocks was verified.
- "MD5-of-0MD5-of-512CRC32C" : http://mail-archives.apache.org/mod_mbox/hadoop-hdfs-user/201508.mbox/%3CCAMm20=5K+f3ArVtoo9qMSesjgd_opdcvnGiDTkd3jpn7SHkysg@mail.gmail.com%3E
```

### installing jupyter on windows

```
# On command prompt
C:\> python -m pip install jupyter

# It creats entry in C:\Python36\Scripts
C:\Python36\Scripts\jupyter.exe

C:\>jupyter notebook
[I 12:36:39.808 NotebookApp] Serving notebooks from local directory: C:\
[I 12:36:39.808 NotebookApp] 0 active kernels
[I 12:36:39.808 NotebookApp] The Jupyter Notebook is running at:
[I 12:36:39.808 NotebookApp] http://localhost:8888/?token=1d3293c485f32b492a93cf6dae1088d51d6d4635dff7630d
[I 12:36:39.808 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 12:36:39.808 NotebookApp]

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=1d3293c485f32b492a93cf6dae1088d51d6d4635dff7630d
[I 12:36:39.976 NotebookApp] Accepting one-time-token-authenticated connection from ::1
```


### Test your Knowledge with Stack Overflow
https://medium.com/dunder-data/how-to-learn-pandas-108905ab4955
You don’t really know a Python library if you cannot answer the majority of questions on it that are asked on Stack Overflow. This statement might be a little too strong, but in general, Stack Overflow provides a great testing ground for your knowledge of a particular library. There are over 50,000 questions tagged as pandas, so you have an endless test bank to build your pandas knowledge.

If you have never answered a question on Stack Overflow, I would recommend looking at older questions that already have answers and attempting to answer them by only using the documentation. After you feel like you can put together high-quality answers, I would suggest making attempts at unanswered questions. Nothing improved my pandas skills more than answering questions on Stack Overflow.


### Alter HIVE table name 
https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-Create/Drop/Alter/UseDatabase
```
ALTER TABLE old_table RENAME TO new_table;
This statement lets you change the name of a table to a different name.
As of version 0.6, a rename on a managed table moves its HDFS location. 
Rename has been changed as of version 2.2.0 (HIVE-14909) so that a managed table's HDFS location is moved only if the table is created without a LOCATION clause and under its database directory.
Hive versions prior to 0.6 just renamed the table in the metastore without moving the HDFS location.

```

### git commonly used commands
```
git init
git pull
git clone <git dir path>
git add .
git status
git commit -m "comments"
git push origin <branch name>

git rm file1.txt
#But if you want to remove the file only from the Git repository and not remove it from the filesystem, use:
git rm --cached ipmvp-nifi-custom.iml
```


### AWS CLI
Install CLI : https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-windows.html#awscli-install-windows-path

Create a profile 
```
C:\Users\vkbomb>aws configure --profile test
AWS Access Key ID []: XXX
AWS Secret Access Key []: YY
Default region name []: eu-central-1
Default output format [None]:
```

List S3 objects
```
C:\Users>aws s3 ls s3://bucket_name/folder1/ --profile test
```

Download data from buckte
```
C:\Users>aws s3 cp s3://bucket_name/folder1/test_file.txt --profile test .
download: s3://bucket_name/folder1/test_file.txt to .\test_file.txt

#to download entire bucket  
C:\Users>aws s3 sync s3://bucket_name/folder1 --profile test .
```

### Python Decorator and Java annotation
http://supercoderz.in/how-python-decorators-are-better-than-java-annotations/
https://stackoverflow.com/questions/15347136/is-a-python-decorator-the-same-as-java-annotation-or-java-with-aspects


### The Gradle Wrapper
https://docs.gradle.org/current/userguide/gradle_wrapper.html

The recommended way to execute any Gradle build is with the help of the Gradle Wrapper (in short just “Wrapper”). The Wrapper is a script that invokes a declared version of Gradle, downloading it beforehand if necessary. As a result, developers can get up and running with a Gradle project quickly without having to follow manual installation processes saving your company time and money.

```
.
├── build.gradle
├── settings.gradle
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
└── gradlew.bat

- build.gradle
mainClassName = 'com.gfk.nifi.Main'
// this tells the build to run the code from class Main
// so when we build the project, it actually call the code .  

```


### remove zero byte files from HDFS

```
#List the zero byte files
hdfs dfs -ls hdfs://<path> | awk '{ if ($5 == 0) print $8 }'

#delete all zero byte files
hdfs dfs -ls hdfs://<path> | awk '{ if ($5 == 0) print $8 }' | xargs hadoop fs -rm

# delete zero byte files from subfolders 
hdfs dfs -lsr hdfs://<path>/\* | awk '{ if ($5 == 0) print $8 }' | xargs hadoop fs -rm

#\* avoides the folder itself to comming in the list
```

### Commands to generate a keytab file, using the Kerberos password

```
$ ktutil
ktutil:  add_entry -password -p pos-ingest@INSIGHTS.SUPERCRUNCH.IO -k 5 -e aes256-cts-hmac-sha1-96
ktutil:  add_entry -password -p pos-ingest@INSIGHTS.SUPERCRUNCH.IO -k 5 -e aes128-cts-hmac-sha1-96
ktutil:  add_entry -password -p pos-ingest@INSIGHTS.SUPERCRUNCH.IO -k 5 -e des3-cbc-sha1
ktutil:  add_entry -password -p pos-ingest@INSIGHTS.SUPERCRUNCH.IO -k 5 -e arcfour-hmac
ktutil:  wkt ./pos-ingest.keytab
ktutil:  quit

```

### HIVE create table if not exists & create or replace view 
- 'create or replace view' dose not supported very well, hence it is wise to drop view before hand.
- and use CREATE VIEW [IF NOT EXISTS]

### What's in the HIVE JDBC URL
> https://streever.atlassian.net/wiki/spaces/HADOOP/pages/9961474/Hive+JDBC+Extended+Connection+URL+Examples
> https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Clients
```
jdbc:hive2://zookeeper_quorum|hs2_host:port
/[db][;principal=<hs2_principal>/<hs2_host>|_HOST@<KDC_REALM>]
[;transportMode=binary|http]
[;httpPath=<http_path>]
[;serviceDiscoveryMode=zookeeper;zooKeeperNamespace=<zk_namespace>]
```
- Adding ;SocketTimeout=0 in URL could solve the problems like below
```
ERROR processing query/stat
ement. Error Code: 0, SQL state: TStatus(statusCode:ERROR_STATUS, infoMessages:[*org.apache.hive.service.cli.HiveSQLException:Invalid S
essionHandle: SessionHandle [xxx]:12:11,
```

### DOCKER
> https://amaysim.engineering/the-3-musketeers-how-make-docker-and-compose-enable-us-to-release-many-times-a-day-e92ca816ef17
> https://serversforhackers.com/s/docker-in-development
> https://djangostars.com/blog/what-is-docker-and-how-to-use-it-with-python/

- ***docker***

- ***docker composer***
> manages Docker containers in a very neat way. 
> It allows multiple Docker commands to be written as a single one, which allows our Makefile to be a lot cleaner and easier to maintain.

- ***make - makefile***
> Make is a cross-platform build tool to test and build software and it is used as an interface between the CI/CD server and the application code.
> A single Makefile per application defines and encapsulates all the steps for testing, building, and deploying that application.
> Having a clean Makefile is key. It helps to understand it quickly and to maintain. Therefore, having some conventions like target vs _target, Pipeline targets, and Pipeline targets really aim to make developers’ life easier.


- ***gettig started with docker***
```
C:\WINDOWS\system32>docker run -i -t --rm ubuntu /bin/bash
root@c61ba2599bbb:/# exit


C:\WINDOWS\system32>docker ps -a
CONTAINER ID        IMAGE                                             COMMAND                  CREATED             STATUS                    PORTS               NAMES
5b9fe6cd227e        ubuntu                                            "/bin/echo 'Hello wo…"   10 hours ago        Exited (0) 10 hours ago     

```

- ***dockerfile***
> FROM — set base image
> RUN — execute command in container
> ENV — set environment variable
> WORKDIR — set working directory
> VOLUME — create mount-point for a volume
> CMD — set executable for container


