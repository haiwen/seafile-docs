# Config Seahub with Apache

## Important

According to the [security advisory](https://www.djangoproject.com/weblog/2013/aug/06/breach-and-django/) published by Django team, we recommend disable [GZip compression](http://httpd.apache.org/docs/2.2/mod/mod_deflate.html) to mitigate [BREACH attack](http://breachattack.com/).

This tutorial assumes you run at least Apache 2.4.

## Prepare

Install and enable apache modules

On Ubuntu you can use:

```bash
sudo a2enmod rewrite
sudo a2enmod proxy_fcgi
sudo a2enmod proxy_http
```


On raspbian install fcgi like [this](http://raspberryserver.blogspot.co.at/2013/02/installing-lamp-with-fastcgi-php-fpm.html)

## Deploy Seahub/FileServer With Apache

Seahub is the web interface of Seafile server. FileServer is used to handle raw file uploading/downloading through browsers. By default, it listens on port 8082 for HTTP request.

Here we deploy Seahub using fastcgi, and deploy FileServer with reverse proxy. We assume you are running Seahub using domain '''www.myseafile.com'''.

Modify Apache config file:
(`sites-enabled/000-default`) for ubuntu/debian, (`vhost.conf`) for centos/fedora

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

## Modify ccnet.conf and seahub_setting.py

### Modify ccnet.conf

You need to modify the value of `SERVICE_URL` in [ccnet.conf](../config/ccnet-conf.md)
to let Seafile know the domain you choose. You can also modify SERVICE_URL via web UI in "System Admin->Settings". (**Warning**: if you set the value both via Web UI and ccnet.conf, the setting via Web UI will take precedence.)

```python
SERVICE_URL = http://www.myseafile.com
```

Note: If you later change the domain assigned to seahub, you also need to change the value of  `SERVICE_URL`.

### Modify seahub_settings.py

You need to add a line in `seahub_settings.py` to set the value of `FILE_SERVER_ROOT`. You can also modify `FILE_SERVER_ROOT` via web UI in "System Admin->Settings". (**Warning**: if you set the value both via Web UI and seahub_settings.py, the setting via Web UI will take precedence.)

```python
FILE_SERVER_ROOT = 'http://www.myseafile.com/seafhttp'
```

## Start Seafile and Seahub

```bash
sudo service apache2 restart
./seafile.sh start
./seahub.sh start # or "./seahub.sh start-fastcgi" if you're using fastcgi
```

## Troubleshooting

### Problems with paths and files containing spaces

If there are problems with paths or files containing spaces, make sure to have at least Apache 2.4.12.

References
 * https://github.com/haiwen/seafile/issues/1258#issuecomment-188866740
 * https://bugs.launchpad.net/ubuntu/+source/apache2/+bug/1284641
 * https://bugs.launchpad.net/ubuntu/+source/apache2/+bug/1284641/comments/5
 * https://svn.apache.org/viewvc/httpd/httpd/tags/2.4.12/CHANGES?view=markup#l45
