# LDAP/AD에서 그룹 가져오기

버전 4.1.0부터 전문가판에서는 LDAP 또는 액티브 디렉터리에서 그룹 가져오기(동기화)를 지원합니다.

## 동작 방식

가져오기 또는 동기화 처리 과정에서는 LDAP 디렉터리 서버의 그룹을 Seafile의 자체 데이터베이스의 그룹과 대응합니다. 이 처리 과정은 단일 방식으로 진행합니다.

* 데이터베이스의 그룹 바뀜은 LDAP에 다시 영향을 주지 않습니다
* "구성원을 그룹 관리자로 설정" 항목을 제외한 데이터베이스의 그룹 바쓈은 다음 LDAP 동기화 과정에서 덮어씁니다. 구성원 추가, 삭제는 LDAP 서버에서만 가능합니다.
* 가져온 그룹의 생성 담당자는 시스템 관리자입니다.

AD와 같은 일부 LDAP 서버에서는 다른 그룹의 구성원에 대한 그룹 설정이 가능합니다. 이를 "중첩 그룹"이라 합니다. Seafile 에서는 중첩 그룹 동기화 처리 과정을 지원합니다. 그룹 B가 그룹 A의 구성 그룹이라고 가정하면 결과는 다음과 같습니다. 그룹 B의 모든 구성원은 그룹 A와 그룹 B의 구성원으로 가져옵니다.

동작 방식에는 두가지가 있습니다:

* 주기 동작: 동기화 처리 과정을 고정 주기별로 실행합니다
* 수동 동작: 동기화 동작을 한 번 실행할 수 있는 스크립트가 있습니다

## 준비

python-ldap 라이브러리를 시스템에 설치해야합니다.

데비안 또는 우분투

```
sudo apt-get install python-ldap
```

CentOS 또는 레드햇

```
sudo yum install python-ldap
```

## 설정

LDAP 그룹 동기화를 활성화하기 전, LDAP 인증을 설정해야합니다. 자세한 내용을 보려면 [LDAP 사용 설정](using_ldap.md)을 참고하십시오.

다음은 LDAP 그룹 동기화 관련 설정 항목입니다. [ccnet.conf](../config/ccnet-conf.md)의 "[LDAP_SYNC]" 섹션에 있습니다.

* **ENABLE_GROUP_SYNC**: LDAP 그룹 동기화를 활성화하려면 "true"로 설정하십시오
* **SYNC_INTERVAL**: 동기화 주기. 단위는 분입니다. 기본값은 60분입니다.
* **GROUP_OBJECT_CLASS**: 그룹 객체 검색에 사용하는 클래스의 이름. 액티브 디렉터리에서는, 보통 "group" 입니다. OpenLDAP 또는 다른 서비스에서는, LDAP 서버에 따라 "groupOfNames" 또는 "groupOfUniqueNames"를 사용할 수 있습니다. 기본값은 "group" 입니다.
* **GROUP_FILTER**: 그룹 검색에 활용할 추가 필터. 이 값을 설정하면, 검색 실행에 활용할 최종 필터는 "(&(objectClass=GROUP_OBJECT_CLASS)(GROUP_FILTER))" 입니다. 설정하지 않으면 "(objectClass=GROUP_OBJECT_CLASS)" 입니다.
* **GROUP_MEMBER_ATTR**: 그룹 구성원을 불러올 때 사용할 속성 필드. 대부분 디렉터리 서버에서 속성 기본값은 "member"입니다.

그룹 검색 기반은 ccnet.conf의 "[LDAP]" 섹션의 "BASE_DN"입니다.

액티브 디렉터리 설정 예제는 다음과 같습니다:

```
[LDAP]
HOST = ldap://192.168.1.123/
BASE = cn=users,dc=example,dc=com
USER_DN = administrator@example.local
PASSWORD = secret
LOGIN_ATTR = mail

[LDAP_SYNC]
ENABLE_GROUP_SYNC = true
SYNC_INTERVAL = 60
```

AD에서는 보통 "ENABLE_GROUP_SYNC"을 제외한 기타 설정 항목을 설정할 필요가 없습니다. 다른 설정 항목의 기본값은 AD의 값이기 때문입니다.. LDAP 서버에 별도로 설정한 항목이 있다면 관련 설정 항목 값을 설정하십시오.

OpenLDAP 설정 예제는 다음과 같습니다:

```
[LDAP]
HOST = ldap://192.168.1.123/
BASE = ou=users,dc=example,dc=com
USER_DN = cn=admin,dc=example,dc=com
PASSWORD = secret
LOGIN_ATTR = mail

[LDAP_SYNC]
ENABLE_GROUP_SYNC = true
SYNC_INTERVAL = 60
GROUP_OBJECT_CLASS = groupOfNames
```

**참고** Seafile 서버를 다시 시작하고 나면 주기적 동기화 작업을 바로 진행하진 않습니다. 첫 동기화 주기 처리 후 일정을 수립합니다. 예를 들어 30분마다 동기화하도록 설정했다면, 처음 자동 동기화는 다시 시작하고 나서 30분 후에 일어납니다. 즉시 동기화 처리하려면, 직접 실행해야합니다. 이 방법은 다음 섹션에서 다룹니다.

동기화를 실행하고 나면 logs/seafevents.log에서 다음과 같은 기록 메시지를 볼 수 있습니다. 그리고 시스템 관리자 페이지에서 그룹을 볼 수 있어야합니다.

```
[2015-03-30 18:15:05,109] [DEBUG] create group 1, and add dn pair CN=DnsUpdateProxy,CN=Users,DC=Seafile,DC=local<->1 success.
[2015-03-30 18:15:05,145] [DEBUG] create group 2, and add dn pair CN=Domain Computers,CN=Users,DC=Seafile,DC=local<->2 success.
[2015-03-30 18:15:05,154] [DEBUG] create group 3, and add dn pair CN=Domain Users,CN=Users,DC=Seafile,DC=local<->3 success.
[2015-03-30 18:15:05,164] [DEBUG] create group 4, and add dn pair CN=Domain Admins,CN=Users,DC=Seafile,DC=local<->4 success.
[2015-03-30 18:15:05,176] [DEBUG] create group 5, and add dn pair CN=RAS and IAS Servers,CN=Users,DC=Seafile,DC=local<->5 success.
[2015-03-30 18:15:05,186] [DEBUG] create group 6, and add dn pair CN=Enterprise Admins,CN=Users,DC=Seafile,DC=local<->6 success.
[2015-03-30 18:15:05,197] [DEBUG] create group 7, and add dn pair CN=dev,CN=Users,DC=Seafile,DC=local<->7 success.
```

## 동기화 직접 실행

LDAP 동기화를 직접 실행하려면,

```
cd seafile-server-lastest
./pro/pro.py ldapsync
```

