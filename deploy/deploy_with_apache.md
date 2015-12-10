# Config Seahub with Apache

## Important

According to the [security advisory](https://www.djangoproject.com/weblog/2013/aug/06/breach-and-django/) published by Django team, we recommend disable [GZip compression](http://httpd.apache.org/docs/2.2/mod/mod_deflate.html) to mitigate [BREACH attack](http://breachattack.com/).

## Prepare

1. Install and enable mod_fastcgi and also enable mod_rewrite. On Ubuntu:

    ```bash
    sudo apt-get install libapache2-mod-fastcgi
    sudo a2enmod rewrite
    sudo a2enmod fastcgi
    ```
   
    On Debian you will need to first enable the **non-free** repo in **/etc/apt/sources.list** before you can install libapache2-mod-fastcgi e.g.:
    
    ```bash
    deb http://ftp.debian.org/pub/debian/ wheezy main non-free
    deb-src http://ftp.debian.org/pub/debian/ wheezy main non-free

    deb http://security.debian.org/ wheezy/updates main non-free
    deb-src http://security.debian.org/ wheezy/updates main non-free
    ```
    
    On CentOS/Redhat, you will need to compile mod_fastcgi from source, please refer to [this](http://www.cyberciti.biz/tips/rhel-centos-fedora-apache2-fastcgi-php-configuration.html).
    
2. Enable apache proxy

    ```bash
    sudo a2enmod proxy_http
    ```


On raspbian install fcgi like [this](http://raspberryserver.blogspot.co.at/2013/02/installing-lamp-with-fastcgi-php-fpm.html)

## Deploy Seahub/FileServer With Apache

Seahub is the web interface of Seafile server. FileServer is used to handle raw file uploading/downloading through browsers. By default, it listens on port 8082 for HTTP request.

Here we deploy Seahub using fastcgi, and deploy FileServer with reverse proxy. We assume you are running Seahub using domain '''www.myseafile.com'''.

First edit your apache config file. Depending on your distro, you will need to add this line to **the end of the file**:

`apache2.conf`, for Ubuntu/Debian:
```apache
FastCGIExternalServer /var/www/seahub.fcgi -host 127.0.0.1:8000
```

`httpd.conf`, for Centos/Fedora:
```apache
FastCGIExternalServer /var/www/html/seahub.fcgi -host 127.0.0.1:8000
```

Note, `seahub.fcgi` is just a placeholder, you don't need to actually have this file in your system, but be sure to use a path that is in the DocumentRoot of your Domain/Subdomain to avoid 404 errors.

Second, modify Apache config file:
(`sites-enabled/000-default`) for ubuntu/debian, (`vhost.conf`) for centos/fedora

```apache
<VirtualHost *:80>
    ServerName www.myseafile.com
    # Use "DocumentRoot /var/www/html" for Centos/Fedora
    # Use "DocumentRoot /var/www" for Ubuntu/Debian
    DocumentRoot /var/www
    Alias /media  /home/user/haiwen/seafile-server-latest/seahub/media

    RewriteEngine On

    # For apache2.2, you may need to change to
    #  <Location /media>
    #    Order allow,deny
    #    Allow from all
    #  </Location>
    <Location /media>
        Require all granted
    </Location>

    #
    # seafile fileserver
    #
    ProxyPass /seafhttp http://127.0.0.1:8082
    ProxyPassReverse /seafhttp http://127.0.0.1:8082
    RewriteRule ^/seafhttp - [QSA,L]
    # For apache2.2, you may need to add
    #  <Location /seafhttp>
    #    Order allow,deny
    #    Allow from all
    # </Location>
    
    #
    # seahub
    #
    RewriteRule ^/(media.*)$ /$1 [QSA,L,PT]
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^(.*)$ /seahub.fcgi$1 [QSA,L,E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
</VirtualHost>
```

If you are running Apache 2.2 then you will need to [update your access control configuration](https://httpd.apache.org/docs/2.4/upgrading.html#access) accordingly e.g.

```apache
    <Location /media>
        Order allow,deny
        Allow from all
    </Location>
    <Location /seafhttp>
        Order allow,deny
        Allow from all
    </Location>
```

If you are running ModSecurity with Apache 2.2 then you will need to disable Modsecurity for the (Sub-)Domain where you setup Seafile, to avoid problems while synching. (http://www.atomicorp.com/wiki/index.php/Mod_security)

```apache
    <IfModule mod_security2.c>
        SecRuleEngine Off 
    </IfModule>
```

## Modify ccnet.conf and seahub_setting.py

### Modify ccnet.conf

You need to modify the value of <code>SERVICE_URL</code> in [ccnet.conf](../config/ccnet-conf.md)
to let Seafile know the domain you choose.

```python
SERVICE_URL = http://www.myseafile.com
```

Note: If you later change the domain assigned to seahub, you also need to change the value of  <code>SERVICE_URL</code>.

### Modify seahub_settings.py

You need to add a line in <code>seahub_settings.py</code> to set the value of `FILE_SERVER_ROOT` (or `HTTP_SERVER_ROOT` before version 3.1)

```python
FILE_SERVER_ROOT = 'http://www.myseafile.com/seafhttp'
```

## Start Seafile and Seahub

```bash
sudo service apache2 restart
./seafile.sh start
./seahub.sh start-fastcgi
```

## Notes when Upgrading Seafile Server

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
    RewriteRule ^/(media.*)$ /$1 [QSA,L,PT]
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^/(seahub.*)$ /seahub.fcgi/$1 [QSA,L,E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
```
and
```apache
    FastCGIExternalServer /var/www/seahub.fcgi -host 127.0.0.1:8000
```

When a user click a file download link in Seahub, Seahub reads the value of `FILE_SERVER_ROOT` and redirects the user to address `https://example.com/seafhttp/xxxxx/`. `https://example.com/seafhttp` is the value of `FILE_SERVER_ROOT`. Here, the `FILE_SERVER` means the FileServer component of Seafile, which only serves for raw file downloading/uploading.

When Apache receives the request at 'https://example.com/seafhttp/xxxxx/', it proxies the request to FileServer, which is listening at 127.0.0.1:8082. This is controlled by the following config items:

```apache
    ProxyPass /seafhttp http://127.0.0.1:8082
    ProxyPassReverse /seafhttp http://127.0.0.1:8082
    RewriteRule ^/seafhttp - [QSA,L]
```
