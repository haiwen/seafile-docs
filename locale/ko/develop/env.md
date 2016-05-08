# 개발 환경 설정

## 준비 ##

꾸러미 이름은 우분투 12.04에 따릅니다. 다른 리눅스 배포판의 경우, 여러분이 직접 해당 이름을 찾아보십시오.

* libevent-dev(2.0 이상)
* libcurl4-openssl-dev(1.0.0 이상)
* libglib2.0-dev(2.28 이상)
* uuid-dev
* intltool(0.40 이상)
* libsqlite3-dev(3.7 이상)
* libmysqlclient-dev(5.5 이상)
* libarchive-dev
* libtool
* libjansson-dev
* valac
* libfuse-dev


다음 라이브러리의 소스 코드를 컴파일해야합니다.

* [libzdb](http://www.tildeslash.com/libzdb/dist/libzdb-2.12.tar.gz)
* [libevhtp](https://github.com/ellzey/libevhtp/archive/1.1.6.zip)

libzdb는 <code>re2c</code> 와 <code>flex</code> 꾸러미 두가지에 의존합니다.
libevhtp는 <code>cmake .; make; sudo make install</code> 명령으로 빌드할 수 있습니다. libevhtp의 버전은 1.1.6 또는 1.1.7이어야합니다.

'''Seahub'''는 Seafile의 웹 프론트엔드입니다. 장고 프레임워크로 작성했습니다. Seahub는 파이썬 2.6(2.7)을 서버에 설치해야 하며, 다음 파이썬 라이브러리가 필요합니다:

* [Django1.5](https://www.djangoproject.com/download/1.5.2/tarball/)
* [Djblets](https://github.com/djblets/djblets/tarball/release-0.6.14)
* sqlite3
* simplejson (python-simplejson)
* PIL (aka. python imaging library, python-image) 또는 Pillow
* chardet
* python-dateutil

## 다운로드 및 컴파일

[libsearpc](https://github.com/haiwen/libsearpc/), [ccnet](https://github.com/haiwen/ccnet/), [seafile](https://github.com/haiwen/seafile/), [seahub](https://github.com/haiwen/seahub/)를 ~/dev(또는 원하는 위치)에 복제하십시오.

다음 명령으로 libsearpc를 컴파일하십시오

    cd ~/dev/libsearpc
    ./autogen.sh
    ./configure
    make
    make install

다음 명령으로 ccnet을 컴파일하십시오

    cd ~/dev/ccnet
    ./autogen.sh
    ./configure --disable-client --enable-server   # `export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig` if libsearpc is not found
    make
    make install

다음 명령으로 Seafile을 컴파일하십시오

    cd ~/dev/seafile
    ./autogen.sh
    ./configure --disable-client --enable-server
    make     # in Mac, use `make LDFLAGS=-liconv`
    make install


## Seafile 실행

다음 명령으로 Seafile을 실행하십시오

    cd ~/dev/seafile/tests/basic
    ./seafile.sh 2

또는 ccnet, seafile, fileserver를 다음 명령으로 직접 시작할 수 있습니다:

    ccnet-server -c ~/dev/seafile/tests/basic/conf2/ -D all -f -
    seaf-server -c ~/dev/seafile/tests/basic/conf2/ -d ~/dev/seafile/tests/basic/conf2/seafile-data/ -f -l -

## Seahub 준비

Seahub 위치로 이동하십시오

    cd ~/dev/seahub

django-1.5를 thirdpart로 다운로드하십시오. 그리고 템플릿으로 setenv.sh를 만들고 수정하십시오

    cp setenv.sh.template setenv.sh

데이터베이스를 만드십시오

    . setenv.sh
    python manage.py syncdb

admin 계정을 만드십시오(Seafile을 ~/dev/seafile에 두었다고 가정)

    python tools/seahub-admin.py ~/dev/seafile/tests/basic/conf2

Seahub를 시작하십시오

    ./run-seahub.sh.template

