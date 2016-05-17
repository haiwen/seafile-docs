# Seafile

## Upgrade Manual

This page is for users who use the pre-compiled seafile server package.

- If you [build seafile server from source](../build_seafile/server.md), please read the **Upgrading Seafile Server** section on that page, instead of this one.
- After upgrading, you may need to clean [seahub cache](add_memcached.md) if it doesn't behave as expect.

If you are running a **cluster**, please read [upgrade a Seafile cluster](../deploy_pro/upgrade_a_cluster.md).

## Major version upgrade (like from 2.x to 3.y)


Suppose you are using version 2.1.0 and like to upgrade to version 3.1.0. First download and extract the new version. You should have a directory layout similar to this:


<pre>
haiwen
   -- seafile-server-2.1.0
   -- seafile-server-3.1.0
   -- ccnet
   -- seafile-data
</pre>


升级到 3.1.0：

1. 关闭 Seafile 服务（如果正在运行）：

   ```sh
   cd haiwen/seafile-server-2.1.0
   ./seahub.sh stop
   ./seafile.sh stop
   ```
2. 查看 seafile-server-3.1.0 目录下的升级脚本：

   ```sh
   cd haiwen/seafile-server-3.1.0
   ls upgrade/upgrade_*
   ```

   可以看到升级脚本文件如下:

   ```
   ...
   upgrade/upgrade_2.0_2.1.sh
   upgrade/upgrade_2.1_2.2.sh
   upgrade/upgrade_2.2_3.0.sh
   upgrade/upgrade_3.0_3.1.sh
   ```

3. Start from you current version, run the script one by one

   ```
   upgrade/upgrade_2.1_2.2.sh
   upgrade/upgrade_2.2_3.0.sh
   upgrade/upgrade_3.0_3.1.sh
   ```

4. 启动新版本 Seafile 服务器，完成升级：

   ```sh
   cd haiwen/seafile-server-3.1.0/
   ./seafile.sh start
   ./seahub.sh start # or "./seahub.sh start-fastcgi" if you're using fastcgi
   ```

## Minor version upgrade (like from 3.0.x to 3.2.y)

假设你现在使用 3.0.0 版本，想要升级到 3.2.2 版本，下载、解压新版本安装包，得到目录结构如下：


<pre>
haiwen
   -- seafile-server-3.0.0
   -- seafile-server-3.2.2
   -- ccnet
   -- seafile-data
</pre>


升级到 3.2.2：

1. 关闭 Seafile 服务（如果正在运行）：

   ```sh
   cd haiwen/seafile-server-3.0.0
   ./seahub.sh stop
   ./seafile.sh stop
   ```
2. Check the upgrade scripts in seafile-server-3.2.2 directory.

   ```sh
   cd haiwen/seafile-server-3.2.2
   ls upgrade/upgrade_*
   ```

   可以看到升级脚本文件如下:

   ```
   ...
   upgrade/upgrade_2.2_3.0.sh
   upgrade/upgrade_3.0_3.1.sh
   upgrade/upgrade_3.1_3.2.sh
   ```

3. Start from you current version, run the script one by one

   ```
   upgrade/upgrade_3.0_3.1.sh
   upgrade/upgrade_3.1_3.2.sh
   ```

4. 启动新版本 Seafile 服务器，完成升级：

   ```sh
   cd haiwen/seafile-server-3.2.2/
   ./seafile.sh start
   ./seahub.sh start
   ```


## 维护版本升级 (比如从 3.1.0 升级到 3.1.2)

类似从 3.1.0 升级到 3.1.2，为维护版本升级。


1. 关闭 Seafile 服务（如果正在运行）
2. 对于此类升级，只需更新头像链接，直接运行升级脚本即可(因为历史原因，此升级脚本命名为 `minor-upgrade.sh`):

   ```sh
   cd seafile-server-3.1.2
   upgrade/minor-upgrade.sh
   ```

3. 运行升级脚本之后，启动新版本 Seafile 服务器，完成升级

4. If the new version works fine, the old version can be removed

   ```sh
   rm -rf seafile-server-3.1.0
   ```

