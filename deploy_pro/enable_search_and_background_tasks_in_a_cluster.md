# Enable search and background tasks in a cluster

In the seafile cluster, only one server should run the background tasks, including:

- indexing files for search
- email notification
- office documents converts service


You need to choose one node to run the background tasks.

Let's assume you have three nodes in your cluster: A, B, and C. And you decide that:

* Node A would run background tasks.
* Node B and C would be normal nodes.

![cluster-nodes](../images/cluster-nodes.png)


## Configuring Node A (the background-tasks node)

On this node, you need:

### Install Java and LibreOffice

On Ubuntu/Debian:
```
sudo apt-get install openjdk-7-jre libreoffice python-uno # or python3-uno for ubuntu 14.04+
```

On CentOS/Red Hat:
```
sudo yum install java-1.7.0-openjdk
sudo yum install libreoffice libreoffice-headless libreoffice-pyuno
```

*Note*: Since version 3.1.12, java 1.7 is required, please check your java version by `java -version`. If not, please [change the default java version](./change_default_java.md).


Edit **pro-data/seafevents.conf** and ensure this line does NOT exist:

```
external_es_server = true
```

Edit **seahub_settings.py** and add a line:

```
OFFICE_CONVERTOR_NODE = True
```

### Edit the firewall rules

In your firewall rules for node A, you should open the port 9500 (for search requests).

## Configure Other Nodes

On nodes B and C, you need to:

* Edit pro-data/seafevents.conf, add the following lines:
```
[INDEX FILES]
external_es_server = true
es_host = <ip of node A>
es_port = 9500
```

Edit **seahub_settings.py** and add a line:

```
OFFICE_CONVERTOR_ROOT = http://<ip of node A>
```

## Start the background tasks

On node A (the background tasks node), you can star/stop background tasks by:

```
./seafile-background-tasks.sh { start | stop | restart }
```
