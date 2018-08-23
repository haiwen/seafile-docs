# Enabling Https with Nginx

Here we suggest you use [Let’s Encrypt](https://letsencrypt.org/getting-started/) to get a certificate from a Certificate Authority (CA). If you use a paid ssl certificate from some authority, just skip the first step.

### Generate SSL certificate

For users who use Let’s Encrypt, you can obtain a valid certificate via [Certbot ACME client](https://certbot.eff.org/)

On Ubuntu systems, the Certbot team maintains a PPA. Once you add it to your list of repositories all you'll need to do is apt-get the following packages.

```bash
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install python-certbot-nginx
```

Certbot has an Nginx plugin, which is supported on many platforms, and automates both obtaining and installing certs:

```bash
sudo certbot --nginx
```

Running this command will get a certificate for you and have Certbot edit your Nginx configuration automatically to serve it. If you're feeling more conservative and would like to make the changes to your Nginx configuration by hand, you can use the certonly subcommand:

```bash
sudo certbot --nginx certonly
```

To learn more about how to use Certbot you can read threir [documentation](https://certbot.eff.org/docs/).

> If you're using a custom CA to sign your SSL certificate, you have to enable certificate revocation list (CRL) in your certificate. Otherwise http syncing on Windows client may not work. See [this thread](https://forum.seafile-server.org/t/https-syncing-on-windows-machine-using-custom-ca/898) for more information.

### Enable SSL module of Nginx (optional)

If your Nginx does not support SSL, you need to recompile it, the commands are as follows:

```bash
    ./configure --with-http_stub_status_module --with-http_ssl_module
    make && make install
```

### Modify Nginx configuration file

Assume you have configured nginx as [Deploy-Seafile-with-nginx](deploy_with_nginx.md). To use https, you need to modify your nginx configuration file.

```nginx
server {
    listen       80;
    server_name  seafile.example.com;
    rewrite ^ https://$http_host$request_uri? permanent;	# force redirect http to https

    # Enables or disables emitting nginx version on error pages and in the "Server" response header field.
    server_tokens off;
}

server {
    listen 443;
    ssl on;
    ssl_certificate /etc/ssl/cacert.pem;    	# path to your cacert.pem
    ssl_certificate_key /etc/ssl/privkey.pem;	# path to your privkey.pem
    server_name seafile.example.com;
    server_tokens off;
    # ......
    proxy_pass         http://127.0.0.1:8000;
    proxy_set_header   Host $host;
    proxy_set_header   X-Real-IP $remote_addr;
    proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header   X-Forwarded-Host $server_name;
    proxy_set_header   X-Forwarded-Proto https;

    proxy_read_timeout  1200s;
}
```

### Sample configuration file

#### Generate DH params
(this takes some time)
```bash
    openssl dhparam 2048 > /etc/nginx/dhparam.pem
```

Here is the sample configuration file:

```nginx
    server {
        listen       80;
        server_name  seafile.example.com;
        rewrite ^ https://$http_host$request_uri? permanent;	# force redirect http to https
        server_tokens off;
    }
    server {
        listen 443;
        ssl on;
        ssl_certificate /etc/ssl/cacert.pem;        # path to your cacert.pem
        ssl_certificate_key /etc/ssl/privkey.pem;	# path to your privkey.pem
        server_name seafile.example.com;
        ssl_session_timeout 5m;
        ssl_session_cache shared:SSL:5m;

        # Diffie-Hellman parameter for DHE ciphersuites, recommended 2048 bits
        ssl_dhparam /etc/nginx/dhparam.pem;

        # secure settings (A+ at SSL Labs ssltest at time of writing)
        # see https://wiki.mozilla.org/Security/Server_Side_TLS#Nginx
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_ciphers 'ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:DHE-RSA-CAMELLIA256-SHA:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-SEED-SHA:DHE-RSA-CAMELLIA128-SHA:HIGH:!aNULL:!eNULL:!LOW:!3DES:!MD5:!EXP:!PSK:!SRP:!DSS';
        ssl_prefer_server_ciphers on;

        proxy_set_header X-Forwarded-For $remote_addr;

        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
        server_tokens off;

        location / {
            proxy_pass         http://127.0.0.1:8000;
            proxy_set_header   Host $host;
            proxy_set_header   X-Real-IP $remote_addr;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Host $server_name;
            proxy_set_header   X-Forwarded-Proto https;

            access_log      /var/log/nginx/seahub.access.log;
    	    error_log       /var/log/nginx/seahub.error.log;

            proxy_read_timeout  1200s;

            client_max_body_size 0;
        }
# If you are using [FastCGI](http://en.wikipedia.org/wiki/FastCGI),
# which is not recommended, you should use the following config for location `/`.
#
#    location / {
#         fastcgi_pass    127.0.0.1:8000;
#         fastcgi_param   SCRIPT_FILENAME     $document_root$fastcgi_script_name;
#         fastcgi_param   PATH_INFO           $fastcgi_script_name;
#
#         fastcgi_param	 SERVER_PROTOCOL	 $server_protocol;
#         fastcgi_param   QUERY_STRING        $query_string;
#         fastcgi_param   REQUEST_METHOD      $request_method;
#         fastcgi_param   CONTENT_TYPE        $content_type;
#         fastcgi_param   CONTENT_LENGTH      $content_length;
#         fastcgi_param	 SERVER_ADDR         $server_addr;
#         fastcgi_param	 SERVER_PORT         $server_port;
#         fastcgi_param	 SERVER_NAME         $server_name;
#         fastcgi_param   REMOTE_ADDR         $remote_addr;
#     	 fastcgi_read_timeout 36000;
#
#         client_max_body_size 0;
#
#         access_log      /var/log/nginx/seahub.access.log;
#     	 error_log       /var/log/nginx/seahub.error.log;
#    }

        location /seafhttp {
            rewrite ^/seafhttp(.*)$ $1 break;
            proxy_pass http://127.0.0.1:8082;
            client_max_body_size 0;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
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

### Large file uploads

Tip for uploading very large files (> 4GB): By default Nginx will buffer large request body in temp file. After the body is completely received, Nginx will send the body to the upstream server (seaf-server in our case). But it seems when file size is very large, the buffering mechanism dosen't work well. It may stop proxying the body in the middle. So if you want to support file upload larger for 4GB, we suggest you install Nginx version >= 1.8.0 and add the following options to Nginx config file:

```nginx
    location /seafhttp {
        ... ...
        proxy_request_buffering off;
    }

```

If you have WebDAV enabled it is recommended to add the same:

```nginx
    location /seafdav {
        ... ...
        proxy_request_buffering off;
    }
```

### Reload Nginx
```bash
    nginx -s reload
```

## Modify settings to use https

### ccnet conf

Since you changed from http to https, you need to modify the value of `SERVICE_URL` in [ccnet.conf](../config/ccnet-conf.md). You can also modify `SERVICE_URL` via web UI in "System Admin->Settings". (**Warning**: If you set the value both via Web UI and ccnet.conf, the setting via Web UI will take precedence.)

```bash
SERVICE_URL = https://seafile.example.com
```

### seahub_settings.py

You need to add a line in seahub_settings.py to set the value of `FILE_SERVER_ROOT`. You can also modify `FILE_SERVER_ROOT` via web UI in "System Admin->Settings". (**Warning**: If you set the value both via Web UI and seahub_settings.py, the setting via Web UI will take precedence.)

```python
FILE_SERVER_ROOT = 'https://seafile.example.com/seafhttp'
```

### Change Seafile config

Update the [configuration](../config/seafile-conf.md#seafile-fileserver-configuration
) of seafile fileserver is in the `[fileserver]` section of the file `seafile.conf` to local ip `127.0.0.1`

```
[fileserver]
# bind address for fileserver
# default to 0.0.0.0, if deployed without proxy: no access restriction
# set to 127.0.0.1, if used with local proxy: only access by local
host = 127.0.0.1
```

## Start Seafile and Seahub

```bash
./seafile.sh start
./seahub.sh start # or "./seahub.sh start-fastcgi" if you're using fastcgi
```

## Additional modern settings for nginx (optional)

### Activate IPv6

Require IPv6 on server otherwise the server will not start! Also the AAAA dns record is required for IPv6 usage.

```nginx
listen 443;
listen [::]:443;
```

### Activate HTTP2

Activate HTTP2 for more performance. Only available for SSL and nginx version>=1.9.5. Simply add `http2`.
```nginx
listen 443 http2;
listen [::]:443 http2;
```

## Additional security settings for nginx (optional)

### Force https on next visit

Add the HSTS header. If you already visited the https version the next time your browser will directly visit the https site and not the http one. Prevent man-in-the-middle-attacks:
```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
```

### Obfuscate nginx version

Disable exact server version in header. Prevent scans for vulnerable server.
**This should be added to every server block, as it shall obfuscate the version of nginx.**
```nginx
server_tokens off;
```

## Test your server

To check your configuration you can use the service from ssllabs: https://www.ssllabs.com/ssltest/index.html .
