# 시스템 부팅 시 Seafile 시작

우분투
----------

우분투에서, 시스템을 부팅할 때 seafile/seahub를 시작하는 [/etc/init.d/](https://help.ubuntu.com/community/UbuntuBootupHowto) 스크립트를 사용하도록 하겠습니다.

### **/etc/init.d/seafile-server** 스크립트 만들기

    sudo vim /etc/init.d/seafile-server

The content of this script is: (You need to modify the value of **user** and **seafile\_dir** accordingly)

    #!/bin/bash

    # Change the value of "user" to your linux user name
    user=haiwen

    # Change the value of "seafile_dir" to your path of seafile installation
    # usually the home directory of $user
    seafile_dir=/data/haiwen
    script_path=${seafile_dir}/seafile-server-latest
    seafile_init_log=${seafile_dir}/logs/seafile.init.log
    seahub_init_log=${seafile_dir}/logs/seahub.init.log

    # Change the value of fastcgi to falst if fastcgi is not used
    fastcgi=true
    # Set the port of fastcgi, default is 8000. Change it if you need different.
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



### **/etc/init/seafile-server.conf** 파일 만들기

#### MySQL 또는 외부 MySQL 서버를 사용하지 않는 경우

    start on (runlevel [2345])
    stop on (runlevel [016])

    pre-start script
    /etc/init.d/seafile-server start
    end script

    post-stop script
    /etc/init.d/seafile-server stop
    end script

#### MySQL을 사용하는 경우

    start on (started mysql
    and runlevel [2345])
    stop on (runlevel [016])

    pre-start script
    /etc/init.d/seafile-server start
    end script

    post-stop script
    /etc/init.d/seafile-server stop
    end script

### seafile-server 스크립트를 실행할 수 있게 만들기

    sudo chmod +x /etc/init.d/seafile-server

### 완료

Seafile 서버를 업데이트할 때  **script\_path** 값의 업데이트를 잊지 마십시오.

다른 데비안 기반 리눅스
----------------------------

### **/etc/init.d/seafile-server** 스크립트 만들기

    sudo vim /etc/init.d/seafile-server

The content of this script is: (You need to modify the value of **user** and **seafile\_dir** accordingly)

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

**참고**:

1. fastcgi 모드로 seahub를 시작하려면 **fastcgi** 변수 값을 **true**로 바꾸십시오
2. Seafile을 MySQL과 가동한다면 필요한 시작 줄에 "mysql"을 추가하십시오:

<!-- -->

    # Required-Start: $local_fs $remote_fs $network mysql

### 로그 파일용 디렉터리 추가

     mkdir /path/to/seafile/dir/logs

### seafile-server 스크립트를 실행할 수 있게 만들기

    sudo chmod +x /etc/init.d/seafile-server

### rc.d에 seafile-server 추가

    sudo update-rc.d seafile-server defaults

### 완료

Seafile 서버를 업데이트한 다음 **seafile\_dir** 값의 업데이트를 잊지 마십시오.

RHEL/CentOS
---------------

RHEL/CentOS에서, [/etc/rc.local](http://www.centos.org/docs/5/html/Installation_Guide-en-US/s1-boot-init-shutdown-run-boot.html)스크립트는 시스템을 부팅할 때 실행하여 seafile/seahub를 시작합니다.

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

**참고**: fastcgi 모드로 seahub를 시작하려면, 위 마지막 줄의 **"seahub.sh start"**를 **"seahub.sh start-fastcgi"**로 바꾸십시오

-   끝났습니다. Seafile 서버를 업데이트한 다음 **seafile\_dir** 값의 업데이트를 잊지 마십시오.

RHEL/CentOS 에서 서비스로 실행
------------------------------

RHEL/CentOS에서 시스템을 부팅할 때 seafile/seahub를 서비스로 가동하는 /etc/init.d/ 스크립트를 사용하도록 하겠습니다.

### **/etc/sysconfig/seafile** 파일 만들기

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


### **/etc/init.d/seafile** 스크립트 만들기

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

### **/etc/init.d/seahub** 스크립트 만들기

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

다음, 서비스를 활성화하신 후:

    chmod 550 /etc/init.d/seafile
    chmod 550 /etc/init.d/seahub
    chkconfig --add seafile
    chkconfig --add seahub
    chkconfig seahub on
    chkconfig seafile on

다음 명령을 실행하십시오:

    service seafile start
    service seahub start

systemd를 실행하는 시스템
---------------------------

systemd 서비스 파일을 만들고 **${seafile\_dir}** 경로를 **Seafile** 설치 경로로 바꾼 후, (적당하다면) **Seafile**을 실행하는 **seafile** 사용자를 만드십시오. 그 다음 systemd의 데몬을 다시 불러와야합니다: **systemctl daemon-reload**

### /etc/systemd/system/seafile.service systemd 서비스 파일 만들기

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

### /etc/systemd/system/seahub.service systemd 서비스 파일 만들기

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

### /etc/systemd/system/seafile-client.service systemd 서비스 파일 만들기(개별 선택)

시스템을 부팅할 때 **Seafile** 콘솔 클라이언트를 실행할 경우에만 이 서비스 파일을 만들어야합니다.

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

### 완료

