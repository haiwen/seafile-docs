# 서버에 logrotate 설정

## 동작 방식

seaf-server 및 ccnet-server은 이제(3.1 버전 부터) SIGUR1 시그널을 받았을 때 로그 파일을 다시 여는 기능을 지원합니다.

이 기능은 서버 프로그램을 끄지 않고 로그 파일을 자르고 싶을 때 쓸만합니다. 여기서 필요한 동작은 실행 중 로그 파일을 자르는 일 하나 뿐입니다.

> **참고**: 시그널은 윈도우에서 지원하지 않으므로 윈도우에서 사용할 수 없습니다

## 기본 logrotate 설정 디렉터리

데비안에서 logrotate 기본 디렉터리는 ``/etc/logrotate.d/``입니다

## 예제 설정

ccnet-server의 로그 파일은 `/home/haiwen/logs/ccnet.log`, pid 파일은 ``/home/haiwen/pids/ccnet.pid``라고 가정합니다.

seaf-server의 로그 파일은 ``/home/haiwen/logs/seaf-server.log``, pid 파일은 ``/home/haiwen/pids/seaf-server.pid``라고 가정합니다:

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

