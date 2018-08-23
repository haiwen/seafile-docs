# Linux

#### Preparation

The following list is what you need to install on your development machine. __You should install all of them before you build Seafile__.

Package names are according to Ubuntu 14.04. For other Linux distros, please find their corresponding names yourself.

* autoconf/automake/libtool
* libevent-dev ( 2.0 or later )
* libcurl4-openssl-dev  (1.0.0 or later)
* libgtk2.0-dev ( 2.24 or later)
* uuid-dev
* intltool (0.40 or later)
* libsqlite3-dev (3.7 or later)
* valac  (only needed if you build from git repo)
* libjansson-dev
* qtchooser
* qtbase5-dev
* libqt5webkit5-dev
* qttools5-dev
* qttools5-dev-tools
* valac
* cmake
* python-simplejson (for seaf-cli)
* libssl-dev

```bash
sudo apt-get install autoconf automake libtool libevent-dev libcurl4-openssl-dev libgtk2.0-dev uuid-dev intltool libsqlite3-dev valac libjansson-dev cmake qtchooser qtbase5-dev libqt5webkit5-dev qttools5-dev qttools5-dev-tools libssl-dev
```
For a fresh Fedora 20 / 23 installation, the following will install all dependencies via YUM:

```bash
$ sudo yum install wget gcc libevent-devel openssl-devel gtk2-devel libuuid-devel sqlite-devel jansson-devel intltool cmake libtool vala gcc-c++ qt5-qtbase-devel qt5-qttools-devel qt5-qtwebkit-devel libcurl-devel openssl-devel
```

#### Building

First you should get the latest source of libsearpc/ccnet/seafile/seafile-client:

Download the source tarball of the latest tag from

- https://github.com/haiwen/libsearpc/tags (use v3.0-latest)
- https://github.com/haiwen/ccnet/tags (NOTE: from 6.2 version on, ccnet is no longer needed)
- https://github.com/haiwen/seafile/tags
- https://github.com/haiwen/seafile-client/tags

For example, if the latest released seafile client is 5.0.7, then just use the **v5.0.7** tags of the four projects. You should get four tarballs:

- libsearpc-v3.0-latest.tar.gz
- ccnet-5.0.7.tar.gz (NOTE: from 6.2 version on, ccnet is no longer needed)
- seafile-5.0.7.tar.gz
- seafile-client-5.0.7.tar.gz

```sh
# without alias wget= might not work
shopt -s expand_aliases

export version=5.0.7
alias wget='wget --content-disposition -nc'
wget https://github.com/haiwen/libsearpc/archive/v3.0-latest.tar.gz
# NOTE: from 6.2 version on, ccnet is no longer needed
wget https://github.com/haiwen/ccnet/archive/v${version}.tar.gz 
wget https://github.com/haiwen/seafile/archive/v${version}.tar.gz
wget https://github.com/haiwen/seafile-client/archive/v${version}.tar.gz
```

Now uncompress them:

```sh
tar xf libsearpc-3.0-latest.tar.gz
# NOTE: from 6.2 version on, ccnet is no longer needed
tar xf ccnet-${version}.tar.gz
tar xf seafile-${version}.tar.gz
tar xf seafile-client-${version}.tar.gz
```

To build Seafile client, you need first build **libsearpc** and **ccnet**, **seafile**.

##### set paths
```bash
export PREFIX=/usr
export PKG_CONFIG_PATH="$PREFIX/lib/pkgconfig:$PKG_CONFIG_PATH"
export PATH="$PREFIX/bin:$PATH"
```

##### libsearpc

```bash
cd libsearpc-3.0-latest
./autogen.sh
./configure --prefix=$PREFIX
make
sudo make install
cd ..
```

##### ccnet #####

NOTE: from 6.2 version on, ccnet is no longer needed

```bash
cd ccnet-${version}
./autogen.sh
./configure --prefix=$PREFIX
make
sudo make install
cd ..
```

##### seafile

```bash
cd seafile-${version}/
./autogen.sh
./configure --prefix=$PREFIX --disable-fuse
make
sudo make install
cd ..
```

#### seafile-client

```bash
cd seafile-client-${version}
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$PREFIX .
make
sudo make install
cd ..
```

#### custom prefix
when installing to a custom ```$PREFIX```, i.e. ```/opt```, you may need a script to set the path variables correctly

```bash
cat >$PREFIX/bin/seafile-applet.sh <<END
#!/bin/bash
export LD_LIBRARY_PATH="$PREFIX/lib:$LD_LIBRARY_PATH"
export PATH="$PREFIX/bin:$PATH"
exec seafile-applet $@
END
cat >$PREFIX/bin/seaf-cli.sh <<END
export LD_LIBRARY_PATH="$PREFIX/lib:$LD_LIBRARY_PATH"
export PATH="$PREFIX/bin:$PATH"
export PYTHONPATH=$PREFIX/lib/python2.7/site-packages
exec seaf-cli $@
END
chmod +x $PREFIX/bin/seafile-applet.sh $PREFIX/bin/seaf-cli.sh
```
you can now start the client with ```$PREFIX/bin/seafile-applet.sh```.

