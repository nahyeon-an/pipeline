# Demo1  

<br>

#### 개요
- 합격 자소서를 수집하여 spooldir 에 저장  
- spooldir 에서 hdfs 로 저장하는 flume agent  
- hdfs 의 데이터를 읽어 전처리하는 spark app  
- hdfs 에 데이터가 존재하면 spark app 을 실행시키는 데몬 프로그램  

## Pipeline architecture
- 수집 프로그램 > flume > hdfs > spark  
- spooldir 경로 : /home/ec2-user/spooldir  

## EC2 에 chrome, chromedriver 설치  

[참조 블로그](https://dvpzeekke.tistory.com/1)
