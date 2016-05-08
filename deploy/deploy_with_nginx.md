# Config Seahub with Nginx

## Important

According to the [security advisory](https://www.djangoproject.com/weblog/2013/aug/06/breach-and-django/) published by Django team, we recommend disable [GZip compression](http://wiki.nginx.org/HttpGzipModule) to mitigate [BREACH attack](http://breachattack.com/).

## Deploy Seahub/FileServer with Nginx

Seahub is the web interface of Seafile server. FileServer is used to handle raw file uploading/downloading through browsers. By default, it listens on port 8082 for HTTP request.

Here we deploy Seahub using [FastCGI](http://en.wikipedia.org/wiki/FastCGI), and deploy FileServer with reverse proxy. We assume you are running Seahub using domain '''www.myseafile.com'''.

This is a sample Nginx config file.

In Ubuntu 14.04, you can add the config file as follows:

1. create file `/etc/nginx/sites-available/seafile.conf`
2. Delete `/etc/nginx/sites-enabled/default`: `rm /etc/nginx/sites-enabled/default`
3. Create symbolic link: `ln -s /etc/nginx/sites-available/seafile.conf /etc/nginx/sites-enabled/seafile.conf`

```nginx
server {
    listen 80;
    server_name www.myseafile.com;

    proxy_set_header X-Forwarded-For $remote_addr;

    location / {
        fastcgi_pass    127.0.0.1:8000;
        fastcgi_param   SCRIPT_FILENAME     $document_root$fastcgi_script_name;
        fastcgi_param   PATH_INFO           $fastcgi_script_name;

        fastcgi_param	SERVER_PROTOCOL	    $server_protocol;
        fastcgi_param   QUERY_STRING        $query_string;
        fastcgi_param   REQUEST_METHOD      $request_method;
        fastcgi_param   CONTENT_TYPE        $content_type;
        fastcgi_param   CONTENT_LENGTH      $content_length;
        fastcgi_param	SERVER_ADDR         $server_addr;
        fastcgi_param	SERVER_PORT         $server_port;
        fastcgi_param	SERVER_NAME         $server_name;
        fastcgi_param   REMOTE_ADDR         $remote_addr;

        access_log      /var/log/nginx/seahub.access.log;
    	error_log       /var/log/nginx/seahub.error.log;
    	fastcgi_read_timeout 36000;
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

Nginx settings "client_max_body_size" is by default 1M. Uploading a file bigger than this limit will give you an error message HTTP error code 413 ("Request Entity Too Large").

You should use 0 to disable this feature or write the same value than for the parameter `max_upload_size` in section `[fileserver]` of [seafile.conf](../config/seafile-conf.md).

Tip for uploading very large files (> 4GB): By default Nginx will buffer large request body in temp file. After the body is completely received, Nginx will send the body to the upstream server (seaf-server in our case). But it seems when file size is very large, the buffering mechanism dosen't work well. It may stop proxying the body in the middle. So if you want to support file upload larger for 4GB, we suggest you install Nginx version >= 1.8.0 and add the following options to Nginx config file:

```nginx
    location /seafhttp {
        ... ...
        proxy_request_buffering off;
    }
```

## Modify ccnet.conf and seahub_setting.py

### Modify ccnet.conf

You need to modify the value of <code>SERVICE_URL</code> in [ccnet.conf](../config/ccnet-conf.md) to let Seafile know the domain you choose.

```python
SERVICE_URL = http://www.myseafile.com
```

Note: If you later change the domain assigned to seahub, you also need to change the value of  <code>SERVICE_URL</code>.

### Modify seahub_settings.py

You need to add a line in <code>seahub_settings.py</code> to set the value of `FILE_SERVER_ROOT` (or `HTTP_SERVER_ROOT` before version 3.1)

```python
FILE_SERVER_ROOT = 'http://www.myseafile.com/seafhttp'
```

## Start Seafile and Seahub

```bash
./seafile.sh start
./seahub.sh start-fastcgi
```

