# 使用 memcached

Seahub caches items (avatars, profiles, etc) on the file system in /tmp/seahub_cache/ by default. You can replace it with Memcached. You need to install

* memcached
* python memcached module (python-memcache or python-memcached)

然后在 **seahub_settings.py** 中加入以下配置信息.

```
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
```

