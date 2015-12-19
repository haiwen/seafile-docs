# Configure Seafile to use LDAP
The current code of seahub assumes that user name to be email address, so it's not possible to log in with UNIX user names or Windows Domain user names now. The support may be added later.

Seafile will find a user both from database and LDAP. LDAP will be tried first. Note that the Seafile admin  accounts are always stored in sqlite/mysql database.

## LDAP User Management

Before 4.2 version, there are some limitation on admin operations to LDAP users. The system admin cannot deactivate a LDAP user, and cannot set a LDAP user as system admin.
After 4.2 version, we introduce a more flexible design for LDAP user management. In this design,

* When a LDAP user logs in, it will be automatically imported from LDAP server into the database (table `LDAPUser` in the ccnet database).
* Now the admin can change various properties about this user in the database, such as deactivating, setting as system admin.
* The admin can manage imported LDAP users in the sysmtem admin page.
* For Pro Edition, system user count only includes imported LDAP users. So customers can buy less licenses than all the users they have in LDAP server.

In 4.2 Pro Edition, we introduced LDAP user sync feature, which brings even more management capabilities on LDAP users:

* Periodically sync users from LDAP server to the database. Additional user properties can be synced too, such as full name, department.
* Automatically detect changes to users in the LDAP server. These includes user password change, user deletion. Corresponding actions will be taken when user changes are detected, such as logging out the user or deactivating the user.

For more information about LDAP user sync, please refer to [this documentation](ldap_user_sync.md).

## Connect to LDAP/AD from Linux

To use LDAP to authenticate user, please add the following lines to ccnet.conf. Note that the values in the following config are just examples. You need to change the values for your own use.

    [LDAP]
    HOST = ldap://ldap.example.com
    BASE = base DN for searching users
    USER_DN = admin user DN for accessing other user information
    PASSWORD = secret
    LOGIN_ATTR = mail

Meaning of each config options:

* HOST: LDAP URL for the host. ldap://, ldaps:// and ldapi:// are supported. You can also include port number in the URL, like ldap://ldap.example.com:389. To use TLS, you should configure the LDAP server to listen on LDAPS port and specify ldaps:// here. More details about TLS will be covered below.
* BASE: The root distinguished name (DN) to use when running queries against the directory server.
* USER_DN: The distinguished name of the user that Seafile will use when connecting to the directory server. This user should have sufficient privilege to access all the nodes under BASE. It's recommended to use a user in the administrator group.
* PASSWORD: Password of the above user.
* LOGIN_ATTR: The attribute to be used as user login id. By default it's the 'mail' attribute.

Tips for connecting to Active Directory:

* To determine the BASE, you first have to navigate your organization hierachy on the domain controller GUI.
    * If you want to allow all users to use Seafile, you can use 'cn=users,dc=yourdomain,dc=com' as BASE (with proper adjustment for your own needs).
    * If you want to limit users to a certain OU (Organization Unit), you run `dsquery` command on the domain controller to find out the DN for this OU. For example, if the OU is 'staffs', you can run 'dsquery ou -name staff'. More information can be found [here](https://technet.microsoft.com/en-us/library/cc770509.aspx).
* AD supports 'user@domain.name' format for the USER_DN option. For example you can use administrator@example.com for USER_DN. Sometime the domain controller doesn't recognize this format. You can still use `dsquery` command to find out user's DN. For example, if the user name is 'seafileuser', run `dsquery user -name seafileuser`. More information [here](https://technet.microsoft.com/en-us/library/cc725702.aspx).

Example config for Active Directory:

    [LDAP]
    HOST = ldap://192.168.1.123/
    BASE = cn=users,dc=example,dc=com
    USER_DN = administrator@example.local
    PASSWORD = secret
    LOGIN_ATTR = mail

Example config for OpenLDAP or other LDAP servers:

    [LDAP]
    HOST = ldap://192.168.1.123/
    BASE = ou=users,dc=example,dc=com
    USER_DN = cn=admin,dc=example,dc=com
    PASSWORD = secret
    LOGIN_ATTR = mail

If you're using Active Directory but don't have email address for the users, you can use the following config:

    [LDAP]
    HOST = ldap://192.168.1.123/
    BASE = cn=users,dc=example,dc=com
    USER_DN = administrator@example.local
    PASSWORD = secret
    LOGIN_ATTR = userPrincipalName

The `userPrincipalName` is an user attribute provided by AD. It's usually of the form `username@domain-name`, where `username` is Windows user login name. The the user can log in to seahub with `username@domain-name`, such as `poweruser@example.com`. Note that such login name is not actually an email address. So sending emails from seahub won't work with this setting.

## Connect to LDAP/AD from Windows server

The config syntax on Windows is slightly different from Linux. 

To use LDAP to authenticate user, please add the following lines to ccnet.conf

    [LDAP]
    HOST = ldap.example.com[:port]
    # Default 'false'. Set to true if you want Seafile to communicate with the LDAP server via TLS connection.
    USE_SSL = true | false
    BASE = base DN for searching users
    USER_DN = admin user DN for accessing other user information
    PASSWORD = secret
    LOGIN_ATTR = mail

Meaning of each config options:

* HOST: LDAP server address and port. **You should not add ldap:// prefix to the HOST field.**.
* USE_SSL: To use TLS, set this option to true. More details about TLS will be covered below.
* BASE: The root distinguished name (DN) to use when running queries against the directory server.
* USER_DN: The distinguished name of the user that Seafile will use when connecting to the directory server. This user should have sufficient privilege to access all the nodes under BASE. It's recommended to use a user in the administrator group.
* PASSWORD: Password of the above user.
* LOGIN_ATTR: The attribute to be used as user login id. By default it's the 'mail' attribute.

Tips for connecting to Active Directory:

* To determine the BASE, you first have to navigate your organization hierachy on the domain controller GUI.
    * If you want to allow all users to use Seafile, you can use 'cn=users,dc=yourdomain,dc=com' as BASE (with proper adjustment for your own needs).
    * If you want to limit users to a certain OU (Organization Unit), you run `dsquery` command on the domain controller to find out the DN for this OU. For example, if the OU is 'staffs', you can run 'dsquery ou -name staff'. More information can be found [here](https://technet.microsoft.com/en-us/library/cc770509.aspx).
* AD supports 'user@domain.name' format for the USER_DN option. For example you can use administrator@example.com for USER_DN. Sometime the domain controller doesn't recognize this format. You can still use `dsquery` command to find out user's DN. For example, if the user name is 'seafileuser', run `dsquery user -name seafileuser`. More information [here](https://technet.microsoft.com/en-us/library/cc725702.aspx).

Example config for Active Directory:

    [LDAP]
    HOST = 192.168.1.123
    BASE = cn=users,dc=example,dc=com
    USER_DN = administrator@example.local
    PASSWORD = secret
    LOGIN_ATTR = mail

Example config for OpenLDAP or other LDAP servers:

    [LDAP]
    HOST = 192.168.1.123
    BASE = ou=users,dc=example,dc=com
    USER_DN = cn=admin,dc=example,dc=com
    PASSWORD = secret
    LOGIN_ATTR = mail

If you're using Active Directory but don't have email address for the users, you can use the following config:

    [LDAP]
    HOST = 192.168.1.123
    BASE = cn=users,dc=example,dc=com
    USER_DN = administrator@example.local
    PASSWORD = secret
    LOGIN_ATTR = userPrincipalName

The `userPrincipalName` is an user attribute provided by AD. It's usually of the form `username@domain-name`, where `username` is Windows user login name. The the user can log in to seahub with `username@domain-name`, such as `poweruser@example.com`. Note that such login name is not actually an email address. So sending emails notifications from Seahub won't work with this setting.

## Testing Your LDAP Configuration

Since 5.0.0 Pro Edition, we provide a command line tool for checking your LDAP configuration.

To use this tool, make sure you are using the Pro Edition and have `python-ldap` package installed on your system.

```
sudo apt-get install python-ldap
```

Then you can run the test:

```
cd seafile-server-latest
./pro/pro.py ldapsync --test
```

The test script will test your LDAP settings under the `[LDAP]` section of ccnet.conf. If everything works, it'll print the first ten users in the search results. Otherwise, it'll print out possible errors in your config.

Note that currently the script doesn't test advanced LDAP syncing options in the `[LDAP_SYNC]` section of ccnet.conf.

## Multiple base DN/Additional search filter

Multiple base DN is useful when your company has more than one OUs to use Seafile. You can specify a list of base DN in the "BASE" config. The DNs are separated by ";", e.g. `cn=developers,dc=example,dc=com;cn=marketing,dc=example,dc=com`

Search filter is very useful when you have a large organization but only a portion of people want to use Seafile. The filter can be given by setting "FILTER" config. The value of this option follows standard LDAP search filter syntax (https://msdn.microsoft.com/en-us/library/aa746475(v=vs.85).aspx).

The final filter used for searching for users is `(&($LOGIN_ATTR=*)($FILTER))`. `$LOGIN_ATTR` and `$FILTER` will be replaced by your option values.

For example, add the following line to LDAP config:

```
FILTER = memberOf=CN=group,CN=developers,DC=example,DC=com
```

The final search filter would be `(&(mail=*)(memberOf=CN=group,CN=developers,DC=example,DC=com))`

Note that the cases in the above example is significant. The `memberOf` attribute is only available in Active Directory.

## Limiting Seafile Users to a Group in Active Directory

You can use the FILTER option to limit user scope to a certian AD group.

1. First, you should find out the DN for the group. Again, we'll use `dsquery` command on the domain controller. For example, if group name is 'seafilegroup', run `dsquery group -name seafilegroup`.
2. Add following line to LDAP config:

```
FILTER = memberOf={output of dsquery command}
```

## Using TLS connection to LDAP/AD server

To use TLS connection to the directory server, you should install a valid SSL certificate on the directory server.

The current version of Seafile Linux server package is compiled on CentOS. We include the ldap client library in the package to maintain compatibility with older Linux distributions. But since different Linux distributions have different path or configuration for OpenSSL library, sometimes Seafile is unable to connect to the directory server with TLS.

The ldap library (libldap) bundled in the Seafile package is of version 2.4. If your Linux distribution is new enough (like CentOS 6, Debian 7 or Ubuntu 12.04 or above), you can use system's libldap instead.

To do this, just run the following command

```
cd ${SEAFILE_INSTALLATION_DIR}/seafile-server-latest/seafile/lib
mv liblber-2.4.so.2 libldap-2.4.so.2 libsasl2.so.2 libldap_r-2.4.so.2 ..
```

This effectively remove the bundled ldap library from the library path. When the server runs, it'll look for ldap library from the system paths. Remember to repeat the command after each update of your seafile installation.

## Password reset page redirection

"forgot password" link on login page redirect to a form that don't allow to reset password of LDAP user. (They are notified to contact their LDAP administrator). If you have a web service that allows your users reset their password, it is possible to setup a redirect in the apache configuration.
Add this line just after "RewriteEngine On" :

```
RewriteRule ^/accounts/password/reset/$ https://selfservice.mycompany.com/password_reset [R,L]
```

## Advanced LDAP options for Professional Edition

### Use paged results extension

LDAP protocol version 3 supports "paged results" (PR) extension. When you have large number of users, this option can greatly improve the performance of listing users. Most directory server nowadays support this extension.

In Seafile Pro Edition, add this option to LDAP section of ccnet.conf to enable PR:

```
USE_PAGED_RESULT = true
```

### Follow referrals

Starting from Pro Edition 4.0.4, Seafile supports auto following referrals in LDAP search. This is useful for partitioned LDAP or AD servers, where users may be spreaded on multiple directory servers. For more information about referrals, you can refer to [this article](https://technet.microsoft.com/en-us/library/cc978014.aspx).

To configure, add following option to ccnet.conf in the [LDAP] section:

```
FOLLOW_REFERRALS = true
```

### Importing Groups from LDAP

Since 4.1.0 of Pro Edition, Seafile supports importing groups from LDAP. Please see [importing groups from LDAP](ldap_group_sync.md).
