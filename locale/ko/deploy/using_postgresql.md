# Seafile
## PostgreSQL 사용

**Note**: Postgres support is still in Beta status and may have some minor bugs. Please use MySQL in production environment.

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

1. Shutdown services by `./seahub.sh stop` and `./seafile.sh stop`. Then, append the following PostgreSQL configurations to 3 config files (you may need to change to fit your configuration).

    Append following lines to [ccnet.conf](../config/ccnet-conf.md):

        [Database]
        ENGINE=pgsql
        HOST=localhost
        USER=seafile
        PASSWD=seafile
        DB=ccnet_db

    Replace the database section in [seafile.conf](../config/seafile-conf.md) with following lines:

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

2. Start seafile by `./seafile.sh start`. There will be several tables created in `ccnet_db` and `seafile_db` if your configuration is correct.

3. Install python-psycopg2 (package name on ubuntu):

        [sudo] apt-get build-dep python-psycopg2

        [sudo] pip install psycopg2

4. Start seahub as follows (assume current path is `/data/haiwen/seafile-server-1.7.0`:

        export CCNET_CONF_DIR=/data/haiwen/ccnet
        export SEAFILE_CONF_DIR=/data/haiwen/seafile-data
        INSTALLPATH=/data/haiwen/seafile-server-1.7.0
        export PYTHONPATH=${INSTALLPATH}/seafile/lib/python2.6/site-packages:${INSTALLPATH}/seafile/lib64/python2.6/site-packages:${INSTALLPATH}/seahub/thirdpart:$PYTHONPATH
        cd seahub
        python manage.py syncdb

    There will be several tables created in `seahub_db`. Then start seahub by `./seahub.sh start`.

## Seahub 관리자 계정 만들기

Assume current path is `/data/haiwen/seafile-server-1.7.0`, and you have exported all the variables above,

    cd seahub
    python manage.py createsuperuser

This command tool will guide you to create a seahub admin.

