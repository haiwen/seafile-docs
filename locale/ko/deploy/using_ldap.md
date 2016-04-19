# Seafile LDAP 사용 설정

Note: This documentation is for the Community Edition. If you're using Pro Edition, please refer to [the Seafile Pro documentation](../deploy_pro/using_ldap_pro.md).

## Seafile의 LDAP 사용자 관리 동작 방식

When Seafile is integrated with LDAP/AD, users in the system can be divided into two tiers:

- Users within Seafile's internal user database. Some attributes are attached to these users, such as whether it's a system admin user, whether it's activated. This tier includes two types of users:
    * Native users: these users are created by the admin on Seafile's system admin interface. These users are stored in the `EmailUser` table of the `ccnet` database.
    * Users imported from LDAP/AD server: When a user in LDAP/AD logs into Seafile, its information will be imported from LDAP/AD server into Seafile's database. These users are stored in the `LDAPUsers` table of the `ccnet` database.
- Users in LDAP/AD server. These are all the intended users of Seafile inside the LDAP server. Seafile doesn't manipulate these users directly. It has to import them into its internal database before setting attributes on them.

When Seafile counts the number of users in the system, it only counts the **activated** users in its internal database.

When Seafile is integrated with LDAP/AD, it'll look up users from both the internal database and LDAP server. As long as the user exists in one of these two sources, they can log into the system.

## Basic LDAP/AD Integration

The only requirement for Seafile to use LDAP/AD for authentication is that there must be a unique identifier for each user in the LDAP/AD server. Seafile can only use email-address-format user identifiers. So there are usually only two options for this unique identifier:

- Email address: this is the most common choice. Most organizations assign unique email address for each member.
- UserPrincipalName: this is a user attribute only available in Active Directory. It's format is `user-login-name@domain-name`, e.g. `john@example.com`. It's not a real email address, but it works fine as the unique identifier.

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

* HOST: LDAP URL for the host. ldap://, ldaps:// and ldapi:// are supported. You can also include a port number in the URL, like ldap://ldap.example.com:389. To use TLS, you should configure the LDAP server to listen on LDAPS port and specify ldaps:// here. More details about TLS will be covered below.
* BASE: The root distinguished name (DN) to use when running queries against the directory server. **You cannot use the root DN (e.g. dc=example,dc=com) as BASE**.
* USER_DN: The distinguished name of the user that Seafile will use when connecting to the directory server. This user should have sufficient privilege to access all the nodes under BASE. It's recommended to use a user in the administrator group.
* PASSWORD: Password of the above user.
* LOGIN_ATTR: The attribute used for user's unique identifier. Use `mail` or `userPrincipalName`.

Tips for choosing BASE and USER_DN:

* To determine the BASE, you first have to navigate your organization hierachy on the domain controller GUI.
    * If you want to allow all users to use Seafile, you can use 'cn=users,dc=yourdomain,dc=com' as BASE (with proper adjustment for your own needs).
    * If you want to limit users to a certain OU (Organization Unit), you run `dsquery` command on the domain controller to find out the DN for this OU. For example, if the OU is 'staffs', you can run 'dsquery ou -name staff'. More information can be found [here](https://technet.microsoft.com/en-us/library/cc770509.aspx).
* AD supports 'user@domain.name' format for the USER_DN option. For example you can use administrator@example.com for USER_DN. Sometime the domain controller doesn't recognize this format. You can still use `dsquery` command to find out user's DN. For example, if the user name is 'seafileuser', run `dsquery user -name seafileuser`. More information [here](https://technet.microsoft.com/en-us/library/cc725702.aspx).

### 기타 LDAP 서버에 연결

Please add the following options to ccnet.conf:

    [LDAP]
    HOST = ldap://192.168.1.123/
    BASE = ou=users,dc=example,dc=com
    USER_DN = cn=admin,dc=example,dc=com
    PASSWORD = secret
    LOGIN_ATTR = mail

The meaning of the options are the same as described in the previous section. With other LDAP servers, you can only use `mail` attribute as user's unique identifier.

## 고급 LDAP/AD 통합 옵션

### 다중 BASE

Multiple base DN is useful when your company has more than one OUs to use Seafile. You can specify a list of base DN in the "BASE" config. The DNs are separated by ";", e.g. `ou=developers,dc=example,dc=com;ou=marketing,dc=example,dc=com`

### 추가 검색 필터

Search filter is very useful when you have a large organization but only a portion of people want to use Seafile. The filter can be given by setting "FILTER" config. The value of this option follows standard LDAP search filter syntax (https://msdn.microsoft.com/en-us/library/aa746475(v=vs.85).aspx).

The final filter used for searching for users is `(&($LOGIN_ATTR=*)($FILTER))`. `$LOGIN_ATTR` and `$FILTER` will be replaced by your option values.

For example, add the following line to LDAP config:

```
FILTER = memberOf=CN=group,CN=developers,DC=example,DC=com
```

The final search filter would be `(&(mail=*)(memberOf=CN=group,CN=developers,DC=example,DC=com))`

Note that the case of attribute names in the above example is significant. The `memberOf` attribute is only available in Active Directory.

### Limiting Seafile Users to a Group in Active Directory

You can use the FILTER option to limit user scope to a certain AD group.

1. 우선, 그룹 DN을 찾으십시오. 다시 말해, 도메인 컨트롤러의 `dsquery` 명령을 사용합니다. 예를 들어, 그룹 이름이 `seafilegroup`이면,  `dsquery group -name seafilegroup`을 실행합니다.
2. 다음 줄을 LDAP 설정에 추가하십시오:

```
FILTER = memberOf={output of dsquery command}
```

### LDAP/AD 서버 연결에 TLS 사용

To use a TLS connection to the directory server, you should install a valid SSL certificate on the directory server.

The current version of Seafile Linux server package is compiled on CentOS. We include the ldap client library in the package to maintain compatibility with older Linux distributions. But since different Linux distributions have different path or configuration for OpenSSL library, sometimes Seafile is unable to connect to the directory server with TLS.

The ldap library (libldap) bundled in the Seafile package is of version 2.4. If your Linux distribution is new enough (like CentOS 6, Debian 7 or Ubuntu 12.04 or above), you can use system's libldap instead.

On Ubuntu 14.04 and Debian 7/8, moving the bundled ldap related libraries out of the library path should make TLS connection work.

```
cd ${SEAFILE_INSTALLATION_DIR}/seafile-server-latest/seafile/lib
mkdir disabled_libs_use_local_ones_instead
mv liblber-2.4.so.2 libldap-2.4.so.2 libsasl2.so.2 libldap_r-2.4.so.2 disabled_libs_use_local_ones_instead/
```

On CentOS 6, you have to move the libnssutil library:

```
cd ${SEAFILE_INSTALLATION_DIR}/seafile-server-latest/seafile/lib
mkdir disabled_libs_use_local_ones_instead
mv libnssutil3.so disabled_libs_use_local_ones_instead/
```

This effectively removes the bundled libraries from the library search path. 
When the server starts, it'll instead find and use the system libraries (if they are installed). 
This change has to be repeated after each update of the Seafile installation.

