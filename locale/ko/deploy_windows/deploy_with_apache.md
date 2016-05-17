# Seafile과 Apache 가동

## 준비

### mod_fastcgi 설치

[mod_fastcgi-*.dll] (http://fastcgi.com/dist/)를 우선 다운로드하고, 아파치 설치 경로의 `modules/` 디렉터리에 복사하십시오.

**참고**: Apache 버전에 맞는 `mod_fastcgi`를 다운로드해야 합니다. 그러니까 이를테면:

- Apache 2.2를 사용한다면 http://fastcgi.com/dist/mod_fastcgi-2.4.6-AP22.dll 을 다운로드하십시오. dll의 **AP22**부분은 Apache **2.2**를 나타냅니다.
- Apache 2.0을 사용한다면 http://fastcgi.com/dist/old/mod_fastcgi-2.4.2-AP20.dll 을 다운로드하십시오

## Seahub/FileServer와 Apache 가동

Seahub는 Seafile 서버의 웹 인터페이스입니다. FileServer는 브라우저로 원시 파일을 업로드/다운로드하는 동작을 처리할 때 사용합니다. 기본적으로, http 요청을 8082번 포트에서 대기합니다.

fastcgi로 Seahub를 가동하고 FileServer를 역방향 프록시로 가동하겠습니다. 여기서 가동 중인 Seahub는 '''www.myseafile.com''' 도메인을 활용한다고 가정하겠습니다.

### httpd.conf 편집

우선 `httpd.conf`를 편집하십시오. **파일 마지막 부분**에 다음 줄을 추가하십시오:

```
LoadModule fastcgi_module modules/mod_fastcgi-2.4.6-AP22.dll
LoadModule rewrite_module modules/mod_rewrite.so
LoadModule proxy_module modules/mod_proxy.so
LoadModule proxy_http_module modules/mod_proxy_http.so
Include conf/extra/httpd-vhosts.conf
```

그 다음 이 줄을 추가하십시오(`YourDocumentRoot`를 Apache의 `DocumentRoot` 값으로 바꾸십시오)

```
FastCGIExternalServer "YourDocumentRoot/seahub.fcgi" -host 127.0.0.1:8000
```

참고로, `seahub.fcgi`는 일종의 빈 칸 역할을 하며, 실제로 이 파일을 시스템에 둘 필요는 없습니다.

### httpd-vhost.conf 편집

Seafile 서버 꾸러미 압축을 `C:/SeafileProgram/seafile-pro-server-2.1.4`에 풀었다고 가정하겠습니다.

```
<VirtualHost *:80>
  ServerName www.myseafile.com
  Alias /media  "C:/SeafileProgram/seafile-pro-server-2.1.4/seahub/media"

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
  RewriteRule ^/(media.*)$ /$1 [QSA,L,PT]
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteRule ^(.*)$ /seahub.fcgi$1 [QSA,L,E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
</VirtualHost>

<Directory "C:/SeafileProgram/seafile-pro-server-2.1.4/seahub/media">
    Options Indexes FollowSymLinks
    AllowOverride None
    Order allow,deny
    Allow from all
</Directory>
```

## 설정 수정

### ccnet.conf 수정


```
SERVICE_URL = http://www.myseafile.com
```

참고: Seahub에 할당한 도메인을 나중에 바꾸면 <code>SERVICE_URL</code>의 값도 바꿔야합니다.

### seafile-data/seafile.conf 수정

`seafile-data/seafile.conf`의 `seahub` 섹션을 수정하십시오:

```
[seahub]
port=8000
fastcgi=true
```

### seahub_settings.py 수정

<code>seahub_settings.py</code>에 다음 줄을 추가하여 `FILE_SERVER_ROOT` 값을 설정하십시오

```
FILE_SERVER_ROOT = 'http://www.myseafile.com/seafhttp'
```

## Seafile 서버 업그레이드 참고

Seafile 서버 업그레이드시, 진행해야 할 과정 말고도, 추가로 진행해야 할 일이 있습니다: '''nginx 설정에 있는 정적 파일의 경로를 업데이트하십시오'''. 예를 들자면, Seafile 서버를 2.1.4에서 2.1.5로 업그레이드한다면:

```
<VirtualHost *:80>
  ...
  Alias /media  "C:/SeafileProgram/seafile-pro-server-2.1.5/seahub/media"
  ...
</VirtualHost>

<Directory "C:/SeafileProgram/seafile-pro-server-2.1.5/seahub/media">
  ...
</Directory>
```

