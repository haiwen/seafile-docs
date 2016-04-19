# 서버 설정 및 개별 설정

**참고**: Seafile 서버 5.0.0부터 모든 설정 파일은 **conf** 폴더에 옮겨서 모아둡니다. [자세한 내용은 이 글을 읽어보십시오](../deploy/new_directory_layout_5_0_0.md)

이 설명서는 Seafile 서버의 다양한 설정 옵션을 바꾸는 방법을 설명합니다.

커뮤니티판에는 세가지 설정 파일이 있습니다:

- [ccnet.conf](ccnet-conf.md): 네트워크 설정이 들어있습니다
- [seafile.conf](seafile-conf.md): Seafile 데몬 및 파일 서버 설정이 들어있습니다.
- [seahub_settings.py](seahub_settings_py.md): Seahub 설정이 들어있습니다

전문가판에는 추가 설정 파일이 있습니다:

- `seafevents.conf`: ccnet/ccnet.search 및 문서 미리 보기 기능의 설정이 들어있습니다




## 저장소 용량 제한 설정(seafile.conf)

You may set a default quota (e.g. 2GB) for all users. To do this, just add the following lines to `seafile.conf` file

<pre>
[quota]
# default user quota in GB, integer only
default = 2
</pre>

This setting applies to all users. If you want to set quota for a specific user, you may log in to seahub website as administrator, then set it in "System Admin" page.

## 기본 기록 용량 제한(seafile.conf)

If you don't want to keep all file revision history, you may set a default history length limit for all libraries.

<pre>
[history]
keep_days = days of history to keep
</pre>

## Seafile 파일 서버 설정(seafile.conf)

Seafile 파일 서버의 설정은 `seafile.conf`의 <code>[fileserver]</code> 섹션에 있습니다

<pre>
[fileserver]
# binding host for fileserver
host = 0.0.0.0
# tcp port for fileserver
port = 8082
</pre>

업로드/다운로드 설정을 바꾸십시오.

<pre>
[fileserver]
# Set maximum upload file size to 200M.
max_upload_size=200

# Set maximum download directory size to 200M.
max_download_dir_size=200
</pre>

**참고**: 바꾼 설정을 적용하려면 seafile과 seahub를 다시 시작해야합니다.
<pre>
./seahub.sh restart
./seafile.sh restart
</pre>

## Seahub 설정(seahub_settings.py)

#### Seahub에서 전자메일 알림 보내기

A few features work better if it can send email notifications, such as notifying users about new messages.
If you want to setup email notifications, please add the following lines to seahub_settings.py (and set your email server).

<pre>
EMAIL_USE_TLS = False
EMAIL_HOST = 'smtp.example.com'        # smpt server
EMAIL_HOST_USER = 'username@example.com'    # username and domain
EMAIL_HOST_PASSWORD = 'password'    # password
EMAIL_PORT = '25'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
</pre>

GMail을 전자메일 서버로 활용하면 다음 줄을 추가하십시오:

<pre>
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'username@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
</pre>

**참고**: 여전히 전자메일 서비스가 동작하지 않으면, <code>logs/seahub.log</code> 로그 파일에서 어떤 부분에 문제가 있는지 확인하십시오. 완벽한 전자메일 알림 목록 기능을 갖추려면, [전자메일 알림 목록](customize_email_notifications.md)을 참고하십시오.

**Note2**: If you want to use the Email service without authentication leaf <code>EMAIL_HOST_USER</code> and <code>EMAIL_HOST_PASSWORD</code> **blank** (<code>''</code>). (But notice that the emails then will be sent without a <code>From:</code> address.)

#### 캐시

Seahub는 기본적으로(/tmp/seahub_cache) 사용자 계정 항목(아바타, 프로파일 등)을 캐싱합니다. 이 부분을 memcached로 대체할 수 있습니다(python-memcache를 우선 설치해야합니다).

<pre>
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
\t'LOCATION': '127.0.0.1:11211',
    }
}
</pre>

#### Seahub 설정

You may change seahub website's settings by adding variables in `seahub_settings.py`.

<pre>

# Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Set this to seahub website's URL. This URL is contained in email notifications.
SITE_BASE = 'http://www.example.com/'

# Set this to your website's name. This is contained in email notifications.
SITE_NAME = 'example.com'

# Set seahub website's title
SITE_TITLE = 'Seafile'

# If you don't want to run seahub website on your site's root path, set this option to your preferred path.
# e.g. setting it to '/seahub/' would run seahub on http://example.com/seahub/.
SITE_ROOT = '/'

# pdf 파일을 온라인으로 볼 때 pdf.js 사용 여부를 설정합니다. 기본값: `True`,  설정을 끌 수 있습니다.
# 참고: 1.4 버전 부터.
USE_PDFJS = True

# 웹 등록 활성화 여부를 설정합니다. 기본값: `False`.
# 참고: 1.4 버전 부터
ENABLE_SIGNUP = False

# 등록이 끝난 후 사용자 활성화 여부를 결정합니다. 기본값: `True`.
# `False`로 설정하면 admin 패널에서 관리자가 직접 활성화해야합니다.
# 참고: 1.8 버전 부터
ACTIVATE_AFTER_REGISTRATION = False

# 시스템 admin이 새 구성원을 추가했을 때 전자메일을 보낼 지 여부를 설정합니다. 기본값: `True`.
# 참고: 1.4 버전 부터.
SEND_EMAIL_ON_ADDING_SYSTEM_MEMBER = True

 # 시스템 admin이 사용자 암호를 다시 설정했을 때 전자메일을 보낼 지 여부를 설정합니다. 기본값: `True`.
# 참고: 1.4 버전 부터.
SEND_EMAIL_ON_RESETTING_USER_PASSWD = True

# `조직` 탭 숨김.
# https://cloud.seafile.com/와 완전히 같은 개인 Seafile을 보유했다면, 이 플래그를 설정할 수 있습니다.
CLOUD_MODE = True

# 온라인 미리 보기 최대 파일 크기. 기본 크기: 30M.
FILE_PREVIEW_MAX_SIZE = 30 * 1024 * 1024

# 초 단위 쿠키 수명(기본: 2주).
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2

# 모든 요청에 대한 세션 데이터 저장 여부.
SESSION_SAVE_EVERY_REQUEST = False

# 웹 브라우저를 닫았을 때 사용자 세션 쿠기 유지 여부.
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# 서버측 암호화를 기본으로 사용하고, 아니면 사용자가 암호화 방식을 선택.
FORCE_SERVER_CRYPTO = True

</pre>

**참고**:

* You need to restart seahub so that your changes take effect.
* If your changes don't take effect, You may need to delete 'seahub_setting.pyc'. (A cache file)

<pre>
./seahub.sh restart
</pre>

