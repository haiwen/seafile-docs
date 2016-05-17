# 오픈스택 Swift 설정

**참고**: Seafile 서버 5.0.0부터 모든 설정 파일은 **conf** 폴더로 한 곳에 옮겨 모아둡니다. [더 읽어보십시오](../deploy/new_directory_layout_5_0_0.md).

Seafile에서는 5.1.0에서부터 오픈스택 Swift를 저장소 백엔드로 지원합니다. 이 백엔드는 자체 Swift API를 활용합니다. 이전에는 사용자가 Swift의 S3 호환 계층만 사용할 수 있었습니다. 이젠 이 방식이 오래되었습니다. 이전 문서는 여전히 [여기](setup_with_openstackswift.md)에 있습니다.

## 준비

Seafile 전문가판 서버와 Swift를 설정하려면:

- [Seafile 전문가판 서버 다운로드 및 설치](download_and_setup_seafile_professional_server.md)의 안내를 따라 Seafile 전문가판 서버 기본 구성 요소를 설치하십시오
- memcached를 설치하고 설정하십시오. 최상의 성능을 발휘하려면 Seafile에서는 memcached를 설치하고 객체에 대한 memcache를 활성화해야합니다. memcached에 128MB 메모리 확보를 권장합니다. /etc/memcached.conf를 편집하십시오

```
# Start with a cap of 64 megs of memory. It's reasonable, and the daemon default
# Note that the daemon will grow to this size, but does not start out holding this much
# memory
# -m 64
-m 128
```

## Seafile.conf 수정

`seafile.conf`를 편집하여 다음 줄을 추가하십시오:

```
[block_backend]
name = swift
tenant = yourTenant
user_name = user
password = secret
container = seafile-blocks
auth_host = 192.168.56.31:5000
auth_ver = v2.0
memcached_options = --SERVER=192.168.1.134:11211 --POOL-MIN=10 --POOL-MAX=100

[commit_object_backend]
name = swift
tenant = yourTenant
user_name = user
password = secret
container = seafile-commits
auth_host = 192.168.56.31:5000
auth_ver = v2.0
memcached_options = --SERVER=192.168.1.134:11211 --POOL-MIN=10 --POOL-MAX=100

[fs_object_backend]
name = swift
tenant = yourTenant
user_name = user
password = secret
container = seafile-fs
auth_host = 192.168.56.31:5000
auth_ver = v2.0
memcached_options = --SERVER=192.168.1.134:11211 --POOL-MIN=10 --POOL-MAX=100
```

위 설정은 예제일 뿐입니다. 여러분의 환경에 따라 설정 항목 값을 바꿔야합니다.

Seafile은 Swift를 지원하며 인증 매커니즘으로 Keystone만 사용할 수 있습니다. 현재 v2.0 인증 프로토콜만 지원합니다. `auth_host` 설정 항목은 Keystone 서비스의 주소와 포트 번호 값을 지닙니다.

commit, fs, block 객체에 대해 별도의 컨테이너를 만드는 것이 좋습니다.

### memcached 클러스터 활용

클러스터 환경에서는 memcached 클러스터를 활용할 수도 있습니다. 위 설정에서 seafile.conf의 모든 memcached 서버 노드 주소를 지정해야합니다.

```
memcached_options = --SERVER=192.168.1.134 --SERVER=192.168.1.135 --SERVER=192.168.1.136 --POOL-MIN=10 --POOL-MAX=100
```

### Swift와 https로 연결하기

전문가판 5.0.4부터 Swift에 https로 연결할 수 있습니다. 다음 설정 항목을 seafile.conf에 추가하십시오:

```
[commit_object_backend]
name = swift
......
use_https = true

[fs_object_backend]
name = swift
......
use_https = true

[block_backend]
name = swift
......
use_https = true
```

서버 꾸러미를 CentOS 6에서 빌드했기 때문에 데비안/우분투를 사용하면, CentOS의 CA 번들 경로에 시스템 CA 번들을 복사해야합니다. 그렇지 않으면 Seafile에서 CA 번들을 차지 못하여 SSL 연결에 실패합니다.

```
sudo mkdir -p /etc/pki/tls/certs
sudo cp /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt
sudo ln -s /etc/pki/tls/certs/ca-bundle.crt /etc/pki/tls/cert.pem
```

## 실행 및 시험 ##

이제 `./seafile.sh start` 및 `./seahub.sh start` 명령으로 Seafile을 시작하고 웹사이트를 둘러볼 수 있습니다.

