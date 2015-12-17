# Seafile FSCK

On the server side, Seafile stores the files in the libraries in an internal format. Seafile has its own representation of directories and files (similar to Git).

With default installation, these internal objects are stored in the server's file system directly (such as Ext4, NTFS). But most file systems don't assure the integrity of file contents after a hard shutdown or system crash. So if new Seafile internal objects are being written when the system crashes, they can be corrupt after the system reboots. This will make part of the corresponding library not accessible.

Note: If you store the seafile-data directory in a battery-backed NAS (like EMC or NetApp), or use S3 backend available in the Pro edition, the internal objects won't be corrupt.

Starting from version 2.0, Seafile server comes with a seaf-fsck tool to help you recover from this corruption (similar to git-fsck tool). This tool recovers any corrupted library back to its last consistent and usable state.

Starting from version 4.1, we provide a seaf-fsck.sh script. The seaf-fsck tool accepts the following arguments:

```
cd seafile-server-latest
./seaf-fsck.sh [--repair|-r] [--enable-sync|-e] [--export|-E export_path] [repo_id_1 [repo_id_2 ...]]
```

There are three modes of operation for seaf-fsck:

1. checking integrity of libraries.
2. repairing corrupted libraries.
3. exporting libraries.

## Checking Integrity of Libraries

Running seaf-fsck.sh without any arguments will run a **read-only** integrity check for all libraries.

```
cd seafile-server-latest
./seaf-fsck.sh
```

If you want to check integrity for specific libraries, just append the library id's as arguments:

```
cd seafile-server-latest
./seaf-fsck.sh [library-id1] [library-id2] ...
```

The output looks like:

```
[02/13/15 16:21:07] fsck.c(470): Running fsck for repo ca1a860d-e1c1-4a52-8123-0bf9def8697f.
[02/13/15 16:21:07] fsck.c(413): Checking file system integrity of repo fsck(ca1a860d)...
[02/13/15 16:21:07] fsck.c(35): Dir 9c09d937397b51e1283d68ee7590cd9ce01fe4c9 is missing.
[02/13/15 16:21:07] fsck.c(200): Dir /bf/pk/(9c09d937) is curropted.
[02/13/15 16:21:07] fsck.c(105): Block 36e3dd8757edeb97758b3b4d8530a4a8a045d3cb is corrupted.
[02/13/15 16:21:07] fsck.c(178): File /bf/02.1.md(ef37e350) is curropted.
[02/13/15 16:21:07] fsck.c(85): Block 650fb22495b0b199cff0f1e1ebf036e548fcb95a is missing.
[02/13/15 16:21:07] fsck.c(178): File /01.2.md(4a73621f) is curropted.
[02/13/15 16:21:07] fsck.c(514): Fsck finished for repo ca1a860d.
```

The corrupted files and directories are reported.

Sometimes you can see output like the following:

```
[02/13/15 16:36:11] Commit 6259251e2b0dd9a8e99925ae6199cbf4c134ec10 is missing
[02/13/15 16:36:11] fsck.c(476): Repo ca1a860d HEAD commit is corrupted, need to restore to an old version.
[02/13/15 16:36:11] fsck.c(314): Scanning available commits...
[02/13/15 16:36:11] fsck.c(376): Find available commit 1b26b13c(created at 2015-02-13 16:10:21) for repo ca1a860d.
```

This means the "head commit" (current state of the library) recorded in database is not consistent with the library data. In such case, fsck will try to find the last consistent state and check the integrity in that state.

Tips: **If you have many libraries, it's helpful to save the fsck output into a log file for later analysis.**

## Repairing Corruption

Corruption repair in seaf-fsck basically works in two steps:

1. If the library state (commit) recorded in database is not found in data directory, find the last available state from data directory.
2. Check data integrity in that specific state. If files or directories are corrupted, set them to empty files or empty directories. The corrupted paths will be reported, so that the user can recover them from somewhere else.

Running the following command repairs all the libraries:

```
cd seafile-server-latest
./seaf-fsck.sh --repair
```

Most of time you run the read-only integrity check first, to find out which libraries are corrupted. And then you repair specific libraries with the following command:

```
cd seafile-server-latest
./seaf-fsck.sh --repair [library-id1] [library-id2] ...
```

Because corrupted files and directories are emptied after repair, syncing the library after repair may result in data lost in the clients. The good copies on the clients may be replaced by the empty copies. To prevent this from happening, the system prevents a "repaired" library from syncing to clients. The system admin should inform the users to recover the corrupted files and folders. And then run the following command to enable syncing for the library again:

```
cd seafile-server-latest
./seaf-fsck.sh --enable-sync [library-id1] [library-id2] ...
```

### Change after CE 5.0.3 and Pro 5.0.2

Since community eidition 5.0.3 and Pro edition 5.0.2, we improved seaf-fsck repair operation. Two improvements are added:

- After running "--repair" operation, the system admin doesn't need to run "--enable-sync" command any more. Instead, seaf-fsck automatically disconnects all syncing clients to the library. So the users are forced to re-sync the library.
- In the library history, seaf-fsck includes the list of files and folders that are corrupted. So it's much easier to located corrupted paths.

### Best Practice for Repairing a Library

To check all libraries and find out which library is corrupted, the system admin can run seaf-fsck.sh without any argument and save the output to a log file. Search for keyword "Fail" in the log file to locate corrupted libraries.

When the system admin find a library is corrupted, he/she should run seaf-fsck.sh with "--repair" for the library. After the command fixes the library, the admin should inform user to recover files from other places. There are two ways:

- Upload corrupted files or folders via the web interface
- If the library was synced to some desktop computer, and that computer has a correct version of the corrupted file, resyncing the library on that computer will upload the corrupted files to the server.

## Exporting Libraries to File System

Since version 4.2.0, you can use seaf-fsck to export all the files in libraries to external file system (such as Ext4). This procedure doesn't rely on the seafile database. As long as you have your seafile-data directory, you can always export your files from Seafile to external file system.

The command syntax is

```
cd seafile-server-latest
./seaf-fsck.sh --export top_export_path [library-id1] [library-id2] ...
```

The argument `top_export_path` is a directory to place the exported files. Each library will be exported as a sub-directory of the export path. If you don't specify library ids, all libraries will be exported.

Currently only un-encrypted libraries can be exported. Encrypted libraries will be skipped.
