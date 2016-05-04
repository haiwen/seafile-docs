# Seafile
## PostgreSQL 사용

**참고**: Postgres 지원은 아직 베타 단계이며, 자잘한 버그가 있습니다. 실 사용 환경에서는 MySQL을 사용하십시오.

## Seafile과 PostgreSQL 가동

## 준비

1. [[Seafile 서버를 다운로드하고 설치]]한 후, seafile 및 seahub를 시작하시고 모든 기능이 동작하는지 확인하십시오.

2. PostgreSQL을 설정하십시오.

        sudo apt-get install postgresql

3. Seafile의 postgres 사용자와 필요한 데이터베이스를 만드십시오(분명히 Seafile에서 사용하는 암호보다 더 안전한 암호를 설정해야합니다).

        sudo -u postgres psql -U postgres -d postgres -c "CREATE USER seafile WITH PASSWORD 'seafile' CREATEDB;"
        createdb ccnet_db -U seafile -W -h localhost
        createdb seafile_db -U seafile -W -h localhost
        createdb seahub_db -U seafile -W -h localhost

3. ``create database ccnet_db encoding 'utf8';`` 같은 질의 명령으로  `ccnet_db`, `seafile_db`, `seahub_db` 데이터베이스 3개를 만드십시오

## 단계

1. `./seahub.sh stop` 및 `./seafile.sh stop` 명령으로 서비스를 끄십시오. 다음 PostgreSQL 설정을 세가지 설정 파일에 추가하십시오(기존의 설정에 맞게 설정 내용을 바꿔야할 수도 있습니다).

    다음 줄을 [ccnet.conf](../config/ccnet-conf.md)에 추가하십시오:

        [Database]
        ENGINE=pgsql
        HOST=localhost
        USER=seafile
        PASSWD=seafile
        DB=ccnet_db

    [seafile.conf](../config/seafile-conf.md)의 데이터베이스 섹션 설정 값을 다음 줄로 바꾸십시오:

        [database]
        type=pgsql
        host=localhost
        user=seafile
        password=seafile
        db_name=seafile_db

    다음 줄을 `seahub_settings.py`에 추가하십시오:

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME' : 'seahub_db',
                'USER' : 'seafile',
                'PASSWORD' : 'seafile',
                'HOST' : 'localhost',
            }
        }

2. `./seafile.sh start` 명령으로 Seafile을 시작하십시오. 올바르게 설정했다면 `ccnet_db` 및 `seafile_db` 데이터베이스에 여러가지 테이블을 만듭니다.

3. python-psycopg2(우분투 꾸러미 이름)를 설치하십시오 :

        [sudo] apt-get build-dep python-psycopg2

        [sudo] pip install psycopg2

4. 다음 명령으로 Seahub를 시작하십시오(현재 경로를 `/data/haiwen/seafile-server-1.7.0`으로 가정):

        export CCNET_CONF_DIR=/data/haiwen/ccnet
        export SEAFILE_CONF_DIR=/data/haiwen/seafile-data
        INSTALLPATH=/data/haiwen/seafile-server-1.7.0
        export PYTHONPATH=${INSTALLPATH}/seafile/lib/python2.6/site-packages:${INSTALLPATH}/seafile/lib64/python2.6/site-packages:${INSTALLPATH}/seahub/thirdpart:$PYTHONPATH
        cd seahub
        python manage.py syncdb

    `seahub_db`에 몇가지 테이블을 만듭니다. 과정이 끝나면 `./seahub.sh start` 명령으로 Seahub를 시작하십시오.

## Seahub 관리자 계정 만들기

현재 경로는 `/data/haiwen/seafile-server-1.7.0`이고, 위에 언급한 모든 변수값을 내보냈다고 가정하겠습니다.

    cd seahub
    python manage.py createsuperuser

이 명령 도구는 Seahub admin 계정을 만드는 절차를 안내합니다.

