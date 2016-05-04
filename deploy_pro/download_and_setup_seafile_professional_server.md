# Download and Setup Seafile Professional Server
## <a id="wiki-preparation"></a>Preparation ##

The following document is tested in Ubuntu 14.04 and CentOS 7. We recommend that you use Ubuntu 14.04 or CentOS 7 as your server.

> NOTE:
>
> If you are using Ubuntu 14.04, you can use the following command to install all the dependency that Seafile requires at one time.
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
> For more information please see bellow.

### Minimum System Requirement ###

- A Linux server with 2GB RAM

### Install Java Runtime Environment (JRE) ###

On Ubuntu/Debian:
```
sudo apt-get install openjdk-7-jre
```

On CentOS/Red Hat:
```
sudo yum install java-1.7.0-openjdk
```

### Install poppler-utils ###

We need poppler-utils for full text search of pdf files.

On Ubuntu/Debian:
```
sudo apt-get install poppler-utils
```

On CentOS/Red Hat:
```
sudo yum install poppler-utils
```


### Install Python libraries ###

First make sure your have installed python 2.7
```
sudo easy_install pip
sudo pip install boto
```

If you receive an error about "Wheel installs require setuptools >= ...", run this between the pip and boto lines above
```
sudo pip install setuptools --no-use-wheel --upgrade
```

### Install libpython2.7 if you use Ubuntu 14.04

```
sudo apt-get install libpython2.7
```

### Install other libraries as required in the community edition

See [Download and Setup Seafile Server With MySQL](../deploy/using_mysql.md).

## <a id="wiki-download-and-setup"></a>Download and Setup Seafile Professional Server ##

### Get the license ###

Put the license you get under the top level diretory. In our wiki, we use the diretory `/data/haiwen/` as the top level directory.


### <a id="wiki-download-and-uncompress"></a>Download/Uncompress Seafile Professional Server ###


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

If you have any problem in setting up the service, please check [Common problems in setting up Seafile server](../deploy/common_problems_for_setting_up_server.md).

After you have succesfully setup Seafile Professional Server, you would have a directory layout like this:

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

If you have more than 50 users in your Seafile system, we highly recommand you to [add memcached](../deploy/add_memcached.md). This will make the web 10x faster.  

## <a id="wiki-done"></a>Done

At this point, the basic setup of Seafile Professional Server is done.

You may want to read more about Seafile Professional Server:

- [FAQ For Seafile Professional Server](faq_for_seafile_pro_server.md)
