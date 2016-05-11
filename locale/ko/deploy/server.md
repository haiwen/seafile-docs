# Seafile
## 서버

이 설명서는 미리 빌드한 Seafile 서버 꾸러미를 설치하고 실행하는 방법을 설명합니다.

## 플랫폼 지원

- 일반 리눅스
    - 라즈베리 파이 포함
- 윈도우

## 다운로드

[다운로드 페이지](http://www.seafile.com/en/download)로 가셔서 최신 서버 꾸러미를 다운로드하십시오.

<pre>
#check if your system is x86 (32bit) or x86_64 (64 bit)
uname -m
</pre>


## Deploying and Directory Layout

참고: NFS, CIFS 마운트로 외장 저장소에 Seafile 데이터 디렉터리를 두는 경우 SQLite를 데이터베이스로 쓰면 안되며, 대신 MySQL을 쓰셔야합니다. Seafile 서버 설정시 [https://github.com/haiwen/seafile/wiki/Download-and-Setup-Seafile-Server-with-MySQL 이 설명서] 내용을 따르십시오.

조직 이름을 "haiwen"이라 하고, seafile-server_1.4.0_*을 내 폴더에 다운로드했음을 가정하겠습니다.
가동 구성을 다음과 같이 제안합니다 :

<pre>
mkdir haiwen
mv seafile-server_* haiwen
cd haiwen
# after moving seafile-server_* to this directory
tar -xzf seafile-server_*
mkdir installed
mv seafile-server_* installed
</pre>

이제 다음 디렉터리 배치 상태를 갖추고 있어야합니다
<pre>
# tree . -L 2
.
├── installed
│   └── seafile-server_1.4.0_x86-64.tar.gz
└── seafile-server-1.4.0
    ├── reset-admin.sh
    ├── runtime
    ├── seafile
    ├── seafile.sh
    ├── seahub
    ├── seahub.sh
    ├── setup-seafile.sh
    └── upgrade
</pre>

'''이 디렉터리 배치의 장점은'''

* "haiwen" 디렉터리에 Seafile 서버에 필요한 모든 설정 파일을 둘 수 있어 관리하기 쉽습니다.
* Seafile 새 버전으로 업그레이드 할 때 "haiwen" 디렉터리에 최신 꾸러미 압축을 풀기만 하면 됩니다. ''이 방식으로 "haiwen" 디렉터리의 기존 설정 파일을 다시 사용할 수 있으며, 설정 값을 다시 만들 필요가 없습니다''.

## Seafile 서버 설치

#### 사전 요구사항

Seafile 서버 꾸러미에서는 시스템에 우선 설치한 다음 꾸러미가 필요합니다.

* python 2.6.5+ or 2.7
* python-setuptools
* python-simplejson
* python-imaging
* sqlite3

<pre>
# Debian
apt-get update
apt-get install python2.7 python-setuptools python-simplejson python-imaging sqlite3
</pre>

#### 설정

<pre>
cd seafile-server-*
./setup-seafile.sh  #run the setup script & answer prompted questions
</pre>

선행 요구사항을 설치하지 않았다면 Seafile 초기화 스크립트에서 해당 구성요소를 설치하라고 요청합니다.

[[images/server-setup.png|설정 스크립트를 실행하면 볼 수 있는 출력입니다]]

스크립트는 다양한 설정 옵션 설정을 안내합니다.


{| border="1" cellspacing="0" cellpadding="5" align="center"
|+ Seafile 설정 항목
! 설정 항목
! 설명
! 참고
|-
| 서버 이름
| Seafile 서버 이름
| 3-15 문자, 영문자, 숫자, 밑줄 문자('_')만 허용
|-
| 서버 IP 또는 도메인
| 서버에서 사용하는 IP 주소 또는 도메인 이름
| Seafile 클라이언트 프로그램에서 이 주소로 서버에 접근합니다
|-
| ccnet 서버 포트
| Seafile의 네트워크 하부 서비스 ccnet에서 사용하는 TCP 포트
| 기본값은 10001 입니다. 다른 서비스에서 이미 사용중이라면 다른 포트 번호로 설정할 수 있습니다.
|-
| Seafile 데이터 디렉터리
| Seafile은 이 디렉터리에 데이터를 저장합니다. 기본적으로 현재 디렉터리에 저장합니다.
| 이 디렉터리 크기는 Seafile에 데이터를 넣는 만큼 늘어납니다. 충분한 용량을 갖는 디스크 분할 영역을 선택하십시오.
|-
| Seafile 서버 포트
| Seafile에서 데이터 전송에 사용하는 TCP 포트
| 기본값은 12001 입니다. 다른 서비스에서 이미 사용중이라면 다른 포트 번호로 설정할 수 있습니다.
|-
| fileserver 포트
| Seafile 파일 서버에서 사용하는 TCP 포트입니다
| 기본값은 8082 입니다. 다른 서비스에서 이미 사용중이라면 다른 포트 번호로 설정할 수 있습니다.
|-
|}


설정을 완전히 끝냈으면 다음 출력을 볼 수 있습니다

[[images/server-setup-successfully.png]]

이제 다음 디렉터리 배치 상태를 지니고 있어야합니다:
<pre>
#tree haiwen -L 2
haiwen
├── ccnet               # 설정 파일
│   ├── ccnet.conf
│   ├── mykey.peer
│   ├── PeerMgr
│   └── seafile.ini
├── installed
│   └── seafile-server_1.4.0_x86-64.tar.gz
├── seafile-data
│   └── seafile.conf
├── seafile-server-1.4.0  # 현재 버전
│   ├── reset-admin.sh
│   ├── runtime
│   ├── seafile
│   ├── seafile.sh
│   ├── seahub
│   ├── seahub.sh
│   ├── setup-seafile.sh
│   └── upgrade
├── seafile-server-latest  # seafile-server-1.4.0 심볼릭 링크
├── seahub-data
│   └── avatars
├── seahub.db
├── seahub_settings.py   # 추가 설정 파일
└── seahub_settings.pyc
</pre>

<code>seafile-server-latest</code> 폴더는 현재 Seafile 서버 폴더의 심볼릭 링크입니다. 나중에 새 버전으로 업그레이드 하면, 업그레이드 스크립트에서 이 링크를 업데이트하여 항상 최신 Seafile 서버 폴더를 가리키도록 합니다.


## Seafile 서버 실행

#### 실행 전

Seafile은 클라이언트 서버간 연결을 유지하므로 '''상당히 많은 클라이언트'''를 보유하고 있다면, Seafile을 시작하기 전, 다음과 같이 ulimit으로 리눅스 파일 서술자 갯수를 늘리셔야합니다:

<pre>
ulimit -n 30000
</pre>

#### Seafile 서버 및 Seafile 웹사이트 시작하기

seafile-server-1.4.0 디렉터리 아래에서 다음 명령을 실행하십시오

* Seafile을 시작하십시오:

<pre>
./seafile.sh start # Start seafile service
</pre>

* Seahub를 시작하십시오

<pre>
./seahub.sh start <port>  # Start seahub website, port defaults to 8000
</pre>

'''참고''': seahub를 처음 시작할 때, 스크립트에서는 Seafile 서버에서 사용할 admin 계정 생성 여부를 물어봅니다.

서비스를 시작하고 나면 웹 브라우저를 열고 다음 주소를 입력하십시오
<pre>
http://192.168.1.111:8000/
</pre>
로그인 페이지로 이동합니다. Seafile 설정 중 제시한 사용자 이름 및 암호를 입력하십시오. 라이브러리를 만들 수 있는 ` 내 페이지`로 돌아갑니다.

'''고생하셨습니다!''' 이제 개인 Seafile 서버 설정을 성공적으로 끝냈습니다.

#### 다른 포트에서 Seahub 실행

8000번 기본 포트 대신 8001번과 같은 포트 번호에서 Seahub를 실행하려면 다음 과정을 수행해야합니다:

* Seafile 서버를 멈추십시오
<pre>
./seahub.sh stop
./seafile.sh stop
</pre>

* [ccnet.conf](../config/ccnet-conf.md)파일의 <code>SERVICE_URL</code> 값을 다음과 같은 값으로 바꾸십시오(IP 또는 도메인을 <code>192.168.1.100</code>으로 가정):
<pre>
SERVICE_URL = http://192.168.1.100:8001
</pre>

* Seafile 서버를 다시 시작하십시오
<pre>
./seafile.sh start
./seahub.sh start 8001
</pre>

<code>ccnet.conf</code>에 대한 자세한 내용을 알아보려면 [[Seafile server configuration options|Seafile 서버 설정 항목]]을 참고하십시오.

## Seafile 및 Seahub 중지 및 다시 시작

#### 중지

<pre>
./seahub.sh stop # stop seahub website
./seafile.sh stop # stop seafile processes
</pre>

#### 다시 시작

<pre>
./seafile.sh restart
./seahub.sh restart
</pre>

#### 스크립트 동작에 실패했을 때

대부분의 경우 seafile.sh와 seahub.sh는 잘 동작합니다. 하지만 동작에 실패했을 경우:

* '''pgrep''' 명령으로 seafile/seahub 프로세스가 여전히 동작중인지 확인하십시오

<pre>
pgrep -f seafile-controller # check seafile processes
pgrep -f "manage.py run_gunicorn" # check seahub process
</pre>

* '''pkill''' 명령으로 해당 프로세스를 강제로 끝내십시오

<pre>
pkill -f seafile-controller
pkill -f "manage.py run_gunicorn"
</pre>

## 다 됐습니다!
다 됐습니다! 이제 Seafile에 대한 내용을 더 읽어 볼 차례입니다.

* [[Seafile-server-management|서버 관리 방법]].

