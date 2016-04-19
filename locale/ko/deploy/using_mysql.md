# Seafile과 MySQL 가동

이 설명서는 미리 빌드한 Seafile 서버 꾸러미를 MySQL과 함께 설치하고 실행하는 방법을 설명합니다.

## 다운로드

최신 서버 꾸러미를 [다운로드](http://www.seafile.com/en/download) 하십시오.


## Deploying and Directory Layout

Supposed your organization's name is "haiwen", and you've downloaded `seafile-server_1.8.2_*` into your home directory. We suggest you to layout your deployment as follows :

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

The benefit of this layout is that:

* We can place all the config files for Seafile server inside "haiwen" directory, making it easier to manage.
* When you upgrade to a new version of Seafile, you can simply untar the latest package into "haiwen" directory. In this way you can reuse the existing config files in "haiwen" directory and don't need to configure again.

## MySQL 데이터베이스 준비

Three components of Seafile Server need their own databases:

* ccnet 서버
* seafile 서버
* seahub

Seafile 서버 구성요소에 대해 더 알아보려면 [Seafile 서버 구성 요소 둘러보기](../overview/components.md)를 살펴보십시오.

There are two ways to intialize the databases:

- let the <code>setup-seafile-mysql.sh</code> script create the databases for you.
- create the databases by yourself, or someone else (the database admin, for example)

We recommend the first way. The script would ask you for the root password of the mysql server, and it will create:

* ccnet/seafile/seahub 데이터베이스
* 데이터베이스에 접근할 새 사용자

However, sometimes you have to use the second way. If you don't have the root password, you need someone who has the privileges, e.g., the database admin, to create the three databases, as well as a mysql user who can access the three databases for you. For example, to create three databases: `ccnet-db` / `seafile-db` / `seahub-db` for ccnet/seafile/seahub respectively, and a mysql user "seafile" to access these databases:

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

* python 2.7 or 2.6.5+
* python-setuptools
* python-imaging
* python-ldap
* python-mysqldb
* python-memcache (or python-memcached)

<pre>
#on Debian/Ubuntu
apt-get update
apt-get install python2.7 libpython2.7 python-setuptools python-imaging \
  python-ldap python-mysqldb python-memcache
</pre>

### 설정

<pre>
cd seafile-server-*
./setup-seafile-mysql.sh  #run the setup script & answer prompted questions
</pre>

If some of the prerequisites are not installed, the seafile initialization script will ask you to install them.

스크립트는 다양한 설정 옵션 설정을 안내합니다.

** Seafile 설정 옵션 **

| Option | Description | Note |
| -- | -- | ---- |
| server name | Name of this seafile server | 3-15 characters, only English letters, digits and underscore ('_') are allowed |
| server ip or domain | The IP address or domain name used by this server | Seafile client program will access the server with this address |
| seafile data dir | Seafile stores your data in this directory. By default it'll be placed in the current directory.  | The size of this directory will increase as you put more and more data into Seafile. Please select a disk partition with enough free space.  |
| fileserver port | The TCP port used by Seafile fileserver | Default is 8082. If it's been used by other service, you can set it to another port.  |


At this moment, you will be asked to choose a way to initialize seafile databases:

```sh
-------------------------------------------------------
Please choose a way to initialize seafile databases:
-------------------------------------------------------

[1] Create new ccnet/seafile/seahub databases
[2] Use existing ccnet/seafile/seahub databases

```


Which one to choose depends on if you have the root password.

* If you choose "1", you need to provide the root password. The script would create the databases and a new user to access the databases
* If you choose "2", the ccnet/seafile/seahub databases must have already been created, either by you, or someone else.

If you choose "[1] Create new ccnet/seafile/seahub databases", you would be asked these questions:


| Question | Description | Note
| -- | -- | ---- |
| mysql server host | the host address of the mysql server | the default is localhost |
| mysql server port | the port of the mysql server | the default is 3306. Almost every mysql server uses this port.  |
| root password | the password of mysql root account | the root password is required to create new databases and a new user |
| mysql user for seafile | the username for seafile programs to use to access MySQL server | if the user does not exist, it would be created |
| password for seafile mysql user | the password for the user above | |
| ccnet dabase name | the name of the database used by ccnet, default is "ccnet-db" | the database would be created if not existing |
| seafile dabase name | the name of the database used by seafile, default is "seafile-db" | the database would be created if not existing |
| seahub dabase name | the name of the database used by seahub, default is "seahub-db" | the database would be created if not existing |


If you choose "[2] Use existing ccnet/seafile/seahub databases", you would be asked these questions:


** related questions for "Use existing ccnet/seafile/seahub databases" **

| Question | Description | Note |
| -- | -- | ---- |
| mysql server host | the host address of the mysql server | the default is localhost |
| mysql server port | the port of the mysql server | the default is 3306. Almost every mysql server uses this port |
| mysql user for seafile | the user for seafile programs to use to access MySQL server | the user must already exists |
| password for seafile mysql user | the password for the user above | |
| ccnet dabase name | the name of the database used by ccnet | this database must already exist |
| seafile dabase name | the name of the database used by seafile, default is "seafile-db" | this database must already exist |
| seahub dabase name | the name of the database used by seahub, default is "seahub-db" | this database must already exist |


설정을 완전히 끝냈으면 다음 출력을 볼 수 있습니다

![server-setup-succesfully](../images/Server-setup-successfully.png)

이제 다음 디렉터리 배치 상태를 지니고 있어야합니다:
```sh
#tree haiwen -L 2
haiwen
├── ccnet               # configuration files
│   ├── ccnet.conf
│   ├── mykey.peer
│   ├── PeerMgr
│   └── seafile.ini
├── installed
│   └── seafile-server_1.8.2_x86-64.tar.gz
├── seafile-data
│   └── seafile.conf
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
├── seahub_settings.py   # optional config file
└── seahub_settings.pyc
```

The folder <code>seafile-server-latest</code> is a symbolic link to the current seafile server folder. When later you upgrade to a new version, the upgrade scripts would update this link to keep it always point to the latest seafile server folder.

## Seafile 서버 실행


### Seafile 서버 및 Seahub 웹사이트 시작

Under seafile-server-1.8.2 directory, run the following commands


```
./seafile.sh start # Start seafile service
./seahub.sh start <port>  # Start seahub website, port defaults to 8000
```

Note: The first time you start seahub, the script would prompt you to create an admin account for your seafile server.

After starting the services, you may open a web browser and visit Seafile web interface at (assume your server IP is 192.168.1.111):

```
http://192.168.1.111:8000/
```


Congratulations! Now you have successfully setup your private Seafile server.


### 다른 포트에서 Seahub 실행

If you want to run seahub in a port other than the default 8000, say 8001, you must:

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

see [Seafile server configuration options](server_configuration.md) for more details about <code>ccnet.conf</code>.

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

* Use `pgrep` command to check if seafile/seahub processes are still running

<pre>
pgrep -f seafile-controller # check seafile processes
pgrep -f "manage.py run_gunicorn" # check seahub process
</pre>

* Use `pkill` to kill the processes

<pre>
pkill -f seafile-controller
pkill -f "manage.py run_gunicorn"
</pre>

## 성능 조정

If you have more than 50 users in your Seafile system, we highly recommand you to [add memcached](../deploy/add_memcached.md). This will make the web 10x faster.  

## 다 됐습니다!

다 됐습니다! 이제 Seafile에 대한 내용을 더 읽어 볼 차례입니다.


* [Deploy Seafile with Nginx](deploy_with_nginx.md) / [Deploy Seafile with Apache](deploy_with_apache.md)
* [Enable Https on Seafile Web with Nginx](https_with_nginx.md) / [Enable Https on Seafile Web with Apache](https_with_apache.md)
* [Seafile LDAP 사용 설정](using_ldap.md)
* [How to manage the server](../maintain/README.md)

