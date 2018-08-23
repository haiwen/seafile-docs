*Note:* Before you try to deploy file search office documents preview, make sure other parts of your seafile cluster are already working, e.g upload/download files in a web browser. Make sure memcached is configured as described in ["Deploy in a cluster"](./deploy_in_a_cluster.md).

# Enable search and background tasks in a cluster

In the seafile cluster, only one server should run the background tasks, including:

- indexing files for search
- email notification
- office documents converts service
- LDAP sync
- virus scan

Let's assume you have three nodes in your cluster: A, B, and C.

* Node A is backend node that run background tasks.
* Node B and C are frontend nodes that serving requests from clients.

![cluster-nodes](../images/cluster-nodes.png)


## Configuring Node A (the backend node)

If you following the steps on settings up a cluster, node B and node C should have already be configed as frontend node. You can copy the configuration of node B as a base for node A. Then do the following steps:

### Install Dependencies (Java, LibreOffice, poppler)

On Ubuntu/Debian:
```shell
sudo apt-get install openjdk-7-jre libreoffice poppler-utils python-uno # or python3-uno for ubuntu 14.04+
```

On CentOS/Red Hat:
```shell
sudo yum install java-1.7.0-openjdk
sudo yum install libreoffice libreoffice-headless libreoffice-pyuno
sudo yum install poppler-utils
```


Edit **seafevents.conf** and ensure this line does NOT exist:

```
external_es_server = true
```

Edit **seahub_settings.py** and add a line:

```python
OFFICE_CONVERTOR_NODE = True
```

Edit **seafile.conf** to enable virus scan according to [virus scan document](virus_scan.md)


### Edit the firewall rules

In your firewall rules for node A, you should open the port 9200 (for search requests). For versions older than 6.1, `es_port` was 9500.

## Configure Other Nodes

On nodes B and C, you need to:

* Edit `seafevents.conf`, add the following lines:
```
[INDEX FILES]
external_es_server = true
es_host = <ip of node A>
es_port = 9200
```

Edit **seahub_settings.py** and add a line:

```python
OFFICE_CONVERTOR_ROOT = 'http://<ip of node A>'
```

Make sure requests to http://<ip of node A> is also handled by Seahub. For example, you may need to add this Nginx configuration in the background node:

```
server {
    listen 80;
    server_name <IP of node A>;
    location / {
        proxy_pass         http://127.0.0.1:8000;
        ...
  }
```

As a simple test, you can use this command to test if you set it up correctly.

```shell
curl -v http://<IP of node A>/office-convert/internal/status/
```

It should say "400 Bad Request" when you have Nginx config updated.


## Start the background node

Type the following commands to start the background node (Note, one additional command `seafile-background-tasks.sh` is needed)

```shell
./seafile.sh start
./seahub.sh start # or "./seahub.sh start-fastcgi" if you're using fastcgi
./seafile-background-tasks.sh start
```

To stop the background node, type:

```shell
./seafile-background-tasks.sh stop
./seafile.sh stop
./seahub.sh stop
```

You should also configure Seafile background tasks to start on system bootup. For systemd based OS, you can add `/etc/systemd/system/seafile-background-tasks.service`:

```
[Unit]
Description=Seafile Background Tasks Server
After=network.target seahub.service

[Service]
Type=forking
ExecStart=/opt/seafile/seafile-server-latest/seafile-background-tasks.sh start
ExecStop=/opt/seafile/seafile-server-latest/seafile-background-tasks.sh stop
User=root
Group=root

[Install]
WantedBy=multi-user.target
```

Then enable this task in systemd:

```
systemctl enable seafile-background-tasks.service
```

## The final configuration of the background node

Here is the summary of configurations at the background node that related to clustering setup.

For **seafile.conf**:

```
[cluster]
enabled = true
memcached_options = --SERVER=<IP of memcached node> --POOL-MIN=10 --POOL-MAX=100
```

For **seahub_settings.py**:

```
OFFICE_CONVERTOR_NODE = True

AVATAR_FILE_STORAGE = 'seahub.base.database_storage.DatabaseStorage'
COMPRESS_CACHE_BACKEND = 'django.core.cache.backends.locmem.LocMemCache'
```

For **seafevents.conf**:

```
[INDEX FILES]
enabled = true
interval = 10m

[OFFICE CONVERTER]
enabled = true
workers = 1
## how many pages are allowed to be previewed online. Default is 50 pages
max-pages = 50
## the max size of documents allowed to be previewed online, in MB. Default is 10 MB
## Previewing a large file (for example >30M) online is likely going to freeze the browser.
max-size = 10
```
