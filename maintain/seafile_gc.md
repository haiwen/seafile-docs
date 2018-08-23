# Seafile GC

Seafile uses storage de-duplication technology to reduce storage usage. The underlying data blocks will not be removed immediately after you delete a file or a library. As a result, the number of unused data blocks will increase on Seafile server.

To release the storage space occupied by unused blocks, you have to run a
"garbage collection" program to clean up unused blocks on your server.

The GC program cleans up two types of unused blocks:

1. Blocks that no library references to, that is, the blocks belong to deleted libraries;
2. If you set history length limit on some libraries, the out-dated blocks in those libraries will also be removed.

**Before running GC, you must shutdown the Seafile program on your server if you use the community edition. For professional edition, from version 3.1.11, online GC operation is supported. If you use Professional edition, you don't need to shutdown the Seafile program if you are using MySQL or PostgreSQL as database.**  
This is because new blocks written into Seafile while GC is running may be mistakenly deleted by the GC program.

***Community version - GC cleanup Script***

At the bottom of the page there is a script that you can use to run the cleanup manually or e.g. once a week with as cronjob.

## Run GC in version 4.1.1 and later

In community edition 4.1.1 and Pro edition 4.1.0, GC program's command line and output are improved.

### Dry-run Mode

To see how much garbage can be collected without actually removing any garbage, use the dry-run option:

```
seaf-gc.sh --dry-run [repo-id1] [repo-id2] ...
```

The output should look like:

```
[03/19/15 19:41:49] seafserv-gc.c(115): GC version 1 repo My Library(ffa57d93)
[03/19/15 19:41:49] gc-core.c(394): GC started. Total block number is 265.
[03/19/15 19:41:49] gc-core.c(75): GC index size is 1024 Byte.
[03/19/15 19:41:49] gc-core.c(408): Populating index.
[03/19/15 19:41:49] gc-core.c(262): Populating index for repo ffa57d93.
[03/19/15 19:41:49] gc-core.c(308): Traversed 5 commits, 265 blocks.
[03/19/15 19:41:49] gc-core.c(440): Scanning unused blocks.
[03/19/15 19:41:49] gc-core.c(472): GC finished. 265 blocks total, about 265 reachable blocks, 0 blocks can be removed.

[03/19/15 19:41:49] seafserv-gc.c(115): GC version 1 repo aa(f3d0a8d0)
[03/19/15 19:41:49] gc-core.c(394): GC started. Total block number is 5.
[03/19/15 19:41:49] gc-core.c(75): GC index size is 1024 Byte.
[03/19/15 19:41:49] gc-core.c(408): Populating index.
[03/19/15 19:41:49] gc-core.c(262): Populating index for repo f3d0a8d0.
[03/19/15 19:41:49] gc-core.c(308): Traversed 8 commits, 5 blocks.
[03/19/15 19:41:49] gc-core.c(264): Populating index for sub-repo 9217622a.
[03/19/15 19:41:49] gc-core.c(308): Traversed 4 commits, 4 blocks.
[03/19/15 19:41:49] gc-core.c(440): Scanning unused blocks.
[03/19/15 19:41:49] gc-core.c(472): GC finished. 5 blocks total, about 9 reachable blocks, 0 blocks can be removed.

[03/19/15 19:41:49] seafserv-gc.c(115): GC version 1 repo test2(e7d26d93)
[03/19/15 19:41:49] gc-core.c(394): GC started. Total block number is 507.
[03/19/15 19:41:49] gc-core.c(75): GC index size is 1024 Byte.
[03/19/15 19:41:49] gc-core.c(408): Populating index.
[03/19/15 19:41:49] gc-core.c(262): Populating index for repo e7d26d93.
[03/19/15 19:41:49] gc-core.c(308): Traversed 577 commits, 507 blocks.
[03/19/15 19:41:49] gc-core.c(440): Scanning unused blocks.
[03/19/15 19:41:49] gc-core.c(472): GC finished. 507 blocks total, about 507 reachable blocks, 0 blocks can be removed.

[03/19/15 19:41:50] seafserv-gc.c(124): === Repos deleted by users ===
[03/19/15 19:41:50] seafserv-gc.c(145): === GC is finished ===

[03/19/15 19:41:50] Following repos have blocks to be removed:
repo-id1
repo-id2
repo-id3
```

If you give specific library ids, only those libraries will be checked; otherwise all libraries will be checked.

Notice that at the end of the output there is a "repos have blocks to be removed" section. It contains the list of librareis that have garbage blocks. Later when you run GC without --dry-run option, you can use these libraris ids as input arguments to GC program.

### Removing Garbage

To actually remove garbage blocks, run without the --dry-run option:

```
seaf-gc.sh [repo-id1] [repo-id2] ...
```

If libraries ids are specified, only those libraries will be checked for garbage.

As described before, there are two types of garbage blocks to be removed. Sometimes just removing the first type of blocks (those that belong to deleted libraries) is good enough. In this case, the GC program won't bother to check the libraries for outdated historic blocks. The "-r" option implements this feature:

```
seaf-gc.sh -r
```

**In Seafile version 4.1.1 and later, libraries deleted by the users are not immediately removed from the system. Instead, they're moved into a "trash" in the system admin page. Before they're cleared from the trash, their blocks won't be garbage collected.**

### Using Multiple Threads in GC

Since Pro server 5.1.0, you can specify the thread number in GC. By default,

- If storage backend is S3/Swift/Ceph, 10 threads are started to do the GC work.
- If storage backend is file system, only 1 thread is started.

You can specify the thread number in with "-t" option. "-t" option can be used together with all other options. Each thread will do GC on one library. For example, the following command will use 20 threads to GC all libraries:

```
seaf-gc.sh -t 20
```

Since the threads are concurrent, the output of each thread may mix with each others. Library ID is printed in each line of output.

## Run GC in older versions (before 4.1.1)

To run GC program

    ./seaf-gc.sh run

If you want to do sanity check before actually removing any data, you can use the --dry-run option

    ./seaf-gc.sh dry-run

It will show you the total block number vs. the number of blocks to be removed.

To check data integrity after running GC, you can use [seaf-fsck](seafile_fsck.md)

## GC cleanup script for Community Version

To use this script you need:

- Setup the seafile-service file at '/etc/init.d/seafile-server'
- Files of seafile setup need to be owner by 'seafile:nogroup' or 'seafile:seafile'
- Run the script with sudo or as root
- Put the script into crontab of a root user

Create the script file (change the location to your liking):

    touch /opt/haiwen/seafile/cleanupScript.sh
    
Use your favorite text editor and paste the following code:

```
#!/bin/bash

#####
# Uncomment the following line if you rather want to run the script manually.
# Display usage if the script is not run as root user
#        if [[ $USER != "root" ]]; then
#                echo "This script must be run as root user!"
#                exit 1
#        fi
#
# echo "Super User detected!!"
# read -p "Press [ENTER] to start the procedure, this will stop the seafile server!!"
#####

# stop the server
echo Stopping the Seafile-Server...
systemctl stop seafile.service
systemctl stop seahub.service

echo Giving the server some time to shut down properly....
sleep 20

# run the cleanup
echo Seafile cleanup started...
sudo -u seafile $pathtoseafile/seafile-server-latest/seaf-gc.sh

echo Giving the server some time....
sleep 10

# start the server again
echo Starting the Seafile-Server...
systemctl start seafile.service
systemctl start seahub.service

echo Seafile cleanup done!
```
Make sure that the script has been given execution rights, to do that run this command.

    sudo chmod +x /path/to/yourscript.sh

Then open crontab with the root user

    crontab -e
    
Add the following line (change the location of your script accordingly!)

    0 2 * * Sun /opt/haiwen/seafile/cleanupScript.sh
    
The script will then run every Sunday at 2:00 AM.

## GC in the [seafile docker container](https://github.com/haiwen/seafile-docker)

To perform garbage collection inside the seafile docker container, you must run the `/scripts/gc.sh` script. Simply run `docker exec <whatever-your-seafile-container-is-called> /scripts/gc.sh`.
