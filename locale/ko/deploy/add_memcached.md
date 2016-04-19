# memcached 추가

Seahub는 기본적으로 /tmp/seahub_cache에 사용자 계정 항목(아바타, 프로파일 등)을 캐싱합니다. 이 부분을 memcached로 대체할 수 있습니다. 다음 항목을 설치하시고

* memcached
* 파이썬 memcached 모듈 (python-memcache 또는 python-memcached)

다음 줄을 **seahub_settings.py**에 추가하셔야합니다:

```
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
```

