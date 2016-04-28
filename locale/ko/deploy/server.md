# Seafile
## 서버

이 설명서는 미리 빌드한 Seafile 서버 꾸러미를 설치하고 실행하는 방법을 설명합니다.

## 플랫폼 지원

- 일반 리눅스
    - 라즈베리 파이 포함
- 윈도우

## 다운로드

Visit [our download page](http://www.seafile.com/en/download), download the latest server package.

<pre>
#check if your system is x86 (32bit) or x86_64 (64 bit)
uname -m
</pre>


## Deploying and Directory Layout

NOTE: If you place the Seafile data directory in external storage, such as NFS, CIFS mount, you should not use SQLite as the database, but use MySQL instead. Please follow [https://github.com/haiwen/seafile/wiki/Download-and-Setup-Seafile-Server-with-MySQL this manual] to setup Seafile server.

Supposed your organization's name is "haiwen", and you've downloaded seafile-server_1.4.0_* into your home directory.
We suggest you to layout your deployment as follows :

<pre>
mkdir haiwen
mv seafile-server_* haiwen
cd haiwen
# after moving seafile-server_* to this directory
tar -xzf seafile-server_*
mkdir installed
mv seafile-server_* installed
</pre>

Now you should have the following directory layout
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

'''The benefit of this layout is that'''

* We can place all the config files for Seafile server inside "haiwen" directory, making it easier to manage.
* When you upgrade to a new version of Seafile, you can simply untar the latest package into "haiwen" directory. ''In this way you can reuse the existing config files in "haiwen" directory and don't need to configure again''.

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

If some of the prerequisites are not installed, the seafile initialization script will ask you to install them.

[[images/server-setup.png|설정 스크립트를 실행하면 볼 수 있는 출력입니다]]

스크립트는 다양한 설정 옵션 설정을 안내합니다.


{| border="1" cellspacing="0" cellpadding="5" align="center"
|+ Seafile configuration options
! Option
! Description
! Note
|-
| server name
| Name of this seafile server
| 3-15 characters, only English letters, digits and underscore ('_') are allowed
|-
| server ip or domain
| The IP address or domain name used by this server
| Seafile client program will access the server with this address
|-
| ccnet server port
| The TCP port used by ccnet, the underlying networking service of Seafile
| Default is 10001. If it's been used by other service, you can set it to another port.
|-
| seafile data dir
| Seafile stores your data in this directory. By default it'll be placed in the current directory.
| The size of this directory will increase as you put more and more data into Seafile. Please select a disk partition with enough free space.
|-
| seafile server port
| The TCP port used by Seafile to transfer data
| Default is 12001. If it's been used by other service, you can set it to another port.
|-
| fileserver  port
| The TCP port used by Seafile fileserver
| Default is 8082. If it's been used by other service, you can set it to another port.
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

The folder <code>seafile-server-latest</code> is a symbolic link to the current seafile server folder. When later you upgrade to a new version, the upgrade scripts would update this link to keep it always point to the latest seafile server folder.


## Seafile 서버 실행

#### 실행 전

Since Seafile uses persistent connection between client and server, if you have '''a large number of clients ''', you should increase Linux file descriptors by ulimit before start seafile, like:

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
you will be redirected to the Login page. Enter the username and password you were provided during the Seafile setup. You will then be returned to the `Myhome` page where you can create libraries.

'''Congratulations!''' Now you have successfully setup your private Seafile server.

#### 다른 포트에서 Seahub 실행

If you want to run seahub in a port other than the default 8000, say 8001, you must:

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

