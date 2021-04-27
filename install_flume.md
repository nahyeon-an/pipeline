# Flume 설치

<br>

1. 설치파일 다운로드 및 압축 해제
```
wget https://downloads.apache.org/flume/1.9.0/apache-flume-1.9.0-bin.tar.gz
gunzip apache-flume-1.9.0-bin.tar.gz
tar xvf apache-flume-1.9.0-bin.tar
```

2. 링크 생성  
```
ln -s apache-flume-1.9.0-bin flume
```

3. 환경 변수 설정  
```
sudo vi /etc/profile

### /etc/profile 에서 추가 ###

export FLUME_HOME=/home/ec2-user/apps/flume

PATH=...:$FLUME_HOME/bin

############################

source /etc/profile
```

4. flume 환경 설정  
(자바 힙 메모리 설정)  
```
cd $FLUME_HOME/conf

cp flume-env.sh.template flume-env.sh

vi flume-env.sh

### flume-env.sh 에서 추가/주석해제 ###

export JAVA_OPTS="-Xms100m -Xmx2000m -Dcom.sun.management.jmxremote"

##################################

```