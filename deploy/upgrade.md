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


Now upgrade to version 3.1.0.

1. Shutdown Seafile server if it's running

   ```sh
   cd haiwen/seafile-server-2.1.0
   ./seahub.sh stop
   ./seafile.sh stop
   ```
2. Check the upgrade scripts in seafile-server-3.1.0 directory.

   ```sh
   cd haiwen/seafile-server-3.1.0
   ls upgrade/upgrade_*
   ```

   You will get a list of upgrade files:

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

4. Start the new server version as for any upgrade

   ```sh
   cd haiwen/seafile-server-3.1.0/
   ./seafile.sh start
   ./seahub.sh start # or "./seahub.sh start-fastcgi" if you're using fastcgi
   ```

## Minor version upgrade (like from 3.0.x to 3.2.y)

Suppose you are using version 3.0.0 and like to upgrade to version 3.2.2. First download and extract the new version. You should have a directory layout similar to this:


<pre>
haiwen
   -- seafile-server-3.0.0
   -- seafile-server-3.2.2
   -- ccnet
   -- seafile-data
</pre>


Now upgrade to version 3.2.2.

1. Shutdown Seafile server if it's running

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

   You will get a list of upgrade files:

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

4. Start the new server version as for any upgrade

   ```sh
   cd haiwen/seafile-server-3.2.2/
   ./seafile.sh start
   ./seahub.sh start
   ```


## Maintenance version upgrade (like from 3.1.0 to 3.1.2)

Maintenance upgrade is like an upgrade from 3.1.0 to 3.1.2.


1. Stop the current server first as for any upgrade
2. For this type of upgrade, you only need to update the symbolic links (for avatar and a few other folders). We provide a script for you, just run it (For history reason, the script called `minor-upgrade.sh`):

   ```sh
   cd seafile-server-3.1.2
   upgrade/minor-upgrade.sh
   ```

3. Start the new server version as for any upgrade

4. If the new version works file, the old version can be removed

   ```sh
   rm -rf seafile-server-3.1.0
   ```
