# 部署 Seafile 服务器（使用 SQLite）

## 下载

到[下载页面](http://www.seafile.com/en/download/#server)下载最新的服务器安装包.

Choose one of:
- Generic Linux
- Windows
- Server for Raspberry Pi

```
#check if your system is x86 (32bit) or x86_64 (64 bit)
uname -m
```
Click the tarball link and save it.


## Deploying and Directory Layout

NOTE: If you place the Seafile data directory in external storage, such as NFS, CIFS mount, you should not use SQLite as the database, but use MySQL instead.

Supposed your organization's name is "haiwen", and you've downloaded seafile-server_1.4.0_* into your home directory. We suggest you to use the following layout for your deployment:
```sh
mkdir haiwen
mv seafile-server_* haiwen
cd haiwen
# after moving seafile-server_* to this directory
tar -xzf seafile-server_*
mkdir installed
mv seafile-server_* installed
```

Now you should have the following directory layout
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

Benefits of this layout are

- 和 seafile 相关的配置文件都放在 "haiwen" 目录下，便于集中管理.
 - When you upgrade to a new version of Seafile, you can simply untar the latest package into "haiwen" directory. In this way you can reuse the existing config files in "haiwen" directory and don't need to configure again.


## Setting Up Seafile Server
#### Prerequisites

The Seafile server package requires the following packages have been installed in your system

- python 2.7
- python-setuptools
- python-imaging
- python-ldap
- sqlite3

```
#Debian系统下
apt-get update
apt-get install python2.7 libpython2.7 python-setuptools python-imaging python-ldap sqlite3
```

```
# 在 CentOS 7 下
sudo yum install python-imaging MySQL-python python-memcached python-ldap
```

#### Setup

```sh
cd seafile-server-*
./setup-seafile.sh  #运行安装脚本并回答预设问题
```

If some of the prerequisites are not installed, the Seafile initialization script will ask you to install them.

The script will guide you through the settings of various configuration options.

**Seafile configuration options**

| 参数 | 作用 | 说明 |
| -- | -- | ---- |
| server name | Name of this Seafile server | 3-15 characters, only English letters, digits and underscore ('_') are allowed |
| server ip or domain  | The IP address or domain name used by this server  | Seafile client program will access the server with this address |
| Seafile data dir  | Seafile stores your data in this directory. By default it'll be placed in the current directory.  | The size of this directory will increase as you put more and more data into Seafile. Please select a disk partition with enough free space. |
| fileserver port | The TCP port used by Seafile fileserver  | Default is 8082. If it's been used by other service, you can set it to another port. |


现在你的目录结构将会是如下:

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

seafile-server-latest文件夹是当前 Seafile 服务器文件夹的符号链接.将来你升级到新版本后, 升级脚本会自动更新使其始终指向最新的 Seafile 服务器文件夹.

## Running Seafile Server

#### Before Running

Since Seafile uses persistent connections between client and server, you should increase Linux file descriptors by ulimit if you have a large number of clients before start Seafile, like:

``ulimit -n 30000``

#### Starting Seafile Server and Seahub Website

- 启动 Seafile:
```
./seafile.sh start # 启动 Seafile 服务
```

- 启动 Seahub:
```
./seahub.sh start <port>  # 启动 Seahub 网站 （默认运行在8000端口上）
```

**Note**: The first time you start Seahub, the script is going to prompt you to create an admin account for your Seafile server.

服务启动后, 打开浏览器并输入以下地址

``http://192.168.1.111:8000``

you will be redirected to the Login page. Just enter the admin username and password.

**恭喜!** 现在你已经成功的安装了 Seafile 服务器.

#### Run Seahub on another port

If you want to run Seahub on a port other than the default 8000, say 8001, you must:

- 关闭 Seafile 服务器
```
./seahub.sh stop
./seafile.sh stop
```

- 更改 [haiwen/conf/ccnet.conf](../config/ccnet-conf.md)文件中SERVICE_URL 的值(假设你的 ip 或者域名时192.168.1.100), 如下 (从 5.0 版本开始，可以直接在管理员界面中设置):
```
SERVICE_URL = http://192.168.1.100:8001
```

- 重启 Seafile 服务器
```
./seafile.sh start
./seahub.sh start 8001
```

See Seafile [Server Configuration Manual](deploy/server_configuration.md) for more details about ``ccnet.conf``.

## Manage Seafile and Seahub
#### Stopping
```
./seahub.sh stop # 停止 Seahub
./seafile.sh stop # 停止 Seafile 进程
```
#### Restarting
```
./seafile.sh restart
./seahub.sh restart
```
#### When the Scripts Fail

大多数情况下 `seafile.sh`, `seahub.sh` 脚本可以正常工作。如果遇到问题：

- 使用 pgrep 命令检查 seafile/seahub 进程是否还在运行中
```
pgrep -f seafile-controller # 查看 Seafile 进程
pgrep -f "manage.py run_gunicorn" # 查看 Seahub 进程
```

- 使用 pkill 命令杀掉相关进程
```
pkill -f seafile-controller
pkill -f "manage.py run_gunicorn"
```

## That's it!
For a production server we highly recommend to setup with Nginx/Apache and enable SSL/TLS.

That's it! Now you might want read more about Seafile.
- [Administration](../maintain/README.md)

