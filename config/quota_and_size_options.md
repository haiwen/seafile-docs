# Quota and other options

**Note**: Since Seafile Server 5.0.0, all config files are moved to the central **conf** folder. [Read More](../deploy/new_directory_layout_5_0_0.md).

#### Quota

You may set a default quota (e.g. 2GB) for all users. To do this, just add the following lines to [seafile.conf](../config/seafile-conf.md) file

<pre>
[quota]
# default user quota in GB, integer only
default = 2
</pre>

After Community Edition 5.0.5, you can also set the default quota in KB, MB, GB or TB. For example,

```
[quota]
default = 200MB
```

Note that 1TB = 1000GB = 1000*1000MB and so forth.

This setting applies to all users. If you want to set quota for a specific user, you may log in to seahub website as administrator, then set it in "System Admin" page.

#### Default history length limit (seafile.conf)

If you don't want to keep all file revision history, you may set a default history length limit for all libraries. In `seafile.conf`:

<pre>
[history]
keep_days = days of history to keep
</pre>


#### Change upload/download size limit.

In `seafile.conf`:

<pre>
[fileserver]
# Set maximum upload file size to 200M.
max_upload_size=200

# Set maximum download directory size to 200M.
max_download_dir_size=200
</pre>
