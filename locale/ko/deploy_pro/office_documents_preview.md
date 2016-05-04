Seafile 전문가판 서버에서는 오피스/pdf 문서 온라인 미리보기를 지원하며, 이 기능을 사용하려면 이 페이지에 설명한 절차를 따라야합니다.

### 리버오피스/UNO 설치 ###

오피스 파일 온라인 미리보기 기능을 활성화하려면 리버오피스 4.1 이상 그리고 Python-uno 라이브러리가 필요합니다.

우분투/데비안:
```
sudo apt-get install libreoffice libreoffice-script-provider-python
```
> 우분투 이전 버전: `sudo apt-get install libreoffice python-uno`

CentOS/RHEL:
```
sudo yum install libreoffice libreoffice-headless libreoffice-pyuno
```

다른 리눅스 배포판: [리눅스에서 리버오피스 설치](http://www.libreoffice.org/get-help/installation/linux/)

또한, 사용 언어에 따라, 특히 아시아 언어권 사용자라면 글꼴을 설치해야하며, 설치하지 않으면 오피스/pdf 문서를 제대로 표시할 수 없습니다.

예를 들어, 중국어권 사용자는 WenQuanYi 트루타입 글꼴 모음을 설치하면 좋습니다:

```
# For ubuntu/debian
sudo apt-get install ttf-wqy-microhei ttf-wqy-zenhei xfonts-wqy
```

### 오피스 미리보기 활성화

1. `seafevents.conf` 파일을 열고 `OFFICE CONVERTER` 섹션에서:
```conf
[OFFICE CONVERTER]
enabled = true
```
2. `seafevents.conf`를 수정하고 저장한 다음, `./seafile.sh restart` 명령으로 Seafile 서버를 다시 시작하십시오
3. doc/ppt/xls/pdf 파일을 Seahub에서 열어보십시오. 브라우저에서 미리보기 화면이 나와야합니다.

### 다른 설정 가능 항목

좀 더 세밀하게 설정할 수 있는 설정 항목 모두를 모아두었습니다:

```conf
[OFFICE CONVERTER]

## must be "true" to enable office/pdf file online preview
enabled = true

## How many libreoffice worker processes to run concurrenlty
workers = 1

## where to store the converted office/pdf files. Deafult is /tmp/.
outputdir = /tmp/

## how many pages are allowed to be previewed online. Default is 50 pages
max-pages = 50

## the max size of documents to allow to be previewed online, in MB. Default is 2 MB
## Preview a large file (for example >30M) online will freeze the browser.
max-size = 2

```

## <a id="wiki-doc-preview"></a>오피스/PDF 문서 미리 보기 관련 자주 묻는 질문 ##

- 문서 미리보기 기능이 동작하지 않는데, 어디서 추가 정보를 찾을 수 있죠?

    logs/seafevents.log 로그를 확인해볼 수 있습니다


- 온라인 미리보기 기능 이용시 문서의 최대 용량 및 최대 페이지 수를 어떻게 바꿀 수 있죠?

1. `seafevents.conf`의 `OFFICE CONVERTER` 섹션을 찾으십시오.
2. 섹션에 다음 줄을 추가하십시오
```
# the max size of documents to allow to be previewed online, in MB. Default is 2 MB
max-size = 2
# how many pages are allowed to be previewed online. Default is 50 pages
max-pages = 50
```

그 다음 Seafile 서버를 다시 시작하십시오
```
cd /data/haiwen/seafile-server-latest/
./seafile.sh restart
./seahub.sh restart
```

- 우분투/데비안 서버에서 문서 미리보기 기능이 동작하지 않는데 뭘 할 수 있죠?

현재 오피스 온라인 미리보기 기능은 리버오피스 4.0-4.2와 동작합니다. `apt-get`으로 설치한 리버오피스 버전이 너무 오래됐거나 너무 최신이면 다음 절차로 해결할 수 있습니다:

- 설치한 libreoffice를 제거하십시오:
```
sudo apt-get remove libreoffice* python-uno python3-uno
```
- [리버 오피스 공식 사이트](http://sourceforge.net/projects/libreoffice.mirror/files/LibreOffice%204.1.6/)에서 리버 오피스 꾸러미를 다운로드하십시오

- 다운로드한 꾸러미를 설치하십시오:
```
tar xf LibreOffice_4.1.6_Linux_x86-64_deb.tar.gz
cd LibreOffice_4.1.6.2_Linux_x86-64_deb
cd DEBS
sudo dpkg -i *.deb
```

- Seafile 서버를 다시 시작하고 다시 시도해보십시오. 잘 동작해야합니다.
```
./seafile.sh restart
```

