# FreeBSD

#### 준비

**FreeBSD 지원** 부분은 아직 작성중입니다.

다음 목록은 개발 머신에 설치해야 할 항목을 나타냅니다. __Seafile을 빌드하기 전 아래 항목을 모두 설치해야합니다__.

FreeBSD port의 꾸러미 이름을 따릅니다. port 또는 ``pkgng``로 직접 설치하시면 됩니다.

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
* devel/py-simplejson (다음 릴리스에서 제거)

GUI
* devel/qt4

```bash
#portmaster devel/autoconf devel/automake textproc/intltool textproc/gsed \
devel/libtool devel/libevent2 ftp/curl devel/glib20 misc/ossp-uuid databases/sqlite3 \
devel/jansson lang/vala devel/cmake devel/py-simplejson archivers/libarchive
```
PkgNG 사용자라면,

```bash
#pkg install autoconf automake intltool gsed libtool libevent2 curl \
  glib20 ossp-uuid sqlite3 jansson vala cmake py-simplejson libarchive
```

#### 빌드

우선 libsearpc/ccnet/seafile/seafile-client의 최신 소스 코드를 가져와야합니다:

다음 저장소에서 latest 태그가 붙은 소스 코드 타르볼을 다운로드하십시오

- https://github.com/haiwen/libsearpc/tags (v3.0-latest 활용)
- https://github.com/haiwen/ccnet/tags
- https://github.com/haiwen/seafile/tags
- https://github.com/haiwen/seafile-client/tags

예를 들어, Seafile 클라이언트 최신 출시 버전이 3.1.0이면, 다음 네가지 프로젝트의 **v3.1.0** 태그를 활용하십시오. 다음 타르볼 파일 네개를 가져오십시오:

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

이제 압축을 해제하십시오:

```sh
tar xf libsearpc-v3.0-latest.tar.gz
tar xf ccnet-${version}.tar.gz
tar xf seafile-${version}.tar.gz
tar xf seafile-client-${version}.tar.gz
```

Seafile 클라이언트를 빌드하려면, **libsearpc**, **ccnet**, **seafile** 을 우선 빌드해야합니다.

##### 경로 설정
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

#### 개별 PREFIX 설정
```/opt```와 같은 개별 ```$PREFIX```에 설치하려면, 경로 변수를 올바르게 설정하는 스크립트가 필요합니다

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
이제 ```$PREFIX/bin/seafile-applet.sh```로 클라이언트를 시작할 수 있습니다.

