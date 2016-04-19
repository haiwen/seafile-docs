# Seafile CLI

init
----
설정 파일을 초기화합니다

사용법: seaf-cli -c <설정-디렉터리> -o init

start
-----
seafile 클라이언트를 실행하려면 seafile-applet을 시작하십시오

사용법: seaf-cli -c <설정-디렉터리> -o start

start-ccnet
-----------
ccnet 데몬을 시작하십시오

사용법: seaf-cli -c <설정-디렉터리> -o start-ccnet

start-seafile
-------------
seafile 데몬을 시작하십시오

사용법: seaf-cli -c <설정-디렉터리> [-w <작업트리>] -o start-seafile

clone
-----
seafile 서버의 저장소를 복제합니다

이 프로그램에서 저장소 정보를 가져올 때 seafile 웹 API v2을 활용하므로 저장소 ID와 URL값을 지정해야합니다.

사용법: seaf-cli -c <설정-디렉터리> -r <저장소-ID> -u <URL> [-w <작업트리>] -o clone

sync
----
저장소 동기화를 시도합니다

사용법: seaf-cli -c <설정-디렉터리> -r <저장소-ID> -o clone

remove
------
저장소 동기화 관계를 끊습니다

사용법: seaf-cli -c <설정-디렉터리> -r <저장소-ID> -o remove

## 사용법

하위 명령:

    init:           seafile 클라이언트 설정 파일을 만듭니다
    start:          Seafile 클라이언트를 데몬으로 시작하고 실행합니다
    stop:           seafile 클라이언트를 멈춥니다
    list:           로컬 라이브러리를 나타냅니다
    status:         동기화 상태를 표시합니다
    download:       seafile 서버에서 라이브러리를 다운로드합니다
    sync:           seafile 서버에 있는 라이브러리의 폴더를 동기화합니다
    desync:         seafile 서버와의 라이브러리 동기화를 해제합니다


## 더 자세한 내용

Seafile 클라이언트의 모든 설정 정보는 설정 디렉터리에 저장합니다. 기본 위치는 `~/.ccnet` 입니다. 하단의 모든 명령은 `-c <설정-디렉터리>` 설정을 받아들입니다.

init
----
seafile 클라이언트를 초기화합니다. 이 명령은 `상위-디렉터리`에 `seafile-data`와 `seafile` 하위 디렉터리를 만듭니다. `seafile-data`는 내부 데이터 저장에 활용하며 `seafile`은 다운로드한 라이브러리의 기본 위치로 활용합니다.

    seaf-cli init [-c <설정-디렉터리>] -d <상위-디렉터리>

start
-----
Seafile 클라이언트를 시작합니다. 이 명령은 `ccnet`, `seaf-daemon`, seafile 클라이언트의 네트워크 기능을 담당하는 `ccnet`, 파일을 관리하는 `seaf-daemon`을 시작합니다.

    seaf-cli start [-c <설정-디렉터리>]

stop
----
seafile 클라이언트를 멈춥니다.

    seaf-cli stop [-c <설정-디렉터리>]


download
--------
seafile 서버에서 라이브러리를 다운로드합니다

    seaf-cli download -l <라이브러리-ID> -s <seahub-server-url> -d <상위-디렉터리> -u <사용자이름> [-p <암호>]


sync
----
기존 폴더에 라이브러리를 동기화합니다.

    seaf-cli sync -l <라이브러리-ID> -s <seahub-서버-URL> -d <기존-폴더> -u <사용자이름> [-p <암호>]

desync
------
seafile 서버의 라이브러리 동기화 관계를 끊습니다

    seaf-cli desync -d <기존-폴더>

