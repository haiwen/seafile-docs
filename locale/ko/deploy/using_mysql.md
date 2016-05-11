# Seafile과 MySQL 가동

이 설명서는 미리 빌드한 Seafile 서버 꾸러미를 MySQL과 함께 설치하고 실행하는 방법을 설명합니다.

## 다운로드

최신 서버 꾸러미를 [다운로드](http://www.seafile.com/en/download) 하십시오.


## Deploying and Directory Layout

조직 이름을 "haiwen"이라 하고 `seafile-server_1.8.2_*` 파일을 내 폴더에 다운로드했다고 치겠습니다. 다음과 같은 구동 디렉터리 배치를 추천합니다:

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
#tree haiwen -L 2
haiwen
├── installed
│   └── seafile-server_1.8.2_x86-64.tar.gz
└── seafile-server-1.8.2
    ├── reset-admin.sh
    ├── runtime
    ├── seafile
    ├── seafile.sh
    ├── seahub
    ├── seahub.sh
    ├── setup-seafile.sh
    └── upgrade
</pre>

이 배치의 장점:

* "haiwen" 디렉터리에 Seafile 서버에 필요한 모든 설정 파일을 둘 수 있어 관리하기 쉽습니다.
* 새 Seafile 버전으로 업그레이드할 때, 간단하게 "haiwen" 디렉터리에 최신 꾸러미 압축을 해제할 수 있습니다. 이 방식으로 "haiwen" 디렉터리의 기존 설정 파일을 다시 사용할 수 있으며, 설정을 다시 만들 필요가 없습니다.

## MySQL 데이터베이스 준비

Seafile 서버에서는 다음 세가지 구성 요소의 자체 데이터베이스가 필요합니다:

* ccnet 서버
* seafile 서버
* seahub

Seafile 서버 구성요소에 대해 더 알아보려면 [Seafile 서버 구성 요소 둘러보기](../overview/components.md)를 살펴보십시오.

데이터베이스를 초기화하는 방법에는 두가지가 있습니다:

- 데이터베이스를 만드는 <code>setup-seafile-mysql.sh</code>  스크립트를 실행합니다.
- 여러분 자신 또는 누군가(데이터베이스 관리자)가 데이터베이스를 직접 만듭니다

첫번째 방법을 추천합니다. 스크립트에서는 MySQL 서버의 루트 암호를 물어본 후 다음 항목을 만듭니다:

* ccnet/seafile/seahub 데이터베이스.
* 데이터베이스에 접근할 새 사용자

하지만, 때로는 차선 책을 진행해야 할 수도 있습니다. 루트 암호를 모른다면, 데이터베이스 세가지를 만들고 해당 데이터베이스에 접근할 수 있는 사용자를 만들어줄 데이터베이스 관리자와 같은 권한을 가진 누군가가 필요합니다. 예를 들어 ccnet/Seafile/Seahub 각각에 대해 `ccnet-db` / `seafile-db` / `seahub-db` 데이터베이스와, 이 데이터베이스에 접근할 mysql 사용자 "seafile"을 만들려면:

<pre>
create database `ccnet-db` character set = 'utf8';
create database `seafile-db` character set = 'utf8';
create database `seahub-db` character set = 'utf8';

create user 'seafile'@'localhost' identified by 'seafile';

GRANT ALL PRIVILEGES ON `ccnet-db`.* to `seafile`@localhost;
GRANT ALL PRIVILEGES ON `seafile-db`.* to `seafile`@localhost;
GRANT ALL PRIVILEGES ON `seahub-db`.* to `seafile`@localhost;
</pre>

## Seafile 서버 설치

### 선행 과정

Seafile 서버 꾸러미에서는 시스템에 우선 설치한 다음 꾸러미가 필요합니다.

* python 2.7
* python-setuptools
* python-imaging
* python-ldap
* python-mysqldb
* python-memcache (or python-memcached)

<pre>
# on Debian/Ubuntu
apt-get update
apt-get install python2.7 libpython2.7 python-setuptools python-imaging \
  python-ldap python-mysqldb python-memcache
</pre>

<pre>
# on CentOS 7
sudo yum install python-imaging MySQL-python python-memcached python-ldap
</pre>

### 설정

<pre>
cd seafile-server-*
./setup-seafile-mysql.sh  #run the setup script & answer prompted questions
</pre>

선행 요구사항을 설치하지 않았다면 Seafile 초기화 스크립트에서 해당 구성요소를 설치하라고 요청합니다.

스크립트는 다양한 설정 옵션 설정을 안내합니다.

** Seafile 설정 옵션 **

| 설정 항목 | 설명 | 참고 |
| -- | -- | ---- |
| 서버 이름 | Seafile 서버 이름 | 영 대소문자, 숫자, 밑줄 문자('_')만으로 이루어진 3-15개 문자 허용 |
| 서버 IP 또는 도메인 | 서버에서 사용할 IP 주소 또는 도메인 이름 | Seafile 클라이언트 프로그램은 이 주소로 서버에 접근합니다 |
| Seafile 데이터 디렉터리 | Seafile에서는 이 디렉터리에 데이터를 저장합니다. 기본적으로 현재 디렉터리에 둡니다.  | 이 디렉터리의 크기는 Seafile에 데이터를 더 많이 두는 만큼 늘어납니다. 충분한 공간을 지닌 디스크 분할 공간을 선택하십시오.  |
| 파일 서버 포트 | Seafile 파일 서버에서 사용하는 TCP 포트 | 기본 값은 8082 입니다. 다른 서비스에서 사용한다면 다른 포트로 설정할 수 있습니다.  |


여기서, Seafile 데이터베이스 초기화 방식에 대한 질문을 받습니다:

```sh
-------------------------------------------------------
Please choose a way to initialize seafile databases:
-------------------------------------------------------

[1] Create new ccnet/seafile/seahub databases
[2] Use existing ccnet/seafile/seahub databases

```


루트 암호 설정 여부에 따라 다음 중 하나를 선택하십시오.

* "1"을 선택하면, 루트 암호를 입력해야합니다. 스크립트는 데이터베이스 및 데이터베이스 접근용 새 사용자를 만듭니다.
* "2"를 선택하면, 누가 만들어두었든지간에 ccnet/seafile/seahub 데이터베이스를 이미 만들어 둔 상태여야합니다.

"[1] Create new ccnet/seafile/seahub databases"를 선택하면, 다음 질문을 받습니다:


| 질문 | 설명 | 참고
| -- | -- | ---- |
| MySQL 서버 호스트 | MySQL 서버 호스트 주소 | 기본 주소 값은 localhost 입니다 |
| MySQL 서버 포트 | MySQL 서버 포트 | 기본값은 3306입니다. 대부분 모든 MySQL 서버는 이 포트를 사용합니다.  |
| 루트 암호 | MySQL 루트 계정 암호 | 새 데이터베이스 및 새 사용자를 만들 때 필요한 루트 암호 |
| Seafile MySQL 사용자 | Seafile 프로그램에서 MySQL 서버에 접근할 때 사용할 사용자 이름 | 사용자가 없다면 만듭니다 |
| Seafile MySQL 사용자 암호 | 위 사용자의 암호 | |
| ccnet 데이터베이스 이름 | ccnet에서 사용하는 데이터베이스 이름, 기본값은 "ccnet-db" | 없으면 데이터베이스를 만듭니다 |
| Seafile 데이터베이스 이름 | Seafile에서 사용하는 데이터베이스 이름, 기본값은 "seafile-db" | 없으면 데이터베이스를 만듭니다 |
| Seahub 데이터베이스 이름 | Seahub에서 사용하는 데이터베이스 이름, 기본값은 "seahub-db" | 없으면 데이터베이스를 만듭니다 |


"[2] Use existing ccnet/seafile/seahub databases"를 선택하면, 다음 질문을 받습니다:


** "Use existing ccnet/seafile/seahub databases" 관련 질문 **

| 질문 | 설명 | 참고
| -- | -- | ---- |
| MySQL 서버 호스트 | MySQL 서버 호스트 주소 | 기본 주소 값은 localhost 입니다 |
| MySQL 서버 포트 | MySQL 서버 포트 | 기본값은 3306입니다. 대부분 모든 MySQL 서버는 이 포트를 사용합니다 |
| Seafile MySQL 사용자 | Seafile 프로그램에서 MySQL 서버에 접근할 때 사용할 사용자 이름 | 사용자가 이미 있어야 합니다 |
| Seafile MySQL 사용자 암호 | 위 사용자의 암호 | |
| ccnet 데이터베이스 이름 | ccnet에서 사용하는 데이터베이스 이름, 기본값은 "ccnet-db" | 데이터베이스가 이미 있어야 합니다 |
| Seafile 데이터베이스 이름 | Seafile에서 사용하는 데이터베이스 이름, 기본값은 "seafile-db" | 데이터베이스가 이미 있어야 합니다 |
| Seahub 데이터베이스 이름 | Seahub에서 사용하는 데이터베이스 이름, 기본값은 "seahub-db" | 데이터베이스가 이미 있어야 합니다 |


설정을 완전히 끝냈으면 다음 출력을 볼 수 있습니다

![서버 설정 성공](../images/Server-setup-successfully.png)

이제 다음 디렉터리 배치 상태를 지니고 있어야합니다:
```sh
#tree haiwen -L 2
haiwen
├── ccnet               # configuration files
│   ├── mykey.peer
│   ├── PeerMgr
│   └── seafile.ini
├── conf
│   └── ccnet.conf
│   └── seafile.conf
│   └── seahub_settings.py
├── installed
│   └── seafile-server_1.8.2_x86-64.tar.gz
├── seafile-data
├── seafile-server-1.8.2  # active version
│   ├── reset-admin.sh
│   ├── runtime
│   ├── seafile
│   ├── seafile.sh
│   ├── seahub
│   ├── seahub.sh
│   ├── setup-seafile.sh
│   └── upgrade
├── seafile-server-latest  # symbolic link to seafile-server-1.8.2
├── seahub-data
│   └── avatars
```

<code>seafile-server-latest</code> 폴더는 현재 Seafile 서버 폴더의 심볼릭 링크입니다. 나중에 새 버전으로 업그레이드 하면, 업그레이드 스크립트에서 이 링크를 업데이트하여 항상 최신 Seafile 서버 폴더를 가리키도록 합니다.

## Seafile 서버 실행


### Seafile 서버 및 Seahub 웹사이트 시작

seafile-server-1.8.2 디렉터리에서 다음 명령을 실행하십시오


```
./seafile.sh start # Start seafile service
./seahub.sh start <port>  # Start seahub website, port defaults to 8000
```

참고: Seahub를 처음 실행할 때 스크립트에서 Seafile 서버의 admin 계정을 만들 지 여부를 물어봅니다.

서비스를 시작한 후, 웹 브라우저를 열고 다음 주소로 Seafile 웹 인터페이스에 접근하십시오(서버 IP를 192.168.1.111로 가정):

```
http://192.168.1.111:8000/
```


고생하셨습니다! 이제 개인 Seafile 서버 설정을 성공적으로 끝냈습니다.


### 다른 포트에서 Seahub 실행

8000번 기본 포트 대신 8001번과 같은 포트 번호에서 Seahub를 실행하려면 다음 과정을 수행해야합니다:

* Seafile 서버를 멈추십시오
<pre>
./seahub.sh stop
./seafile.sh stop
</pre>

* [ccnet.conf](../config/ccnet-conf.md)파일의 `SERVICE_URL` 값을 다음과 같은 값으로 바꾸십시오(IP 또는 도메인을 <code>192.168.1.100</code>으로 가정):
<pre>
SERVICE_URL = http://192.168.1.111:8001
</pre>

* Seafile 서버를 다시 시작하십시오
<pre>
./seafile.sh start
./seahub.sh start 8001
</pre>

<code>ccnet.conf</code>에 대한 자세한 내용은 [Seafile 서버 설정 항목](server_configuration.md)을 참고하십시오.

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

* `pgrep` 명령으로 Seafile/Seahub 프로세스가 여전히 실행중인지 확인하십시오

<pre>
pgrep -f seafile-controller # check seafile processes
pgrep -f "manage.py run_gunicorn" # check seahub process
</pre>

* `pkill` 명령으로 프로세스를 강제로 끝내십시오

<pre>
pkill -f seafile-controller
pkill -f "manage.py run_gunicorn"
</pre>

## 성능 조정

Seafile 시스템 사용자가 50명이 넘으면, [memcached 추가](../deploy/add_memcached.md)를 추천합니다. 웹 동작 속도가 10배 빨라집니다.  

## 다 됐습니다!

다 됐습니다! 이제 Seafile에 대한 내용을 더 읽어 볼 차례입니다.


* [Seafile과 Nginx 가동](deploy_with_nginx.md) / [Seafile과 Apache 가동](deploy_with_apache.md)
* [Nginx에서 Seafile 웹의 https 활성화](https_with_nginx.md) / [Apache에서 Seafile 웹의 https 활성화](https_with_apache.md)
* [Seafile LDAP 사용 설정](using_ldap.md)
* [서버 관리 방법](../maintain/README.md)

