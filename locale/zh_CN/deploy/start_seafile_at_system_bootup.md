# Start Seafile at System Bootup

For Ubuntu
----------

On Ubuntu, we make use of the [/etc/init.d/](https://help.ubuntu.com/community/UbuntuBootupHowto) scripts to start seafile/seahub at system boot.

### Create a script **/etc/init.d/seafile-server**

    sudo vim /etc/init.d/seafile-server

脚本内容为: (同时需要修改相应的 **user** 和 **seafile\_dir** 字段的值)

    #!/bin/bash

    # 请将 user 改为你的Linux用户名
    user=haiwen

    # 请将 script_dir 改为你的 Seafile 文件安装路径
    # usually the home directory of $user
    seafile_dir=/data/haiwen
    script_path=${seafile_dir}/seafile-server-latest
    seafile_init_log=${seafile_dir}/logs/seafile.init.log
    seahub_init_log=${seafile_dir}/logs/seahub.init.log

    # 若使用 Nginx/Apache, 请将其设置为true, 否者为 false
    fastcgi=true
    # fastcgi 端口, 默认为 8000.
    fastcgi_port=8000
    #
    # Write a polite log message with date and time
    #
    echo -e "\
 \
 About to perform $1 for seafile at `date -Iseconds` \
 " >> ${seafile_init_log}    echo -e "\
 \
 About to perform $1 for seahub at `date -Iseconds` \
 " >> ${seahub_init_log}    case "$1" in
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



### 创建 **/etc/init/seafile-server.conf** 文件

#### If you're not using MySQL or an external MySQL server

    start on (runlevel [2345])
    stop on (runlevel [016])

    pre-start script
    /etc/init.d/seafile-server start
    end script

    post-stop script
    /etc/init.d/seafile-server stop
    end script

#### If you're using MySQL

    start on (started mysql
    and runlevel [2345])
    stop on (runlevel [016])

    pre-start script
    /etc/init.d/seafile-server start
    end script

    post-stop script
    /etc/init.d/seafile-server stop
    end script

### 设置 seafile-sever 脚本为可执行文件

    sudo chmod +x /etc/init.d/seafile-server

### 完成

Don't forget to update the value of **script\_path** later if you update your seafile server.

其他 Debian 系的 Linux 下
----------------------------

### Create a script **/etc/init.d/seafile-server**

    sudo vim /etc/init.d/seafile-server

脚本内容为: (同时需要修改相应的 **user** 和 **seafile\_dir** 字段的值)

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

    # 请将 user 改为你的Linux用户名
    user=haiwen

    # 请将 script_dir 改为你的 Seafile 文件安装路径
    # usually the home directory of $user
    seafile_dir=/data/haiwen
    script_path=${seafile_dir}/seafile-server-latest
    seafile_init_log=${seafile_dir}/logs/seafile.init.log
    seahub_init_log=${seafile_dir}/logs/seahub.init.log

    # 若使用 fastcgi, 请将其设置为true
    fastcgi=false
    # fastcgi 端口, 默认为 8000.
    fastcgi_port=8000

    #
    # Write a polite log message with date and time
    #
    echo -e "\
 \
 About to perform $1 for seafile at `date -Iseconds` \
 " >> ${seafile_init_log}    echo -e "\
 \
 About to perform $1 for seahub at `date -Iseconds` \
 " >> ${seahub_init_log}    case "$1" in
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

1.  If you want to start seahub in fastcgi, just change the **fastcgi** variable to **true**
2.  If you deployed Seafile with MySQL, append "mysql" to the Required-Start line:

<!-- -->

    # Required-Start: $local_fs $remote_fs $network mysql

### Add Directory for Logfiles

     mkdir /path/to/seafile/dir/logs

### 设置 seafile-sever 脚本为可执行文件

    sudo chmod +x /etc/init.d/seafile-server

### Add seafile-server to rc.d

    sudo update-rc.d seafile-server defaults

### 完成

Don't forget to update the value of **seafile\_dir** later if you update your seafile server.

For RHEL/CentOS
---------------

On RHEL/CentOS, the script [/etc/rc.local](http://www.centos.org/docs/5/html/Installation_Guide-en-US/s1-boot-init-shutdown-run-boot.html) is executed by the system at bootup, so we start seafile/seahub there.

-   Locate your python executable (python 2.6 or 2.7)

<!-- -->

    which python2.6 # or "which python2.7"

-   In /etc/rc.local, add the directory of python2.6(2.7) to **PATH**, and add the seafile/seahub start command

<!-- -->

    `
    # Assume the python 2.6(2.7) executable is in "/usr/local/bin"
    PATH=$PATH:/usr/local/bin/

    # 请将 user 改为你的Linux用户名
    user=haiwen

    # 请将 script_dir 改为你的 Seafile 文件安装路径
    # usually the home directory of $user
    seafile_dir=/data/haiwen
    script_path=${seafile_dir}/seafile-server-latest

    sudo -u ${user} ${script_path}/seafile.sh start > /tmp/seafile.init.log 2>&1
    sudo -u ${user} ${script_path}/seahub.sh start > /tmp/seahub.init.log 2>&1

**Note**: If you want to start seahub in fastcgi, just change the **"seahub.sh start"** in the last line above to **"seahub.sh start-fastcgi"**

-   Done. Don't forget to update the value of **seafile\_dir** later if you update your seafile server.

For RHEL/CentOS run as service
------------------------------

On RHEL/CentOS , we make use of the /etc/init.d/ scripts to start seafile/seahub at system boot as service.

### 创建 **/etc/sysconfig/seafile** 文件

    # 请将 user 改为你的Linux用户名
    user=haiwen

    # 请将 script_dir 改为你的 Seafile 文件安装路径
    # usually the home directory of $user
    seafile_dir=/data/haiwen
    script_path=${seafile_dir}/seafile-server-latest
    seafile_init_log=${seafile_dir}/logs/seafile.init.log
    seahub_init_log=${seafile_dir}/logs/seahub.init.log

    # 若使用 fastcgi, 请将其设置为true
    fastcgi=false

    # fastcgi 端口, 默认为 8000.
    fastcgi_port=8000


### 创建 **/etc/init.d/seafile** 文件

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
    echo -e "\
 \
 About to perform $1 for seafile at `date -Iseconds` \
 " >> ${seafile_init_log}    # See how we were called.
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

### 创建**/etc/init.d/seahub**脚本

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
    echo -e "\
 \
 About to perform $1 for seahub at `date -Iseconds` \
 " >> ${seahub_init_log}    # See how we were called.
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

接下来启动服务程序:

    chmod 550 /etc/init.d/seafile
    chmod 550 /etc/init.d/seahub
    chkconfig --add seafile
    chkconfig --add seahub
    chkconfig seahub on
    chkconfig seafile on

执行:

    service seafile start
    service seahub start

For systems running systemd
---------------------------

Create systemd service files, change **${seafile\_dir}** to your **seafile** installation location and **seafile** to user, who runs **seafile** (if appropriate). Then you need to reload systemd's daemons: **systemctl daemon-reload**.

### Create systemd service file /etc/systemd/system/seafile.service

    [Unit]
    Description=Seafile
    # add mysql.service or postgresql.service depending on your database to the line below
    After=network.target

    [Service]
    Type=oneshot
    ExecStart=${seafile_dir}/seafile-server-latest/seafile.sh start
    ExecStop=${seafile_dir}/seafile-server-latest/seafile.sh stop
    RemainAfterExit=yes
    User=seafile
    Group=seafile

    [Install]
    WantedBy=multi-user.target

### Create systemd service file /etc/systemd/system/seahub.service

    [Unit]
    Description=Seafile hub
    After=network.target seafile.service

    [Service]
    # change start to start-fastcgi if you want to run fastcgi
    ExecStart=${seafile_dir}/seafile-server-latest/seahub.sh start
    ExecStop=${seafile_dir}/seafile-server-latest/seahub.sh stop
    User=seafile
    Group=seafile
    Type=oneshot
    RemainAfterExit=yes

    [Install]
    WantedBy=multi-user.target

### Create systemd service file /etc/systemd/system/seafile-client.service (optional)

You need to create this service file only if you have **seafile** console client and you want to run it on system boot.

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

### 完成

