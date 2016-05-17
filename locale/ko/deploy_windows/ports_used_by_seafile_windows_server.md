# Seafile 윈도우 서버에서 사용하는 포트

Seafile 서버의 구성 요소는 두 부분이기에, TCP 포트 두개를 사용합니다.

## 두 설정 파일

설정에 관련된 모든 포트는 ``ccnet.conf``와 ``seafile.conf``에 적어두었습니다.
### ``ccnet.conf`` 열기

- Seafile 서버 트레이 아이콘에 마우스 커서를 두고 오른쪽 단추를 누른 후 __seafile-server 폴더 열기__를 선택하십시오
-  ``seafile-server`` 폴더의 ``ccnet`` 폴더를 여십시오. 해당 위치에 ``ccnet.conf`` 파일이 있습니다.

### ``seafile.conf`` 열기

- Seafile 서버 트레이 아이콘에 마우스 커서를 두고 오른쪽 단추를 누른 후 __seafile-server 폴더 열기__를 선택하십시오
- ``seafile-server`` 폴더의 ``seafile-data`` 폴더를 여십시오. 해당 위치에 ``seafile.conf`` 파일이 있습니다.

다음 섹션에서는 Seafile의 각 구성 요소가 사용하는 TCP 포트를 확인하고, 또한 이 설정을 어떻게 바꾸는지도 알아보겠습니다(예를 들면, 일부 포트 설정은 다른 프로그램에서 이미 사용하고 있을지도 모릅니다).

**참고**: 어떤 포트 설정이든 바꾸면 Seafile 서버를 다시 시작해야합니다.

## seafile fileserver

Seafile FileServer는 Seahub의 원시 파일 업로드/다운로드를 처리합니다

- 기본값: 8082
- 포트 바꾸기: Seafile 데스크톱 클라이언트에서는 파일 동기화 목적으로 연결시 이 포트 번호를 활용합니다. 이 포트 설정을 바꾸지 마십시오.

## seahub

Seahub는 Seafile 서버의 웹 인터페이스입니다.

**참고**: Seahub의 포트 설정을 바꾸면 ``ccnet.conf``의 ``SERVICE_URL`` 값을 바꾸어야 합니다.

- 기본값: 8000
- 포트 바꾸기: ``seafile.conf`` 파일을 편집하십시오. Seahub 섹션에 있는 포트 값을 바꾸십시오. (Seafile 윈도우 서버 1.7.0.1에 추가했습니다)

```
[seahub]
port=8000
```
- ``ccnet.conf`` 파일을 편집하여 ``SERVICE_URL`` 값을 올바르게 수정하십시오. 예를 들어 포트를 8001로 바꾸었다면, ``SERVICE_URL`` 값을 이에 맞춰 올바르게 수정하십시오:

```
[General]
SERVICE_URL = <Your IP OR DOMAIN>:8001
```

