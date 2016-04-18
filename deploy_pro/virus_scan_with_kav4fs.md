# Virus Scan with kav4fs

## Prerequisite

Assume you have installed Kaspersky Anti-Virus for Linux File Server in Seafile server machine.

If the user that runs Seafile server is not root, it should have sudoers privilege to avoid writing password when running kav4fs-control. Add following content to /etc/sudoers:

```
<user of running seafile server>	ALL=(ALL:ALL) ALL
<user of running seafile server> ALL=NOPASSWD: /opt/kaspersky/kav4fs/bin/kav4fs-control
```

## Script

As the return code of kav4fs can not reflect the file scan result, we use a shell script to parse
the scan output and based on the parse result to return different return code to reflect the scan result.

Save following contents to a file such as `kav4fs_scan.sh`:

```
#!/bin/bash

TEMP_LOG_FILE=`mktemp /tmp/XXXXXXXXXX`
VIRUS_FOUND=1
CLEAN=0
UNDEFINED=2
KAV4FS='/opt/kaspersky/kav4fs/bin/kav4fs-control'
if [ ! -x $KAV4FS ]
then
    echo "Binary not executable"
    exit $UNDEFINED
fi

sudo $KAV4FS --scan-file $1 > $TEMP_LOG_FILE
if [ "$?" -ne 0 ]
then
    echo "Error due to check file '$1'"
    exit 3
fi
THREATS_C=`grep 'Threats found:' $TEMP_LOG_FILE|cut -d':' -f 2|sed 's/ //g'`
RISKWARE_C=`grep 'Riskware found:' $TEMP_LOG_FILE|cut -d':' -f 2|sed 's/ //g'`
INFECTED=`grep 'Infected:' $TEMP_LOG_FILE|cut -d':' -f 2|sed 's/ //g'`
SUSPICIOUS=`grep 'Suspicious:' $TEMP_LOG_FILE|cut -d':' -f 2|sed 's/ //g'`
SCAN_ERRORS_C=`grep 'Scan errors:' $TEMP_LOG_FILE|cut -d':' -f 2|sed 's/ //g'`
PASSWORD_PROTECTED=`grep 'Password protected:' $TEMP_LOG_FILE|cut -d':' -f 2|sed 's/ //g'`
CORRUPTED=`grep 'Corrupted:' $TEMP_LOG_FILE|cut -d':' -f 2|sed 's/ //g'`

rm -f $TEMP_LOG_FILE

if [ $THREATS_C -gt 0 -o $RISKWARE_C -gt 0 -o $INFECTED -gt 0 -o $SUSPICIOUS -gt 0 ]
then
    exit $VIRUS_FOUND
elif [ $SCAN_ERRORS_C -gt 0 -o $PASSWORD_PROTECTED -gt 0 -o $CORRUPTED -gt 0 ]
then
    exit $UNDEFINED
else
    exit $CLEAN
fi
```

Grant executable privilege to the script:

```
chmod u+x kav4fs_scan.sh
```

The meaing of the script return code:

```
1: found virus
0: no virus
other: scan failed
```

## configuration

Add following content to `seafile.conf`:

```
[virus_scan]
scan_command = <absolute path of kav4fs_scan.sh>
virus_code = 1
nonvirus_code = 0
scan_interval = <scanning interval, in unit of minutes, default to 60 minutes>
```
