# Deploy with Windows

## Setup and Upgrade

Seafile Windows Community Edition supports SQLite/MySQL database.

- [Download and Setup Seafile Windows Server](download_and_setup_seafile_windows_server.md)
- [Deploy Seafile with MySQL](deploy_with_mysql.md)
- [Deploy Seafile with Apache](deploy_with_apache.md)
- [Deploy Seafile with Nginx](deploy_with_nginx.md)
- [LDAP Integration](../deploy/using_ldap.md)
- [Install Seafile Server as a Windows Service](install_seafile_server_as_a_windows_service.md)
- [Ports used by Seafile Windows Server](ports_used_by_seafile_windows_server.md)
- [Upgrading Seafile Windows Server](upgrading_seafile_windows_server.md)
- [Options & Customization](../config/README.md)

For more information on Seafile server, check the documents on [Seafile Linux version](../deploy/README.md)

## Server Administration

- [Garbage Collecting Unused Blocks on Seafile Server](windows_gc.md)
- [Running seaf-fsck on corrupted repositories](windows_fsck.md)

## Common Issues

If you failed to set up Seafile server, first check seafserv-applet.log.
### "ERROR: D:/seafile-server\seahub.db not found"

This file is created during Seafile initialization. Please:

- Check whether your Python and the ``PATH`` for Python is correctly set.
- Put Seafile server package in a simple path, like ``C:\seafile-packages``.

### Failed to create seahub.db

Use python version 2.7.4 32bit, do not use python 3+.
### Can not upload/download files in the Web interface

Make sure you have modified ``SERVICE_URL`` in ccnet.conf.

### The browser can't get the css and javascript files

- Use python 2.7.4 32bit. If you have installed other python version, uninstall it and install python 2.7.4. Restart seafile server to see whether the problem has gone.
- Delete non-ASCII keys from the registry path ``HKEY_CLASSES_ROOT\MIME\Database\Content`` Type, and try again.



