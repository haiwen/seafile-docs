# Config Seahub with Traefik

## Deploy Seahub/FileServer with Traefik

Seahub is the web interface of Seafile server. FileServer is used to handle raw file uploading/downloading through browsers. By default, it listens on port 8082 for HTTP requests.

Here we deploy Seahub and FileServer with the [Traefik](https://traefik.io) reverse proxy. We assume you are running Seahub using domain `seafile.example.com`.

### Configuring Traefik with a Configuration File
Traefik can be configured in the main `traefik.toml` file, and / or in files specified therein.  Here is an example of configuring Traefik's configuration file for a locally installed instance of Seafile:

```toml
[backends]
  [backends.seafapp]
    [backends.seafapp.servers.primary]
      url = "http://127.0.0.1:8000"
      weight = 1
  [backends.seafdav]
    [backends.seafdav.servers.primary]
      url = "http://127.0.0.1:8080"
      weight = 1
  [backends.seafile]
    [backends.seafhttp.servers.primary]
      url = "http://127.0.0.1:8082"
      weight = 1

[frontends]
   [frontends.seafapp]
     backend = "seafapp"
     [frontends.seafapp.routes]
       [frontends.seafapp.routes.primary]
         rule = "Host:seafile.example.com"
   [frontends.seafdav]
     backend = "seafdav"
     [frontends.seafdav.routes]
       [frontends.seafdav.routes.primary]
         rule = "Host:seafile.example.com;PathPrefixStrip:/seafdav"
   [frontends.seafhttp]
     backend = "seafhttp"
     [frontends.seafhttp.routes]
       [frontends.seafhttp.routes.primary]
         rule = "Host:seafile.example.com;PathPrefixStrip:/seafhttp"
```

Note that this is valid for a locally installed instance of Traefik, or a Traefik container running with NET=HOST.  If Traefik is running in a container without these privelages, `host.docker.internal` or an address bound to the host's loopback interface should be substituted for `127.0.0.1`.

### Proxying the Official Docker Image
The official Docker image for Seafile has a built-in Nginx server that proxies the `/seafhttp` and `/seafdav` paths to their respective ports.  Thus the official Docker image can be proxied simply by making Traefik aware through labels:

```yaml
services:
  seafile:
    labels:
      - traefik.docker.network=traefik
      - traefik.enable=true
      - traefik.frontend.rule=Host:seafile.example.com
      - traefik.port=80
    networks:
      - traefik
```

### Proxying Unofficial Docker Images
In Docker images that do not include their own proxy, Traefik can handle proxying the `/seafhttp` and `/seafdav` paths to the right ports through segment labels:

```yaml
services:
  seafile:
    labels:
      - traefik.docker.network=traefik
      - traefik.enable=true
      - traefik.seafapp.backend=Seafile Web App
      - traefik.seafapp.frontend.rule=Host:seafile.example.com
      - traefik.seafdav.port=8000
      - traefik.seafdav.backend=Seafile WebDAV Server
      - traefik.seafdav.frontend.rule=Host:seafile.example.com;PathPrefixStrip:/seafdav
      - traefik.seafdav.port=8080
      - traefik.seafhttp.backend=Seafile File Server
      - traefik.seafhttp.frontend.rule=Host:seafile.example.com;PathPrefixStrip:/seafhttp
      - traefik.seafhttp.port=8082
    networks:
      - traefik
```
## Modify ccnet.conf and seahub_setting.py

### Modify ccnet.conf

You need to modify the value of `SERVICE_URL` in [ccnet.conf](../config/ccnet-conf.md) to let Seafile know the domain, protocol and port you choose. You can also modify `SERVICE_URL` via web UI in "System Admin->Settings". (**Warning**: If you set the value both via Web UI and ccnet.conf, the setting via Web UI will take precedence.)

```python
SERVICE_URL = http://seafile.example.com
```

Note: If you later change the domain assigned to Seahub, you also need to change the value of  `SERVICE_URL`.

### Modify seahub_settings.py

You need to add a line in `seahub_settings.py` to set the value of `FILE_SERVER_ROOT`. You can also modify `FILE_SERVER_ROOT` via web UI in "System Admin->Settings". (**Warning**: if you set the value both via Web UI and seahub_settings.py, the setting via Web UI will take precedence.)


```python
FILE_SERVER_ROOT = 'http://seafile.example.com/seafhttp'
```

## Start Seafile and Seahub

```bash
./seafile.sh start
./seahub.sh start # or "./seahub.sh start-fastcgi" if you're using fastcgi
```
