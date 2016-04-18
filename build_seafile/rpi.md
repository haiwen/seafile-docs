# How to Build Seafile Server Release Package for Raspberry Pi

*Table of contents*:

- [Setup the build environment](#wiki-setup-build-env)
  - [Install packages](#wiki-install-packages)
  - [Compile development libraries](#wiki-compile-dev-libs)
  - [Install Python libraries](#wiki-install-python-libs)
- [Prepare source code](#wiki-prepare-seafile-source-code)
  - [Fetch git tags and prepare source tarballs](#wiki-fetch-tags-and-prepare-tarballs)
  - [Run the packaging script](#wiki-run-pkg-script)
- [Test the built package](#wiki-test-built-pkg)
  - [Test a fresh install](#wiki-test-fresh-install)
  - [Test upgrading](#wiki-test-upgrading)

## <a id="wiki-setup-build-env"></a>Setup the build environment

Requirements:

- A raspberry pi with raspian distribution installed.

### <a id="wiki-install-packages"></a> Install packages

```
sudo apt-get install build-essential
sudo apt-get install libevent-dev libcurl4-openssl-dev libglib2.0-dev uuid-dev intltool libsqlite3-dev libmysqlclient-dev libarchive-dev libtool libjansson-dev valac libfuse-dev re2c flex python-setuptools cmake
```
### <a id="wiki-compile-dev-libs"></a> Compile development libraries

#### libevhtp

libevhtp is a http server libary on top of libevent. It's used in seafile file server.

```
git clone https://www.github.com/haiwen/libevhtp.git
cd libevhtp
cmake -DEVHTP_DISABLE_SSL=OFF -DEVHTP_BUILD_SHARED=ON .
make
sudo make install
```

#### libzdb

`libzdb` provides a consistent API to various database backends, including sqlite/mysql/pg/oracle. It's used by ccnet-server and seafile-server.

```
git clone https://www.github.com/haiwen/libzdb.git
cd libzdb
./autogen.sh
./configure
make
sudo make install
```

After compiling all the libraries, run `ldconfig` to update the system libraries cache:

```
sudo ldconfig
```

### <a id="wiki-install-python-libs"></a> Install python libraries


Create a new directory `/home/pi/dev/seahub_thirdpart`:

```
mkdir -p ~/dev/seahub_thirdpart
```

Download these tarballs to `/tmp/`:

- [pytz](https://pypi.python.org/packages/source/p/pytz/pytz-2016.1.tar.gz)
- [Django](https://www.djangoproject.com/m/releases/1.8/Django-1.8.10.tar.gz)
- [django-statici18n](https://pypi.python.org/packages/source/d/django-statici18n/django-statici18n-1.1.3.tar.gz)
- [djangorestframework](https://pypi.python.org/packages/source/d/djangorestframework/djangorestframework-3.3.2.tar.gz)
- [django_compressor](https://pypi.python.org/packages/source/d/django_compressor/django_compressor-1.4.tar.gz)
- [jsonfield](https://pypi.python.org/packages/source/j/jsonfield/jsonfield-1.0.3.tar.gz)
- [django-post_office](https://pypi.python.org/packages/source/d/django-post_office/django-post_office-2.0.6.tar.gz)
- [gunicorn](http://pypi.python.org/packages/source/g/gunicorn/gunicorn-19.4.5.tar.gz)
- [flup](http://pypi.python.org/packages/source/f/flup/flup-1.0.2.tar.gz)
- [chardet](https://pypi.python.org/packages/source/c/chardet/chardet-2.3.0.tar.gz)
- [python-dateutil](https://labix.org/download/python-dateutil/python-dateutil-1.5.tar.gz)
- [six](https://pypi.python.org/packages/source/s/six/six-1.9.0.tar.gz)
- [django-picklefield](https://pypi.python.org/packages/source/d/django-picklefield/django-picklefield-0.3.2.tar.gz)
- [django-constance](https://github.com/haiwen/django-constance/archive/bde7f7c.zip)
- [jdcal](https://pypi.python.org/packages/source/j/jdcal/jdcal-1.2.tar.gz)
- [et_xmlfile](https://pypi.python.org/packages/source/e/et_xmlfile/et_xmlfile-1.0.1.tar.gz)
- [openpyxl](https://pypi.python.org/packages/source/o/openpyxl/openpyxl-2.3.0.tar.gz)

Install all these libaries to `/home/pi/dev/seahub_thirdpart`:

```
cd ~/dev/seahub_thirdpart
export PYTHONPATH=.
easy_install -d . /tmp/pytz-2016.1.tar.gz
easy_install -d . /tmp/Django-1.8.10.tar.gz
easy_install -d . /tmp/django-statici18n-1.1.3.tar.gz
easy_install -d . /tmp/djangorestframework-3.3.2.tar.gz
easy_install -d . /tmp/django_compressor-1.4.tar.gz
easy_install -d . /tmp/jsonfield-1.0.3.tar.gz
easy_install -d . /tmp/django-post_office-2.0.6.tar.gz
easy_install -d . /tmp/gunicorn-19.4.5.tar.gz
easy_install -d . /tmp/flup-1.0.2.tar.gz
easy_install -d . /tmp/chardet-2.3.0.tar.gz
easy_install -d . /tmp/python-dateutil-1.5.tar.gz
easy_install -d . /tmp/six-1.9.0.tar.gz
easy_install -d . /tmp/django-picklefield-0.3.2.tar.gz
wget -O /tmp/django_constance.zip https://github.com/haiwen/django-constance/archive/bde7f7c.zip
easy_install -d . /tmp/django_constance.zip
easy_install -d . /tmp/jdcal-1.2.tar.gz
easy_install -d . /tmp/et_xmlfile-1.0.1.tar.gz
easy_install -d . /tmp/openpyxl-2.3.0.tar.gz
```

## <a id="wiki-prepare-seafile-source-code"></a>Prepare seafile source code

To build seafile server, there are four sub projects involved:

- [libsearpc](https://github.com/haiwen/libsearpc)
- [ccnet](https://github.com/haiwen/ccnet)
- [seafile](https://github.com/haiwen/seafile)
- [seahub](https://github.com/haiwen/seahub)

The build process has two steps:

- First, fetch the tags of each projects, and make a soruce tarball for each of them.
- Then run a `build-server.py` script to build the server package from the source tarballs.

### <a id="wiki-fetch-tags-and-prepare-tarballs"></a> Fetch git tags and prepare source tarballs

Seafile manages the releases in tags on github.

Assume we are packaging for seafile server 4.1.1, then the tags are:

- ccnet, seafile, and seahub would all have a `v4.1.1-sever` tag.
- libsearpc would have the `v3.0-latest` tag (libsearpc has been quite stable and basically has no further development, so the tag is always `v3.0-latest`)

First setup the `PKG_CONFIG_PATH` enviroment variable (So we don't need to make and make install libsearpc/ccnet/seafile into the system):

```
export PKG_CONFIG_PATH=/home/pi/dev/seafile/lib:$PKG_CONFIG_PATH
export PKG_CONFIG_PATH=/home/pi/dev/libsearpc:$PKG_CONFIG_PATH
export PKG_CONFIG_PATH=/home/pi/dev/ccnet:$PKG_CONFIG_PATH
```


### libsearpc

```
cd ~/dev
git clone https://github.com/haiwen/libsearpc.git
cd libsearpc
git reset --hard v3.0-latest
./autogen.sh
./configure
make dist
```

### ccnet

```
cd ~/dev
git clone https://github.com/haiwen/ccnet.git
cd ccnet
git reset --hard v4.1.1-server
./autogen.sh
./configure
make dist
```

### seafile

```
cd ~/dev
git clone https://github.com/haiwen/seafile.git
cd seafile
git reset --hard v4.1.1-server
./autogen.sh
./configure
make dist
```

### seahub

```
cd ~/dev
git clone https://github.com/haiwen/seahub.git
cd seahub
git reset --hard v4.1.1-server
./tools/gen-tarball.py --version=4.1.1 --branch=HEAD
```

### seafobj

```
cd ~/dev
git clone https://github.com/haiwen/seafobj.git
cd seafobj
git reset --hard v4.1.1-server
make dist
```

### seafdav

```
cd ~/dev
git clone https://github.com/haiwen/seafdav.git
cd seafdav
git reset --hard v4.1.1-server
make
```

### Copy the source tar balls to the same folder

```
mkdir ~/seafile-sources
cp ~/dev/libsearpc/libsearpc-<version>-tar.gz ~/seafile-sources
cp ~/dev/ccnet/ccnet-<version>-tar.gz ~/seafile-sources
cp ~/dev/seafile/seafile-<version>-tar.gz ~/seafile-sources
cp ~/dev/seahub/seahub-<version>-tar.gz ~/seafile-sources

cp ~/dev/seafobj/seafobj.tar.gz ~/seafile-sources
cp ~/dev/seafdav/seafdav.tar.gz ~/seafile-sources
```

### <a id="wiki-run-pkg-script"></a> Run the packaging script

Now we have all the tarballs prepared, we can run the `build-server.py` script to build the server package.

```
mkdir ~/seafile-server-pkgs
~/dev/seafile/scripts/build-server.py --libsearpc_version=<libsearpc_version> --ccnet_version=<ccnet_version> --seafile_version=<seafile_version> --seahub_version=<seahub_version> --srcdir=  --thidrpartdir=/home/pi/dev/seahub_thirdpart --srcdir=/home/pi/seafile-sources --outputdir=/home/pi/seafile-server-pkgs
```

After the script finisheds, we would get a `seafile-server_4.1.1_pi.tar.gz` in `~/seafile-server-pkgs` folder.

## <a id="wiki-test-built-pkg"></a> Test the built package

### <a id="wiki-test-fresh-install"></a>Test a fresh install

Use the built seafile server package to go over the steps of [Deploying Seafile with SQLite](http://manual.seafile.com/deploy/using_sqlite.html).

The test should cover these steps at least:

- The setup process is ok
- After `seafile.sh start` and `seahub.sh start`, you can login from a browser.
- Uploading/Downloading files through a web browser works correctly.
- Seafile [WebDAV](http://manual.seafile.com/extension/webdav.html) server works correctly

### <a id="wiki-test-upgrading"></a> Test upgrading from a previous version

- Download the package of the previous version seafile server, and setup it.
- Upgrading according to [the manual](http://manual.seafile.com/deploy/upgrade.html)
- After the upgrade, check the functionality is ok:
  - Uploading/Downloading files through a web browser works correctly.
  - Seafile [WebDAV](http://manual.seafile.com/extension/webdav.html) server works correctly
