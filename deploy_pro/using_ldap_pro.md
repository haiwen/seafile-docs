# Configure Seafile Pro Edition to use LDAP

## How does LDAP User Management works with Seafile

When Seafile is integrated with LDAP/AD, users in the system can be divided into two tiers:

- Users within Seafile's internal user database. Some attributes are attached to these users, such as whether it's a system admin user, whether it's activated. This tier includes two types of users:
    * Native users: these users are created by the admin on Seafile's system admin interface and are stored in the `EmailUser` table of the `ccnet` database.
    * Users imported from LDAP/AD server: When a user in LDAP/AD logs into Seafile, its information will be imported from LDAP/AD server into Seafile's database. These users are stored in the `LDAPUsers` table of the `ccnet` database.
- Users in LDAP/AD server. These are all the intended users of Seafile inside the LDAP server. Seafile doesn't manipulate these users directly. It has to import them into its internal database before setting attributes on them.

When Seafile counts the user number in the system, it only counts the **activated** users in its internal database.

When Seafile is integrated with LDAP/AD, it'll look up users from both the internal database and LDAP server. As long as the user exists in one of these two sources, he/she can log into the system.

## Basic LDAP/AD Integration

The only requirement for Seafile to use LDAP/AD for authentication is that there must be a unique identifier for each user in the LDAP/AD server. Seafile can only use email-address-format user identifiers. So there are usually only two options for this unique identifier:

- Email address: this is the most common choice. Most organizations assign a unique email address for each member.
- UserPrincipalName: this is a user attribute only available in Active Directory. It's format is `user-login-name@domain-name`, e.g. `john@example.com`. It's not a real email address, but it works fine as the unique identifier.

### Connecting to Active Directory

To use AD to authenticate a user, please add the following lines to ccnet.conf.

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

* HOST: LDAP URL for the host. ldap://, ldaps:// and ldapi:// are supported. You can also include port number in the URL, like ldap://ldap.example.com:389. To use TLS, you should configure the LDAP server to listen on LDAPS port and specify ldaps:// here. More details about TLS are covered below.
* BASE: The distinguished name (DN) of the search base when running queries against the directory server. If you want to use the root DN as search base (e.g. dc=example,dc=com), you need to add `FOLLOW_REFERRALS = false` to the configuration. The meaning of this option will be explained in following sections.
* USER_DN: The distinguished name of the user that Seafile will use when connecting to the directory server. This user should have sufficient privileges to access all the nodes under BASE. It's recommended to use a user in the administrator group.
* PASSWORD: Password of the above user.
* LOGIN_ATTR: The attribute used for user's unique identifier. Use `mail` or `userPrincipalName`.

Tips for choosing BASE and USER_DN:

* To determine the BASE, you first have to navigate your organization hierachy on the domain controller GUI.
    * If you want to allow all users to use Seafile, you can use 'cn=users,dc=yourdomain,dc=com' as BASE (with proper adjustment for your own needs).
    * If you want to limit users to a certain OU (Organization Unit), you run `dsquery` command on the domain controller to find out the DN for this OU. For example, if the OU is 'staffs', you can run 'dsquery ou -name staff'. More information can be found [here](https://technet.microsoft.com/en-us/library/cc770509.aspx).
* AD supports 'user@domain.name' format for the USER_DN option. For example you can use administrator@example.com for USER_DN. Sometimes the domain controller doesn't recognize this format. You can still use `dsquery` command to find out user's DN. For example, if the user name is 'seafileuser', run `dsquery user -name seafileuser`. More information [here](https://technet.microsoft.com/en-us/library/cc725702.aspx).

### Connecting to other LDAP servers

Please add the following options to ccnet.conf:

    [LDAP]
    HOST = ldap://192.168.1.123/
    BASE = ou=users,dc=example,dc=com
    USER_DN = cn=admin,dc=example,dc=com
    PASSWORD = secret
    LOGIN_ATTR = mail

The meaning of these options is the same as described in the previous section. With other LDAP servers, you can only use `mail` attribute as user's unique identifier.

### Testing your LDAP Configuration

Since 5.0.0 Pro Edition, we provide a command line tool for checking your LDAP configuration.

To use this tool, make sure you have `python-ldap` package installed on your system.

```
sudo apt-get install python-ldap
```

Then you can run the test:

```
cd seafile-server-latest
./pro/pro.py ldapsync --test
```

The test script checks your LDAP settings under the `[LDAP]` section of ccnet.conf. If everything works, it'll print the first ten users of the search results. Otherwise, it'll print out possible errors in your config.

## Setting Up LDAP/AD User Sync (optional)

In Seafile Pro, except for importing users into internal database when they log in, you can also configure Seafile to periodically sync user information from LDAP/AD server into the internal database.

- User's full name, department and contact email address can be synced to internal database. Users can use this information to more easily search for a specific user.
- User's Windows or Unix login id can be synced to the internal database. This allows the user to log in with its familiar login id.
- When a user is removed from LDAP/AD, the corresponding user in Seafile will be deactivated. Otherwise, he could still sync files with Seafile client or access the web interface.

After synchronization is complete, you can see the user's full name, department and contact email on its profile page.

### Active Directory

If you're using Active Directory, add the following options to ccnet.conf:

```
[LDAP]
......

[LDAP_SYNC]
ENABLE_USER_SYNC = true
DEACTIVE_USER_IF_NOTFOUND = true
SYNC_INTERVAL = 60
USER_OBJECT_CLASS = person
ENABLE_EXTRA_USER_INFO_SYNC = true
FIRST_NAME_ATTR = givenName
LAST_NAME_ATTR = sn
UID_ATTR = sAMAccountName
```

Meaning of each options:

- **ENABLE_USER_SYNC**: set to "true" if you want to enable ldap user synchronization
- **DEACTIVE_USER_IF_NOTFOUND**: set to "true" if you want to deactivate a user when he/she was deleted in AD server.
- **SYNC_INTERVAL**: The interval to sync. Unit is minutes. Defaults to 60 minutes.
- **USER_OBJECT_CLASS**: This is the name of the class used to search for user objects. In Active Directory, it's usually "person". The default value is "person".
- **ENABLE_EXTRA_USER_INFO_SYNC**: Enable synchronization of additional user information, including user's full name, department, and Windows login name, etc.
- **FIRST_NAME_ATTR**: Attribute for user's first name. It's "givenName" by default.
- **LAST_NAME_ATTR**: Attribute for user's last name. It's "sn" by default.
- **USER_NAME_REVERSE**: In some languages, such as Chinese, the display order of the first and last name is reversed. Set this option if you need it.
- **UID_ATTR**: Attribute for Windows login name. If this is synchronized, users can also log in with their Windows login name. In AD, the attribute `sAMAccountName` can be used as `UID_ATTR`.

If you choose `userPrincipalName` as the unique identifier for user, Seafile cannot use it as real email address to send notification emails to user. If the users in AD also have an email address attribute, you can sync these email addresses into Seafile's internal database. Seafile can then use them to send emails. The configuration option is:
- **CONTACT_EMAIL_ATTR**: usually you can set it to the `mail` attribute.

### Other LDAP servers

Add the following options to ccnet.conf:

```
[LDAP]
......

[LDAP_SYNC]
ENABLE_USER_SYNC = true
DEACTIVE_USER_IF_NOTFOUND = true
SYNC_INTERVAL = 60
USER_OBJECT_CLASS = userOfNames
ENABLE_EXTRA_USER_INFO_SYNC = true
FIRST_NAME_ATTR = givenName
LAST_NAME_ATTR = sn
UID_ATTR = uid
```

Meaning of each option:

- **ENABLE_USER_SYNC**: set to "true" if you want to enable ldap user synchronization
- **DEACTIVE_USER_IF_NOTFOUND**: set to "true" if you want to deactivate a user when he/she was deleted in LDAP server.
- **SYNC_INTERVAL**: The synchronization interval. Unit is minutes. Defaults to 60 minutes.
- **USER_OBJECT_CLASS**: This is the name of the class used to search for user objects. In OpenLDAP, you can use "userOfNames". The default value is "person".
- **ENABLE_EXTRA_USER_INFO_SYNC**: Enable synchronization of additional user information, including user's full name, department, and Windows/Unix login name, etc.
- **FIRST_NAME_ATTR**: Attribute for user's first name. It's "givenName" by default.
- **LAST_NAME_ATTR**: Attribute for user's last name. It's "sn" by default.
- **USER_NAME_REVERSE**: In some languages, such as Chinese, the display order of the first and last name is reversed. Set this option if you need it.
- **UID_ATTR**: Attribute for Windows/Unix login name. If this is synchronized, users can also log in with their Windows/Unix login name. In OpenLDAP, the attribute `uid` or something similar can be used.

### Importing Users without Activating Them

The users imported with the above configuration will be activated by default. For some organizations with large number of users, they may want to import user information (such as user full name) without activating the imported users. Activating all imported users will require licenses for all users in AD/LDAP, which may not be affordable.

Seafile provides a combination of options for such use case. First, you have to add below option to [LDAP_SYNC] section of ccnet.conf:

```
ACTIVATE_USER_WHEN_IMPORT = false
```

This prevents Seafile from activating imported users. Second, add below option to `seahub_settings.py`:

```
ACTIVATE_AFTER_FIRST_LOGIN = True
```

This option will automatically activate users when they login to Seafile for the first time.

With these configurations, an imported user can be searched and be shared with folders, but will not consume license until he/she logs in.

### Manually Trigger Synchronization

To test your LDAP sync configuration, you can run the sync command manually.

To trigger LDAP sync manually,

```
cd seafile-server-lastest
./pro/pro.py ldapsync
```

## Advanced LDAP/AD Integration Options

### Multiple BASE

Multiple base DN is useful when your company has more than one OUs to use Seafile. You can specify a list of base DN in the "BASE" config. The DNs are separated by ";", e.g. `ou=developers,dc=example,dc=com;ou=marketing,dc=example,dc=com`

### Additional Search Filter

Search filter is very useful when you have a large organization but only a portion of people want to use Seafile. The filter can be given by setting "FILTER" config. The value of this option follows standard LDAP search filter syntax (https://msdn.microsoft.com/en-us/library/aa746475(v=vs.85).aspx).

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

### Using TLS connection to LDAP/AD server

To use TLS connection to the directory server, you should install a valid SSL certificate on the directory server.

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

### Configure Multi-ldap Servers

Since seafile 5.1.4 pro edition, we support multi-ldap servers, that is besides base ldap server info in [LDAP] section, you can set other ldap servers info in [LDAP_MULTI_1], [LDAP_MULTI_2] ... [LDAP_MULTI_9] sections, so you can configure ten ldap servers to work with seafile. Multi-ldap servers mean that, when get or search ldap user, it will iterate all configured ldap servers until a match is found; When listing all ldap users, it will iterate all ldap servers to get all users; For Ldap sync it will sync all user/group info in all configured ldap servers to seafile.

For example I have configured base ldap server in `ccnet.conf` as follow:
```
[LDAP]
HOST = ldap://192.168.1.123/
BASE = ou=users,dc=example,dc=com
USER_DN = cn=admin,dc=example,dc=com
PASSWORD = secret
LOGIN_ATTR = mail
```
Then I can configure another ldap server in `ccnet.conf` as follow:
```
[LDAP_MULTI_1]
HOST = ldap://192.168.1.124/
BASE = ou=users,dc=example,dc=com
USER_DN = cn=admin,dc=example,dc=com
PASSWORD = secret
```

Before 6.3.8, all ldap servers share LOGIN_ATTR, USE_PAGED_RESULT, FOLLOW_REFERRALS attributes in [LDAP] section; For ldap user/group sync, all ldap servers share all ldap sync related attributes in [LDAP_SYNC] section.

Since seafile 6.3.8 pro, we support more independent config sections for each ldap server. The LOGIN_ATTR, USE_PAGED_RESULT, FOLLOW_REFERRALS options can be set independently in each [LDAP_MULTI_x] section. Furthermore, independent [LDAP_SYNC_MULTI_x] sections can be set for each LDAP server. That is, each LDAP server can use different LDAP sync options.

There are still some shared config options that can only be set in [LDAP_SYNC] section, which is used for all LDAP servers.

* SYNC_INTERVAL
* DEACTIVE_USER_IF_NOTFOUND
* ACTIVATE_USER_WHEN_IMPORT
* IMPORT_NEW_USER
* DEL_GROUP_IF_NOT_FOUND

These options are used to control synchronization behaviors, so they're shared for all LDAP servers.

NOTE: It is recommended to have a [LDAP_SYNC_MULTI_x] section for each [LDAP_MULTI_x] section. Otherwise the LDAP sync process will use the options in [LDAP_SYNC] section for that LDAP server.
