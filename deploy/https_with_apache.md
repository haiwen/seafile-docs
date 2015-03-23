# Enabling Https with Apache

## Generate SSL digital certificate with OpenSSL

Here we use self-signed SSL digital certificate for free. If you use a paid ssl certificate from some authority, just skip the this step.

<pre>
    openssl genrsa -out privkey.pem 2048
    openssl req -new -x509 -key privkey.pem -out cacert.pem -days 1095
</pre>

## Enable https on Seahub

Assume you have configured Apache as [Deploy Seafile with
Apache](deploy_with_apache.md). To use https, you need to enable mod_ssl

<pre>
[sudo] a2enmod ssl
</pre>

On Windows, you have to add ssl module to httpd.conf
<pre>
LoadModule ssl_module modules/mod_ssl.so
</pre>

Then modify your Apache configuration file. Here is a sample:

<pre>
<VirtualHost *:80>
  ServerName www.myseafile.com
  redirectMatch / https://www.myseafile.com/
</virtualHost>
<VirtualHost *:443>
  SSLEngine On
  SSLCertificateFile /path/to/cacert.pem
  SSLCertificateKeyFile /path/to/privkey.pem


  ServerName www.myseafile.com
  DocumentRoot /var/www
  ... and so on, same as for without SSL ....
</VirtualHost>
</pre>

## Modify settings to use https

### ccnet conf

Since you change from http to https, you need to modify the value of "SERVICE_URL" in <code>ccnet/ccnet.conf</code>:
<pre>
SERVICE_URL = https://www.myseafile.com
</pre>

### seahub_settings.py

You need to add a line in seahub_settings.py to set the value of `FILE_SERVER_ROOT` (Or `HTTP_SERVER_ROOT` before version 3.1.0)

<pre>
FILE_SERVER_ROOT = 'https://www.myseafile.com/seafhttp'
</pre>

## Start Seafile and Seahub

<pre>
./seafile.sh start
./seahub.sh start-fastcgi
</pre>


## Detailed explanation

The picture at the end of [this document](components.md) may help you understand seafile server better

There are two components in Seafile server, Seahub and FileServer. FileServer only servers for raw file uploading/downloading, it listens on 8082. Seahub, that serving all the other pages, is still listen on 8000. But under https, Seahub should listen as in fastcgi mode on 8000 (run as ./seahub.sh start-fastcgi). And as in fastcgi mode, when you visit  http://domain:8000 directly, it should return an error page.

When a user visit https://example.com/home/my/, Apache receives this request and sends it to Seahub via fastcgi. This is controlled by the following config items:

    #
    # seahub
    #
    RewriteRule ^/(media.*)$ /$1 [QSA,L,PT]
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^/(seahub.*)$ /seahub.fcgi/$1 [QSA,L,E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]

and

    FastCGIExternalServer /var/www/seahub.fcgi -host 127.0.0.1:8000


When a user click a file download link in Seahub, Seahub reads the value of `FILE_SERVER_ROOT` and redirects the user to address `https://example.com/seafhttp/xxxxx/`. `https://example.com/seafhttp` is the value of FILE_SERVER_ROOT. Here, the `FILE_SERVER` means the FileServer component of Seafile, which only serves for raw file downloading/uploading.

When Apache receives the request at 'https://example.com/seafhttp/xxxxx/', it proxies the request to FileServer, which is listening at 127.0.0.1:8082. This is controlled by the following config items:

    ProxyPass /seafhttp http://127.0.0.1:8082
    ProxyPassReverse /seafhttp http://127.0.0.1:8082
    RewriteRule ^/seafhttp - [QSA,L]
