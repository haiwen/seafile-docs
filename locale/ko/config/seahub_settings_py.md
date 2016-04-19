# Seahub 설정

## Seahub에서 전자메일 알림 전송

Seahub 자체에서 사용자에게 새 메시지 알림과 같은 전자메일 알림을 전송할 수 있다면 몇가지 기능이 잘 동작할 수 있습니다.
전자메일 알림을 설정하려면, `seahub_settings.py`에 다음 줄을 추가하십시오(그리고 전자메일 서버를 설정하십시오).

```python
EMAIL_USE_TLS = False
EMAIL_HOST = 'smtp.example.com'        # smpt server
EMAIL_HOST_USER = 'username@example.com'    # username and domain
EMAIL_HOST_PASSWORD = 'password'    # password
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
```

Gmail을 전자메일 서버로 사용한다면, 다음 줄을 추가하십시오:

```python
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'username@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
```

**참고**: 전자메일 서비스가 여전히 동작하지 않는다면, <code>logs/seahub.log</code> 로그 파일을 보고 어디서 문제가 있는지 확인하십시오. 완전한 전자메일 알림 리스트 동작을 수행하려면 [전자메일 알림 리스트](customize_email_notifications.md)를 참고하십시오.

**참고2**: 전자메일 서비스를 인증 없이 사용하려면 <code>EMAIL_HOST_PASSWORD</code>  값을 **빈** 상태(<code>''</code>)로 두십시오.


## Memcached

Seahub에서는 기본적으로 파일 시스템에 사용자 설정 항목(아바타, 프로파일 등)을 캐시(/tmp/seahub_cache/)에 저장합니다. 이 부분을 Memcached로 바꿀 수 있습니다.
**python-memcache**를 설치한 후, **seahub_settings.py**에 다음 줄을 추가하십시오.

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
```

## 사용자 관리 설정 항목

다음 설정 항목은 사용자 등록, 암호, 세션에 영향을 줍니다.

```python
# Enalbe or disalbe registration on web. Default is `False`.
ENABLE_SIGNUP = False

# Activate or deactivate user when registration complete. Default is `True`.
# If set to `False`, new users need to be activated by admin in admin panel.
ACTIVATE_AFTER_REGISTRATION = False

# Whether to send email when a system admin adding a new member. Default is `True`.
SEND_EMAIL_ON_ADDING_SYSTEM_MEMBER = True

# Whether to send email when a system admin resetting a user's password. Default is `True`.
SEND_EMAIL_ON_RESETTING_USER_PASSWD = True

# Remember days for login. Default is 7
LOGIN_REMEMBER_DAYS = 7

# Attempt limit before showing a captcha when login.
LOGIN_ATTEMPT_LIMIT = 3
    
# mininum length for user's password
USER_PASSWORD_MIN_LENGTH = 6

# LEVEL based on four types of input:
# num, upper letter, lower letter, other symbols
# '3' means password must have at least 3 types of the above.
USER_PASSWORD_STRENGTH_LEVEL = 3

# default False, only check USER_PASSWORD_MIN_LENGTH
# when True, check password strength level, STRONG(or above) is allowed
USER_STRONG_PASSWORD_REQUIRED = False

# Force user to change password when admin add/reset a user.
# Added in 5.1.1, deafults to True.
FORCE_PASSWORD_CHANGE = True

# Age of cookie, in seconds (default: 2 weeks).
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2

# Whether a user's session cookie expires when the Web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Whether to save the session data on every request. Default is `False`
SESSION_SAVE_EVERY_REQUEST = False

```


## 라이브러리 설정 항목

라이브러리 설정 항목:

```python
# mininum length for password of encrypted library
REPO_PASSWORD_MIN_LENGTH = 8

# mininum length for password for share link (since version 4.4)
SHARE_LINK_PASSWORD_MIN_LENGTH = 8

# Disable sync with any folder. Default is `False`
# NOTE: since version 4.2.4
DISABLE_SYNC_WITH_ANY_FOLDER = True

# Enable or disable library history setting
ENABLE_REPO_HISTORY_SETTING = True

# Enable or disable normal user to create organization libraries
# Since version 5.0.5
ENABLE_USER_CREATE_ORG_REPO = True
```

온라인 파일 미리 보기 설정 항목:

```python
# Whether to use pdf.js to view pdf files online. Default is `True`,  you can turn it off.
# NOTE: since version 1.4.
USE_PDFJS = True

# Online preview maximum file size, defaults to 30M.
# Note, this option controls files that can be previewed online, like pictures, txt, pdf.
# In pro edition, for preview doc/ppt/excel/pdf, there is another option `max-size` 
# in seafevents.conf that controls the limit of files that can be previewed.
FILE_PREVIEW_MAX_SIZE = 30 * 1024 * 1024

# Enable or disable thumbnails
# NOTE: since version 4.0.2 
ENABLE_THUMBNAIL = True

# Absolute filesystem path to the directory that will hold thumbnail files.
THUMBNAIL_ROOT = '/haiwen/seahub-data/thumbnail/thumb/'
```


## 클라우드 모드

알 수 없는 사용자 기반으로 Seafile을 사용한다면 클라우드 모드를 활성화해야합니다. 사용자가 사용자 목록에 접근하지 못하도록 Seahub 웹 사이트의 조직 탭을 비활성화합니다. 클라우드 모드에서는 비등록 사용자 에게 컨텐트를 공유하고 초대하는 일부 멋들어진 기능이 있습니다. 이리하여 사용자 등록을 가능케 할 수 있습니다. 글로벌 주소록(4.2.3부터)으로 모든 사용자 계정을 검색할 수 있습니다. 이 부분을 비활성화할 수도 있습니다.

```python
# Enable cloude mode and hide `Organization` tab.
CLOUD_MODE = True

# Disable global address book
ENABLE_GLOBAL_ADDRESSBOOK = False
```


## 기타 설정 항목


```python

# Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
# Default language for sending emails.
LANGUAGE_CODE = 'en'

# Set this to your website's name. This is contained in email notifications.
SITE_NAME = 'example.com'

# Set seahub website's title
SITE_TITLE = 'Seafile'

# If you don't want to run seahub website on your site's root path, set this option to your preferred path.
# e.g. setting it to '/seahub/' would run seahub on http://example.com/seahub/.
SITE_ROOT = '/'
```

## 전문가판 전용 설정 항목

```python
# Whether to show the used traffic in user's profile popup dialog. Default is True
SHOW_TRAFFIC = True

# Allow administrator to view user's file in UNENCRYPTED libraries
# through Libraries page in System Admin. Default is False.
ENABLE_SYS_ADMIN_VIEW_REPO = True
```

## 참고

* 바꾼 설정 값을 적용하려면 Seahub를 다시 시작해야합니다.
* 설정 값을 적용하지 않으려면 `seahub_setting.pyc`(캐시 파일)을 삭제해야합니다

```bash
./seahub.sh restart
```

