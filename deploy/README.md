# Deploying Seafile under Linux

Here we describe how to deploy Seafile from prebuild binary packages.

## Deploy Seafile in Home/Personal Environment

* [Deploying Seafile with SQLite](using_sqlite.md)

## Deploy Seafile in Production/Enterprise Environment

In production environment we recommend using MySQL as the database and config Seafile web behing Nginx or Apache. For those who are not familiar with Nginx and Apache. We recommend Nginx, since it is easier to config than Apache.

We provide three ways to deploy Seafile services:

* Using [Docker](deploy_with_docker.md)
* Using [installation script](https://github.com/haiwen/seafile-server-installer)
* Manually installing Seafile and setting up database, memcached and Nginx/Apache. See the following section.

### Install Seafile manually

* [Deploying Seafile with MySQL](using_mysql.md)
* [Config Seahub with Nginx](deploy_with_nginx.md)
* [Enabling Https with Nginx](https_with_nginx.md)
* [Config Seahub with Apache](deploy_with_apache.md)
* [Enabling Https with Apache](https_with_apache.md)
* [Add Memcached](add_memcached.md), adding memcached is very important if you have more than 50 users.
* [Start Seafile at System Bootup](start_seafile_at_system_bootup.md)
* [Firewall settings](using_firewall.md)
* [Logrotate](using_logrotate.md)

### User Authentication

Seafile supports a few external user authentication methods.

* [Configure Seafile to use LDAP](using_ldap.md)
* [Shibboleth Authentication](shibboleth_config.md)
* [Kerberos Authentication](kerberos_config.md)

### Other Deployment Issues

* [Deploy Seafile behind NAT](deploy_seafile_behind_nat.md)
* [Deploy Seahub at Non-root domain](deploy_seahub_at_non-root_domain.md)
* [Migrate From SQLite to MySQL](migrate_from_sqlite_to_mysql.md)

Check [configuration options](../config/README.md) for server config options like enabling user registration.

### Trouble shooting

1. Read [Seafile Server Components Overview](../overview/components.md) to understand how Seafile server works. This will save you a lot of time.
2. [Common Problems for Setting up Server](common_problems_for_setting_up_server.md)
3. Go to our [forum](https://forum.seafile.com/) for help.

### Upgrade Seafile Server

* [Upgrade Seafile server](upgrade.md)
