# Seafile Real-Time Backup Server

NOTE: The real-time backup feature is currently in beta state. It may have minor issues on the backup server side. But this feature will not affect the functionality or data integrity of the primary server.

Backup is the procedure that copies data from a primary server (which is running production service) to a backup server.

Backup is an important procedure to keep data safe. The basic backup procedure described in [this documentation](../maintain/backup_recovery.md) has a few drawbacks:

- The backup is done in fixed "backup windows" (once per day or a few times per day). The latest data written between two backup windows will be lost if the primary server storage is damaged.
- The backup procedure backup database and data directory separately. In the backup server, some entries in the database may become inconsistent with the data directory. This causes some libraries become "corrupted" after restore.

The real-time backup server uses a syncing algorithm similar to the Seafile desktop client to retrieve data from the primary server. It works as follows:

- Whenever a library is updated, the primary server notifies the backup server to retrieve the changed data. With a delta syncing algorithm, this procedure runs quickly and updates the backup server in nearly real-time.
- The backup server also checks all libraries on the primary server at a fixed period. Any new or updated libraries will be synced to the backup server. This will pick up any legged updates due to glitches in the above real-time sync procedure.
- The backup server always keep the database and data directory consistent. So no libraries on the backup server will be in corrupted state (unless they're already corrupted on the primary server).
- The full history of all libraries will be backed up. This is not like the desktop client, which only syncs the latest state of a library.

There are two sets of data that need to be backup:

- The seafile-data directory and the core library metadata tables in the seafile database. This data is the core data structures of the libraries in Seafile. They're synced to the backup server with Seafile's syncing algorithm. In this procedure, the metadata tables are kept consistent with the seafile-data directory.
- All other tables in the database (including seafile, ccnet and seahub databases) are backup with MySQL replication.

## Configure Real-Time Backup Server

We assume you already have a primary server running, and now you want to setup a backup server.

The steps to setup the backup server are:

1. Install Seafile on the backup server
2. Configure MySQL replication between the primary server and the backup server
3. Configure Seafile syncing between the primary server and the backup server

### Install Seafile on the Backup Server

You should install Seafile Pro Edition on the backup server according to [this documentation](../deploy_pro/download_and_setup_seafile_professional_server.md). Since the real-time backup feature is only available for 5.1.0 or later, you also have to upgrade your primary server to 5.1.0 version or later.

When installing Seafile on the backup server, you have to notice:

- The database names (ccnet, seafile and seahub database) should be the same as the names on the primary server.
- You don't need to enable other Pro features, such as Office file preview, search indexing, file auditing etc.

### Configure MySQL Replication

MySQL replication asynchronously replicates database updates from a Master server (in our case, the primary server) to a Slave server (the backup server). To better understand how MySQL replication works and how to configure it, you should first read [MySQL official documentation](https://dev.mysql.com/doc/refman/5.6/en/replication-howto.html). The following steps are based on the steps in MySQL documentation, with some modifications for Seafile.

In the following discussion, we'll use "primary server" and "master server", "backup server" and "slave server" interchangeably.

#### Modify MySQL Server Configuration on Primary Server (my.cnf)

On the primary server, add following options to my.cnf:

```
[mysqld]
log-bin=mysql-bin
server-id=1
```

In the my.cnf of the primary server, another important option is `expire_logs_days` ([reference](http://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_expire_logs_days)). This option controls the retention time of the binary log, which is used for replication. The default value of this option is to keep binary log files forever. You can set this option to keep the binary log files for specific days. Binary log files older than the specified days will be deleted. So if the backup server is offline for more than `expire_logs_days`, the replication cannot be resumed after the backup server is online. We recommend to set this option to a long enough time.

After saving the changes, you should restart MySQL on primary server.

#### Create a User for Replication in MySQL

On the primary server, create a user dedicated for replication. In MySQL client prompt,

```
CREATE USER 'repl'@'%' IDENTIFIED BY 'slavepass';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';
```

Replace the user name and password with your own choice.

#### Obtain the Replication Master Binary Log Coordinates

Before running this step, you should stop Seafile service on the primary server, so that no update will be written into database.

On the primary (Master) server, in MySQL client prompt,

```
FLUSH TABLES WITH READ LOCK;
SHOW MASTER STATUS;
```

You'll get output similar to the following:

```
+------------------+----------+--------------+------------------+-------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+------------------+----------+--------------+------------------+-------------------+
| mysql-bin.000002 |   368915 |              |                  |                   |
+------------------+----------+--------------+------------------+-------------------+
```

The `File` and `Position` fields in output will be used to configure the backup server (replication Slave).

#### Export Existing Data on the Primary Server

Exporting data from the databases on the primary server with mysqldump:

```
mysqldump -u <user> -p<password> --databases \
--ignore-table=<seafile_db>.Repo --ignore-table=<seafile_db>.Branch --ignore-table=<seafile_db>.RepoHead \
--ignore-table=<seahub_db>.base_userlastlogin --ignore-table=<seahub_db>.django_session \
--ignore-table=<seahub_db>.sysadmin_extra_userloginlog --ignore-table=<seahub_db>.UserTrafficStat \
--ignore-table=<seahub_db>.FileAudit --ignore-table=<seahub_db>.FileUpdate --ignore-table=<seahub_db>.PermAudit \
--ignore-table=<seahub_db>.Event --ignore-table=<seahub_db>.UserEvent --ignore-table=<seahub_db>.avatar_avatar \
--ignore-table=<seahub_db>.avatar_groupavatar --ignore-table=<seahub_db>.avatar_uploaded \
--master-data <seafile_db> <ccnet_db> <seahub_db> > dbdump.sql
```

You should replace `<user>`, `<password>` with your MySQL admin user and password. You should replace `<seafile_db>`, `<seahub_db>` and `<ccnet_db>` with your database names.

#### Modify MySQL Server Configuration on Backup Server (my.cnf)

On the backup server, add following options to my.cnf:

```
[mysqld]
server-id=2
replicate-ignore-table = <seafile db>.Repo
replicate-ignore-table = <seafile db>.Branch
replicate-ignore-table = <seafile db>.RepoHead
replicate-ignore-table = <seahub db>.base_userlastlogin
replicate-ignore-table = <seahub db>.django_session
replicate-ignore-table = <seahub db>.sysadmin_extra_userloginlog
replicate-ignore-table = <seahub db>.UserTrafficStat
replicate-ignore-table = <seahub db>.FileAudit
replicate-ignore-table = <seahub db>.FileUpdate
replicate-ignore-table = <seahub db>.PermAudit
replicate-ignore-table = <seahub db>.avatar_avatar
replicate-ignore-table = <seahub db>.avatar_groupavatar
replicate-ignore-table = <seahub db>.avatar_uploaded
replicate-ignore-table = <seahub db>.Event
replicate-ignore-table = <seahub db>.UserEvent
```

The above configuration tells the backup server to ignore following tables on replication:

- The library metadata tables in Seafile db：Repo, Branch, RepoHead。These tables will be synced by Seafile backup server itself.
- Local or temporary tables in Seahub database. When the admin logs into the backup server to view the data, these tables may be updated on the backup server. To avoid conflicts with the replicated entries, we ignore them on replication.

Notes:

- The `server-id` for the primary and backup server must be different.
- You should replace `<seafile db>` and `<seahub db>` with your database names.

Restart MySQL server on backup server, with `--skip-slave-start` option so that replication does not start.

```
sudo /etc/init.d/mysql start --skip-slave-start
```

#### Import Existing Data into backup server

Importing existing data into the backup server's MySQL:

```
mysql -u <usr> -p<pas> < dbdump.sql
```

Replace `<user>` and `<pass>` with your MySQL admin user name and password.

#### Start Replication

Unlock MySQL on the primary server. In MySQL client prompt,

```
unlock tables;
```

On the backup server, setup replication start coordinates:

```
CHANGE MASTER TO MASTER_HOST='primary-host', MASTER_USER='user', MASTER_PASSWORD='slavepass', MASTER_LOG_FILE='bin-log-file', MASTER_LOG_POS=position;
```

Replace `primary-host` with the MySQL master server address; Replace `user` with the dedicated user for replication; Replace `slavepass` with the dedicated user's password; Replace `bin-log-file` and `position` with the information you obtained in the "Obtain the Replication Master Binary Log Coordinates" section.

Start replication on the backup server. In MySQL client prompt,

```
start slave;
```

After staring replication, you should see some log messages in MySQL's error.log on the backup server, stating the replication is started. And the slave will catch up with any new updates on the master server.

### Configure Real-time Backup in Seafile

On the primary server, add following options to seafile.conf:

```
[backup]
backup_url = http://backup-server
sync_token = c7a78c0210c2470e14a20a8244562ab8ad509734
```

On the backup server, add following options to seafile.conf:

```
[backup]
primary_url = http://primary-server
sync_token = c7a78c0210c2470e14a20a8244562ab8ad509734
sync_poll_interval = 3
```

- `backup_url`: the backup server's address in url format. You can use http or https.
- `primary_url`: the primary server's address in url format.
- `sync_token`: a secret that shared between the primary and backup server. It's 40 character SHA1 generated by the system admin. You can use `uuidgen | openssl sha1` command to generate a random token.
- `sync_poll_interval`: The backup server polls all libraries of the primary server periodically. You can set the poll interval in the unit of hours. The default interval is 1 hour, which mean the backup server will poll the primary every hour. You should choose larger intervals if you have large number of libraries.

After saving the configuration, restart seafile service on the primary and backup servers. The backup server will automatically start backup on restart.

### Setup Backup Server for Seafile Cluster

If your primary service runs as a Seafile cluster, you have two points to notice when setting up a backup server:

1. You should only use one MySQL instance as the replication master, if you're using MariaDB cluster.
2. You have to change seafile.conf and set the `backup_url` and `sync_token` options on each Seafile node. The configuration on all primary Seafile node should be the same. They all point to the same backup server.

Currently you cannot deploy the backup service **as** a cluster. That is, you can only use a single node as backup server. This support may be added in the future.

## Managing the Real-time Backup Server

Once set up, the backup server is a fully working Seafile instance. The admin can manage the backup server in two ways:

1. Access the server via Seahub web interface, just like a normal Seafile instance.
2. Use the `seaf-backup-cmd.sh` script in the server package to manage the backup function.

The `seaf-backup-cmd.sh` script provides the following commands:

### Checking Backup Status

`seaf-backup-cmd.sh` provides `status` command to view the backup status. The output is like:

```
# ./seaf-backup-cmd.sh status
Total number of libraries: xxx
Number of synchronized libraries: xxx
Number of libraries waiting for sync: xxx
Number of libraries syncing: xxx
Number of libraries failed to sync: xxx

List of syncing libraries:
xxx
xxx

List of libraries failed to sync:
xxx
xxx
```

There are a few reasons that may fail the backup of a library:

- Some data in the primary server is corrupted. The data may be in the latest state or in history. Since the backup procedure syncs the full history, corruption in history will fail the backup.
- The primary server has run seaf-fsck, which may restore a library back to an older state.

### Manually Trigger Syncing a Library

You can use the `sync` command to manually schedule backup of a library:

```
# ./seaf-backup-cmd.sh sync <library id>
```

The command will block until the backup is finished.

### Handling Backup Errors

The `--force` option of `sync` command can be used to force failing backup to complete. Permanent backup failures are usually caused by data corruption of a library in the primary server. The `--force` option asks the backup to skip corrupted objects and finish the backup.

When you find a backup error, follow two steps:

1. Run seaf-fsck on the primary server, for the failing libraries. Fsck fixes any corruption for the latest state of the libraries.
2. Run `seaf-backup-cmd.sh sync --force <library id>` on the backup server.

## Restore from the Backup Server

Since the backup server is a fully workable Seafile instance, you can switch your service to the backup server after your primary is severely damaged. But you need to take a few points into consideration before switching to the backup server.

- You should first try to repair the primary server as long as possible. Running seaf-fsck will fix most daily corruptions on the primary server.
- Even with the near real-time feature of the backup server, the data on the backup server may still be a bit older than the primary server. This is especially true for the libraries failed to backup.

Before switching to the backup server, you should first unsync all clients which is syncing with "failed to backup" libraries.

Supposed the output of `seaf-backup-cmd.sh status` is as follows:

```
List of libraries failed to sync:
f690ea2c-fe4d-459a-ba1e-165cdc6df391
e2df70b5-cd80-496f-98cf-c9f038cf1307
```

You run the following command within MySQL on the backup server:

```
use seafile-db;
delete from RepoUserToken where repo_id in ('f690ea2c-fe4d-459a-ba1e-165cdc6df391', 'e2df70b5-cd80-496f-98cf-c9f038cf1307');
```

