# FAQ


## Clustering

### Page layout broken because seahub/media/CACHE is created only on first node

Please add

    COMPRESS_CACHE_BACKEND = 'django.core.cache.backends.locmem.LocMemCache'

to `seahub_settings.py` as documented at http://manual.seafile.com/deploy_pro/deploy_in_a_cluster.html

This is going to tell every node to generate the CSS CACHE in its local folder.
