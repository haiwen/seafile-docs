# Ceph 설정

**참고**: Seafile 서버 5.0.0부터 모든 설정 파일은 **conf** 폴더로 한 곳에 옮겨 모아둡니다. [더 읽어보십시오](../deploy/new_directory_layout_5_0_0.md).

Ceph는 확장 가능한 분산 저장소 시스템입니다. Seafile은 Ceph의 RADOS 객체 저장소 계층을 저장소 백엔드로 활용할 수 있습니다.

## ceph 설정 파일 및 클라이언트 키 모음 복사

Seafile은 클라이언트 입장에서 Ceph/RADOS 처럼 동작하므로, ceph 클러스터의 설정 파일과 키 모음에 접근해야합니다. 다음 파일을 관리자 노드의 /etc/ceph 디렉터리에서 Seafile 머신으로 복사해야합니다.

```
seafile-machine# sudo scp user@ceph-admin-node:/etc/ceph/ /etc
```

## memcached 설치 및 활성화

성능을 최상으로 끌어 올리려면 Seafile에 memcached를 설치하고 객체에 대해 memcache를 활성화해야합니다.

memcached에 128MB 메모리 용량을 할당해주는게 좋습니다. /etc/memcached.conf를 편집하십시오

```
# Start with a cap of 64 megs of memory. It's reasonable, and the daemon default
# Note that the daemon will grow to this size, but does not start out holding this much
# memory
# -m 64
-m 128
```

## 파이썬 Ceph 라이브러리 설치

파일 검색 기능과 WebDAV 기능은 시스템에 설치한 파이썬 Ceph 라이브러리에 의존합니다.

데비안/우분투:

```
sudo apt-get install python-ceph
```

RedHat/CentOS:

```
sudo yum install python-rados
```

## Seafile 설정 편집

`seafile.conf`를 편집하여 다음 줄을 추가하십시오:

```
[block_backend]
name = ceph
ceph_config = /etc/ceph/ceph.conf
pool = seafile-blocks
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100

[commit_object_backend]
name = ceph
ceph_config = /etc/ceph/ceph.conf
pool = seafile-commits
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100

[fs_object_backend]
name = ceph
ceph_config = /etc/ceph/ceph.conf
pool = seafile-fs
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100
```

commit, fs, block 객체의 별개 풀을 만들어두시는게 좋습니다.

```
ceph-admin-node# rados mkpool seafile-blocks
ceph-admin-node# rados mkpool seafile-commits
ceph-admin-node# rados mkpool seafile-fs
```

### memcached 클러스터 활용

클러스터 환경에서는 memcached 클러스터를 활용할 수도 있습니다. 위 설정에서 seafile.conf의 모든 memcached 서버 노드 주소를 지정해야합니다.

```
memcached_options = --SERVER=192.168.1.134 --SERVER=192.168.1.135 --SERVER=192.168.1.136 --POOL-MIN=10 --POOL-MAX=100
```

## 임의의 Ceph 사용자 활용

위 설정에서는 Ceph 연결시 기본(client.admin)사용자를 사용합니다.
다른 Ceph 사용자로 연결하고 싶을 때가 있습니다. Seafile에서 이 기능을 지원합니다.
Ceph 사용자를 지정하려면, 다음과 같이 `ceph_client_id` 옵션을 추가해야합니다:

```
[block_backend]
name = ceph
ceph_config = /etc/ceph/ceph.conf
# Sepcify Ceph user for Seafile here
ceph_client_id = seafile
pool = seafile-blocks
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100

[commit_object_backend]
name = ceph
ceph_config = /etc/ceph/ceph.conf
# Sepcify Ceph user for Seafile here
ceph_client_id = seafile
pool = seafile-commits
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100

[fs_object_backend]
name = ceph
ceph_config = /etc/ceph/ceph.conf
# Sepcify Ceph user for Seafile here
ceph_client_id = seafile
pool = seafile-fs
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100
```

/etc/ceph/ceph.conf에 사용자 키 모음 경로를 추가해야합니다:

```
[client.seafile]
keyring = <path to user's keyring file>
```

