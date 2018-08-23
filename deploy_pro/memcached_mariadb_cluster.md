# Setup Memcached Cluster and MariaDB Galera Cluster

For high availability, it is recommended to set up a memcached cluster and MariaDB Galera cluster for Seafile cluster. This documentation will provide information on how to do this with 3 servers. You can either use 3 dedicated servers or use the 3 Seafile server nodes.

## Setup Memcached Cluster

Seafile servers share session information within memcached. So when you set up a Seafile cluster, there needs to be a memcached server (cluster) running.

The simplest way is to use a single-node memcached server. But when this server fails, some functions in the web UI of Seafile cannot work. So for HA, it's usually desirable to have more than one memcached servers.

### For Seafile Server bofore 6.2.11 version

For Seafile servers before 6.2.11 version, we recommend to use an architecture in which the cache items are distributed across all memcached nodes.

Unlike other cluster architecture, when you create a memcached cluster with multiple nodes, the key distribution in memcached cluster is controlled by the memcached clients. So there is no special configuration on the memcached server for building a cluster. But there are a few things to take care when building a memcached cluster:

- Make sure all the seafile server nodes connects to all the memcached nodes. The memcached servers should be listed in the same order in Seafile's config files.
- After one memcached server gets shut down and restarted, sometimes the Seafile servers' views on the memcached cluster will become inconsistent. This is due to limitation of the memcached cluster architecture. You may notice some errors in the web UI functionalities. You have to restart the Seafile server processes to make their views consistent again. Typical error messages you can find in seafile.log are:
    * `SERVER HAS FAILED AND IS DISABLED UNTIL TIMED RETRY`
    * `SERVER IS MARKED DEAD`

Seafile servers, work as memcached clients, are designed to automatically migrate keys to living memcached nodes when a memcached node fails. But there are some tricky cases when the Seafile servers cannot automatically recover from errors of memcahced servers. That's why we change the recommended architecture since 6.3 version.

### Seafile server 6.2.11 or newer

In this new recommended architecture, you setup two independent memcached servers, in active/standby mode. A floating IP address (or Virtual IP address in some context) is assigned to the current active node. When the active node goes down, Keepalived will migrate the virtual IP to the standby node. So you actually use a single node memcahced, but use Keepalived (or other alternatives) to provide high availability.

After installing memcahced on each server, you need to make some modification to the memcached config file.

```
# Under Ubuntu
vi /etc/memcached.conf

# Start with a cap of 64 megs of memory. It's reasonable, and the daemon default
# Note that the daemon will grow to this size, but does not start out holding this much
# memory
# -m 64
-m 256

# Specify which IP address to listen on. The default is to listen on all IP addresses
# This parameter is one of the only security measures that memcached has, so make sure
# it's listening on a firewalled interface.
-l 0.0.0.0

service memcached restart
```

```
# Under CentOS 7
vim /etc/sysconfig/memcached

PORT="11211"
USER="memcached"
MAXCONN="1024"
CACHESIZE="64"
OPTIONS="-l 0.0.0.0 -m 256"

systemctl restart memcached
systemctl enable memcached
```

**NOTE: Please configure memcached to start on system startup.**

Install and configure Keepalived.

```
# For Ubuntu
sudo apt-get install keepalived -y

# For CentOS
sudo yum install keepalived -y
```

Modify keepalived config file `/etc/keepalived/keepalived.conf`.

On active node
```
cat /etc/keepalived/keepalived.conf

! Configuration File for keepalived

global_defs {
    notification_email {
        root@localhost
    }
    notification_email_from keepalived@localhost
    smtp_server 127.0.0.1
    smtp_connect_timeout 30
    router_id node1
    vrrp_mcast_group4 224.0.100.19
}
vrrp_script chk_memcached {
    script "killall -0 memcached && exit 0 || exit 1"
    interval 1
    weight -5
}

vrrp_instance VI_1 {
    state MASTER
    interface ens33
    virtual_router_id 51
    priority 100
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass hello123
    }
    virtual_ipaddress {
        192.168.1.113/24 dev ens33
    }
    track_script {
	chk_memcached
    }
}
```

On standby node
```
cat /etc/keepalived/keepalived.conf

! Configuration File for keepalived

global_defs {
    notification_email {
        root@localhost
    }
    notification_email_from keepalived@localhost
    smtp_server 127.0.0.1
    smtp_connect_timeout 30
    router_id node2
    vrrp_mcast_group4 224.0.100.19
}
vrrp_script chk_memcached {
    script "killall -0 memcached && exit 0 || exit 1"
    interval 1
    weight -5
}

vrrp_instance VI_1 {
    state BACKUP
    interface ens33
    virtual_router_id 51
    priority 98
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass hello123
    }
    virtual_ipaddress {
        192.168.1.113/24 dev ens33
    }
    track_script {
        chk_memcached
    }
}
```

**NOTE: Please adjust the network device names accordingly. virtual_ipaddress is the floating IP address in use.**

### Setup MariaDB Cluster

MariaDB cluster helps you to remove single point of failure from the cluster architecture. Every update in the database cluster is synchronously replicated to all instances.

You can choose between two different setups:

- For a small cluster with 3 nodes, you can run MariaDB cluster directly on the Seafile server nodes. Each Seafile server access its local instance of MariaDB.
- For larger clusters, it's preferable to have 3 dedicated MariaDB nodes to form a cluster. You have to set up a HAProxy in front of the MariaDB cluster. Seafile will access database via HAProxy.

We refer to the documentation from MariaDB team:

- [Setting up MariaDB cluster on CentOS 7](https://mariadb.com/resources/blog/setting-mariadb-enterprise-cluster-part-2-how-set-mariadb-cluster)
- [Setting up HAProxy for MariaDB Galera Cluster](https://mariadb.com/resources/blog/setup-mariadb-enterprise-cluster-part-3-setup-ha-proxy-load-balancer-read-and-write-pools). Note that Seafile doesn't use read/write isolation techniques. So you don't need to setup read and write pools.
