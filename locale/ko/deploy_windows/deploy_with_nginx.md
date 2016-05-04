# Seafile과 Nginx 가동

## Seahub/FileServer와 Nginx 가동

Seahub는 Seafile 서버의 웹 인터페이스입니다. FileServer는 브라우저로 원시 파일을 업로드/다운로드하는 동작을 처리할 때 사용합니다. 기본적으로, http 요청을 8082번 포트에서 대기합니다.

fastcgi로 Seahub를 가동하고 FileServer를 역방향 프록시로 가동하겠습니다. 여기서 가동 중인 Seahub는 '''www.myseafile.com''' 도메인을 활용한다고 가정하겠습니다.

아래는 Nginx 설정 파일 예제입니다.

```
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

        access_log      logs/seahub.access.log;
        error_log       logs/seahub.error.log;
    }

    location /seafhttp {
        rewrite ^/seafhttp(.*)$ $1 break;
        proxy_pass http://127.0.0.1:8082;
        client_max_body_size 0;
    }

    location /media {
        root C:/SeafileProgram/seafile-pro-server-2.1.4/seahub;
    }
}
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

Seafile 서버 업그레이드시, 진행해야 할 과정 말고도, 추가로 진행해야 할 일이 있습니다: '''nginx 설정에 있는 정적 파일의 경로를 업데이트하십시오'''. 예를 들자면, Seafile 서버를 2.1.0에서 2.1.1로 업그레이드한다면:

```
    location /media {
        root C:/SeafileProgram/seafile-pro-server-2.1.1/seahub;
    }
```

