# Seafile.conf settings

**Note**: Seafile 服务器 5.0.0 之后，所有配置文件都移动到了统一的 **conf** 目录下。 [了解详情](../deploy/new_directory_layout_5_0_0.md).

## 文件修改历史保存期限 (seafile.conf)

You may set a default quota (e.g. 2GB) for all users. To do this, just add the following lines to `seafile.conf` file

<pre>
[quota]
# 用户存储容量，单位默认为 GB，要求为整数。
default = 2
</pre>

此设置对所有用户有效，如果想为某一用户单独设置，请在管理员界面更改。

## Default history length limit (seafile.conf)

If you don't want to keep all file revision history, you may set a default history length limit for all libraries.

<pre>
[history]
# 文件修改历史保存期限（单位为“天”）
keep_days = 10
</pre>
## Seafile fileserver configuration (seafile.conf)

The configuration of seafile fileserver is in the <code>[fileserver]</code> section of the file `seafile.conf`

<pre>
[fileserver]
# bind address for fileserver, default to 0.0.0.0
host = 0.0.0.0
# tcp port for fileserver
port = 8082
</pre>

Change upload/download settings.

<pre>
[fileserver]
# 设置最大上传文件为 200M.
max_upload_size=200

# 设置最大下载文件/目录为 200M.
max_download_dir_size=200
</pre>

After a file is uploaded via the web interface, or the cloud file browser in the client, it needs to be divided into fixed size blocks and stored into storage backend. We call this procedure "indexing". By default, the file server uses 1 thread to sequentially index the file and store the blocks one by one. This is suitable for most cases. But if you're using S3/Ceph/Swift backends, you may have more bandwidth in the storage backend for storing multiple blocks in parallel. We provide an option to define the number of concurrent threads in indexing:

```
[fileserver]
max_indexing_threads = 10
```

You can download a folder as a zip archive from seahub, but some zip software on windows doesn't support UTF-8, in which case you can use the "windows_encoding" settings to solve it.
<pre>
[zip]
# The file name encoding of the downloaded zip file.
windows_encoding = iso-8859-1
</pre>

## Changing MySQL Connection Pool Size

When you configure seafile server to use MySQL, the default connection pool size is 100, which should be enough for most use cases. You can change this value by adding following options to seafile.conf:

```
[database]
......
# Use larger connection pool
max_connections = 200
```

**Note**: You need to restart seafile and seahub so that your changes take effect.
<pre>
./seahub.sh restart
./seafile.sh restart
</pre>

