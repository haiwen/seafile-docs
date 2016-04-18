# Download and Setup Seafile Windows Server

## Download/Uncompress
### Install Python 2.7.4 32bit

- Download and install [python 2.7.4 32bit](http://python.org/ftp/python/2.7.4/python-2.7.4.msi)
- Add the installation path of python2.7 to the system PATH environment variable. If you installed python 2.7 to ``C:\Python27`` add ``C:\Python27`` to the PATH environment variable


**Warning**: Be sure to use Python 2.7.4 32bit. 64 bit and other versions can't work.

### Download/Uncompress Seafile Server

- Get the latest version of Seafile Server program
- Create a new folder to store seafile program, such as ``C:\SeafileProgram\``. Please remember the location of the folder, we'll use it later.
- Uncompress ``seafile-server_5.0.3_win32.tar.gz`` to ``C:\SeafileProgram\``

Now you have a folder like this:
```sh
C:\SeafileProgram
         |__ seafile-server-5.0.3
```
## Start/Initialization

### Start Seafile Server

Go to the folder ``C:\SeafileProgram\seafile-server-5.0.3\``, and double click run.bat to start Seafile Server. You should notice a seafile icon appears in the system tray.
Choose a disk to store Seafile Server data

Now you'll be prompted a dialog to choose a disk to store the data of seafile server

- Please choose a disk with enough free space
- Once you clicked the OK button, Seafile would create a folder named seafile-server under the disk you choosed. That would be the data folder of Seafile Server. If you choose disk D, your data folder would be ``D:\seafile-server``

### Add an admin account

Right click the tray icon of Seafile Server, choose __Add an admin__. Input your admin username and password in the prompted dialog.

If the operation is successful, the tray icon would show a bubble saying __Successully added the admin acount__

### Configure Seafile Server

After initialization, there are some options need to be configured:

- Right click the tray icon, choose __Open seafile-server folder__. Your seafile-server data folder would be opened.
- Edit the file `conf/ccnet.conf`. Modify the following line of `ccnet.conf`:
```
SERVICE_URL = XXX
```

- Change the value of `SERVICE_URL` to `http://<your ip address>:8000`. Say the ip address of your windows server is 192.168.1.100, then change it to `SERVICE_URL = http://192.168.1.100:8000`

After the edit, right click tray icon, choose __Restart seafile__

### Visit Seahub

Open your browser, and visit `http://127.0.0.1:8000`. Login with the admin account. If you can login, the initialization is successful.
Configuration done

Seafile Server configuration is finished. See Seafile Client Manual for how to use the client

### You may also want to read about:

- [Deploy Seafile with MySQL](deploy_with_mysql.md)
- [Deploy Seafile with Apache](deploy_with_apache.md)
- [Deploy Seafile with Nginx](deploy_with_nginx.md)
- [LDAP Integration](../deploy/using_ldap.md)
- [Install Seafile Server as a Windows Service](install_seafile_server_as_a_windows_service.md)
- [Ports used by Seafile Windows Server](ports_used_by_seafile_windows_server.md)
- [Upgrading Seafile Windows Server](upgrading_seafile_windows_server.md)
- [Options & Customization](../deploy/server_configuration.md)
