# Setup Seafile Server Development Environment

The following operations have been tested on ubuntu-16.04.1-desktop-amd64 system.

## Install Necessary Packages

#### install necessary packages by `apt`

```
sudo apt install ssh libevent-dev libcurl4-openssl-dev libglib2.0-dev uuid-dev intltool libsqlite3-dev libmysqlclient-dev libarchive-dev libtool libjansson-dev valac libfuse-dev python-dateutil cmake re2c flex sqlite3 python-pip python-simplejson git libssl-dev libldap2-dev libonig-dev
```

#### install `libevhtp` from source

```
cd ~/Downloads/
git clone https://github.com/haiwen/libevhtp.git
cd libevhtp/
cmake -DEVHTP_DISABLE_SSL=ON -DEVHTP_BUILD_SHARED=OFF .
make
sudo make install
sudo ldconfig
```

## Download and Build Seafile

#### create project root directory *dev*

```
cd
mkdir dev
```

#### download and install `libsearpc`

```
cd ~/dev/
git clone https://github.com/haiwen/libsearpc.git
cd libsearpc/
./autogen.sh
./configure
make
sudo make install
sudo ldconfig
```

#### download and install `ccnet-server`

```
cd ~/dev/
git clone https://github.com/haiwen/ccnet-server.git
cd ccnet-server/
./autogen.sh
./configure --enable-ldap
make
sudo make install
sudo ldconfig
```

#### download and install `seafile-server`

```
cd ~/dev/
git clone https://github.com/haiwen/seafile-server.git
cd seafile-server/
./autogen.sh
./configure
make
sudo make install
```

#### download `seahub`

```
cd ~/dev/
git clone https://github.com/haiwen/seahub.git
cd seahub/
```

## Start `ccnet-server` and `seaf-server`

Start `ccnet-server` and `seaf-server` in two separate terminals.

```
cd ~/dev/seafile-server/tests
ccnet-server -c conf -f -
```

```
cd ~/dev/seafile-server/tests
mkdir -p conf/seafile-data
touch seafile-data/seafile.conf
seaf-server -c conf -d conf/seafile-data -f -l -
```

The config files and databases (if you use sqlite, which is by default) of `ccnet-server` are located in `~/dev/seafile-server/tests/conf`. This directory is called "ccnet conf directory". The config files, databases and data of `seaf-server` are located in `~/dev/seafile-server/tests/conf/seafile-data`. This directory is called "seafile conf directory". 

## Start `seahub`

`Seahub` is the web front end of Seafile. It is written in the Django framework, requires Python 2.7 installed on your server.

#### set environment

```
cd ~/dev/seahub/

cat > setenv.sh << EOF
export CCNET_CONF_DIR=~/dev/seafile-server/tests/conf
export SEAFILE_CONF_DIR=~/dev/seafile-server/tests/conf/seafile-data
export PYTHONPATH=/usr/local/lib/python2.7/dist-packages:thirdpart:\$PYTHONPATH
EOF

sudo chmod u+x setenv.sh
```

#### install requirements

```
# Expand setenv.sh in the current shell
. setenv.sh
cd ~/dev/seahub/
sudo pip install -r requirements.txt
```

**NOTE**: if *locale.Error: unsupported locale setting*, you should `export LC_ALL=en_US.UTF-8`

#### create database and admin account

```
. setenv.sh
python manage.py migrate
python tools/seahub-admin.py # create admin account
```

**NOTE**: currently, your *ccnet directory* is `~/dev/seafile-server/tests/conf`

#### run `seahub`

```
python manage.py runserver 0.0.0.0:8000
```

then open browser and navigate to http://127.0.0.1:8000

If you have set up Nginx/Apache to run Seafile, you should run seahub in fastcgi mode.

```
python manage.py runfcgi host=127.0.0.1 port=8000
```
