# Firewall settings

By default, you should open 2 ports, 8000 and 8082, in your firewall settings.

If you run Seafile behind Nginx/Apache with HTTPS, you only need to open ports 443.

In addition, if you have any Libraries that were created prior to Seafile 3.0, then you will
need to open ports 10001 and 12001 to enable client syncing.
