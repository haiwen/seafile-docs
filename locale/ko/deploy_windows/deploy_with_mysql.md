# Seafile 윈도우 서버 및 MySQL 가동

## 준비

- [Seafile 윈도우 서버 다운로드 및 설치](download_and_setup_seafile_windows_server.md)
- Seafile 윈도우 서버를 멈추십시오
  - Seafile 서버 트레이 아이콘에 마우스 커서를 두고 마우스 오른쪽 단추를 누르십시오
  - "Seafile 서버 끝내기"를 선택하십시오
- MySQL 서버가 동작 중인지 확인하십시오

### MySQL-python 라이브러리 설치

- https://pypi.python.org/pypi/MySQL-python/1.2.4 에서 윈도우 설치 프로그램을 다운로드하십시오
- 다운로드한 exe 파일을 두 번 눌러 설치하십시오

## MySQL 데이터베이스 만들기

다음을 만들어야합니다:

- ccnet/seafile/seahub 데이터베이스
- 이 데이터베이스에 접근할 새 사용자

터미널(cmd, Win + R, cmd)을 열고 허가 받은 사용자로 MySQL에 로그인하십시오:
```
mysql -u root -p
```

MySQL 서버에서 아래 SQL 구문을 실행하십시오:

```
create database `ccnet-db` character set = 'utf8';
create database `seafile-db` character set = 'utf8';
create database `seahub-db` character set = 'utf8';

create user 'seafile'@'localhost' identified by 'your secure password';

GRANT ALL PRIVILEGES ON `ccnet-db`.* to `seafile`;
GRANT ALL PRIVILEGES ON `seafile-db`.* to `seafile`;
GRANT ALL PRIVILEGES ON `seahub-db`.* to `seafile`;
```

## Seafile 설정 수정

* 다음 줄을 **ccnet/ccnet.conf**에 추가하십시오:

```
[Database]
ENGINE=mysql
HOST=localhost
USER=seafile
PASSWD=your secure password
DB=ccnet-db
```

* **seafile-data/seafile.conf**에 `database` 섹션을 편집하십시오:

```
[database]
type=mysql
host=localhost
user=seafile
password=your secure password
db_name=seafile-db
```

* 다음 줄을 **seahub_settings.py** 에 추가하십시오

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'seahub-db',
        'USER' : 'seafile',
        'PASSWORD' : 'your secure password',
        'HOST' : 'localhost',
    }
}
```

### Seahub 데이터베이스 테이블 만들기

이제 Seahub에서 사용할 데이터베이스 테이블을 만들겠습니다.

Seafile 서버 꾸러미 압축을 `C:/SeafileProgram/seafile-pro-server-3.1.3`에 풀었다고 가정하겠습니다.

윈도우 명령 프롬프트를 열고 다음 명령을 실행하십시오:

```
mysql -u seafile -p seahub-db < C:/SeafileProgram/seafile-server-3.1.3/seahub/sql/mysql.sql
```

## 완료

이제 Seafile 서버를 시작할 수 있습니다.

