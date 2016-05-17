# Configure Seafile to use LDAP

注意：这个文档是社区版的 LDAP 配置文档。企业版中包含了 LDAP 用户/群组同步等高级功能，企业版用户请参考[企业版文档](../deploy_pro/using_ldap_pro.md).

## Seafile 是如何管理 LDAP 用户的

Seafile 中的用户分为两类：

- 保存在 Seafile 内部数据库中的用户。这些用户关联了一些属性，比如是否管理员，是否已激活等。这类用户又分为两个子类别：
    * 系统管理员直接创建的用户。这些用户保存在 `ccnet` 数据库里面的 `EmailUser` 表中。
    * Users imported from LDAP/AD server: When a user in LDAP/AD logs into Seafile, its information will be imported from LDAP/AD server into Seafile's database. These users are stored in the `LDAPUsers` table of the `ccnet` database.
- Users in LDAP/AD server. These are all the intended users of Seafile inside the LDAP server. Seafile doesn't manipulate these users directly. It has to import them into its internal database before setting attributes on them.

When Seafile counts the number of users in the system, it only counts the **activated** users in its internal database.

When Seafile is integrated with LDAP/AD, it'll look up users from both the internal database and LDAP server. As long as the user exists in one of these two sources, they can log into the system.

## 基本的 LDAP/AD 集成配置

Seafile 要求 LDAP/AD 服务器中每个用户都有一个唯一的 ID。这个 ID 只能使用邮箱地址格式。一般来说，AD 有两个用户属性可以用作 Seafile 用户的 ID：

- email 地址：一般的机构都会给每个成员分配唯一的 email 地址，所以这是最常见配置。
- UserPrincipalName (UPN)：这个 AD 赋予给每个用户的一个唯一 ID。它的格式为 用户登录名@域名。尽管这个不是真实的 email 地址，但是它也能作为 Seafile 的用户 ID。如果机构的用户没有 email 地址，可以使用这个属性。

### Connecting to Active Directory

To use AD to authenticate user, please add the following lines to ccnet.conf.

If you choose email address as unique identifier:

    [LDAP]
    HOST = ldap://192.168.1.123/
    BASE = cn=users,dc=example,dc=com
    USER_DN = administrator@example.local
    PASSWORD = secret
    LOGIN_ATTR = mail

If you choose UserPrincipalName as unique identifier:

    [LDAP]
    HOST = ldap://192.168.1.123/
    BASE = cn=users,dc=example,dc=com
    USER_DN = administrator@example.local
    PASSWORD = secret
    LOGIN_ATTR = userPrincipalName

Meaning of each config options:

* HOST: LDAP URL for the host. ldap://, ldaps:// and ldapi:// are supported. You can also include a port number in the URL, like ldap://ldap.example.com:389. To use TLS, you should configure the LDAP server to listen on LDAPS port and specify ldaps:// here. More details about TLS will be covered below.
* BASE: The root distinguished name (DN) to use when running queries against the directory server. **You cannot use the root DN (e.g. dc=example,dc=com) as BASE**.
* USER_DN: The distinguished name of the user that Seafile will use when connecting to the directory server. This user should have sufficient privilege to access all the nodes under BASE. It's recommended to use a user in the administrator group.
* PASSWORD: USER_DN 对应的用户的密码。
* LOGIN_ATTR: 用作 Seafile 中用户登录 ID 的 LDAP 属性，可以使用 `mail` 或者 `userPrincipalName`。

关于如何选定 BASE 和 USER_DN 的一些技巧：

* 要确定您的 BASE 属性，您首先需要打开域管理器的图形界面，并浏览您的组织架构。
    * 如果您想要让系统中所有用户都能够访问 Seafile，您可以用 'cn=users,dc=yourdomain,dc=com' 作为 BASE 选项（需要替换成你们的域名）。
    * 如果您只想要某个部门的人能访问，您可以把范围限定在某个 OU （Organization Unit）中。您可以使用 `dsquery` 命令行工具来查找相应 OU 的 DN。比如，如果 OU 的名字是 'staffs'，您可以运行 'dsquery ou -name staff'。更多的信息可以参考[这里](https://technet.microsoft.com/en-us/library/cc770509.aspx)。
* AD supports 'user@domain.name' format for the USER_DN option. For example you can use administrator@example.com for USER_DN. Sometime the domain controller doesn't recognize this format. You can still use `dsquery` command to find out user's DN. For example, if the user name is 'seafileuser', run `dsquery user -name seafileuser`. More information [here](https://technet.microsoft.com/en-us/library/cc725702.aspx).

### 与其他 LDAP 服务器集成

把以下配置添加到 ccnet.conf 中：

    [LDAP]
    HOST = ldap://192.168.1.123/
    BASE = ou=users,dc=example,dc=com
    USER_DN = cn=admin,dc=example,dc=com
    PASSWORD = secret
    LOGIN_ATTR = mail

The meaning of the options are the same as described in the previous section. With other LDAP servers, you can only use `mail` attribute as user's unique identifier.

## LDAP 高级配置选项

### 使用多个 BASE DN

使用多个 BASE DN当您想把公司中多个 OU 加入 Seafile 中时，您可以使用在配置中指定多个 BASE DN。您可以在"BASE"配置中指定一个 DN 的列表，标识名由";"分开, 比如： `ou=developers,dc=example,dc=com;ou=marketing,dc=example,dc=com`

### 用户过滤选项

Search filter is very useful when you have a large organization but only a portion of people want to use Seafile. The filter can be given by setting "FILTER" config. The value of this option follows standard LDAP search filter syntax (https://msdn.microsoft.com/en-us/library/aa746475(v=vs.85).aspx).

The final filter used for searching for users is `(&($LOGIN_ATTR=*)($FILTER))`. `$LOGIN_ATTR` and `$FILTER` will be replaced by your option values.

For example, add the following line to LDAP config:

```
FILTER = memberOf=CN=group,CN=developers,DC=example,DC=com
```

The final search filter would be `(&(mail=*)(memberOf=CN=group,CN=developers,DC=example,DC=com))`

请注意上面的示例只是象征性的简介. memberOf只有在活动目录(Active Directory)中才适用.

### 把 Seafile 用户限定在 AD 的一个组中

You can use the FILTER option to limit user scope to a certain AD group.

1. 首先，您需要找到这个组的 DN。我们再次使用 dsquery 命令。比如，如果组的名字是 'seafilegroup'，那么您可以运行 `dsquery group -name seafilegroup`。
2. Add the following line to LDAP config:

```
FILTER = memberOf={命令的输出}
```

### Using TLS connection to LDAP/AD server

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

