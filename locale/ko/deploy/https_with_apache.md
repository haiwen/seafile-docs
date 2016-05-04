# Apache https 활성화

## OpenSSL에서 SSL 디지털 서명 만들기

무료 자체 서명 SSL 디지털 인증서를 사용하겠습니다. 일부 인증 기관의 유료 SSL 인증서를 사용하신다면 이 단계를 건너뛰십시오.

```bash
    openssl genrsa -out privkey.pem 2048
    openssl req -new -x509 -key privkey.pem -out cacert.pem -days 1095
```

SSL 인증서 서명에 개별 인증서 발급 기관을 사용하면, 인증서에서 인증서 철회 목록(CRL)을 활성화해야합니다. 그렇지 않으면 윈도우 클라이언트의 http 동기화가 동작하지 않을 수 있습니다. 자세한 정보는 [이 글타래](https://forum.seafile-server.org/t/https-syncing-on-windows-machine-using-custom-ca/898)를 참고하십시오.

## Seahub의 https 활성화

[Seafile과 Apache 가동](deploy_with_apache.md)편을 따라 Apache를 설정했다고 가정하겠습니다. https를 사용하려면 mod_ssl을 활성화해야 합니다

```bash
    sudo a2enmod ssl
```

윈도우에서는 httpd.conf에 ssl 모듈을 추가해야합니다
```apache
LoadModule ssl_module modules/mod_ssl.so
```

다음 Apache 설정 파일을 수정하십시오. 아래는 예제입니다:

```apache
<VirtualHost *:443>
  ServerName www.myseafile.com
  DocumentRoot /var/www
  
  SSLEngine On
  SSLCertificateFile /path/to/cacert.pem
  SSLCertificateKeyFile /path/to/privkey.pem

  Alias /media  /home/user/haiwen/seafile-server-latest/seahub/media
  
  <Location /media>
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
  ProxyPass / fcgi://127.0.0.1:8000/
</VirtualHost>
```

## https를 사용하도록 설정 수정

### ccnet conf

http에서 https로 바꾸려면 [ccnet.conf](../config/ccnet-conf.md)의 "SERVICE_URL"을 수정해야합니다:
```python
SERVICE_URL = https://www.myseafile.com
```

### seahub_settings.py

seahub_settings.py에 설정 줄을 추가하여 `FILE_SERVER_ROOT`(3.1.0 버전 이전의 경우 `HTTP_SERVER_ROOT`)의 값을 설정해야 합니다

```python
FILE_SERVER_ROOT = 'https://www.myseafile.com/seafhttp'
```

## Seafile 및 Seahub를 시작하십시오

```bash
./seafile.sh start
./seahub.sh start-fastcgi
```

## 세부 설명

[이 문서](components.md) 마지막의 그림은 Seafile 서버의 동작 상태를 더 쉽게 이해할 수 있도록 도와드립니다

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
그리고
```apache
    FastCGIExternalServer /var/www/seahub.fcgi -host 127.0.0.1:8000
```

사용자가 Seahub의 파일 다운로드 링크를 누르면, Seahub에서 `FILE_SERVER_ROOT` 값을 읽고 `https://example.com/seafhttp/xxxxx/` 주소로 사용자를 안내합니다. `https://example.com/seafhttp`는 FILE_SERVER_ROOT의 값입니다. 여기서 `FILE_SERVER`는 원시 파일 업로드/다운로드만 처리하는 Seafile의 FileServer 구성 요소입니다.

Apache에서 'https://example.com/seafhttp/xxxxx/' 요청을 받으면,  127.0.0.1:8082에서 대기 중인 FileServer에 요청을 전달합니다. 다음 설정 항목으로 이 동작을 관리합니다:
```apache
    #
    # seafile fileserver
    #
    ProxyPass /seafhttp http://127.0.0.1:8082
    ProxyPassReverse /seafhttp http://127.0.0.1:8082
    RewriteRule ^/seafhttp - [QSA,L]
```

