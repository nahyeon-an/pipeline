# Java 설치

### EC2 root 계정 활성화

*ec2-user로 접속*

1. root 계정의 password 변경  
```
sudo passwd root
```

2. root 계정으로 ssh 접속 허용 설정
```
sudo vi /etc/ssh/sshd_config

# 명령모드에서 :set nu를 입력하고
# 38번째 줄의 주석 해제 
```

3. ec2-user의 인증키를 root 계정에 복사
```
sudo cp /home/ec2-user/.ssh/authorized_keys /root/.ssh
```

4. ssh 서비스 재시작
```
sudo systemctl restart sshd
```


### java 설치

1. jdk 파일을 인스턴스로 복사
```
scp -i "pipeline.pem" ~/Downloads/jdk-8u281-linux-x64.tar.gz root@{ public ip }:/root/
```

*root 계정으로 인스턴스에 ssh 접속*

2. 압축 풀기
```
gunzip jdk-8u281-linux-x64.tar.gz
tar xvf jdk-8u281-linux-x64.tar
rm -f *.tar
```

3. jdk 파일 이동 및 링크 생성
```
mv jdk1.8.0_281 /usr/local/
cd /usr/local
ln -s jdk1.8.0_281 active-java
```

4. 환경변수 등록
```
vi /etc/profile

# 아래의 내용을 추가
export JAVA_HOME=/usr/local/active-java
PATH=$PATH:$JAVA_HOME/bin
```