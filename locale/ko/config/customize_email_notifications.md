# 전자메일 알림 개별 설정

**참고:** 제목 줄은 개정판 별로 바뀔 수 있습니다. 이 도움말은 2.0.1 개정판을 기반으로 합니다. Seahub를 다시 시작하여 바꾼 설정 값을 적용하십시오.

## 사용자 암호 재설정 ##

**제목**

seahub/seahub/auth/forms.py 103번째 줄

**본문**

seahub/seahub/templates/registration/password_reset_email.html

참고: password_reset_email.html 파일을 `seahub-data/custom/templates/registration/password_reset_email.html`에 복사하고 새로운 내용으로 수정할 수 있습니다. 이 방식으로 업그레이드 한 후에도 개별 설정 값을 유지할 수 있습니다. 

## 시스템 관리자의 새 구성원 추가 ##

**제목**

seahub/seahub/views/sysadmin.py 424번째 줄

**본문**

seahub/seahub/templates/sysadmin/user_add_email.html

참고: user_add_email.html 파일을 `seahub-data/custom/templates/sysadmin/user_add_email.html`에 복사하고 새로운 내용으로 수정할 수 있습니다. 이 방식으로 업그레이드 한 후에도 개별 설정 값을 유지할 수 있습니다. 

## 시스템 관리자의 사용자 암호 재설정 ##

**제목**

seahub/seahub/views/sysadmin.py 368번째 줄

**본문**

seahub/seahub/templates/sysadmin/user_reset_email.html

참고: user_reset_email.html 파일을 `seahub-data/custom/templates/sysadmin/user_reset_email.html`에 복사하고 새로운 내용으로 수정할 수 있습니다. 이 방식으로 업그레이드 한 후에도 개별 설정 값을 유지할 수 있습니다. 

## 사용자의 파일/폴더 공유 링크 전송 ##

**제목**

seahub/seahub/share/views.py 668번째 줄

**본문**

seahub/seahub/templates/shared_link_email.html

