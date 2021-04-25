# pipeline

## 개요
Amazon Linux2 인스턴스를 이용하여 다양한 파이프라인 구성 및 데이터 분석 프로젝트  
```
# 다운받은 키페어의 접근권한 변경  
chmod 400 pipeline.pem

# ssh 연결 
ssh -i "pipeline.pem" ec2-user@{ public_ip }
```

## Java 설치
- install_java.md
- jdk 1.8을 /usr/local 경로에 설치

## Hadoop 설치
- version : 3.2.2
- 