# Add memcached

Seahub caches items (avatars, profiles, etc) on the file system in /tmp/seahub_cache/ by default. You can use memcached instead to improve the performance.

First, make sure `libmemcached` library and development headers are installed on your system.

On Ubuntu 16.04 (`apt-get install python-dev`) and CentOS 7 (`yum install python-devel`) you can install it using the systems package manager.

```
sudo apt-get install libmemcached-dev
```

Install Python memcache library.

```
sudo pip install pylibmc
sudo pip install django-pylibmc
```

Add the following configuration to `seahub_settings.py`.

```
CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
    },
    'locmem': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}
COMPRESS_CACHE_BACKEND = 'locmem'

```

If you use a memcached cluster, your configuration depends on your Seafile server version. You can find how to setup memcached cluster [here](../deploy_pro/memcached_mariadb_cluster.md).

### Seafile server before 6.2.11

Please replace the `CACHES` variable with the following. This configuration uses consistent hashing to distribute the keys in memcached. More information can be found on [pylibmc documentation](http://sendapatch.se/projects/pylibmc/behaviors.html) and [django-pylibmc documentation](https://github.com/django-pylibmc/django-pylibmc). Supposed your memcached server addresses are 192.168.1.13[4-6].

```
CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': ['192.168.1.134:11211', '192.168.1.135:11211', '192.168.1.136:11211',],
        'OPTIONS': {
            'ketama': True,
            'remove_failed': 1,
            'retry_timeout': 3600,
            'dead_timeout': 3600
        }
    },
    'locmem': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}
COMPRESS_CACHE_BACKEND = 'locmem'
```

### Seafile Server 6.2.11 or newer

The configuration is the same as single node memcached server. Just replace the IP address with the floating IP.
