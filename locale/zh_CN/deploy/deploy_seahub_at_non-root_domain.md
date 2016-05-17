# 在非根域名下部署 Seahub
This documentation will talk about how to deploy Seafile Web using Apache/Nginx at Non-root directory of the website(e.g., www.example.com/seafile/). Please note that the file server path will still be e.g. www.example.com/seafhttp (rather than www.example.com/seafile/seafhttp) because this path is hardcoded in the clients.

注意: 请先阅读 [Nginx 下配置 Seahub](deploy_with_nginx.md) 或者 [Apache 下配置 Seahub](deploy_with_apache.md).

## Configure Seahub

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

## Modify ccnet.conf and seahub_setting.py

### 更改 ccnet.conf

为使 Seafile 知道你所使用的域名，请更改 [/data/haiwen/conf/ccnet.conf](../config/ccnet-conf.md) 中 <code>SERVICE_URL</code> 变量的值。

<pre>
SERVICE_URL = http://www.myseafile.com/seafile
</pre>

注意: 如果以后域名有所变动，请记得更改 <code>SERVICE_URL</code>.

### 更改 seahub_settings.py

更改 <code>seahub_settings.py</code> 中 `FILE_SERVER_ROOT` 的值

```python
FILE_SERVER_ROOT = 'http://www.myseafile.com/seafhttp'
```
**Note:** The file server path MUST be `/seafhttp` because this path is hardcoded in the clients.


## Webserver configuration

### Nginx 下部署

接下来，配置 Nginx 如下:

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
#       fastcgi_param   HTTPS               on; # 如果使用 https，请取消掉这行的注释。
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


## Apache 下部署

Here is the sample configuration:

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

## Clear the cache

By default, Seahub caches some data like the link to the avatar icon in `/tmp/seahub_cache/` (unless memcache is used). We suggest to clear the cache after seafile has been stopped:

<pre>
rm -rf /tmp/seahub_cache/
</pre>

For memcache users, please purge the cache there instead by restarting your memcached server.

## 启动 Seafile 和 Seahub

<pre>
./seafile.sh start
./seahub.sh start-fastcgi
</pre>

