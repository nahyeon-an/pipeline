# Spark 설치

1. 설치파일 다운로드 및 압축 해제  
```
wget https://downloads.apache.org/spark/spark-2.4.7/spark-2.4.7-bin-hadoop2.7.tgz
gunzip spark-2.4.7-bin-hadoop2.7.tgz
tar xvf spark-2.4.7-bin-hadoop2.7.tar
```

2. 링크 생성  
```
ln -s spark-2.4.7-bin-hadoop2.7 spark
```

3. 환경 변수 설정  
```
sudo vi /etc/profile

### /etc/profile 에서 추가 ###

export SPARK_HOME=/home/ec2-user/apps/spark

PATH=...:$SPARK_HOME/bin:$SPARK_HOME/sbin

############################

source /etc/profile
```

4. spark 환경 설정  
```
cd $SPARK_HOME/conf

cp spark-env.sh.template spark-env.sh

vi spark-env.sh

### spark-env.sh 에서 맨 아래에 추가 ###

# java 경로
export JAVA_HOME=/usr/local/active-java
# hadoop 설정 경로 
export HADOOP_CONF_DIR=/home/ec2-user/apps/hadoop/etc/hadoop
# yarn 설정 경로
export YARN_CONF_DIR=/home/ec2-user/apps/hadoop/etc/hadoop
# pyspark 사용시 python 환경 경로  
export PYSPARK_PYTHON=/home/ec2-user/apps/miniconda3/envs/pyspark/bin/python
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/ec2-user/apps/hadoop/lib/native

####################################
```

5. master, worker 실행 및 확인  
- 인스턴스의 8080 포트를 열어준 후  
- http://{public ip}:8080 에서 spark web ui 확인 가능  
```
start-master.sh
start-worker.sh
jps  # Master, Worker 프로세스 확인
```

<br>

### Miniconda 설치

<br>

1. 설치파일 다운로드 및 설치
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod 755 Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh

### 설치 진행 중 ###
설치 경로
#################

# 미니콘다 설치 변경 사항 적용
source .bashrc

cd ~

# 가상 환경 확인
conda info --envs

# spark-env.sh 와 이름 일치하도록 설정/생성
conda create --name pyspark python=3.8
```

2. (선택) jupyter notebook/lab 설치  
- 외부에서 호스트 인스턴스의 주피터 실행 가능하도록 설정 
```
conda activate pyspark

pip install jupyter jupyterlab

# jupyter 설정 파일 생성
jupyter notebook --generate-config

vi .jupyter/jupyter_notebook_config.py

### jupyter_notebook_config.py 에서 해당 부분 주석 해제하고 값 변경 ###

# 외부의 접속 허용 
c.NotebookApp.ip = '0.0.0.0'  
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8180

##############################################################

# password 설정
jupyter notebook password
jupyter lab password

# jupyter notebook 서버 실행
jupyter lab --notebook-dir={작업 경로}
```
- http://{public ip}:8180 으로 원격 접속 확인  

3. pyspark 연결 설정  
- pyspark shell 실행 시 jupyter lab으로 연결 설정  
- spark-submit 으로 spark app 제출 시 jupyter lab 연결 설정을 해제해줘야 함  
```
sudo vi /etc/profile

### /etc/profile 에서 추가 ###

export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='lab --notebook-dir=/home/ec2-user/nb-workspace'

############################

source /etc/profile
```
- pyspark shell을 spark standalone 모드로 실행시켜 확인  
- hdfs, spark master, spark worker 프로세스가 먼저 실행되어야 함  
- 인스턴스의 포트 열어주기  
```
pyspark --master spark://{public dns}:7077
```