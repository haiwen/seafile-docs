# Seafile 실시간 백업 서버

참고: 실시간 백업 기능은 현재 베타 상태입니다. 백업 서버측에 사소한 문제가 있을 수 있지만, 이 가능은 주 서버의 기능 또는 데이터 무결성에는 전혀 영향을 주지 않습니다.

백업은(실 서비스를 가동하는) 주 서버의 데이터를 백업 서버로 복사하는 과정입니다.

백업은 데이터를 안전하게 지켜주는 중요한 과정입니다. 기본 백업 과정은 몇가지 빠진 내용을 담고 있는 [이 문서](../maintain/backup_recovery.md)에 설명했습니다:

- 백업은 고정 "백업 윈도우"에서 처리합니다(하루에 한 번 또는 하루에 몇 번). 주 서버 저장소가 손상되면 두 백업 윈도우간 최신 데이터를 기록한 최근 데이터를 잃게 됩니다.
- 백업 과정에서는 데이터베이스와 데이터 디렉터리를 각각 백업합니다. 백업 서버에서는, 데이터베이스의 일부 항목이 데이터 디렉터리와 일관성이 떨어질 수도 잇습니다. 이는 추후 복구할 때 일부 라이브러리의 "손상"을 유발합니다.

실시간 백업 서버는 주 서버의 데이터를 가져올 때 Seafile 클라이언트와 동일한 동기화 알고리즘을 활용합니다. 다음과 같이 동작합니다:

- 라이브러리를 업데이트할 때마다 주 서버는 백업 서버에 바뀐 데이터를 전달함을 알립니다. 델타 동기화 알고리즘으로 이 과정은 빠르게 진행하며 거의 실시간으로 백업 서버를 업데이트합니다.
- 또한 백업 서버에서는 주 서버의 모든 라이브러리를 주기적으로 확인합니다. 일부 새 라이브러리 또는 최신 업데이트 라이브러리를 백업 서버로 동기화합니다. 이 과정에서 실시간 동기화 처리 과정에 사소한 어긋남이 발생하여 나타나는 모난 업데이트를 추려냅니다.
- 백업 서버는 항상 데이터베이스와 데이터 디렉터리의 일관성을 유지합니다. 따라서 백업 서버의 어떤 라이브러리도(주 서버가 손상되지 않은 이상) 손상된 상태가 되지 않습니다.
- 모든 라이브러리의 전체 기록을 백업합니다. 이는 라이브러리의 최신 상태만 동기화하는 데스크톱 클라이언트와 유사한 방식으로 동작하지 않습니다.

백업에 필요한 데이터는 두가지 종류가 있습니다:

- seafile-data 디렉터리와 Seafile 데이터베이스의 핵심 라이브러리 메타데이터 테이블입니다. 이 데이터는 Seafile의 라이브러리 핵심 데이터 구조를 담고 있습니다. Seafile의 동기화 알고리즘으로 백업 서버와 동기화합니다. 이 절차를 통해 메타데이터 테이블은 seafile-data 디렉터리와의 일관성을 유지합니다.
- 데이터베이스의 모든 기타 테이블(seafile, ccnet, seahub 데이터베이스 포함)을 MySQL 리플리케이션으로 백업합니다.

## 실시간 백업 서버 설정

주 서버를 이미 가동 중이고 이제 백업 서버를 설정하려 한다고 가정하겠습니다.

백업 서버 설정 단계는 다음과 같습니다:

1. 백업 서버에 Seafile을 설치하십시오
2. 주 서버와 백업 서버의 MySQL 리플리케이션을 설정하십시오
3. 주 서버와 백업 서버의 Seafile 동기화를 설정하십시오

### 백업 서버에 Seafile 설치

[이 문서](../deploy_pro/download_and_setup_seafile_professional_server.md)를 따라 Seafile 전문가판을 백업 서버에 설치해야합니다. 실시간 백업 기능은 5.1.0 이상에서만 쓸 수 있으므로, 5.1.0 이후 버전으로 업그레이드해야합니다.

백업서버에 Seafile을 설치할 때, 다음을 참고하십시오:

- 데이터베이스 이름(ccnet, seafile, seahub 데이터베이스)은 주 서버의 데이터베이스 이름과 동일해야합니다.
- 오피스 파일 미리 보기, 검색 색인 처리, 파일 감사 등 전문가판의 다른 기능을 활성화할 필요가 없습니다.

### MySQL 리플리케이션 설정

MySQL 리플리케이션은 마스터 서버(이 경우, 주 서버)에서 슬레이브 서버(백업 서버)로 최신 데이터베이스를 비동기 방식으로 복제합니다. MySQL 리플리케이션 동작 방식, 설정 방법을 더 잘 이해하려면 우선 [MySQL 공식 문서](https://dev.mysql.com/doc/refman/5.6/en/replication-howto.html)를 읽어보아야합니다. 다음 단계는 MySQL 문서에 기반한 단계이며, Seafile에 맞게 조금 수정했습니다.

다음 내용에서는 "주 서버", "마스터 서버", "백업 서버", "슬레이브 서버"를 혼용합니다.

#### 주 서버의 MySQL 서버 설정 수정(my.cnf)

주 서버에서 my.cnf에 다음 설정 항목을 추가하십시오:

```
[mysqld]
log-bin=mysql-bin
server-id=1
```

주 서버의 my.cnf에서, 다른 중요한 설정 항목은 `expire_logs_days`입니다([참고](http://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_expire_logs_days)). 이 설정 항목은 리플리케이션에 사용할 바이너리 로그의 유지 시간을 관리합니다. 이 설정 항목의 기본 값은 바이너리 로그 파일을 오래토록 유지하는 값입니다. 지정 일 수 만큼 바이너리 로그 파일을 유지하도록 이 설정 항목 값을 정할 수 있습니다. 지정 일 수보다 오래된 바이너리 로그 파일은 삭제합니다. 따라서 백업 서버가 `expire_logs_days` 값 이상의 일 수 만큼 오프라인 상태이면, 백업 서버를 온라인으로 전환한 후에 리플리케이션을 재개할 수 없습니다. 이 설정 항목을 충분한 시간으로 설정하시는 것이 좋습니다.

바뀐 내용을 저장하고 나면, 주 서버의 MySQL 서버를 다시 시작하십시오.

#### MySQL 리플리케이션 사용자 만들기

주 서버에서 리플리케이션에 관련된 사용자를 만드십시오. MySQL 클라이언트 프롬프트에서,

```
CREATE USER 'repl'@'%' IDENTIFIED BY 'slavepass';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';
```

보유한 사용자 이름 및 암호로 바꾸십시오.

#### 리플리케이션 마스터 바이너리 로그 위치 가져오기

이 단계를 진행하는 동안, 주 서버의 Seafile 서비스를 멈추어 데이터베이스에 최신 내용을 기록하지 못하게 막아야합니다.

주 서버에서, MySQL 클라이언트 프롬프트에,

```
FLUSH TABLES WITH READ LOCK;
SHOW MASTER STATUS;
```

출력은 다음과 같이 나타납니다:

```
+------------------+----------+--------------+------------------+-------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+------------------+----------+--------------+------------------+-------------------+
| mysql-bin.000002 |   368915 |              |                  |                   |
+------------------+----------+--------------+------------------+-------------------+
```

출력 내용에서 `File`과 `Position` 필드는 백업 서버(리플리케이션 슬레이브) 설정에 활용합니다.

#### 주 서버 기존 데이터 내보내기

mysqldump로 주 서버 데이터베이스 데이터를 내보내는 방법은:

```
mysqldump -u <user> -p<password> --databases \
--ignore-table=<seafile_db>.Repo --ignore-table=<seafile_db>.Branch --ignore-table=<seafile_db>.RepoHead \
--ignore-table=<seahub_db>.base_userlastlogin --ignore-table=<seahub_db>.django_session \
--ignore-table=<seahub_db>.sysadmin_extra_userloginlog --ignore-table=<seahub_db>.UserTrafficStat \
--ignore-table=<seahub_db>.FileAudit --ignore-table=<seahub_db>.FileUpdate --ignore-table=<seahub_db>.PermAudit \
--ignore-table=<seahub_db>.Event --ignore-table=<seahub_db>.UserEvent --ignore-table=<seahub_db>.avatar_avatar \
--ignore-table=<seahub_db>.avatar_groupavatar --ignore-table=<seahub_db>.avatar_uploaded \
--master-data <seafile_db> <ccnet_db> <seahub_db> > dbdump.sql
```

`<user>`, `<password>`를 MySQL 관리 사용자 이름 및 암호로 바꿔야합니다. `<seafile_db>`, `<seahub_db>`, `<ccnet_db>`를 데이터베이스 이름으로 바꾸십시오.

#### 백업 서버의 MySQL 서버 설정 수정(my.cnf)

백업 서버에서 다음 옵션을 my.cnf에 추가하십시오:

```
[mysqld]
server-id=2
replicate-ignore-table = <seafile db>.Repo
replicate-ignore-table = <seafile db>.Branch
replicate-ignore-table = <seafile db>.RepoHead
replicate-ignore-table = <seahub db>.base_userlastlogin
replicate-ignore-table = <seahub db>.django_session
replicate-ignore-table = <seahub db>.sysadmin_extra_userloginlog
replicate-ignore-table = <seahub db>.UserTrafficStat
replicate-ignore-table = <seahub db>.FileAudit
replicate-ignore-table = <seahub db>.FileUpdate
replicate-ignore-table = <seahub db>.PermAudit
replicate-ignore-table = <seahub db>.avatar_avatar
replicate-ignore-table = <seahub db>.avatar_groupavatar
replicate-ignore-table = <seahub db>.avatar_uploaded
replicate-ignore-table = <seahub db>.Event
replicate-ignore-table = <seahub db>.UserEvent
```

위 설정은 리플리케이션 진행시 언급한 테이블을 무시하라고 백업 서버에 알려줍니다:

- Seafile 데이터베이스의 라이브러리 메타데이터 테이블: Repu, Branch, RepoHead로 구성합니다。이 테이블은 Seafile 백업 서버 자체에서 동기화합니다.
- Seahub 데이터베이스의 로컬 또는 임시 테이블. 관리자가 백업 서버의 데이터를 살펴보려 기록을 남겨두었다면, 이 테이블은 백업 서버에서 업데이트됩니다. 복제 항목 충돌을 막으려면 복제 과정에서 이 항목은 무시하십시오.

참고:

- 주 서버 및 백업 서버의 `server-id`는 달라야합니다.
- `<seafile db>` 및 `<seahub db>` 값은 데이터베이스 이름으로 바꾸십시오.

리플리케이션을 시작하지 않도록 `--skip-slave-start` 옵션을 붙여 백업 서버의 MySQL 서버를 다시 시작하십시오.

```
sudo /etc/init.d/mysql start --skip-slave-start
```

#### 백업 서버에서 기존 데이터 가져오기

백업 서버의 MySQL로 기존 데이터를 가져오려면:

```
mysql -u <usr> -p<pas> < dbdump.sql
```

`<user>` 및 `<pass>`를 MySQL 관리 사용자 이름 및 암호로 바꾸십시오.

#### 리플리케이션 시작

주 서버의 MySQL 잠금을 해제하십시오. MySQL 클라이언트 프롬프트에서,

```
unlock tables;
```

백업 서버에서 리플리케이션 시작 지점을 설정하십시오:

```
CHANGE MASTER TO MASTER_HOST='primary-host', MASTER_USER='user', MASTER_PASSWORD='slavepass', MASTER_LOG_FILE='bin-log-file', MASTER_LOG_POS=position;
```

`primary-host`는 MySQL 마스터 서버 주소 값으로 바꿔주시고 `user`는 리플리케이션 진행 사용자로, `slavepass`는 제공할 사용자 암호로, `bin-log-file`과 `position`dms "리플리케이션 마스터 바이너리 로그 위치 가져오기" 섹션에서 확인한 정보로 바꾸십시오.

백업 서버 리플리케이션을 시작하십시오 MySQL 클라이언트 프롬프트에서,

```
start slave;
```

리플리케이션을 시작하면, 백업 서버의 MySQL error.log에서 리플리케이션을 시작함을 나타내는 몇가지 로그 메시지를 볼 수 있습니다. 그리고 슬레이브에서는 마스터 서버의 새 최신 내용을 찾아냅니다.

### Seafile의 실시간 백업 설정

주 서버에서 다음 설정 항목을 seafile.conf에 추가하십시오:

```
[backup]
backup_url = http://backup-server
sync_token = c7a78c0210c2470e14a20a8244562ab8ad509734
```

백업 서버에서 다음 설정 항목을 seafile.conf에 추가하십시오:

```
[backup]
primary_url = http://primary-server
sync_token = c7a78c0210c2470e14a20a8244562ab8ad509734
sync_poll_interval = 3
```

- `backup_url`: URL 형식의 백업 서버 주소. http 또는 https를 사용할 수 있습니다.
- `primary_url`: URL 형식의 주 서버 주소.
- `sync_token`: 주 서버 및 백업 서버간 공유하는 비밀 토큰. 시스템 관리자가 만든 문자 40개로 이루어진 SHA1 토큰입니다. `uuidgen | openssl sha1` 명령을 사용하여 임의 토큰을 만들 수 있습니다.
- `sync_poll_interval`: 백업 서버는 주 서버의 모든 라이브러리를 주기적으로 순차처리합니다. 폴링 주기를 시간 단위로 설정할 수 있습니다. 기본 주기는 1 시간이며 매 시간마다 백업 서버가 주 서버를 폴링 방식으로 처리함을 의미합니다. 라이브러리 갯수가 많으면 주기 시간을 더 늘려야합니다.

설정을 저장한 후, 주 서버와 백업 서버의 Seafile 서비스를 다시 시작하십시오. 백업 서버를 다시 시작할 때 자동으로 백업을 시작합니다.

### Seafile 클러스토의 백업 서버 설정

주 서비스를 Seafile 클러스터로 실행 중이라면, 백업 서버를 설정할 때 확인할 두가지 주안점이 있습니다:

1. MariaDB 클러스터를 사용한다면 MySQL 인스턴스를 리플리케이션 마스터로만 사용해야 합니다.
2. seafile.conf 설정을 바꾸면서 각 Seafile 노드에 있는 `backup_url` 및 `sync_token` 설정 항목의 값을 설정해야합니다. 모든 첫 Seafile 노드 설정은 동일해야합니다. 해당 노드는 동일한 백업 서버를 가리킵니다.

현재 백업 서비스를 클러스터 **로** 구동할 수 없습니다. 단일 노드만 백업 서버로 활용할 수 있다는 의미입니다. 추후 이 부분을 개선할 예정입니다.

## 실시간 백업 서버 관리

설정이 끝나면, 백업 서버는 완벽하게 동작하는 Seafile 인스턴스가 됩니다. 관리자는 백업 서버를 두가지 방식으로 관리할 수 있습니다:

1. 일반적인 Seafile 인스턴스와 같이 Seahub 웹 인터페이스로 서버를 접근합니다.
2. 서버 꾸러미에 있는 `seaf-backup-cmd.sh` 스크립트를 활용하여 백업 기능을 관리합니다.

`seaf-backup-cmd.sh` 스크립트는 다음 명령을 제공합니다:

### 백업 상태 검사

`seaf-backup-cmd.sh`는 백업 상태를 살펴보는 `status` 명령을 제공합니다. 출력은 다음과 같습니다:

```
# ./seaf-backup-cmd.sh status
Total number of libraries: xxx
Number of synchronized libraries: xxx
Number of libraries waiting for sync: xxx
Number of libraries syncing: xxx
Number of libraries failed to sync: xxx

List of syncing libraries:
xxx
xxx

List of libraries failed to sync:
xxx
xxx
```

몇가지 이유로 라이브러리 백업에 실패할 수 있습니다:

- 주 서버의 일부 데이터 손상. 데이터는 최근 상태 또는 기록상 남아있는 상태로 되돌립니다. 백업 처리 과정은 전체 기록을 동기화하므로 기록이 손상되면 백업에 실패합니다.
- 라이브러리를 이전 상태로 복원하려면 주 서버에서 seaf-fsck를 실행하십시오.

### 라이브러리 동기화 직접 실행

`sync` 명령을 사용하여 라이브러리의 백업 계획을 직접 수립할 수 있습니다:

```
# ./seaf-backup-cmd.sh sync <library id>
```

이 명령은 백업이 끝나기 전까지 다른 작업을 막습니다.

### 백업 오류 처리

`sync` 명령의 `--force` 옵션은 백업 과정중 실패한 부분을 강제로 마무리할 때 사용할 수 있습니다. 완전한 백업 실패는 주 서버 라이브러리에 있는 데이터의 손상을 야기합니다. `--force` 옵션은 손상 객체를 무시하고 백업하고 백업을 끝낼지를 물어봅니다.

백업 오류를 찾았따면 다음 두 과정을 따르십시오:

1. 주 서버에서 seaf-fsck를 실행하여 문제가 생긴 라이브러리를 검사하십시오. fsck는 라이브러리를 최근 상태로 돌려 손상 상태를 수정합니다.
2. `seaf-backup-cnd.sh sync --force <library id>` 명령을 백업 서버에서 실행하십시오.

## 백업 서버에서 복원

백업 서버는 완벽하게 동작하는 Seafile 인스턴스이므로, 주 서버가 치명적인 손상을 입고 나면 백업 서버로 서비스를 전환할 수 있습니다. 그러나 백업 서버로 전환하기 전 몇가지 요점을 고려해야 합니다.

- 최대한 충분한 시간을 잡고 주 서버를 복구해봐야 합니다. seaf-fsck를 실행하면 주 서버의 일일 손상 대부분을 수정합니다.
- 백업 서버의 실시간에 가까운 기능으로 백업 서버의 데이터는 여전히 주 서버에 저장한 데이터보다는 조금 시기가 지납니다. 이는 특히 라이브러리 백업에 실패했을 경우에 해당합니다.

백업 서버로 전환하기 전, 우선, "백업에 실패한" 라이브러리를 동기화하는 모든 클라이언트의 동기화를 해제해야합니다.

`seaf-backup-cmd.sh` 출력은 다음과 같다고 가정하겠습니다:

```
List of libraries failed to sync:
f690ea2c-fe4d-459a-ba1e-165cdc6df391
e2df70b5-cd80-496f-98cf-c9f038cf1307
```

백업 서버의 MySQL에서 다음 명령을 실행하십시오:

```
use seafile-db;
delete from RepoUserToken where repo_id in ('f690ea2c-fe4d-459a-ba1e-165cdc6df391', 'e2df70b5-cd80-496f-98cf-c9f038cf1307');
```

