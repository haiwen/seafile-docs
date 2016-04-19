# 서버 설정 일반 문제

#### "Error when calling the metaclass bases" during Seafile initialization

Seafile uses Django 1.5, which requires Python 2.6.5+. Make sure your Python version is 2.7.

#### Seahub.sh can't start, the error message contains: "Could not import settings 'seahub.settings', libpython2.7.so.1.0: can not open shared object file"

You probably encounter this problem in Ubuntu 14.04. Seafile pro edition requires libpython2.7. Install it by:

```
sudo apt-get install libpython2.7
```

#### 온라인 파일 업로드/다운로드 실패

* Check your SERVICE_URL setting in ccnet.conf and FILE_SERVER_ROOT setting in seahub_settings.py
* Make sure you firewall for seafile fileserver is opened.
* Using chrome/firefox debug mode to find which link is given when click download button and what's wrong with this link


#### Apache 로그 오류가 있습니다: "File does not exist: /var/www/seahub.fcgi"

Make sure you use "FastCGIExternalServer /var/www/seahub.fcgi -host 127.0.0.1:8000" in httpd.conf or apache2.conf, especially the "/var/www/seahub.fcgi" part.

#### Error on Apache log: "FastCGI: comm with server "/var/www/seahub.fcgi" aborted: idle timeout (30 sec)"

When accessing file history in huge libraries you get HTTP 500 Error.

해결책:

Change in in httpd.conf or apache2.conf from "FastCGIExternalServer /var/www/seahub.fcgi -host 127.0.0.1:8000"
to "FastCGIExternalServer /var/www/seahub.fcgi -host 127.0.0.1:8000 -idle-timeout 60"

#### Apache/https 로 동작하는 Seafile이 텍스트만 나타남(CSS 포매팅/그림 없음)

The media folder (Alias location identified in /etc/apache2/sites-enabled/000-default (Ubuntu) has inappropriate permissions

해결책:

1. Run installation script as non-root user
2. Copy /media folder to var/www/ and edit the Alias location in /etc/apache2/sites-enabled/000-default

