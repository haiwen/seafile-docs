## 둘러보기

백업할 데이터는 두 부분으로 이루어져있습니다

* Seafile 라이브러리 데이터
* 데이터베이스

설명서를 따라 Seafile 서버를 설정했다면, 디렉터리 구조는 다음과 같습니다:

    haiwen       # 조직 이름으로 바꿈
      --seafile-server-2.x.x # Seafile 꾸러미 압축 해제본
      --seafile-data   # Seafile 설정 및 데이터(기본으로 선택했을 경우)
      --seahub-data    # Seahub 데이터
      --ccnet          # ccnet 설정 및 데이터
      --seahub.db      # Seahub에서 사용하는 SQLite3 데이터베이스
      --seahub_settings.py # Seahub용 추가 설정 파일

모든 라이브러리 데이터는 'haiwen' 디렉터리에 저장합니다.

Seafile 에는 데이터베이스 몇군데에 중요한 일부 메타데이터를 저장합니다. 이 데이터베이스의 이름 및 위치는 어떤 데이터베이스 프로그램을 사용하느냐에 따라 다릅니다.

SQLite에서 데이터베이스 파일은 'haiwen'  디렉터리에 저장하며 위치는 다음과 같습니다:

* ccnet/PeerMgr/usermgr.db: 사용자 정보
* ccnet/GroupMgr/groupmgr.db: 그룹 정보
* seafile-data/seafile.db: 라이브러리 메타데이터
* seahub.db: 웹 프론트엔드(seahub)에서 사용하는 테이블

MySQL에서 데이터베이스는 관리자가 만들기 때문에 어떻게 구동하느냐에 따라 이름이 다를 수 있습니다. 데이터베이스는 세가지가 있습니다:

* ccnet-db: 사용자 및 그룹 정보
* seafile-db: 라이브러리 메타데이터
* seahub.db: 웹 프론트엔드(seahub)에서 사용하는 테이블

## 백업 단계 ##

백업 단계는 3단계로 구성합니다:

1. 선택: SQLite를 데이터베이스로 사용한다면 Seafile 서버를 우선 멈춥니다.
2. 데이터베이스 백업
3. Seafile 데이터 디렉터리 백업

### 백업 순서: 데이터베이스 먼저 또는 데이터 디렉터리 먼저

- 데이터 디렉터리 백업 먼저, SQL 나중 실행: 데이터 디렉터리를 백업할 때 백업하지 않은 일부 새 객체를 기록합니다. 새 객체는 SQL 데이터베이스에서 참조합니다. 복원할 때 데이터베이스 기록 일부는 이 객체를 찾지 못합니다. 때문에, 라이브러리가 깨집니다.
- SQL 백업 먼저, 데이터 디렉터리 나중: 데이터베이스 백업을 먼저 하면, 모든 데이터베이스 레코드는 올바른 객체를 참조합니다. 따라서 라이브러리가 깨지지 않습니다. 하지만 백업 과정에서 저장소에 보관한 새 객체는 데이터베이스 레코드에서 참조하지 않습니다. 따라서 일부 라이브러리는 오래된 상태가 됩니다. 복원할 때, 일부 새 데이터를 유실합니다.

라이브러리 손상 방지에는 두번째 순서가 더 나을지도 모르겠습니다. 다른 백업 방식으로는 복원 과정에 새 데이터를 잃을 수 있습니다. 때문에 백업에 있어서는 언제나 제한이 있습니다.
그러나, 신속하게 끝낼 수 있는 저장소 백업 방식이 있다면, 첫번째 순서 방식이 더 많은 데이터를 백업할 수 있습니다.

Seafile 데이터 디렉터리는 `/data/haiwen`이며, `/backup` 디렉터리에 백업한다고 가정하겠습니다. `/backup` NFS, 디렉터리는 다른 머신에서 가져온 윈도우 공유 폴더, 외장 디스크일 수 있습니다. `/backup` 디렉터리를 다음과 같이 만들 수 있습니다:

    /backup
    ---- databases/  데이터베이스 백업 파일
    ---- data/  데이터 디렉터리 백업본

### 데이터베이스 백업 ###

데이터베이스를 때때로 파일 제각각으로 백업하심이 좋습니다. 최소한 일주일 단위로 이전 데이터베이스 백업을 덮어쓰지 마십시오.

**MySQL**

데이터베이스 이름을 `ccnet-db`, `seafile-db`, `seahub-db`라 하겠습니다. mysqldump는 테이블을 자동으로 잠그므로 MySQL 데이터베이스를 백업할 때 Seafile 서버를 굳이 멈출 필요가 없습니다. 보통 데이터베이스 테이블은 매우 작으므로 덤프의 크기는 그리 작지 않을지도 모릅니다.

    mysqldump -h [<MySQL 호스트>] -u[<사용자이름>] -p[<암호>] --opt ccnet-db > /backup/databases/ccnet-db.sql.`date +"%Y-%m-%d-%H-%M-%S"`

    mysqldump -h [<MySQL 호스트>] -u[<사용자이름>] -p[<암호>] --opt seafile-db > /backup/databases/seafile-db.sql.`date +"%Y-%m-%d-%H-%M-%S"`

    mysqldump -h [<MySQL 호스트>] -u[<사용자이름>] -p[<암호>] --opt seahub-db > /backup/databases/seahub-db.sql.`date +"%Y-%m-%d-%H-%M-%S"`

**SQLite**

SQLite 데이터베이스를 백업하기 전 Seafile 서버를 우선 멈추어야합니다.

    sqlite3 /data/haiwen/ccnet/GroupMgr/groupmgr.db .dump > /backup/databases/groupmgr.db.bak.`date +"%Y-%m-%d-%H-%M-%S"`

    sqlite3 /data/haiwen/ccnet/PeerMgr/usermgr.db .dump > /backup/databases/usermgr.db.bak.`date +"%Y-%m-%d-%H-%M-%S"`

    sqlite3 /data/haiwen/seafile-data/seafile.db .dump > /backup/databases/seafile.db.bak.`date +"%Y-%m-%d-%H-%M-%S"`

    sqlite3 /data/haiwen/seahub.db .dump > /backup/databases/seahub.db.bak.`date +"%Y-%m-%d-%H-%M-%S"`

### Seafile 라이브러리 데이터 백업 ###

모든 데이터 파일은 `/data/haiwen` 디렉터리에 저장하므로, 디렉터리 전체를 백업합니다. 백업 대상 저장소에 디렉터리 전체를 복사하거나 rsync로 증분 백업을 수행할 수 있습니다.

데이터 디렉터리 전체를 직접 복사하려면,

    cp -R /data/haiwen /backup/data/haiwen-`date +"%Y-%m-%d-%H-%M-%S"`

이 명령은 데이터 디렉터리를 시간별로 따로 복사합니다. 새 디렉터리 복사가 끝나면 이전 백업 사본을 삭제할 수 있습니다.

데이터가 많으면 데이터 디렉터리 전체 복사에 시간이 걸릴 수 있습니다. rsync를 사용하여 증분 백업할 수 있습니다.

    rsync -az /data/haiwen /backup/data

이 명령은 데이터 디렉터리를 `/backup/data/haiwen`으로 백업합니다.

## 백업 복원 ##

이제 초기 Seafile 서버가 손상되어, 새 머신으로 전환하는 상황을 가정해보겠습니다. Seafile 인스턴스 복원에 백업 데이터를 사용합니다:

1. `/backup/data/haiwen` 디렉터리를 새 머신으로 복사합니다. 새 머신의 Seafile 가동 위치를 `/data/haiwen` 이라고 하겠습니다.
2.데이터베이스를 복원합니다.
3. 데이터베이스 및 데이터를 제각기 백업했으니, 서로 일관성이 없을 수도 있습니다. 잠재적 비 일관성을 해결하려면, seaf-fsck 도구를 실행하여 새 머신에서 데이터 무결성을 확인하십시오. [seaf-fsck 문서를 참고하십시오](seafile_fsck.md).

### 데이터베이스 복원

이제 최신 유효 데이터베이스 파일을 직접 복원할 수 있습니다.

**MySQL**

    mysql -u[<사용자이름>] -p[<암호>] ccnet-db < ccnet-db.sql.2013-10-19-16-00-05
    mysql -u[<사용자이름>] -p[<암호>] seafile-db < seafile-db.sql.2013-10-19-16-00-20
    mysql -u[<사용자이름>] -p[<암호>] seahub-db < seahub-db.sql.2013-10-19-16-01-05

**SQLite**

    cd /data/haiwen
    mv ccnet/PeerMgr/usermgr.db ccnet/PeerMgr/usermgr.db.old
    mv ccnet/GroupMgr/groupmgr.db ccnet/GroupMgr/groupmgr.db.old
    mv seafile-data/seafile.db seafile-data/seafile.db.old
    mv seahub.db seahub.db.old
    sqlite3 ccnet/PeerMgr/usermgr.db < usermgr.db.bak.xxxx
    sqlite3 ccnet/GroupMgr/groupmgr.db < groupmgr.db.bak.xxxx
    sqlite3 seafile-data/seafile.db < seafile.db.bak.xxxx
    sqlite3 seahub.db < seahub.db.bak.xxxx

