# LDAP를 사용하도록 Seafile 전문가판 설정

## Seafile의 LDAP 사용자 관리 동작 방식

Seafile을 LDAP/AD와 통합하면, 시스템 사용자는 두 티어로 구분합니다:

- Seafile의 자체 사용자 데이터베이스에 있는 사용자. 일부 속성은 이 사용자로 붙는데, 시스템 관리 사용자인지, 활성 상태인지 여부 속성이 여기에 해당합니다. 이 티어에는 두 가지 형태의 사용자가 있습니다:
    * 자체 사용자: 이 사용자는 Seafile의 시스템 관리자 인터페이스에서 관리자가 만듭니다. 이 사용자는 `ccnet` 데이터베이스의 `EmailUser` 테이블에 저장합니다.
    * LDAP/AD 서버에서 온 사용자: Seafile에 LDAP/AD 사용자가 로그인하면, LDAP/AD 서버의 사용자 정보를 Seafile 데이터베이스로 가져옵니다. 이 사용자는 `ccnet` 데이터베이스의 `LDAPUsers` 테이블에 저장합니다.
- LDAP/AD 서버 사용자. 이 사용자는 LDAP 서버에 있는 Seafile을 사용하려는 사용자입니다. Seafile은 이 사용자를 직접 다루지 못합니다. 설정 속성을 자체 데이터베이스로 가져옵니다.

Seafile에서 시스템 사용자를 셀 때는 자체 데이터베이스의 **활성** 사용자만 셉니다.

Seafile을 LDAP/AD와 통합하면, 자체 서버와 LDAP 서버 양측에서 사용자를 찾습니다. 두 곳에 사용자가 있으면 시스템에 로그인할 수 있습니다.

## 기본 LDAP/AD 통합

Seafile에서 LDAP/AD를 인증용으로 사용하는데 필요한 유일한 사항은, LDAP/AD서버에 있는 각 사용자의 유일 식별자입니다. Seafile은 전자메일 주소 형식 사용자 식별자만 사용할 수 있습니다. 따라서 유일 식별자 사용에 두가지 선택지만 있습니다:

- 전자메일 주소: 대부분 선택하는 수단입니다. 대부분의 조직에서는 각 구성원에게 유일 전자메일 주소를 할당합니다.
- UserPrincipalName: 액티브 디렉터리에서만 사용하는 사용자 속성입니다. 형식은 `user-login-name@domain-name`이며, 예를 들면 `john@example.com`과 같습니다. 실제 전자메일 주소는 아니지만 유일 식별자로 잘 동작합니다.

### 액티브 디렉터리에 연결

사용자 인증에 AD를 사용한다면, 다음 줄을 ccnet.conf에 추가하십시오.

전자메일 주소를 유일 식별자로 사용할 경우:

    [LDAP]
    HOST = ldap://192.168.1.123/
    BASE = cn=users,dc=example,dc=com
    USER_DN = administrator@example.local
    PASSWORD = secret
    LOGIN_ATTR = mail

UserPrincipalName을 유일 식별자로 사용한다면:

    [LDAP]
    HOST = ldap://192.168.1.123/
    BASE = cn=users,dc=example,dc=com
    USER_DN = administrator@example.local
    PASSWORD = secret
    LOGIN_ATTR = userPrincipalName

UserPrincipalName을 유일 식별자로 사용한다면:

* HOST: 호스트의 LDAP URL입니다. ldap:// ldaps:// ldapi://를 지원합니다. ldap://ldap.example.com:389처럼 URL에 포트 번호를 넣을 수 있습니다. TLS를 사용하려면 LDAP 서버에 LDAPS 포트에서 응답 대기하도록 설정하고 ldaps://를 지정하십시오. TLS에 대한 자세한 내용은 아래에 다룹니다.
* BASE: 디렉터리 서버에서 요청문을 실행할 때 사용할 루트 구별 이름(DN)입니다. **루트 DN(e.g. dc=example,dc=com)을 BASE로 사용할 수 없습니다**.
* USER_DN: 디렉터리 서버에 연결할 때 Seafile에서 사용할 사용자의 식별 이름입니다. BASE 기반의 모든 노드에 접근하려면 해당 사용자는 충분한 권한을 가지고 있어야합니다. 관리자 그룹의 사용자 활용을 추천합니다.
* PASSWORD: 위 사용자의 암호.
* LOGIN_ATTR: 사용자 유일 식별자에 사용하는 속성입니다. `mail` 또는 `userPrincipalName`을 사용하십시오.

BASE 및 USER_DN을 설정하는 요령:

* BASE 값을 설정하려면, 도메인 컨트롤러 GUI에 있는 조직 계층을 우선 탐색하십시오.
    * 모든 사용자가 Seafile을 쓸 수 있게 한다면, 'cn=users,dc=yourdomain,dc=com'을 BASE 값으로 활용할 수 있습니>다(그리고 필요에 따라 적당히 조절하십시오).
    * 사용자를 일부 OU (조직 단위)로 한정하려면, 도메인 컨트롤러에서 `dsquery` 명령을 실행하여 이 OU에 있는 DN을 찾으십시오. 예를 들어, OU가 'staffs'면, 'dsquery ou -name staff'을 실행하시면 됩니다. 더 자세한 내용은 [여기](https://technet.microsoft.com/en-us/library/cc770509.aspx)에 있습니다.
* AD는 USER_DN 옵션에 'user@domain.name' 형식을 지원합니다. 예를 들어 USER_DN에 administrator@example.com 값을 사용할 수 있습니다. 때로는 도메인 컨트롤러에서 이 형식을 인지하지 못할 수도 있습니다. 사용자 DN을 찾을 때 `dsquery` 명령을 사용할 수 있습니다. 예를 들면 `seafileuser` 이름을 가진 사용자라면 `dsquery user -name seafileuser`를 실행하십시오. 더 자세>한 내용은 [여기에 있습니다](https://technet.microsoft.com/en-us/library/cc725702.aspx).

### 기타 LDAP 서버로 연결

ccnet.conf에 다음 설정 항목 값을 추가하십시오:

    [LDAP]
    HOST = ldap://192.168.1.123/
    BASE = ou=users,dc=example,dc=com
    USER_DN = cn=admin,dc=example,dc=com
    PASSWORD = secret
    LOGIN_ATTR = mail

이 설정 항목은 이전 섹션에 언급한 항목과 의미가 같습니다. 기타 LDAP 서버에서는 사용자 유일 식별자로 `mail` 속성을 사용할 수 있습니다.

### LDAP 설정 시험

5.0.0 전문가판에서부터 LDAP 설정을 확인하는 명령행 도구를 제공합니다.

이 도구를 사용하려면 `python-ldap` 꾸러미를 시스템에 설치했는지 확인하십시오.

```
sudo apt-get install python-ldap
```

그러면 다음 명령으로 시험을 진행할 수 있습니다:

```
cd seafile-server-latest
./pro/pro.py ldapsync --test
```

시험 스크립트는 ccnet.conf의 `[LDAP]` 섹션에 설정한 LDAP 설정을 시험합니다. 모든 검사 대상 동작이 반응하면, 검색 결과의 첫 10명의 사용자를 출력합니다. 설정을 제대로 하지 않았다면 설정상 발생할 수 있는 오류 메시지를 출력합니다.

## LDAP/AD 사용자 동기화 설정(선택)

Seafile 전문가판에서는 사용자가 로그인했을 때 자체 데이터베이스로 사용자 정보를 가져오는 경우를 제외하고, LDAP/AD 서버의 사용자 정보를 자체 데이터베이스로 주기적으로 동기화하도록 Seafile을 설정할 수 있습니다.

- 사용자 성명, 부서, 연락처 전자메일 주소를 자체 데이터베이스에 동기화할 수 있습니다. 사용자는 특정 사용자를 쉽게 검색할 때 이 정보를 활용할 수 있습니다.
- 사용자의 윈도우 또는 유닉스 로그인 이름을 자체 데이터베이스에 동기화할 수 있습니다. 사용자 자신의 익숙한 로그인 ID로 로그인할 수 있습니다.
- LDAP/AD에서 사용자를 제거하면 Seafile의 관련 사용자를 비활성화합니다. 삭제하지 않으면, 해당 사용자는 Seafile로 파일을 여전히 동기화하거나 웹 인터페이스로 접근할 수 있습니다.

동기화 과정이 끝나면 사용자 프로파일 페이지에서 사용자의 성명, 부서, 연락처 전자메일 주소를 볼 수 있습니다.

### 액티브 디렉터리

액티브 디렉터리를 사용한다면 다음 설정 항목을 ccnet.conf에 추가하십시오:

```
[LDAP]
......

[LDAP_SYNC]
ENABLE_USER_SYNC = true
SYNC_INTERVAL = 60
USER_OBJECT_CLASS = person
ENABLE_EXTRA_USER_INFO_SYNC = true
FIRST_NAME_ATTR = givenName
LAST_NAME_ATTR = sn
DEPT_ATTR = department
UID_ATTR = sAMAccountName
```

각 설정 항목의 의미는 다음과 같습니다:

- **ENABLE_USER_SYNC**: LDAP 사용자 동기화를 활성화하려면 "true"로 설정하십시오
- **SYNC_INTERVAL**: 동기화 주기. 단위는 분입니다. 기본 값은 60분입니다.
- **USER_OBJECT_CLASS**: 사용자 객체 검색시 사용할 클래스 이름. 액티브 디렉터리에서는 보통 "person"이며, 기본값입니다.
- **ENABLE_EXTRA_USER_INFO_SYNC**: 사용자 성명, 부서, 윈도우 로그인 이름 등의 추가 사용자 정보 동기화를 활성합니다.
- **FIRST_NAME_ATTR**: 사용자의 이름 속성. 기본값은 "givenName" 입니다.
- **LAST_NAME_ATTR**: 사용자 이름의 성에 해당하는 속성. 기본값은 "sn" 입니다.
- **USER_NAME_REVERSE**: 중국어와 같은 일부 언어에서는 성과 이름 순서가 바뀌어 나타납니다. 필요하다면 이 설정 항목 값을 설정하십시오.
- **DEPT_ATTR**: 사용자 부서 속성. 기본값은 "department" 입니다.
- **UID_ATTR**: 윈도우 로그인 이름 속성입니다. 동기화하면, 사용자는 윈도우 로그인 이름으로 로그인할 수 있습니다. AD에서, `sAMAccountName` 속성을 `UID_ATTR` 값으로 사용할 수 있습니다.

`userPrincipalName`을 사용자의 유일 식별자로 선택하면, Seafile에서는 실제 사용자에게 알림 전자메일을 보낼 때 활용할 전자메일 주소로 사용할 수 없습니다. AD의 사용자가 전자메일 주소 속성을 지니고 있다면 Seafile 자체 데이터베이스에 이 전자메일 주소를 동기화할 수 있습니다. 이렇게 하면 Seafile에서 이 속성을 활용하여 전자메일을 보낼 수 있습니다. 설정 항목은 다음과 같습니다:
- **CONTACT_EMAIL_ATTR**: 보통 이 값을 `mail` 속성에 설정할 수 있습니다.

### 기타 LDAP 서버

다음 설정 항목 값을 ccnet.conf에 추가하십시오:

```
[LDAP]
......

[LDAP_SYNC]
ENABLE_USER_SYNC = true
SYNC_INTERVAL = 60
USER_OBJECT_CLASS = userOfNames
ENABLE_EXTRA_USER_INFO_SYNC = true
FIRST_NAME_ATTR = givenName
LAST_NAME_ATTR = sn
DEPT_ATTR = department
UID_ATTR = uid
```

각 설정 항목의 의미는 다음과 같습니다:

- **ENABLE_USER_SYNC**: LDAP 사용자 동기화를 활성화하려면 "true"로 설정하십시오
- **SYNC_INTERVAL**: 동기화 주기. 단위는 분입니다. 기본 값은 60분입니다.
- **USER_OBJECT_CLASS**: 사용자 객체를 검색할 때 활용하는 클래스의 이름. OpenLDAP에서는 "userOfNames"를 활용할 수 있습니다. 기본값은 "person" 입니다.
- **ENABLE_EXTRA_USER_INFO_SYNC**: 성명, 부서, 윈도우/유닉스 로그인 이름 등 추가 사용자 정보 동기화를 활성화합니다.
- **FIRST_NAME_ATTR**: 사용자의 이름 속성. 기본값은 "givenName" 입니다.
- **LAST_NAME_ATTR**: 사용자 이름의 성에 해당하는 속성. 기본값은 "sn" 입니다.
- **USER_NAME_REVERSE**: 중국어와 같은 일부 언어에서는 성과 이름 순서가 바뀌어 나타납니다. 필요하다면 이 설정 항목 값을 설정하십시오.
- **DEPT_ATTR**: 사용자 부서 속성. 기본값은 "department" 입니다.
- **UID_ATTR**: 윈도우/유닉스 로그인 이름 속성입니다. 동기화 처리했다면, 동기화한 사용자는 윈도우/유닉스 로그인 이름으로 로그인할 수 있습니다. OpenLDAP에서는, `uid` 또는 유사 속성을 사용할 수 있습니다.

### 동기화 수동 실행

LDAP 동기화 설정을 시험해보려면 동기화 명령을 직접 실행하시면 됩니다.

LDAP 동기화를 직접 실행하려면,

```
cd seafile-server-lastest
./pro/pro.py ldapsync
```

### LDAP 동기화 중 새 사용자를 가져오지 못함

기본적으로 LDAP 동기화 처리 과정에서 LDAP 서버에 새 사용자 추가를 감지하면 자체 데이터베이스에 해당 사용자를 자동으로 동기화합니다. 그리고 새 사용자를 기본적으로 활성화합니다. 이 과정을 통해 하나 이상의 사용자 라이선스를 이용합니다.

다음 상황을 가정해보겠습니다: LDAP 서버에 상당히 많은 사용자가 있지만, 이 사용자를 Seafile에 추가하기에 충분하지 않은 라이선스를 구매했습니다. LDAP 동기화를 활성화하면 구매한 모든 라이선스를 호비하고 Seafile 설치를 진행할 수 없습니다. 최적의 방책은 새 사용자가 처음 로그인했을 때만 Seafile에 추가하는 방식입니다. 그리고 LDAP 동기화는 기존의 사용자에 대해서만 LDAP 서버에서 정보를 동기화처리합니다. 다음 설정 항목 값은 정확히 이 목적으로 활용합니다:

```
[LDAP_SYNC]
IMPORT_NEW_USER = false
```

## 고급 LDAP/AD 통합 설정 항목

### 다중 BASE

다중 베이스 DN은 회사에 Seafile을 사용하려는 조직 단위가 하나 이상일 경우 유용합니다. "BASE" 설정에 베이스 DN을 여러 항목으로 지정할 수 있습니다. DN은 ";" 문자로 구분하며 다음과 같이 설정합니다. `ou=developers,dc=example,dc=com;ou=marketing,dc=example,dc=com`

### 추가 검색 필터

검색 필터는 거대 조직에서 일부 사용자가 Seafile을 사용하려 할 때 유용합니다. "FILTER" 값을 설정하면 필터 조건을 줄 수 있습니다. 이 설정 항목의 값은 표준 LDAP 검색 필터 문법을 따릅니다(https://msdn.microsoft.com/en-us/library/aa746475(v=vs.85).aspx).

사용자 검색에 사용할 최종 필터는 `(&($LOGIN_ATTR=*)($FILTER))`입니다. `$LOGIN_ATTR` 및 `$FILTER` 변수는 개별 설정 항목 값으로 바뀝니다.

예를 들자면, LDAP 설정에 다음 줄을 추가하십시오:

```
FILTER = memberOf=CN=group,CN=developers,DC=example,DC=com
```

최종 검색 필터는 `(&(mail=*)(memberOf=CN=group,CN=developers,DC=example,DC=com))`입니다

참고로 위 예제에서 대소문자는 중요합니다. `memberOf` 속성은 액티브 디렉터리에서만 사용할 수 있습니다.

### Seafile 사용자를 액티브 디렉터리 그룹으로 제한하기

FILTER 옵션을 사용하여 사용자 범위를 각각의 AD 그룹으로 제한할 수 있습니다.

1. 우선 그룹의 DN을 확인하십시오. 다시 말씀드리지만, 도메인 컨트롤러의 `dsquery` 명령을 사용합니다. 예를 들어 그룹 이름이 `seafilegroup`이라면, `dsquery group -name seafilegroup`을 실행하십시오.
2. 다음 줄을 LDAP 설정에 추가하십시오:

```
FILTER = memberOf={output of dsquery command}
```

### LDAP/AD 서버에 TLS로 연결하기

디렉터리 서버에 TLS로 연결하려면 디렉터리 서버에 올바른 SSL 인증서를 설치해야합니다.

Seafile 리눅스 서버 꾸러미 현재 버전은 CentOS에서 컴파일했습니다. 꾸러미에 넣은 LDAP 클라이언트 라이브러리는 이전 리눅스 배포판 버전과 호환되도록 관리합니다. 하지만 제각기 다른 리눅스 배포판은 OpenSSL 라이브러리 경로가 다르고 설정도 다르기 때문에 Seafile이 때로는 디렉터리 서버를 TLS로 연결할 수 없을 때도 있습니다.

Seafile 꾸러미에 들어있는 LDAP 라이브러리(libldap) 버전은 2.4입니다. 리눅스 배포판이 최신일 경우(CentOS 8, 데비안 7, 우분투 12.04 이상), 시스템의 libldap를 대신 사용할 수 있습니다.

우분투 14.04 및 데비안 7/8에서는 압축 파일에 들어있는 LDAP 관련 라이브러리를 라이브러리 경로 밖으로 옮길 때 TLS 연결이 동작하도록 해야합니다.

```
cd ${SEAFILE_INSTALLATION_DIR}/seafile-server-latest/seafile/lib
mkdir disabled_libs_use_local_ones_instead
mv liblber-2.4.so.2 libldap-2.4.so.2 libsasl2.so.2 libldap_r-2.4.so.2 disabled_libs_use_local_ones_instead/
```

CentOS 6에서는 libnssutil 라이브러리를 옮겨야합니다:

```
cd ${SEAFILE_INSTALLATION_DIR}/seafile-server-latest/seafile/lib
mkdir disabled_libs_use_local_ones_instead
mv libnssutil3.so disabled_libs_use_local_ones_instead/
```

이 작업으로 라이브러리 검색 경로에 포함한 라이브러리를 제거합니다. 
서버를 시작할 때 시스템 라이브러리를(설치했으면) 대신 찾고 사용합니다.
Seafile 설치를 업데이트 한 후 이 변경 과정을 반복합니다.


### 페이지 단위 결과 반환 확장 기능 활용

LDAP 프로토콜 버전 3에서는 "페이지 단위 결과 출력"(PR) 확장 기능을 지원합니다. 사용자가 상당히 많을 경우 이 선택지를 활용하여 사용자 조회시 시스템 성능을 상당히 끌어올릴 수 있습니다. 최근 대부분 디렉터리 서버에서는 이 확장 기능을 지원합니다.

Seafile 전문가판에서는 ccnet.conf의 LDAP 섹션에 이 설정 항목을 추가하여 PR을 활성화하십시오:

```
USE_PAGED_RESULT = true
```

### 리퍼럴 따르기

전문가판 4.0.4 부터, Seafile에서는 LDAP 검색시 자동 리퍼럴 따름 동작을 지원합니다. 여러 사용자가 다중 디렉터리 서버에 퍼져 LDAP 또는 AD 서버가 나뉘어 있을 때 유용합니다. 리퍼럴에 대한 더 많은 정보는 [이 게시글](https://technet.microsoft.com/en-us/library/cc978014.aspx)에서 찾아볼 수 있습니다.

설정하려면 ccnet.conf의 [LDAP] 섹션에 다음 설정 항목을 추가하십시오:

```
FOLLOW_REFERRALS = true
```

