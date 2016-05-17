# Seafile LDAP 사용 설정

참고: 이 문서는 커뮤니티판용입니다. 전문가판을 사용중이라면, [Seafile 전문가판 문서|../deploy_pro/using_ldap_pro.md]를 참고하십시오.

## Seafile의 LDAP 사용자 관리 동작 방식

Seafile을 LDAP/AD와 통합하면, 시스템 사용자는 두 티어로 구분합니다:

- Seafile의 자체 사용자 데이터베이스에 있는 사용자. 일부 속성은 이 사용자로 붙는데, 시스템 관리 사용자인지, 활성 상태인지 여부 속성이 여기에 해당합니다. 이 티어에는 두가지 형태의 사용자가 있습니다:
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
    HOST = 192.168.1.123
    USE_SSL = false
    BASE = cn=users,dc=example,dc=com
    USER_DN = administrator@example.local
    PASSWORD = secret
    LOGIN_ATTR = mail

UserPrincipalName을 유일 식별자로 사용한다면:

    [LDAP]
    HOST = 192.168.1.123
    USE_SSL = false
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

ccnet.conf에 다음 설정 항목을 추가하십시오:

    [LDAP]
    HOST = 192.168.1.123
    USE_SSL = false
    BASE = ou=users,dc=example,dc=com
    USER_DN = cn=admin,dc=example,dc=com
    PASSWORD = secret
    LOGIN_ATTR = mail

이 설정 항목은 이전 섹션에 언급한 항목과 의미가 같습니다. 기타 LDAP 서버에서는 사용자 유일 식별자로 `mail` 속성을 사용할 수 있습니다.

## 고급 LDAP/AD 통합 옵션

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

