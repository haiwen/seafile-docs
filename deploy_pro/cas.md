# Log In By CAS

Since Seafile-pro 6.3.0, Seafile supports CAS single-sign-on protocol.

## Requirements

Supposed you have a usable CAS service, and the service can be accessed by the `https://<CAS-SERVER-IP>:<PORT>/cas/`.

## configure seahub_settings.py

- Add the following lines in `conf/seahub_settings.py`

```
ENABLE_CAS = True
CAS_SERVER_URL = 'https://192.168.99.100:8443/cas/'
CAS_LOGOUT_COMPLETELY = True
# Uncomment following line if CAS server is using self-signed certificate
#CAS_SERVER_CERT_VERIFY = False
```

- Restart the seahub

```
./seahub.sh restart
```

Now, you can login to Seafile web interface with CAS authentication. Please click the "Single Sign-on" on the Seafile's login page.
