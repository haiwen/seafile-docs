# Seahub Settings

##  Sending Email Notifications on Seahub

A few features work better if it can send email notifications, such as notifying users about new messages.
If you want to setup email notifications, please add the following lines to `seahub_settings.py` (and set your email server).

```python
EMAIL_USE_TLS = False
EMAIL_HOST = 'smtp.example.com'        # smpt server
EMAIL_HOST_USER = 'username@example.com'    # username and domain
EMAIL_HOST_PASSWORD = 'password'    # password
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
```

If you are using Gmail as email server, use following lines:

```python
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'username@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
```

**Note**: If your Email service still can not work, you may checkout the log file <code>logs/seahub.log</code> to see what may cause the problem. For complete email notification list, please refer to [Email notification list](customize_email_notifications.md).

**Note2**: If you want to use the Email service without authentication leaf <code>EMAIL_HOST_PASSWORD</code> **blank** (<code>''</code>).


## Memcached

Seahub caches items(avatars, profiles, etc) on file system by default(/tmp/seahub_cache/). You can replace with Memcached.
After install **python-memcache**, add the following lines to **seahub_settings.py**.

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
```

## User management options

The following options affect user registration, password and session.

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


## Library options

Options for libraries:

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

Options for online file preview:

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


## Cloud Mode

You should enable cloud mode if you use Seafile with an unknown user base. It disables the organization tab in Seahub's website to ensure that users can't access the user list. Cloud mode provides some nice features like sharing content with unregistered users and sending invitations to them. Therefore you also want to enable user registration. Through the global address book (since version 4.2.3) you can do a search for every user account. So you probably want to disable it.

```python
# Enable cloude mode and hide `Organization` tab.
CLOUD_MODE = True

# Disable global address book
ENABLE_GLOBAL_ADDRESSBOOK = False
```


## Other options


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

## Pro edition only options

```python
# Whether to show the used traffic in user's profile popup dialog. Default is True
SHOW_TRAFFIC = True

# Allow administrator to view user's file in UNENCRYPTED libraries
# through Libraries page in System Admin. Default is False.
ENABLE_SYS_ADMIN_VIEW_REPO = True
```

## Note

* You need to restart seahub so that your changes take effect.
* If your changes don't take effect, You may need to delete 'seahub_setting.pyc'. (A cache file)

```bash
./seahub.sh restart
```
