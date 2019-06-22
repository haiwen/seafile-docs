# Seafile.conf settings

**Note**: Since Seafile Server 5.0.0, all config files are moved to the central **conf** folder. [Read More](../deploy/new_directory_layout_5_0_0.md).

**Important**: Every entry in this configuration file is **case-sensitive**.

You need to restart seafile and seahub so that your changes take effect.

```
./seahub.sh restart
./seafile.sh restart
```

## Storage Quota Setting

You may set a default quota (e.g. 2GB) for all users. To do this, just add the following lines to `seafile.conf` file

```
[quota]
# default user quota in GB, integer only
default = 2
```

This setting applies to all users. If you want to set quota for a specific user, you may log in to seahub website as administrator, then set it in "System Admin" page.

## Default history length limit

If you don't want to keep all file revision history, you may set a default history length limit for all libraries.

```
[history]
keep_days = days of history to keep
```

## System Trash

Seafile uses a system trash, where deleted libraries will be moved to. In this way, accidentally deleted libraries can be recovered by system admin.
<pre>
[library_trash]
# How often trashed libraries are scanned for removal, default 1 day.
scan_days = xx

# How many days to keep trashed libraries, default 30 days.
expire_days = xx
</pre>

## Seafile fileserver configuration

The configuration of seafile fileserver is in the `[fileserver]` section of the file `seafile.conf`

```
[fileserver]
# bind address for fileserver
# default to 0.0.0.0, if deployed without proxy: no access restriction
# set to 127.0.0.1, if used with local proxy: only access by local
host = 127.0.0.1
# tcp port for fileserver
port = 8082
```

Since Community Edition 6.2 and Pro Edition 6.1.9, you can set the number of worker threads to server http requests. Default value is 10, which is a good value for most use cases.

```
[fileserver]
worker_threads = 15
```

Change upload/download settings.

```
[fileserver]
# Set maximum upload file size to 200M.
max_upload_size=200

# Set maximum download directory size to 200M.
max_download_dir_size=200
```

After a file is uploaded via the web interface, or the cloud file browser in the client, it needs to be divided into fixed size blocks and stored into storage backend. We call this procedure "indexing". By default, the file server uses 1 thread to sequentially index the file and store the blocks one by one. This is suitable for most cases. But if you're using S3/Ceph/Swift backends, you may have more bandwidth in the storage backend for storing multiple blocks in parallel. We provide an option to define the number of concurrent threads in indexing:

```
[fileserver]
max_indexing_threads = 10
```

When users upload files in the web interface (seahub), file server divides the file into fixed size blocks. Default blocks size for web uploaded files is 1MB. The block size can be set here.

```
[fileserver]
#Set block size to 2MB
fixed_block_size=2
```

When users upload files in the web interafece, file server assigns an token to authorize the upload operation. This token is valid for 1 hour by default. When uploading a large file via WAN, the upload time can be longer than 1 hour. You can change the token expire time to a larger value.

```
[fileserver]
#Set uploading time limit to 3600s
web_token_expire_time=3600
```

You can download a folder as a zip archive from seahub, but some zip software
on windows doesn't support UTF-8, in which case you can use the "windows_encoding"
settings to solve it.

```
[zip]
# The file name encoding of the downloaded zip file.
windows_encoding = iso-8859-1
```

## Database configuration

The whole database configuration is stored in the `[database]` section of the configuration file, whether you use SQLite, MySQL or PostgreSQL.

```
[database]
type=mysql
host=127.0.0.1
user=root
password=root
db_name=seafile_db
connection_charset=utf8
max_connections=100
```

When you configure seafile server to use MySQL, the default connection pool size is 100, which should be enough for most use cases.

## Change File Lock Auto Expire time (Pro edition only)

The Seafile Pro server auto expires file locks after some time, to prevent a locked file being locked for too long. The expire time can be tune in seafile.conf file.

```
[file_lock]
default_expire_hours = 6
```

The default is 12 hours.

## Enabled Slow Log

Since Seafile-pro-6.3.10, you can enable seaf-server's RPC slow log to do performance analysis.The slow log is enabled by default.

If you want to configure related options, add the options to seafile.conf:

```
[slow_log]
# default to true
enable_slow_log = true
# the unit of all slow log thresholds is millisecond.
# default to 5000 milliseconds, only RPC queries processed for longer than 5000 milliseconds will be  logged.
rpc_slow_threshold = 5000
```

You can find `seafile_slow_rpc.log` in `logs/slow_logs`. You can also use [log-rotate](../deploy/using_logrotate.md) to rotate the log files. You just need to send `SIGUSR2` to `seaf-server` process. The slow log file will be closed and reopened.
