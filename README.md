# Introduction
This repository is the updated version of what has been available from Wasabi Technologies LLC.
The following are the updates to the original source code:
* The log file is named with timestamp (where it was static with name benchmark.log)
* The log file is with output with comma (CSV format) so it can be used for easier analytics with Excell
* Added a bash script template where the options can be specified easly

# Wasabi Original s3-benchmark repository
The repository can be found at https://github.com/wasabi-tech/s3-benchmark. 
For details please refer to this repository as most of the source code is not modified from the original version.

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

# Example Benchmark
The following is an example of the log created:
```
ubuntu:~/s3-benchmark-updated$ ./s3-benchmark-all.sh
Wasabi benchmark program v2.1
Parameters, url=https://s3.ap-northeast-1.wasabisys.com, bucket=s3-benchmark-bucket-5619, region=ap-northeast-1, duration=60, threads=50, loops=2, size=1M
Loop 1,PUT time,66.0,secs,objects,301,speed,4.6M,B/sec,4.6,operations/sec.,Slowdowns,0
Loop 1,GET time,61.4,secs,objects,3899,speed,63.5M,B/sec,63.5,operations/sec.,Slowdowns,0
Loop 1,DELETE time,0.3,secs,,,,,,1199.2,deletes/sec.,Slowdowns,0
Loop 2,PUT time,66.0,secs,objects,302,speed,4.6M,B/sec,4.6,operations/sec.,Slowdowns,0
Loop 2,GET time,61.2,secs,objects,3696,speed,60.4M,B/sec,60.4,operations/sec.,Slowdowns,0
Loop 2,DELETE time,0.2,secs,,,,,,1245.9,deletes/sec.,Slowdowns,0 
```
The log file name is created based on the region, date and time with the following format:
s3-benchmark_<REGION_NAME>_<TIME STAMP:yyyymmddThhmmss>.log

# Note
This version is NOT provided officially from Wasabi Technologies LLC, so if you have issue, it is recommended to try execute the original version first. If still you have the issue, please contact Wasabi technical support (support@wasabi.com).
