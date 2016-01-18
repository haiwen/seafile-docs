# Seafile
## Upgrade Manual

This page is for users who use the pre-compiled seafile server package.

- If you [build seafile server from source](../build_seafile/server.md), please read the **Upgrading Seafile Server** section on that page, instead of this one.
- After upgrading, you may need to clean [seahub cache](add_memcached.md) if it doesn't behave as expect.

### IMPORTANT
Always make a backup of your current databases in case something goes wrong. If you have the option to make snapshots on your virtual server you can save yourself a lot of trouble and time!


## Major version upgrade (like from 4.x.x to 5.y.y)


Suppose you are using version 4.3.0 and like to upgrade to version 5.0.0. First download and extract the new version. You should have a directory layout similar to this:


<pre>
haiwen
   -- seafile-server-4.3.0
   -- seafile-server-5.0.0
   -- ccnet
   -- seafile-data
</pre>


Now upgrade to version 5.0.0.

1. Shutdown Seafile server if it's running

   ```sh
   cd haiwen/seafile-server-4.3.0
   ./seahub.sh stop
   ./seafile.sh stop
   ```
2. Check the upgrade scripts in seafile-server-5.0.0 directory.

   ```sh
   cd haiwen/seafile-server-5.0.0
   ls upgrade/upgrade_*
   ```

   You will get a list of upgrade files:

   ```
   ...
   upgrade/upgrade_3.1_4.0.sh
   upgrade/upgrade_4.0_4.1.sh
   upgrade/upgrade_4.1_4.2.sh
   upgrade/upgrade_4.2_4.3.sh
   upgrade/upgrade_4.3_4.4.sh
   upgrade/upgrade_4.4_5.0.sh
   ```

3. Start from you current version, run the script one by one

   ```
   upgrade/upgrade_4.3_4.4.sh
   upgrade/upgrade_4.4_5.0.sh
   ```

4. Start the new server version as for any upgrade

   ```sh
   cd haiwen/seafile-server-5.0.0/
   ./seafile.sh start
   ./seahub.sh start
   ```
5. If the new version works file, the old version can be removed

   ```sh
   rm -rf seafile-server-4.3.0/
   ```
   or alternatively be moved to the directory installed (in case you set it up)
   
    ```sh
   mv seafile-server-4.3.0/ installed/
   ```
   
## Minor version upgrade (like from 4.2.x to 4.4.y)

Suppose you are using version 4.2.0 and like to upgrade to version 4.4.0. First download and extract the new version. You should have a directory layout similar to this:


<pre>
haiwen
   -- seafile-server-4.2.0
   -- seafile-server-4.4.0
   -- ccnet
   -- seafile-data
</pre>


Now upgrade to version 4.4.0.

1. Shutdown Seafile server if it's running

   ```sh
   cd haiwen/seafile-server-4.2.0
   ./seahub.sh stop
   ./seafile.sh stop
   ```
2. Check the upgrade scripts in seafile-server-4.4.0 directory.

   ```sh
   cd haiwen/seafile-server-4.4.0
   ls upgrade/upgrade_*
   ```

   You will get a list of upgrade files:

   ```
   ...
   upgrade/upgrade_3.1_4.0.sh
   upgrade/upgrade_4.0_4.1.sh
   upgrade/upgrade_4.1_4.2.sh
   upgrade/upgrade_4.2_4.3.sh
   upgrade/upgrade_4.3_4.4.sh
   ```

3. Start from you current version, run the script one by one

   ```
   upgrade/upgrade_4.2_4.3.sh
   upgrade/upgrade_4.3_4.4.sh
   ```

4. Start the new server version as for any upgrade

   ```sh
   cd haiwen/seafile-server-4.4.0/
   ./seafile.sh start
   ./seahub.sh start
   ```
5. If the new version works file, the old version can be removed

   ```sh
   rm -rf seafile-server-4.2.0/
   ```
   or alternatively be moved to the directory installed (in case you set it up)
   
    ```sh
   mv seafile-server-4.2.0/ installed/
   ```

## Tiny upgrade (like from 5.0.2 to 5.0.4)

Tiny upgrade is like an upgrade from 5.0.2 to 5.0.4.


1. Stop the current server first as for any upgrade
2. For this type of upgrade, you only need to update the avatar link. We provide a script for you, just run it (For history reason, the script is called `minor-upgrade.sh` and not `tiny-upgrade.sh`):

   ```sh
   cd seafile-server-5.0.2
   upgrade/minor-upgrade.sh
   ```

3. Start the new server version as for any upgrade
4. If the new version works file, the old version can be removed

   ```sh
   rm -rf seafile-server-5.0.2/
   ```
   or alternatively be moved to the directory installed (in case you set it up)
   
    ```sh
   mv seafile-server-5.0.2/ installed/
   ```
   
