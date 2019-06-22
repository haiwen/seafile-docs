## Kerberos

NOTE: Since version 7.0, this documenation is deprecated. Users should use Apache as a proxy server for Kerberos authentication. Then configure Seahub by the instructions in [Remote User Authentication](remote_user.md).

[Kerberos](https://web.mit.edu/kerberos/) is a widely used single sign on (SSO) protocol. Seafile server supports authentication via Kerberos. It allows users to log in to Seafile without entering credentials again if they have a kerberos ticket.

In this documentation, we assume the reader is familiar with Kerberos installation and configuration.

Seahub provides a special URL to handle Kerberos login. The URL is `https://your-server/krb5-login`. Only this URL needs to be configured under Kerberos protection. All other URLs don't go through the Kerberos module. The overall workflow for a user to login with Kerberos is as follows:

1. In the Seafile login page, there is a separate "Kerberos" login button. When the user clicks the button, it will be redirected to `https://your-server/krb5-login`.
2. Since that URL is controlled by Kerberos, the apache module will try to get a Ticket from the Kerberos server.
3. Seahub reads the user information from the request and brings the user to its home page.
4. Further requests to Seahub will not pass through the Kerberos module. Since Seahub keeps session information internally, the user doesn't need to login again until the session expires.

The configuration includes three steps:

1. Get a keytab for Apache from Kerberos
2. Configure Apache
3. Configure Seahub

## Get keytab for Apache

Store the keytab under the name defined below and make it accessible only to the apache user (e.g. httpd or www-data and chmod 600).

## Apache Configuration

You should create a new location in your virtual host configuration for Kerberos.

```
<IfModule mod_ssl.c>
    <VirtualHost _default_:443>
        ServerName seafile.example.com
        DocumentRoot /var/www
...
        <Location /krb5-login/>
            SSLRequireSSL
            AuthType Kerberos
            AuthName "Kerberos EXAMPLE.ORG"
            KrbMethodNegotiate On
            KrbMethodK5Passwd On
            Krb5KeyTab /etc/apache2/conf.d/http.keytab
            #ErrorDocument 401 '<html><meta http-equiv="refresh" content="0; URL=/accounts/login"><body>Kerberos authentication did not pass.</body></html>'
            Require valid-user
        </Location>
...
    </VirtualHost>
</IfModule>

```

After restarting Apache, you should see in the Apache logs that user@REALM is used when accessing https://seafile.example.com/krb5-login/.

## Configure Seahub

Seahub extracts the username from the `REMOTE_USER` environment variable. 

Now we have to tell Seahub what to do with the authentication information passed in by Kerberos.

Add the following option to seahub_settings.py.

```
ENABLE_KRB5_LOGIN = True
```

## Verify

After restarting Apache and Seafile services, you can test the Kerberos login workflow.
