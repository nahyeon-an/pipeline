# Demo1  

<br>

## Preprocess Pipeline  
- 수집한 데이터를 전처리하여 mongo DB에 넣는 파이프라인  

<br>

#### 개요
- 합격 자소서를 수집하여 spooldir 에 저장  
- spooldir 에서 hdfs 로 저장하는 flume agent  
- hdfs 의 데이터를 읽어 전처리하는 spark app  
- hdfs 에 데이터가 존재하면 spark app 을 실행시키는 데몬 프로그램  

<br>

## Pipeline architecture
![architecture](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FscNJY%2Fbtq3TsAzox6%2FIekRoQtmVPKxFlonHoonk1%2Fimg.png) 

<br>

### Crawling file
![after crawling](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FQH06n%2Fbtq3WnECMJv%2FH949LaHxrneYbxOs118slk%2Fimg.png)

<br>

### Flume file  
- spool-to-hdfs.conf  
- source : spooldir  
- channel : file  
- sink : hdfs  

<br>

### Executor file
- executor.py
- Check the number of hdfs files and execute spark-submit command or not

<br>

### Spark file
- preprocess.py
- gb_preprocess.py, rating_preprocess.py : extract input data and label for modeling

![spark preprocess app](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbgYhdh%2Fbtq3U7veNWH%2FKiG5jsAqAkxMLrmALbSZ01%2Fimg.png)