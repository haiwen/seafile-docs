# 서버

## 준비

다음 목록은 머신에 설치해야 할 모든 라이브러리를 나타냅니다. **Seafile을 빌드하기 전 모두 설치해야합니다**.

꾸러미 이름은 우분투 12.04를 따릅니다. 다른 리눅스 배포판에서는, 해당 이름을 직접 찾으십시오.

* libevent-dev  (2.0 이상)
* libcurl4-openssl-dev  (1.0.0 이상)
* libglib2.0-dev (2.28 이상)
* uuid-dev
* intltool (0.40 이상)
* libsqlite3-dev (3.7 이상)
* libmysqlclient-dev (5.5 이상)
* libarchive-dev
* libtool
* libjansson-dev
* valac
* libfuse-dev

또한 Seafile 서버 5.1.0부터 파이썬 2.7이 필요합니다.

다음 라이브러리의 소스 코드를 컴파일해야합니다.

### libzdb

* `re2c`와 `flex`를 설치하십시오
* [libzdb](http://www.tildeslash.com/libzdb/dist/libzdb-2.12.tar.gz)를 다운로드하십시오

#### libevhtp

* [libevhtp](https://github.com/ellzey/libevhtp/archive/1.1.6.tar.gz)를 다운로드하십시오.
* 다음 명령으로 libevhtp를 빌드하십시오:

```
cmake -DEVHTP_DISABLE_SSL=ON -DEVHTP_BUILD_SHARED=ON .
make
sudo make install

```

### Seahub 의존 관계

**Seahub** 는 Seafile의 웹 프론트엔드입니다. [장고](http://djangoproject.com) 프레임워크로 작성했습니다. Seahub를 사용하려면 서버에 파이썬 2.6(또는 2.7)을 설치해야 하며, 다음 파이썬 라이브러리가 필요합니다:

- Django 1.8
- pytz
- django-statici18n
- djangorestframework
- django_compressor
- django-post_office
- [django-constance](https://github.com/haiwen/django-constance/) (`pip install https://github.com/haiwen/django-constance/archive/bde7f7c.zip` 명령으로 설치)
- gunicorn
- flup
- chardet
- python-dateutil
- six
- openpyxl

계속하기 전, 위에 언급한 모든 라이브러리를 시스템에 설치했는지 확인하십시오.

### 디렉터리 배치 준비

다음 섹션에서는 Seafile 서버 빌드 및 설치 방법을 과정 별로 안내합니다. Seafile 서버에는 여러 구성 요소가 들어있습니다. 이들 구성 요소가 제대로 동작하려면:

* 단계별 절차를 따르십시오
* 디렉터리 배치가 각 단계별로 안내서와 정확히 일치하는지 확인하십시오.

우선 최상위 디렉터리를 만드십시오. 다음 섹션에서 "/data/haiwen"을 최상위 디렉터리로 사용합니다.

<pre>
mkdir /data/haiwen/
cd /data/haiwen/
mkdir seafile-server
cd seafile-server
</pre>

현재 배치는 다음과 같습니다:

<pre>
haiwen/
└── seafile-server
</pre>

### 소스 코드 가져오기

우선 libsearpc/ccnet/seafile/seahub의 최신 소스 코드를 가져와야합니다

다음 저장소에서 latest 태그가 붙은 소스 코드 타르볼을 다운로드하십시오

* https://github.com/haiwen/libsearpc/tags
* https://github.com/haiwen/ccnet/tags
* https://github.com/haiwen/seafile/tags
* https://github.com/haiwen/seahub/tags

예를 들어 Seafile 최신 출시 버전이 4.4.7이면 프로젝트의 **v4.4.7-server** 태그를 활용하십시오(libsearpc는 **v3.0-latest**태그를 활용하므로 제외). 다음 네 가지 타르볼 파일을 가져오십시오:

* libsearpc-3.0-latest.tar.gz
* ccnet-4.4.7-server.tar.gz
* seafile-4.4.7-server.tar.gz
* seahub-4.4.7-server.tar.gz

<code>haiwen/src</code> 폴더를 만들고 libsearpc/ccnet/seafile 소스코드를 풀어 복사하십시오.

<pre>
cd haiwen/seafile-server
mkdir src
cd src
tar xf /path/to/libsearpc-3.0-latest.tar.gz
tar xf /path/to/ccnet-4.4.7-server.tar.gz
tar xf /path/to/seafile-4.4.7-server.tar.gz
</pre>

그리고 <code>haiwen/seafile-server</code>에 seahub 타르볼 압축을 푸십시오:

<pre>
cd haiwen/seafile-server
tar xf /path/to/seahub-4.4.7-server.tar.gz
mv seahub-4.4.7-server seahub
</pre>

현재, 디렉터리 배치는 다음과 같습니다:

<pre>
haiwen/
└── seafile-server
    └── seahub
    └── src
        ├── libsearpc-4.4.7-server
        ├── ccnet-4.4.7-server
        ├── seafile-4.4.7-server
        ├── ... (다른 파일)
</pre>

### 빌드

Seafile 서버를 빌드하려면 **libsearpc**, **ccnet**을 우선 빌드해야합니다.

##### libsearpc

<pre>
cd libsearpc-${version}
./autogen.sh
./configure
make
make install
</pre>

##### ccnet

<pre>
cd ccnet-${version}
./autogen.sh
./configure --disable-client --enable-server   # `export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig` if libsearpc is not found
make
make install
</pre>

##### seafile

<pre>
cd seafile-${version}
./autogen.sh
./configure --disable-client --enable-server
make
make install
</pre>


*참고*: 모든 구성 요소를 컴파일하고 난 후 `sudo ldconfig`를 실행하여 시스템 라이브러리 캐시를 새로 고쳐야합니다.

## Seafile 서버 가동

### Seafile 서버 구성 요소

Seafile 서버는 다음 구성요소로 이루어져있습니다:

<table>
  <tr>
    <th>프로세스 이름</th><th>기능</th>
  </tr>
  <tr>
    <td>ccnet-server</td><td>네트워크 기반</td>
  </tr>
  <tr>
    <td>seaf-server</td><td>데이터 관리</td>
  </tr>
  <tr>
    <td>Seahub</td><td>Seafile 서버 웹 사이트 프론트엔드</td>
  </tr>
  <tr>
    <td>fileserver</td><td>Seafile의 RAW 파일 업로드/다운로드 처리</td>
  </tr>
</table>

![Server 구성](../images/server-arch.png "server architecture")

* **ccnet**은 설정값을 보유하며 메타데이터는 <code>ccnet</code>이라는 디렉터리입니다.
* **seaf-server**는 설정값과 데이터를 <code>seafile-data</code>디렉터리에 저장합니다.
* **seahub**는 장고(Django)로 작성했습니다. 장고를 사용해 본 경험이 있다면, 모든 데이터베이스 테이블을 만드는 <code>syncdb</code> 명령을 실행해야 함을 알고 있어야합니다.
* **admin 계정**을 만들어 서버를 관리하는 admin 계정으로 로그인할 수 있습니다.

설정 값을 만드는 핵심 단계는 다음과 같습니다:

* Seafile을 이미 설치했고, Seahub에서 필요한 모든 파이썬 라이브러리를 설치했는지 확인합니다.
* **ccnet-init** 프로그램으로 ccnet 설정을 만듭니다
* **seaf-server-init** 프로그램으로 Seafile 설정을 만듭니다
* seahub의 **syncdb** 장고(Django) 명령을 실행합니다
* Seafile 서버의 admin 계정을 만듭니다

설정 값을 만들려면 다음 방법 중 한가지를 택할 수 있습니다:

* seafile-admin 스크립트 사용(하단 참조)
* [[서버 설정값 직접 만들기]]


### seafile-script로 설정값 만들기

소스 코드로 Seafile을 빌드하고 설치했다면 시스템 경로에 <code>seafile-admin</code>가 이미 설치된 상태입니다.
<pre>
usage: seafile-admin [-h] {setup,start,stop,reset-admin} ...

optional arguments:
  -h, --help            show this help message and exit

subcommands:

  {setup,start,stop,reset-admin}
    setup               setup the seafile server
    start               start the seafile server
    stop                stop the seafile server
    reset-admin         reset seafile admin account
</pre>

최상위 디렉터리로 이동(이 안내서에서는 **/data/haiwen**)한 후, **seafile-admin setup** 을 실행하여 모든 설정값을 만드십시오:
<pre>
cd /data/haiwen
export PYTHONPATH=/data/haiwen/seafile-server/seahub/thirdpart
seafile-admin setup
</pre>

다음 스크립트는 여러분에게 여러가지 질문을 던져주고, 모든 설정을 만들어줍니다.

<table>
  <tr>
    <th>이름</th><th>용도</th><th>기본값</th><th>요구사항</th>
  </tr>
  <tr>
    <td>서버 이름</td>
    <td>클라이언트에 나타나는 서버 이름</td>
    <td></td>
    <td>3 ~ 15 영숫자</td>
  </tr>
  <tr>
    <td>IP 또는 도메인</td>
    <td>서버의  IP 주소 또는 도메인 이름</td>
    <td></td>
    <td>올바른 IP 주소 또는 도메인 이름을 사용하지 않으면, 클라이언트 연결에 문제가 있습니다</td>
  </tr>
  <tr>
  <td>ccnet 포트</td>
  <td>ccnet에서 사용하는 TCP 포트</td>
  <td>10001</td>
  <td></td>
  </tr>
  <tr>
    <td>Seafile 포트</td>
    <td>Seafile에서 사용하는 TCP 포트</td>
    <td>12001</td>
    <td></td>
  </tr>
  <tr>
    <td>Seafile 파일 서버 포트</td>
    <td>Seafile 파일 서버에서 활용하는 TCP 포트</td>
    <td>8082</td>
    <td></td>
  </tr>
  <tr>
    <td>admin 전자메일 주소</td>
    <td>admin 계정의 전자메일 주소</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>admin 암호</td>
    <td>admin 계정 암호</td>
    <td></td>
    <td></td>
  </tr>
</table>

**seafile-admin setup** 명령의 실행 화면입니다:
![admin 설정 실행 중](../images/seafile-admin-1.png)

설정 과정이 제대로 끝난 화면은 다음과 같습니다:
![admin 설정 완료](images/seafile-admin-2.png)

이 때, 디렉터리 배치는 다음과 같습니다:
<pre>
haiwen/
└── ccnet # ccnet 설정 디렉터리
    └── ccnet.conf # ccnet 설정 파일
└── seafile-data # seafile 설정 및 데이터
    └── seafile.conf # seafile 설정 파일
└── seahub-data/ # seahub 데이터
└── seahub.db # seahub sqlite3 데이터베이스
└── seahub_settings.py # seahub 개별 설정
└── seafile-server
    └── seahub/
    └── seafile-{VERSION} # seafile 소스 코드
</pre>

### Seafile 서버 시작하기

설정값을 제대로 만든 후, 최상위 디렉터리에서 **seafile-admin start**를 실행하여 Seafile의 모든 구성 요소를 실행하십시오. (**seafile-admin 스크립트는 반드시 최상위 디렉터리에서 실행해야합니다**).

<pre>
cd /data/haiwen # go to the top level directory
seafile-admin start
</pre>

이 때, 모든 구성 요소가 동작해야 하며 **http://yourserver-ip-or-domain:8000** 주소로 seahub에 접근할 수 있습니다

**참고** nginx 또는 apache에서 가동할 경우가 있습니다. 이 때, [Nginx](../deploy/deploy_with_nginx.md)/[Apache](../deploy/deploy_with_apache.md)에서 Seafile 웹을 가동하는 방법을 따르십시오.

### Seafile 서버 멈추기

Seafile 서버 가동을 멈추려면, **seafile-admin stop**을 실행하십시오.

<pre>
cd /data/haiwen # 최상위 디렉터리로 이동
seafile-admin stop
</pre>

## Seafile 서버 업그레이드

Seafile 서버를 새 버전으로 업그레이드 할 때, 다음 과정을 거쳐야합니다:

* Seafile 서버를 실행중이면 멈추십시오

<pre>
cd /data/haiwen
seafile-admin stop
</pre>

* 새로 설치하는 방식대로 libsearpc/ccnet/seafile의 최신 소스 코드를 가져온 후 빌드하십시오.
* 업그레이드 스크립트를 실행하십시오. 업그레이드 스크립트는 주로 Seafile의 데이터베이스를 업데이트합니다. 예를 들면, Seafile 이전 버전이 아닌 최신 버전에서 사용하는 새 데이터베이스 테이블을 만듭니다.

### 최신 libsearpc/ccnet/seafile을 가져온 후 컴파일

상단의 **빌드** 섹션을 참고하십시오.

### 새 seahub 타르볼을 가져온 후 압축 풀기

<pre>
cd haiwen/seafile-server
mv seahub/ seahub-old # move away the old seahub folder
tar xf /path/to/new/seahub-x.x.x-server.tar.gz
mv seahub-x.x.x-server seahub
</pre>


### 업그레이드 수행

* scripts/upgrade/ 하위 디렉터리를 다른 곳으로 복사하십시오

업그레이드 스크립트는 Seafile 소스 코드의 <code>scripts/upgrade</code> 하위 디렉터리에 마련했습니다. 이 스크립트를 실행하기 전 **seafile-server** 디렉터리에 복사해야합니다.

<pre>
cd /data/haiwen/seafile-server
cp -rf seafile-{version}/scripts/upgrade .
</pre>

#### 연속 버전 업그레이드(1.1에서 1.2로 업그레이드하는 방식)

연속 버전 업그레이드란 Seafile 서버의 임의 버전에서 바로 다음버전으로의 업그레이드를 말합니다. 예를 들면 1.1.0에서 1.2.0으로 업그레이드 하는 절차를 연속 버전 업그레이드로 볼 수 있습니다.

**참고:** 1.3.0에서 1.3.1로 업그레이드하는 마이너 업그레이드는 하단의 별도의 섹션에 문서로 남겨두었습니다.

1.1.0에서 1.2.0으로 업그레이드 한다면, <code>seafile-server</code> 디렉터리에서 **upgrade_1.1_1.2.sh** 스크립트를 실행해야합니다.

<pre>
cd /data/haiwen/seafile-server
./upgrade/upgrade_1.1_1.2.sh
</pre>

#### 비연속 버전 업그레이드(1.1에서 1.3으로 업그레이드하는 방식)

1.1.0에서 1.3.0으로 업그레이드 하는 방식과 같이, 어떤 버전에서 건너뛰어 업그레이드 하는 절차는:

* 1.1.0에서 1.2.0으로 업그레이드
* 1.2.0에서 1.3.0으로 업그레이드

다음 업그레이드 스크립트를 차례대로 실행하십시오.

#### 마이너 업그레이드(1.3.0에서 1.3.1로 업그레이드 하는 방식)마

1.3.0에서 1.3.1로 업그레이드 하는 이런 방식을 마이너 업그레이드라고 합니다. 이런 업그레이드 방식에서는 아바타 링크 업데이트만 수행하면 됩니다:

<pre>
cd /data/haiwen/seafile-server/seahub/media
cp -rf avatars/* ../../../seahub-data/avatars/
rm -rf avatars
ln -s ../../../seahub-data/avatars
</pre>

## 문제 보고

Seafile을 빌드/배포 가동하는 과정에 문제가 있다면, 메시지를 전달하든지 [문제점 글타래를 열어주십시오](https://github.com/haiwen/seafile/issues).

