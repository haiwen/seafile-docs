# Add memcached

Seahub caches items (avatars, profiles, etc) on the file system in /tmp/seahub_cache/ by default. You can use memcached instead to improve the performance.

First, make sure `libmemcached` library and development headers are installed on your system. Version 1.0.18 of libmemcached or later should be used.

On Ubuntu 16.04 or similar, the version in system repository is new enough. So you can install it directly.

```
sudo apt-get install libmemcached-dev zlib1g-dev
```

On other systems, such as CentOS 7 or Ubuntu 14.04, you should install the library from source code.

```
sudo apt-get install build-essential # or sudo yum install gcc gcc-c++ make openssl-devel
wget https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz
tar zxf libmemcached
cd libmemcached-1.0.18
./configure
make
sudo make install
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
    }
}

```

bind memcache to unix sockets instead of unix ports is also possible and [suggested](https://serverfault.com/questions/124517/whats-the-difference-between-unix-socket-and-tcp-ip-socket) to be more performant.
```
CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': '/tmp/memcached.sock',
    }
}
```
If you use a memcached cluster, please replace the `CACHES` variable with the following. This configuration uses consistent hashing to distribute the keys in memcached. More information can be found on [pylibmc documentation](http://sendapatch.se/projects/pylibmc/behaviors.html) and [django-pylibmc documentation](https://github.com/django-pylibmc/django-pylibmc). Supposed your memcached server addresses are 192.168.1.13[4-6].

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
    }
}
```
