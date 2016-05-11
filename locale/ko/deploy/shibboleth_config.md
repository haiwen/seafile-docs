## 둘러보기

[Shibboleth](https://shibboleth.net/)는 널리 사용하는 단일 접속(SSO) 프로토콜입니다. Seafile 서버(커뮤니티판 >= 4.1.0, 전문가판 >= 4.0.6)에서는 시볼레스 인증을 지원합니다. 시볼레스는 다른 조직 구성원이 서비스 제공 업체에 계정을 등록하지 않고도 Seafile에 로그인할 수 있게 합니다.

이 문서에서는, 독자 여러분이 시볼레스 설치 및 설정을 어느정도 할 줄 안다고 가정하겠습니다. 시볼레스 개념 소개는 https://wiki.shibboleth.net/confluence/display/SHIB2/UnderstandingShibboleth 주소를 참고하십시오.

시볼레스 서비스 제공자(SP)를 Seafile 서버와 동일한 서버에 설치해야합니다. 공식 SP는 https://shibboleth.net/ 에 있으며 아파치 모듈로 구현했습니다. 이 모듈은 모든 시볼레스 인증 세부 절차를 다룹니다. Seafile 서버는 인증 정보(사용자 이름)을 fastcgi로 받습니다. 그 다음 사용자 이름을 사용자의 로그인 이름으로 사용할 수 있습니다.

Seahub에서는 시볼레스 로그인을 처리하는 특별한 URL을 제공합니다. `https://your-server/shib-login` 입니다. 이 URL은 시볼레스 보안하에 설정해야합니다. 다른 URL은 시볼레스 모듈로 접근할 수 없습니다. 시볼레스 사용자 로그인 전체 흐름은 다음과 같습니다:

1. Seafile 로그인 페이지에서 "시볼레스" 로그인 단추가 따로 있습니다. 이 단추를 사용자가 누르면 `https://your-server/shib-login`으로 이동합니다.
2. 이 URL은 시볼레스로 통제하므로, 사용자는 로그인 할 IdP로 이동합니다. 사용자 로그인이 끝나면 `https://your-server/shib-login`으로 돌아갑니다.
3. 여기서 시볼레스 모듈은 Seahub에 요청을 전달합니다. Seahub는 요청에서 사용자 정보를 읽고, 자신의 홈페이지로 사용자를 안내합니다.
4. 이후 모든 Seahub로의 접근은 시볼레스 모듈로 전달하지 않습니다. Seahub는 자체적으로 세션 정보를 유지하므로, 사용자는 세션이 끝나기 전까지는 다시 로그인 할 필요가 없습니다.

시볼레스 지원은 아파치가 필요하므로, Nginx를 사용하면, 비-시볼레스 접근용 서버와 시볼레스 로그인을 할 수 있도록 설정한 아파치 서버가 필요합니다. 클러스터 환경에서는 URL에 따라 제각기 다른 서버로 트래픽을 전달하는 로드 밸런서를 설정할 수 있습니다. 아파치에는 `https://your-server/shib-login` URL 주소로만 안내하면 됩니다.

설정은 3단계로 진행합니다:

1. 시볼레스 서비스 제공자를 설치하고 설정하십시오
2. Apache를 섲렁하십시오
3. Seahub를 설정하십시오.

## 시볼레스 서비스 제공자 설치 및 설정

시볼레스 설치 및 설정은 이 문서의 범위를 벗어납니다. 다음 몇가지 참고 자료가 있습니다:

* 레드햇 및 수세: https://wiki.shibboleth.net/confluence/display/SHIB2/NativeSPLinuxInstall
* 우분투: http://bradleybeddoes.com/2011/08/12/installing-a-shibboleth-2-sp-in-ubuntu-11-04-within-virtualbox/

위 링크의 아파치 설정을 따를 필요가 없다는 점 참고하십시오. 다음 섹션에서 제공하는 아파치 설정을 활용하십시오.

## Apache 설정

시볼레스 새 가상 호스트 설정을 만들어야합니다.

```
<IfModule mod_ssl.c>
    <VirtualHost _default_:443>
        ServerName seafile.example.com
        DocumentRoot /var/www
        #Alias /seafmedia  /home/ubuntu/dev/seahub/media
        Alias /media /home/user/seafile-server-latest/seahub/media

        ErrorLog ${APACHE_LOG_DIR}/seahub.error.log
        CustomLog ${APACHE_LOG_DIR}/seahub.access.log combined

        SSLEngine on
        SSLCertificateFile  /path/to/ssl-cert.pem
        SSLCertificateKeyFile /path/to/ssl-key.pem

        <Location /Shibboleth.sso>
        SetHandler shib
        </Location>

        <Location /api2>
        AuthType None
        Require all granted
        Allow from all
        satisfy any
        </Location>

        RewriteEngine On
        <Location /media>
        Require all granted
        </Location>

        <Location /shib-login>
        AuthType shibboleth
        ShibRequestSetting requireSession true
        Require valid-user
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
        RewriteRule ^/(media.*)$ /$1 [QSA,L,PT]
        RewriteCond %{REQUEST_FILENAME} !-f
        RewriteCond %{REQUEST_URI} !^/Shibboleth.sso
        RewriteRule ^(.*)$ /seahub.fcgi$1 [QSA,L,E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]

    </VirtualHost>
</IfModule>

```

Apache를 다시 시작하고 나면, https://seafile.example.com/Shibboleth.sso/Metadata에 접근하여 서비스 제공 업체 메타데이터를 가져와야합니다. 이 메타데이터는 인증 제공 업체(IdP) 서버 업체에 업로드합니다.

## Seahub 설정

Seahub는 `REMOTE_USER` 환경 변수에서 사용자 이름을 가져옵니다. 따라서 SP의 shibboleth2.xml 설정 파일을 수정하여 `REMOTE_USER` 환경 변수에 원하는 속성 값을 시볼레스가 해셕할 수 있게 해야 합니다.

```
    <ApplicationDefaults entityID="https://your-server/shibboleth"
        REMOTE_USER="xxxx">
```

Seafile에서는 `eppn` 및 `mail` 두가지 속성 중 하나만 사용자 이름으로 간주할 수 있습니다. `eppn`은 "Edu Person Principal Name" 입니다. 액티브 디렉터리에서 보통 UserPrincipalName입니다. 올바른 전자메일 주소는 필요하지 않습니다. `mail`은 사용자의 전자메일 주소입니다. `REMOTE_USER`를 앞에서 언급한 속성 값 중 하나로 설정해야합니다.

이제 시볼레스 방식으로 전달하는 인증 정보를 어떻게 Seahub에 전달하는지 알릴 차례입니다.

seahub_settings.py에 다음 설정 내용을 추가하십시오.

```
EXTRA_AUTHENTICATION_BACKENDS = (
    'shibboleth.backends.ShibbolethRemoteUserBackend',
)
EXTRA_MIDDLEWARE_CLASSES = (
    'shibboleth.middleware.ShibbolethRemoteUserMiddleware',
)

ENABLE_SHIB_LOGIN = True

SHIBBOLETH_ATTRIBUTE_MAP = {
    # Change eppn to mail if you use mail attribute for REMOTE_USER
    "eppn": (False, "username"),
}
```

버전 5.0부터, Seahub는 시볼레스 추가 사용자 속성을 처리할 수 있습니다. 해당 속성은 Seahub 데이터베이스에 사용자 속성으로 저장합니다. 모든 속성이 필수는 아닙니다. Seahub에서 현재 자체 사용자 속성으로 지원하는 항목은 다음과 같습니다:

- 이름
- 성
- contact_email: 사용자 이름이 올바른 전자메일 주소가 아닐 경우 사용자에게 알림 전자메일을 보낼 때 사용할 전자메일 주소(eppn과 유사).
- institution: used to identify user's institution

시볼레스 속성 및 Seahub 사용자 속성 매핑을 seahub_settings.py에서 지정할 수 있습니다:

```
SHIBBOLETH_ATTRIBUTE_MAP = {
    "eppn": (False, "username"),
    "givenname": (False, "givenname"),
    "sn": (False, "surname"),
    "mail": (False, "contact_email"),
    "organization": (False, "institution"),
}
```

위 설정에서 해시 키는 시볼레스 속성 이름이며, 해시 값의 두번째 항목은 Seahub의 속성 이름입니다. 시볼레스 속성 이름을 원하는대로 조정할 수 있습니다. ***참고로 시볼레스 SP의 attribute-mal.xml를 수정하여 Seahub에 원하는 속성 값을 전달할 수 있게 하십시오. 그리고 IdP에서 SP로 이 속성 값을 전달하는지 확인해야합니다.***

버전 5.1.1부터 시볼레스 연결 후 사용자 상태를 처리하는 `SHIB_ACTIVATE_AFTER_CREATION` (기본값 `True`) 설정 항목을 추가했습니다. 이 항목을 `False`로 설정하면, 사용자 연결 후 비활성 상태가 되며, 시스템 관리자는 사용자 계정을 활성화 하라는 전자메일 알림을 받습니다.

## 검증

Apache 및 Seafile 서비스를 다시 시작하고 나면, 시볼레스 로그인 절차를 시험해볼 수 있습니다.

