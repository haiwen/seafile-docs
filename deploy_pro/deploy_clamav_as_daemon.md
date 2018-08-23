# Run ClamAV as a Daemon

## For Ubuntu 16.04

### Install clamav-daemon & clamav-freshclam

```
apt-get install clamav-daemon clamav-freshclam
```

You should run Clamd with a root permission to scan any files. 
Edit the conf `/etc/clamav/clamd.conf`,change the following line:

```
LocalSocketGroup root
User root
```

### Start the clamav-daemon

```
systemctl start clamav-daemon
```

* Test the software

```
$ curl https://www.eicar.org/download/eicar.com.txt | clamdscan -
```

The output must include:

```
stream: Eicar-Test-Signature FOUND
```

## For CentOS 7

### Install Clamd

```
yum install epel-release
yum install clamav-server clamav-data clamav-filesystem clamav-lib clamav-update clamav clamav-devel
```

### Run freshclam

* Configure the freshclam to updating database

```
cp /etc/freshclam.conf /etc/freshclam.conf.bak
sed -i '/^Example/d' /etc/freshclam.conf
```

* Create the init script

```
cat > /usr/lib/systemd/system/clam-freshclam.service << 'EOF'
# Run the freshclam as daemon
[Unit]
Description = freshclam scanner
After = network.target

[Service]
Type = forking
ExecStart = /usr/bin/freshclam -d -c 4
Restart = on-failure
PrivateTmp = true

[Install]
WantedBy=multi-user.target

EOF
```

* Boot up

```
systemctl enable clam-freshclam.service
systemctl start clam-freshclam.service
```

### Configure Clamd

```
cp /usr/share/clamav/template/clamd.conf /etc/clamd.conf
sed -i '/^Example/d' /etc/clamd.conf
```

You should run Clamd with a root permission to scan any files. 
Edit the `/etc/clamd.conf`,change the following line:

```
User root
...
LocalSocket /var/run/clamd.sock
```

### Run Clamd

* Create the init script

```
cat > /etc/init.d/clamd << 'EOF'
case "$1" in
  start)
    echo -n "Starting Clam AntiVirus Daemon... "
    /usr/sbin/clamd
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && touch /var/lock/subsys/clamd
    ;;
  stop)
    echo -n "Stopping Clam AntiVirus Daemon... "
    pkill clamd
    rm -f /var/run/clamav/clamd.sock
    rm -f /var/run/clamav/clamd.pid
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && rm -f /var/lock/subsys/clamd
    ;;
esac

EOF
```

```
chmod +x /etc/init.d/clamd
```

* Boot up

```
chkconfig clamd on
service clamd start
```

* Test the software

```
$ curl https://www.eicar.org/download/eicar.com.txt | clamdscan -
```

The output must include:

```
stream: Eicar-Test-Signature FOUND
```