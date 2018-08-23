# Office Online Server

In Seafile Professional Server Version 4.4.0 (or above), you can use Microsoft Office Online Server (formerly named Office Web Apps) to preview documents online. Office Online Server provides the best preview for all Office format files. It also support collaborative editing of Office files directly in the web browser. For organizations with Microsoft Office Volume License, it's free to use Office Online Server. For more information about Office Online Server and how to deploy it, please refer to https://technet.microsoft.com/en-us/library/jj219455(v=office.16).aspx.

**Notice**: Seafile only supports Office Online Server 2016 and above.

Seafile's own Office file preview is still the default. To use Office Online Server for preview, please add following config option to seahub_settings.py.

``` python
# Enable Office Online Server
ENABLE_OFFICE_WEB_APP = True

# Url of Office Online Server's discovery page
# The discovery page tells Seafile how to interact with Office Online Server when view file online
# You should change `http://example.office-web-app.com` to your actual Office Online Server server address
OFFICE_WEB_APP_BASE_URL = 'http://example.office-web-app.com/hosting/discovery'

# Expiration of WOPI access token
# WOPI access token is a string used by Seafile to determine the file's
# identity and permissions when use Office Online Server view it online
# And for security reason, this token should expire after a set time period
WOPI_ACCESS_TOKEN_EXPIRATION = 30 * 60 # seconds

# List of file formats that you want to view through Office Online Server
# You can change this value according to your preferences
# And of course you should make sure your Office Online Server supports to preview
# the files with the specified extensions
OFFICE_WEB_APP_FILE_EXTENSION = ('ods', 'xls', 'xlsb', 'xlsm', 'xlsx','ppsx', 'ppt',
    'pptm', 'pptx', 'doc', 'docm', 'docx')

# Enable edit files through Office Online Server
ENABLE_OFFICE_WEB_APP_EDIT = True

# types of files should be editable through Office Online Server
# Note, Office Online Server 2016 is needed for editing docx
OFFICE_WEB_APP_EDIT_FILE_EXTENSION = ('xlsx', 'pptx', 'docx')


# HTTPS authentication related (optional)

# Server certificates
# Path to a CA_BUNDLE file or directory with certificates of trusted CAs
# NOTE: If set this setting to a directory, the directory must have been processed using the c_rehash utility supplied with OpenSSL.
OFFICE_WEB_APP_SERVER_CA = '/path/to/certfile'


# Client certificates
# You can specify a single file (containing the private key and the certificate) to use as client side certificate
OFFICE_WEB_APP_CLIENT_PEM = 'path/to/client.pem'

# or you can specify these two file path to use as client side certificate
OFFICE_WEB_APP_CLIENT_CERT = 'path/to/client.cert'
OFFICE_WEB_APP_CLIENT_KEY = 'path/to/client.key'
```

Then restart

```
./seafile.sh restart
./seahub.sh restart
```

After you click the document you specified in seahub_settings.py, you will see the new preview page.

![office-web-app](../images/office-web-app.png)

## Trouble shooting

Understanding how the web app integration works is going to help you debugging the problem. When a user visits a file page:

1. (seahub->browser) Seahub will generate a page containing an iframe and send it to the browser
2. (browser->office online server) With the iframe, the browser will try to load the file preview page from the office online server
3. (office online server->seahub) office online server receives the request and sends a request to Seahub to get the file content
4. (office online server->browser) office online server sends the file preview page to the browser.

Please check the Nginx log for Seahub (for step 3) and Office Online Server to see which step is wrong.

### Notes on Windows paging files

You should make sure you have configured at least a few GB of paging files in your Windows system. Otherwise the IIS worker processes may die randomly when handling Office Online requests.
