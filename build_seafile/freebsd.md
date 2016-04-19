# FreeBSD

#### Preparation

**support for FreeBSD** is still under construction.

The following list is what you need to install on your development machine. __You should install all of them before you build seafile__.

Package names are according to FreeBSD Ports. You might install your ports manually or via ``pkgng``.

* devel/autoconf
* devel/automake
* textproc/intltool
* textproc/gsed
* devel/libtool
* devel/libevent2
* ftp/curl
* devel/glib20
* misc/ossp-uuid
* databases/sqlite3
* devel/jansson
* lang/vala
* devel/cmake
* archivers/libarchive
* devel/py-simplejson (removed in furture release)
 
GUI
* devel/qt4

```bash
#portmaster devel/autoconf devel/automake textproc/intltool textproc/gsed \
devel/libtool devel/libevent2 ftp/curl devel/glib20 misc/ossp-uuid databases/sqlite3 \
devel/jansson lang/vala devel/cmake devel/py-simplejson archivers/libarchive
```
For a fresh PkgNG users,

```bash
#pkg install autoconf automake intltool gsed libtool libevent2 curl \
  glib20 ossp-uuid sqlite3 jansson vala cmake py-simplejson libarchive
```

#### Building

First you should get the latest source of libsearpc/ccnet/seafile/seafile-client:

Download the source tarball of the latest tag from

- https://github.com/haiwen/libsearpc/tags (use v3.0-latest)
- https://github.com/haiwen/ccnet/tags
- https://github.com/haiwen/seafile/tags
- https://github.com/haiwen/seafile-client/tags

For example, if the latest released seafile client is 3.1.0, then just use the **v3.1.0** tags of the four projects. You should get four tarballs:

- libsearpc-v3.0-latest.tar.gz
- ccnet-3.1.0.tar.gz
- seafile-3.1.0.tar.gz
- seafile-client-3.1.0.tar.gz

```sh
export version=3.1.0
alias wget='wget --content-disposition -nc'
wget https://github.com/haiwen/libsearpc/archive/v3.0-latest.tar.gz
wget https://github.com/haiwen/ccnet/archive/v${version}.tar.gz
wget https://github.com/haiwen/seafile/archive/v${version}.tar.gz
wget https://github.com/haiwen/seafile-client/archive/v${version}.tar.gz
```

Now uncompress them:

```sh
tar xf libsearpc-v3.0-latest.tar.gz
tar xf ccnet-${version}.tar.gz
tar xf seafile-${version}.tar.gz
tar xf seafile-client-${version}.tar.gz
```

To build Seafile client, you need first build **libsearpc** and **ccnet**, **seafile**.

##### set paths
```bash
ln -sfh ../libdata/pkgconfig /usr/local/lib/pkgconfig
```

##### libsearpc

```bash
cd libsearpc-${version}
./autogen.sh
./configure --prefix=$PREFIX
make
sudo make install
```

##### ccnet #####

```bash
export CFLAGS="-I/usr/local/include/ossp/uuid -I/usr/local/include/event2"
export LDFLAGS="-L/usr/local/lib -L/usr/local/lib/event2"
cd ccnet-${version}
./autogen.sh
./configure --prefix=$PREFIX
make
sudo make install
```

##### seafile

```bash
cd seafile-${version}/
./autogen.sh
./configure --prefix=$PREFIX
make
sudo make install
```

#### seafile-client

```bash
cd seafile-client-${version}
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$PREFIX .
make
sudo make install
```

#### custom prefix
when installing to a custom ```$PREFIX```, i.e. ```/opt```, you may need a script to set the path variables correctly

```bash
cat >$PREFIX/bin/seafile-applet.sh <<END
#!/bin/bash
exec seafile-applet $@
END
cat >$PREFIX/bin/seaf-cli.sh <<END
export PYTHONPATH=/usr/local/lib/python2.7/site-packages
exec seaf-cli $@
END
chmod +x $PREFIX/bin/seafile-applet.sh $PREFIX/bin/seaf-cli.sh
```
you can now start the client with ```$PREFIX/bin/seafile-applet.sh```.

