# Seafile에 디렉터리 가져오기

5.1.3 전문가판부터 서버의 로컬 디렉터리를 Seafile로 가져오는 기능을 지원합니다. 시스템 관리자가 기존 파일 서버(NFS, 삼바 등)에서 파일을 가져올 때 쓸만한 도구입니다.

디렉터리를 가져오려면 seafile-server-latest 디렉터리에서 `seaf-import.sh` 스크립트를 사용하십시오.

```
usage :
seaf-import.sh
 -p <import dir path, must set>
 -n <repo name, must set>
 -u <repo owner, must set>
```

지정 디렉터리는 Seafile에 라이브러리로 가져옵니다. 가져온 라이브러리의 이름과 소유자를 설정할 수 있습니다.

`./seaf-import.sh -p <dir you want to import> -n <repo name> -u <repo owner>`를 실행하십시오,

```
Starting seaf-import, please wait ...
[04/26/16 03:36:23] seaf-import.c(79): Import file ./runtime/seahub.pid successfully.
[04/26/16 03:36:23] seaf-import.c(79): Import file ./runtime/error.log successfully.
[04/26/16 03:36:23] seaf-import.c(79): Import file ./runtime/seahub.conf successfully.
[04/26/16 03:36:23] seaf-import.c(79): Import file ./runtime/access.log successfully.
[04/26/16 03:36:23] seaf-import.c(183): Import dir ./runtime/ to repo 5ffb1f43 successfully.
 run done
Done.
```

지정 라이브러리 소유자로 Seafile 서버에 로그인하시면 지정 이름을 가진 새 라이브러리를 찾을 수 있습니다.

