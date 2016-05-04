# Seafile 윈도우 서버 다운로드 및 설치

## 다운로드/압축 해제
### 파이썬 2.7.4 32비트 버전 설치

- [파이썬 2.7.4 32비트 버전](http://python.org/ftp/python/2.7.4/python-2.7.4.msi)을 다운로드하고 설치하십시오
- 파이썬 2.7의 설치 경로를 시스템 PATH 환경 변수에 추가하십시오. 파이썬 2.7을 ``C:\Python27``에 설치했다면 PATH 환경 변수에 ``C:\Python27``을 추가하십시오


**경고**: 파이썬 2.7.4 32비트 버전을 사용하는지 확인하십시오. 64비트 버전이거나 다른 버전에서는 동작하지 않습니다.

### Seafile 서버 다운로드 및 압축 해제

- Seafile 서버 프로그램 최신 버전을 가져오십시오
- ``C:\SeafileProgram\``과 같이 Seafile 프로그램을 저장할 새 폴더를 만드십시오. 폴더 위치를 기억하십시오. 나중에 활용합니다.
-  ``seafile-server_5.0.3_win32.tar.gz`` 파일을 ``C:\SeafileProgram\`` 폴더에 압축 해제하십시오

이제 폴더 구성은 다음과 같아야합니다:
```sh
C:\SeafileProgram
         |__ seafile-server-5.0.3
```
## 시작/초기화

### Seafile 서버 시작

``C:\SeafileProgram\seafile-server-5.0.3\`` 폴더로 이동한 후 run.bat를 두 번 눌러 Seafile 서버를 시작하십시오. Seafile 아이콘이 상태 표시줄에 나타나야합니다.
Seafile 서버 데이터를 저장할 디스크를 선택하십시오

이제 Seafile 서버의 데이터를 저장할 디스크를 물어보는 대화상자가 뜹니다

- 충분한 공간이 남아있는 디스크를 선택하십시오
- 확인 단추를 누르면 Seafile은 선택한 디스크에 seafile-server 폴더를 만듭니다. 이 폴더는 Seafile 서버의 데이터 폴더입니다. D 디스크를 선택했다면 ``D:\seafile-server`` 데이터 폴더가 나타납니다

### admin 계정 추가

Seafile 서버의 상태 표시줄 아이콘에 마우스 커서를 가져다 두고 오른쪽 단추를 누른 후 __관리자 추가__를 선택하십시오. 관리 사용자 이름 및 암호를 프롬프트 대화상자에 입력하십시오.

과정이 끝나면 상태 표시줄 아이콘의 풍선 도움말 상자에 __관리자 계정을 성공적으로 추가했습니다__ 라고 나타납니다

### Seafile 서버 설정

초기화 후, 설정해야 할 몇가지 항목이 있습니다:

- 상태 표시줄 아이콘에 마우스 커서를 가져다 두고 오른쪽 단추를 누른 후 __seafile-server 폴더 열기__를 선택하십시오. seafile-server 데이더 폴더를 엽니다.
- `conf/ccnet.conf` 파일을 편집하여 `ccnet.conf`의 다음 줄을 수정하십시오:
```
SERVICE_URL = XXX
```

- `SERVICE_URL` 값을 `http://<your ip address>:8000`으로 바꾸십시오. 윈도우 서버의 IP 주소가 192.168.1.100이라면, `SERVICE_URL = http://192.168.1.100:8000`으로 바꾸십시오

편집이 끝난 후 상태 표시줄 아이콘에 마우스 커서를 가져다 둔 후 오른쪽 단추를 누르고 __Seafile 다시 시작__을 선택하십시오

### Seahub 방문

브라우저를 열고 `http://127.0.0.1:8000` 주소에 들어가십시오. admin 계정으로 로그인하십시오. 로그인할 수 있다면 초기화는 성공한 상태입니다.
설정 완료

Seafile 서버 설정이 끝났습니다. 클라이언트 사용법은 Seafile 클라이언트 설명서를 참고하십시오

### 다음 문서를 읽어보시면 좋습니다:

- [Seafile과 MySQL 가동](deploy_with_mysql.md)
- [Seafile과 Apache 가동](deploy_with_apache.md)
- [Seafile과 Nginx 가동](deploy_with_nginx.md)
- [LDAP 통합](../deploy/using_ldap.md)
- [Seafile 서버를 윈도우 서비스로 설치](install_seafile_server_as_a_windows_service.md)
- [Seafile 윈도우 서버에서 사용하는 포트](ports_used_by_seafile_windows_server.md)
- [Seafile 윈도우 서버 업그레이드](upgrading_seafile_windows_server.md)
- [설정 항목 및 개별 설정](../deploy/server_configuration.md)

