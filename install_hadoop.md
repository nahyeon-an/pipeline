# Hadoop 설치

<br>

*ec2-user로 접속*  

1. 하둡 설치파일 다운로드 및 압축 해제  
```
cd apps
wget https://downloads.apache.org/hadoop/common/hadoop-3.2.2/hadoop-3.2.2.tar.gz
gunzip hadoop-3.2.2.tar.gz
tar -xvf hadoop-3.2.2.tar
```

2. 링크 생성  
```
ln -s hadoop-3.2.2 hadoop
```

3. 환경 변수 설정  
```
sudo vi /etc/profile

### /etc/profile 에서 추가 ###

export HADOOP_HOME=/home/ssac/apps/hadoop

PATH=...:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

############################

source /etc/profile

```

4. hadoop 환경 설정(Single Cluster Mode)  
```
cd $HADOOP_HOME/etc/hadoop

vi hadoop-env.sh

### hadoop-env.sh 에서 추가 ###

export JAVA_HOME=/usr/local/active-java
export HADOOP_PID_DIR=/home/ec2-user/data/hadoop/pids
export HADOOP_LOG_DIR=/home/ec2-user/data/hadoop/logs 

#############################

 vi core-site.xml

 ### core-site.xml 에서 ###



 #########################

 vi hdfs-site.xml

 ### hdfs-site.xml 에서 ###



 #########################

 vi workers

 ### workers 에서 ###
 {인스턴스의 public dns 입력}
 ###################

```

5. hadoop 정보를 저장할 경로 생성  
(위의 설정파일에서 설정한 경로 생성)  
```
cd ~
mkdir -p data/hadoop/dfs/namenode
mkdir -p data/hadoop/dfs/datanode
mkdir -p data/hadoop/pids
mkdir -p data/hadoop/logs
```

6. ssh key 생성  
(하둡에서 호스트에 접근 시 참조할 키를 생성)  
```
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
sudo chmod 755 /home
sudo chmod 700 /home/ec2-user /home/ec2-user/.ssh
sudo chmod 600 /home/ec2-user/.ssh/authorized_keys
```

7. hdfs 실행
```
hdfs namenode -format  # namenode 포맷, 최초에 한번만
start-dfs.sh
jps  # DataNode, SecondaryNameNode, NameNode
```