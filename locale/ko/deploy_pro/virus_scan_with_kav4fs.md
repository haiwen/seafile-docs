# kav4fs로 바이러스 검사

## 준비

Seafile 서버 머신에서 리눅스 파일 서버용 카스퍼스키 바이러스 예방 프로그램을 설치했다고 가정하겠습니다.

Seafile 서버를 비 루트 계정으로 실행한다면 kav4fs-control을 실행할 때 암호 작성을 피하려는 목적으로 sudoers 권한을 주어야합니다. 다음 설정을 /etc/sudoers에 추가하십시오:

```
<user of running seafile server>\tALL=(ALL:ALL) ALL
<user of running seafile server> ALL=NOPASSWD: /opt/kaspersky/kav4fs/bin/kav4fs-control
```

## 스크립트

kav4fs의 반환 코드를 파일 검사 결과에 반영할 수 없기에, 검색 출력 해석에 셸 스크립트를 사용하겠습니다
검사 결과와 해석 결과 기반은 검사 결과를 반영하는 반환 코드를 다르게 반환합니다.

다음 내용을 `kav4fs_scan.sh`와 같은 이름으로 저장하십시오:

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

스크립트 실행 권한을 부여하십시오:

```
chmod u+x kav4fs_scan.sh
```

스크립트 반환 코드 값의 의미는 다음과 같습니다:

```
1: found virus
0: no virus
other: scan failed
```

## 설정

다음 설정 항목을 `seafile.conf`에 추가하십시오:

```
[virus_scan]
scan_command = <absolute path of kav4fs_scan.sh>
virus_code = 1
nonvirus_code = 0
scan_interval = <scanning interval, in unit of minutes, default to 60 minutes>
```

