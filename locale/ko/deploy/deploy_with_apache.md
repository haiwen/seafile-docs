# Seahub와 Apache 설정

## 중요사항

장고 팀의 [보안 권고안](https://www.djangoproject.com/weblog/2013/aug/06/breach-and-django/)에 따르면, [BREACH 공격](http://breachattack.com/)을 피하도록 [GZip 압축](http://httpd.apache.org/docs/2.2/mod/mod_deflate.html) 비활성화를 추천합니다.

이 지침서는 최소한 Apache 2.4를 사용한다고 가정합니다.

## 준비

Apache 모듈을 설치하고 활성화하십시오

우분투라면 다음 명령으로 활성화할 수 있습니다:

```bash
sudo a2enmod rewrite
sudo a2enmod proxy_fcgi
sudo a2enmod proxy_http
```


라즈비안에서는 [이 곳](http://raspberryserver.blogspot.co.at/2013/02/installing-lamp-with-fastcgi-php-fpm.html)에서 언급한대로 fcgi를 설치하십시오

## Seafile/FileServer와 Apache 가동

Seahub는 Seafile 서버의 웹 인터페이스입니다. FileServer는 브라우저의 원시 파일 업로드/다운로드 처리에 활용합니다. FileServer는 기본적으로 8082 포트에서 요청 대기를 수행합니다.

여기서 fastcgi를 활용하여 Seahub를 구동하고 역방향 프록시로 FileServer를 구동하겠습니다. 여기서 Seahub를 실행하는 환경에서 '''www.myseafile.com''' 도메인을 사용한다고 가정하겠습니다.

Apache 설정 파일을 수정하십시오: 우분투/데비안에서는(`sites-enabled/000-default`), 센트OS/페도라 에서는(`vhost.conf`)입니다

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

참고: Seahub에 할당한 도메인을 나중에 바꾸면 <code>SERVICE_URL</code>의 값도 바꿔야합니다.

### seahub_settings.pySeafile 수정

<code>seahub_settings.py</code>에 설정 줄을 추가하여 `FILE_SERVER_ROOT`(3.1.0 버전 이전의 경우 `HTTP_SERVER_ROOT`) 값을 설정해야 합니다

```python
FILE_SERVER_ROOT = 'http://www.myseafile.com/seafhttp'
```

## Seafile 및 Seahub를 시작하십시오

```bash
sudo service apache2 restart
./seafile.sh start
./seahub.sh start-fastcgi
```

## 문제 해결

### 공백 문자가 들어있는 경로 및 파일의 문제

경로 또는 파일에 공백이 들어가 있어 문제가 발생한다면 Apache 버전이 2.4.12 이상이 아닌지 확인하십시오.

참고
 * https://github.com/haiwen/seafile/issues/1258#issuecomment-188866740
 * https://bugs.launchpad.net/ubuntu/+source/apache2/+bug/1284641
 * https://bugs.launchpad.net/ubuntu/+source/apache2/+bug/1284641/comments/5
 * https://svn.apache.org/viewvc/httpd/httpd/tags/2.4.12/CHANGES?view=markup#l45

## Seafile 서버 업그레이드 참고

[Seafile 서버를 업그레이드](upgrade.md)할 때, 일반 과정을 거친 다음의 추가 진행 과정이 있습니다. '''Nginx/Apache 설정에서 정적 파일 경로를 업데이트하십시오'''. 예를 들어 Seafile 서버를 1.3.0에서 1.4.0으로 업데이트 한다면:

```apache
  Alias /media  /home/user/haiwen/seafile-server-1.4.0/seahub/media
```

**요령:**
<code>seafile-server-latest</code> 심볼릭 링크를 작성하여 현재 Seafile 서버 폴더를 가리킬 수 있습니다(Seafile 서버 2.1.0부터, <code>setup-seafile.sh</code> 스크립트가 이 동작을 진행합니다). 그 다음 업그레이드 스크립트를 실행할 때마다 최신 버전의 Seafile 서버 폴더를 항상 가리키도록 <code>seafile-server-latest</code> 심볼릭 링크를 업데이트합니다.

이 경우, 다음 설정을 작성할 수 있습니다:

```apache
  Alias /media  /home/user/haiwen/seafile-server-latest/seahub;
```
이 방법으로 Seafile 서버를 업그레이드할 때마다 더 이상 Apache 설정 파일을 업데이트할 필요가 없습니다.


## 세부 설명

이 부분은 Seafile 서버의 이해를 돕습니다: [Seafile 구성요소](../overview/components.md)

Seafile 서버는 두가지 부분, Seahub와 FileServer로 이루어져있습니다. FileServer는 8082번 포트에서 요청 대기하며 원시 파일 업로드/다운로드 전용 서버입니다. Seahub는 모든 기타 페이지를 제공하며 8000번 포트에서 요청 대기합니다. 다만 https에서는 Seahub는 8000번 포트에서 fastcgi 모드(./seahub.sh start-fastcgi로 실행)로 요청 대기해야합니다. 그리고 fastcgi 모드에서 http://domain:8000 주소로 바로 접근하면 오류 페이지를 반환해야합니다.

사용자가 https://example.com/home/my/ 주소로 접근하면, Apache에서 요청을 받아 fastcgi로 Seahub에 전달합니다. 이 동작은 다음 설정 항목으로 관리합니다:

```apache
    #
    # seahub
    #
    SetEnvIf Request_URI . proxy-fcgi-pathinfo=unescape
    SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1
    ProxyPass / fcgi://127.0.0.1:8000/
```

사용자가 Seahub의 파일 다운로드 링크를 누르면, Seahub에서 `FILE_SERVER_ROOT` 값을 읽고 `https://example.com/seafhttp/xxxxx/` 주소로 사용자를 안내합니다. `https://example.com/seafhttp`는 `FILE_SERVER_ROOT`의 값입니다. 여기서 `FILE_SERVER`는 원시 파일 업로드/다운로드만 처리하는 Seafile의 FileServer 구성 요소입니다.

Apache에서 'https://example.com/seafhttp/xxxxx/' 요청을 받으면,  127.0.0.1:8082에서 대기 중인 FileServer에 요청을 전달합니다. 다음 설정 항목으로 이 동작을 관리합니다:

```apache
    #
    # seafile fileserver
    #
    ProxyPass /seafhttp http://127.0.0.1:8082
    ProxyPassReverse /seafhttp http://127.0.0.1:8082
    RewriteRule ^/seafhttp - [QSA,L]
```

