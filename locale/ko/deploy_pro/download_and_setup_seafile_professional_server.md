# Seafile 전문가 서버 다운로드 및 설치
## <a id="wiki-preparation"></a>준비 ##

다음 문서는 우분투 14.04와 CentOS 7에서 확인했습니다. 우분투 14.04 또는 CentOS 7 서버를 사용하시는게 좋습니다.

> 참고:
>
> 우분투 14.04를 활용중이면, 다음 명령을 활용하여 Seafile에서 필요한 모든 의존 요소를 한번에 설치할 수 있습니다.
>
> ```
> sudo apt-get install openjdk-7-jre poppler-utils libpython2.7 python-pip \
> mysql-server python-setuptools python-imaging python-mysqldb python-memcache python-ldap
>
> sudo pip install boto
> ```
>
> CentOS 7:
>
> ```
> wget https://bootstrap.pypa.io/get-pip.py
> sudo python get-pip.py
> sudo yum install java-1.7.0-openjdk poppler-utils python-dev python-setuptools \
> python-imaging MySQL-python mysql-server.x86_64 python-memcached python-ldap
>
> sudo pip install boto
> sudo /etc/init.d/mysqld start
> ```
>
> 자세한 내용은 하단을 참고하십시오.

### 최소 시스템 요구 사항 ###

- 2GB 램을 장착한 리눅스 서버

### 자바 런타임 환경(JRE) 설치 ###

우분투/데비안:
```
sudo apt-get install openjdk-7-jre
```

CentOS/레드햇:
```
sudo yum install java-1.7.0-openjdk
```

### poppler-utils 설치 ###

pdf 파일에서 완전한 문구 검색을 처리하려면 poppler-utils가 필요합니다.

우분투/데비안:
```
sudo apt-get install poppler-utils
```

CentOS/레드햇:
```
sudo yum install poppler-utils
```


### 파이썬 라이브러리 설치 ###

우선 파이썬 2.7을 설치했는지 확인하십시오
```
sudo easy_install pip
sudo pip install boto
```

"Wheel installs require setuptools >= ..." 오류 메시지가 나타났다면, pip과 boto 줄 사이에 다음 명령을 실행하십시오
```
sudo pip install setuptools --no-use-wheel --upgrade
```

### 우분투 14.04일 경우 libpython2.7 설치

```
sudo apt-get install libpython2.7
```

### 커뮤니티판에서 필요한 기타 라이브러리 설치

[Seafile 서버 및 MySQL 다운로드 및 설치](../deploy/using_mysql.md)를 참고하십시오.

## <a id="wiki-download-and-setup"></a> Seafile 전문가 서버 다운로드 및 설치 ##

### 라이선스 취득 ###

라이선스 파일을 최상위 디렉터리에 넣으십시오. 위키에서는 최상위 디렉터리로 `/data/haiwen` 디렉터리를 사용합니다.


### <a id="wiki-download-and-uncompress"></a>Seafile 전문가판 서버 다운로드/압축 해제 ###


```
tar xf seafile-pro-server_1.8.0_x86-64.tar.gz
```

이제 다음 파일 및 디렉터리가 나타납니다:

```
haiwen
├── seafile-license.txt
└── seafile-pro-server-1.8.0/
```


-----------

커뮤니티판 서버와 전문가판 서버의 이름이 다르다는 점에 주목하십시오. 1.8.0 64비트 버전을 예로 들어보겠습니다:

- Seafile 커뮤니티판 서버 타르볼은 `seafile-server_1.8.0_x86-86.tar.gz`이며, 압축을 해제하면 `seafile-server-1.8.0` 폴더가 나옵니다
- Seafile 전문가판 서버 타르볼은 `seafile-pro-server_1.8.0_x86-86.tar.gz`이며, 압축을 해제하면 `seafile-pro-server-1.8.0` 폴더가 나옵니다

-----------


### 설치 ###

 Seafile 전문가판 설치 과정은 Seafile 커뮤니티판 서버 설치 과정과 비슷합니다. [Seafile 서버 및 MySQL 다운로드 및 설치](../deploy/using_mysql.md)를 참고하십시오.

서비스 설정에 문제가 있다면 [Seafile 서버 설정 과정 중 일반적인 문제](../deploy/common_problems_for_setting_up_server.md)를 확인하십시오.

Seafile 전문가판 서버 설정이 제대로 끝나면, 디렉터리 배치는 다음과 같습니다:

```
#tree haiwen -L 2
haiwen
├── seafile-license.txt # license file
├── ccnet               # configuration files
│   ├── mykey.peer
│   ├── PeerMgr
│   └── seafile.ini
├── conf
│   └── ccnet.conf
│   └── seafile.conf
│   └── seahub_settings.py
│   └── seafevents.conf
├── pro-data            # data specific for professional version
├── seafile-data
├── seafile-pro-server-1.8.0
│   ├── reset-admin.sh
│   ├── runtime
│   ├── seafile
│   ├── seafile.sh
│   ├── seahub
│   ├── seahub-extra
│   ├── seahub.sh
│   ├── setup-seafile.sh
│   ├── setup-seafile-mysql.py
│   ├── setup-seafile-mysql.sh
│   └── upgrade
├── seahub-data
│   └── avatars         # for user avatars
├── seahub.db
```

## 성능 조정

Seafile 시스템 사용자가 50명 이상인 경우 [memcached를 추가](../deploy/add_memcached.md) 하시는 것이 좋습니다. 웹을 10배 빠르게 해줍니다.

## <a id="wiki-done"></a>완료

여기서 Seafile 전문가판 서버 기본 설정은 끝납니다.

Seafile 전문가판 서버에 대해 더 읽어볼 만한 내용이 있습니다:

- [Seafile 전문가판 서버에 대한 자주 묻는 질문](faq_for_seafile_pro_server.md)

