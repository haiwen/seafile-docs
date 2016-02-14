# Deploy Seahub at Non-root domain
This documentation will talk about how to deploy Seafile Web using Apache/Nginx at Non-root directory of the website(e.g., www.example.com/seafile/). Please note that the file server path will still be e.g. www.example.com/seafhttp (rather than www.example.com/seafile/seafhttp) because this path is hardcoded in the clients.

**Note:** We assume you have read [Deploy Seafile with nginx](deploy_with_nginx.md) or [Deploy Seafile with apache](deploy_with_apache.md).

## Deploy with Nginx

First, we need to overwrite some variables in seahub_settings.py:

<pre>
SERVE_STATIC = False
MEDIA_URL = '/seafmedia/'
COMPRESS_URL = MEDIA_URL
STATIC_URL = MEDIA_URL + 'assets/'
SITE_ROOT = '/seafile/'
LOGIN_URL = '/seafile/accounts/login/'    # NOTE: since version 5.0.4
</pre>

We will use Nginx to serve static files(js, css, etc), so we just disable <code>SERVE_STATIC</code>.

<code>MEDIA_URL</code> can be anything you like, just make sure a trailing slash is appended at the end.

We deploy Seafile at <code>/seafile/</code> directory instead of root directory, so we set <code>SITE_ROOT</code> to <code>/seafile/</code>.

Then, we need to configure the Nginx:

<pre>
server {
    listen 80;
    server_name www.example.com;

    proxy_set_header X-Forwarded-For $remote_addr;

    location /seafile {
        fastcgi_pass    127.0.0.1:8000;
        fastcgi_param   SCRIPT_FILENAME     $document_root$fastcgi_script_name;
        fastcgi_param   PATH_INFO           $fastcgi_script_name;

        fastcgi_param	SERVER_PROTOCOL	    $server_protocol;
        fastcgi_param   QUERY_STRING        $query_string;
        fastcgi_param   REQUEST_METHOD      $request_method;
        fastcgi_param   CONTENT_TYPE        $content_type;
        fastcgi_param   CONTENT_LENGTH      $content_length;
        fastcgi_param	SERVER_ADDR         $server_addr;
        fastcgi_param	SERVER_PORT         $server_port;
        fastcgi_param	SERVER_NAME         $server_name;
#       fastcgi_param   HTTPS               on; # enable this line only if https is used
        access_log      /var/log/nginx/seahub.access.log;
    	error_log       /var/log/nginx/seahub.error.log;
    }

    location /seafhttp {
        rewrite ^/seafhttp(.*)$ $1 break;
        proxy_pass http://127.0.0.1:8082;
        client_max_body_size 0;
    }

    location /seafmedia {
        rewrite ^/seafmedia(.*)$ /media$1 break;
        root /home/user/haiwen/seafile-server-latest/seahub;
    }
}
</pre>

You need also to modify `SERVICE_URL` and `FILE_SERVER_ROOT` (see below).

## Deploy with Apache

First, you need to modify seahub_settings.py as above.

If you are using **mod_fastcgi** then edit httpd.conf file, add this line:
<pre>
  FastCGIExternalServer /var/www/seahub.fcgi -host 127.0.0.1:8000
</pre>
After that, you need to configure your Apache, here is the sample configuration:

```
 <VirtualHost *:80>
  ServerName www.example.com
  DocumentRoot /var/www
  Alias /seafmedia  /home/user/haiwen/seafile-server-2.0.2/seahub/media

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
  RewriteRule ^/(seafmedia.*)$ /$1 [QSA,L,PT]
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteRule ^/(seafile.*)$ /seahub.fcgi/$1 [QSA,L,E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
 </VirtualHost>
```

If you are using **mod_proxy_fcgi** you need only to configure your Apache, here is the sample configuration of a virtual host:

```
 <VirtualHost *:80>
  Alias /seafmedia /home/user/haiwen/seafile-server-latest/seahub/media
  <Location /seafmedia>
   ProxyPass !
   Require all granted
  </Location>

  SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1
  SetEnvIf Request_URI . proxy-fcgi-pathinfo=1

  # Seafile file server
  ProxyPass "/seafhttp" "http://127.0.0.1:8082"
  ProxyPassReverse "/seafhttp" "http://127.0.0.1:8082"

  # Seafile seahub server
  ProxyPass "/seafile" "fcgi://127.0.0.1:8000/seafile"

 </VirtualHost>
```

We use Alias to let Apache serve static files, please change the second argument to your path.

## Modify ccnet.conf and seahub_setting.py

### Modify ccnet.conf

You need to modify the value of <code>SERVICE_URL</code> in [ccnet.conf](../config/ccnet-conf.md)
to let Seafile know the domain you choose.

<pre>
SERVICE_URL = http://www.myseafile.com/seafile
</pre>

Note: If you later change the domain assigned to seahub, you also need to change the value of  <code>SERVICE_URL</code>.

### Modify seahub_settings.py

You need to add a line in <code>seahub_settings.py</code> to set the value of `FILE_SERVER_ROOT`

```python
FILE_SERVER_ROOT = 'http://www.myseafile.com/seafhttp'
```
**Note:** The file server path MUST be `/seafhttp` because this path is hardcoded in the clients.

## Clear the cache

By default, Seahub caches some data like the link to the avatar icon in `/tmp/seahub_cache/` (unless memcache is used). We suggest to clear the cache after seafile has been stopped:

<pre>
rm -rf /tmp/seahub_cache/
</pre>

For memcache users, please purge the cache there instead by restarting your memcached server.

## Start Seafile and Seahub

<pre>
./seafile.sh start
./seahub.sh start-fastcgi
</pre>
