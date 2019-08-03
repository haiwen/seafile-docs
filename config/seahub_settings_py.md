# Seahub Settings

Note: You can also modify most of the config items via web interface. The config items are saved in database table (seahub-db/constance_config). They have a higher priority over the items in config files. If you want to disable settings via web interface, you can add `ENABLE_SETTINGS_VIA_WEB = False` to `seahub_settings.py`.

##  Sending Email Notifications on Seahub

Refer to [email sending documentation](sending_email.md).

## Memcached

Seahub caches items(avatars, profiles, etc) on file system by default(/tmp/seahub_cache/). You can replace with Memcached.

Refer to ["add memcached"](../deploy/add_memcached.md).

## Security settings

```python
# For security consideration, please set to match the host/domain of your site, e.g., ALLOWED_HOSTS = ['.example.com'].
# Please refer https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts for details.
ALLOWED_HOSTS = ['.myseafile.com']
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

# Send system admin notify email when user registration is complete. Default is `False`.
NOTIFY_ADMIN_AFTER_REGISTRATION = True

# Remember days for login. Default is 7
LOGIN_REMEMBER_DAYS = 7

# Attempt limit before showing a captcha when login.
LOGIN_ATTEMPT_LIMIT = 3

# deactivate user account when login attempts exceed limit
# Since version 5.1.2 or pro 5.1.3
FREEZE_USER_ON_LOGIN_FAILED = False

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

# Whether enable personal wiki and group wiki. Default is `False`
# Since 6.1.0 CE
ENABLE_WIKI = True

# In old version, if you use Single Sign On, the password is not saved in Seafile.
# Users can't use WebDAV because Seafile can't check whether the password is correct.
# Since version 6.3.8, you can enable this option to let user's to specific a password for WebDAV login.
# Users login via SSO can use this password to login in WebDAV.
# Enable the feature. pycryptodome should be installed first.
# sudo pip install pycryptodome==3.7.2
ENABLE_WEBDAV_SECRET = True
```

## `repo snapshot label` feature

```
# Turn on this option to let users to add a label to a library snapshot. Default is `False`
ENABLE_REPO_SNAPSHOT_LABEL = False
```

## Library options

Options for libraries:

```python
# if enable create encrypted library
ENABLE_ENCRYPTED_LIBRARY = True

# version for encrypted library
# should only be `2` or `3`
ENCRYPTED_LIBRARY_VERSION = 2

# mininum length for password of encrypted library
REPO_PASSWORD_MIN_LENGTH = 8

# mininum length for password for share link (since version 4.4)
SHARE_LINK_PASSWORD_MIN_LENGTH = 8

# minimum expire days for share link (since version 6.3.6)
SHARE_LINK_EXPIRE_DAYS_MIN = 3 # default is 0, no limit.

# maximum expire days for share link (since version 6.3.6)
SHARE_LINK_EXPIRE_DAYS_MAX = 8 # default is 0, no limit.

# default expire days for share link (since version 6.3.8)
# only valid when SHARE_LINK_EXPIRE_DAYS_MIN and SHARE_LINK_EXPIRE_DAYS_MAX is configured
# should be greater than or equal to MIN and less than or equal to MAX
SHARE_LINK_EXPIRE_DAYS_DEFAULT = 5

# force user login when view file/folder share link (since version 6.3.6)
SHARE_LINK_LOGIN_REQUIRED = True

# enable water mark when view(not edit) file in web browser (since version 6.3.6)
ENABLE_WATERMARK = True

# Disable sync with any folder. Default is `False`
# NOTE: since version 4.2.4
DISABLE_SYNC_WITH_ANY_FOLDER = True

# Enable or disable library history setting
ENABLE_REPO_HISTORY_SETTING = True

# Enable or disable normal user to create organization libraries
# Since version 5.0.5
ENABLE_USER_CREATE_ORG_REPO = True

# Enable or disable user share library to any group
# Since version 6.2.0
ENABLE_SHARE_TO_ALL_GROUPS = True

# Enable or disable user to clean trash (default is True)
# Since version 6.3.6
ENABLE_USER_CLEAN_TRASH = True
```

Options for online file preview:

```python
# Whether to use pdf.js to view pdf files online. Default is `True`,  you can turn it off.
# NOTE: since version 1.4.
USE_PDFJS = True

# Online preview maximum file size, defaults to 30M.
FILE_PREVIEW_MAX_SIZE = 30 * 1024 * 1024

# Extensions of previewed text files.
# NOTE: since version 6.1.1
TEXT_PREVIEW_EXT = """ac, am, bat, c, cc, cmake, cpp, cs, css, diff, el, h, html,
htm, java, js, json, less, make, org, php, pl, properties, py, rb,
scala, script, sh, sql, txt, text, tex, vi, vim, xhtml, xml, log, csv,
groovy, rst, patch, go"""

# Enable or disable thumbnails
# NOTE: since version 4.0.2
ENABLE_THUMBNAIL = True

# Seafile only generates thumbnails for images smaller than the following size.
# Since version 6.3.8 pro, suport the psd online preview.
THUMBNAIL_IMAGE_SIZE_LIMIT = 30 # MB

# Enable or disable thumbnail for video. ffmpeg and moviepy should be installed first.
# For details, please refer to https://manual.seafile.com/deploy/video_thumbnails.html
# NOTE: since version 6.1
ENABLE_VIDEO_THUMBNAIL = False

# Use the frame at 5 second as thumbnail
THUMBNAIL_VIDEO_FRAME_TIME = 5

# Absolute filesystem path to the directory that will hold thumbnail files.
THUMBNAIL_ROOT = '/haiwen/seahub-data/thumbnail/thumb/'

# Default size for picture preview. Enlarge this size can improve the preview quality.
# NOTE: since version 6.1.1
THUMBNAIL_SIZE_FOR_ORIGINAL = 1024
```

## Cloud Mode

You should enable cloud mode if you use Seafile with an unknown user base. It disables the organization tab in Seahub's website to ensure that users can't access the user list. Cloud mode provides some nice features like sharing content with unregistered users and sending invitations to them. Therefore you also want to enable user registration. Through the global address book (since version 4.2.3) you can do a search for every user account. So you probably want to disable it.

```python
# Enable cloude mode and hide `Organization` tab.
CLOUD_MODE = True

# Disable global address book
ENABLE_GLOBAL_ADDRESSBOOK = False
```


## External authentication

```python
# Enable authentication with ADFS
# Default is False
# Since 6.0.9
ENABLE_ADFS_LOGIN = True

# Enable authentication wit Kerberos
# Default is False
ENABLE_KRB5_LOGIN = True

# Enable authentication with Shibboleth
# Default is False
ENABLE_SHIBBOLETH_LOGIN = True
```

## Other options


```python
# Disable settings via Web interface in system admin->settings
# Default is True
# Since 5.1.3
ENABLE_SETTINGS_VIA_WEB = False

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

# Custom language code choice.
LANGUAGES = (
    ('en', 'English'),
    ('zh-cn', '简体中文'),
    ('zh-tw', '繁體中文'),
)

# Set this to your website/company's name. This is contained in email notifications and welcome message when user login for the first time.
SITE_NAME = 'Seafile'

# Browser tab's title
SITE_TITLE = 'Private Seafile'

# If you don't want to run seahub website on your site's root path, set this option to your preferred path.
# e.g. setting it to '/seahub/' would run seahub on http://example.com/seahub/.
SITE_ROOT = '/'

# Max number of files when user upload file/folder.
# Since version 6.0.4
MAX_NUMBER_OF_FILES_FOR_FILEUPLOAD = 500

# Control the language that send email. Default to user's current language.
# Since version 6.1.1
SHARE_LINK_EMAIL_LANGUAGE = ''

# Interval for browser requests unread notifications
# Since PRO 6.1.4 or CE 6.1.2
UNREAD_NOTIFICATIONS_REQUEST_INTERVAL = 3 * 60 # seconds

# Whether to allow user to delete account, change login password or update basic user
# info on profile page.
# Since PRO 6.3.10
ENABLE_DELETE_ACCOUNT = False
ENABLE_UPDATE_USER_INFO = False
ENABLE_CHANGE_PASSWORD = False
```

## Pro edition only options

```python
# Whether to show the used traffic in user's profile popup dialog. Default is True
SHOW_TRAFFIC = True

# Allow administrator to view user's file in UNENCRYPTED libraries
# through Libraries page in System Admin. Default is False.
ENABLE_SYS_ADMIN_VIEW_REPO = True

# For un-login users, providing an email before downloading or uploading on shared link page.
# Since version 5.1.4
ENABLE_SHARE_LINK_AUDIT = True

# Check virus after upload files to shared upload links. Defaults to `False`.
# Since version 6.0
ENABLE_UPLOAD_LINK_VIRUS_CHECK = True

# Enable system admin add T&C, all users need to accept terms before using. Defaults to `False`.
# Since version 6.0
ENABLE_TERMS_AND_CONDITIONS = True

# Enable two factor authentication for accounts. Defaults to `False`.
# Since version 6.0
ENABLE_TWO_FACTOR_AUTH = True

# Enable user select a template when he/she creates library.
# When user select a template, Seafile will create folders releated to the pattern automaticly.
# Since version 6.0
LIBRARY_TEMPLATES = {
    'Technology': ['/Develop/Python', '/Test'],
    'Finance': ['/Current assets', '/Fixed assets/Computer']
}

# Send email to these email addresses when a virus is detected.
# This list can be any valid email address, not necessarily the emails of Seafile user.
# Since version 6.0.8
VIRUS_SCAN_NOTIFY_LIST = ['user_a@seafile.com', 'user_b@seafile.com']

# Enable a user to change password in 'settings' page. Default to `True`
# Since version 6.2.11
ENABLE_CHANGE_PASSWORD = True

# Enable group discussion. Default to `True`
# Since version 6.2.11
ENABLE_GROUP_DISCUSSION = True

# Enable file comments. Default to `True`
# Since version 6.2.11
ENABLE_FILE_COMMENT = True
```

## RESTful API

```
# API throttling related settings. Enlarger the rates if you got 429 response code during API calls.
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'ping': '600/minute',
        'anon': '5/minute',
        'user': '300/minute',
    },
    'UNICODE_JSON': False,
}

# Throtting whitelist used to disable throttle for certain IPs.
# e.g. REST_FRAMEWORK_THROTTING_WHITELIST = ['127.0.0.1', '192.168.1.1']
# Please make sure `REMOTE_ADDR` header is configured in Nginx conf according to https://manual.seafile.com/deploy/deploy_with_nginx.html.
REST_FRAMEWORK_THROTTING_WHITELIST = []
```

## Seahub Custom Functions

Since version 6.2, you can define a custom function to modify the result of user search function.

For example, if you want to limit user only search users in the same institution, you can define `custom_search_user` function in `{seafile install path}/conf/seahub_custom_functions/__init__.py`

Code example:

```
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
seahub_dir = os.path.join(current_path, \
        '../../seafile-server-latest/seahub/seahub')
sys.path.append(seahub_dir)

from seahub.profile.models import Profile
def custom_search_user(request, emails):

    institution_name = ''

    username = request.user.username
    profile = Profile.objects.get_profile_by_user(username)
    if profile:
        institution_name = profile.institution

    inst_users = [p.user for p in
            Profile.objects.filter(institution=institution_name)]

    filtered_emails = []
    for email in emails:
        if email in inst_users:
            filtered_emails.append(email)

    return filtered_emails
```

> **NOTE**, you should NOT change the name of `custom_search_user` and `seahub_custom_functions/__init__.py`

Since version 6.2.5 pro, if you enable the **ENABLE_SHARE_TO_ALL_GROUPS** feather on sysadmin settings page, you can also define a custom function to return the groups a user can share library to.

For example, if you want to let a user to share library to both its groups and the groups of user `test@test.com`, you can define a `custom_get_groups` function in `{seafile install path}/conf/seahub_custom_functions/__init__.py`

Code example:

```
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
seaserv_dir = os.path.join(current_path, \
        '../../seafile-server-latest/seafile/lib64/python2.7/site-packages')
sys.path.append(seaserv_dir)

def custom_get_groups(request):

    from seaserv import ccnet_api

    groups = []
    username = request.user.username

    # for current user
    groups += ccnet_api.get_groups(username)

    # for 'test@test.com' user
    groups += ccnet_api.get_groups('test@test.com')

    return groups
```

> **NOTE**, you should NOT change the name of `custom_get_groups` and `seahub_custom_functions/__init__.py`

## Note

* You need to restart seahub so that your changes take effect.
* If your changes don't take effect, You may need to delete 'seahub_setting.pyc'. (A cache file)

```bash
./seahub.sh restart
```

