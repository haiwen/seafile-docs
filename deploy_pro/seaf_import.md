# Import Directory To Seafile

Since seafile 5.1.3 pro edition, we support importing a local directory on the server to seafile. It's a handy tool for the system admin to import files from existing file servers (NFS, Samba etc.).

To import a directory, use the `seaf-import.sh` script in seafile-server-latest directory.

```
usage :
seaf-import.sh
 -p <import dir path, must set>
 -n <repo name, must set>
 -u <repo owner, must set>
```

The specified directory will be imported into Seafile as a library. You can set the name and owner of the imported library.

Run `./seaf-import.sh -p <dir you want to import> -n <repo name> -u <repo owner>`,

```
Starting seaf-import, please wait ...
[04/26/16 03:36:23] seaf-import.c(79): Import file ./runtime/seahub.pid successfully.
[04/26/16 03:36:23] seaf-import.c(79): Import file ./runtime/error.log successfully.
[04/26/16 03:36:23] seaf-import.c(79): Import file ./runtime/seahub.conf successfully.
[04/26/16 03:36:23] seaf-import.c(79): Import file ./runtime/access.log successfully.
[04/26/16 03:36:23] seaf-import.c(183): Import dir ./runtime/ to repo 5ffb1f43 successfully.
 run done
Done.
```

Login to seafile server with the specified library owner, you will find a new library with the specified name.
