# Upgrade Notes V4.x.x

## V4.3.1 - V4.4.6

Nothing to be installed/changed.

## V4.3.0

Change the setting of THUMBNAIL_DEFAULT_SIZE from string to number in ```seahub_settings.py```:

Use ```THUMBNAIL_DEFAULT_SIZE = 24```, instead of ```THUMBNAIL_DEFAULT_SIZE = '24'```.


## V4.2.0 - V4.2.3

#### Note when upgrading to 4.2:
If you deploy Seafile in a non-root domain, you need to add the following extra settings in ```seahub_settings.py```:
```
COMPRESS_URL = MEDIA_URL
STATIC_URL = MEDIA_URL + '/assets/'
```

## V4.0.0 - V4.1.2

Nothing to be installed/changed.
