# Enabling Https with Apache

Here we suggest you use [Let’s Encrypt](https://letsencrypt.org/getting-started/) to get a certificate from a Certificate Authority (CA). If you use a paid ssl certificate from some authority, just skip the first step.

### Generate SSL certificate

For users who use Let’s Encrypt, you can obtain a valid certificate via [Certbot ACME client](https://certbot.eff.org/)

On Ubuntu systems, the Certbot team maintains a PPA. Once you add it to your list of repositories all you'll need to do is apt-get the following packages.

```bash
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install python-certbot-apache
```

Certbot has a fairly solid beta-quality Apache plugin, which is supported on many platforms, and automates both obtaining and installing certs:

```bash
sudo certbot --apache
```

Running this command will get a certificate for you and have Certbot edit your Apache configuration automatically to serve it. If you're feeling more conservative and would like to make the changes to your Apache configuration by hand, you can use the certonly subcommand:

```bash
sudo certbot --apache certonly
```

To learn more about how to use Certbot you can read threir [documentation](https://certbot.eff.org/docs/).

> If you're using a custom CA to sign your SSL certificate, you have to enable certificate revocation list (CRL) in your certificate. Otherwise http syncing on Windows client may not work. See [this thread](https://forum.seafile-server.org/t/https-syncing-on-windows-machine-using-custom-ca/898) for more information.

## Enable https on Seahub

Assume you have configured Apache as [Deploy Seafile with
Apache](deploy_with_apache.md). To use https, you need to enable mod_ssl

```bash
    sudo a2enmod ssl
```

On Windows, you have to add ssl module to httpd.conf
```apache
LoadModule ssl_module modules/mod_ssl.so
```

Then modify your Apache configuration file. Here is a sample:

```apache
<VirtualHost *:443>
  ServerName www.myseafile.com
  DocumentRoot /var/www

  SSLEngine On
  SSLCertificateFile /path/to/cacert.pem
  SSLCertificateKeyFile /path/to/privkey.pem

  Alias /media  /home/user/haiwen/seafile-server-latest/seahub/media

  <Location /media>
    Require all granted
  </Location>

  RewriteEngine On

  #
  # seafile fileserver
  #
  ProxyPass /seafhttp http://127.0.0.1:8082
  ProxyPassReverse /seafhttp http://127.0.0.1:8082
  RewriteRule ^/seafhttp - [QSA,L]

  #
  # seahub
  #
  SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1
  ProxyPass / http://127.0.0.1:8000/
  ProxyPassReverse / http://127.0.0.1:8000/
</VirtualHost>
```

## Modify settings to use https

### ccnet conf

Since you change from http to https, you need to modify the value of "SERVICE_URL" in [ccnet.conf](../config/ccnet-conf.md). You can also modify SERVICE_URL via web UI in "System Admin->Settings". (**Warning**: if you set the value both via Web UI and ccnet.conf, the setting via Web UI will take precedence.)

```python
SERVICE_URL = https://www.myseafile.com
```

### seahub_settings.py

You need to add a line in seahub_settings.py to set the value of `FILE_SERVER_ROOT`. You can also modify `FILE_SERVER_ROOT` via web UI in "System Admin->Settings". (**Warning**: if you set the value both via Web UI and seahub_settings.py, the setting via Web UI will take precedence.)

```python
FILE_SERVER_ROOT = 'https://www.myseafile.com/seafhttp'
```

## Start Seafile and Seahub

```bash
./seafile.sh start
./seahub.sh start
```
