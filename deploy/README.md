# Deploying Seafile under Linux

Here we describe how to deploy Seafile from prebuild binary packages.

### Deploy Seafile in Home/Personal Environment

* [Deploying Seafile with SQLite](using_sqlite.md)

### Deploy Seafile in Production/Enterprise Environment

In production environment we recommend using MySQL as the database and config Seafile web behing Nginx or Apache. For those who are not familiar with Nginx and Apache. We recommend Nginx, since it is easier to config than Apache.

Note: We have prepared an installation script [Deploy Seafile with an installation script](https://github.com/haiwen/seafile-server-installer). The installer offer a quick and easy way to set up a production ready Seafile Server using MariaDB, Memcached and NGINX as a reverse proxy in under 5 minutes.

You can also install Seafile manually without the installation script as following:

Basic:

* [Deploying Seafile with MySQL](using_mysql.md)
* [Config Seahub with Nginx](deploy_with_nginx.md)
* [Enabling Https with Nginx](https_with_nginx.md)
* [Config Seahub with Apache](deploy_with_apache.md)
* [Enabling Https with Apache](https_with_apache.md)

Advanced:

* [Add Memcached](add_memcached.md), adding memcached is very important if you have more than 50 users.
* [Start Seafile at System Bootup](start_seafile_at_system_bootup.md)
* [Firewall settings](using_firewall.md)
* [Logrotate](using_logrotate.md)

User Authentication:

Seafile supports a few external user authentication methods.

* [Configure Seafile to use LDAP](using_ldap.md)
* [Shibboleth Authentication](shibboleth_config.md)
* [Kerberos Authentication](kerberos_config.md)

Other Deployment Issues

* [Deploy Seafile behind NAT](deploy_seafile_behind_nat.md)
* [Deploy Seahub at Non-root domain](deploy_seahub_at_non-root_domain.md)
* [Migrate From SQLite to MySQL](migrate_from_sqlite_to_mysql.md)

Check [configuration options](../config/README.md) for server config options like enabling user registration.

**Read here** if you have troubles setting up Seafile server

1. Read [Seafile Server Components Overview](../overview/components.md) to understand how Seafile server works. This will save you a lot of time.
2. [Common Problems for Setting up Server](common_problems_for_setting_up_server.md)
3. Go to our [forum](https://forum.seafile.com/) for help.

## Upgrade Seafile Server

* [Upgrade Seafile server](upgrade.md)

## For those that want to package Seafile server

If you want to package seafile yourself, (e.g. for your favorite Linux distribution), you should always use the correspondent tags:

* When we release a new version of seafile client, say 3.0.1, we will add tags `v3.0.1` to ccnet, seafile and seafile-client.
* Likewise, when we release a new version of seafile server, say 3.0.1, we will add tags `v3.0.1-server` to ccnet, seafile and seahub.
* For libsearpc, we always use tag `v3.0-latest`.

**Note**: The version numbers of each project has nothing to do with the tag name.
