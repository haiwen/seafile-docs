# Seafile 클러스터 업그레이드

## 주/부 버전 업그레이드

Seafile 에서는 주/부 버전에 새 기능을 추가합니다. 일부 데이터베이스 테이블을 수정하거나 검색 색인을 업데이트해야 할 수도 있습니다. 보통 클러스터 업그레이드는 다음 단계를 따릅니다:

1. 데이터베이스를 업그레이드하십시오
2. 프론트엔드 및 백엔드 노드의 심볼릭 링크를 최신 버전을 가리키도록 업데이트하십시오.
3. 각 노드의 설정 파일을 업데이트하십시오.
4. 백엔드 노드의 검색 색인을 업데이트하십시오.

보통 클러스터 업그레이드 진행시 다음 과정 진행이 필요합니다:

1. 프론트엔드 노드에서 업그레이드 스크립트(예: ./upgrade/upgrade_4_0_4_1.sh)를 실행하십시오.
2. 기타 노드에서 마이너 업그레이드 스크립트(./upgrade/minor_upgrade.sh)를 실행하여 심볼릭 링크를 업데이트하십시오
3. 각 버전에 대해 문서 내용을 따라 각 노드에서 설정 파일을 업데이트하십시오
4. 필요하다면 백엔드 노드의 이전 검색 색인을 삭제하십시오

## 업그레이드 유지

유지보수 업그레이드는 간단하며, 각 노드에서 `./upgrade/minor_upgrade.sh`스크립트를 실행하여 심볼릭 링크를 업데이트 하기만 하면 됩니다.

## 버전별 절차

### v5.0에서 v5.1로

장고를 1.8로 업그레이드 했으므로 COMPRESS_CACHE_BACKEND 값을 바꾸어야합니다

```
   -    COMPRESS_CACHE_BACKEND = 'locmem://'
   +    COMPRESS_CACHE_BACKEND = 'django.core.cache.backends.locmem.LocMemCache'
```

### v4.4에서 v5.0으로

v5.0에서 도입한 데이터베이스 스키마가 바뀌었으며 모든 설정 파일(ccnet.conf, seafile.conf, seafevents.conf, seahub_settings.py)을 설정 디렉터리에 한데 옮겨 모아두었습니다.

업그레이드시 다음 단계를 따라가십시오:

- 프론트엔드 노드에서 업그레이드 스크립트를 실행하여 데이터베이스를 업그레이드하십시오.
```
./upgrade/upgrade_4.4_5.0.sh
```
- 그 다음, 기타 프론트엔드 노드와 백그라운드 노드에서 `SEAFILE_SKIP_DB_UPGRADE` 환경 변수 값을 활성화해둔 상태에서 업그레이드 스크립트를 실행하십시오:
```
SEAFILE_SKIP_DB_UPGRADE=1 ./upgrade/upgrade_4.4_5.0.sh
```

업그레이드 과정이 끝나면, 설정 파일은 conf/ 폴더로 이동해두어야합니다.

```
conf/
  |__ ccnet.conf
  |__ seafile.conf
  |__ seafevent.conf
  |__ seafdav.conf
  |__ seahub_settings.conf
```


### v4.3에서 v4.4로

v4.3에서 v4.4로 업그레이드할 때 데이터베이스 및 검색 색인 부분에서 업그레이드할 부분은 없습니다. 업그레이드를 수행할 때 다음 과정을 따르십시오:

1. 부 버전(minor) 업그레이드 스크립트를 프론트엔드 노드 및 백엔드 노드에서 실행하십시오

### v4.2에서 v4.3으로

v4.3에서는 v4.2 버전으로부터 바뀐 테이블이 없습니다. 하지만 이전 검색 색인을 삭제하고 다시 만듭니다.

COMPRESS_CACHE_BACKEND = 'django.core.cache.backends.locmem.LocMemCache' 새 옵션을 seahub_settings.py에 추가해야합니다

이전 비밀키는 임의성이 충분하지 않으므로 seahub_settings.py의 비밀 키를 다시 만드십시오.

업그레이드시 다음 단계를 따라가십시오:

1. 프론트엔드 노드에서 업그레이드 스크립트를 실행하여 seahub_settings.py를 수정하십시오
2. 각 노드의 seahub_settings.py를 수정하여 비밀 키를 새 키로 교체하고 COMPRESS_CACHE_BACKEND 옵션을 추가하십시오
3. 프론트엔드와 백엔드 노드의 부 버전(minor) 업그레이드 스크립트를 실행하십시오
4. 백엔드 노드의 이전 검색 색인(pro-data/search 폴더)을 삭제하십시오
5. 백엔드 노드의 이전 오피스 미리보기 출력 폴더(/tmp/seafile-office-output)를 삭제하십시오

