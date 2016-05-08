# 비 루트 도메인에서 Seahub 가동
이 문서는 웹 사이트의 비 루트 디렉터리(예: www.example.com/seafile/)로 Apache/Nginx에서 Seafile을 가동하는 방법을 다룹니다. 클라이언트에서(www.example.com/seafile/seafhttp가 아닌)www.example.com/seafhttp와 같은 경로를 하드코딩 해두었기 때문에 파일 서버 주소는 언급한 그대로임을 참고하십시오.

**참고:** [Seafile과 Nginx 가동](deploy_with_nginx.md) 또는 [Seafile과 Apache 가동](deploy_with_apache.md)을 이미 읽었다고 가정합니다.

## Seahub 설정

우선 seahub_settings.py의 몇가지 변수 값을 바꿔야합니다:

<pre>
SERVE_STATIC = False
MEDIA_URL = '/seafmedia/'
COMPRESS_URL = MEDIA_URL
STATIC_URL = MEDIA_URL + 'assets/'
SITE_ROOT = '/seafile/'
LOGIN_URL = '/seafile/accounts/login/'    # NOTE: since version 5.0.4
</pre>

웹서버에서 정적 파일(js, css 등)을 제공하므로 <code>SERVE_STATIC</code>을 비활성으로 설정하겠습니다.

<code>MEDIA_URL</code>은 원하는대로 설정할 수 있습니다만, 마지막에 슬래시를 넣었는지 확인하십시오.

루트 디렉터리 대신 <code>/seafile/</code>에서 Seafile을 가동하므로 <code>SITE_ROOT</code>는 <code>/seafile/</code> 값으로 설정합니다.

## ccnet.conf 및 seahub_setting.py 설정 수정

### ccnet.conf 수정

사용 도메인을 Seafile에서 알도록 [ccnet.conf](../config/ccnet-conf.md)파일의 <code>SERVICE_URL</code> 값을 바꾸어야합니다.

<pre>
SERVICE_URL = http://www.myseafile.com/seafile
</pre>

참고: Seahub에 할당한 도메인을 나중에 바꾸면 <code>SERVICE_URL</code>의 값도 바꿔야합니다.

### seahub_settings.pySeafile 수정

<code>seahub_settings.py</code>에 설정 줄을 추가하여 `FILE_SERVER_ROOT` 값을 설정해야합니다

```python
FILE_SERVER_ROOT = 'http://www.myseafile.com/seafhttp'
```
**참고:** 파일 서버 경로는 `/seafhttp` 여야 하며, 이 경로는 클라이언트에 하드코딩 처리되어 있습니다.


## 웹 서버 설정

### Nginx로 가동

그 다음 Nginx를 설정해야합니다:

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

Apache에서 정적 파일을 제공하도록 Alias 지시문을 사용했으므로 경로에 두번째 인자를 바꾸십시오.

## 캐시 정리

기본적으로 Seahub에서는(memcache를 사용하지 않으면) `/tmp/seahub_cache/`에 아바타 링크 아이콘 같은 일부 데이터를 캐시로 저장합니다. Seafile을 멈추고 나면 캐시를 비우는 것이 좋습니다:

<pre>
rm -rf /tmp/seahub_cache/
</pre>

memcache 사용자는, memcached 서버를 다시 시작하는 대신 캐시를 완전히 삭제하십시오.

## Seafile 및 Seahub를 시작하십시오

<pre>
./seafile.sh start
./seahub.sh start-fastcgi
</pre>

