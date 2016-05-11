# Seahub 配置

Note: You can also modify most of the config items via web interface. The config items are saved in database table (seahub-db/constance_config). They have a higher priority over the items in config files.

## Seahub 下发送邮件提醒

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

**注意1**: 如果邮件功能不能正常使用，请在<code>logs/seahub.log</code>日志文件中查看问题原因. 更多信息请见 [Email notification list].

**注意2**: 如果你想在非用户验证情况下使用邮件服务，请将 <code>EMAIL_HOST_PASSWORD</code> 置为 **blank** (<code>''</code>).


## 缓存

Seahub 在默认文件系统(/tmp/seahub_cache/)中缓存文件(avatars, profiles, etc) . 你可以通过 Memcached 进行缓存操作 (前提是你已经安装了python-memcache模块).
After install **python-memcache**, add the following lines to **seahub_settings.py**.

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
```

## 用户管理选项

The following options affect user registration, password and session.

```python
# 是非开启用户注册功能. 默认为 `False`.
ENABLE_SIGNUP = False

# 用户注册后是否立刻激活，默认为 `True`.
# 如设置为 `False`, 需管理员手动激活.
ACTIVATE_AFTER_REGISTRATION = False

# 管理员新增用户后是否给用户发送邮件. 默认为 `True`.
SEND_EMAIL_ON_ADDING_SYSTEM_MEMBER = True

# 管理员重置用户密码后是否给用户发送邮件. 默认为 `True`.
SEND_EMAIL_ON_RESETTING_USER_PASSWD = True

# 登录记住天数. 默认 7 天
LOGIN_REMEMBER_DAYS = 7

# 用户输入密码错误次数超过改设置后，显示验证码
LOGIN_ATTEMPT_LIMIT = 3

# deactivate user account when login attempts exceed limit
# Since version 5.1.2 or pro 5.1.3
FREEZE_USER_ON_LOGIN_FAILED = False

# 用户密码最少长度
USER_PASSWORD_MIN_LENGTH = 6

# 用户密码复杂性:
#    数字, 大写字母, 小写字母, 其他符号
# '3' 表示至少包含以上四种类型中的 3 个
USER_PASSWORD_STRENGTH_LEVEL = 3

# 检查用户密码的复杂性
USER_STRONG_PASSWORD_REQUIRED = False

# 管理员添加／重置用户后，强制用户修改登录密码
# 在版本 5.1.1 加入, 默认开启
FORCE_PASSWORD_CHANGE = True

# cookie 的保存时限，(默认为 2 周).
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2

# 浏览器关闭后，是否清空用户会话 cookie.
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# 是否存储每次请求的会话数据. 默认为 `False`
SESSION_SAVE_EVERY_REQUEST = False

```



## 资料库设置

Options for libraries:

```python
# 加密资料库密码最小长度
REPO_PASSWORD_MIN_LENGTH = 8

# mininum length for password for share link (since version 4.4)
SHARE_LINK_PASSWORD_MIN_LENGTH = 8

# Disable sync with any folder. Default is `False`
# NOTE: since version 4.2.4
DISABLE_SYNC_WITH_ANY_FOLDER = True

# 允许用户设置资料库的历史保留天数
ENABLE_REPO_HISTORY_SETTING = True

# Enable or disable normal user to create organization libraries
# Since version 5.0.5
ENABLE_USER_CREATE_ORG_REPO = True
```

Options for online file preview:

```python
# 是否使用 pdf.js 来在线查看文件. 默认为 `True`,  you can turn it off.
# NOTE: since version 1.4.
USE_PDFJS = True

# 在线文件查看最大文件大小，默认为 30M.
# 注意, 在专业版中，seafevents.conf 中有另一个选项
# `max-size` 也控制 doc/ppt/excel/pdf 文件在线查看的最大文件大小。
# 您需要同时把这两个选项调大，如果您要允许 30M 以上 doc/ppt/excel/pdf 的查看。
FILE_PREVIEW_MAX_SIZE = 30 * 1024 * 1024

# 开启 thumbnails 功能
# NOTE: since version 4.0.2
ENABLE_THUMBNAIL = True

# 文件缩略图的存储位置
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

## 注意

* 请重启 Seahub 以使更改生效.
* 如果更改没有生效，请删除 seahub_setting.pyc 缓存文件.

```bash
./seahub.sh restart
```

