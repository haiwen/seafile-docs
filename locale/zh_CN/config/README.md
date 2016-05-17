# 服务器配置

## 配置文件

**Important**: Since Seafile Server 5.0.0, all config files are moved to the central **conf** folder. [Read More](../deploy/new_directory_layout_5_0_0.md).

开源版中包括以下三个配置文件:

- [ccnet.conf](ccnet-conf.md): 用来配置网络和 LDAP/AD 连接
- [seafile.conf](seafile-conf.md): 用来配置 Seafile
- [seahub_settings.py](seahub_settings_py.md): 用来配置 Seahub

专业版中还包含以下一个配置文件:

- `seafevents.conf`: 包含搜索与文件预览的配置

Note: Since version 5.0.0, you can also modify most of the config items via web interface. The config items are saved in database table (seahub-db/constance_config). They have a higher priority over the items in config files.

![Seafile Config via Web](../images/seafile-server-config.png)

## 配置项

邮件:

* [发送邮件提醒](sending_email.md)
* [个性化邮件提醒](customize_email_notifications.md)

用户管理：

* [用户管理](user_options.md)

用户存储容量和上传/下载文件大小限制：

* [存储容量与文件上传/下载大小限制](quota_and_size_options.md)

## 自定义 Web

* [自定义 Web](seahub_customization.md)

