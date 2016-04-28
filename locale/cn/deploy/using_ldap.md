# Seafile LDAP 和 Active Directory 配置

注意：这个文档是社区版的 LDAP 配置文档。企业版中包含了 LDAP 用户/群组同步等高级功能，企业版用户请参考[企业版文档](../deploy_pro/using_ldap_pro.md)

LDAP (Light-weight Directory Access Protocol) 是企业广泛部署的用户信息管理服务器，微软的活动目录服务器（Active Directory）完全兼容 LDAP。这个文档假定您已经了解了 LDAP 相关的知识和术语。

社区版只支持用 Email 登录。 从 5.0 开始 Seafile 企业版支持用用户名登录，不过需要配置和开启 AD/LDAP 同步功能。

## Seafile 是如何管理 LDAP 用户的

Seafile 中的用户分为两类：

* 保存在 Seafile 内部数据库中的用户。这些用户关联了一些属性，比如是否管理员，是否已激活等。这类用户又分为两个子类别：
    - 系统管理员直接创建的用户。这些用户保存在 ccnet 数据库里面的 EmailUser 表中。
    - 由 LDAP 导入的用户。当 LDAP 里的用户第一次登录 Seafile 时，Seafile 会把该用户的信息导入到内部数据库。
* 在 LDAP 中存在的用户。管理员可以通过配置文件指定 LDAP 中可以使用 Seafile 服务的用户范围。这些用户在第一次登录时被导入到 Seafile 数据库中。Seafile 只会直接操作存在数据库中的用户。

Seafile 会自动从内部数据库和 LDAP 中查找用户，只要用户存在于任何一个来源，他们都能登录。

## 基本的 LDAP/AD 集成配置

Seafile 要求 LDAP/AD 服务器中每个用户都有一个唯一的 ID。这个 ID 只能使用邮箱地址格式。一般来说，AD 有两个用户属性可以用作 Seafile 用户的 ID：

- email 地址：一般的机构都会给每个成员分配唯一的 email 地址，所以这是最常见配置。
- UserPrincipalName (UPN)：这个 AD 赋予给每个用户的一个唯一 ID。它的格式为 `用户登录名@域名`。尽管这个不是真实的 email 地址，但是它也能作为 Seafile 的用户 ID。如果机构的用户没有 email 地址，可以使用这个属性。

### 与 AD 集成

把下面的配置添加到 ccnet.conf 中。

如果你使用 email 地址作为用户唯一 ID：

```
[LDAP]
HOST = ldap://192.168.1.123/
BASE = cn=users,dc=example,dc=com
USER_DN = administrator@example.local
PASSWORD = secret
LOGIN_ATTR = mail
```

如果你使用 UserPrincipalName 作为用户 ID：

```
[LDAP]
HOST = ldap://192.168.1.123/
BASE = cn=users,dc=example,dc=com
USER_DN = administrator@example.local
PASSWORD = secret
LOGIN_ATTR = userPrincipalName
```

各个配置选项的含义如下：

* HOST: LDAP 服务器的地址 URL。如果您的 LDAP 服务器监听在非标准端口上，您也可以在 URL 里面包含端口号，如 ldap://ldap.example.com:389。
* BASE: 在 LDAP 服务器的组织架构中，用于查询用户的根节点的唯一名称（Distingushed Name，简称 DN）。这个节点下面的所有用户都可以访问 Seafile。注意这里必须使用 *OU* 或 *CN*，即 `BASE = cn=users,dc=example,dc=com` 或者 `BASE = ou=users,dc=example,dc=com` 可以工作。但是 `BASE = dc=example,dc=com` 不能工作。`BASE` 中可以填多个 OU, 用 `;` 分隔。
* USER_DN: 用于查询 LDAP 服务器中信息的用户的 DN。这个用户应该有足够的权限访问 BASE 以下的所有信息。通常建议使用 LDAP/AD 的管理员用户。
* PASSWORD: USER_DN 对应的用户的密码。
* LOGIN_ATTR: 用作 Seafile 中用户登录 ID 的 LDAP 属性，可以使用 `mail` 或者 `userPrincipalName`。

**注意：如果配置项包含中文，需要确保配置文件使用 UTF8 编码保存。**

关于如何选定 BASE 和 USER_DN 的一些技巧：

* 要确定您的 BASE 属性，您首先需要打开域管理器的图形界面，并浏览您的组织架构。
    * 如果您想要让系统中所有用户都能够访问 Seafile，您可以用 'cn=users,dc=yourdomain,dc=com' 作为 BASE 选项（需要替换成你们的域名）。
    * 如果您只想要某个部门的人能访问，您可以把范围限定在某个 OU （Organization Unit）中。您可以使用 `dsquery` 命令行工具来查找相应 OU 的 DN。比如，如果 OU 的名字是 'staffs'，您可以运行 `dsquery ou -name staff`。更多的信息可以参考[这里](https://technet.microsoft.com/en-us/library/cc770509.aspx)。
* AD 支持使用 'user@domain.com' 格式的用户名作为 `USER_DN`。比如您可以使用 administrator@example.com 作为 `USER_DN`。有些时候 AD 不能正确识别这种格式。此时您可以使用 `dsquery` 来查找用户的 DN。比如，假设用户名是 'seafileuser'，运行 `dsquery user -name seafileuser` 来找到该用户的 DN。更多的信息可以参考[这里](https://technet.microsoft.com/en-us/library/cc725702.aspx)。

### 与其他 LDAP 服务器集成

把以下配置添加到 ccnet.conf 中：

```
[LDAP]
HOST = ldap://192.168.1.123/
BASE = ou=users,dc=example,dc=com
USER_DN = cn=admin,dc=example,dc=com
PASSWORD = secret
LOGIN_ATTR = mail
```

配置选项的含义与 AD 配置相同。不过，你只能使用 mail 作为用户的 ID，因为其他 LDAP 服务器不支持 UserPrincipalName。

## LDAP 高级配置选项

### 使用多个 BASE DN

当您想把公司中多个 OU 加入 Seafile 中时，您可以使用在配置中指定多个 BASE DN。您可以在"BASE"配置中指定一个 DN 的列表，标识名由";"分开, 比如： `cn=developers,dc=example,dc=com;cn=marketing,dc=example,dc=com`

### 用户过滤选项

当你的公司组织庞大，但是只有一小部分人使用 Seafile 的时候，搜索过滤器（Search filter）会很有用处. 过滤器可以通过修改"FILTER"配置来实现，例如，在 LDAP 配置中增加以下语句:

```
FILTER = memberOf=CN=group,CN=developers,DC=example,DC=com
```

请注意上面的示例只是象征性的简介. `memberOf`只有在活动目录(Active Directory)中才适用.

### 把 Seafile 用户限定在 AD 的一个组中

您可以利用用户过滤器选项来只允许 AD 某个组中的用户使用 Seafile。

1. 首先，您需要找到这个组的 DN。我们再次使用 `dsquery` 命令。比如，如果组的名字是 'seafilegroup'，那么您可以运行 `dsquery group -name seafilegroup`。
2. 然后您可以把一下配置加入 ccnet.conf 的 LDAP 配置中：

```
FILTER = memberOf={dsquery 命令的输出}
```

