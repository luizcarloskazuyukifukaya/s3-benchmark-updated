# Introduction
This repository is the updated version of what has been available from Wasabi Technologies LLC.
The following are the updates to the original source code:
* 2 files are created as the result of the execution (benchmark-*.log and benchmark-*.csv)
* The log file is named with timestamp (where it was static with the name being benchmark.log)
* The CSV file is with comma separation so it can be used for easier analytics (example, with Excell)
* Added a bash script template with it the options can be specified easily

# Wasabi Original s3-benchmark repository
The repository can be found at https://github.com/wasabi-tech/s3-benchmark. 
For details please refer to this repository as most part of the source code is not modified from the original version.

# Prerequisites
To leverage this tool, the following prerequisites apply:
* Ubuntu Linux shell programming skills
* Editor tool such as vim or any text editor (to modify the bash script template)    
 
# Bash script template
s3-benchmark-all.sh.template is provided so you copy and modify the parameters value based on your environment.

You should copy and change it to be executable with the following commands:
```
ubuntu:~/s3-benchmark-updated$ cp s3-benchmark-all.sh.template s3-benchmark-all.sh
ubuntu:~/s3-benchmark-updated$ chmod +x s3-benchmark-all.sh
```
# Specify the Access Key and Secret Key
The following are the part that at least should be specified before executing the script.
```
ACCESS_KEY=<Access key value here>
SECRET_KEY=<Secret key value here>
```
Once specified you should be able to execute it.

# Bash script execution
s3-benchmark-all.sh should be executable if you follow the instruction above.
Make sure you modified the bash script so the S3 Access Key and the Secret Key are provided.
You should be able to execute the bash script as the following:
```
ubuntu:~/s3-benchmark-updated$ ./s3-benchmark-all.sh
```

The following is an example of the output in the terminal:
```
ubuntu:~/dev/s3/s3-benchmark-updated$ ./s3-benchmark-all.sh
Wasabi benchmark program v2.1
Parameters { url=https://s3.ap-northeast-1.wasabisys.com, bucket=s3-benchmark-bucket-6082, region=ap-northeast-1, duration=60, threads=50, loops=2, size=1M }
Loop 1: PUT time=68.5 secs, objects 301, speed 4.4M B/sec, 4.4 operations/sec., Slowdowns=0
Loop 1: GET time=61.6 secs, objects 3968, speed 64.4M B/sec, 64.4 operations/sec., Slowdowns=0
Loop 1: DELETE time=0.2 secs, 1354.8 deletes/sec., Slowdowns=0
Loop 2: PUT time=66.0 secs, objects 302, speed 4.6M B/sec, 4.6 operations/sec., Slowdowns=0
Loop 2: GET time=61.3 secs, objects 3849, speed 62.8M B/sec, 62.8 operations/sec., Slowdowns=0
Loop 2: DELETE time=0.3 secs, 987.4 deletes/sec., Slowdowns=0
```

# Example log output
The following is an example of the log file:
```
Tue, 23 Jan 2024 16:56:33 GMT: Parameters { url=https://s3.ap-northeast-1.wasabisys.com, bucket=s3-benchmark-bucket-6082, region=ap-northeast-1, duration=60, threads=50, loops=2, size=1M }
Tue, 23 Jan 2024 16:57:43 GMT: Loop 1: PUT time=68.5 secs, objects 301, speed 4.4M B/sec, 4.4 operations/sec., Slowdowns=0
Tue, 23 Jan 2024 16:58:45 GMT: Loop 1: GET time=61.6 secs, objects 3968, speed 64.4M B/sec, 64.4 operations/sec., Slowdowns=0
Tue, 23 Jan 2024 16:58:45 GMT: Loop 1: DELETE time=0.2 secs, 1354.8 deletes/sec., Slowdowns=0
Tue, 23 Jan 2024 16:59:51 GMT: Loop 2: PUT time=66.0 secs, objects 302, speed 4.6M B/sec, 4.6 operations/sec., Slowdowns=0
Tue, 23 Jan 2024 17:00:53 GMT: Loop 2: GET time=61.3 secs, objects 3849, speed 62.8M B/sec, 62.8 operations/sec., Slowdowns=0
Tue, 23 Jan 2024 17:00:53 GMT: Loop 2: DELETE time=0.3 secs, 987.4 deletes/sec., Slowdowns=0
```

The log file name is created based on the region, date and time with the following format:
```
benchmark_<REGION_NAME>_<yyyymmddThhmmss>.log
```

# Example CSV output
The following is an example of the CSV file:
```
DateTime,LoopNumber,Operation,OperationTime(sec),Objects,Speed(B/sec),Operation/sec,Slowdowns,region
"Tue, 23 Jan 2024 16:57:43 GMT", 1,PUT,68.5,301,4606318.8,4.4,0,ap-northeast-1
"Tue, 23 Jan 2024 16:58:45 GMT", 1,GET,61.6,3968,67567377.6,64.4,0,ap-northeast-1
"Tue, 23 Jan 2024 16:58:45 GMT", 1,DELETE,0.2,,,1354.8,0,ap-northeast-1
"Tue, 23 Jan 2024 16:59:51 GMT", 2,PUT,66.0,302,4797176.1,4.6,0,ap-northeast-1
"Tue, 23 Jan 2024 17:00:53 GMT", 2,GET,61.3,3849,65858746.8,62.8,0,ap-northeast-1
"Tue, 23 Jan 2024 17:00:53 GMT", 2,DELETE,0.3,,,987.4,0,ap-northeast-1
```

The CSV file name is created based on the region, date and time with the following format:
```
benchmark_<REGION_NAME>_<yyyymmddThhmmss>.csv
```
The log file and CSV file should be the same except the file extension.

# Note
This version is NOT provided officially from Wasabi Technologies LLC, so if you have an issue, it is recommended to try execute the original version first. If still you have the issue, please contact Wasabi technical support (support@wasabi.com).
