# Seafile 윈도우 서버 업그레이드

- 부 버전 업그레이드
- 주 버전 업그레이드
- 윈도우 서비스 업그레이드

**참고**: 업그레이드를 진행하기 전 Seafile 서버 가동을 멈추어야합니다.
## Seafile 서버 새 버전 압축 해제

업그레이드 전 다음 디렉터리 구조 상태라고 가정합니다:
```
C:/SeafileProgram
             |______ seafile-server-3.0.0/
```
이 때 첫단계에서 할 일은 Seafile 서버 새 버전을 다운로드하고 ``C:/SeafileProgram``에 압축 해제하는 일입니다. 이 과정이 끝난 후 디렉터리 구조는 다음과 같습니다:
```
C:/SeafileProgram
             |______ seafile-server-3.0.0/
             |______ seafile-server-3.1.0/
```
## 부 버전 업그레이드(3.0.0에서 3.0.1로 업그레이드하는 방식)

Seafile 윈도우 서버를 3.0.0에서 3.0.1로 업그레이드 한다고 가정하겠습니다
### 아바타 폴더 내용 이동

``seafile-server-3.0.0/seahub/media/avatars`` 폴더로 이동하십시오

``avatars`` 폴더에는 Seafile 사용자가 업로드한 모든 아바타가 있습니다.

``foo@foo.com`` 사용자가 있다면, 이 폴더의 하위 폴더 ``foo@foo.com``을 찾을 수 있습니다. 하위 폴더에는 사용자 ``foo@foo.com``의 아바타 그림이 들어있습니다.

``foo@foo.com``과 같은 모든 하위 폴더를 ``seafile-server-3.0.1/seahub/media/avatars``에 복사하십시오. 이리 하여 새 Seafile 서버 3.0.1을 시작하면 이 아바타를 올바르게 불러올 수 있습니다.
## 주 버전 업그레이드(3.0.0에서 3.1.0으로 업그레이드하는 방식)

Seafile 윈도우 서버를 3.0.x에서 3.1.y로 업그레이드한다고 가정하겠습니다:

### 주 버전 업그레이드 스크립트 실행

데이터베이스 업그레이드 스크립트를 실행하십시오

- seafile-server-3.1.y/upgrade로 이동하십시오
- `upgrade_3.0_3.1.bat` 파일에 마우스 커서를 두고 오른쪽 단추를 누르십시오
- "관리자 권한으로 실행"을 선택하십시오

MySQL을 사용한다면 데이터베이스를 직접 업그레이드해야합니다:

- seafile-server-3.1.y/upgrade/sql/3.1.0/mysql/ 폴더로 이동하십시오
- `ccnet.sql` 파일이 있다면, `ccnet-db` 데이터베이스에 대해 다음 명령을 실행하십시오
```
mysql ccnet-db < ccnet.sql
```
- `seafile.sql` 파일이 있다면, `seafile-db` 데이터베이스에 대해 다음 명령을 실행하십시오
```
mysql ccnet-db < seafile.sql
```
- `seahub.sql` 파일이 있다면, `seahub-db` 데이터베이스에 대해 다음 명령을 실행하십시오
```
mysql seahub-db < seafile.sql
```

### 아바타 복사

``seafile-server-3.0.0/seahub/media/avatars``의 모든 하위 폴더를 ``seafile-server-3.1.0/seahub/media/avatars``에 복사하십시오
## 윈도우 서비스 업그레이드

Seafile 서버를 윈도우 서비스로 설치했다면 다음 과정을 진행해야합니다:

- Seafile 윈도우 서버의 이전 버전을 실행하고, 상태 표시줄 아이콘에 마우스 커서를 올려다 놓은 후 오른쪽 단추를 누르시고 메뉴의 윈도우 서비스 설치 제거를 선택하십시오
- Seafile 윈도우 서버 이전 버전에서 빠져나가십시오
- Seafile 윈도우 서버의 새 버전을 시작하시고, 상태 표시줄 아이콘에 마우스 커서를 올려다 놓은 후 오른쪽 단추를 누르시고 메뉴의 윈도우 서비스 설치를 선택하십시오

