# 클러스터에서 가동

**참고**: Seafile 서버 5.0.0부터 모든 설정 파일은 **conf** 폴더로 한 곳에 옮겨 모아둡니다. [더 읽어보십시오](../deploy/new_directory_layout_5_0_0.md).

## <a id="wiki-arch"></a> 구조

Seafile 클러스터 솔루션은 3-티어 구조로 동작합니다:

* 로드 밸런서 티어: Seafile 서버로 들어오는 트래픽을 분산합니다. 여러대의 로드 밸런스 인스턴스를 가동하면 고가용성 처리도 가능합니다.
* Seafile 서버 클러스터: Seafile 서버 인스턴스의 클러스터. 인스턴스 하나가 망가지면, 로드 밸런서에서 이 인스턴스로 넘어가는 트래픽 처리를 중단합니다. 따라서 고가용성 기능 동작에 성공합니다.
* 백엔드 저장소: S3, 오픈스택 Swift, Ceph 같은 분산 저장소 클러스터.

이 구조는 수평 방향으로 확장합니다. 머신을 추가하여 더 많은 트래픽을 다룰 수 있음을 의미합니다. 이 구조는 다음 그림과 같습니다.

![seafile-cluster](../images/seafile-cluster.png)

Seafile 서버 노드에는 두가지 주 구성요소가 있는데, 하나는 웹 서버(Nginx/Apache) 그리고 다른 하나는 Seafile 앱 서버입니다. 웹 서버는 클라이언트 요청을 Seafile 앱 서버에 전달합니다. Seafile 앱 서버는 별개로 동작합니다. 각 구성요소간 상태는 알 수 없습니다. 각 앱 서버는 다른 앱 서버 인스턴스에 영향을 주지 않고 개별적으로 망가질 수 있다는 의미입니다. 로드 밸런서는 망가짐 증상을 발견하고 요청을 우회하는 역할을 수행합니다.

Seafile 앱 서버는 개별적으로 동작하지만 일부 세션 정보는 공유해야합니다. 모든 공유 세션 정보는 memcached에 저장합니다. 따라서 Seafile 앱 서버는 동일한 memcached(클러스터)에 연결해야합니다. memcached 설정 세부 내용은 다음에 다루겠습니다.

모든 Seafile 앱서버를 통해 동일한 사용자 데이터로 접근합니다.

데이터베이스에 대해서는, 모든 앱서버는 동일한 데이터베이스 또는 데이터베이스 클러스터에 연결해야합니다. 데이터베이스 클러스터가 필요하다면 MariaDB 갈레라 클러스터 사용을 추천합니다.

Seafile 클러스터를 가동하려면 몇가지 과정을 거칩니다:

1. 하드웨어, 운영체제, memcached 데이터베이스를 준비합니다
2. 단일 Seafile 서버 노드를 설정합니다
3. 기타 Seafile 노드에 설정을 복사합니다
4. Nginx/Apache 및 방화벽 규칙을 설정합니다
5. 로드 밸런서를 설정합니다
6. [백그라운드 작업 노드를 설정합니다](enable_search_and_background_tasks_in_a_cluster.md)

## <a id="wiki-preparation"></a>준비

### 하드웨어

최소한 2GB 램을 보유한 리눅스 서버 두대가 있어야합니다.

### 파이썬 라이브러리 설치 ###

각 노드에 파이썬 라이브러리를 설치해야합니다.

우선 파이썬 2.6 또는 2.7을 설치했는지 확인하시고, 그 다음:
```
sudo easy_install pip
sudo pip install boto
```

"Wheel installs require setuptools >= ..." 오류 메시지가 나타났다면, pip과 boto 줄 사이에 다음 명령을 실행하십시오
```
sudo pip install setuptools --no-use-wheel --upgrade
```

### Memcached 설정

모든 Seafile 서버 인스턴스는 동일한 memcached 서버를 함께 활용합니다. memcached 서버의 주소는 192.168.1.134, 11211번 포트(기본)에서 요청을 대기한다고 가정하겠습니다.

기본적으로 memcached는 127.0.0.1에서만 요청대기합니다. 따라서 memcached.conf 설정을 수정하고 memcached를 다시 시작해야합니다.

```
# Specify which IP address to listen on. The default is to listen on all IP addresses
# This parameter is one of the only security measures that memcached has, so make sure
# it's listening on a firewalled interface.
-l 0.0.0.0
```

memcached의 메모리 상위 한계 값을 256MB 처럼 설정하는 것이 좋습니다.

```
# Start with a cap of 64 megs of memory. It's reasonable, and the daemon default
# Note that the daemon will grow to this size, but does not start out holding this much
# memory
-m 256
```

Seafile 서버는 memcached의 세션 정보를 공유합니다. memcached 클러스터를 설정하면, 모든 memcached 노드에 Seafile 서버 노드를 연결했는지 확인하십시오.

memcached 클러스터를 설정하면, 각 Seafile 서버 노드에 memcached 인스턴스를 실행하거나 memcached 클러스터로 머신을 따로 설정할 수 있습니다. Seafile 서버 노드에 memcached를 실행하면 비용을 절약할 수 있습니다.

### (선택) MariaDB 클러스터 설정

MariaDB 클러스터는 클러스터 구조에서 문제가 발생하는 단일 지점을 제거하도록 합니다. 데이터베이스 클러스터의 모든 업데이트 과정에서 모든 인스턴스를 대상으로 동시에 리플리케이션을 진행합니다.

각 Seafile 서버 노드마다 데이터베이스 인스턴스 하나씩 실행하시는것이 좋습니다. 이 방식으로 구동하면 몇가지 이득이 있습니다:

* Seafile 앱 서버는 항상 빠른 로컬 데이터베이스 인스턴스에 접근합니다.
* 데이터베이스 인스턴스용도로 다른 로드 밸런서를 설정할 필요가 없습니다.

Seafile에서는 DB에 쓰기 동작을 그다지 많이 처리하지 않기 때문에 이 구조로 데이터베이스 노드 열댓개로 늘릴 수 있습니다. 좀 더 큰 구동 환경이라면, 데이터베이스에 좀 더 세련된 로드 밸런싱 기술을 활용하는게 좋습니다.

MariaDB 클러스터 설정 관련 자세한 내용은 [이 문서](clustering_with_mariadb_ceph.md)에서 다룹니다.

## <a id="wiki-configure-single-node"></a> 단일 노드 설정

모든 Seafile 서버의 설정 파일을 비슷하게 일관되게 두었는지 확인하십시오. **각 머신별로 Seafile 서버를 설정할 필요가 없다는 점이 **

### 라이선스 취득 ###

라이선스 파일을 최상위 디렉터리에 넣으십시오. 위키에서는 최상위 디렉터리로 `/data/haiwen` 디렉터리를 사용합니다.


### Seafile 전문가판 서버 다운로드 및 압축 해제 ###

```
tar xf seafile-pro-server_2.1.3_x86-64.tar.gz
```

이제 다음 파일 및 디렉터리가 나타납니다:

```
haiwen
├── seafile-license.txt
└── seafile-pro-server-2.1.3/
```
### Seafile 설정

Seafile 전문가판 서버의 설치 절차는 Seafile 커뮤니티판 서버와 동일합니다. 커뮤니티 위키의  [Seafile 서버 및 MySQL 다운로드 및 설치](../deploy/using_mysql.md)를 참고하십시오.

참고: **서버 주소에는 로드 밸런서 주소 또는 도메인 이름을 사용하십시오. 각 Seafile 서버 머신에 로컬 IP주소는 사용하지 마십시오. 로드 밸런서로 서비스에 항상 접근할 수 있게 합니다.**

설치 절차가 끝났다면, 설정 파일에 몇가지 설정을 직접 바꾸는 일이 남았습니다.

#### seafile.conf

다음 설정 내용을 `seafile.conf`에 추가하십시오

```
[cluster]
enabled = true
memcached_options = --SERVER=192.168.1.134 --POOL-MIN=10 --POOL-MAX=100
```

memcached 클러스터가 있다면, seafile.conf에 memcached 서버 주소를 설정하십시오. 형식은 다음과 같습니다

```
[cluster]
enabled = true
memcached_options = --SERVER=192.168.1.134 --SERVER=192.168.1.135 --SERVER=192.168.1.136 --POOL-MIN=10 --POOL-MAX=100
```

(선택) Seafile 서버는 상태 검사 실행 목적으로 로드 밸런서의 포트를 열어둡니다. Seafile에서는 기본적으로 11001번을 사용합니다. 이 값은 `seafile.conf`의 다음 설정을 추가하여 바꿀 수 있습니다

```
[cluster]
health_check_port = 12345
```

#### seahub_settings.py

파이썬 memcache 라이브러리를 설치하십시오.

데비안/우분투:

```
sudo apt-get install python-memcache
```

CentOS/RedHat:

```
sudo yum install python-memcached
```

`seahub_settings.py`에 다음 설정을 추가하십시오. 이 설정은 데이터베이스에 아바타를 저장하고 memcached에 아바타를 캐시 공간에 저장해두며, 모든 노드의 자체 메모리에 css 캐시를 저장해둘 것을 Seahub에 알려줍니다.

```
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '192.168.1.134:11211',
    }
}

AVATAR_FILE_STORAGE = 'seahub.base.database_storage.DatabaseStorage'

COMPRESS_CACHE_BACKEND = 'django.core.cache.backends.locmem.LocMemCache'

```

memcached 클러스터를 사용하면 `CACHES` 변수값을 다음 값으로 바꾸십시오:

```
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': ['192.168.1.134:11211', '192.168.1.135:11211', '192.168.1.136:11211',],
    }
}
```

썸네일 기능을 활성화했다면, 썸네일 저장소 경로를 **공유 폴더**로 설정하여, 모든 노드에서 **공유 폴더**를 통해 썸네일을 만들고 가져올 수 있게 하는 것이 좋습니다.

```
THUMBNAIL_ROOT = 'path/to/shared/folder/'
```

#### seafevents.conf

다음 설정을 `seafevents.conf`에 추가하여 로컬 서버의 파일 색인화 서비스를 비활성화하십시오. 파일 색인 서비스는 별도로 제공한 백그라운드 서버에서 시작해야합니다.

```
[INDEX FILES]
external_es_server = true
```

### Seahub 데이터베이스 업데이트

클러스터 환경에서는 로컬 디스크 대신 데이터베이스에 아바타를 저장해야합니다.

```
CREATE TABLE `avatar_uploaded` (`filename` TEXT NOT NULL, `filename_md5` CHAR(32) NOT NULL PRIMARY KEY, `data` MEDIUMTEXT NOT NULL, `size` INTEGER NOT NULL, `mtime` datetime NOT NULL);
```

### 백엔드 저장 장치 설정

백엔드 클라우드 저장소 시스템 설정을 설정 파일에 추가해야합니다.

* NFS: [Seafile 클러스터 및 NFS 설정](setup_seafile_cluster_with_nfs.md)
* S3: [Amazon S3 설정](setup_with_mazon_S3.md)
* 오픈스택 Swift: [오픈스택 Swift 설정](setup_with_OpenStackSwift.md)
* Ceph: [Ceph 설정](setup_with_Ceph.md)


### 단일 노드 실행 및 시험

이 단일 노드 설정이 끝났으면, 서버를 시작하여 제대로 동작하는지 시험하십시오:

```
cd /data/haiwen/seafile-server-latest
./seafile.sh start
./seahub.sh start
```

*참고:*

브라우저를 열고 http://ip-address-of-this-node:8000 주소에 들어가서 admin 계정으로 로그인하십시오.


## <a id="wiki-configure-other-nodes"></a>기타 노드 설정

이제 노드 하나가 잘 동작한, 다른 노드도 계속 설정하겠습니다.

### 모든 Seafile 서버에 설정 복사

Seafile 설치 디렉터리를 `/data/haiwen`이라고 하고, 이 디렉터리 전체를 타르볼로 압축한 후 다른 Seafile 서버 머신에 복사했다고 가정하겠습니다. 간단하게 이 타르볼을 풀어 사용할 수 있습니다.

각 노드에서 `./seafile.sh` 및 `./seahub.sh`를 실행하여 Seafile 서버를 시작하십시오.

## Nginx/Apache 및 https 설정

웹 접근 용도로 Nginx/Apache와 https를 사용할 수 있습니다. Seafile 서버를 실행하는 각 머신마다 설정해야합니다. **모든 서버의 인증서가 동일한지 확인하십시오.**

* Nginx:
   * [Seahub 및 Nginx 설정](../deploy/deploy_with_nginx.md)
   * [Nginx에서 https 활성화](../deploy/https_with_nginx.md)
* Apache:
   * [Seahub 및 Apache 설정](../deploy/deploy_with_apache.md)
   * [Apache에서 https 활성화](../deploy/https_with_apache.md)

## 방화벽 설정

[Seafile 서버 표준 포트](../deploy/using_firewall.md)를 설정하기 전, Seafile 클러스터의 방화벽 규칙 두가지를 설정해야합니다:

* 각 Seafile 서버 머신에 대해, 상태 검사 포트를 열어두십시오(기본값 11001);
* memcached 서버에서 11211 포트를 여십시오. 보안을 위해 Seafile 서버에서만 이 포트로 접근할 수 있어야합니다.


## <a id="wiki-lb-settings"></a>로드 밸런서 설정

이제 클러스터가 이미 동작중이니, 로드 밸런서를 실행하여 사용자를 맞아들이십시오.

### AWS 엘라스틱 로드 밸런서(ELB)

AWS 엘라스틱 로드 밸런서 관리 콘솔에서, Seafile 서버 인스턴스를 인스턴스 목록에 추가하고 나면, 두 단계 이상의 설정 과정을 진행해야 합니다.

우선 TCP 요청 대기자를 설정하십시오

![elb-listeners](../images/elb-listeners.png)

그 다음 상태 검사를 설정하십시오

![elb-health-check](../images/elb-health-check.png)

### HAProxy

다음은 `/etc/haproxy/haproxy.cfg` 예제입니다:

(상태 검사 포트를 `11001`번이라고 가정합니다)

```
global
    log 127.0.0.1 local1 notice
    maxconn 4096
    user haproxy
    group haproxy

defaults
    log global
    mode http
    retries 3
    maxconn 2000
    timeout connect 10000
    timeout client 300000
    timeout server 300000

listen seahub 0.0.0.0:80
    mode http
    option httplog
    option dontlognull
    option forwardfor
    server seahubserver01 192.168.1.165:80 check port 11001
    server seahubserver02 192.168.1.200:80 check port 11001

listen seahub-https 0.0.0.0:443
    mode tcp
    option tcplog
    option dontlognull
    server seahubserver01 192.168.1.165:443 check port 11001
    server seahubserver02 192.168.1.200:443 check port 11001
```

## 동작 방식 살펴보기

이제 클러스터를 시험해볼 수 있습니다. https://seafile.example.com 주소를 브라우저에서 열고 재밌게 활용해보십시오. Seafile 클라이언트로 파일을 동기화할 수 있습니다.

위 과정을 진행한 결과가 동작한다면, 다음 진행 단계는 [클러스터에서 검색 기능 및 백그라운드 작업 활성화](enable_search_and_background_tasks_in_a_cluster.md) 입니다.

