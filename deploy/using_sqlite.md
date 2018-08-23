# Deploying Seafile with SQLite

## Download binary package

Visit our [download page](http://www.seafile.com/en/download/#server),  download the latest server package.

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

 - We can place all the config files for Seafile server inside "haiwen" directory, making it easier to manage.
 - When you upgrade to a new version of Seafile, you can simply untar the latest package into "haiwen" directory. In this way you can reuse the existing config files in "haiwen" directory and don't need to configure again.


## Setting Up Seafile Server
#### Prerequisites

The Seafile server package requires the following packages have been installed in your system

- python 2.7
- python-setuptools
- python-imaging
- python-ldap
- python-urllib3
- python-requests
- sqlite3

```
#on Debian/Ubuntu 14.04 server
apt-get update
apt-get install python2.7 libpython2.7 python-setuptools python-imaging python-ldap python-urllib3 sqlite3 python-requests
```

```
# on Ubuntu 16.04 server
# As the default python binary on Ubuntu 16.04 server is python 3, we need to install python (python 2) first.
apt-get update
apt-get install python
apt-get install python2.7 libpython2.7 python-setuptools python-imaging python-ldap python-urllib3 ffmpeg python-pip sqlite3 python-requests
pip install pillow moviepy
```

```
# on CentOS 7
yum -y install epel-release
rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
yum -y install python-imaging MySQL-python python-memcached python-ldap python-urllib3 ffmpeg ffmpeg-devel python-requests
pip install pillow moviepy
```

#### Setup

```sh
cd seafile-server-*
./setup-seafile.sh  #run the setup script & answer prompted questions
```

If some of the prerequisites are not installed, the Seafile initialization script will ask you to install them.

The script will guide you through the settings of various configuration options.

**Seafile configuration options**

| Option | Description | Note |
| -- | -- | ---- |
| server name | Name of this Seafile server | 3-15 characters, only English letters, digits and underscore ('_') are allowed |
| server ip or domain  | The IP address or domain name used by this server  | Seafile client program will access the server with this address |
| Seafile data dir  | Seafile stores your data in this directory. By default it'll be placed in the current directory.  | The size of this directory will increase as you put more and more data into Seafile. Please select a disk partition with enough free space. |
| fileserver port | The TCP port used by Seafile fileserver  | Default is 8082. If it's been used by other service, you can set it to another port. |


Now you should have the following directory layout:

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

The folder seafile-server-latest is a symbolic link to the current Seafile server folder. When later you upgrade to a new version, the upgrade scripts would update this link to keep it always point to the latest Seafile server folder.

## Running Seafile Server

#### Before Running

Since Seafile uses persistent connections between client and server, you should increase Linux file descriptors by ulimit if you have a large number of clients before start Seafile, like:

``ulimit -n 30000``

#### Starting Seafile Server and Seahub Website

- Start Seafile:
```
./seafile.sh start # Start Seafile service
```

- Start Seahub:
```
./seahub.sh start <port>  # Start Seahub website, port defaults to 8000
```

**Note**: The first time you start Seahub, the script is going to prompt you to create an admin account for your Seafile server.

After starting the services, you may open a web browser and type in

``http://192.168.1.111:8000``

you will be redirected to the Login page. Just enter the admin username and password.

**Congratulations!** Now you have successfully setup your private Seafile server.

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

You can assign the port of Seahub by setting the `conf/gunicorn.conf`.

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

## Manage Seafile and Seahub
#### Stopping
```
./seahub.sh stop # stop seahub website
./seafile.sh stop # stop seafile processes
```
#### Restarting
```
./seafile.sh restart
./seahub.sh restart
```
#### When the Scripts Fail

Most of the time, `seafile.sh` and `seahub.sh` work fine. But if they fail, you might want to

- Use pgrep command to check if Seafile/Seahub processes are still running
```
pgrep -f seafile-controller # check Seafile processes
pgrep -f "seahub" # check Seahub process
```

- Use pkill to kill the processes
```
pkill -f seafile-controller
pkill -f "seahub"
```

## Setup in non-interactive way

Since Seafile version 5.1.4, `setup-seafile.sh` supports auto mode. You can run the setup script in non-interactive by supply the needed parameters via script parameters or environment variables.

```sh
cd seafile-server-*
./setup-seafile.sh auto [param1] [param2]...
```

Related parameters as follow:

Option | Script parameter | Environment variable | Default value
--------|--------|--------|--------
server name | -n | SERVER_NAME | hostname -s(short host name)
server ip or domain | -i |SERVER_IP | hostname -i(address for the host name)
fileserver port | -p | FILESERVER_PORT | 8082
seafile data dir | -d | SEAFILE_DIR | current directory

**Note: If both script parameter and environment variable assigned, script parameter has higher priority. If neither script parameter nor environment variable assigned, default value will be used.**

## That's it!
For a production server we highly recommend to setup with Nginx/Apache and enable SSL/TLS.

That's it! Now you might want read more about Seafile.
- [Administration](../maintain/README.md)
