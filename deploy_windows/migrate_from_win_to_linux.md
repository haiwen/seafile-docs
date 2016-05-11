# Migrate From Windows to Linux

This tutorial show you how to migrate Seafile from Windows(using SQLite) to Linux.

### 1. Deploying Seafile Under Linux

First, you should [Deploy Seafile with SQLite](../deploy/using_sqlite.md). And we assume that you deploy Seafile under `/home/haiwen/` directory.

### 2. Replace Config Files And Databases

#### Delete config files and databases in Linux

```
rm /home/haiwen/seahub_settings.py
rm /home/haiwen/seahub.db
rm -r /home/haiwen/seafile-data
cp /home/haiwen/ccnet/seafile.ini /home/haiwen/seafile.ini
rm -r /home/haiwen/ccnet
```

> Note: `seafile.ini` is used to record the path to `seafile-data`, we will use it later, so we just copy it out, not delete it.

#### Copy config files and databases to Linux

- copy file `seahub_settings.py` from Windows **seafile-server** to Linux `/home/haiwen/`;

- copy file `seahub.db` from Windows **seafile-server** to Linux `/home/haiwen/`;

- copy sub-directory `seafile-data` from Windows **seafile-server** to Linux `/home/haiwen/`;

- copy sub-directory `ccnet` from Windows **seafile-server** to Linux `/home/haiwen/`;

- copy `/home/haiwen/seafile.ini` to new Linux **ccnet** directory.

### Start Seafile

```
./seafile.sh start
./seahub.sh start
```
