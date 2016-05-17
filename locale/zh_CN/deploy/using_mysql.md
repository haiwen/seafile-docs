# 部署 Seafile 服务器（使用 MySQL）

本文档用来说明通过预编译好的安装包来安装并运行基于 MySQL 的 Seafile 服务器。

## Download

到[下载页面](http://www.seafile.com/download)下载最新的服务器安装包.


## Deploying and Directory Layout

假设你公司的名称为 "haiwen", 你也已经下载 `seafile-server_1.8.2_*` 到你的 home 目录下。 我们建议这样的目录结构:

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

## Prepare MySQL Databases

Three components of Seafile Server need their own databases:

* ccnet server
* seafile server
* seahub

See [Seafile Server Components Overview](components.md) if you want to know more about the seafile server components.

There are two ways to intialize the databases:

- let the <code>setup-seafile-mysql.sh</code> script create the databases for you.
- create the databases by yourself, or someone else (the database admin, for example)

We recommend the first way. The script would ask you for the root password of the mysql server, and it will create:

* database for ccnet/seafile/seahub.
* a new user to access these databases

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

## Setting Up Seafile Server

### 安装前的准备工作

The Seafile server package requires the following packages have been installed in your system

* python 2.7
* python-setuptools
* python-imaging
* python-ldap
* python-mysqldb
* python-memcache (或者 python-memcached)

<pre>
# 在Debian/Ubuntu系统下
apt-get update
apt-get install python2.7 libpython2.7 python-setuptools python-imaging \
  python-ldap python-mysqldb python-memcache
</pre>

<pre>
# 在 CentOS 7 下
sudo yum install python-imaging MySQL-python python-memcached python-ldap
</pre>

### 安装

<pre>
cd seafile-server-*
./setup-seafile-mysql.sh  #run the setup script & answer prompted questions
</pre>

If some of the prerequisites are not installed, the seafile initialization script will ask you to install them.

The script will guide you through the settings of various configuration options.

** Seafile configuration options **

| 参数 | 作用 | 说明 |
| -- | -- | ---- |
| server name | seafile 服务器的名字，目前该配置已经不再使用 | 3 ~ 15 个字符，可以用英文字母，数字，下划线 |
| server ip or domain | seafile 服务器的 IP 地址或者域名 | 客户端将通过这个 IP 或者地址来访问你的 Seafile 服务 |
| seafile data dir | seafile 数据存放的目录，用上面的例子，默认将是 /data/haiwen/seafile-data  | seafile 数据将随着使用而逐渐增加，请把它放在一个有足够大空闲空间的分区上  |
| fileserver port | seafile fileserver 使用的 TCP 端口 | 该端口用于文件同步，请使用默认的 8082，不能更改。  |


在这里, 你会被要求选择一种创建 Seafile 数据库的方式:

```sh
-------------------------------------------------------
Please choose a way to initialize seafile databases:
-------------------------------------------------------

[1] Create new ccnet/seafile/seahub databases
[2] Use existing ccnet/seafile/seahub databases

```


Which one to choose depends on if you have the root password.

* 如果选择 "1", 你需要提供根密码. 脚本程序会创建数据库和用户。
* 如果选择 "2", ccnet/seafile/seahub 数据库应该已经被你（或者其他人）提前创建。

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

| Question | Description | Note
| -- | -- | ---- |
| mysql server host | the host address of the mysql server | the default is localhost |
| mysql server port | the port of the mysql server | the default is 3306. Almost every mysql server uses this port |
| mysql user for seafile | the user for seafile programs to use to access MySQL server | the user must already exists |
| password for seafile mysql user | the password for the user above | |
| ccnet dabase name | the name of the database used by ccnet | this database must already exist |
| seafile dabase name | the name of the database used by seafile, default is "seafile-db" | this database must already exist |
| seahub dabase name | the name of the database used by seahub, default is "seahub-db" | this database must already exist |


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

The folder <code>seafile-server-latest</code> is a symbolic link to the current seafile server folder. When later you upgrade to a new version, the upgrade scripts would update this link to keep it always point to the latest seafile server folder.

## Running Seafile Server


### 启动 Seafile 服务器和 Seahub 网站

在 seafile-server-1.8.2 目录下，运行如下命令


```
./seafile.sh start # 启动 Seafile 服务
./seahub.sh start <port>  # 启动 Seahub 网站 （默认运行在8000端口上）
```

小贴士: 你第一次启动 seahub 时，seahub.sh 脚本会提示你创建一个 seafile 管理员帐号。

After starting the services, you may open a web browser and visit Seafile web interface at (assume your server IP is 192.168.1.111):

```
http://192.168.1.111:8000/
```


恭喜! 现在你已经成功的安装了 Seafile 服务器.


### 在另一端口上运行 Seahub

If you want to run seahub in a port other than the default 8000, say 8001, you must:

* stop the seafile server
<pre>
./seahub.sh stop
./seafile.sh stop
</pre>

* modify the value of `SERVICE_URL` in the file [ccnet.conf](../config/ccnet-conf.md), like this: (assume your ip or domain is `192.168.1.111`)
<pre>
SERVICE_URL = http://192.168.1.111:8001
</pre>

* restart seafile server
<pre>
./seafile.sh start
./seahub.sh start 8001
</pre>

see [Seafile server configuration options](server_configuration.md) for more details about <code>ccnet.conf</code>.

## Stopping and Restarting Seafile and Seahub

#### Stopping

<pre>
./seahub.sh stop # stop seahub website
./seafile.sh stop # stop seafile processes
</pre>

#### Restarting

<pre>
./seafile.sh restart
./seahub.sh restart
</pre>

#### When the Scripts Fail

Most of the time, seafile.sh and seahub.sh work fine. But if they fail, you may

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

## Performance turning

If you have more than 50 users in your Seafile system, we highly recommand you to [add memcached](../deploy/add_memcached.md). This will make the web 10x faster.  

## That's it!

That's it! Now you may want read more about seafile.


* [Nginx 下配置 Seafile](deploy_with_nginx.md) / [Apache 下配置 Seafile](deploy_with_apache.md)
* [Enable Https on Seafile Web with Nginx](https_with_nginx.md) / [Enable Https on Seafile Web with Apache](https_with_apache.md)
* [Seafile LDAP 配置](using_ldap.md)
* [管理员手册](../maintain/README.md)

