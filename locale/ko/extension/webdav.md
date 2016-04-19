# WebDAV 확장 기능

Seafile WebDAV 서버(SeafDAV)는 Seafile 서버 2.1.0에 추가했습니다.

아래 위키 문서에서 Seafile 설치 폴더를 `/data/haiwen`으로 가정합니다.

## SeafDAV 설정

설정 파일은 `/data/haiwen/conf/seafdav.conf`입니다. 아직 만들지 않았다면 이 파일을 만들 수 있습니다.

<pre>
[WEBDAV]

# Default is false. Change it to true to enable SeafDAV server.
enabled = true

port = 8080

# Change the value of fastcgi to true if fastcgi is to be used
fastcgi = false

# If you deploy seafdav behind nginx/apache, you need to modify "share_name".
share_name = /
</pre>

설정을 수정하고 나면, 항상 Seafile 서버를 다시 시작하여 설정 내용을 적용해야합니다.

<pre>
./seafile.sh restart
</pre>


### 예제 설정 1: Nginx/Apache 미 사용

WebDAV 클라이언트에서 <code>http://example.com:8080</code> 주소로 WebDAV 서버에 접근합니다

<pre>
[WEBDAV]
enabled = true
port = 8080
fastcgi = false
share_name = /
</pre>

### 예제 설정 2: Nginx

WebDAV 클라이언트에서 <code>http://example.com/seafdav</code> 주소로 Seafile WebDAV 서버에 접근합니다

<pre>
[WEBDAV]
enabled = true
port = 8080
fastcgi = true
share_name = /seafdav
</pre>

위 설정에서, '''share_name''' 값은 seafdav 서버에 할당할 주소의 접미부인 '''/seafdav'''로 바꾸었습니다.

#### https를 활용하지 않는 Nginx

Nginx 해당 설정(https 제외)은 다음과 같습니다:

<pre>
     location /seafdav {
        fastcgi_pass    127.0.0.1:8080;
        fastcgi_param   SCRIPT_FILENAME     $document_root$fastcgi_script_name;
        fastcgi_param   PATH_INFO           $fastcgi_script_name;

        fastcgi_param   SERVER_PROTOCOL     $server_protocol;
        fastcgi_param   QUERY_STRING        $query_string;
        fastcgi_param   REQUEST_METHOD      $request_method;
        fastcgi_param   CONTENT_TYPE        $content_type;
        fastcgi_param   CONTENT_LENGTH      $content_length;
        fastcgi_param   SERVER_ADDR         $server_addr;
        fastcgi_param   SERVER_PORT         $server_port;
        fastcgi_param   SERVER_NAME         $server_name;
        
        client_max_body_size 0;
        
        # This option is only available for Nginx >= 1.8.0. See more details below.
        proxy_request_buffering off;

        access_log      /var/log/nginx/seafdav.access.log;
        error_log       /var/log/nginx/seafdav.error.log;
    }
</pre>

#### https를 활용하는 Nginx

https를 활용하는 nginx 설정:

<pre>
     location /seafdav {
        fastcgi_pass    127.0.0.1:8080;
        fastcgi_param   SCRIPT_FILENAME     $document_root$fastcgi_script_name;
        fastcgi_param   PATH_INFO           $fastcgi_script_name;

        fastcgi_param   SERVER_PROTOCOL     $server_protocol;
        fastcgi_param   QUERY_STRING        $query_string;
        fastcgi_param   REQUEST_METHOD      $request_method;
        fastcgi_param   CONTENT_TYPE        $content_type;
        fastcgi_param   CONTENT_LENGTH      $content_length;
        fastcgi_param   SERVER_ADDR         $server_addr;
        fastcgi_param   SERVER_PORT         $server_port;
        fastcgi_param   SERVER_NAME         $server_name;

        fastcgi_param   HTTPS               on;
        
        client_max_body_size 0;
        
        # This option is only available for Nginx >= 1.8.0. See more details below.
        proxy_request_buffering off;

        access_log      /var/log/nginx/seafdav.access.log;
        error_log       /var/log/nginx/seafdav.error.log;
    }
</pre>

기본적으로 Nginx에서 임시 파일에 있는 대형 요청 본문을 버퍼에 저장합니다. 다음 요청 본문을 완전히 받으면, Nginx에서 업스트림 서버에 요청 본문을 보냅니다(이 경우 seafdav). 하지만 파일 크기가 상당히 큰 것 같으면, 버퍼링 기능이 제대로 동작하지 않습니다. 중간에서 요청 본문 중개가 멈출 수도 있습니다. 따라서 4GB 이상의 파일 업로드를 지원하려면 Nginx 1.8.0 이상의 버전을 설치하시고 `proxy_request_buffering off` 설정을  Nginx 설정에 추가하십시오.

### 예제 설정 3: Apache

다음 설정은 Apache 2.4 이상을 사용함을 가정합니다.

WebDAV 클라이언트에서 <code>http://example.com/seafdav</code> 주소로 Seafile WebDAV 서버에 접근합니다

<pre>
[WEBDAV]
enabled = true
port = 8080
fastcgi = false
share_name = /seafdav
</pre>

위 설정에서 '''share_name''' 값은 SeafDAV 서버의 주소 접미부 '''/seafdav'''로 바꾸었습니다. **참고로 이 부분은 Apache에서 fastcgi를 사용하지 않습니다.**

Apache 설정 파일(site-enabled/000-default)을 수정하십시오:

#### https를 활용하지 않는 Apache

Apache 설정에 따라 [Seafile과 Apache를 가동](../deploy/deploy_with_apache.md)할 때, 관련 설정 파일에 Seafdav를 추가하십시오:

<pre>
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
    # WebDAV
    # We use http proxy, since SeafDAV is incompatible with FCGI proxy in Apache 2.4.
    #
    ProxyPass /seafdav http://127.0.0.1:8080/seafdav
    ProxyPassReverse /seafdav http://127.0.0.1:8080/seafdav

    #
    # seahub
    #
    SetEnvIf Request_URI . proxy-fcgi-pathinfo=unescape
    SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1
    ProxyPass / fcgi://127.0.0.1:8000/

</virtualhost>
</pre>

#### https를 활용하는 Apache

Apache 설정에 따라 [Apache에서 Seafile 웹의 https를 활성화](../deploy/https_with_apache.md)했다면, seafdav를 관련 설정 파일에 추가하십시오:

<pre>
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
  # WebDAV
  # We use http proxy, since SeafDAV is incompatible with FCGI proxy in Apache 2.4.
  #
  ProxyPass /seafdav http://127.0.0.1:8080/seafdav
  ProxyPassReverse /seafdav http://127.0.0.1:8080/seafdav
  
  #
  # seahub
  #
  SetEnvIf Request_URI . proxy-fcgi-pathinfo=unescape
  SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1
  ProxyPass / fcgi://127.0.0.1:8000/

</virtualhost>
</pre>

## 클라이언트 측 참고

Seafile WebDAV 서버를 로컬 파일 시스템(또는 네트워크 드라이브)으로 매핑할 때 알려진 성능 제약이 있음을 우선적으로 참고하십시오.
- 한 번에 상당히 많은 양의 파일을 업로드하면 클라이언트와 동기화할 때보다 더 느려집니다. 각각의 파일을 개별적으로 커밋해야 하기 때문입니다.
- WebDAV 서버 접근은 때로는 느릴 수 있습니다. 로컬 파일 시스템 드라이버에서 파일 속성을 가져올 때 불필요한 요청을 많이 보내기 때문입니다.

따라서 WebDAV는 빈번하지 않은 파일 접근 용도에 가장 적합합니다. 더 나은 성능을 기대한다면, 동기화 클라이언트를 대신 사용하십시오.

### 윈도우

WebDAV용 클라이언트 추천은 윈도우 버전에 따라 다릅니다:
- 윈도우 XP: 윈도우 탐색기에서 비 암호화 HTTP 연결만 지원합니다. 보안을 위해, Cyberduck 또는 BitKinex같은 서드 파티 클라이언트 사용만이 유효한 선택입니다.
- 비스타 이상 버전: 윈도우 탐색기에서 https 연결을 지원합니다만, 서버에 유효한 인증서가 있어야합니다. 윈도우 탐색기에서 WebDAV 서버를 네트워크 드라이브로 매핑할 경우 추천합니다. 자체 서명 인증서를 사용한다면 윈도우 시스템의 발급 기관 저장소에 인증서 발급 기관을 추가해야합니다.

### 리눅스

리눅스에서는 여러가지 선택의 여지가 있습니다. WebDAV 서버에 연결할 때 노틸러스 같은 파일 관리자 프로그램을 사용하거나, 명령 프롬프트에서 davfs2를 사용할 수 있습니다.

davfs2를 사용하려면

<pre>
sudo apt-get install davfs2
sudo mount -t davfs -o uid=<username> https://example.com/seafdav /media/seafdav/
</pre>

-o 옵션으로 <사용자이름> 디렉터리로 마운트한 디렉터리의 소유주를 설정하여 비 루트 사용자가 기록하게 할 수 있습니다.

davfs2의 LOCK 동작 비활성화를 추천합니다. /etc/davfs2/davfs2.conf를 편집해야합니다.

<pre>
 use_locks       0
</pre>

### Mac OS X

Finder의 WebDAV 지원은 안정적이지 않으며 느립니다. 따라서 Cyberduck 같은 WebDAV 클라이언트 프로그램 사용을 권장합니다.

## 자주 묻는 질문

### 클라이언트에서 seafdav 서버에 연결할 수 없음

기본적으로, seafdav는 비활성 기능입니다. <code>seafdav.conf</code>에 <code>enabled = true</code> 설정 값이 들어있는지 확인하십시오.
비활성 상태로 두고 싶지 않으면, 수정하시고 Seafile 서버를 다시 시작하십시오.


### 클라이언트에 "Error: 404 Not Found" 오류가 떴을 때

SeafDAV 서버를 Nginx/Apache 뒤에서 동작하게 하고 싶다면, 위 예제 설정과 같이 <code>share_name</code>의 값을 바꿨는지 확인하십시오. Seafile 서버를 다시 시작한 후 확인해보십시오.

### 윈도우 탐색기에 "파일이 너무 커서 대상 파일 시스템에서 사용할 수 없습니다" 오류가 떴을 때

WebDAV를 네트워크 드라이브로 매핑한 후 네트워크 드라이브에서 로컬 폴더로 50MB 이상의 파일을 복사할 때 일어납니다.

윈도우 탐색기에서 WebDAV 서버에서 다운로드한 파일 크기에 제약을 두기 때문입니다. 이 크기를 더 크게 하려면, 클라이언트 머신의 레지스트리 항목 값을 바꾸십시오. `HKEY_LOCAL_MACHINE -> SYSTEM -> CurrentControlSet -> Services -> WebClient -> Parameters`에 `FileSizeLimitInBytes` 레지스트리 키가 있습니다.

