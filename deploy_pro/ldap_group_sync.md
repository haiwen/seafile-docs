# Importing Groups from LDAP/AD

Since version 4.1.0, the Pro Edition supports importing (syncing) groups from LDAP or Active Directory.

## How It Works

The importing or syncing process maps groups from LDAP directory server to groups in Seafile's internal database. This process is one-way.

* Any changes to groups in the database won't propagate back to LDAP;
* Any changes to groups in the database, except for "setting a member as group admin", will be overwritten in the next LDAP sync operation. If you want to add or delete members, you can only do that on LDAP server.
* The creator of imported groups will be set to the system admin.

Some LDAP servers, such as AD, allows setting a group as member of another group. This is called "nested group". Our process supports syncing nested groups. Supposed group B is a member of group A, the result would be: every member of group B will be imported as a member of both group A and group B.

Since version 6.3.0, in addition to syncing nested groups, we also support importing groups from OU to the Seafile's Departments. This will map the hierarchical relationship of the OUs to departments hierarchy. 

There are two modes of operation:

* Periodical: the syncing process will be executed in a fixed interval
* Manual: there is a script you can run to trigger the syncing once

## Prerequisite

You have to install python-ldap library in your system.

For Debian or Ubuntu

```
sudo apt-get install python-ldap
```

For CentOS or RedHat

```
sudo yum install python-ldap
```

## Configuration

Before enabling LDAP group sync, you should have configured LDAP authentication. See [Configure Seafile to use LDAP](using_ldap.md) for details.

The following are LDAP group sync related options. They're in the "[LDAP_SYNC]" section of [ccnet.conf](../config/ccnet-conf.md).

* **ENABLE_GROUP_SYNC**: set to "true" if you want to enable ldap group syncing
* **IMPORT_GROUP_STRUCTURE**: you may want to preserve the hierarchical relationship of the OU, when import groups from OU to Seafile. set to "true"; need Seafile-pro-6.3.0 and above version
* **DEL_GROUP_IF_NOT_FOUND**: set to "true", will deleted the groups if not found it in the OU; need Seafile-pro-6.3.0 and above version
* **CREATE_GROUP_REPO**: set to "true", if you want to automatically create a Department Libraries when imoprt groups from OU; need Seafile-pro-6.3.0 and above version
* **GROUP_OBJECT_CLASS**: This is the name of the class used to search for group objects. In Active Directory, it's usually "group"; in OpenLDAP or others, you may use "groupOfNames","groupOfUniqueNames" or "posixGroup", depends on your LDAP server. The default value is "group". And **since version 6.3.0**, we have added **"organizationalUnit"**, if you want to import groups by OU, you should and only set `GROUP_OBJECT_CLASS=organizationalUnit`.
* **SYNC_INTERVAL**: The interval to sync. Unit is minutes. Default to 60 minutes.
* **GROUP_FILTER**: An additional filter to use when searching group objects. If it's set, the final filter used to run search is "(&(objectClass=GROUP_OBJECT_CLASS)(GROUP_FILTER))"; otherwise the final filter would be "(objectClass=GROUP_OBJECT_CLASS)".
* **GROUP_MEMBER_ATTR**: The attribute field to use when loading the group's members. For most directory servers, the attributes is "member", which is the default value.For "posixGroup", it should be set to "memberUid".
* **USER_ATTR_IN_MEMBERUID**: The user attribute set in 'memberUid' option, which is used in "posixGroup".The default value is "uid".

The search base for groups is the "BASE_DN" set in "[LDAP]" section of ccnet.conf. 

### Sync groups from LDAP or AD

Here is an example configuration for syncing nested groups in Active Directory:

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

For AD, you usually don't need to configure other options except for "ENABLE_GROUP_SYNC". That's because the default values for other options are the usual values for AD. If you have special settings in your LDAP server, just set the corresponding options.

Here is an example configuration for syncing nested groups in OpenLDAP:

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

### Sync OU to departments

If you want to sync groups by OU, in addition to `ENABLE_GROUP_SYNC = true`, you should add the following options:

* **GROUP_OBJECT_CLASS=organizationalUnit**: Specify to import groups from the OU.(Must be configured)
* **IMPORT_GROUP_STRUCTURE=true**：Preserve the hierarchical relationship between departments or groups in the OU.(Recommended)
* **DEL_GROUP_IF_NOT_FOUND=true**：Will deleted the groups if not found it in the OU.(Use with caution)
* **CREATE_GROUP_REPO=true**：Automatically create a Department Libraries when imoprt groups from OU.(Recommended)

Here is an example configuration for syncing OU groups:(Do not need to distinguish between AD and OpenLDAP.)

```
[LDAP]
HOST = ldap://192.168.1.123/
BASE = cn=users,dc=example,dc=com
USER_DN = administrator@example.local
PASSWORD = secret
LOGIN_ATTR = mail

[LDAP_SYNC]
ENABLE_GROUP_SYNC = true
GROUP_OBJECT_CLASS = organizationalUnit
IMPORT_GROUP_STRUCTURE = true
DEL_GROUP_IF_NOT_FOUND = false
CREATE_GROUP_REPO = true
SYNC_INTERVAL = 60
```

**NOTE** Periodical sync won't happen immediately after you restart seafile server. It gets scheduled after the first sync interval. For example if you set sync interval to 30 minutes, the first auto sync will happen after 30 minutes you restarts. To sync immediately, you need to manually trigger it. This is covered in the next section.

After the sync is run, you should see log messages like the following in logs/seafevents.log. And you should be able to see the groups in system admin page.

```
[2015-03-30 18:15:05,109] [DEBUG] create group 1, and add dn pair CN=DnsUpdateProxy,CN=Users,DC=Seafile,DC=local<->1 success.
[2015-03-30 18:15:05,145] [DEBUG] create group 2, and add dn pair CN=Domain Computers,CN=Users,DC=Seafile,DC=local<->2 success.
[2015-03-30 18:15:05,154] [DEBUG] create group 3, and add dn pair CN=Domain Users,CN=Users,DC=Seafile,DC=local<->3 success.
[2015-03-30 18:15:05,164] [DEBUG] create group 4, and add dn pair CN=Domain Admins,CN=Users,DC=Seafile,DC=local<->4 success.
[2015-03-30 18:15:05,176] [DEBUG] create group 5, and add dn pair CN=RAS and IAS Servers,CN=Users,DC=Seafile,DC=local<->5 success.
[2015-03-30 18:15:05,186] [DEBUG] create group 6, and add dn pair CN=Enterprise Admins,CN=Users,DC=Seafile,DC=local<->6 success.
[2015-03-30 18:15:05,197] [DEBUG] create group 7, and add dn pair CN=dev,CN=Users,DC=Seafile,DC=local<->7 success.
```

## Manually Trigger Syncing

To trigger LDAP sync manually,

```
cd seafile-server-lastest
./pro/pro.py ldapsync
```
