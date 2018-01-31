# Because its never late to start taking notes and 'public' it...

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
