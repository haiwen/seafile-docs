# Configure Syncing via HTTP Protocol

Starting from version 4.0.0, Seafile supports file syncing via HTTP protocol. The server configuration depends on which version of Seafile client do you use.

Client version >= 4.2 use http syncing protocol exclusively, the cases are

* If you're not using https, you don't have to configure Nginx or Apache to use http sync. The client can talk directly with the file server on port 8082.
* If you're using https, you have to configure Nginx or Apache.

If you'are using clients version < 4.2,

* If you want to use http(s) sync, you have to configure Nginx or Apache.
* If you don't configure Nginx or Apache, the client falls back to use non-http syncing protocol (using port 10001 and 12001).

Servers >= 4.0 are compatible with all syncing protocols, any version of client should work with the server.

## Nginx

Follow [this guide](deploy_with_nginx.md) to configure Nginx without HTTPS, or [this guide](https_with_nginx.md) to configure Nginx with HTTPS.

The section in Nginx config file related to HTTP sync is

```
    location /seafhttp {
        rewrite ^/seafhttp(.*)$ $1 break;
        proxy_pass http://127.0.0.1:8082;
        client_max_body_size 0;
        proxy_connect_timeout  36000s;
        proxy_read_timeout  36000s;
    }
```

there are two things to note:

* You must use the path "/seafhttp" for http syncing. This is hard coded in the client.
* You should add the "client_max_body_size" configuration. The value should be set to 0 (means no limit) or 100M (suffice for most cases).

## Apache

Follow [this guide](deploy_with_apache.md) to configure Apache without HTTPS, or [this guide](https_with_apache.md) to configure Nginx with HTTPS.

The section in Apache config file related to HTTP sync is

```
    #
    # seafile fileserver
    #
    ProxyPass /seafhttp http://127.0.0.1:8082
    ProxyPassReverse /seafhttp http://127.0.0.1:8082
    RewriteRule ^/seafhttp - [QSA,L]
```

Note that you must use the path "/seafhttp" for http syncing. This is hard coded in the client.

## Client Side Configuration for HTTPS

If you buy a valid SSL certificate, the syncing should work out of the box. If you use self-signed certificate, when you first add an account on the client, it'll pop up a window for you to confirm the server's certificate. If you choose to accept the certificate, the client will use that for https connection.

The client loads trusted CA list from the system trusted CA store on start. It then combines those CA list with the user accepted certificates. The combined list is then used for certificate verification.

If you follow certificate generation instruction in [this guide](https_with_nginx.md) to generate your self-signed certificate, the syncing should work after confirmation.

There may be cases when you can't establish https connection to the server. You can try two work-arounds:

1. Add your self-signed certificate to system trusted CA store. 
2. Open the client "settings" window, in "advanced" tab, check "Do not verifiy server certificate in HTTPS sync".

## FAQ and Trouble Shooting

### My Client Doesn't Sync after Upgrading to 4.2.x

Older clients fall back to non-http sync protocol if http sync fails. So you may get the false sense that the old client works with http sync. But actually it doesn't. Client 4.2 use http sync exclusively, so it doesn't sync any more. You have to correctly configure the server for http sync.

### Choosing Ciphers on Nginx/Apache

You should choose strong ciphers on the server side. The following Nginx cipher list is tested to be working fine:

```
ssl_ciphers ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+3DES:!aNULL:!MD5:!DSS;
```

You may fine tune the list to meet your needs.


