# Nginx https 활성화

Here we use self-signed SSL digital certificate for free. If you use a paid ssl certificate from some authority, just skip the first step.

### Generate SSL digital certificate with OpenSSL
```bash
    openssl genrsa -out privkey.pem 2048
    openssl req -new -x509 -key privkey.pem -out cacert.pem -days 1095
```

If you're using a custom CA to sign your SSL certificate, you have to enable certificate revocation list (CRL) in your certificate. Otherwise http syncing on Windows client may not work. See [this thread](https://forum.seafile-server.org/t/https-syncing-on-windows-machine-using-custom-ca/898) for more information.

### Enable SSL module of Nginx (optional)
If your Nginx does not support SSL, you need to recompile it, the commands are as follows:
```bash
    ./configure --with-http_stub_status_module --with-http_ssl_module
    make && make install
```

### Nginx 설정 파일 수정

Assume you have configured nginx as [Deploy-Seafile-with-nginx](deploy_with_nginx.md). To use https, you need to modify your nginx configuration file.
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
Tip for uploading very large files (> 4GB): By default Nginx will buffer large request body in temp file. After the body is completely received, Nginx will send the body to the upstream server (seaf-server in our case). But it seems when file size is very large, the buffering mechanism dosen't work well. It may stop proxying the body in the middle. So if you want to support file upload larger for 4GB, we suggest you install Nginx version >= 1.8.0 and add the following options to Nginx config file:

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

### nginx 다시 불러오기
```bash
    nginx -s reload
```

## https를 사용하도록 설정 수정

Seafile

Since you change from http to https, you need to modify the value of "SERVICE_URL" in [ccnet.conf](../config/ccnet-conf.md):
```bash
SERVICE_URL = https://www.example.com
```

Seafile

You need to add a line in seahub_settings.py to set the value of `FILE_SERVER_ROOT` (Or `HTTP_SERVER_ROOT` before version 3.1.0)

```python
FILE_SERVER_ROOT = 'https://www.example.com/seafhttp'
```

## Seafile 및 Seahub를 시작하십시오

```bash
./seafile.sh start
./seahub.sh start-fastcgi
```

## nginx용 추가 보안 설정(개별 선택)

Add the HSTS header. If you already visited the https version the next time your browser will visit directly the https site and not the http. Prevent man-in-the-middle-attacks.
```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubdomains";
```

Disable exact server version in header. Prevent scans for vulnerable server.
```nginx
server_tokens off;
```

