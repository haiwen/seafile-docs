# Virus Scan

**Note**: Since Seafile Server 5.0.0, all config files are moved to the central **conf** folder. [Read More](../deploy/new_directory_layout_5_0_0.md).

In Seafile Professional Server 4.4.0 (or above), Seafile can scan uploaded files for malicious content in the background. When configured to run periodically, the scan process scans all existing libraries on the server. In each scan, the process only scans newly uploaded/updated files since the last scan. For each file, the process executes a user-specified virus scan command to check whether the file is a virus or not. Most anti-virus programs provide command line utility for Linux.

To enable this feature, add the following options to `seafile.conf`:

```
[virus_scan]
scan_command = (command for checking virus)
virus_code = (command exit codes when file is virus)
nonvirus_code = (command exit codes when file is not virus)
scan_interval = (scanning interval, in unit of minutes, default to 60 minutes)
```

More details about the options:

* On Linux/Unix, most virus scan commands returns specific exit codes for virus and non-virus. You should consult the manual of your anti-virus program for more information.

An example for ClamAV (http://www.clamav.net/) is provided below:

```
[virus_scan]
scan_command = clamscan
virus_code = 1
nonvirus_code = 0
```

To test whether your configuration works, you can trigger a scan manually:

```
cd seafile-server-latest
./pro/pro.py virus_scan
```

If a virus was detected, you can see scan records and delete infected files on the Virus Scan page in the admin area.
![virus-scan](../images/virus-scan.png)

**INFO**: If you directly use clamav command line tool to scan files, scanning files will takes a lot of time. If you want to speed it up, we recommend to run Clamav as a daemon. Please refer to [Run ClamAV as a Daemon](deploy_clamav_as_daemon.md)

When run Clamav as a daemon, the `scan_command` should be `clamdscan` in `seafile.conf`. An example for Clamav-daemon is provided below:
```
[virus_scan]
scan_command = clamdscan
virus_code = 1
nonvirus_code = 0
```
 
Since Pro edition 6.0.0, a few more options are added to provide finer grained control for virus scan.

```
[virus_scan]
......
scan_size_limit = (size limit for files to be scanned)
scan_skip_ext = (a comma (',') separated list of file extensions to be ignored)
threads = (number of concurrent threads for scan, one thread for one file, default to 4)
```

The file extensions should start with '.'. The extensions are case insensitive. By default, files with following extensions will be ignored:

```
.bmp, .gif, .ico, .png, .jpg, .mp3, .mp4, .wav, .avi, .rmvb, .mkv
```

The list you provide will override default list.
