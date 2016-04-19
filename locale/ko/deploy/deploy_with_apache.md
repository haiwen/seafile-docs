# Config Seahub with Apache

## 중요사항

According to the [security advisory](https://www.djangoproject.com/weblog/2013/aug/06/breach-and-django/) published by Django team, we recommend disable [GZip compression](http://httpd.apache.org/docs/2.2/mod/mod_deflate.html) to mitigate [BREACH attack](http://breachattack.com/).

This tutorial assumes you run at least Apache 2.4.

## 준비

Apache 모듈을 설치하고 활성화하십시오

우분투라면 다음 명령으로 활성화할 수 있습니다:

```bash
sudo a2enmod rewrite
sudo a2enmod proxy_fcgi
sudo a2enmod proxy_http
```


On raspbian install fcgi like [this](http://raspberryserver.blogspot.co.at/2013/02/installing-lamp-with-fastcgi-php-fpm.html)

## Deploy Seahub/FileServer With Apache

Seahub is the web interface of Seafile server. FileServer is used to handle raw file uploading/downloading through browsers. By default, it listens on port 8082 for HTTP request.

Here we deploy Seahub using fastcgi, and deploy FileServer with reverse proxy. We assume you are running Seahub using domain '''www.myseafile.com'''.

Modify Apache config file: (`sites-enabled/000-default`) for ubuntu/debian, (`vhost.conf`) for centos/fedora

```apache
<VirtualHost *:80>
    ServerName www.myseafile.com
    # Use "DocumentRoot /var/www/html" for Centos/Fedora
    # Use "DocumentRoot /var/www" for Ubuntu/Debian
    DocumentRoot /var/www
    Alias /media  /home/user/haiwen/seafile-server-latest/seahub/media

    RewriteEngine On

    <Location /media>
        Require all granted
    </Location>

    #
    # seafile fileserver
    #
    ProxyPass /seafhttp http://127.0.0.1:8082
    ProxyPassReverse /seafhttp http://127.0.0.1:8082
    RewriteRule ^/seafhttp - [QSA,L]

    #
    # seahub
    #
    SetEnvIf Request_URI . proxy-fcgi-pathinfo=unescape
    SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1
    ProxyPass / fcgi://127.0.0.1:8000/
</VirtualHost>
```

## ccnet.conf 및 seahub_setting.py 설정 수정

### ccnet.conf 수정

사용 도메인을 Seafile에서 알도록 [ccnet.conf](../config/ccnet-conf.md)파일의 <code>SERVICE_URL</code> 값을 바꾸어야합니다.

```python
SERVICE_URL = http://www.myseafile.com
```

Note: If you later change the domain assigned to seahub, you also need to change the value of  <code>SERVICE_URL</code>.

### seahub_settings.pySeafile 수정

You need to add a line in <code>seahub_settings.py</code> to set the value of `FILE_SERVER_ROOT` (or `HTTP_SERVER_ROOT` before version 3.1)

```python
FILE_SERVER_ROOT = 'http://www.myseafile.com/seafhttp'
```

## Seafile 및 Seahub를 시작하십시오

```bash
sudo service apache2 restart
./seafile.sh start
./seahub.sh start-fastcgi
```

## Troubleshooting

### Problems with paths and files containing spaces

If there are problems with paths or files containing spaces, make sure to have at least Apache 2.4.12.

References
 * https://github.com/haiwen/seafile/issues/1258#issuecomment-188866740
 * https://bugs.launchpad.net/ubuntu/+source/apache2/+bug/1284641
 * https://bugs.launchpad.net/ubuntu/+source/apache2/+bug/1284641/comments/5
 * https://svn.apache.org/viewvc/httpd/httpd/tags/2.4.12/CHANGES?view=markup#l45

## Seafile 서버 업그레이드 참고

When [upgrading seafile server](upgrade.md), besides the normal steps you should take, there is one extra step to do: '''Update the path of the static files in your Nginx/Apache configuration'''. For example, assume your are upgrading seafile server 1.3.0 to 1.4.0, then:

```apache
  Alias /media  /home/user/haiwen/seafile-server-1.4.0/seahub/media
```

**Tip:**
You can create a symbolic link <code>seafile-server-latest</code>, and make it point to your current seafile server folder (Since seafile server 2.1.0, the <code>setup-seafile.sh</code> script will do this for you). Then, each time you run a upgrade script, it would update the <code>seafile-server-latest</code> symbolic link to keep it always point to the latest version seafile server folder.

In this case, you can write:

```apache
  Alias /media  /home/user/haiwen/seafile-server-latest/seahub;
```
This way, you no longer need to update the apache config file each time you upgrade your seafile server.


## Detailed explanation

This may help you understand seafile server better: [Seafile Components](../overview/components.md)

There are two components in Seafile server, Seahub and FileServer. FileServer only servers for raw file uploading/downloading, it listens on 8082. Seahub that serving all the other pages, is still listen on 8000. But under https, Seahub should listen as in fastcgi mode on 8000 (run as ./seahub.sh start-fastcgi). And as in fastcgi mode, when you visit  http://domain:8000 directly, it should return an error page.

When a user visit https://example.com/home/my/, Apache receives this request and sends it to Seahub via fastcgi. This is controlled by the following config items:

```apache
    #
    # seahub
    #
    SetEnvIf Request_URI . proxy-fcgi-pathinfo=unescape
    SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1
    ProxyPass / fcgi://127.0.0.1:8000/
```

When a user click a file download link in Seahub, Seahub reads the value of `FILE_SERVER_ROOT` and redirects the user to address `https://example.com/seafhttp/xxxxx/`. `https://example.com/seafhttp` is the value of `FILE_SERVER_ROOT`. Here, the `FILE_SERVER` means the FileServer component of Seafile, which only serves for raw file downloading/uploading.

When Apache receives the request at 'https://example.com/seafhttp/xxxxx/', it proxies the request to FileServer, which is listening at 127.0.0.1:8082. This is controlled by the following config items:

```apache
    #
    # seafile fileserver
    #
    ProxyPass /seafhttp http://127.0.0.1:8082
    ProxyPassReverse /seafhttp http://127.0.0.1:8082
    RewriteRule ^/seafhttp - [QSA,L]
```

