# Deploy Seahub at Non-root domain
This documentation will talk about how to deploy Seafile Web using Apache/Nginx at Non-root directory of the website(e.g., www.example.com/seafile/). Please note that the file server path will still be e.g. www.example.com/seafhttp (rather than www.example.com/seafile/seafhttp) because this path is hardcoded in the clients.

**Note:** We assume you have read [Deploy Seafile with nginx](deploy_with_nginx.md) or [Deploy Seafile with apache](deploy_with_apache.md).

## Seahub 설정

First, we need to overwrite some variables in seahub_settings.py:

<pre>
SERVE_STATIC = False
MEDIA_URL = '/seafmedia/'
COMPRESS_URL = MEDIA_URL
STATIC_URL = MEDIA_URL + 'assets/'
SITE_ROOT = '/seafile/'
LOGIN_URL = '/seafile/accounts/login/'    # NOTE: since version 5.0.4
</pre>

The webserver will serve static files (js, css, etc), so we just disable <code>SERVE_STATIC</code>.

<code>MEDIA_URL</code> can be anything you like, just make sure a trailing slash is appended at the end.

We deploy Seafile at <code>/seafile/</code> directory instead of root directory, so we set <code>SITE_ROOT</code> to <code>/seafile/</code>.

## ccnet.conf 및 seahub_setting.py 설정 수정

### ccnet.conf 수정

사용 도메인을 Seafile에서 알도록 [ccnet.conf](../config/ccnet-conf.md)파일의 <code>SERVICE_URL</code> 값을 바꾸어야합니다.

<pre>
SERVICE_URL = http://www.myseafile.com/seafile
</pre>

Note: If you later change the domain assigned to seahub, you also need to change the value of  <code>SERVICE_URL</code>.

### seahub_settings.pySeafile 수정

You need to add a line in <code>seahub_settings.py</code> to set the value of `FILE_SERVER_ROOT`

```python
FILE_SERVER_ROOT = 'http://www.myseafile.com/seafhttp'
```
**Note:** The file server path MUST be `/seafhttp` because this path is hardcoded in the clients.


## 웹 서버 설정

### Nginx로 가동

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

        fastcgi_param\tSERVER_PROTOCOL\t    $server_protocol;
        fastcgi_param   QUERY_STRING        $query_string;
        fastcgi_param   REQUEST_METHOD      $request_method;
        fastcgi_param   CONTENT_TYPE        $content_type;
        fastcgi_param   CONTENT_LENGTH      $content_length;
        fastcgi_param\tSERVER_ADDR         $server_addr;
        fastcgi_param\tSERVER_PORT         $server_port;
        fastcgi_param\tSERVER_NAME         $server_name;
#       fastcgi_param   HTTPS               on; # enable this line only if https is used
        access_log      /var/log/nginx/seahub.access.log;
    \terror_log       /var/log/nginx/seahub.error.log;
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


## Apache로 가동

예제 설정 파일은 다음과 같습니다:

<pre>
<VirtualHost *:80>
  ServerName www.example.com
  DocumentRoot /var/www
  Alias /seafmedia  /home/user/haiwen/seafile-server-latest/seahub/media

  <Location /seafmedia>
    ProxyPass !
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
  SetEnvIf Request_URI . proxy-fcgi-pathinfo=unescape
  SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1
  ProxyPass /seafile fcgi://127.0.0.1:8000/seafile
</VirtualHost>
</pre>

We use Alias to let Apache serve static files, please change the second argument to your path.

## 캐시 비우기

By default, Seahub caches some data like the link to the avatar icon in `/tmp/seahub_cache/` (unless memcache is used). We suggest to clear the cache after seafile has been stopped:

<pre>
rm -rf /tmp/seahub_cache/
</pre>

For memcache users, please purge the cache there instead by restarting your memcached server.

## Seafile 및 Seahub를 시작하십시오

<pre>
./seafile.sh start
./seahub.sh start-fastcgi
</pre>

