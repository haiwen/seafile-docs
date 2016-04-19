# Seahub의 전자 메일 알림 전송

## Seafile 의 전자메일 전송 형식

현재 Seafile에서 보내는 메일에는 다섯가지 형식이 있습니다:

- 사용자의 암호 재설정
- 시스템 관리자의 새 구성원 추가
- 시스템 관리자의 사용자 암호 재설정
- 사용자의 파일/폴더 공유 링크 및 업로드 링크 전송
- [전문가판] 읽지 않은 알림 전송(전문가판에서만 백그라운드 작업으로 전송)

처음 네가지 유형은 전자메일을 직접 보냅니다. 마지막 유형은 주기적으로 실행하는 백그라운드 작업으로 보냅니다.

## 전자메일 전송 설정 항목

seahub_settings.py에 다음 줄을 추가하여 전자메일 전송을 활성화하십시오.

<pre>
EMAIL_USE_TLS = False
EMAIL_HOST = 'smtp.example.com'        # smpt server
EMAIL_HOST_USER = 'username@example.com'    # username and domain
EMAIL_HOST_PASSWORD = 'password'    # password
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
</pre>

Gmail을 전자메일 서버로 사용한다면, 다음 줄을 추가하십시오:

<pre>
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'username@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
</pre>

**참고**: 전자메일 서비스가 여전히 동작하지 않는다면, <code>logs/seahub.log</code> 로그 파일을 보고 어디서 문제가 있는지 확인하십시오. 완전한 전자메일 알림 리스트 동작을 수행하려면 [전자메일 알림 리스트](customize_email_notifications.md)를 참고하십시오.

**참고2**: 인증 없이 전자메일 서비스를 사용한다면 <code>EMAIL_HOST_USER</code> 및 <code>EMAIL_HOST_PASSWORD</code> 값을 **비워**(<code>''</code>)두십시오(하지만 이렇게 하면 <code>From:</code> 주소 없이 전자메일을 보낼 수 있습니다).

**참고3**: SSL 연결 사용 정보(465번 포트 사용)

587번 포트는 전자메일 서버에 사용하는 TLS 연결 포트입니다. 465번 포트는 SSL 연결에 사용하는 포트입니다. 장고 1.8부터 모두를 지원합니다. 하지만 아직은 TLS 연결만 지원하는 장고 5.0을 사용합니다. 전자메일 서버에서 SSL 연결만 지원한다면 https://github.com/bancek/django-smtp-ssl 에서 소스코드를 찾아볼 수 있습니다.

## 전자메일의 `송신자` 및 `회신 주소` 바꾸기

전자메일의 송신자 및 회신 주소 부분을 seahub_settings.py의 다음 설정을 추가하여 바꿀 수 있습니다. 이 설정은 파일 공유 링크를 전자메일로 보낼 때만 유효합니다.

<pre>
# Replace default from email with user's email or not, defaults to ``False``
REPLACE_FROM_EMAIL = True

# Set reply-to header to user's email or not, defaults to ``False``. For details,
# please refer to http://www.w3.org/Protocols/rfc822/
ADD_REPLY_TO_HEADER = True
</pre>

## 백그라운드 전자메일 전송 작업 설정(전문가판 전용)

백그라운드 작업은 사용자에게 읽지 않은 새로운 알림이 있는지 주기적으로 실행하여 확인합니다. 만약 읽지 않은 알림이 있다면 사용자에게 알림 전자메일을 보냅니다. 백그라운드 전자메일 전송 작업은 `seafevents.conf`에서 설정합니다.

```
[SEAHUB EMAIL]

## must be "true" to enable user email notifications when there are new unread notifications
enabled = true

## interval of sending seahub email. Can be s(seconds), m(minutes), h(hours), d(days)
interval = 30m
```

## 전자메일 메시지 개별 설정

전자메일 메시지를 개별 설정하는 가장 단순한 방법은 seahub_settings.py의 `SITE_NAME`을 설정하는 방법입니다. 이게 충분하지 않은 경우라면 전자메일 양식을 개별 설정할 수 있습니다.

**참고**: 제목 줄은 각 개정판 별로 다를 수 있으며, 현재는 5.0.0 개정판을 기반으로 합니다. 바꾼 값을 적용하려면 Seahub를 다시 시작하십시오.

### 전자메일 기반 양식

[seahub/seahub/templates/email_base.html](https://github.com/haiwen/seahub/blob/master/seahub/templates/email_base.html)

참고: email_base.html 파일을 `seahub-data/custom/templates/email_base.html`에 복사하고 새로운 내용으로 수정할 수 있습니다. 이 방식으로 업그레이드 한 후에도 개별 설정 값을 유지할 수 있습니다. 

### 사용자 암호 재설정

**제목**

seahub/seahub/auth/forms.py line번째 줄

```
        send_html_email(_("Reset Password on %s") % site_name,
                  email_template_name, c, None, [user.username])
```

**본문**

[seahub/seahub/templates/registration/password_reset_email.html](https://github.com/haiwen/seahub/blob/master/seahub/templates/registration/password_reset_email.html)


에 복사하고 새로운 내용으로 수정할 수 있습니다. 이 방식으로 업그레이드 한 후에도 개별 설정 값을 유지할 수 있습니다. 

### 시스템 관리자의 새 구성원 추가

**제목**

seahub/seahub/views/sysadmin.py 424번째 줄

```
send_html_email(_(u'Password has been reset on %s') % SITE_NAME,
            'sysadmin/user_reset_email.html', c, None, [email])
```

**본문**

[seahub/seahub/templates/sysadmin/user_add_email.html](https://github.com/haiwen/seahub/blob/master/seahub/templates/sysadmin/user_add_email.html)

참고: user_add_email.html 파일을 `seahub-data/custom/templates/sysadmin/user_reset_email.html`에 복사하고 새로운 내용으로 수정할 수 있습니다. 이 방식으로 업그레이드 한 후에도 개별 설정 값을 유지할 수 있습니다. 

### 시스템 관리자의 사용자 암호 재설정

**제목**

seahub/seahub/views/sysadmin.py 1224번째 줄

```
send_html_email(_(u'Password has been reset on %s') % SITE_NAME,
            'sysadmin/user_reset_email.html', c, None, [email])
```

**본문**

[seahub/seahub/templates/sysadmin/user_reset_email.html](https://github.com/haiwen/seahub/blob/master/seahub/templates/sysadmin/user_reset_email.html)

참고: user_reset_email.html 파일을 `seahub-data/custom/templates/sysadmin/user_reset_email.html`에 복사하고 새로운 내용으로 수정할 수 있습니다. 이 방식으로 업그레이드 한 후에도 개별 설정 값을 유지할 수 있습니다. 

### 사용자의 파일/폴더 공유 링크 및 업로드 링크 전송

**제목**

seahub/seahub/share/views.py 913번째 줄

```
try:
    if file_shared_type == 'f':
        c['file_shared_type'] = _(u"file")
        send_html_email(_(u'A file is shared to you on %s') % SITE_NAME,
                        'shared_link_email.html',
                        c, from_email, [to_email],
                        reply_to=reply_to
                        )
    else:
        c['file_shared_type'] = _(u"directory")
        send_html_email(_(u'A directory is shared to you on %s') % SITE_NAME,
                        'shared_link_email.html',
                        c, from_email, [to_email],
                        reply_to=reply_to)
```

**본문**

[seahub/seahub/templates/shared_link_email.html](https://github.com/haiwen/seahub/blob/master/seahub/templates/shared_link_email.html)

[seahub/seahub/templates/shared_upload_link_email.html](https://github.com/haiwen/seahub/blob/master/seahub/templates/shared_upload_link_email.html)

참고: shared_link_email.html 파일을 `seahub-data/custom/templates/shared_link_email.html`에 복사하고 새로운 내용으로 수정할 수 있습니다. 이 방식으로 업그레이드 한 후에도 개별 설정 값을 유지할 수 있습니다. 


### 읽지 않은 알림 다시 알림

**제목**

```
send_html_email(_('New notice on %s') % settings.SITE_NAME,
                                'notifications/notice_email.html', c,
                                None, [to_user])
```

**본문**

[seahub/seahub/notifications/templates/notifications/notice_email.html](https://github.com/haiwen/seahub/blob/master/seahub/notifications/templates/notifications/notice_email.html)

