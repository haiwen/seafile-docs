# 윈도우에서 리눅스로 이전

이 지침서는 윈도우(SQLite 사용)에서 리눅스로 Seafile을 이전하는 방법을 알려드립니다.

### 1. 리눅스에서 Seafile 가동

우선 [Seafile과 SQLite를 가동](../deploy/using_sqlite.md) 준비 하십시오. 그리고 `/home/haiwen` 디렉터리에 Seafile 가동을 준비했다고 가정합니다.

### 2. 설정 파일 및 데이터베이스 바꾸기

#### 리눅스에서 설정 파일 및 데이터베이스 삭제

```
rm /home/haiwen/seahub_settings.py
rm /home/haiwen/seahub.db
rm -r /home/haiwen/seafile-data
cp /home/haiwen/ccnet/seafile.ini /home/haiwen/seafile.ini
rm -r /home/haiwen/ccnet
```

> 참고: `seafile.ini`는 `seafile-data`에 경로를 기록할 떄 사용하며, 나중에 활용하므로, 어딘가에 복사만 해두시고 삭제하지마십시오.

#### 리눅스에 설정 파일 및 데이터베이스 복사

- `seahub_settings.py` 파일을 윈도우의 **seafile-server** 디렉터리에서 `/home/haiwen/` 디렉터리로 복사하십시오

- `seahub.db` 파일을 윈도우의 **seafile-server** 디렉터리에서 리눅스의 `/home/haiwen/` 디렉터리로 복사하십시오

- `seafile-data`의 하위 디렉터리를 윈도우의 **seafile-data** 디렉터리에서 리눅스의 `/home/haiwen/` 디렉터리로 복사하십시오

- `ccnet` 하위 디렉터리를 윈도우의 **seafile-server** 디렉터리에서 `/home/haiwen/` 디렉터리로 복사하십시오

- `/home/haiwen/seafile.ini`파일을 리눅스의 새 **ccnet** 디렉터리로 복사하십시오.

### Seafile 시작

```
./seafile.sh start
./seahub.sh start
```

