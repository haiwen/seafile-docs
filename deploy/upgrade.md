# Upgrade manual

This page is for users who use the pre-compiled seafile server package.
- If you [build seafile server from source](../build_seafile/server.md), please read the **Upgrading Seafile Server** section on that page, instead of this one.
- After upgrading, you may need to clean [seahub cache](add_memcached.md) if it doesn't behave as expect.
- If you are running a **cluster**, please read [upgrade a Seafile cluster](../deploy_pro/upgrade_a_cluster.md).

## Upgrade notes
Please check the [upgrade notes](upgrade_notes.md) for any special configuration or changes before/while upgrading.

--- 

## Major version upgrade (e.g. from 4.x.x to 5.y.y)


Suppose you are using version 4.3.0 and like to upgrade to version 5.0.0. First download and extract the new version. You should have a directory layout similar to this:

```
haiwen
   -- seafile-server-4.3.0
   -- seafile-server-5.0.0
   -- ccnet
   -- seafile-data
```


Now upgrade to version 5.0.0.

1. Shutdown Seafile server if it's running

   ```sh
   cd haiwen/seafile-server-4.3.0
   ./seahub.sh stop
   ./seafile.sh stop
   # or via service
   /etc/init.d/seafile-server stop
   ```
2. Check the upgrade scripts in seafile-server-5.0.0 directory.

   ```sh
   cd haiwen/seafile-server-5.0.0
   ls upgrade/upgrade_*
   ```

   You will get a list of upgrade files:

   ```
   ...
   upgrade/upgrade_4.0_4.1.sh
   upgrade/upgrade_4.1_4.2.sh
   upgrade/upgrade_4.2_4.3.sh
   upgrade/upgrade_4.3_4.4.sh
   upgrade/upgrade_4.4_5.0.sh
   ```

3. Start from your current version, run the script(s one by one)

   ```
   upgrade/upgrade_4.3_4.4.sh
   upgrade/upgrade_4.4_5.0.sh
   ```

4. Start Seafile server

   ```sh
   cd haiwen/seafile-server-5.0.0/
   ./seafile.sh start
   ./seahub.sh start # or "./seahub.sh start-fastcgi" if you're using fastcgi
   # or via service
   /etc/init.d/seafile-server start
   ```
   
5. If the new version works fine, the old version can be removed

   ```sh
   rm -rf seafile-server-4.3.0/
   ```

## Minor version upgrade (e.g. from 5.0.x to 5.1.y)

Suppose you are using version 5.0.0 and like to upgrade to version 5.1.0. First download and extract the new version. You should have a directory layout similar to this:

```
haiwen
   -- seafile-server-5.0.0
   -- seafile-server-5.1.0
   -- ccnet
   -- seafile-data
```


Now upgrade to version 5.1.0.

1. Shutdown Seafile server if it's running

   ```sh
   cd haiwen/seafile-server-5.0.0
   ./seahub.sh stop
   ./seafile.sh stop
   # or via service
   /etc/init.d/seafile-server stop
   ```
   
2. Check the upgrade scripts in seafile-server-5.1.0 directory.

   ```sh
   cd haiwen/seafile-server-5.1.0
   ls upgrade/upgrade_*
   ```

   You will get a list of upgrade files:

   ```
   ...
   upgrade/upgrade_4.0_4.1.sh
   upgrade/upgrade_4.1_4.2.sh
   upgrade/upgrade_4.2_4.3.sh
   upgrade/upgrade_4.3_4.4.sh
   upgrade/upgrade_4.4_5.0.sh
   upgrade/upgrade_5.0_5.1.sh
   ```

3. Start from your current version, run the script(s one by one)

   ```
   upgrade/upgrade_5.0_5.1.sh
   ```

4. Start Seafile server

   ```sh
   cd haiwen/seafile-server-5.1.0/
   ./seafile.sh start
   ./seahub.sh start # or "./seahub.sh start-fastcgi" if you're using fastcgi
   # or via service
   /etc/init.d/seafile-server start
   ```
   
5. If the new version works, the old version can be removed

   ```sh
   rm -rf seafile-server-5.0.0/
   ```

## Maintenance version upgrade (e.g. from 5.1.2 to 5.1.3)

A maintenance upgrade is for example an upgrade from 5.1.2 to 5.1.3.

1. Shutdown Seafile server if it's running

2. For this type of upgrade, you only need to update the symbolic links (for avatar and a few other folders). 
A script to perform a minor upgrade is provided with Seafile server (for history reasons, the script is called `minor-upgrade.sh`):

   ```sh
   cd seafile-server-5.1.3
   upgrade/minor-upgrade.sh
   ```

3. Start Seafile

4. If the new version works, the old version can be removed

   ```sh
   rm -rf seafile-server-5.1.2/
   ```
