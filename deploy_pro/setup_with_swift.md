# Setup With OpenStack Swift

**Note**: Since Seafile Server 5.0.0, all config files are moved to the central **conf** folder. [Read More](../deploy/new_directory_layout_5_0_0.md).

Seafile supports OpenStack Swift as storage backend since 5.1.0. This backend uses the native Swift API. Previously users can only use the S3-compatibility layer of Swift. That way is obsolete now. The old documentation is still available [here](setup_with_openstackswift.md).

## Prepare

To setup Seafile Professional Server with Swift:

- Setup the basic Seafile Professional Server following the guide on [Download and setup Seafile Professional Server](download_and_setup_seafile_professional_server.md)
- Install and configure memcached. For best performance, Seafile requires install memcached and enable memcache for objects. We recommend to allocate 128MB memory for memcached. Edit /etc/memcached.conf

```
# Start with a cap of 64 megs of memory. It's reasonable, and the daemon default
# Note that the daemon will grow to this size, but does not start out holding this much
# memory
# -m 64
-m 128
```

## Modify Seafile.conf

Edit `seafile.conf`, add the following lines:

```
[block_backend]
name = swift
tenant = yourTenant
user_name = user
password = secret
container = seafile-blocks
auth_host = 192.168.56.31:5000
auth_ver = v2.0
memcached_options = --SERVER=192.168.1.134:11211 --POOL-MIN=10 --POOL-MAX=100

[commit_object_backend]
name = swift
tenant = yourTenant
user_name = user
password = secret
container = seafile-commits
auth_host = 192.168.56.31:5000
auth_ver = v2.0
memcached_options = --SERVER=192.168.1.134:11211 --POOL-MIN=10 --POOL-MAX=100

[fs_object_backend]
name = swift
tenant = yourTenant
user_name = user
password = secret
container = seafile-fs
auth_host = 192.168.56.31:5000
auth_ver = v2.0
memcached_options = --SERVER=192.168.1.134:11211 --POOL-MIN=10 --POOL-MAX=100
```

The above config is just an example. You should replace the options according to your own environment.

Seafile only supports Swift with Keystone as authentication mechanism. Currently only the v2.0 auth protocol is supported. The `auth_host` option is the address and port of Keystone service.

It's recommended to create separate containers for commit, fs, and block objects.

### Using memcached cluster

In a cluster environment, you may want to use a memcached cluster. In the above configuration, you have to specify all the memcached server node addresses in seafile.conf

```
memcached_options = --SERVER=192.168.1.134 --SERVER=192.168.1.135 --SERVER=192.168.1.136 --POOL-MIN=10 --POOL-MAX=100
```

### Use HTTPS connections to Swift

Since Pro 5.0.4, you can use HTTPS connections to Swift. Add the following options to seafile.conf:

```
[commit_object_backend]
name = swift
......
use_https = true

[fs_object_backend]
name = swift
......
use_https = true

[block_backend]
name = swift
......
use_https = true
```

Because the server package is built on CentOS 6, if you're using Debian/Ubuntu, you have to copy the system CA bundle to CentOS's CA bundle path. Otherwise Seafile can't find the CA bundle so that the SSL connection will fail.

```
sudo mkdir -p /etc/pki/tls/certs
sudo cp /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt
sudo ln -s /etc/pki/tls/certs/ca-bundle.crt /etc/pki/tls/cert.pem
```

## Run and Test ##

Now you can start Seafile by `./seafile.sh start` and `./seahub.sh start` and visit the website.
