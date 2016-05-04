# 오픈스택 Swift 설정

**참고**: Seafile 서버 5.0.0부터 모든 설정 파일은 **conf** 폴더로 한 곳에 옮겨 모아둡니다. [더 읽어보십시오](../deploy/new_directory_layout_5_0_0.md).

참고: 이 문서는 오래됐습니다. [새 스위프트 활용 방법 문서](setup_with_swift.md)를 참고하십시오.

전문가판 서버 2.0.5부터, Seafile에서 S3 호환 클라우드 저장소(OpenStack/Swift)를 백엔드로 사용할 수 있습니다. 이 문서는 Swift를 예제로 활용합니다.

## Seafile 서버 준비

Seafile 전문가판 서버와 오픈스택 Swift를 설정하려면:

- [Seafile 전문가판 서버 다운로드 및 설치](download_and_setup_seafile_professional_server.md) 지침을 따라 Seafile 전문가판 서버 기본 설정을 진행하십시오
- 파이썬 `boto` 라이브러리를 설치하십시오 Swift 접근에 필요합니다.
```
sudo easy_install boto
```

성능을 최상으로 끌어 올리려면 Seafile에 memcached를 설치하고 객체에 대해 memcache를 활성화해야합니다.

memcached에 128MB 메모리 용량을 할당해주는게 좋습니다. /etc/memcached.conf를 편집하십시오

```
# Start with a cap of 64 megs of memory. It's reasonable, and the daemon default
# Note that the daemon will grow to this size, but does not start out holding this much
# memory
# -m 64
-m 128
```

## Swift 준비

실 서비스 환경에서 Swift와 S3 미들웨어를 함께 사용하고 Keystone을 인증 수단으로 활용합니다. 다음 절차는 Swift를 Keystone 인증과 활용하도록 이미 설정했다고 가정합니다. Swift와 S3 미들웨어가 동작하도록 바꾸는데 역점을 두겠습니다.

### Swift3 설치

미들웨어는 Swift용 S3 API를 구현합니다.

```
git clone https://github.com/fujita/swift3.git
cd swift3
sudo python setup.py install
```

### keystonmiddleware 설치

이 미들웨어에는 S3 API와 Keystone의 인증 용도로 사용하는 `s3token` 필터가 있습니다. Swift를 Keystone과 동작하도록 설정했다면, 이미 미들웨어를 설치했어야합니다.

```
git clone https://github.com/openstack/keystonemiddleware.git
cd keystonmiddleware
sudo pip install -r requirements.txt
sudo python setup.py install
```

### Swift용 proxy-server.conf 수정

우분투에서 설정 파일은 `/etc/swift/proxy-server.conf` 입니다.

우선 메인 파이프라인에서 `tempauth`를 `authtoken keystoneauth`로 바꾸었는지 확인하십시오. Swift와 Keystone이 함께 동작하도록 설정했다면 이 과정을 진행해야합니다.

`swift3 s3token`을 `[pipeline:main]`에 추가하십시오:

```
[pipeline:main]
pipeline = [...] swift3 s3token authtoken keystoneauth proxy-server
```

필터를 추가하십시오:

```
[filter:swift3]  
use = egg:swift3#swift3

[filter:s3token]  
paste.filter_factory = keystonemiddleware.s3_token:filter_factory  
auth_port = 35357  
auth_host = [keystone-ip]  
auth_protocol = http  
```

### Swift 다시 시작

```
swift-init proxy restart
```

### S3 API로 Swift 접근

S3 API로 Swift에 접근하려면, AWS 유사 접근 키 ID와 비밀 접근 키가 필요합니다. 다음 명령으로 지정 공여물과 사용자용 접근 키 ID와 비밀 접근키를 만드십시오(tenant-id와 user-id를 바꿔야합니다):

```
keystone ec2-credentials-create --tenant-id=d6fdc8460c7b46d0ad24aa23667b85c3 --user-id=b66742a744eb4fc98abd945781bf969d
```

S3 미들 웨어를 성공적으로 설정한 후, S3 클라이언트에 접근할 수 있어야합니다. 다음에는 Seafile에 버킷을 만들어야합니다. 파이썬 boto 라이브러리로 다음과 같이 진행할 수 있습니다(`key_id` 및 `secret_key`를 여러분이 소유한 값으로 바꾸십시오):

```
import boto
import boto.s3.connection

connection = boto.connect_s3(
    aws_access_key_id='<key_id>',
    aws_secret_access_key='<secret_key>',
    port=8080,
    host='swift-proxy-server-address',
    is_secure=False,
    calling_format=boto.s3.connection.OrdinaryCallingFormat())
connection.create_bucket('seafile-commits')
connection.create_bucket('seafile-fs')
connection.create_bucket('seafile-blocks')
```

각 S3 버킷은 Swift의 컨테이너에 대응합니다. 따라서 컨테이너럴 확인할 때 자체 Swift 명령을 활용할 수 있습니다. 예를 들면:

```
swift -V 2 -A http://[keystone_ip]:5000/v2.0 -U [tenant]:[user] -K [pas] list
```

## seafile.conf 수정

`seafile.conf`에 다음 줄을 추가하십시오(`key_id` 및 `secret_key` 값을 본인 소유 값으로 바꾸십시오)

```
[block_backend]
name = s3
bucket = seafile-blocks
key_id = <key_id>
key = <secret_key>
host = <swift-proxy-server-address>:8080
path_style_request = true
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100

[commit_object_backend]
name = s3
bucket = seafile-commits
key_id = <key_id>
key = <secret_key>
host = <swift-proxy-server-address>:8080
path_style_request = true
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100

[fs_object_backend]
name = s3
bucket = seafile-fs
key_id = <key_id>
key = <secret_key>
host = <swift-proxy-server-address>:8080
path_style_request = true
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100
```

### memcached 클러스터 활용

클러스터 환경에서는 memcached 클러스터를 활용할 수도 있습니다. 위 설정에서 seafile.conf의 모든 memcached 서버 노드 주소를 지정해야합니다.

```
memcached_options = --SERVER=192.168.1.134 --SERVER=192.168.1.135 --SERVER=192.168.1.136 --POOL-MIN=10 --POOL-MAX=100
```

## 실행 및 시험 ##

이제 `./seafile.sh start` 및 `./seahub.sh start` 명령으로 Seafile을 시작하고 웹사이트를 둘러볼 수 있습니다.

