# FAQ

## Questions about file syncing

#### When downloading a library, the client hangs at "connecting server"

First, you can check the Seafile client log (`~/.ccnet/logs/seafile.log` for Linux, `C:/users/your_name/ccnet/logs/seafile.log` for Windows) to see what's wrong.

Possible reasons:

* Firewall: Ensure the firewall is configured properly. See [Firewall Settings for Seafile Server](deploy/using_firewall.md)

#### How to add more verbose log information at the client

Set environment variable `SEAFILE_DEBUG = all` before running Seafile desktop client. On Linux, you can open a terminal and type: 

```
export SEAFILE_DEBUG=all
./seafile-applet
```

## Questions about server setup

#### Failed to upload/download file online

* Make sure you firewall for seafile fileserver is opened.
* Make `SERVICE_URL` in ccnet.conf and `FILE_SERVER_ROOT` in seahub_settings.py are set correctly.
* Using chrome/firefox debug mode to find which link is given when click download button and what's wrong with this link

#### Does Seafile server support Python 3?

No, You must have python 2.6.5+ or 2.7 installed on your server.

#### Can Seafile server run on FreeBSD?

There was an unconfirmed solution on the internet, which later has vanished.
(Please explain the installation routine if you successfully set up Seafile in FreeBSD.)

#### Website displays "Page unavailable", what can I do?

* You can check the back trace in seahub log files(`installation folder/logs/seahub_django_request.log`)

* You can also turn on debug by adding <code>DEBUG = True</code> to seahub_settings.py and restart seahub by <code>./seahub.sh restart</code>, then refresh that page, all the debug infomations will be displayed. Make sure ./seahub.sh was started as: ./seahub.sh start-fastcgi

#### Avatar pictures vanished after upgrading server, what can I do?

* You need to check whether the "avatars" symbolic link under seahub/media/ is correctly link to ../../../seahub-data/avatars. If not, you need to correct the link according to the "minor upgrade" section in [Upgrading-Seafile-Server](deploy/upgrade.md)

* If your avatars link is correctly linked, and avatars are still broken, you may refresh seahub cache by `rm -rf /tmp/seahub_cache/*`

#### How to change seafile-data location after setup?

Modify file seafile.ini under ccnet. This file contains the location of seafile-data. Move seafile-data to another place, like `/opt/new/seafile-data`. Then modify the file accordingly.

#### Failed to send email, what can I do?

Please check logs/seahub.log.

There are some common mistakes:

1. Check whether there are some typos in the config, e.g., forget single quote, `EMAIL_HOST_USER = XXX`, which should be `EMAIL_HOST_USER = 'XXX'`
1. Your mail server is not available.

#### After upgrade Web UI is broken because CSS files can't be loaded

Please remove the cache and try again, `rm -rf /tmp/seahub_cache/*`. If you configured memecached, restart memcached, then restart Seahub.

If the problem is not fixed, check whether seafile-server-latest point to the right folder. Then check whether `seafile-server-latest/seahub/media/CACHE` is correctly generated (it should contain the auto-generated CSS file). 

## Questions about Clustering

### Page layout broken because seahub/media/CACHE is created only on first node

Please add

    COMPRESS_CACHE_BACKEND = 'locmem://'

to seahub_settings.py as documented http://manual.seafile.com/deploy_pro/deploy_in_a_cluster.html

This will tell every node to generate the CSS CACHE in its local folder.


## Questions about server maintenance

### How to migrate libraries and groups from one account to another?

Since version 4.4.2, system admin can migrate libraries and groups from one account to another existing account using [RESTful web api](https://github.com/haiwen/seafile-docs/blob/master/develop/web_api.md#migrate-account).

### Seafile GC shows errors, FSCK can’t fix them

GC scans the history. But FSCK only scan the currently version. You can ignore the error. It is a minor issue.

## Questions about LDAP and User management

### How to restrict Seafile access to a certain accounts in AD

You can use FILTER field in LDAP configuration in `ccnet.conf`. For example, the following filter restricts the access to Seafile to members of a group.

    FILTER = (memberOf=cn=group,cn=users,DC=x)

AD also supports groups within group. The following filter restricts the access to Seafile to members/groups of a group.

    FILTER = (memberOf:1.2.840.113556.1.4.1941:=cn=group,cn=users,DC=x)

For more information on the Filter syntax, see http://msdn.microsoft.com/en-us/library/aa746475%28VS.85%29.aspx
