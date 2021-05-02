## EC2 에 chrome, chromedriver, selenium 설치  

<br>

```
# chrome browser 설치 
sudo curl https://intoli.com/install-google-chrome.sh | bash
sudo mv /usr/bin/google-chrome-stable /usr/bin/google-chrome
# chrome version 확인
google-chrome -version && which google-chrome

# chromedriver 설치
# 확인한 chromee version과 일치하는 드라이버 설치
sudo wget https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip

# selenium 설치
conda activate {virtual env}
pip install selenium
```

<br>

[참조 블로그](https://jhleed.tistory.com/195)