# Setup

## Failed to upload/download file online

* Make sure your firewall for seafile fileserver is opened.
* Make sure `SERVICE_URL` in ccnet.conf and `FILE_SERVER_ROOT` in seahub_settings.py are set correctly. Furthermore check that you haven't overwritten them using the settings in the Seahub Admin section.
* Use Chrome/Firefox debug mode to find out which address is being used when clicking download button and whether it is correct.

## Does Seafile server support Python 3?

No, You must have Python 2.7 installed on your server.

## Seahub/Seafile started correctly, but when visiting the web interface, it shows "Internal Server Error"

It is mostly likely some required Python packages of Seahub is not installed correctly.

You can check the detailed error messages in `/var/log/nginx/seahub.error.log` if you use Nginx.


## Website displays "Page unavailable", what can I do?

* You can check the back trace in Seahub log files (`installation folder/logs/seahub_django_request.log`)

* You can also turn on debug mode by adding `DEBUG = True` to `seahub_settings.py` and restarting Seahub with `./seahub.sh restart`, then refresh the page, all the debug infomations will be displayed. Make sure ./seahub.sh was started as: ./seahub.sh start-fastcgi in case you're using fastcgi.

## Files with a space in their name do not work using Apache

See http://manual.seafile.com/deploy/deploy_with_apache.html#problems-with-paths-and-files-containing-spaces


## How to change seafile-data location after setup?

Modify file `seafile.ini` under ccnet. This file contains the location of seafile-data. Move seafile-data to another place, like `/opt/new/seafile-data` and modify `seafile.ini` accordingly.

## Failed to send email, what can I do?

Please check logs/seahub.log.

There are some common mistakes:

1. Check whether there are typos in the config (`seahub_settings.py`, e.g. you could have forgotten to add a single quote `EMAIL_HOST_USER = XXX`, which should be `EMAIL_HOST_USER = 'XXX'` or you could habe a space at the end of a config line.
2. Your mail server is not available.
