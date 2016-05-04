# http 프로토콜로 동기화하도록 설정

4.0.0 버전부터 Seafile에서는 http 프로토콜 파일 동기화를 지원합니다. 서버 설정은 어떤 Seafile 클라이언트 버전을 사용하느냐에 따라 다릅니다.

4.2 버전 이상의 클라이언트에서는 배타적으로 http 동기화 프로토콜을 사용하는데, 다음의 경우가 이에 해당합니다

* https를 사용하지 않는다면 Nginx 또는 Apache에 http 동기화를 수행하도록 설정할 필요가 없습니다. 클라이언트에서는 8082 포트로 파일 서버와 바로 통신할 수 있습니다.
* https를 사용한다면 Nginx 또는 Apache를 설정해야합니다.

4.2 미만의 클라이언트 버전을 사용한다면,

* http(s) 동기화를 사용할 경우 Nginx 또는 Apache를 설정해야합니다.
* Nginx 또는 Apache를 설정하지 않았다면, 비 http 기반 동기화 프로토콜을 대신 사용합니다(10001 및 12001 포트 사용).

4.0 이상의 서버에서는 모든 동기화 프로토콜과 호환되며, 어떤 버전의 클라이언트에서도 이 서버와 동작해야합니다.

## Nginx

https를 사용하지 않도록 Nginx를 설정하려면 [이 안내서](deploy_with_nginx.md)를, https를 사용하도록 Nginx를 설정하려면 [이 안내서](https_with_nginx.md)를 따르십시오.

HTTP 동기화와 관련된 Nginx 설정 파일의 섹션은 다음과 같습니다

```
    location /seafhttp {
        rewrite ^/seafhttp(.*)$ $1 break;
        proxy_pass http://127.0.0.1:8082;
        client_max_body_size 0;
        proxy_connect_timeout  36000s;
        proxy_read_timeout  36000s;
    }
```

참고해야 할 사항이 두가지가 있습니다:

* http 동기화시 "/seafhttp" 경로를 사용해야합니다. 클라이언트에 하드코딩 해두었습니다.
* "client_max_body_size" 설정을 추가해야합니다. 이 값은 0(제한 없음) 또는 100M(대부분의 경우 적당) 값으로 설정해야합니다.

## Apache

https를 사용하지 않도록 Apache를 설정하려면 [이 안내서](deploy_with_apache.md)를, https를 사용하도록 Apache를 설정하려면 [이 안내서](https_with_apache.md)를 따르십시오.

http 동기화와 관련된 Apache 설정 파일 섹션은 다음과 같습니다

```
    #
    # seafile fileserver
    #
    ProxyPass /seafhttp http://127.0.0.1:8082
    ProxyPassReverse /seafhttp http://127.0.0.1:8082
    RewriteRule ^/seafhttp - [QSA,L]
```

참고로 http 프로토록 동기화 기능을 사용하려면 "/seafhttp" 경로를 사용해야합니다. 클라이언트에 하드코딩 해두었습니다.

## 클라이언트측 https 설정

유효한 SSL 인증서를 구매했다면, 동기화 설정을 따로 해야 합니다. 자체 서명 인증서를 사용할 때 클라이언트에 새 계정을 우선 추가하면 서버 인증서 확인 창이 뜹니다. 인증서 승인을 선택하면, 클라이언트는 https 연결을 활용합니다.

클라이언트를 시작할 때 시스템 신뢰 인증서 발급 기관 저장소에서 신뢰 인증서 발급 기관 목록을 불러옵니다. 그 다음 사용자가 승인한 인증서를 인증서 발급 기관 목록에 대응합니다. 이 과정이 끝나면 대응 목록을 인증서 검증에 활용합니다.

자체 서명 인증서 생성에 [이 안내서](https_with_nginx.md)의 인증서 생성 절차를 따른다면, 확인 과정을 거친 후 동기화 과정이 동작해야합니다.

서버에 https로 연결할 수 없을 경우 몇가지 이유가 있습니다. 다음 두가지 해결책을 시도해볼 수 있습니다:

1. 시스템 신뢰 인증 발급 기관 저장소에 자체 서명 인증서를 추가하십시오. 
2. 클라이언트 "설정" 창을 열고, "고급" 탭을 누른 다음 "HTTPS 동기화시 서버 인증서 검증하지 않음"을 표시하십시오.

## 자주 묻는 질문 및 문제 해결

### 4.2.x로 업그레이드한 다음 클라이언트에서 동기화하지 않음

이전 버전 클라이언트에서는 http 동기화에 실패했을 경우 비 http 동기회 프로토콜로 대신 처리합니다. 따라서 이전 클라이언트의 http 동기화 방식에 대한 오해를 할 수 있습니다. 다만, 실제로는 그렇지 않습니다. 클라이언트 4.2에서는 http 동기화를 배타적으로 처리하므로 더이상의 동기화 동작을 진행하지 않습니다. http 동기화를 수행하려면 서버를 제대로 설정해야합니다.

### Nginx/Apache에서 암호화 방식 설정

서버측에 강력한 암호를 설정해야합니다. 다음 Nginx 암호 목록은 잘 동작함을 시험하여 확인했습니다:

```
ssl_ciphers ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+3DES:!aNULL:!MD5:!DSS;
```

필요에 따라 목록을 적절히 설정하시는게 좋습니다.

