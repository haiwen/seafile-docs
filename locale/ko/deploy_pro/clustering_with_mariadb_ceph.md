# MariaDB 및 Ceph를 활용한 Seafile 클러스터링

이 문서에서는 확장이 용이한 Seafile 클러스터와 MariaDB, Ceph를 가동하는 자세한 방법을 설명합니다. 이 문서로 내용이 끝나는건 아닙니다. 프로젝트가 진행 중인 만큼 쌓이는 지식을 반영하여 계속 내용을 고쳐나가겠습니다.

## 배경

Seafile은 파일을 라이브러리에 모아둡니다. 모든 라이브러리는 git 저장소와 유사한 파일 시스템 트리로, 각 파일 및 폴더는 유일한 해시 값을 갖습니다. 이 유일 ID는 동기화 알고리즘에서 활용하며 각 파일의 동기화 상태를 데이터베이스에 저장할 필요가 없습니다. Ceph와 Swift같은 객체 저장소는 확장이 용이하지만 MySQL과 같은 기존의 데이터베이스는 수천만개의 레코드로 확장할 수 없습니다. 따라서 이론적으로는 Seafile은 동기화 및 공유 목적으로 수십억개의 파일을 저장할 수 있습니다.

파일을 객체 저장소에 저장하면, 공유 및 권한 같은 기타 정보는 데이터베이스에 저장합니다. MariaDB 갈레라는 확장 가능하고 신뢰성 있는 데이터베이스 저장소로 활용할 수 있습니다.

## 하드웨어 및 시스템 요구사항

최소한 클러스터 설정에 머신 세개를 사용합니다. 각 머신의 구성은 다음과 같습니다

* 코어 4개 및 8GB 이상 용량을 지닌 메모리.
* Ceph 저널을 저장하는 1 SSD.
* 운영 체제를 저장하는 1 SATA 디스크
* MariaDB 데이터베이스를 저장하는 1 SATA 디스크
* Ceph 데이터를 저장하는 SATA 디스크 네개 이상

우분투 14.04를 운영 체제로 사용하겠습니다. 아래에서 서버 세대 각각을 node1, node2, node3로 표현했습니다.

## Ceph 클러스터 설치

#### 준비

노드 하나(node1이라 하겠습니다)를 설치용 관리자 노드로 선택하십시오. ceph-deploy를 설치하십시오.

* 릴리스 키를 추가하십시오:  

```
wget -q -O- 'https://ceph.com/git/?p=ceph.git;a=blob_plain;f=keys/release.asc' | sudo apt-key add -
```

* Ceph 꾸러미를 저장소에 추가하십시오. {ceph-stable-releast} 대신 안정 Ceph 릴리스 버전(emperor, firefly, giant 등)으로 바꾸십시오. 최종 안정 릴리스는 'giant' 입니다.

```
echo deb http://ceph.com/debian-{ceph-stable-release}/ $(lsb_release -sc) main | sudo tee /etc/apt/sources.list.d/ceph.list
```

* 저장소를 업데이트하고 ceph-deploy를 설치하십시오:  

```
sudo apt-get update && sudo apt-get install ceph-deploy
```

모든 노드에 ntp를 설치하고 ntp를 다시 시작하십시오  

    sudo apt-get install ntp
    sudo service ntp restart

모든 노드에 openssh를 설치하십시오

    sudo apt-get install openssh-server

설치 과정은 비 루트 사용자로 진행합니다. 이 사용자가 무암호 sudo 권한을 지니고 있는지 확인하십시오.

    echo "{username} ALL = (root) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/{username}
    sudo chmod 0440 /etc/sudoers.d/{username}

node1에 ssh 공용키를 만들어 설치하십시오. 다음 기타 노드에 `~/.ssh/authorized_keys` 노드에 공용키를 복사하십시오.

#### Cept 클러스터 만들기

만들어둔 설정 파일을 저장할 node1에 `ceph-cluster` 디렉터리를 만드십시오. 모든 명령은 이 디렉터리에서 실행해야합니다.

모든 노드에 Ceph를 설치하십시오

    ceph-deploy install node1 node2 node3

클러스터를 만드십시오  

    ceph-deploy new node1 node2 node3

Ceph 감시자를 만드십시오. 모든 노드의 6789 포트를 열어두어야합니다.

    ceph-deploy mon create node1 node2 node3 

키를 획득하십시오

    ceph-deploy gatherkeys node1

#### OSD 추가

Ceph에서, 모든 OSD 데몬은 하나의 디스크를 관리합니다. OSD는 저널링용 SSO를 공유할 수 있습니다.
저널링용 SSD를 `/dev/sdb`라 가정하고 SATA 디스크는 `/dev/sdc`, `/dev/sdd` 등이라고 하겠습니다. 다음 명령으로 OSD를 추가하십시오:

    ceph-deploy osd create node1:/dev/sdc:/dev/sdb
    ceph-deploy osd create node2:/dev/sdc:/dev/sdb
    ceph-deploy osd create node3:/dev/sdc:/dev/sdb
    ceph-deploy osd create node1:/dev/sdd:/dev/sdb
    ceph-deploy osd create node2:/dev/sdd:/dev/sdb
    ceph-deploy osd create node3:/dev/sdd:/dev/sdb

**참고** 기본적으로 Ceph에서 5GB 크기의 저널링 분할 공간을 활용합니다. 저널링 디스크 용량이 너무 적으면 OSD 만들기에 실패합니다. 다음 설정을 /etc/ceph/ceph.conf에 추가할 수 있습니다:

```
[osd]
\t# set journal size to 4GB
        osd journal size = 4000
```

#### 클러스터 상태 검사

Ceph 클러스터 설정이 끝났습니다. `sudo ceph -s` 명령으로 클러스터 상태를 검사할 수 있습니다.

#### 참고

http://ceph.com/docs/master/rados/deployment/

## MariaDB 클러스터 설정

#### MariaDB 및 갈레라 설치

우선, MariaDB 및 갈레라의 apt 공급원을 설정하십시오. [이 페이지](https://downloads.mariadb.org/mariadb/repositories)에서 5.5 저장소를 선택하십시오.
이렇게 준비하면 MariaDB와 갈레라를 설치할 수 있습니다.

    sudo apt-get install mariadb-galera-server galera
    sudo apt-get install rsync

#### MariaDB 설정

`/etc/mysql/conf.d/cluster.cnf`에서,

    [mysqld]

    query_cache_size=0
    binlog_format=ROW
    default-storage-engine=innodb
    innodb_autoinc_lock_mode=2
    query_cache_type=0
    bind-address=0.0.0.0

    # Galera Provider Configuration
    wsrep_provider=/usr/lib/galera/libgalera_smm.so
    #wsrep_provider_options="gcache.size=32G"

    # Galera Cluster Configuration
    wsrep_cluster_name="test_cluster"
    wsrep_cluster_address="gcomm://first_ip,second_ip,third_ip

    # Galera Synchronization Congifuration
    wsrep_sst_method=rsync
    #wsrep_sst_auth=user:pass

    # Galera Node Configuration
    wsrep_node_address="this_node_ip"
    wsrep_node_name="this_node_name"

여기에 있는 first_ip, second_ip, third_ip는 node1, node2, node3의 각각의 IP 주소입니다.

#### MariaDB의 데이터 디렉터리 바꾸기

개별 디스크에 데이터베이스 데이터를 저장하겠습니다. 디스크를 `/mysql` 경로에 마운트했다고 가정하겠습니다.

다음 명령으로 MariaDB를 멈추십시오:

    sudo /etc/init.d/mysql stop

다음 명령으로 기존 데이터 디렉터리(기본적으로 /var/lib/mysql에 있음)를 복사하십시오:

    sudo cp -R -p /var/lib/mysql/* /mysql

/etc/mysql/my.cnf를 편집하여 `datadir` 설정 항목 값을 `/mysql`로 바꾸십시오.

다음 명령으로 MariaDB를 다시 시작하십시오:

    sudo /etc/init.d/mysql restart

#### 시작

MariaDB 클러스터를 시작하기 전에, 모든 데이터베이스 노드의 3456 및 4444 포트를 열었는지 확인하십시오.

node1:

    node1# sudo service mysql start --wsrep-new-cluster

node2, node3:

    node2# sudo service mysql start
    node3# sudo service mysql start

#### 참고

https://www.digitalocean.com/community/tutorials/how-to-configure-a-galera-cluster-with-mariadb-on-ubuntu-12-04-servers

## Seafile 클러스터 설정

[Seafile 및 Ceph 설정](setup_with_ceph.md) 및 [Seafile 클러스터 설정](deploy_in_a_cluster.md) 방식을 따르십시오.

