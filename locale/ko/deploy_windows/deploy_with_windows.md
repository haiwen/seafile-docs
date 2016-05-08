# 윈도우에서 가동

## 설치 및 업그레이드

Seafile 윈도우 커뮤니티판은 SQLite/MySQL 데이터베이스를 지원합니다.

- [Seafile 윈도우 서버 다운로드 및 설치](download_and_setup_seafile_windows_server.md)
- [Seafile과 MySQL 가동](deploy_with_mysql.md)
- [Seafile과 Apache 가동](deploy_with_apache.md)
- [Seafile과 Nginx 가동](deploy_with_nginx.md)
- [LDAP 통합](../deploy/using_ldap.md)
- [Seafile 서버를 윈도우 서비스로 설치](install_seafile_server_as_a_windows_service.md)
- [Seafile 윈도우 서버에서 사용하는 포트](ports_used_by_seafile_windows_server.md)
- [Seafile 윈도우 서버 업그레이드](upgrading_seafile_windows_server.md)
- [설정 항목 및 개별 설정](../config/README.md)

Seafile 서버에 대한 자세한 내용은, [Seafile 리눅스 버전](../deploy/README.md) 문서를 확인하십시오

## 서버 관리

- [Seafile 서버에서 사용하지 않는 블록 가비지 수집](windows_gc.md)
- [손상된 저장소에서 seaf-fsck 실행](windows_fsck.md)

## 일반 문제

Seafile 서버 설치에 실패했다면 seafserv-applet.log를 우선 확인하십시오.
### "ERROR: D:/seafile-server\seahub.db not found"

이 파일은 Seafile 초기화 과정에서 만듭니다. 다음 과정을 행하십시오:

- 파이썬 및 파이썬 ``PATH`` 값을 올바르게 설정했는지 확인하십시오.
- Seafile 서버 꾸러미를 ``C:\seafile-packages``와 같은 단순 경로에 복사하십시오.

### seahub.db 만들기 실패

파이쏜 2.7.4 32비트 버전을 쓰시고 3 이상의 버전은 사용하지 마십시오.
### 웹 인터페이스에서 파일 업로드/다운로드가 안됩니다

ccnet.conf에서 ``SERVICE_URL``을 수정했는지 확인하십시오.

### 브라우저에서 css 및 자바스크립트 파일이 안뜹니다

- 파이썬 2.7.4 32비트 버전을 사용하십시오. 다른 파이썬 버전을 설치했다면, 설치를 제거하고 파이썬 2.7.4를 설치하십시오. Seafile 서버를 다시 시작하여 문제를 해결했는지 확인하십시오.
- 레지스트리 경로 형식 ``HKEY_CLASSES_ROOT\MIME\Database\Content``에서 비 아스키 키를 삭제하고 다시 시도하십시오.

