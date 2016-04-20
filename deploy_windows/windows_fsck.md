
### Running seaf-fsck on corrupted repositories ###

For the time being there is no batch file available for running `seaf-fsck.exe` in a Windows environment.
To manually run `seaf-fsck.exe`, follow the following procedure (assuming you've installed Seafile server to `X:\Seafile\`:

1. Open a command prompt by following *either* of these steps
  - Click **Start**, **Run**, enter `cmd.exe` and then navigate to the binary folder by entering `cd /d X:\Seafile\seafile-server-5.x.x\seafile\bin`
  - Or, using the file explorer:
    * Navigate to the folder where the binaries are located (`X:\Seafile\seafile-server-5.x.x\seafile\bin`)
    * Hold shift and right click in free space to bring up the context menu, then select **Open command window here**
2. Enter the following inside the opened command prompt: `seaf-fsck.exe --repair -c Y:\seafile-user\ccnet -d Y:\seafile-user\seafile-data -F Y:\seafile-user\conf`
  - *seafile-user* is the folder your Seafile data is stored in
  - Make sure you are pointing `seaf-fsck.exe` towards the correct directory: *ccnet*, *seafile-data* and *conf* folders must be present
3. `seaf-fsck` should be running now

For information on *seaf-fsck*, its usage and syntax, see the chapter [Seafile FSCK](../maintain/seafile_fsck.md).
