# Download and Setup Seafile Professional Server

## <a id="wiki-preparation"></a>Preparation ##

The following document is tested with Ubuntu 16.04 and CentOS 7. We recommend that use Ubuntu 16.04 or CentOS 7 for your server.

Now when we release a new version, we will always provide 2 compressed files, for example:

- *seafile-pro-server_6.3.1_x86-64_Ubuntu.tar.gz*, is compiled in Ubuntu 16.04 enviroment.

- *seafile-pro-server_6.3.1_x86-64_CentOS.tar.gz*, is compiled in CentOS 7 enviroment.

If you are using Ubuntu 16.04/Debian server, please use *seafile-pro-server_6.3.1_x86-64_Ubuntu.tar.gz*, for CentOS 7 please use *seafile-pro-server_6.3.1_x86-64_CentOS.tar.gz*.

### Install thirdpart Requirements

For Ubuntu 16.04:

```
sudo apt-get install openjdk-8-jre poppler-utils libpython2.7 python-pip \
mysql-server python-setuptools python-imaging python-mysqldb python-memcache python-ldap \
python-urllib3

sudo pip install boto requests
sudo ln -sf /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java /usr/bin/
```

For CentOS 7:

```
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo yum install java-1.7.0-openjdk poppler-utils python-setuptools \
python-imaging MySQL-python mariadb-server python-memcached python-ldap \
python-urllib3

sudo pip install boto requests
sudo /etc/init.d/mysqld start
```

For more information please see bellow.

### Minimum System Requirements ###

- A Linux server with 2GB RAM

### Install Java Runtime Environment (JRE) ###

On Debian:
```
sudo apt-get install openjdk-7-jre
```

On Ubuntu 16.04:
```
sudo apt-get install openjdk-8-jre
sudo ln -sf /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java /usr/bin/
```

On CentOS/Red Hat:
```
sudo yum install java-1.7.0-openjdk
```

### Install poppler-utils ###

The package poppler-utils is required for full text search of pdf files.

On Ubuntu/Debian:
```
sudo apt-get install poppler-utils
```

On CentOS/Red Hat:
```
sudo yum install poppler-utils
```


### Install Python libraries ###

First make sure your have installed Python 2.7
```
sudo easy_install pip
sudo pip install boto
```

If you receive an error about "Wheel installs require setuptools >= ...", run this between the pip and boto lines above
```
sudo pip install setuptools --no-use-wheel --upgrade
```

### Install all libraries required by the Community Edition

See [Download and Setup Seafile Server With MySQL](../deploy/using_mysql.md).

## <a id="wiki-download-and-setup"></a>Download and Setup Seafile Professional Server ##

### Get the license ###

Put the license you got under the top level diretory. In our wiki, we use the diretory `/data/haiwen/` as the top level directory. If you're using the free Pro Edition with three users you don't need a license file.


### <a id="wiki-download-and-uncompress"></a>Download & uncompress Seafile Professional Server ###


```
tar xf seafile-pro-server_1.8.0_x86-64.tar.gz
```

Now you have:

```
haiwen
├── seafile-license.txt
└── seafile-pro-server-1.8.0/
```


-----------

You should notice the difference between the names of the Community Server and Professional Server. Take the 1.8.0 64bit version as an example:

- Seafile Community Server tarball is `seafile-server_1.8.0_x86-86.tar.gz`; After uncompressing, the folder is `seafile-server-1.8.0`
- Seafile Professional Server tarball is `seafile-pro-server_1.8.0_x86-86.tar.gz`; After uncompressing, the folder is `seafile-pro-server-1.8.0`

-----------


### Setup ###

The setup process of Seafile Professional Server is the same as the Seafile Community Server. See [Download and Setup Seafile Server With MySQL](../deploy/using_mysql.md).

If you have any problem with setting up the service, please check [Common problems in setting up Seafile server](../deploy/common_problems_for_setting_up_server.md).

After you have succesfully setup Seafile Professional Server, you have a directory layout like this:

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

## Performance turning

If you have more than 50 Seafile users, we highly recommend to [add memcached](../deploy/add_memcached.md). This is going to speedup Seahub (the web front end) significantly.

## <a id="wiki-done"></a>Done

At this point, the basic setup of Seafile Professional Server is done.

You may want to read more about Seafile Professional Server:

- [FAQ For Seafile Professional Server](faq_for_seafile_pro_server.md)
