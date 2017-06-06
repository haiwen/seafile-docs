# Upgrade Notes V5.x.x

__In Seafile 5.0, we moved all config files to the folder ```/seafile-root/conf```, including:__

- seahub_settings.py -> conf/seahub_settings.py
- ccnet/ccnet.conf -> conf/ccnet.conf
- seafile-data/seafile.conf -> conf/seafile.conf
- [pro only] pro-data/seafevents.conf -> conf/seafevents.conf

## V5.1.4

### Python upgrade
If you upgrade to 5.1.4+, you need to install the python 3 libs:

```
# for Ubuntu 16.04
sudo apt-get install python-urllib3

# for Debian 8
apt-get install python-urllib3

# for Centos 7
sudo yum install python-urllib3

# for Arch Linux
pacman -Sy python2-urllib3
```

## V5.1.3

Nothing to be installed/changed.

## V5.1.2

Nothing to be installed/changed.

## V5.1.1

Nothing to be installed/changed.

## V5.1.0

Nothing to be installed/changed.

## V5.0.5

Nothing to be installed/changed.

## V5.0.4

Nothing to be installed/changed.

## V5.0.3

Nothing to be installed/changed.

## V5.0.2

Nothing to be installed/changed.

## V5.0.1

Nothing to be installed/changed.

