# SQLite에서 MySQL로 이전

우선 MySQL 파이썬 모듈을 설치했는지 확인하십시오. 우분투에서 설치하려면 `apt-get install python-mysqldb` 명령을 활용하십시오.

SQLite에서 MySQL로 이전하는 단계는 다음과 같습니다:

0. Seafile 및 Seahub를 멈춥니다

1. Seafile 설치 경로 상단에 [sqlite2mysql.sh](https://raw.github.com/haiwen/seafile/master/scripts/sqlite2mysql.sh)와 [sqlite2mysql.py](https://raw.github.com/haiwen/seafile/master/scripts/sqlite2mysql.py) 스크립트를 다운로드합니다. 최상단 디렉터리의 예는 /data/haiwen과 같습니다.

2. sqlite2mysql.sh를 실행합니다
```
  chmod +x sqlite2mysql.sh
  ./sqlite2mysql.sh
```
  이 스크립트는 세 파일(ccnet-db.sql, seafile-db.sql, seahub-db.sql)을 만듭니다.

3. `ccnet-db`, `seafile-db`, `seahub-db` 데이터베이스 3개를 만듭니다.
```
  create database `ccnet-db` character set = 'utf8';
  create database `seafile-db` character set = 'utf8';
  create database `seahub-db` character set = 'utf8';
```

4. MySQL 데이터베이스에 sql 파일을 불러옵니다. 예를 들자면:
```
  mysql> use `ccnet-db`
  mysql> source ccnet-db.sql
  mysql> use `seafile-db`
  mysql> source seafile-db.sql
  mysql> use `seahub-db`
  mysql> source seahub-db.sql
```

5. 설정 파일을 수정합니다

  다음 줄을 [ccnet.conf](../config/ccnet-conf.md)에 추가하십시오:

        [Database]
        ENGINE=mysql
        HOST=127.0.0.1
        USER=root
        PASSWD=root
        DB=ccnet-db
        CONNECTION_CHARSET=utf8

    참고: `localhost`를 사용하지 마시고 `127.0.0.1`을 사용하십시오.

    `seafile.conf`의 데이터베이스 섹션을 다음 줄의 내용으로 바꾸십시오:

        [database]
        type=mysql
        host=127.0.0.1
        user=root
        password=root
        db_name=seafile-db
        CONNECTION_CHARSET=utf8

    다음 줄을 `seahub_settings.py`에 추가하십시오:

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'USER' : 'root',
                'PASSWORD' : 'root',
                'NAME' : 'seahub-db',
                'HOST' : '127.0.0.1',
                'OPTIONS': {
                    "init_command": "SET storage_engine=INNODB",
                }
            }
        }

4. Seafile과 Seahub를 다시 시작합니다


**참고**

MySQL 및 SQLite의 약간의 차이점 때문에 사용자 알림을 삭제합니다. 아바타 옆의 알림 단추를 눌렀을 때 사용 중 아이콘만 나타내려면 `user_notifications` 표를 다음과 같이 제거하십시오:

    use seahub-db
    delete from notifications_usernotification;

