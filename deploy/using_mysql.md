# Deploying Seafile with MySQL

This manual explains how to setup and run Seafile server from a pre-built package with MySQL.

## Download

[Download](https://www.seafile.com/en/download) the latest server package.


## Deploying and Directory Layout

Supposed your organization's name is "haiwen", and you've downloaded `seafile-server_1.8.2_*` into your home directory. We suggest you to to use the following layout for your deployment:

```
mkdir haiwen
mv seafile-server_* haiwen
cd haiwen
# after moving seafile-server_* to this directory
tar -xzf seafile-server_*
mkdir installed
mv seafile-server_* installed
```

Now you should have the following directory layout
```
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
```

The benefit of this layout is that:

* We can place all the config files for Seafile server inside "haiwen" directory, making it easier to manage.
* When you upgrade to a new version of Seafile, you can simply untar the latest package into "haiwen" directory. In this way you can reuse the existing config files in "haiwen" directory and don't need to configure again.

## Prepare MySQL Databases

Three components of Seafile Server need their own databases:

* ccnet server
* seafile server
* seahub

See [Seafile Server Components Overview](../overview/components.md) if you want to know more about the Seafile server components.

There are two ways to intialize the databases:

- let the `setup-seafile-mysql.sh` script create the databases for you.
- create the databases by yourself, or someone else (the database admin, for example)

We recommend the first way. The script would ask you for the root password of the mysql server, and it will create:

* database for ccnet/seafile/seahub.
* a new user to access these databases

However, sometimes you have to use the second way. If you don't have the root password, you need someone who has the privileges, e.g., the database admin, to create the three databases, as well as a mysql user who can access the three databases for you. For example, to create three databases: `ccnet-db` / `seafile-db` / `seahub-db` for ccnet/seafile/seahub respectively, and a mysql user "seafile" to access these databases run the following SQL queries:

```
create database `ccnet-db` character set = 'utf8';
create database `seafile-db` character set = 'utf8';
create database `seahub-db` character set = 'utf8';

create user 'seafile'@'localhost' identified by 'seafile';

GRANT ALL PRIVILEGES ON `ccnet-db`.* to `seafile`@localhost;
GRANT ALL PRIVILEGES ON `seafile-db`.* to `seafile`@localhost;
GRANT ALL PRIVILEGES ON `seahub-db`.* to `seafile`@localhost;
```

## Setting Up Seafile Server

### Prerequisites

The Seafile server package requires the following packages to be installed on your system

* python 2.7
* python-setuptools
* python-imaging
* python-ldap
* python-mysqldb
* python-urllib3
* python-memcache (or python-memcached)
* python-requests

```
# on Debian/Ubuntu 14.04 server
apt-get update
apt-get install python2.7 libpython2.7 python-setuptools python-imaging \
  python-ldap python-mysqldb python-memcache python-urllib3 python-requests
```

```
# on Ubuntu 16.04 server
# As the default python binary on Ubuntu 16.04 server is python 3, we need to install python (python 2) first.
apt-get update
apt-get install python
apt-get install python2.7 libpython2.7 python-setuptools python-imaging python-ldap python-urllib3 ffmpeg python-pip python-mysqldb python-memcache python-requests
pip install pillow moviepy
```

```
# on CentOS 7
yum -y install epel-release
rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
yum -y install python-imaging MySQL-python python-memcached python-ldap python-urllib3 ffmpeg ffmpeg-devel python-requests
pip install pillow moviepy
```

### Setup

```
cd seafile-server-*
./setup-seafile-mysql.sh  #run the setup script & answer prompted questions
```

If some of the prerequisites are not installed, the Seafile initialization script will ask you to install them.

The script will guide you through the settings of various configuration options.

** Seafile configuration options **

| Option | Description | Note |
| -- | -- | ---- |
| server name | Name of this seafile server | 3-15 characters, only English letters, digits and underscore ('_') are allowed |
| server ip or domain | The IP address or domain name used by this server | Seafile client program will access the server with this address |
| seafile data dir | Seafile stores your data in this directory. By default it'll be placed in the current directory.  | The size of this directory will increase as you put more and more data into Seafile. Please select a disk partition with enough free space.  |
| fileserver port | The TCP port used by Seafile fileserver | Default is 8082. If it's been used by other service, you can set it to another port.  |


At this moment, you will be asked to choose a way to initialize Seafile databases:

```sh
-------------------------------------------------------
Please choose a way to initialize Seafile databases:
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
| mysql user for Seafile | the username for Seafile programs to use to access MySQL server | if the user does not exist, it would be created |
| password for Seafile mysql user | the password for the user above | |
| ccnet dabase name | the name of the database used by ccnet, default is "ccnet-db" | the database would be created if not existing |
| seafile dabase name | the name of the database used by Seafile, default is "seafile-db" | the database would be created if not existing |
| seahub dabase name | the name of the database used by seahub, default is "seahub-db" | the database would be created if not existing |


If you choose "[2] Use existing ccnet/seafile/seahub databases", you would be asked these questions:


** related questions for "Use existing ccnet/seafile/seahub databases" **

| Question | Description | Note |
| -- | -- | ---- |
| mysql server host | the host address of the mysql server | the default is localhost |
| mysql server port | the port of the mysql server | the default is 3306. Almost every mysql server uses this port |
| mysql user for Seafile | the user for Seafile programs to use to access MySQL server | the user must already exists |
| password for Seafile mysql user | the password for the user above | |
| ccnet dabase name | the name of the database used by ccnet | this database must already exist |
| seafile dabase name | the name of the database used by Seafile, default is "seafile-db" | this database must already exist |
| seahub dabase name | the name of the database used by Seahub, default is "seahub-db" | this database must already exist |


If the setup is successful, you'll see the following output

![server-setup-succesfully](../images/Server-setup-successfully.png)

Now you should have the following directory layout :
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

The folder `seafile-server-latest` is a symbolic link to the current Seafile server folder. When later you upgrade to a new version, the upgrade scripts update this link to point to the latest Seafile Server folder.

## Running Seafile Server


### Starting Seafile Server and Seahub Website

Under seafile-server-1.8.2 directory, run the following commands


```
./seafile.sh start # Start Seafile service
./seahub.sh start <port>  # Start seahub website, port defaults to 8000
```

Note: The first time you start Seahub, the script would prompt you to create an admin account for your Seafile Server.

After starting the services, you may open a web browser and visit Seafile web interface at (assume your server IP is 192.168.1.111):

```
http://192.168.1.111:8000/
```


Congratulations! Now you have successfully setup your private Seafile Server.


#### Run Seahub on another port

If you want to run Seahub on a port other than the default 8000, say 8001, you must:

**Seafile 6.2.x and previous versions**

- stop the Seafile server
```
./seahub.sh stop
./seafile.sh stop
```

- modify the value of SERVICE_URL in the file [ccnet.conf](../config/ccnet-conf.md), like this: (assume your ip or domain is 192.168.1.100). You can also modify SERVICE_URL via web UI in "System Admin->Settings". (**Warning**: if you set the value both via Web UI and ccnet.conf, the setting via Web UI will take precedence.)

```
SERVICE_URL = http://192.168.1.100:8001
```

- restart Seafile server
```
./seafile.sh start
./seahub.sh start 8001
```

See Seafile [Server Configuration Manual](../config/ccnet-conf.md) for more details about ``ccnet.conf``.

**Seafile 6.3.x and above versions**

At Seafile 6.3.x, you could't simply run Seahub on another port by `./seahub.sh start <port>`. But you can assign the port of seahub by setting the `conf/gunicorn.conf`.

- stop the Seafile server
```
./seahub.sh stop
./seafile.sh stop
```

- modify the value of SERVICE_URL in the file [ccnet.conf](../config/ccnet-conf.md), like this: (assume your ip or domain is 192.168.1.100). You can also modify SERVICE_URL via web UI in "System Admin->Settings". (**Warning**: if you set the value both via Web UI and ccnet.conf, the setting via Web UI will take precedence.)

```
SERVICE_URL = http://192.168.1.100:8001
```

- **modify the conf/gunicorn.conf**

```
# default localhost:8000
bind = "0.0.0.0:8001"
```

- restart Seafile server
```
./seafile.sh start
./seahub.sh start
```

See Seafile [Server Configuration Manual](../config/ccnet-conf.md) for more details about ``ccnet.conf``.

## Stopping and Restarting Seafile and Seahub

#### Stopping

```
./seahub.sh stop # stop Seahub website
./seafile.sh stop # stop Seafile processes
```

#### Restarting

```
./seafile.sh restart
./seahub.sh restart
```

#### When the Scripts Fail

Most of the time, seafile.sh and seahub.sh work fine. But if they fail, you may

* Use `pgrep` command to check if seafile/seahub processes are still running

```
pgrep -f seafile-controller # check seafile processes
pgrep -f "seahub" # check seahub process
```

* Use `pkill` to kill the processes

```
pkill -f seafile-controller
pkill -f "seahub"
```

## Performance turning

If you have more than 50 users, we highly recommand you to [add memcached](../deploy/add_memcached.md). This is going to greatly speed up Seahub (the web frontend).  

## Setup in non-interactive way

Since Seafile Pro Edition version 5.1.4, `setup-seafile-mysql.sh` supports auto mode. You can run the setup script in non-interactive by supplying the needed parameters via script parameters or environment variables.

```sh
cd seafile-server-*
./setup-seafile-mysql.sh auto [param1] [param2]...
```

Related parameters as follow:

Option | Script parameter | Environment variable | Default value
--------|--------|--------|--------
server name | -n | SERVER_NAME | hostname -s(short host name)
server ip or domain | -i | SERVER_IP | hostname -i(address for the host name)
fileserver port | -p | FILESERVER_PORT | 8082
seafile data dir | -d | SEAFILE_DIR | current directory
use existing db | -e | USE_EXISTING_DB | 0(create new db)
mysql server host | -o | MYSQL_HOST | 127.0.0.1
mysql server port | -t | MYSQL_PORT | 3306
mysql root password | -r | MYSQL_ROOT_PASSWD | no default value(must be set when create new db)
mysql user for seafile | -u | MYSQL_USER | no default value(must be set)
password for seafile mysql user | -w | MYSQL_USER_PASSWD | no default value(must be set)
mysql user host | -q | MYSQL_USER_HOST | no default value(must be set when create new db and using non local mysql server)
ccnet dabase name | -c | CCNET_DB | ccnet-db
seafile dabase name | -s | SEAFILE_DB | seafile-db
seahub dabase name | -b | SEAHUB_DB | seahub-db

**Note: If both script parameter and environment variable assigned, script parameter has higher priority. If neither script parameter nor environment variable assigned, default value will be used.**

## That's it!

That's it! Now you may want read more about Seafile.


* [Deploy Seafile with Nginx](deploy_with_nginx.md) / [Deploy Seafile with Apache](deploy_with_apache.md)
* [Enable Https on Seafile Web with Nginx](https_with_nginx.md) / [Enable Https on Seafile Web with Apache](https_with_apache.md)
* [Configure Seafile to use LDAP](using_ldap.md)
* [How to manage the server](../maintain/README.md)
