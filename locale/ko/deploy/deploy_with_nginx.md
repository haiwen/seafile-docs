# Seahub 및 Nginx 설정

## 중요사항

장고 팀의 [보안 권고안](https://www.djangoproject.com/weblog/2013/aug/06/breach-and-django/)에 따르면, [BREACH 공격](http://breachattack.com/)을 피하도록 [GZip 압축](http://wiki.nginx.org/HttpGzipModule) 비활성화를 추천합니다.

## Seahub/FileServer 및 Nginx 가동

Seahub는 Seafile 서버의 웹 인터페이스입니다. FileServer는 브라우저의 원시 파일 업로드/다운로드 처리에 활용합니다. FileServer는 기본적으로 8082 포트에서 요청 대기를 수행합니다.

여기서 [FastCGI](http://en.wikipedia.org/wiki/FastCGI)를 활용하여 Seahub를 구동하고 역방향 프록시로 FileServer를 구동하겠습니다. 여기서 Seahub를 실행하는 환경에서 '''www.myseafile.com''' 도메인을 사용한다고 가정하겠습니다.

아래는 예제 Nginx 설정 파일의 내용입니다.

우분투 14.04에서는 다음 단계를 따라 설정 파일을 추가할 수 있습니다:

1. `/etc/nginx/sites-available/seafile.conf`파일을 만드십시오
2. `/etc/nginx/sites-enabled/default` 파일을 삭제하십시오 : `rm /etc/nginx/sites-enabled/default`
3. 심볼릭 링크를 만드십시오: `ln -s /etc/nginx/sites-available/seafile.conf /etc/nginx/sites-enabled/seafile.conf`

```nginx
server {
    listen 80;
    server_name www.myseafile.com;

    proxy_set_header X-Forwarded-For $remote_addr;

    location / {
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
        fastcgi_param   REMOTE_ADDR         $remote_addr;

        access_log      /var/log/nginx/seahub.access.log;
    \terror_log       /var/log/nginx/seahub.error.log;
    \tfastcgi_read_timeout 36000;
    }

    location /seafhttp {
        rewrite ^/seafhttp(.*)$ $1 break;
        proxy_pass http://127.0.0.1:8082;
        client_max_body_size 0;
        proxy_connect_timeout  36000s;
        proxy_read_timeout  36000s;
        proxy_send_timeout  36000s;
        send_timeout  36000s;
    }

    location /media {
        root /home/user/haiwen/seafile-server-latest/seahub;
    }
}
```

"client_max_body_size" Nginx 기본 설정 값은 1M입니다. 이 지정 용량 이상을 지닌 파일을 업로드하면 HTTP 오류 코드 413을 반환("Request Entity Too Large")합니다.

0으로 설정하여 이 기능을 비활성화하든지 [seafile.conf](../config/seafile-conf.md)의 `[fileserver]` 섹션에 있는 `max_upload_size` 매개변수값과 동일하게 설정하십시오.

매우 큰(4GB 초과) 파일 업로드 요령: 기본적으로 Nginx는 대형 요청을 버퍼에 임시 파일로 저장합니다. 이 요청 본문을 완전히 받고 나면, Nginx에서는 요청 본문을 업스트림 서버로 보냅니다.(이 경우 seaf-server). 파일 크기가 상당히 커보인다면, 버퍼링 기능이 잘 동작하지 않을 수도 있습니다. 게다가 도중에 요청 본문 전달을 멈출 수도 있습니다. 4GB 용량 보다 큰 파일을 업로드하려면 Nginx 1.8.0 이상을 사용하시고 다음 설정 항목을 Nginx 설정 파일에 추가하십시오:

```nginx
    location /seafhttp {
        ... ...
        proxy_request_buffering off;
    }
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
./seafile.sh start
./seahub.sh start-fastcgi
```

