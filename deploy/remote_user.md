## Overview

Starting from 7.0.0, Seafile can integrate with various Single Sign On systems via a proxy server. Examples include Apache as Shibboleth proxy, or LemonLdap as a proxy to LDAP servers, or Apache as Kerberos proxy. Seafile can retrieve user information from special request headers (HTTP_REMOTE_USER, HTTP_X_AUTH_USER, etc.) set by the proxy servers.

After the proxy server (Apache/Nginx) is successfully authenticated, the user information is set to the request header, and Seafile creates and logs in the user based on this information.

Note: Make sure that the proxy server has a corresponding security mechanism to protect against forgery request header attacks.

Please add the following settings to `conf/seahub_settings.py` to enable this feature.

```
ENABLE_REMOTE_USER_AUTHENTICATION = True

# Optional, HTTP header, which is configured in your web server conf file,
# used for Seafile to get user's unique id, default value is 'HTTP_REMOTE_USER'.
REMOTE_USER_HEADER = 'HTTP_REMOTE_USER'

# Optional, when the value of HTTP_REMOTE_USER is not a valid email address，
# Seafile will build a email-like unique id from the value of 'REMOTE_USER_HEADER'
# and this domain, e.g. user1@example.com.
REMOTE_USER_DOMAIN = 'example.com'

# Optional, whether to create new user in Seafile system, default value is True.
# If this setting is disabled, users doesn't preexist in the Seafile DB cannot login.
# The admin has to first import the users from external systems like LDAP.
REMOTE_USER_CREATE_UNKNOWN_USER = True

# Optional, whether to activate new user in Seafile system, default value is True.
# If this setting is disabled, user will be unable to login by default.
# the administrator needs to manually activate this user.
REMOTE_USER_ACTIVATE_USER_AFTER_CREATION = True

# Optional, map user attribute in HTTP header and Seafile's user attribute.
REMOTE_USER_ATTRIBUTE_MAP = {
    'HTTP_DISPLAYNAME': 'name',
    'HTTP_MAIL': 'contact_email',

    # for shibboleth user info
    "HTTP_GIVENNAME": 'givenname',
    "HTTP_SN": 'surname',
    "HTTP_ORGANIZATION": 'institution',
    
    # for shibboleth user role
    'HTTP_Shibboleth-affiliation': 'affiliation',
}

# for shibboleth user role
SHIBBOLETH_AFFILIATION_ROLE_MAP = {
    'employee@uni-mainz.de': 'staff',
    'member@uni-mainz.de': 'staff',
    'student@uni-mainz.de': 'student',
    'employee@hu-berlin.de': 'guest',
    'patterns': (
        ('*@hu-berlin.de', 'guest1'),
        ('*@*.de', 'guest2'),
        ('*', 'guest'),
    ),
}
```

Then restart Seafile.
