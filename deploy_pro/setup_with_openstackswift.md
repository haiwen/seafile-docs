# Setup With OpenStackSwift

**Note**: Since Seafile Server 5.0.0, all config files are moved to the central **conf** folder. [Read More](../deploy/new_directory_layout_5_0_0.md).

Note: This documentation is obsolete. Please refer to [the new documentation about how to use Swift](setup_with_swift.md).

Starting from professional server 2.0.5, Seafile can use S3-compatible cloud storage (such as OpenStack/Swift) as backend. This document will use Swift as example.

## Seafile Server Preparation

To setup Seafile Professional Server with OpenStack Swift:

- Setup the basic Seafile Professional Server following the guide on [Download and Setup Seafile Professional Server](download_and_setup_seafile_professional_server.md)
- Install the python `boto` library. It's needed to access Swift.
```
sudo easy_install boto
```

For best performance, Seafile requires install memcached and enable memcache for objects. 

We recommend to allocate 128MB memory for memcached. Edit /etc/memcached.conf

```
# Start with a cap of 64 megs of memory. It's reasonable, and the daemon default
# Note that the daemon will grow to this size, but does not start out holding this much
# memory
# -m 64
-m 128
```

## Swift Preparation

In a production environment, you'll configure Swift with S3 middleware and use Keystone for authentication. The following instructions assumes you've already setup Swift with Keystone authentication. We'll focus on the change you need to make Swift work with S3 middleware.

### Install Swift3

This middleware implements S3 API for Swift.

```
git clone https://github.com/fujita/swift3.git
cd swift3
sudo python setup.py install
```

### Install keystonmiddleware

This middleware contains the `s3token` filter for authentication between S3 API and Keystone. If you've configured Swift to work with Keystone, you should have this middleware installed already.

```
git clone https://github.com/openstack/keystonemiddleware.git
cd keystonmiddleware
sudo pip install -r requirements.txt
sudo python setup.py install
```

### Modify proxy-server.conf for Swift

On Ubuntu, the config file is `/etc/swift/proxy-server.conf`.

First check whether you've replaced `tempauth` with `authtoken keystoneauth` in the main pipeline. This should have been done if you configured Swift to work with Keystone.

Add `swift3 s3token` to `[pipeline:main]`:

```
[pipeline:main]
pipeline = [...] swift3 s3token authtoken keystoneauth proxy-server
```

Add filters:

```
[filter:swift3]  
use = egg:swift3#swift3

[filter:s3token]  
paste.filter_factory = keystonemiddleware.s3_token:filter_factory  
auth_port = 35357  
auth_host = [keystone-ip]  
auth_protocol = http  
```

### Restart Swift

```
swift-init proxy restart
```

### Accessing Swift via S3 API

To access it via S3 API, you'll need AWS-like access key id and secret access key. Generate it with the following command for your specific tenant and user (You should change the tenant-id and user-id):

```
keystone ec2-credentials-create --tenant-id=d6fdc8460c7b46d0ad24aa23667b85c3 --user-id=b66742a744eb4fc98abd945781bf969d
```

After successfully setup S3 middleware, you should be able to access it with any S3 clients. The next thing you need to do is to create buckets for Seafile. With Python boto library you can do as follows (replace `key_id` and `secret_key` with your own):

```
import boto
import boto.s3.connection

connection = boto.connect_s3(
    aws_access_key_id='<key_id>',
    aws_secret_access_key='<secret_key>',
    port=8080,
    host='swift-proxy-server-address',
    is_secure=False,
    calling_format=boto.s3.connection.OrdinaryCallingFormat())
connection.create_bucket('seafile-commits')
connection.create_bucket('seafile-fs')
connection.create_bucket('seafile-blocks')
```

Each S3 bucket maps to a container in Swift. So you can use native Swift command line to check the containers. For example:

```
swift -V 2 -A http://[keystone_ip]:5000/v2.0 -U [tenant]:[user] -K [pas] list
```

## Modify seafile.conf

Append the following lines to `seafile.conf` (replace `key_id` and `secret_key` with your own)

```
[block_backend]
name = s3
bucket = seafile-blocks
key_id = <key_id>
key = <secret_key>
host = <swift-proxy-server-address>:8080
path_style_request = true
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100

[commit_object_backend]
name = s3
bucket = seafile-commits
key_id = <key_id>
key = <secret_key>
host = <swift-proxy-server-address>:8080
path_style_request = true
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100

[fs_object_backend]
name = s3
bucket = seafile-fs
key_id = <key_id>
key = <secret_key>
host = <swift-proxy-server-address>:8080
path_style_request = true
memcached_options = --SERVER=localhost --POOL-MIN=10 --POOL-MAX=100
```

### Using memcached cluster

In a cluster environment, you may want to use a memcached cluster. In the above configuration, you have to specify all the memcached server node addresses in seafile.conf

```
memcached_options = --SERVER=192.168.1.134 --SERVER=192.168.1.135 --SERVER=192.168.1.136 --POOL-MIN=10 --POOL-MAX=100
```

## Run and Test ##

Now you can start Seafile by `./seafile.sh start` and `./seahub.sh start` and visit the website.
