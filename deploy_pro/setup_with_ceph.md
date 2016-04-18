# Setup With Ceph

**Note**: Since Seafile Server 5.0.0, all config files are moved to the central **conf** folder. [Read More](../deploy/new_directory_layout_5_0_0.md).

Ceph is a scalable distributed storage system. Seafile can use Ceph's RADOS object storage layer for storage backend.

## Copy ceph conf file and client keyring

Seafile acts as a client to Ceph/RADOS, so it needs to access ceph cluster's conf file and keyring. You have to copy these files from a ceph admin node's /etc/ceph directory to the seafile machine.

```
seafile-machine# sudo scp user@ceph-admin-node:/etc/ceph/ /etc
```

## Install and enable memcached

For best performance, Seafile requires install memcached and enable memcache for objects. 

We recommend to allocate 128MB memory for memcached. Edit /etc/memcached.conf

```
# Start with a cap of 64 megs of memory. It's reasonable, and the daemon default
# Note that the daemon will grow to this size, but does not start out holding this much
# memory
# -m 64
-m 128
```

## Install Python Ceph Library

File search and WebDAV functions rely on Python Ceph library installed in the system.

On Debian/Ubuntu:

```
sudo apt-get install python-ceph
```

On RedHat/CentOS:

```
sudo yum install python-rados
```

## Edit seafile configuration

Edit `seafile.conf`, add the following lines:

```
[block_backend]
name = ceph
ceph_config = /etc/ceph/ceph.conf
pool = seafile-blocks
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100

[commit_object_backend]
name = ceph
ceph_config = /etc/ceph/ceph.conf
pool = seafile-commits
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100

[fs_object_backend]
name = ceph
ceph_config = /etc/ceph/ceph.conf
pool = seafile-fs
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100
```

It's recommended to create separate pools for commit, fs, and block objects.

```
ceph-admin-node# rados mkpool seafile-blocks
ceph-admin-node# rados mkpool seafile-commits
ceph-admin-node# rados mkpool seafile-fs
```

### Using memcached cluster

In a cluster environment, you may want to use a memcached cluster. In the above configuration, you have to specify all the memcached server node addresses in seafile.conf

```
memcached_options = --SERVER=192.168.1.134 --SERVER=192.168.1.135 --SERVER=192.168.1.136 --POOL-MIN=10 --POOL-MAX=100
```

## Use arbitary Ceph user

The above configuration will use the default (client.admin) user to connect to Ceph.
You may want to use some other Ceph user to connect. This is supported in Seafile.
To specify the Ceph user, you have to add a `ceph_client_id` option to seafile.conf, as the following:

```
[block_backend]
name = ceph
ceph_config = /etc/ceph/ceph.conf
# Sepcify Ceph user for Seafile here
ceph_client_id = seafile
pool = seafile-blocks
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100

[commit_object_backend]
name = ceph
ceph_config = /etc/ceph/ceph.conf
# Sepcify Ceph user for Seafile here
ceph_client_id = seafile
pool = seafile-commits
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100

[fs_object_backend]
name = ceph
ceph_config = /etc/ceph/ceph.conf
# Sepcify Ceph user for Seafile here
ceph_client_id = seafile
pool = seafile-fs
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100
```

You also have to add this user's keyring path to /etc/ceph/ceph.conf:

```
[client.seafile]
keyring = <path to user's keyring file>
```
