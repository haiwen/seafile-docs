# 서버 설정 및 개별 설정

## 설정 파일

**중요**: Seafile 서버 5.0.0 부터 모든 설정 파일은 **conf** 폴더로 옮겨 모아놓습니다. [좀 더 읽어보십시오](../deploy/new_directory_layout_5_0_0.md).

커뮤니티판에는 세가지 설정 파일이 있습니다:

- [ccnet.conf](ccnet-conf.md): LDAP 설정이 들어있습니다
- [seafile.conf](seafile-conf.md): Seafile 데몬 및 파일 서버 설정이 들어있습니다.
- [seahub_settings.py](seahub_settings_py.md): Seahub 설정이 들어있습니다

전문가판에는 추가 설정 파일이 들어있습니다:

- `seafevents.conf`: 검색 및 문서 미리 보기 설정이 들어있습니다

참고: 5.0.0 버전 부터 대부분의 설정 항목은 웹 인터페이스에서 수정할 수 있습니다. 설정 항목은 데이터베이스 테이블(seahub_dab/constance_config)에 저장합니다. 설정 파일의 항목보다 높은 우선순위를 갖습니다.

![Seafile 웹에서 설정하기](../images/seafile-server-config.png)

## 설정 항목

전자메일:

* [전자메일 알림 전송](sending_email.md)
* [전자메일 알림 개별 설정](customize_email_notifications.md)

사용자 관리

* [사용자 관리 설정 항목](user_options.md)

사용자 저장 용량 제한 및 다운로드/업로드 파일 크기 제한

* [사용자 저장 용량 제한 및 다운로드/업로드 파일 크기 제한 설정 항목](quota_and_size_options.md)

## 웹 개별 설정

* [웹 인터페이스 개별 설정](seahub_customization.md)

