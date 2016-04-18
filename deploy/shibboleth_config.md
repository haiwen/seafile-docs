## Overview

[Shibboleth](https://shibboleth.net/) is a widely used single sign on (SSO) protocol. Seafile server (Community Edition >= 4.1.0, Pro Edition >= 4.0.6) supports authentication via Shibboleth. It allows users from another organization to log in to Seafile without registering an account on the service provider.

In this documentation, we assume the reader is familiar with Shibboleth installation and configuration. For introduction to Shibboleth concepts, please refer to https://wiki.shibboleth.net/confluence/display/SHIB2/UnderstandingShibboleth .

Shibboleth Service Provider (SP) should be installed on the same server as the Seafile server. The official SP from https://shibboleth.net/ is implemented as an Apache module. The module handles all Shibboleth authentication details. Seafile server receives authentication information (username) from fastcgi. The username then can be used as login name for the user.

Seahub provides a special URL to handle Shibboleth login. The URL is `https://your-server/shib-login`. Only this URL needs to be configured under Shibboleth protection. All other URLs don't go through the Shibboleth module. The overall workflow for a user to login with Shibboleth is as follows:

1. In the Seafile login page, there is a separate "Shibboleth" login button. When the user clicks the button, she/he will be redirected to `https://your-server/shib-login`.
2. Since that URL is controlled by Shibboleth, the user will be redirected to IdP for login. After the user logs in, she/he will be redirected back to `https://your-server/shib-login`.
3. This time the Shibboleth module passes the request to Seahub. Seahub reads the user information from the request and brings the user to her/his home page.
4. All later access to Seahub will not pass through the Shibboleth module. Since Seahub keeps session information internally, the user doesn't need to login again until the session expires.

Since Shibboleth support requires Apache, if you want to use Nginx, you need two servers, one for non-Shibboleth access, another configured with Apache to allow Shibboleth login. In a cluster environment, you can configure your load balancer to direct traffic to different server according to URL. Only the URL `https://your-server/shib-login` needs to be directed to Apache.

The configuration includes 3 steps:

1. Install and configure Shibboleth Service Provider;
2. Configure Apache;
3. Configure Seahub.

## Install and Configure Shibboleth Service Provider

Installation and configuration of Shibboleth is out of the scope of this documentation. Here are a few references:

* For RedHat and SUSE: https://wiki.shibboleth.net/confluence/display/SHIB2/NativeSPLinuxInstall
* For Ubuntu: http://bradleybeddoes.com/2011/08/12/installing-a-shibboleth-2-sp-in-ubuntu-11-04-within-virtualbox/

Please note that you don't have to follow the Apache configurations in the above links. Just use the Apache config we provide in the next section.

## Apache Configuration

You should create a new virtual host configuration for Shibboleth.

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

After restarting Apache, you should be able to get the Service Provider metadata by accessing https://seafile.example.com/Shibboleth.sso/Metadata . This metadata should be uploaded to the Identity Provider (IdP) server.

## Configure Seahub

Seahub extracts the username from the `REMOTE_USER` environment variable. So you should modify your SP's shibboleth2.xml (/etc/shibboleth/shibboleth2.xml on Ubuntu) config file, so that Shibboleth translates your desired attribute into `REMOTE_USER` environment variable.

```
    <ApplicationDefaults entityID="https://your-server/shibboleth"
        REMOTE_USER="xxxx">
```

In Seafile, only one of the following two attributes can be used for username: `eppn`, and `mail`. `eppn` stands for "Edu Person Principal Name". It is usually the UserPrincipalName attribute in Active Directory. It's not necessarily a valid email address. `mail` is the user's email address. You should set `REMOTE_USER` to either one of these attributes.

Now we have to tell Seahub how to do with the authentication information passed in by Shibboleth.

Add the following configuration to seahub_settings.py.

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

Since version 5.0, Seahub can process additional user attributes from Shibboleth. These attributes are saved into Seahub's database, as user's properties. They're all not mandatory. The internal user properties Seahub now supports are:

- givenname
- surname
- contact_email: used for sending notification email to user if username is not a valid email address (like eppn).
- institution: used to identify user's institution

You can specify the mapping between Shibboleth attributes and Seahub's user properties in seahub_settings.py:

```
SHIBBOLETH_ATTRIBUTE_MAP = {
    "eppn": (False, "username"),
    "givenname": (False, "givenname"),
    "sn": (False, "surname"),
    "mail": (False, "contact_email"),
    "organization": (False, "institution"),
}
```

In the above config, the hash key is Shibboleth attribute name, the second element in the hash value is Seahub's property name. You can adjust the Shibboleth attribute name for your own needs. ***Note that you may have to change attribute-map.xml in your Shibboleth SP, so that the desired attributes are passed to Seahub. And you have to make sure the IdP sends these attributes to the SP.***

Since version 5.1.1, we added an option `SHIB_ACTIVATE_AFTER_CREATION` (defaults to `True`) which control the user status after shibboleth connection. If this option set to `False`, user will be inactive after connection, and system admins will be notified by email to activate that account.

## Verify

After restarting Apache and Seafile services, you can then test the shibboleth login workflow.
