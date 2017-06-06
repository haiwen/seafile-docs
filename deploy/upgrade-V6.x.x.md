# Upgrade Notes V6.x.x

## V6.1.0

#### Video Thumbnails
If you upgrade to 6.1, you need to install the FFMPEG package to activate video thumbnails:

```
# for Ubuntu 16.04
apt-get install ffmpeg
pip install pillow moviepy

# for Debian 8
apt-get install ffmpeg
pip install pillow moviepy

# for Centos 7
yum -y install epel-release
rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
yum -y install ffmpeg ffmpeg-devel
pip install pillow moviepy
```

#### OnlyOffice
The system requires some minor changes to support the OnlyOffice document server.
Please follow the instructions [here](../deploy/only_office.md)


## V6.0.0 - V6.0.9

Nothing to be installed/changed.
