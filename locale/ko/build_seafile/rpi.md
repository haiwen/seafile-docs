# 라즈베리 파이용 Seafile 서버 출시 꾸러미 빌드 방법

*목차*:

- [빌드 환경 설정](#wiki-setup-build-env)
  - [꾸러미 설치](#wiki-install-packages)
  - [개발 라이브러리 컴파일](#wiki-compile-dev-libs)
  - [파이썬 라이브러리 설치](#wiki-install-python-libs)
- [소스 코드 준비](#wiki-prepare-seafile-source-code)
  - [git 태그 가져온 후 소스코드 타르볼 준비](#wiki-fetch-tags-and-prepare-tarballs)
  - [꾸러미 생성 스크립트 실행](#wiki-run-pkg-script)
- [빌드한 꾸러미 시험](#wiki-test-built-pkg)
  - [새로 설치한 프로그램 시험](#wiki-test-fresh-install)
  - [업그레이드 시험](#wiki-test-upgrading)

## <a id="wiki-setup-build-env"></a>빌드 환경 설정

요구 사항:

- 라즈비안 배포판을 설치한 라즈베리 파이.

### <a id="wiki-install-packages"></a> 꾸러미 설치

```
sudo apt-get install build-essential
sudo apt-get install libevent-dev libcurl4-openssl-dev libglib2.0-dev uuid-dev intltool libsqlite3-dev libmysqlclient-dev libarchive-dev libtool libjansson-dev valac libfuse-dev re2c flex python-setuptools cmake
```
### <a id="wiki-compile-dev-libs"></a> 개발 라이브러리 컴파일

#### libevhtp

libevhtp는 libevent 기반으로 동작하는 http 서버입니다. Seafile 파일 서버에서 활용합니다.

```
git clone https://www.github.com/haiwen/libevhtp.git
cd libevhtp
cmake -DEVHTP_DISABLE_SSL=OFF -DEVHTP_BUILD_SHARED=ON .
make
sudo make install
```

#### libzdb

`libzdb` 에서는 sqlite/mysql/pg/oracle와 같은 다양한 데이터베이스 백엔드에 대한 일관된 API를 제공합니다. ccnet-server와 seafile-server에서 활용합니다.

```
git clone https://www.github.com/haiwen/libzdb.git
cd libzdb
./autogen.sh
./configure
make
sudo make install
```

모든 라이브러리를 컴파일하고 난 후, `ldconfig`를 실행하여 시스템 라이브러리 캐시를 업데이트하십시오:

```
sudo ldconfig
```

### <a id="wiki-install-python-libs"></a> 파이썬 라이브러리 설치


새 `/home/pi/dev/seahub_thirdpart` 디렉터리를 만드십시오:

```
mkdir -p ~/dev/seahub_thirdpart
```

타르볼 파일을 `/tmp/`에 다운로드하십시오:

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

여기 제시한 모든 라이브러리를 `/home/pi/dev/seahub_thirdpart`에 설치하십시오:

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

## <a id="wiki-prepare-seafile-source-code"></a>Seafile 소스 코드 준비

Seafile 서버를 빌드할 때, 네가지 하위 프로젝트가 과정에 들어갑니다:

- [libsearpc](https://github.com/haiwen/libsearpc)
- [ccnet](https://github.com/haiwen/ccnet)
- [seafile](https://github.com/haiwen/seafile)
- [seahub](https://github.com/haiwen/seahub)

빌드 과정은 두 단계입니다:

- 우선 각 프로젝트의 태그를 가져온 후, 해당 프로젝트의 소스코드 타르볼에 대해 make 명령을 수행하십시오.
- Then run a `build-server.py` script to build the server package from the source tarballs.

### <a id="wiki-fetch-tags-and-prepare-tarballs"></a> git 태그를 가져온 후 소스 코드 타르볼 준비

Seafile 출시 버전은 github의 태그로 관리합니다.

Seafile 서버 4.1.1 꾸러비를 생성한다면, 태그는 다음과 같습니다:

- ccnet, seafile, seahub는 모두 `v4.1.1-sever` 태그를 보유.
- libsearpc는 `v3.0-latest` 태그를 보유(libsearpc는 안정적이어서 더이상 개발을 진행하지 않으므로, 항상 `v3.0-latest`태그를 가짐)

우선 `PKG_CONFIG_PATH`환경 변수를 설정하십시오(이 변수를 설정하여 시스템에서 make && make install libsearpc/ccnet/seafile 절차를 진행할 필요가 없습니다):

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

### 동일한 폴더에 소스코드 타르볼 복사

```
mkdir ~/seafile-sources
cp ~/dev/libsearpc/libsearpc-<version>-tar.gz ~/seafile-sources
cp ~/dev/ccnet/ccnet-<version>-tar.gz ~/seafile-sources
cp ~/dev/seafile/seafile-<version>-tar.gz ~/seafile-sources
cp ~/dev/seahub/seahub-<version>-tar.gz ~/seafile-sources

cp ~/dev/seafobj/seafobj.tar.gz ~/seafile-sources
cp ~/dev/seafdav/seafdav.tar.gz ~/seafile-sources
```

### <a id="wiki-run-pkg-script"></a> 꾸러미 생성 스크립트 실행

이제 타르볼 파일을 준비했으니, `build-server.py` 스크립트를 실행하여 서버 꾸러미를 빌드할 수 있습니다.

```
mkdir ~/seafile-server-pkgs
~/dev/seafile/scripts/build-server.py --libsearpc_version=<libsearpc_version> --ccnet_version=<ccnet_version> --seafile_version=<seafile_version> --seahub_version=<seahub_version> --srcdir=  --thidrpartdir=/home/pi/dev/seahub_thirdpart --srcdir=/home/pi/seafile-sources --outputdir=/home/pi/seafile-server-pkgs
```

스크립트 실행이 끝나면, `~/seafile-server-pkgs` 폴더에 `seafile-server_4.1.1_pi.tar.gz`파일이 들어갑니다.

## <a id="wiki-test-built-pkg"></a> 빌드한 꾸러미 시험

### <a id="wiki-test-fresh-install"></a>새로 설치한 프로그램 시험

[SQLite와 Seafile 가동](http://manual.seafile.com/deploy/using_sqlite.html) 단계를 따르도록 이미 빌드한 Seafile 서버 꾸러미를 활용하십시오.

최소한 다음 시험 단계를 통과해야합니다:

- 설치 과정 이상 없음
- `seafile.sh start`및 `seahub.sh start` 실행 후, 브라우저로 로그인할 수 있음.
- 웹 브라우저의 파일 업로드/다운로드 기능 정상 동작.
- Seafile [WebDAV](http://manual.seafile.com/extension/webdav.html) 서버 정상 동작

### <a id="wiki-test-upgrading"></a> 이전 버전의 업그레이드 시험

- Seafile 서버 이전 버전 꾸러미를 다운로드한 후 설치하십시오.
- [설명서](http://manual.seafile.com/deploy/upgrade.html)를 따라 업그레이드하십시오
- 업그레이드가 끝나면 다음 기능이 정상적으로 동작하는지 확인하십시오:
  - 웹 브라우저의 파일 업로드/다운로드 기능 정상 동작.
  - Seafile [WebDAV](http://manual.seafile.com/extension/webdav.html) 서버 정상 동작

