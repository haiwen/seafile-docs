# 安装常见问题

#### "Error when calling the metaclass bases" during Seafile initialization

Seafile uses Django 1.5, which requires Python 2.6.5+. Make sure your Python version is 2.7.

#### Seahub.sh can't start, the error message contains: "Could not import settings 'seahub.settings', libpython2.7.so.1.0: can not open shared object file"

You probably encounter this problem in Ubuntu 14.04. Seafile pro edition requires libpython2.7. Install it by:

```
sudo apt-get install libpython2.7
```

#### 无法上传/下载

* 检查 ccnet.conf 中 SERVICE_URL的配置，检查 seahub_settings.py 中 FILE_SERVER_ROOT的配置
* 确认防火墙没有禁用 seafile fileserver
* 使用 chrome/firefox 调试模式,找到点击下载按钮时使用的链接并查看错误信息


#### Apache 日志文件报错: "File does not exist: /var/www/seahub.fcgi"

Make sure you use "FastCGIExternalServer /var/www/seahub.fcgi -host 127.0.0.1:8000" in httpd.conf or apache2.conf, especially the "/var/www/seahub.fcgi" part.

#### Error on Apache log: "FastCGI: comm with server "/var/www/seahub.fcgi" aborted: idle timeout (30 sec)"

When accessing file history in huge libraries you get HTTP 500 Error.

Solution:

Change in in httpd.conf or apache2.conf from "FastCGIExternalServer /var/www/seahub.fcgi -host 127.0.0.1:8000" to "FastCGIExternalServer /var/www/seahub.fcgi -host 127.0.0.1:8000 -idle-timeout 60"

#### Apache/HTTPS 下，Seafile 只显示文本文件(没有 CSS 样式和图片显示)

The media folder (Alias location identified in /etc/apache2/sites-enabled/000-default (Ubuntu)) has inappropriate permissions

解决方法:

1. 切换到非根（non-root）用户重新运行安装脚本
2. 复制/media文件夹到var/www/下，并在/etc/apache2/sites-enabled/000-default中重新编辑文件路径。

