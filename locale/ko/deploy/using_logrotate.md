# 서버에 logrotate 설정

## 동작 방식

seaf-server and ccnet-server now (since version 3.1) support reopenning logfile by receiving SIGUR1 signal.

This feature is very useful when you need cut logfile while you don't want to shutdown the server programs. All you need to do now is cutting the logfile on
the fly.

> **NOTE**: signal is not supported by windows, so the feature is not available in windows

## 기본 logrotate 설정 디렉터리

데비안에서 logrotate 기본 디렉터리는 ``/etc/logrotate.d/``입니다

## 예제 설정

Assuming your ccnet-server's logfile is `/home/haiwen/logs/ccnet.log`, and your ccnet-server's pidfile for ccnet-server is ``/home/haiwen/pids/ccnet.pid``.

Assuming your seaf-server's logfile is setup to ``/home/haiwen/logs/seaf-server.log``, and your seaf-server's pidfile for seaf-server is setup to ``/home/haiwen/pids/seaf-server.pid``:

logrotate 설정은 다음과 같을 수 있습니다:
```
/home/haiwen/logs/seaf-server.log
{
        daily
        missingok
        rotate 52
        compress
        delaycompress
        notifempty
        sharedscripts
        postrotate
                [ ! -f /home/haiwen/pids/seaf-server.pid ] || kill -USR1 `cat /home/haiwen/pids/seaf-server.pid`
        endscript
}

/home/haiwen/logs/ccnet.log
{
        daily
        missingok
        rotate 52
        compress
        delaycompress
        notifempty
        sharedscripts
        postrotate
                [ ! -f /home/haiwen/pids/ccnet.pid ] || kill -USR1 `cat /home/haiwen/pids/ccnet.pid`
        endscript
}
```

데비안의 경우, ``/etc/logrotate.d/seafile`` 파일로 저장할 수 있습니다

## 다 됐습니다

이제 설정이 다 끝났으니, 앉아서 푹 쉬세요 :-D

