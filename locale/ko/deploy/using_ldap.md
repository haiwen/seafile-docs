# Seafile LDAP 사용 설정

참고: 이 문서는 커뮤니티판용입니다. 전문가판을 사용한다면 [Seafile 전문가판 문서](../deploy_pro/using_ldap_pro.md)를 참고하십시오.

## Seafile의 LDAP 사용자 관리 동작 방식

Seafile을 LDAP/AD와 통합하면, 시스템 사용자는 두 티어로 구분합니다:

- Seafile의 자체 사용자 데이터베이스에 있는 사용자. 일부 속성은 이 사용자로 붙는데, 시스템 관리 사용자인지, 활성 상태인지 여부 속성이 여기에 해당합니다. 이 티어에는 두가지 형태의 사용자가 있습니다:
    * 자체 사용자: 이 사용자는 Seafile의 시스템 관리자 인터페이스에서 관리자가 만듭니다. 이 사용자는 `ccnet` 데이터베이스의 `EmailUser` 테이블에 저장합니다.
    * LDAP/AD 서버에서 온 사용자: Seafile에 LDAP/AD 사용자가 로그인하면, LDAP/AD 서버의 사용자 정보를 Seafile 데이터베이스로 가져옵니다. 이 사용자는 `ccnet` 데이터베이스의 `LDAPUsers` 테이블에 저장합니다.
- LDAP/AD 서버 사용자. 이 사용자는 LDAP 서버에 있는 Seafile을 사용하려는 사용자입니다. Seafile은 이 사용자를 직접 다루지 못합니다. 설정 속성을 자체 데이터베이스로 가져옵니다.

Seafile에서 시스템 사용자를 셀 때는 자체 데이터베이스의 **활성** 사용자만 셉니다.

Seafile을 LDAP/AD와 통합하면, 자체 서버와 LDAP 서버 양측에서 사용자를 찾습니다. 두 곳에 사용자가 있으면 시스템에 로그인할 수 있습니다.

## 기본 LDAP/AD 통합

Seafile에서 인증용 LDAP/AD를 사용하는데 필요한 유일한 요소는 LDAP/AD 서버에서 각 사용자가 유일 식별자를 가지고 있어야 한다는 것 하나뿐입니다. Seafile에서는 전자메일 주소 형식 사용자 식별자만 사용할 수 있습니다. 따라서 유일 식별자 사용에 두가지 선택지가 있습니다:

- 전자메일 주소: 대부분 선택하는 수단입니다. 대부분의 조직에서는 각 구성원에게 유일 전자메일 주소를 할당합니다.
- UserPrincipalName: 액티브 디렉터리에서만 사용하는 사용자 속성입니다. 형식은 `user-login-name@domain-name`이며, 예를 들면 `john@example.com`과 같습니다. 실제 전자메일 주소는 아니지만 유일 식별자로 잘 동작합니다.

### 액티브 디렉터리에 연결

사용자 인증에 AD를 사용하려면, 다음 줄을 ccnet.conf에 추가하십시오.

전자메일 주소를 유일 식별자로 사용할 경우:

    [LDAP]
    HOST = ldap://192.168.1.123/
    BASE = cn=users,dc=example,dc=com
    USER_DN = administrator@example.local
    PASSWORD = secret
    LOGIN_ATTR = mail

유일 식별자 UserPrincipalName을 설정할 경우:

    [LDAP]
    HOST = ldap://192.168.1.123/
    BASE = cn=users,dc=example,dc=com
    USER_DN = administrator@example.local
    PASSWORD = secret
    LOGIN_ATTR = userPrincipalName

각 설정 항목의 의미는 다음과 같습니다:

* HOST: 호스트의 LDAP URL입니다. ldap:// ldaps:// ldapi://를 지원합니다. ldap://ldap.example.com:389처럼 URL에 포트 번호를 넣을 수 있습니다. TLS를 사용하려면 LDAP 서버에 LDAPS 포트에서 응답 대기하도록 설정하고 ldaps://를 지정하십시오. TLS에 대한 자세한 내용은 아래에 다룹니다.
* BASE: 디렉터리 서버에서 요청문을 실행할 때 사용할 루트 구별 이름(DN)입니다. **루트 DN(e.g. dc=example,dc=com)을 BASE로 사용할 수 없습니다**.
* USER_DN: 디렉터리 서버에 연결할 때 Seafile에서 사용할 사용자의 식별 이름입니다. BASE 기반의 모든 노드에 접근하려면 해당 사용자는 충분한 권한을 가지고 있어야합니다. 관리자 그룹의 사용자 활용을 추천합니다.
* PASSWORD: 위 사용자의 암호.
* LOGIN_ATTR: 사용자 유일 식별자에 사용하는 속성입니다. `mail` 또는 `userPrincipalName`을 사용하십시오.

BASE 및 USER_DN을 설정하는 요령:

* BASE 값을 설정하려면, 도메인 컨트롤러 GUI에 있는 조직 계층을 우선 탐색하십시오.
    * 모든 사용자가 Seafile을 쓸 수 있게 한다면, 'cn=users,dc=yourdomain,dc=com'을 BASE 값으로 활용할 수 있습니다(그리고 필요에 따라 적당히 조절하십시오).
    * 사용자를 일부 OU (조직 단위)로 한정하려면, 도메인 컨트롤러에서 `dsquery` 명령을 실행하여 이 OU에 있는 DN을 찾으십시오. 예를 들어, OU가 'staffs'면, 'dsquery ou -name staff'을 실행하시면 됩니다. 더 자세한 내용은 [여기](https://technet.microsoft.com/en-us/library/cc770509.aspx)에 있습니다.
* AD는 USER_DN 옵션에 'user@domain.name' 형식을 지원합니다. 예를 들어 USER_DN에 administrator@example.com 값을 사용할 수 있습니다. 때로는 도메인 컨트롤러에서 이 형식을 인지하지 못할 수도 있습니다. 사용자 DN을 찾을 때 `dsquery` 명령을 사용할 수 있습니다. 예를 들면 `seafileuser` 이름을 가진 사용자라면 `dsquery user -name seafileuser`를 실행하십시오. 더 자세한 내용은 [여기에 있습니다](https://technet.microsoft.com/en-us/library/cc725702.aspx).

### 기타 LDAP 서버에 연결

다음 옵션을 ccnet.conf에 추가하십시오:

    [LDAP]
    HOST = ldap://192.168.1.123/
    BASE = ou=users,dc=example,dc=com
    USER_DN = cn=admin,dc=example,dc=com
    PASSWORD = secret
    LOGIN_ATTR = mail

이 설정 항목의 의미는 이전 섹션에서 설명한 바와 동일합니다. 다른 LDAP 서버에서는 사용자의 유일 식별자로 `mail` 속성만을 사용할 수 있습니다.

## 고급 LDAP/AD 통합 옵션

### 다중 BASE

다중 베이스 DN은 업체에서 OU를 하나 이상 두어 Seafile을 사용할 때 유용합니다. "BASE" 설정에 베이스 DN 목록을 지정할 수 있습니다. DN은 `ou=developers,dc=example,dc=com;ou=marketing,dc=example,dc=com`과 같이 ";"으로 나눌 수 있습니다.

### 추가 검색 필터

Seafile 필터는 거대 조직에서 일부 사용자에게 Seafile을 쓸 수 있게 할 경우 매우 유용합니다. "FILTER" 설정으로 필터 값을 지정할 수 있습니다. 이 설정 항목의 값은 표준 LDAP 검색 필터 문법을 따릅니다(https://msdn.microsoft.com/en-us/library/aa746475(v=vs.85).aspx).

사용자 검색용 최종 필터는 `(&($LOGIN_ATTR=*)($FILTER))`이며, 여기서 `$LOGIN_ATTR` 및 `$FILTER` 값은 옵션 값으로 바뀝니다.

예를 들어 LDAP 설정에 다음 줄을 추가하십시오:

```
FILTER = memberOf=CN=group,CN=developers,DC=example,DC=com
```

최종 검색 필터는 `(&(mail=*)(memberOf=CN=group,CN=developers,DC=example,DC=com))` 입니다

참고로 위 예제의 속성 이름 대소문자는 상당히 중요합니다. `memberOf` 속성은 액티브 디렉터리에서만 사용할 수 있습니다.

### Seafile 사용자를 액티브 디렉터리의 그룹으로 제한

FILTER 옵션으로 각각의 AD 사용자 그룹 범위를 제한할 수 있습니다.

1. 우선, 그룹 DN을 찾으십시오. 다시 말해, 도메인 컨트롤러의 `dsquery` 명령을 사용합니다. 예를 들어, 그룹 이름이 `seafilegroup`이면,  `dsquery group -name seafilegroup`을 실행합니다.
2. 다음 줄을 LDAP 설정에 추가하십시오:

```
FILTER = memberOf={output of dsquery command}
```

### LDAP/AD 서버 연결에 TLS 사용

디렉터리 서버에 TLS 방식으로 연결하려면, 디렉터리 서버에 올바른 SSL 인증서를 설치해야합니다.

Seafile 리눅스 서버 꾸러미의 현재 버전은 CentOS에서 컴파일했습니다. 이전 리눅스 배포판과 호환성을 관리할 목적으로 꾸러미에 LDAP 클라이언트 라이브러리를 넣었습니다. 다만 제각기 다른 리눅스 배포판은 OpenSSL 라이브러리가 제각기 다른 경로 또는 설정을 지니고 있기 때문에, TLS로 디렉터리 서버에 연결할 수 없을 때도 있습니다.

Seafile 꾸러미에 있는 LDAP 라이브러리(libldap)은 2.4 버전입니다. 리눅스 배포판에 충분히 최신(CentOS7, 데비안 7, 우분투 12.04 이상)이라면, 시스템의 libldap을 대신 사용해도 됩니다.

우분투 14.04와 데비안 7/8 에서는, 번들 LDAP 관련 라이브러리를 라이브러리 경로 밖에 옮겨두어 TLS 연결이 동작하도록 하십시오.

```
cd ${SEAFILE_INSTALLATION_DIR}/seafile-server-latest/seafile/lib
mkdir disabled_libs_use_local_ones_instead
mv liblber-2.4.so.2 libldap-2.4.so.2 libsasl2.so.2 libldap_r-2.4.so.2 disabled_libs_use_local_ones_instead/
```

CentOS 6에서 libnssutil 라이브러리를 옮겨야합니다:

```
cd ${SEAFILE_INSTALLATION_DIR}/seafile-server-latest/seafile/lib
mkdir disabled_libs_use_local_ones_instead
mv libnssutil3.so disabled_libs_use_local_ones_instead/
```

이 명령으로 라이브러리 검색 경로의 번들 라이브러리를 제거합니다. 
서버를 시작할 때, 대신 시스템 라이브러리를(설치했다면) 찾고 활용합니다. 
This change has to be repeated after each update of the Seafile installation.

