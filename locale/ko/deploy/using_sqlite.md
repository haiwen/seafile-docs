# Seafile과 SQLite 가동

## 바이너리 꾸러미 다운로드

[다운로드 페이지](http://seafile.com/en/download/#server)를 방문하여 최신 서버 꾸러미를 다운로드하십시오.

다음 중 하나를 선택하십시오:
- 일반 리눅스
- 윈도우
- 라즈베리 파이용 서버

```
#check if your system is x86 (32bit) or x86_64 (64 bit)
uname -m
```
타르볼 링크를 누른 후 저장하십시오.


## Deploying and Directory Layout

참고: Seafile 데이터 디렉터리를 NFS, CIFS 마운트 저장소 같은 외장 저장소에 둘 때, SQLite 대신 MySQL 데이터베이스를 사용하십시오.

조직 이름을 "haiwen"이라 하고, seafile-server_1.4.0_*을 내 폴더에 다운로드했음을 가정하겠습니다. 가동 구성을 다음과 같이 제안합니다:
```sh
mkdir haiwen
mv seafile-server_* haiwen
cd haiwen
# after moving seafile-server_* to this directory
tar -xzf seafile-server_*
mkdir installed
mv seafile-server_* installed
```

이제 다음 디렉터리 배치 상태를 갖추고 있어야합니다
```sh
# tree . -L 2
.
├── installed
│   └── seafile-server_1.4.0_x86-64.tar.gz
└── seafile-server-1.4.0
    ├── reset-admin.sh
    ├── runtime
    ├── seafile
    ├── seafile.sh
    ├── seahub
    ├── seahub.sh
    ├── setup-seafile.sh
    └── upgrade
```

이 디렉터리 배치를 통해 취할 수 있는 이익은

 - "haiwen" 디렉터리에 Seafile 서버용 설정 파일을 둘 수 있으며, 관리하기 쉽습니다.
 - Seafile을 새 버전을 업그레이드 할 때 "haiwen" 디렉터리의 최신 꾸러미 압축을 해제하기만 하면 됩니다. 이 방식으로 "haiwen" 디렉터리의 기존 설정 파일을 다시 사용할 수 있으며 다시 설정할 필요가 없습니다.


## Seafile 서버 설치
#### 사전 요구사항

Seafile 서버 꾸러미에서는 시스템에 우선 설치한 다음 꾸러미가 필요합니다.

- python 2.7
- python-setuptools
- python-imaging
- python-ldap
- sqlite3

```
#on Debian
apt-get update
apt-get install python2.7 libpython2.7 python-setuptools python-imaging python-ldap sqlite3
```

```
# on CentOS 7
sudo yum install python-imaging MySQL-python python-memcached python-ldap
```

#### 설정

```sh
cd seafile-server-*
./setup-seafile.sh  #run the setup script & answer prompted questions
```

이전 준비 요소를 설치하지 않았다면 Seafile 초기화 스크립트에서 설치하라고 요구합니다.

스크립트는 다양한 설정 옵션 설정을 안내합니다.

**Seafile 설정 항목**

| 설정 항목 | 설명 | 참고 |
| -- | -- | ---- |
| 서버 이름 | Seafile 서버 이름 | 3-15 문자, 영문자, 숫자, 밑줄 문자('_')만 허용 |
| 서버 IP 또는 도메인  | 서버에서 사용하는 IP 주소 또는 도메인 이름  | Seafile 클라이언트 프로그램에서 이 주소로 서버에 접근합니다 |
| Seafile 데이터 디렉터리  | Seafile에서는 이 디렉터리에 데이터를 저장합니다. 기본적으로 현재 디렉터리에 둡니다.  | 이 디렉터리 크기는 Seafile에 데이터를 넣는 만큼 늘어납니다. 충분한 용량을 갖는 디스크 분할 영역을 선택하십시오. |
| fileserver 포트 | Seafile 파일 서버에서 사용하는 TCP 포트입니다  | 기본값은 8082 입니다. 다른 서비스에서 이미 사용중이라면 다른 포트 번호로 설정할 수 있습니다. |


다음 디렉터리 구성을 갖춥니다:

```sh
#tree haiwen -L 2
haiwen
├── ccnet               # configuration files
│   ├── mykey.peer
│   ├── PeerMgr
│   └── seafile.ini
├── conf
│   └── ccnet.conf
│   └── seafile.conf
│   └── seahub_settings.py
├── installed
│   └── seafile-server_1.4.0_x86-64.tar.gz
├── seafile-data
├── seafile-server-1.4.0  # active version
│   ├── reset-admin.sh
│   ├── runtime
│   ├── seafile
│   ├── seafile.sh
│   ├── seahub
│   ├── seahub.sh
│   ├── setup-seafile.sh
│   └── upgrade
├── seafile-server-latest  # symbolic link to seafile-server-1.4.0
├── seahub-data
│   └── avatars
├── seahub.db
```

seafile-server-latest 폴더는 현재 Seafile 서버 폴더의 심볼릭 링크입니다. 나중에 새 버전으로 업그레이드하면, 업그레이드 스크립트에서 이 링크를 업데이트하여 최신 Seafile 서버 폴더를 항상 가리키도록합니다.

## Seafile 서버 실행

#### 실행 전

Seafile은 클라이언트-서버간 연결을 유지하므로 Seafile을 시작하기 전에 많은 수의 클라이언트를 보유하고 있다면, 다음과 같이 ulimit로 리눅스 파일 서술자 갯수를 늘려야합니다:

``ulimit -n 30000``

#### Seafile 서버 및 Seafile 웹사이트 시작하기

- Seafile을 시작하십시오:
```
./seafile.sh start # Start Seafile service
```

- Seahub를 시작하십시오:
```
./seahub.sh start <port>  # Start Seahub website, port defaults to 8000
```

**참고**: Seahub를 처음 시작할 때, 스크립트는 Seafile 서버에 admin 계정을 만들지 물어봅니다.

서비스를 시작한 후 웹 브라우저에서 다음 주소를 입력하여 여십시오

``http://192.168.1.111:8000``

이제 로그인 페이지로 돌아갑니다. admin 사용자 이름 및 암호를 입력하십시오.

**고생하셨습니다!** 이제 개인 Seafile 서버 설정을 성공적으로 끝냈습니다.

#### 다른 포트에서 Seahub 실행

기본 8000번 포트가 아닌, 8001번 포트에서 Seahub를 실행하려면, 다음 과정을 진행해야합니다:

- Seafile 서버를 멈추십시오
```
./seahub.sh stop
./seafile.sh stop
```

- [ccnet.conf](../config/ccnet-conf.md) 파일의 SERVICE_URL 값을 다음과 같이 바꾸십시오: (IP 또는 도메인이 192.168.1.100임을 가정). 5.0 이상 버전에서는, 웹 UI의 "시스템 관리자->설정"에서 SERVICE_URL 값을 바꿀 수 있습니다.
```
SERVICE_URL = http://192.168.1.100:8001
```

- Seafile 서버를 다시 시작하십시오
```
./seafile.sh start
./seahub.sh start 8001
```

 ``ccnet.conf``에 대해 자세한 내용을 알아보려면 Seafile [서버 설정 설명서](deploy/server_configuration.md)를 살펴보십시오.

## Seafile, Seahub 관리
#### 중지
```
./seahub.sh stop # stop seahub website
./seafile.sh stop # stop seafile processes
```
#### 다시 시작
```
./seafile.sh restart
./seahub.sh restart
```
#### 스크립트 동작에 실패했을 때

대부분의 경우, `seafile.sh`와 `seahub.sh`는 제대로 동작합니다. 다만, 동작이 실패할경우 다음과 같은 조치를 취할 수 있습니다

- pgrep 명령으로 Seafile/Seahub 프로세스가 여전히 동작 중인지 확인하십시오
```
pgrep -f seafile-controller # check Seafile processes
pgrep -f "manage.py run_gunicorn" # check Seahub process
```

- pkill 명령으로 해당 프로세스를 강제로 끝내십시오
```
pkill -f seafile-controller
pkill -f "manage.py run_gunicorn"
```

## 다 됐습니다!
실 사용 서버에서는 Nginx/Apache 및 SSL/TLS 설정을 추천합니다.

다 됐습니다! 이제 Seafile에 대한 내용을 더 읽어 볼 차례입니다.
- [관리](../maintain/README.md)

