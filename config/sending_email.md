# Sending Email Notifications on Seahub

## Types of Email Sending in Seafile

There are currently five types of emails sent in Seafile:

- User reset his/her password
- System admin add new member
- System admin reset user password
- User send file/folder share link and upload link
- [pro] Reminder of unread notifications (It is sent by a background task which is pro edition only)

The first four types of email are sent immediately. The last type is sent by a background task running periodically.

## Options of Email Sending

Please add the following lines to seahub_settings.py to enable email sending.

```python
EMAIL_USE_TLS = False
EMAIL_HOST = 'smtp.example.com'        # smtp server
EMAIL_HOST_USER = 'username@example.com'    # username and domain
EMAIL_HOST_PASSWORD = 'password'    # password
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_USE_SSL = EMAIL_PORT == 465 # Quick guess of SSL depending on portused.  
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

**Note**: If your email service still does not work, you can checkout the log file `logs/seahub.log` to see what may cause the problem. For a complete email notification list, please refer to [email notification list](customize_email_notifications.md). 
On some hosting services such as scaleway smtp out is blocked by default [see support thread](https://community.online.net/t/solved-smtp-connection-blocked/2262/4)

**Note2**: If you want to use the email service without authentication leaf `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` **blank** (`''`). (But notice that the emails then will be sent without a `From:` address.)

**Note3**: About using SSL connection (using port 465)

Port 587 is being used to establish a TLS connection and port 465 is being used to establish an SSL connection.  Starting from Django 1.8, it supports both. Until version 5.1 Seafile only supported Django 1.5, which only supports TLS connections. If your email server only supports SSL connections and you are using a Seafile Server version below 5.1, you can find a workaround here: [django-smtp-ssl](https://github.com/bancek/django-smtp-ssl).

## Change the `sender` and `reply to` of email

You can change the sender and reply to field of email by add the following settings to seahub_settings.py. This only affects email sending for file share link.

```python
# Replace default from email with user's email or not, defaults to ``False``
REPLACE_FROM_EMAIL = True

# Set reply-to header to user's email or not, defaults to ``False``. For details,
# please refer to http://www.w3.org/Protocols/rfc822/
ADD_REPLY_TO_HEADER = True
```

## Config background email sending task (Pro Edition Only)

The background task will run periodically to check whether an user have new unread notifications. If there are any, it will send a reminder email to that user. The background email sending task is controlled by `seafevents.conf`.

```
[SEAHUB EMAIL]

## must be "true" to enable user email notifications when there are new unread notifications
enabled = true

## interval of sending seahub email. Can be s(seconds), m(minutes), h(hours), d(days)
interval = 30m
```

## Customize email messages

The simplest way to customize the email message is setting the `SITE_NAME` variable in seahub_settings.py. If it is not enough for your case, you can customize the email templates.

**Note:** Subject line may vary between different releases, this is based on Release 5.0.0. Restart Seahub so that your changes take effect.

### The email base template

[seahub/seahub/templates/email_base.html](https://github.com/haiwen/seahub/blob/master/seahub/templates/email_base.html)

Note: You can copy email_base.html to `seahub-data/custom/templates/email_base.html` and modify the new one. In this way, the customization will be maintained after upgrade.

### User reset his/her password

**Subject**

seahub/seahub/auth/forms.py line:127

```python
        send_html_email(_("Reset Password on %s") % site_name,
                  email_template_name, c, None, [user.username])
```

**Body**

[seahub/seahub/templates/registration/password_reset_email.html](https://github.com/haiwen/seahub/blob/master/seahub/templates/registration/password_reset_email.html)


Note: You can copy password_reset_email.html to `seahub-data/custom/templates/registration/password_reset_email.html` and modify the new one. In this way, the customization will be maintained after upgrade.

### System admin add new member

**Subject**

seahub/seahub/views/sysadmin.py line:424

```
send_html_email(_(u'Password has been reset on %s') % SITE_NAME,
            'sysadmin/user_reset_email.html', c, None, [email])
```

**Body**

[seahub/seahub/templates/sysadmin/user_add_email.html](https://github.com/haiwen/seahub/blob/master/seahub/templates/sysadmin/user_add_email.html)

Note: You can copy user_add_email.html to `seahub-data/custom/templates/sysadmin/user_add_email.html` and modify the new one. In this way, the customization will be maintained after upgrade.

### System admin reset user password

**Subject**

seahub/seahub/views/sysadmin.py line:1224

```python
send_html_email(_(u'Password has been reset on %s') % SITE_NAME,
            'sysadmin/user_reset_email.html', c, None, [email])
```

**Body**

[seahub/seahub/templates/sysadmin/user_reset_email.html](https://github.com/haiwen/seahub/blob/master/seahub/templates/sysadmin/user_reset_email.html)

Note: You can copy user_reset_email.html to `seahub-data/custom/templates/sysadmin/user_reset_email.html` and modify the new one. In this way, the customization will be maintained after upgrade.

### User send file/folder share link

**Subject**

seahub/seahub/share/views.py line:913

```python
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

**Body**

[seahub/seahub/templates/shared_link_email.html](https://github.com/haiwen/seahub/blob/master/seahub/templates/shared_link_email.html)

[seahub/seahub/templates/shared_upload_link_email.html](https://github.com/haiwen/seahub/blob/master/seahub/templates/shared_upload_link_email.html)

Note: You can copy shared_link_email.html to `seahub-data/custom/templates/shared_link_email.html` and modify the new one. In this way, the customization will be maintained after upgrade.


### Reminder of unread notifications

**Subject**

```python
send_html_email(_('New notice on %s') % settings.SITE_NAME,
                                'notifications/notice_email.html', c,
                                None, [to_user])
```

**Body**

[seahub/seahub/notifications/templates/notifications/notice_email.html](https://github.com/haiwen/seahub/blob/master/seahub/notifications/templates/notifications/notice_email.html)
