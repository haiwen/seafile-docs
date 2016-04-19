# 리눅스에서 Seafile 가동하기

여기서는 미리 빌드한 Seafile 바이너리 꾸러미를 가동하는 방법을 설명하겠습니다.

### 가정/개인 환경에서 Seafile 가동하기

* [SQLite와 Seafile 가동하기](using_sqlite.md)

### 상업/기업체 환경에서 Seafile 가동하기

상업 환경에서는 MySQL 데이터베이스와 Nginx 또는 Apache를 함께 사용하여 Seafile을 가동하도록 하는 설정을 권장합니다. Nginx와 Apache에 익숙하지 않은 분들에게는 Apache보다 설정 방법이 쉬운 Nginx를 추천합니다.

참고: [설치 스크립트로 Seafile 가동하기](https://forum.seafile-server.org/t/seafile-server-installer-for-production-ready-seafile-ce-and-pro-installations/1464)에서 설치 스크립트를 준비했습니다. 설치 관리자는 MariaDB, Memcached, 리버스 프록시용 Nginx를 5분 내로 설정하여  빠르고 간편한 수단을 

다음과 같이 설치 스크립트를 사용하지 않고 Seafile을 직접 설치할 수도 있습니다:

기본:

* [Seafile과 MySQL 가동](using_mysql.md)
* [Seahub와 Nginx 가동](deploy_with_nginx.md)
* [Nginx https 활성화](https_with_nginx.md)
* [Seahub와 Apache 가동](deploy_with_apache.md)
* [Apache https 활성화](https_with_apache.md)

고급:

* [Memcached 추가](add_memcached.md), 사용자가 50명 이상일 경우 memcached 추가는 상당히 중요합니다.
* [시스템 부팅시 Seafile 시작하기](start_seafile_at_system_bootup.md)
* [방화벽 설정](using_firewall.md)
* [Logrotate](using_logrotate.md)

사용자 인증:

Seafile은 몇가지 외부 사용자 인증 방식을 지원합니다.

* [Seafile LDAP 사용 설정](using_ldap.md)
* [시볼레스 인증](shibboleth_config.md)

다른 가동 문제

* [NAT망에서 Seafile 가동](deploy_seafile_behind_nat.md)
* [비 루트 영역에서 Seafile 가동](deploy_seahub_at_non-root_domain.md)
* [SQLite에서 MySQL로 이전](migrate_from_sqlite_to_mysql.md)

사용자 등록 활성화 같은 서버 설정 항목은 [설정 항목](../config/README.md)을 확인하십시오.

Seafile 서버 설치에 문제가 있다면 **이 부분을 읽으십시오**

1. [Seafile 서버 구성 요소 둘러보기](../overview/components.md)를 읽고 Seafile 서버 동작 방식을 이해하십시오. 상당한 시간을 아낄 수 있습니다.
2. [서버 설치 과정의 일반 문제](common_problems_for_setting_up_server.md)
3. [포럼](https://forum.seafile-server.org/)으로 가서 도움을 받으십시오.

## Seafile 서버 업그레이드

* [Seafile 서버 업그레이드](upgrade.md)

## Seafile 서버 꾸러미 처리 사용자

If you want to package seafile yourself, (e.g. for your favorite Linux distribution), you should always use the correspondent tags:

* When we release a new version of seafile client, say 3.0.1, we will add tags `v3.0.1` to ccnet, seafile and seafile-client.
* Likewise, when we release a new version of seafile server, say 3.0.1, we will add tags `v3.0.1-server` to ccnet, seafile and seahub.
* libsearpc는 항상 `v3.0-latest` 태그를 사용합니다.

**참고**: 각 프로젝트의 버전 번호는 태그 이름으로 정하지 않습니다.

