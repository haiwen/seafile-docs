# Server Configuration and Customization

## Config Files

**Important**: Since Seafile Server 5.0.0, all config files are moved to the central **conf** folder. [Read More](../deploy/new_directory_layout_5_0_0.md).

There are three config files in the community edition:

- [ccnet.conf](ccnet-conf.md): contains the LDAP settings
- [seafile.conf](seafile-conf.md): contains settings for seafile daemon and fileserver.
- [seahub_settings.py](seahub_settings_py.md): contains settings for Seahub

There is one additional config file in the pro edition:

- `seafevents.conf`: contains settings for search and documents preview

Note: Since version 5.0.0, you can also modify most of the config items via web interface.The config items are saved in database table (seahub-dab/constance_config). They have a higher priority over the items in config files.

![Seafile Config via Web](../images/seafile-server-config.png)

## Config Items

Email:

* [Sending email notifications](sending_email.md)
* [Customize email notifications](customize_email_notifications.md)

User management

* [User management options](user_options.md)

User quota and download/upload size limits

* [User quota and download/upload size limits options](quota_and_size_options.md)

## Customize Web

* [Customize web inferface](seahub_customization.md)
