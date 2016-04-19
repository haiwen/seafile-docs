# Seafile
## Upgrade with MySQL or PostgreSQL

First, download the new version, for example seafile-server_1.6.0_x86-64.tar.gz, and extract it to the directory where you put all Seafile related staff. You should have a directory layout similar to this:

<pre>
haiwen
   -- seafile-server-1.5.0
   -- seafile-server-1.6.0
   -- ccnet
   -- seafile-data
</pre>

## 주 버전 연속 업그레이드(1.5에서 1.6으로 업그레이드하는 방식)

1.5.0에서 1.6.0으로 업그레이드 하거나 1.5.0에서 1.6.1로 업그레이드 하는 방식이 주 버전 연속 업그레이드 방식입니다. 다음 네 단계를 거칩니다:

1. Seafile/Seahub를 멈춥니다
2. 아바타 폴더와 데이터베이스 테이블을 업데이트합니다
3. Nginx/Apache 설정을 업데이트합니다
4. Seafile/Seahub를 다시 시작합니다

### 2. 아바타 폴더 및 데이터베이스 테이블 업데이트(MySQL 및 Seafile 서버 2.1.1 이후)

Seafile 서버 2.1.1 부터 업그레이트 스크립트로 아바타 폴더와 데이터베이스를 업그레이드할 수 있습니다. 이 스크립트는 `upgrade_X.X_Y.Y.sh`같은 이름이 붙습니다. 예를 들어, Seafile 서버 2.0.0에서 Seafile 서버 2.1.1로 업그레이드 할 경우 `upgrade_2.0_2.1.sh`  스크립트를 실행해야합니다.

```sh
cd seafile-server-2.1.1/
./upgrade/upgrade_2.0_2.1.sh
```

이 스크립트는 아바타 폴더와 데이터베이스 테이블을 업데이트합니다.

### 2. 아바타 폴더 및 데이터베이스 테이블 업데이트(PostgreSQL 및 Seafile 서버 2.1.1 이전 버전용)

Seafile 서버 2.1.1을 사용하거나 PostgreSQL을 사용한다면 다음 과정을 직접 거쳐야합니다:

- 아바타 폴더 심볼릭 링크 업데이트
- 데이터베이스 테이블 업데이트

#### 아바타 심볼릭 링크 업데이트

Assume your top level directory is `/data/haiwen/`, and you are upgrading to seafile server version 1.6.0:

```
cd /data/haiwen
cp -a seafile-server-1.6.0/seahub/media/avatars/* seahub-data/avatars/
rm -rf seafile-server-1.6.0/seahub/media/avatars
#the new server avatars' folder will be linked to the updated avatars folder
ln -s -t seafile-server-1.6.0/seahub/media/  ../../../seahub-data/avatars/
```

#### 데이터베이스 테이블 업그레이드

When a new version of seafile server is released, there may be changes to the database of seafile/seahub/ccnet. We provide the sql statements to update the databases:

- `upgrade/sql/<VERSION>/mysql/seahub.sql`, for changes to seahub database
- `upgrade/sql/<VERSION>/mysql/seafile.sql`, for changes to seafile database
- `upgrade/sql/<VERSION>/mysql/ccnet.sql`, for changes to ccnet database

To apply the changes, just execute the sqls in the correspondent database. If any of the sql files above do not exist, it means the new version does not bring changes to the correspondent database.

```sh
seafile-server-1.6.0
├── seafile
├── seahub
├── upgrade
    ├── sql
        ├── 1.6.0
            ├── mysql
                ├── seahub.mysql
                ├── seafile.mysql
                ├── ccnet.mysql
```


### 3. Nginx/Apache 설정 업데이트

Nginx:

```
  location /media {
      root /data/haiwen/seafile-server-1.6.0/seahub;
  }
```

 Apache:

```
Alias /media  /data/haiwen/seafile-server-1.6.0/seahub/media
```

**Tip:**
<code>seafile-server-latest</code> 심볼릭 링크를 만들어 현재 Seafile 서버 폴더를 가리칠 수 있습니다(Seafile 서버 2.1.0부터 <code>setup-seafile.sh</code> 스크립트에서 심볼링 링크를 만듬). 다음 업그레이드 스크립트를 실행할 때마다 <code>seafile-server-latest</code> 심볼릭 링크는 최신 Seafile 서버 폴더를 가리킵니다.

In this case, you can write:

```
    location /media {
        root /data/haiwen/seafile-server-latest/seahub;
    }
```

Apache:

```
Alias /media  /data/haiwen/seafile-server-latest/seahub/media
```

이 방법으로 Seafile 서버를 업그레이드할 때마다 더 이상 Nginx/Apache 설정 파일을 업데이트할 필요가 없습니다.


### 4. Seafile/Seahub/Nginx/Apache 다시 시작

After done above updating, now restart Seafile/Seahub/Nginx/Apache to see the new version at work!

## Noncontinuous Upgrade (like from 1.1 to 1.3)

You may also upgrade a few versions at once, e.g. from 1.1.0 to 1.3.0.
The procedure is:

1. upgrade from 1.1.0 to 1.2.0;
2. upgrade from 1.2.0 to 1.3.0.


## 부 버전 업그레이드 (1.5.0에서 1.5.1로 업그레이드 하는 방식)

부 버전 업그레이드는 1.5.0에서 1.5.1로 업그레이드 하는 방식과 같습니다.

디렉터리 구조는 다음과 같습니다

<pre>
haiwen
   -- seafile-server-1.5.0
   -- seafile-server-1.5.1
   -- ccnet
   -- seafile-data
</pre>

### 아바타 링크 업데이트

스크립트를 제공했으니, 실행만 하십시오:

```sh
cd seafile-server-1.5.1
upgrade/minor-upgrade.sh
```

### Nginx/Apache 설정 업데이트

Nginx:

```
  location /media {
      root /data/haiwen/seafile-server-1.5.1/seahub;
  }
```

 Apache:

```
Alias /media  /data/haiwen/seafile-server-1.5.1/seahub/media
```

### Seafile/Seahub/Nginx/Apache 다시 시작

After done above updating, now restart Seafile/Seahub/Nginx/Apache to see the new version at work!

