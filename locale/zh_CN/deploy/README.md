# Linux 下部署 Seafile 服务器

此文档用来说明如何使用预编译安装包来部署 Seafile 服务器.

### 家庭/个人 环境下部署 Seafile 服务器

* [部署 Seafile 服务器（使用 SQLite）](using_sqlite.md)

### 生产/企业 环境下部署 Seafile 服务器

企业环境下我们建议使用 MySQL 数据库，并将 Seafile 部署在 Nginx 或者 Apache 上，如果对于 Nginx 和 Apache 都不是很熟悉的话，我们建议使用 Nginx，相对于 Apache 来说，Nginx 使用起来比较简单。

Note: We have prepared an installation script [Deploy Seafile with an installation script](https://forum.seafile-server.org/t/seafile-server-installer-for-production-ready-seafile-ce-and-pro-installations/1464). The installer offer a quick and easy way to set up a production ready Seafile Server using MariaDB, Memcached and NGINX as a reverse proxy in under 5 minutes.

You can also install Seafile manually without the installation script as following:

基础功能:

* [部署 Seafile 服务器（使用 MySQL）](using_mysql.md)
* [Nginx 下配置 Seahub](deploy_with_nginx.md)
* [Nginx 下启用 Https](https_with_nginx.md)
* [Apache 下配置 Seahub](deploy_with_apache.md)
* [Apache 下启用 Https](https_with_apache.md)

高级功能:

* [Add Memcached](add_memcached.md), adding memcached is very important if you have more than 50 users.
* [开机启动 Seafile](start_seafile_at_system_bootup.md)
* [防火墙设置](using_firewall.md)
* [Logrotate 管理系统日志](using_logrotate.md)

User Authentication:

Seafile supports a few external user authentication methods.

* [Seafile LDAP 配置](using_ldap.md)
* [Shibboleth Authentication](shibboleth_config.md)

其他部署事项

* [使用 NAT](deploy_seafile_behind_nat.md)
* [非根域名下部署 Seahub](deploy_seahub_at_non-root_domain.md)
* [从 SQLite 迁移至 MySQL](migrate_from_sqlite_to_mysql.md)

更多配置选项（比如开启用户注册功能），请查看 [服务器个性化配置](../config/README.md)。

**注意** 如果在部署 Seafile 服务器时遇到困难

1. 阅读 [Seafile 组件](../overview/components.md) 以了解 Seafile 的运行原理。
2. [安装常见问题](common_problems_for_setting_up_server.md)。
3. Go to our [forum](https://forum.seafile-server.org/) for help.

## 升级 Seafile 服务器

* [升级](upgrade.md)

## For those that want to package Seafile server

If you want to package seafile yourself, (e.g. for your favorite Linux distribution), you should always use the correspondent tags:

* When we release a new version of seafile client, say 3.0.1, we will add tags `v3.0.1` to ccnet, seafile and seafile-client.
* Likewise, when we release a new version of seafile server, say 3.0.1, we will add tags `v3.0.1-server` to ccnet, seafile and seahub.
* For libsearpc, we always use tag `v3.0-latest`.

**Note**: The version numbers of each project has nothing to do with the tag name.

