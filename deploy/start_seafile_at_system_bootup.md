# Start Seafile at System Bootup

For systems running systemd
---------------------------
- For example Debian 8 and newer, Linux Ubuntu 15.04 and newer

Create systemd service files, change **${seafile\_dir}** to your
**seafile** installation location and **seafile** to user, who runs
**seafile** (if appropriate). Then you need to reload systemd's daemons:
**systemctl daemon-reload**.

### Create systemd service file /etc/systemd/system/seafile.service

    sudo vim /etc/systemd/system/seafile.service
    
The content of the file is:

    [Unit]
    Description=Seafile
    # add mysql.service or postgresql.service depending on your database to the line below
    After=network.target

    [Service]
    Type=forking
    ExecStart=${seafile_dir}/seafile-server-latest/seafile.sh start
    ExecStop=${seafile_dir}/seafile-server-latest/seafile.sh stop
    User=seafile
    Group=seafile

    [Install]
    WantedBy=multi-user.target

### Create systemd service file /etc/systemd/system/seahub.service

    sudo vim /etc/systemd/system/seahub.service
    
The content of the file is (please dont forget to change it if you want to run fastcgi):

    [Unit]
    Description=Seafile hub
    After=network.target seafile.service

    [Service]
    Type=forking
    # change start to start-fastcgi if you want to run fastcgi
    ExecStart=${seafile_dir}/seafile-server-latest/seahub.sh start
    ExecStop=${seafile_dir}/seafile-server-latest/seahub.sh stop
    User=seafile
    Group=seafile

    [Install]
    WantedBy=multi-user.target

### Create systemd service file /etc/systemd/system/seafile-client.service (optional)

You need to create this service file only if you have **seafile**
console client and you want to run it on system boot.

    sudo vim /etc/systemd/system/seafile-client.service
    
The content of the file is:

    [Unit]
    Description=Seafile client
    # Uncomment the next line you are running seafile client on the same computer as server
    # After=seafile.service
    # Or the next one in other case
    # After=network.target

    [Service]
    Type=oneshot
    ExecStart=/usr/bin/seaf-cli start
    ExecStop=/usr/bin/seaf-cli stop
    RemainAfterExit=yes
    User=seafile
    Group=seafile

    [Install]
    WantedBy=multi-user.target

### Enable service start on system boot

    sudo systemctl enable seafile.service
    sudo systemctl enable seahub.service
    sudo systemctl enable seafile-client.service   # optional



For systems using another init system than systemd
--------------------------------------------------

Ubuntu 14.10 and older
----------------------

On Ubuntu without systemd we make use of the
[/etc/init.d/](https://help.ubuntu.com/community/UbuntuBootupHowto)
scripts to start seafile/seahub at system boot.

### Create a script **/etc/init.d/seafile-server**

    sudo vim /etc/init.d/seafile-server

The content of this script is: (You need to modify the value of **user**
and **seafile\_dir** accordingly)

    #!/bin/bash
    ### BEGIN INIT INFO
    # Provides:          seafile-server
    # Required-Start:    $remote_fs $syslog
    # Required-Stop:     $remote_fs $syslog
    # Default-Start:     2 3 4 5
    # Default-Stop:      0 1 6
    # Short-Description: Seafile server
    # Description:       Start Seafile server
    ### END INIT INFO
    
    # Change the value of "user" to your linux user name
    user=haiwen

    # Change the value of "seafile_dir" to your path of seafile installation
    # usually the home directory of $user
    seafile_dir=/data/haiwen
    script_path=${seafile_dir}/seafile-server-latest
    seafile_init_log=${seafile_dir}/logs/seafile.init.log
    seahub_init_log=${seafile_dir}/logs/seahub.init.log

    # Change the value of fastcgi to false if fastcgi is not used
    fastcgi=true
    # Set the port of fastcgi, default is 8000. Change it if you need different.
    fastcgi_port=8000
    #
    # Write a polite log message with date and time
    #
    echo -e "\n \n About to perform $1 for seafile at `date -Iseconds` \n " >> ${seafile_init_log}
    echo -e "\n \n About to perform $1 for seahub at `date -Iseconds` \n " >> ${seahub_init_log}
    case "$1" in
            start)
                    sudo -u ${user} ${script_path}/seafile.sh ${1} >> ${seafile_init_log}
                    if [ $fastcgi = true ];
                    then
                            sudo -u ${user} ${script_path}/seahub.sh ${1}-fastcgi ${fastcgi_port} >> ${seahub_init_log}
                    else
                            sudo -u ${user} ${script_path}/seahub.sh ${1} >> ${seahub_init_log}
                    fi
            ;;
            restart)
                    sudo -u ${user} ${script_path}/seafile.sh ${1} >> ${seafile_init_log}
                    if [ $fastcgi = true ];
                    then
                            sudo -u ${user} ${script_path}/seahub.sh ${1}-fastcgi ${fastcgi_port} >> ${seahub_init_log}
                    else
                            sudo -u ${user} ${script_path}/seahub.sh ${1} >> ${seahub_init_log}
                    fi
            ;;
            stop)
                    sudo -u ${user} ${script_path}/seahub.sh ${1} >> ${seahub_init_log}
                    sudo -u ${user} ${script_path}/seafile.sh ${1} >> ${seafile_init_log}
            ;;
            *)
                    echo "Usage: /etc/init.d/seafile-server {start|stop|restart}"
                    exit 1
            ;;
    esac

**Note:** If you are using local mysql server, please replace `# Required-Start:    $remote_fs $syslog` with `# Required-Start:    $remote_fs $syslog mysql`.

### Make the seafile-sever script executable

    sudo chmod +x /etc/init.d/seafile-server

### Add seafile-server to rc.d

    sudo update-rc.d seafile-server defaults

**Note:** Don't forget to update the value of **script\_path** later if you update
your seafile server.

Other Debian based Distributions
--------------------------------

### Create a script **/etc/init.d/seafile-server**

    sudo vim /etc/init.d/seafile-server

The content of this script is: (You need to modify the value of **user**
and **seafile\_dir** accordingly)

    #!/bin/sh

    ### BEGIN INIT INFO
    # Provides:          seafile-server
    # Required-Start:    $local_fs $remote_fs $network
    # Required-Stop:     $local_fs
    # Default-Start:     2 3 4 5
    # Default-Stop:      0 1 6
    # Short-Description: Starts Seafile Server
    # Description:       starts Seafile Server
    ### END INIT INFO

    # Change the value of "user" to linux user name who runs seafile
    user=haiwen

    # Change the value of "seafile_dir" to your path of seafile installation
    # usually the home directory of $user
    seafile_dir=/data/haiwen
    script_path=${seafile_dir}/seafile-server-latest
    seafile_init_log=${seafile_dir}/logs/seafile.init.log
    seahub_init_log=${seafile_dir}/logs/seahub.init.log

    # Change the value of fastcgi to true if fastcgi is to be used
    fastcgi=false
    # Set the port of fastcgi, default is 8000. Change it if you need different.
    fastcgi_port=8000

    #
    # Write a polite log message with date and time
    #
    echo -e "\n \n About to perform $1 for seafile at `date -Iseconds` \n " >> ${seafile_init_log}
    echo -e "\n \n About to perform $1 for seahub at `date -Iseconds` \n " >> ${seahub_init_log}

    case "$1" in
            start)
                    sudo -u ${user} ${script_path}/seafile.sh ${1} >> ${seafile_init_log}
                    if [ $fastcgi = true ];
                    then
                            sudo -u ${user} ${script_path}/seahub.sh ${1}-fastcgi ${fastcgi_port} >> ${seahub_init_log}
                    else
                            sudo -u ${user} ${script_path}/seahub.sh ${1} >> ${seahub_init_log}
                    fi
            ;;
            restart)
                    sudo -u ${user} ${script_path}/seafile.sh ${1} >> ${seafile_init_log}
                    if [ $fastcgi = true ];
                    then
                            sudo -u ${user} ${script_path}/seahub.sh ${1}-fastcgi ${fastcgi_port} >> ${seahub_init_log}
                    else
                            sudo -u ${user} ${script_path}/seahub.sh ${1} >> ${seahub_init_log}
                    fi
            ;;
            stop)
                    sudo -u ${user} ${script_path}/seahub.sh ${1} >> ${seahub_init_log}
                    sudo -u ${user} ${script_path}/seafile.sh ${1} >> ${seafile_init_log}
            ;;
            *)
                    echo "Usage: /etc/init.d/seafile-server {start|stop|restart}"
                    exit 1
            ;;
    esac

**Note**:

1.  If you want to start seahub in fastcgi, just change the **fastcgi**
    variable to **true**
2.  If you deployed Seafile with MySQL, append "mysql" to the
    Required-Start line:

<!-- -->

    # Required-Start: $local_fs $remote_fs $network mysql

### Add Directory for Logfiles

     mkdir /path/to/seafile/dir/logs

### Make the seafile-sever script executable

    sudo chmod +x /etc/init.d/seafile-server

### Add seafile-server to rc.d

    sudo update-rc.d seafile-server defaults

### Done

Don't forget to update the value of **seafile\_dir** later if you update
your seafile server.

RHEL/CentOS
-----------

On RHEL/CentOS, the script
[/etc/rc.local](http://www.centos.org/docs/5/html/Installation_Guide-en-US/s1-boot-init-shutdown-run-boot.html)
is executed by the system at bootup, so we start seafile/seahub there.

-   Locate your python executable (python 2.6 or 2.7)

<!-- -->

    which python2.6 # or "which python2.7"

-   In /etc/rc.local, add the directory of python2.6(2.7) to **PATH**,
    and add the seafile/seahub start command

<!-- -->

    `
    # Assume the python 2.6(2.7) executable is in "/usr/local/bin"
    PATH=$PATH:/usr/local/bin/

    # Change the value of "user" to your linux user name
    user=haiwen

    # Change the value of "seafile_dir" to your path of seafile installation
    # usually the home directory of $user
    seafile_dir=/data/haiwen
    script_path=${seafile_dir}/seafile-server-latest

    sudo -u ${user} ${script_path}/seafile.sh start > /tmp/seafile.init.log 2>&1
    sudo -u ${user} ${script_path}/seahub.sh start > /tmp/seahub.init.log 2>&1

**Note**: If you want to start seahub in fastcgi, just change the
**"seahub.sh start"** in the last line above to **"seahub.sh
start-fastcgi"**

-   Done. Don't forget to update the value of **seafile\_dir** later if
    you update your seafile server.

RHEL/CentOS (run as service)
----------------------------

On RHEL/CentOS we make use of the /etc/init.d/ scripts to start
seafile/seahub at system boot as service.

### Create a file **/etc/sysconfig/seafile**

    # Change the value of "user" to your linux user name
    user=haiwen

    # Change the value of "seafile_dir" to your path of seafile installation
    # usually the home directory of $user
    seafile_dir=/data/haiwen
    script_path=${seafile_dir}/seafile-server-latest
    seafile_init_log=${seafile_dir}/logs/seafile.init.log
    seahub_init_log=${seafile_dir}/logs/seahub.init.log

    # Change the value of fastcgi to true if fastcgi is to be used
    fastcgi=false

    # Set the port of fastcgi, default is 8000. Change it if you need different.
    fastcgi_port=8000


### Create a script **/etc/init.d/seafile**

    #!/bin/bash
    #
    # seafile

    #
    # chkconfig: - 68 32
    # description: seafile

    # Source function library.
    . /etc/init.d/functions

    # Source networking configuration.
    . /etc/sysconfig/network

    if [ -f /etc/sysconfig/seafile ];then
            . /etc/sysconfig/seafile
            else
                echo "Config file /etc/sysconfig/seafile not found! Bye."
                exit 200
            fi

    RETVAL=0

    start() {
            # Start daemons.
            echo -n $"Starting seafile: "
            ulimit -n 30000
            su - ${user} -c"${script_path}/seafile.sh start >> ${seafile_init_log} 2>&1"
            RETVAL=$?
            echo
            [ $RETVAL -eq 0 ] && touch /var/lock/subsys/seafile
            return $RETVAL
    }

    stop() {
            echo -n $"Shutting down seafile: "
            su - ${user} -c"${script_path}/seafile.sh stop >> ${seafile_init_log} 2>&1"
            RETVAL=$?
            echo
            [ $RETVAL -eq 0 ] && rm -f /var/lock/subsys/seafile
            return $RETVAL
    }

    #
    # Write a polite log message with date and time
    #
    echo -e "\n \n About to perform $1 for seafile at `date -Iseconds` \n " >> ${seafile_init_log}

    # See how we were called.
    case "$1" in
      start)
            start
            ;;
      stop)
            stop
            ;;
      restart|reload)
            stop
            start
            RETVAL=$?
            ;;
      *)
            echo $"Usage: $0 {start|stop|restart}"
            RETVAL=3
    esac

    exit $RETVAL

### Create a script **/etc/init.d/seahub**

    #!/bin/bash
    #
    # seahub

    #
    # chkconfig: - 69 31
    # description: seahub

    # Source function library.
    . /etc/init.d/functions

    # Source networking configuration.
    . /etc/sysconfig/network

    if [ -f /etc/sysconfig/seafile ];then
            . /etc/sysconfig/seafile
            else
                echo "Config file /etc/sysconfig/seafile not found! Bye."
                exit 200
            fi

    RETVAL=0

    start() {
            # Start daemons.
            echo -n $"Starting seahub: "
            ulimit -n 30000
            if [  $fastcgi = true ];
                    then
                    su - ${user} -c"${script_path}/seahub.sh start-fastcgi ${fastcgi_port} >> ${seahub_init_log} 2>&1"
                    else
                    su - ${user} -c"${script_path}/seahub.sh start >> ${seahub_init_log} 2>&1"
                    fi
            RETVAL=$?
            echo
            [ $RETVAL -eq 0 ] && touch /var/lock/subsys/seahub
            return $RETVAL
    }

    stop() {
            echo -n $"Shutting down seahub: "
            su - ${user} -c"${script_path}/seahub.sh stop >> ${seahub_init_log} 2>&1"
            RETVAL=$?
            echo
            [ $RETVAL -eq 0 ] && rm -f /var/lock/subsys/seahub
            return $RETVAL
    }

    #
    # Write a polite log message with date and time
    #
    echo -e "\n \n About to perform $1 for seahub at `date -Iseconds` \n " >> ${seahub_init_log}

    # See how we were called.
    case "$1" in
      start)
            start
            ;;
      stop)
            stop
            ;;
      restart|reload)
            stop
            start
            RETVAL=$?
            ;;
      *)
            echo $"Usage: $0 {start|stop|restart}"
            RETVAL=3
    esac

    exit $RETVAL

Next, enable services:

    chmod 550 /etc/init.d/seafile
    chmod 550 /etc/init.d/seahub
    chkconfig --add seafile
    chkconfig --add seahub
    chkconfig seahub on
    chkconfig seafile on

and run:

    service seafile start
    service seahub start
