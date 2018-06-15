# FAQ

## Very common problem

#### Seafile/Seahub can't start after upgrade or any other reasons

Please check whether the old version of Seahub is still running.

Please check whether you use the right user to run or upgrade Seafile. Pay special attention to the following files:

* `seafile-directory/seafile-server-6.0.3/runtime/error.log`
* `seafile-directory/seafile-server-6.0.3/runtime/access.log`
* `seafile-directory/logs/*`

You can run the following command to change fix the permission for the whole directory:

```
chown -R userx:groupx seafiledirectory
```

You can also try remove the cache directory of Seahub

```
rm -rf /tmp/seahub_cache
```

## Setup

### Failed to upload/download file online

* Make sure your firewall for Seafile fileserver is opened.
* Make sure `SERVICE_URL` in ccnet.conf and `FILE_SERVER_ROOT` in seahub_settings.py are set correctly. Furthermore check that you haven't overwritten them using the settings in the Seahub Admin section.
* Use Chrome/Firefox debug mode to find out which address is being used when clicking download button and whether it is correct.

### Seahub/Seafile started correctly, but when visiting the web interface, it shows "Internal Server Error"

It is mostly likely some required Python packages of Seahub is not installed correctly.

You can check the detailed error messages in `/var/log/nginx/seahub.error.log` if you use Nginx.

### Website displays "Page unavailable", what can I do?

* You can check the back trace in Seahub log files (`installation folder/logs/seahub_django_request.log`)

* You can also turn on debug mode by adding `DEBUG = True` to `seahub_settings.py` and restarting Seahub with `./seahub.sh restart`, then refresh the page, all the debug infomations will be displayed. Make sure ./seahub.sh was started as: ./seahub.sh start-fastcgi in case you're using fastcgi.


### Failed to send email, what can I do?

Please check logs/seahub.log.

There are some common mistakes:

1. Check whether there are typos in the config (`seahub_settings.py`, e.g. you could have forgotten to add a single quote `EMAIL_HOST_USER = XXX`, which should be `EMAIL_HOST_USER = 'XXX'` or you could have a space at the end of a config line.
2. Your mail server is not available.


### Can't connect to LDAP server with ldaps

#### Description

Seafile server can't communication with my LDAP server. The ccnet.log shows:

```
[08/05/16 09:47:17] ../common/session.c(398): Accepted a local client
[08/05/16 09:47:17] user-mgr.c(335): ldap_initialize failed: Bad parameter to an ldap routine.
[08/05/16 09:47:17] user-mgr.c(773): Ldap init and bind failed using ‘cn=XXX,dc=XXX,dc=XXX': ‘XXXXXXX' on server 'ldaps://10.XX.XX.XX/'.
```

#### Answer

If you are using pro edition, you can check the LDAP configuration by running a script as described in  http://manual.seafile.com/deploy_pro/using_ldap_pro.html  (search Testing your LDAP Configuration).

If the script can correctly talk to ldap server, it is most likely caused by incompatible of bundled LDAP libraries. You can follow http://manual.seafile.com/deploy/using_ldap.html (the end of document) to remove the bundled LDAP libraries.


### How to restrict Seafile access to certain accounts in AD

You can use FILTER field in LDAP configuration in `ccnet.conf`. For example, the following filter restricts the access to Seafile to members of a group.

    FILTER = memberOf=cn=group,cn=users,DC=x

AD also supports subgroups. The following filter restricts the access to Seafile to membersand subgroups of a group.

    FILTER = memberOf:1.2.840.113556.1.4.1941:=cn=group,cn=users,DC=x

For more information on the Filter syntax, see http://msdn.microsoft.com/en-us/library/aa746475%28VS.85%29.aspx


## upgrade

### After upgrading Web UI is broken because CSS files can't be loaded


Please remove the cache and try again, `rm -rf /tmp/seahub_cache/*`. If you configured memecached, restart memcached, then restart Seahub.

If the problem is not fixed, check whether seafile-server-latest point to the correct folder. Then check whether `seafile-server-latest/seahub/media/CACHE` is correctly being generated (it should contain the auto-generated CSS file(s)).


### Avatar pictures vanished after upgrading the server, what can I do?


* You need to check whether the "avatars" symbolic link under seahub/media/ is linking to ../../../seahub-data/avatars. If not, you need to correct the link according to the "minor upgrade" section in [Upgrading-Seafile-Server](deploy/upgrade.md).

* If your avatars link is correct, and avatars are still broken, you may need to refresh Seahub cache using `rm -rf /tmp/seahub_cache/*` or by restarting memcached if being used.


## System can't start

### Seahub can't be started after power failure

Please try clean the cache directory `seahub_cache`.

Please also check the permission of `seahub.pid`, `seahub_django_request.log` and `seahub.log`. If Seahub can't write to these files, it will fail to start.


## Seafevents can't be started

#### Description

Office files online preview can't work. There is no logs in seafevents.log. From `controller.log`, the seafevent process is being started again and again.

#### Answer

Please check the permission of `seafevent.pid` and `seafevent.log`. If seafevent can't write to these files, it will fail to start.

You can also try start seafevents manually following: https://download.seafile.com/f/423d5d6301/


## Management

### How to migrate libraries and groups from one account to another?

Since version 4.4.2, system admins can migrate libraries and groups from one account to another existing account using [RESTful web api](https://github.com/haiwen/seafile-docs/blob/master/develop/web_api.md#migrate-account).


### Seafile GC shows errors, FSCK can’t fix them

GC scans the history. But FSCK only scans the current version. You can ignore the error. It is a minor issue.


## Ceph and S3

### Seafile server can't started when using Ceph

#### Description

Seafile server can't started when using Ceph as storage backend. seafile.log is empty. controller.log shows:

```
[10/20/16 12:39:29] seafile-controller.c(568): pid file /opt/seafile/pids/seaf-server.pid does not exist
[10/20/16 12:39:29] seafile-controller.c(588): seaf-server need restart...
[10/20/16 12:39:29] seafile-controller.c(198): starting seaf-server ...
```

#### Answer

This is most likely caused by Ceph library incompatible.

You can install `librados` provided by the Linux distribution, then remove bundled libraries:

```
cd seafile-server-latest/seafile/lib
rm librados.so.2 libstdc++.so.6 libnspr4.so
```

You can also run `seaf-fsck.sh`. It will print detailed message if Ceph library incompatible.

### Virus scan and search index doesn't work with HTTPS S3

The `use_https = true` options in seafile.conf config are working just for regular file operations to S3, but not indexing or AV scanning.

Create ‘/etc/boto.cfg’ and add the following:

[Boto]
is_secure = True

Then the issue can be resolved.


### GC error when removing blocks in Ceph

#### Description

We just did a GC run which came up with errors when deleting blocks.
This seems to happen with all blocks/libraries. Below is an example for a single library.

```
Starting seafserv-gc, please wait ...
[08/29/16 09:15:41] gc-core.c(768): Database is MySQL/Postgre, use online GC.
[08/29/16 09:15:41] gc-core.c(792): Using up to 10 threads to run GC.
[08/29/16 09:15:41] gc-core.c(738): GC version 1 repo Documents(135ca71c-da2b-4b07-86e3-c7a1d46b9b22)
[08/29/16 09:16:04] gc-core.c(510): GC started for repo 135ca71c. Total block number is 294.
[08/29/16 09:16:04] gc-core.c(68): GC index size is 1024 Byte for repo 135ca71c.
[08/29/16 09:16:04] gc-core.c(269): Populating index for repo 135ca71c.
[08/29/16 09:16:04] gc-core.c(334): Traversed 33 commits, 402 blocks for repo 135ca71c.
[08/29/16 09:16:04] gc-core.c(559): Scanning and deleting unused blocks for repo 135ca71c.
[08/29/16 09:16:04] ../../common/block-backend-ceph.c(463): [block bend] Failed to remove block 79fc986a: No such file
or directory.
[08/29/16 09:16:04] ../../common/block-backend-ceph.c(463): [block bend] Failed to remove block ae2678f8: No such file
or directory.
[08/29/16 09:16:04] ../../common/block-backend-ceph.c(463): [block bend] Failed to remove block 9fe1ca0b: No such file
or directory.
[08/29/16 09:16:04] ../../common/block-backend-ceph.c(463): [block bend] Failed to remove block 4cad277e: No such file
or directory.
[08/29/16 09:16:04] ../../common/block-backend-ceph.c(463): [block bend] Failed to remove block e9c94b16: No such file
or directory.
[08/29/16 09:16:04] gc-core.c(577): GC finished for repo 135ca71c. 294 blocks total, about 402 reachable blocks, 5
blocks are removed.

[08/29/16 09:16:04] gc-core.c(839): === GC is finished ===
seafserv-gc run done
```

#### Answer

Your "issue" looks similar to the one discussed here:
http://lists.ceph.com/pipermail/ceph-users-ceph.com/2015-November/005837.html

That should be related to the behavior of cache tier in Ceph. You could
try to use "rados rm" command to remove that object. If it returns the
same error (no such file or directory), it should be the same issue. You
should try to copy that object out before removing it, in case you still
need it later.



## Clustering

### Page layout broken because seahub/media/CACHE is created only on first node

Please add

    COMPRESS_CACHE_BACKEND = 'django.core.cache.backends.locmem.LocMemCache'

to `seahub_settings.py` as documented at http://manual.seafile.com/deploy_pro/deploy_in_a_cluster.html

This is going to tell every node to generate the CSS CACHE in its local folder.



## Client

* [Common problems about desktop syncing client](client.md)


## Use non standard nginx port

If you want to use a non standard nginx port other than 80 you have to modify following configuration settings:

Change ccnet.conf

  `SERVICE_URL = https://yourSeafileURL:yourNginxPort`

Change seahub_settings.py

	`FILE_SERVER_ROOT = https://yourSeafileURL:yourNginxPort/seafhttp`
	`SITE_BASE = https://yourSeafileURL:yourNginxPort`

Change nginx config file for seafile:

```
  server {
    listen yourNginxPort; # <--------------------------------------- Non standard PORT
    ...
  location / {
    ...
	proxy_set_header   Host $host:$server_port;```
