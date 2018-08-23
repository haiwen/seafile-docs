# Configure Seafile to use LDAP

## How does LDAP User Management Works in Seafile

When Seafile is integrated with LDAP/AD, users in the system can be divided into two tiers:

* Users within Seafile's internal user database. Some attributes are attached to these users, such as whether it's a system admin user, whether it's activated. This tier includes two types of users:
  * Native users: these users are created by the admin on Seafile's system admin interface. These users are stored in the `EmailUser` table of the `ccnet` database.
  * Users imported from LDAP/AD server: When a user in LDAP/AD logs into Seafile, its information will be imported from LDAP/AD server into Seafile's database. These users are stored in the `LDAPUsers` table of the `ccnet` database.
* Users in LDAP/AD server. These are all the intended users of Seafile inside the LDAP server. Seafile doesn't manipulate these users directly. It has to import them into its internal database before setting attributes on them.

When Seafile counts the user number in the system, it only counts the **activated** users in its internal database.

When Seafile is integrated with LDAP/AD, it'll look up users from both the internal database and LDAP server. As long as the user exists in one of these two sources, it can log into the system.

## Basic LDAP/AD Integration

The only requirement for Seafile to use LDAP/AD for authentication is that, there must be a unique identifier for each user in the LDAP/AD server. Seafile can only use email-address-format user identifiers. So there are usually only two options for this unique identifier:

* Email address: this is the most common choice. Most organizations assign unique email address for each member.
* UserPrincipalName: this is a user attribute only available in Active Directory. It's format is `user-login-name@domain-name`, e.g. `john@example.com`. It's not a real email address, but it works fine as the unique identifier.

### Connecting to Active Directory

To use AD to authenticate user, please add the following lines to ccnet.conf.

If you choose email address as unique identifier:

```
[LDAP]
HOST = 192.168.1.123
USE_SSL = false
BASE = cn=users,dc=example,dc=com
USER_DN = administrator@example.local
PASSWORD = secret
LOGIN_ATTR = mail
```

If you choose UserPrincipalName as unique identifier:

```
[LDAP]
HOST = 192.168.1.123
USE_SSL = false
BASE = cn=users,dc=example,dc=com
USER_DN = administrator@example.local
PASSWORD = secret
LOGIN_ATTR = userPrincipalName
```

Meaning of each config options:

* HOST: LDAP URL for the host. ldap://, ldaps:// and ldapi:// are supported. You can also include port number in the URL, like ldap://ldap.example.com:389. To use TLS, you should configure the LDAP server to listen on LDAPS port and specify ldaps:// here. More details about TLS will be covered below.
* BASE: The root distinguished name \(DN\) to use when running queries against the directory server. **You cannot use the root DN \(e.g. dc=example,dc=com\) as BASE**.
* USER\_DN: The distinguished name of the user that Seafile will use when connecting to the directory server. This user should have sufficient privilege to access all the nodes under BASE. It's recommended to use a user in the administrator group.
* PASSWORD: Password of the above user.
* LOGIN\_ATTR: The attribute used for user's unique identifier. Use `mail` or `userPrincipalName`.

Tips for choosing BASE and USER\_DN:

* To determine the BASE, you first have to navigate your organization hierachy on the domain controller GUI.
  * If you want to allow all users to use Seafile, you can use 'cn=users,dc=yourdomain,dc=com' as BASE \(with proper adjustment for your own needs\).
  * If you want to limit users to a certain OU \(Organization Unit\), you run `dsquery` command on the domain controller to find out the DN for this OU. For example, if the OU is 'staffs', you can run 'dsquery ou -name staff'. More information can be found [here](https://technet.microsoft.com/en-us/library/cc770509.aspx).
* AD supports 'user@domain.name' format for the USER\_DN option. For example you can use administrator@example.com for USER\_DN. Sometime the domain controller doesn't recognize this format. You can still use `dsquery` command to find out user's DN. For example, if the user name is 'seafileuser', run `dsquery user -name seafileuser`. More information [here](https://technet.microsoft.com/en-us/library/cc725702.aspx).

### Connecting to other LDAP servers

Please add the following options to ccnet.conf:

```
[LDAP]
HOST = 192.168.1.123
USE_SSL = false
BASE = ou=users,dc=example,dc=com
USER_DN = cn=admin,dc=example,dc=com
PASSWORD = secret
LOGIN_ATTR = mail
```

The meaning of the options are the same as described in the previous section. With other LDAP servers, you can only use `mail` attribute as user's unique identifier.

## Advanced LDAP/AD Integration Options

### Multiple BASE

Multiple base DN is useful when your company has more than one OUs to use Seafile. You can specify a list of base DN in the "BASE" config. The DNs are separated by ";", e.g. `ou=developers,dc=example,dc=com;ou=marketing,dc=example,dc=com`

### Additional Search Filter

Search filter is very useful when you have a large organization but only a portion of people want to use Seafile. The filter can be given by setting "FILTER" config. The value of this option follows standard LDAP search filter syntax \([https://msdn.microsoft.com/en-us/library/aa746475\(v=vs.85\).aspx](https://msdn.microsoft.com/en-us/library/aa746475%28v=vs.85%29.aspx)\).

The final filter used for searching for users is `(&($LOGIN_ATTR=*)($FILTER))`. `$LOGIN_ATTR` and `$FILTER` will be replaced by your option values.

For example, add the following line to LDAP config:

```
FILTER = memberOf=CN=group,CN=developers,DC=example,DC=com
```

The final search filter would be `(&(mail=*)(memberOf=CN=group,CN=developers,DC=example,DC=com))`

Note that the cases in the above example is significant. The `memberOf` attribute is only available in Active Directory.

### Limiting Seafile Users to a Group in Active Directory

You can use the FILTER option to limit user scope to a certain AD group.

1. First, you should find out the DN for the group. Again, we'll use `dsquery` command on the domain controller. For example, if group name is 'seafilegroup', run `dsquery group -name seafilegroup`.
2. Add following line to LDAP config:

```
FILTER = memberOf={output of dsquery command}
```



