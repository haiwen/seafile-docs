# Amazon S3 설정

**참고**: Seafile 서버 5.0.0부터 모든 설정 파일은 **conf** 폴더로 한 곳에 옮겨 모아둡니다. [더 읽어보십시오](../deploy/new_directory_layout_5_0_0.md).

## 준비

Seafile 전문가판 서버와 아마존 S3를 설정하려면:

- [Seafile 전문가판 서버 다운로드 및 설치](download_and_setup_seafile_professional_server.md)의 안내를 따라 Seafile 전문가판 서버 기본 구성 요소를 설치하십시오
- 파이썬 `boto` 라이브러리를 설치하십시오. S3 서비스 접근에 필요합니다.
```
sudo easy_install boto
```
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
[commit_object_backend]
name = s3
# bucket name can only use lowercase characters, numbers, periods and dashes. Period cannot be used in Frankfurt region.
bucket = my-commit-objects
key_id = your-key-id
key = your-secret-key
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100

[fs_object_backend]
name = s3
# bucket name can only use lowercase characters, numbers, periods and dashes. Period cannot be used in Frankfurt region.
bucket = my-fs-objects
key_id = your-key-id
key = your-secret-key
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100

[block_backend]
name = s3
# bucket name can only use lowercase characters, numbers, periods and dashes. Period cannot be used in Frankfurt region.
bucket = my-block-objects
key_id = your-key-id
key = your-secret-key
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100
```

commit, fs, block 객체의 별개 버킷을 만들어두시는게 좋습니다.
key_id와 key는 S3에서 인증할 때 필요합니다. key_id와 key는 AWS 계정 페이지의 "보안 자격" 섹션에서 찾을 수 있습니다.

S3에서 버킷을 만들 때 [S3 버킷 이름 규칙][1]을 먼저 읽어두십시오. 특히, **대문자**를 버킷 이름에 사용하면 안됨을 참고하십시오(MyCommitObjects와 같은 캐멀 케이스 방식 이름을 사용하지 마십시오).

### 새 리전에서 S3 활용

2014년 1월부터 AWS의 새 리전에서는 S3에서 인증 서명 버전 4만 지원합니다. 현재, 프랑크후르트와 중국의 리전도 새 리전에 포함합니다.

이 리전의 S3 백엔드를 활용하려면, seafile.conf에 있는 commit_object_backend, fs_object_backend, block_backend 섹션에 다음 설정 항목을 추가핫비시오

```
use_v4_signature = true
# eu-central-1 for Frankfurt region
aws_region = eu-central-1
```

파일 검색 및 webdav를 v4 서명 매커니즘과 동작하게 하려면 ~/.boto에 다음 줄을 추가해야합니다.

```
[s3]
use-sigv4 = True
```

### memcached 클러스터 활용

클러스터 환경에서는 memcached 클러스터를 활용할 수도 있습니다. 위 설정에서 seafile.conf의 모든 memcached 서버 노드 주소를 지정해야합니다.

```
memcached_options = --SERVER=192.168.1.134 --SERVER=192.168.1.135 --SERVER=192.168.1.136 --POOL-MIN=10 --POOL-MAX=100
```

### S3와 https로 연결하기

전문가판 5.0.4부터 S3에 https로 연결할 수 있습니다. 다음 설정 항목을 seafile.conf에 추가하십시오:

```
[commit_object_backend]
name = s3
......
use_https = true

[fs_object_backend]
name = s3
......
use_https = true

[block_backend]
name = s3
......
use_https = true
```

서버 꾸러미를 CentOS 6에서 빌드했기 때문에 데비안/우분투를 사용하면, CentOS의 CA 번들 경로에 시스템 CA 번들을 복사해야합니다. 그렇지 않으면 Seafile에서 CA 번들을 차지 못하여 SSL 연결에 실패합니다.

```
sudo mkdir -p /etc/pki/tls/certs
sudo cp /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt
sudo ln -s /etc/pki/tls/certs/ca-bundle.crt /etc/pki/tls/cert.pem
```

참고해야 할 다른 중요한 사항은 **버킷 이름에 '.'(점)을 사용하지 말 것** 입니다. 점을 사용하면 AWS S3의 와일드카드 인증서를 해석할 수 없습니다. 이 점은 AWS의 한계입니다.

## S3 호환 객체 저장장치 활용

대부분의 객체 저장소 시스템은 현재 오픈스택 Swift, Ceph의 RADOS 게이트웨이 같은 S3 API와 호환됩니다. 이런 S3 호환 저장소 시스템을 Seafile 백엔드로 활용할 수 있습니다. 예제 설정은 다음과 같습니다:

```
[commit_object_backend]
name = s3
bucket = my-commit-objects
key_id = your-key-id
key = your-secret-key
host = 192.168.1.123:8080
path_style_request = true
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100

[fs_object_backend]
name = s3
bucket = my-fs-objects
key_id = your-key-id
key = your-secret-key
host = 192.168.1.123:8080
path_style_request = true
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100

[block_backend]
name = s3
bucket = my-block-objects
key_id = your-key-id
key = your-secret-key
host = 192.168.1.123:8080
path_style_request = true
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100
```

`host`는 S3 호환 서비스의 주소 및 포트 번호 값을 지닙니다. "http" 및 "https"를 "host" 설정 항목 값 앞에 붙여둘 수 있습니다. 기본적으로 http 연결을 활용합니다. https 연결을 활용하려면 `use_https = true` 설정 항목 값을 설정하십시오.

`path_style_request` 설정 항목은 객체에 접근할 `https://192.168.1.123:8080/bucketname/object`와 같은 URL을 Seafile에 활용하라고 일러주며 기본 URL 형식은 `https://bucketname.s3.amazonaws.com/object`와 같은 가상 호스트 방식입니다. 그러나 이 방식은 고급 DNS 서버 설정에 따라 다릅니다. 따라서 대부분의 S3 호환 저장소 시스템에서는 이 경로 방식만 구현해두었습니다.

## 실행 및 시험 ##

이제 `./seafile.sh start` 및 `./seahub.sh start` 명령으로 Seafile을 시작하고 웹사이트를 둘러볼 수 있습니다.

  [1]: http://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html "the bucket naming rules"

