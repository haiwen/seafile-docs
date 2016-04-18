# Seafile Clustering with MariaDB and Ceph

In this document we describe the detailed solution of deploying a high scalable Seafile cluster with MariaDB and Ceph. The document is not a finished one. We will improve it continuously as our knowledge grow with several on going projects.

## Backgrounds

Seafile organizes files into libraries. Each library is a GIT repository like file system tree with each file and folder identified by a unique hash value. These unique IDs are used in the syncing algorithm and there is no need to storing syncing state for each file in the database. Tranditional database like MySQL are not scalable to tens of millions of records, while object storages like Ceph and Swift are highly scalable. So in theory, Seafile is capable to storing billions of files for syncing and sharing.

While files are saved into object storage, other information like sharing and permission has to be stored in database. MariaDB Galera can be used to provide a scalable and reliable database storage.

## Hardware and system requirement

In the minimum, we use three machines to setup the cluster. Each machine should be of

* 4 cores with 8GB or more memory.
* 1 SSD disk to storing Ceph journal.
* 1 SATA disk to storing the operating system
* 1 SATA disk to storing MariaDB database
* 4 or more SATA disk to store Ceph data

We use Ubuntu 14.04 server as the operating system. In the following, we denote the three server as node1, node2 and node3.

## Setup Ceph cluster

#### Preparation

Choose one node (say, node1) as admin node for installation. Install ceph-deploy on it.

* Add the release key:  

```
wget -q -O- 'https://ceph.com/git/?p=ceph.git;a=blob_plain;f=keys/release.asc' | sudo apt-key add -
```

* Add the Ceph packages to your repository. Replace {ceph-stable-release} with a stable Ceph release (e.g., emperor, firefly, giant etc.). The latest stable release is 'giant'.

```
echo deb http://ceph.com/debian-{ceph-stable-release}/ $(lsb_release -sc) main | sudo tee /etc/apt/sources.list.d/ceph.list
```

* Update your repository and install ceph-deploy:  

```
sudo apt-get update && sudo apt-get install ceph-deploy
```

Install ntp on all nodes, and restart ntp  

    sudo apt-get install ntp
    sudo service ntp restart

Install openssh on all nodes

    sudo apt-get install openssh-server

We'll use a non-root user for installation. Make sure this user has password-less sudo privileges.

    echo "{username} ALL = (root) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/{username}
    sudo chmod 0440 /etc/sudoers.d/{username}

Generate ssh public key for the installation user on node1. Then copy that public key to other nodes `~/.ssh/authorized_keys`.

#### Create Ceph Cluster

Create a `ceph-cluster` directory on node1 for storing the generated config files. All commands should be run under this directory.

Install Ceph on all nodes

    ceph-deploy install node1 node2 node3

Create the cluster  

    ceph-deploy new node1 node2 node3

Create Ceph monitors. You should open port 6789 on all nodes.

    ceph-deploy mon create node1 node2 node3 

Gather keys

    ceph-deploy gatherkeys node1

#### Add OSDs

In Ceph, every OSD daemon manages one disk. The OSDs can share one SSD disk for journal.
Suppose the SSD disk for journal is `/dev/sdb` and the SATA disks are `/dev/sdc`, `/dev/sdd`, etc. Add OSDs by the following commands:

    ceph-deploy osd create node1:/dev/sdc:/dev/sdb
    ceph-deploy osd create node2:/dev/sdc:/dev/sdb
    ceph-deploy osd create node3:/dev/sdc:/dev/sdb
    ceph-deploy osd create node1:/dev/sdd:/dev/sdb
    ceph-deploy osd create node2:/dev/sdd:/dev/sdb
    ceph-deploy osd create node3:/dev/sdd:/dev/sdb

**note** By default Ceph uses a journal partition of size 5GB. The creation of OSD will fail if your journal disk is too small. You can add the following config to /etc/ceph/ceph.conf:

```
[osd]
	# set journal size to 4GB
        osd journal size = 4000
```

#### Check Cluster Status

Ceph cluster setup is done. You can check cluster status by `sudo ceph -s`.

#### References

http://ceph.com/docs/master/rados/deployment/

## Setup MariaDB cluster

#### Install MariaDB and Galera

First, set apt source for MariaDB and Galera. Choose a repository for 5.5 in [this page](https://downloads.mariadb.org/mariadb/repositories).
Then you can install mariadb and galera.

    sudo apt-get install mariadb-galera-server galera
    sudo apt-get install rsync

#### Config MariaDB

In `/etc/mysql/conf.d/cluster.cnf`

    [mysqld]
     
    query_cache_size=0
    binlog_format=ROW
    default-storage-engine=innodb
    innodb_autoinc_lock_mode=2
    query_cache_type=0
    bind-address=0.0.0.0

    # Galera Provider Configuration
    wsrep_provider=/usr/lib/galera/libgalera_smm.so
    #wsrep_provider_options="gcache.size=32G"

    # Galera Cluster Configuration
    wsrep_cluster_name="test_cluster"
    wsrep_cluster_address="gcomm://first_ip,second_ip,third_ip

    # Galera Synchronization Congifuration
    wsrep_sst_method=rsync
    #wsrep_sst_auth=user:pass

    # Galera Node Configuration
    wsrep_node_address="this_node_ip"
    wsrep_node_name="this_node_name"

Here first_ip, second_ip and third_ip are corresponding to the IP address of node1, node2 and node3.

#### Change the data directory for MariaDB

We want to store the database data in a separate disk. Supposed the disk is mounted to the path `/mysql`.

Stop MariaDB using the following command:

    sudo /etc/init.d/mysql stop

Copy the existing data directory (default located in /var/lib/mysql) using the following command:

    sudo cp -R -p /var/lib/mysql/* /mysql

Edit /etc/mysql/my.cnf, update `datadir` option to `/mysql`.

Restart MariaDB with the command:

    sudo /etc/init.d/mysql restart

#### Start

Before staring the MariaDB cluster, make sure port 3456 and 4444 are open on all database nodes.

In node1:

    node1# sudo service mysql start --wsrep-new-cluster

In node2 and node3:

    node2# sudo service mysql start
    node3# sudo service mysql start

#### References

https://www.digitalocean.com/community/tutorials/how-to-configure-a-galera-cluster-with-mariadb-on-ubuntu-12-04-servers

## Setup Seafile cluster

Please follow http://manual.seafile.com/deploy_pro/setup_with_ceph.html to set seafile with Ceph and follow http://manual.seafile.com/deploy_pro/deploy_in_a_cluster.html for setup Seafile cluster.






