# 리눅스

#### 준비

다음 목록은 개발 머신에 설치해야 할 항목을 나타냅니다. __Seafile을 빌드하기 전 아래 항목을 모두 설치해야합니다__.

꾸러미 이름은 우분투 14.04를 따릅니다. 다른 배포판을 사용한다면 관련 이름을 직접 찾으십시오.

* autoconf/automake/libtool
* libevent-dev (2.0 이상)
* libcurl4-openssl-dev  (1.0.0 이상)
* libgtk2.0-dev (2.24 이상)
* uuid-dev
* intltool (0.40 이상)
* libsqlite3-dev (3.7 이상)
* valac  (git 저장소에서 가져와서 빌드할 때만)
* libjansson-dev
* qtchooser
* qtbase5-dev
* libqt5webkit5-dev
* qttools5-dev
* qttools5-dev-tools
* valac
* cmake
* python-simplejson (seaf-cli용)

```bash
sudo apt-get install autoconf automake libtool libevent-dev libcurl4-openssl-dev libgtk2.0-dev uuid-dev intltool libsqlite3-dev valac libjansson-dev cmake qtchooser qtbase5-dev libqt5webkit5-dev qttools5-dev qttools5-dev-tools
```
최신 페도라 20 설치 배포판에서는, 다음 YUM 명령으로 모든 의존 관계에 있는 꾸러미를 설치합니다:

```bash
$ sudo yum install wget gcc libevent-devel openssl-devel gtk2-devel libuuid-devel sqlite-devel jansson-devel intltool cmake libtool vala gcc-c++ qt5-qtbase-devel qt5-qttools-devel qt5-qtwebkit-devel
```

#### 빌드

우선 libsearpc/ccnet/seafile/seafile-client의 최신 소스 코드를 가져와야합니다:

다음 저장소에서 latest 태그가 붙은 소스 코드 타르볼을 다운로드하십시오

- https://github.com/haiwen/libsearpc/tags (v3.0-latest 활용)
- https://github.com/haiwen/ccnet/tags
- https://github.com/haiwen/seafile/tags
- https://github.com/haiwen/seafile-client/tags

예를 들어, Seafile 클라이언트 최신 출시 버전이 5.0.7이라면, 프로젝트의 **v5.0.7** 태그를 사용하십시오. 다음 네가지 타르볼을 가져와야합니다:

- libsearpc-v3.0-latest.tar.gz
- ccnet-5.0.7.tar.gz
- seafile-5.0.7.tar.gz
- seafile-client-5.0.7.tar.gz

```sh
export version=5.0.7
alias wget='wget --content-disposition -nc'
wget https://github.com/haiwen/libsearpc/archive/v3.0-latest.tar.gz
wget https://github.com/haiwen/ccnet/archive/v${version}.tar.gz
wget https://github.com/haiwen/seafile/archive/v${version}.tar.gz
wget https://github.com/haiwen/seafile-client/archive/v${version}.tar.gz
```

이제 압축을 해제하십시오:

```sh
tar xf libsearpc-3.0-latest.tar.gz
tar xf ccnet-${version}.tar.gz
tar xf seafile-${version}.tar.gz
tar xf seafile-client-${version}.tar.gz
```

Seafile 클라이언트를 빌드하려면, **libsearpc**, **ccnet**, **seafile** 을 우선 빌드해야합니다.

##### 경로 설정
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
cmake -DUSE_QT5=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$PREFIX .
make
sudo make install
cd ..
```

#### 개별 PREFIX 설정
```/opt```와 같은 개별 ```$PREFIX```에 설치하려면, 경로 변수를 올바르게 설정하는 스크립트가 필요합니다

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
이제 ```$PREFIX/bin/seafile-applet.sh```로 클라이언트를 시작할 수 있습니다.

