# Nginx https 활성화

무료 자체 서명 SSL 디지털 인증서를 사용하겠습니다. 일부 인증 기관의 유료 SSL 인증서를 사용하신다면 첫 단계를 건너뛰십시오.

### OpenSSL로 SSL 디지털 서명 만들기
```bash
    openssl genrsa -out privkey.pem 2048
    openssl req -new -x509 -key privkey.pem -out cacert.pem -days 1095
```

SSL 인증서 서명에 개별 인증서 발급 기관을 사용하면, 인증서에서 인증서 철회 목록(CRL)을 활성화해야합니다. 그렇지 않으면 윈도우 클라이언트의 http 동기화가 동작하지 않을 수 있습니다. 자세한 정보는 [이 글타래](https://forum.seafile-server.org/t/https-syncing-on-windows-machine-using-custom-ca/898)를 참고하십시오.

### Nginx의 SSL 모듈 활성화(선택)
Nginx에서 SSL을 지원하지 않으면, 다음 명령으로 다시 컴파일해야합니다:
```bash
    ./configure --with-http_stub_status_module --with-http_ssl_module
    make && make install
```

### Nginx 설정 파일 수정

[Seafile과 Nginx 가동](deploy_with_nginx.md) 편을 따라 Nginx를 설정했다고 가정하겠습니다. https를 사용하려면, Nginx 설정 파일을 수정해야합니다.
```nginx
    server {
        listen       80;
        server_name  www.yourdomain.com;
        rewrite ^ https://$http_host$request_uri? permanent;\t# force redirect http to https
    }

    server {
        listen 443;
        ssl on;
        ssl_certificate /etc/ssl/cacert.pem;    \t# path to your cacert.pem
        ssl_certificate_key /etc/ssl/privkey.pem;\t# path to your privkey.pem
        server_name www.yourdomain.com;
        # ......
        fastcgi_param   HTTPS               on;
        fastcgi_param   HTTP_SCHEME         https;
    }
```


### 예제 설정 파일

예제 설정 파일은 다음과 같습니다:

```nginx
    server {
        listen       80;
        server_name  www.yourdomain.com;
        rewrite ^ https://$http_host$request_uri? permanent;\t# force redirect http to https
    }
    server {
        listen 443;
        ssl on;
        ssl_certificate /etc/ssl/cacert.pem;        # path to your cacert.pem
        ssl_certificate_key /etc/ssl/privkey.pem;\t# path to your privkey.pem
        server_name www.yourdoamin.com;
        proxy_set_header X-Forwarded-For $remote_addr;
        
        add_header Strict-Transport-Security "max-age=31536000; includeSubdomains";
        server_tokens off;

        location / {
            fastcgi_pass    127.0.0.1:8000;
            fastcgi_param   SCRIPT_FILENAME     $document_root$fastcgi_script_name;
            fastcgi_param   PATH_INFO           $fastcgi_script_name;

            fastcgi_param   SERVER_PROTOCOL\t    $server_protocol;
            fastcgi_param   QUERY_STRING        $query_string;
            fastcgi_param   REQUEST_METHOD      $request_method;
            fastcgi_param   CONTENT_TYPE        $content_type;
            fastcgi_param   CONTENT_LENGTH      $content_length;
            fastcgi_param   SERVER_ADDR         $server_addr;
            fastcgi_param   SERVER_PORT         $server_port;
            fastcgi_param   SERVER_NAME         $server_name;
            fastcgi_param   HTTPS               on;
            fastcgi_param   HTTP_SCHEME         https;

            access_log      /var/log/nginx/seahub.access.log;
    \t    error_log       /var/log/nginx/seahub.error.log;
    \t    fastcgi_read_timeout 36000;
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

### 대용량 파일 업로드
매우 큰(4GB 초과) 파일 업로드 요령: 기본적으로 Nginx는 대형 요청을 버퍼에 임시 파일로 저장합니다. 이 요청 본문을 완전히 받고 나면, Nginx에서는 요청 본문을 업스트림 서버로 보냅니다.(이 경우 seaf-server). 파일 크기가 상당히 커보인다면, 버퍼링 기능이 잘 동작하지 않을 수도 있습니다. 게다가 도중에 요청 본문 전달을 멈출 수도 있습니다. 4GB 용량 보다 큰 파일을 업로드하려면 Nginx 1.8.0 이상을 사용하시고 다음 설정 항목을 Nginx 설정 파일에 추가하십시오:

```
    location /seafhttp {
        ... ...
        proxy_request_buffering off;
    }
    
```

WebDAV를 활성화했다면 다음 동일 부분 추가를 추천합니다:

```
    location /seafdav {
        ... ...
        proxy_request_buffering off;
    }
```

### Nginx 다시 불러오기
```bash
    nginx -s reload
```

## https를 사용하도록 설정 수정

### ccnet conf

http에서 https로 바꾸려면 [ccnet.conf](../config/ccnet-conf.md)의 "SERVICE_URL"을 수정해야합니다:
```bash
SERVICE_URL = https://www.example.com
```

### seahub_settings.py

seahub_settings.py에 설정 줄을 추가하여 `FILE_SERVER_ROOT`(3.1.0 버전 이전의 경우 `HTTP_SERVER_ROOT`)의 값을 설정해야 합니다

```python
FILE_SERVER_ROOT = 'https://www.example.com/seafhttp'
```

## Seafile 및 Seahub를 시작하십시오

```bash
./seafile.sh start
./seahub.sh start-fastcgi
```

## Nginx용 추가 보안 설정(개별 선택)

HSTS 헤더를 추가하십시오. 이미 https 버전 페이지를 방문했다면 다음에는 http가 아닌 https 사이트로 바로 이동합니다. 이러한 조치는 man-in-the-middle-attack 방식 공격을 막습니다.
```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubdomains";
```

헤더에 정확한 서버 버전 표시를 없애십시오. 서버 취약성 탐색을 막아줍니다.
```nginx
server_tokens off;
```

