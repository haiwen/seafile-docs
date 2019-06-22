# Seafile Server Changelog

## 7.0

**Feature changes**

In version 6.3, users can create public or private Wikis. In version 7.0, private Wikis is replaced by column mode view. Every library has a column mode view. So users don't need to explicitly create private Wikis.

Public Wikis are now renamed to published libraries.

**Upgrade**

Just follow our document on major version upgrade. No special steps are needed.

### 7.0.2 (2019/06/13)

* UI fixes
* Support index.md in published library
* Fix IE Edge support

### 7.0.1 beta (2019/05/31)

* [fix] Fix database upgrade problem
* [fix] Fix WebDAV can't be started
* [fix] Some UI fixes

### 7.0.0 beta (2019/05/23)

* Upgraded Web UI with React framework. The look and feel of the new UI is much better.
* Improved Markdown editor
* Add columns view mode (tree view like in the Windows Explorer)
* Add context menu to manipulate files
* Move files via drag and drop
* Redesigned file tags
* Support editing share link permission after creating a link


## 6.3

In version 6.3, Django is upgraded to version 1.11. Django 1.8, which is used in version 6.2, is deprecated in 2018 April.

With this upgrade, the fast-cgi mode is no longer supported. You need to config Seafile behind Nginx/Apache in WSGI mode.

The way to run Seahub in another port is also changed. You need to modify the configuration file `conf/gunicorn.conf` instead of running `./seahub.sh start <another-port>`.

Version 6.3 also changed the database table for file comments, if you have used this feature, you need migrate old file comments using the following commends after upgrading to 6.3:

```
./seahub.sh python-env seahub/manage.py migrate_file_comment
```

> Note, this command should be run while Seafile server is running.

### 6.3.4 (2018/09/15)

* [fix] Fix a security issue in Shibboleth authentication
* [fix] Fix sometimes Web UI will not autoload a >100 item directory view

### 6.3.3 (2018/09/07)

* Add generating of internal links
* Support copy a file to its own parent folder, creating a file with a suffix like test-1.docx
* Support setting the language list
* Redirect '/shib-login' to '/sso'
* Change "Unknown error" to "network error" when uploading failed caused by network error
* [fix] Fix groups not shown in system admin panel
* Support files be manually saved in OnlyOffice
* Improve performance when getting users quota usage
* Improve Markdown editor
* The new Wiki feature is ready
* Update Django to 1.11.11


### 6.3.2 (2018/07/09)

* [fix] Fix error when public wiki be viewed by anonymous users
* Remove department field in users' profile page
* [fix] Print warning instead of exit when there are errors in database table upgrade
* [fix] Send notification to the upload link creator after there are files uploaded
* [fix] Fix customize css via "custom/custom.css"
* [API] return the last modifier in file detail API
* [fix] Fix ZIP download can't work in some languages

### 6.3.1 (2018/06/24)

* Allow fullscreen presentation when view ppt(x) file via CollaboraOffice.
* Support mobile UI style when view file via OnlyOffice.
* Some UI improvement.
* Show terms and condition link if terms and condition is enabled
* [fix] Update OnlyOffice callback func (save file when status is 6).
* [fix] Show library’s first commit’s desc on library history page.
* [fix] Check if is an deleted library when admin restore a deleted library.
* [fix] Removed dead 'quota doc' link on user info popup.
* [fix] Fix bug of OnlyOffice file co-authoring.
* [API] Add starred field to file detail api.
* Use ID instead of email on sysadmin user page.
* [fix] Fix database upgrade problems
* [fix] Fix support for sqlite3
* [fix] Fix crash when seaf-fsck, seaf-gc receive wrong arguments

### 6.3.0 beta (2018/05/26)

* UI Improvements: moving buttons to top bar, improve scrolling in file/library list
* Update Django to 1.11, remove fast-cgi support
* Update jQuery to version 3.3.1
* Update pdf.js
* Add invite people link to share dialog if the feature is enabled
* Remove login log after delete a user
* \[admin] Support customize site title, site name, CSS via Web UI
* \[beta] Wiki, users can create public wikis
* Add an option to define the listening address for WSGI mode
* \[fix] Fix a bug that causing seaf-fsck crash
* \[fix] Fix support for uploading folder via ‘Cloud file browser’
* \[fix] Cancel Zip download task at the server side when user close zip download dialog
* Other fixes


## 6.2

From 6.2, It is recommended to use WSGI mode for communication between Seahub and Nginx/Apache. Two steps are needed if you'd like to switch to WSGI mode:

1. Change the config file of Nginx/Apache.
2. Restart Seahub with `./seahub.sh start` instead of `./seahub.sh start-fastcgi`

The configuration of Nginx is as following:

```
location / {
         proxy_pass         http://127.0.0.1:8000;
         proxy_set_header   Host $host;
         proxy_set_header   X-Real-IP $remote_addr;
         proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
         proxy_set_header   X-Forwarded-Host $server_name;
         proxy_read_timeout  1200s;

         # used for view/edit office file via Office Online Server
         client_max_body_size 0;

         access_log      /var/log/nginx/seahub.access.log;
         error_log       /var/log/nginx/seahub.error.log;
    }
```

The configuration of Apache is as following:

```
    # seahub
    SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1
    ProxyPass / http://127.0.0.1:8000/
    ProxyPassReverse / http://127.0.0.1:8000/
```

### 6.2.5 (2018/01/23)

* [fix] Fix OAuth bug
* [fix] Improve the performance of returning a user's all group libraries
* [new] Support customize the list of groups that a user can see when sharing a library


### 6.2.4 (2018/01/16)

* [new] Add the feature "remember this device" after two-factor authentication
* [new] Add option to notify the admin after new user registration (NOTIFY_ADMIN_AFTER_REGISTRATION)
* [fix] Fix a bug in modify permission for a a shared sub-folder
* [fix] Fix support for PostgreSQL
* [fix] Fix a bug in SQLite database support
* [fix] Fix support for uploading 500+ files via web interface (caused by API rate throttle)
* [improve, ui] Add transition to show/hide of feedback messages.
* [improve] Improve performance of file history page.
* [improve] Show two file history records at least.
* [fix] show shared sub-folders when copy/move file/folder to “Other Libraries”.
* [fix] Remove the white edge of webpage when previewing file via OnlyOffice.
* [fix] Don’t check if user exists when deleting a group member in admin panel.
* [fix, oauth] Don’t overwrite public registration settings when login a nonexistent user.
* Other UI improvements.

### 6.2.3 (2017/11/15)

* Support OAuth.
* WSGI uses 5 processors by default instead of 3 processors each with 5 threads
* [share] Add "click to select" feature for download/upload links.
* [Admin] Show/edit contact email in admin panel.
* [Admin] Show upload links in admin panel.
* [fix] Fix Shibboleth login redirection issue, see https://forum.seafile.com/t/shared-links-via-shibboleth/4067/19
* [fix] In some case failed to unshare a folder.
* [fix] LDAP search issue.
* [fix] Fix Safari downloaded file names are encoded like 'test-%2F%4B.doc' if it contains special characters.
* [fix] Disable client encrypt library creation when creating encrypt library is disabled on server.

### 6.2.2 (2017/09/25)

* [fix] Fix register button can't be clicked in login page
* [fix] Fix login_success field not exist in sysadmin_extra_userloginlog


### 6.2.1 (2017/09/22)

* [fix] Fix upgrade script for SQLite database
* Add Czech language
* [UI] Move password setting to a separate section
* [UI] Add divider to file operation menu
* [UI] Use high DPI icon in favorites page
* [UI] Focus on password fields by default
* [UI] Show feedback message when restore a library to a snapshot
* [fix] Don't import settings in seafile.conf to database


### 6.2.0 beta (2017/09/14)

* Redesign login page, adding a background image.
* Add two factor authentication
* Clean the list of languages
* Add the ability of tagging a snapshot of a library (Use `ENABLE_REPO_SNAPSHOT_LABEL = True` to turn the feature on)
* [Admin] Add an option to enable users to share a library to any groups in the system.
* Use WSGI as the default mode for deploying Seahub.
* Add a field Reference ID to support changing users primary ID in Shibboleth or LDAP
* Improved performance of loading library list
* Support adding a custom user search function (https://github.com/haiwen/seafile-docs/commit/115f5d85cdab7dc272da81bcc8e8c9b91d85506e)
* Other small UI improvements


## 6.1

If you upgrade from 6.0 and you'd like to use the feature video thumbnail, you need to install ffmpeg package:

```
# for ubuntu 16.04
apt-get install ffmpeg
pip install pillow moviepy

# for Centos 7
yum -y install epel-release
rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
yum -y install ffmpeg ffmpeg-devel
pip install pillow moviepy
```

### 6.1.2 (2017.08.15)

* Use user's language as lang setting for OnlyOffice
* Improve performance for getting user’s unread messages
* Fix error when uploading files to system default library template
* Users can restore their own deleted libraries
* Improve performance when move or copy multiple files/folders
* Add “details” for libraries, folders and files to show information like how many files in a library/folder
* [fix] Fix a bug in seaf-gc
* [fix, API] Fix a bug in creating folder API
* [admin] Improve performance in getting total file number, used space and total number of devices
* [fix] Fix MySQL connection pool in Ccnet

### 6.1.1 (2017.06.15)

* Disable thumbnail for video files in default
* Enable fixing the email for share link to be fixed in certain language (option SHARE_LINK_EMAIL_LANGUAGE in seahub_setting.py). So admin can force the language for a email of a share link to be always in English, regardless of what language the sender is using.
* The language of the interface of CollaboraOffice/OnlyOffice will be determined by the language of the current user.
* Display the correct image thumbnails in favorites instead of the generic one
* Enable set favicon and logo via admin panel
* Admin can add libraries in admin panel


### 6.1.0 beta (2017.05.11)

Web UI Improvement:

1. Add thumbnail for video files
2. Improved image file view, using thumbnail to view pictures
3. Improve pdf preview in community edition
4. Move items by drap & drop
5. Add create docx/xlsx/pptx in web interface
6. Add OnlyOffice integration
7. Add Collabora integration
8. Support folder upload in community edition
9. Show which client modify a file in history, this will help to find which client accidentally modified a file or deleted a file.

Improvement for admins:

1. Admin can set user’s quote, delete users in bulk
2. Support using admin panel in mobile platform
3. Add translation for settings page

System changes:

1. Remove wiki by default
2. Upgrade Django to 1.8.18
3. Clean Ajax API
4. Increase share link token length to 20 characters
5. Upgrade jstree to latest version

## 6.0

Note: If you ever used 6.0.0 or 6.0.1 or 6.0.2 with SQLite as database and encoutered a problem with desktop/mobile client login, follow https://github.com/haiwen/seafile/pull/1738 to fix the problem.

### 6.0.9 (2017.03.30)

* Show user' name instead of user's email in notifications sent out by email
* Add config items for setting favicon, disable wiki feature
* Add css id to easily hide user password reset and delete account button
* [fix] Fix UI bug in restoring a file from snapshot
* [fix] Fix after renaming a file, the old versions before file rename can't be downloaded
* [security] Fix XSS problem of the "go back" button in history page and snapshot view page

### 6.0.8 (2017.02.16)

Improvement for admin

* Admin can add/delete group members
* Admin can create group in admin panel
* Show total storage, total number of files, total number of connected devices in the info page of admin panel
* Force users to change password if imported via csv
* Support set user's quota, name when import user via csv
* Set user's quota in user list page
* Add search group by group name
* Use ajax when deleting a user's library in admin panel
* Support logrotate for controller.log
* Add `# -*- coding: utf-8 -*-` to seahub_settings.py, so that admin can use non-ascii characters in the file.
* Ingore white space character in the end of lines in ccnet.conf
* Add a log when a user can't be find in LDAP during login, so that the system admin can know whether it is caused by password error or the user can't be find
* Delete shared libraries information when deleting a user

Other

* [fix] Uploading files with special names lets seaf-server crash
* [fix] Fix user search when global address book is disabled in CLOUD_MODE
* [fix] Avoid timeout in some cases when showing a library trash
* Show "the account is inactive" when an inactive account try to login
* [security] Remove viewer.js to show open document files (ods, odt) because viewer.js is not actively maintained and may have potential security bugs (Thanks to Lukas Reschke from Nextcloud GmbH to report the issue)
* [fix] Fix PostgreSQL support
* Update Django to 1.8.17
* Change time_zone to UTC as default
* [fix] Fix quota check: users can't upload a file if the quota will be exceeded after uploading the file
* [fix] Fix quota check when copy file from one library to another
* [fix] Prevent admin from access group's wiki
* [fix] Fix a bug when download folder in grid view

### 6.0.7 (2016.12.16)

* [fix] Fix generating of password protected link in file view page
* [fix] Fix .jpg/.JPG image display in IE10
* Export quota usage in export Excel in user list admin page
* [fix] Fix admin can't delete broken libraries
* Add "back to previous page" link in trash page, history page
* [fix] Improve logo show in About page
* [fix] Fix file encoding for text file editing online
* [fix] Don't show operation buttons for broken libraries in normal users page


### 6.0.6 (2016.11.16)

* [fix] Fix the shared folder link in the notification message when a user share a folder to another user
* [fix] Update Django version from 1.8.10 to 1.8.16
* [fix] Fix support for PostgreSQL
* [fix] Fix SQLite database locking problem
* [fix] Fix the shared folder name is not changed after removing the old share, renaming the folder and re-sharing the folder
* [fix] Fix sub-folder accidentially show the files in parent folder when the parent folder contains more than 100 files
* [fix] Fix image preview navigation when there are more than 100 entries in a folder
* [fix] Fix bug when admin searching unexisting user
* [fix] Fix jpeg image display in IE10
* Add support for online view of mov video files
* Make web access token expiring time configurable
* Add an option on server to control block size for web upload files


### 6.0.5 (2016.10.17)

* [fix] Fix API for uploading file by blocks (Used by iOS client when uploading a large file)
* [fix] Fix a database connection problem in ccnet-server
* [fix] Fix moved files are still present in local folder until refresh
* [fix] Fix admin panel can't show deleted libraries


### 6.0.4 (2016.09.22)

* [fix] Fix not able to move files via WebDAV interface
* Check whether the quota will exceed before saving the uploaded file to Seafile via Web UI or API
* [fix] Fix owner can't restore a deleted file or folder in snapshot
* [fix] Fix UI of personal profile page
* [fix] Fix in some cases mobile devices can't be unlinked
* [fix] Fix connection problem for the latest MariaDB in initialisation script
* [fix] PNG Thumbnail creation broken in 6.0.3 (getexif failes)
* Make maxNumberOfFiles configurable
* [fix] Remember the sorting of libraries
* Add Finnish translation
* Video + audio no longer be limited by max preview size

### 6.0.3 (2016.09.03)

* [fix] Fix a bug in sqlite database upgrade script
* [fix] Fix a bug in database connection pool
* [fix] Fix a bug in file comment

### 6.0.2 (2016.09.02)

* [fix] Fix a bug in sqlite database table locking
* Update translations
* Support create libraries for Seafile Drive client

### 6.0.1 beta (2016.08.22)

* [fix] Fix  default value of created_at in table api2_tokenv2. This bug leads to login problems for desktop and mobile clients.
* [fix] Fix a bug in generating a password protected share link
* Improve checking the user running Seafile must be the owner of seafile-data. If seafile-data is symbolic link, check the destination folder instead of the symbolic link.
* [UI] Improve rename operation
* Admin can set library permissions in admin panel
* Show name/contact email in admin panel and enable search user by name/contact email
* Add printing style for markdown
* The “Seafile” in "Welcome to Seafile" message can be customised by SITE_NAME
* Improve sorting of files with numbers
* [fix] Fix can't view more than 100 files
* [API] Add admin API to only return LDAP imported user list


### 6.0.0 beta (2016.08.02)

* Add full screen Web UI
* Code clean and update Web APIs
* Add file comment
* Improve zip downloading by adding zip progress
* Change of navigation labels
* [admin] Add group transfer function in admin panel
* Remove number of synced libraries in devices page for simplify the interface and concept
* Update help pages

## 5.1

Warning:

* The concept of sub-library is removed in version 5.1. You can do selective sync with the latest desktop client
* The group message **reply** function is removed, and the old reply messages will not be shown with the new UI

Note: when upgrade from 5.1.3 or lower version to 5.1.4+, you need to install python-urllib3 (or python2-urllib3 for Arch Linux) manually:

```
# for Ubuntu
sudo apt-get install  python-urllib3
# for CentOS
sudo yum install python-urllib3
```

### 5.1.4 (2016.07.23)

* [fix] Fix seaf-fsck.sh --export fails without database
* [fix] Fix users with Umlauts in their display name breaks group management and api2/account/info on some special Linux distribution
* Remove user from groups when a user is deleted.
* [fix] Fix can't generate shared link for read-only shared library
* [fix] Fix can still view file history after library history is set to "no history".
* [fix] Fix after moving or deleting multiple selected items in the webinterface, the buttons are lost until reloading
* Check user before start seafile. The user must be the owner of seafile-data directory
* Don't allow emails with very special characters that may containing XSS string to register
* [fix] During downloading multiple files/folders, show "Total size exceeds limits" instead of "internal server error" when selected items exceeds limits.
* [fix] When delete a share, only check whether the be-shared user exist or not. This is to avoid the situation that share to a user can't be deleted after the user be deleted.
* Add a notificition to a user if he/she is added to a group
* Improve UI for password change page when forcing password change after admin reset a user's password
* [fix] Fix duplicated files show in Firefox if the folder name contains single quote '


### 5.1.3 (2016.05.30)

* [security]  Fix permission checking for generating share links
* Add an option (ENABLE_SETTINGS_VIA_WEB) to ignore settings via Web UI (system admin->settings)
* [fix] Making user search (used in auto-completion) case insensitive

### 5.1.2 (2016.05.13)

* [fix] Fix group rename
* [fix] Fix group transfer
* Send notifications to members when a new library is shared to a group
* Download multiple selected files from Seahub as a ZIP-file
* Use seafile-data/http-temp to store zip file when downloading a dir
* [UI] Remember the expanded status of groups in the left hand nav bar
* [accessibility] Improve accessiblity of library trash/history page by making links for operations selectable by tab.
* [accessibility] Improve accessiblity of dialogs, add missing labelledby properties for the whole dialog.
* [accessibility] Improve file/folder upload menu
* list all devices in admin panel
* Add syslog support for seafile.log


### 5.1.1 (2016.04.08)

Note: downloading multiple files at once will be added in the next release.


* A few UI Improvement and fixes
* Add group-discussion (warning: the group message reply function is removed, and the old reply messages will not be shown with the new UI)
* Add an option for disable forcing users to change password (FORCE_PASSWORD_CHANGE, default is True)
* Support new Shibboleth users be created as inactive and activated via Admin later (SHIB_ACTIVATE_AFTER_CREATION , default is True)
* Update jquery to v1.11


### 5.1.0 beta (2016.03.22)

Note: in this version, the group discussion is not re-implement yet. It will be available when the stable verison is released.

* Redesign navigation
* Rewrite group management
* Improve sorting for large folder
* Remember the sorting option for folder
* Improve devices page
* Update icons for libraries and files
* Remove library settings page, re-implement them with dialogs
* Remove group avatar
* Don't show share menu in top bar when multiple item selected
* Auto-focus on username field when loading the login page
* Remove self-introduction in user profile
* Upgrade to django 1.8
* Force the user to change password if adding by admin or password reset by admin
* disable add non-existing user to a group

## 5.0

**Note when upgrade to 5.0 from 4.4**

You can follow the document on major upgrade (http://manual.seafile.com/deploy/upgrade.html)

In Seafile 5.0, we have moved all config files to folder `conf`, including:

* seahub_settings.py -> conf/seahub_settings.py
* ccnet/ccnet.conf -> conf/ccnet.conf
* seafile-data/seafile.conf -> conf/seafile.conf
* [pro only]  pro-data/seafevents.conf -> conf/seafevents.conf

If you want to downgrade from v5.0 to v4.4, you should manually copy these files back to the original place, then run minor_upgrade.sh to upgrade symbolic links back to version 4.4.

The 5.0 server is compatible with v4.4 and v4.3 desktop clients.

Common issues (solved) when upgrading to v5.0:

* DatabaseError after Upgrade to 5.0 https://github.com/haiwen/seafile/issues/1429#issuecomment-153695240

### 5.0.5 (2016.03.02)

* Get name, institution, contact_email field from Shibboleth
* [WebDAV] Don't show sub-libraries
* Enable LOGIN_URL to be configured, user need to add LOGIN_URL to seahub_settings.py explicitly if deploy at non-root domain, e.g. LOGIN_URL = '/<sub-path>/accounts/login/'.
* Add ENABLE_USER_CREATE_ORG_REPO to enable/disable organization repo creation.
* Change the Chinese translation of "organization"
* Use GB/MB/KB instead of GiB/MiB/KiB in quota calculation and quota setting (1GB = 1000MB = 1,000,000KB)
* Show detailed message if sharing a library failed.
* [fix] Fix JPG Preview in IE11
* [fix] Show "out of quota" instead of "DERP" in the case of out of quota when uploading files via web interface
* [fix] Fix empty nickname during shibboleth login.
* [fix] Fix default repo re-creation bug when web login after desktop.
* [fix] Don't show sub-libraries at choose default library page, seafadmin page and save shared file to library page
* [fix] Seafile server daemon: write PID file before connecting to database to avoid a problem when the database connection is slow
* [fix] Don't redirect to old library page when restoring a folder in snapshot page



### 5.0.4 (2016.01.13)

* [fix] Fix unable to set a library to keep full history when the  globally default keep_days is set.
* [fix] Improve the performance of showing library trash
* [fix] Improve share icon
* Search user by name in case insensitive way
* Show broken libraries in user's library page (so they can contact admin for help)
* [fix] Fix cache for thumbnail in sharing link
* [fix] Enable copy files from read-only shared libraries to other libraries
* [fix] Open image gallery popup in grid view when clicking the thumbnail image


### 5.0.3 (2015.12.17)

* [UI] Improve UI of all groups page
* Don't allow sharing library to a non-existing user
* [fix, admin] Fix deleting a library when the owner does not exist anymore
* [fix] Keep file last modified time when copy files between libraries
* Enable login via username in API
* [UI] Improve markdown editor

Improve seaf-fsck

* Do not set "repaired" mark
* Clean syncing tokens for repaired libraries so the user are forced to resync the library
* Record broken file paths in the modification message

Sharing link

* Remember the "password has been checked" information in session instead of memcached
* [security] Fix password check for visiting a file in password protected sharing link.
* Show file last modified time
* [fix] Fix image thumbnail in grid view
* [UI] Improve UI of grid view mode


### 5.0.2 (2015.12.04)

* [admin] Show the list of groups an user joined in user detail page
* [admin] Add exporting user/group statistics into Excel file
* Showing libraries list in "All Groups" page
* Add importing group members from CSV file
* [fix] Fix the performance problem in showing thumbnails in folder sharing link page
* [fix] Clear cache when set user name via API
* [fix, admin] Fix searching libraries by name when some libraries are broken


### 5.0.1 beta (2015.11.12)

* [fix] Fix start up parameters for seaf-fuse, seaf-server, seaf-fsck
* Update Markdown editor and viewer. The update of the markdown editor and parser removed support for the Seafile-specific wiki syntax: Linking to other wikipages isn't possible anymore using `[[ Pagename]]`.
* Add tooltip in admin panel->library->Trash: "libraries deleted 30 days before will be cleaned automatically"
* Include fixes in v4.4.6

### 5.0.0 beta (2015.11.03)

UI changes:

* change most png icons to icon font
* UI change of file history page
* UI change of library history page
* UI change of trash page
* UI change of sharing link page
* UI change of rename operation
* Add grid view for folder sharing link
* Don't open a new page when click the settings, trash and history icons in the library page
* other small UI improvements

Config changes:

* Move all config files to folder `conf`
* Add web UI to config the server. The config items are saved in database table (seahub-dab/constance_config). They have a higher priority over the items in config files.

Trash:

* A trash for every folder, showing deleted items in the folder and sub-folders.
Others changes

Admin:

* Admin can see the file numbers of a library
* Admin can disable the creation of encrypted library

Security:

* Change most GET requests to POST to increase security

## 4.4

### 4.4.6 (2015.11.09)

* [security] Fix a XSS problem in raw sharing link
* [fix] Delete sharing links when deleting a library
* [fix] Clean Seafile tables when deleting a library
* [fix] Add <a> tag to the link in upload folder email notification
* [fix] Fix a bug in creating a library (after submit a wrong password, the submit button is no longer clickable)


### 4.4.5 (2015.10.31)

* [fix] Fix a bug in deleting sharing link in sharing dialog.

### 4.4.4 (2015.10.27)

* [fix] Fix support for syncing old formatted libraries
* Only import LDAP users to Seafile internal database upon login
* Only list imported LDAP users in "organization->members"
* Remove commit and fs objects in GC for deleted libraries
* Improve error log for LDAP
* Add "transfer" operation to library list in "admin panel->a single user"
* [fix] Fix the showing of the folder name for upload link generated from the root of a library

### 4.4.3 (2015.10.15)

* [security] Check validity of file object id to avoid a potential attack
* [fix] Check the validity of system default library template, if it is broken, recreate a new one.
* [fix] After transfer a library, remove original sharing information
* [security] Fix possibility to bypass Captcha check
* [security] More security fixes.


### 4.4.2 (2015.10.12)

* [fix] Fix sometimes a revision is missing from a file's version history
* [security] Use HTTP POST instead of GET to remove libraries
* [fix] Fix a problem that sharing dialog not popup in IE10
* A few other small UI improvements

### 4.4.1 (2015.09.24)

* [fix] Fix a bug in setting an user's language
* [fix] Show detailed failed information when sharing libraries failed
* Update translations
* [API] Add API to list folders in a folder recursively
* [API] Add API to list only folders in a folder


### 4.4.0 (2015.09.16)

New features:

* Allow group names with spaces
* Enable generating random password when adding an user
* Add option SHARE_LINK_PASSWORD_MIN_LENGTH
* Add sorting in share link management page
* Show total/active number of users in admin panel
* Other UI improvements

Fixes:

* [fix] Fix a bug that causing duplications in table LDAPImport
* [security] Use POST request to handle password reset request to avoid CSRF attack
* Don't show password reset link for LDAP users
* set locale when Seahub start to avoid can't start Seahub problem in a few environments.

## 4.3

### 4.3.2 (2015.08.20)

* [fix, important] Bug-fix and improvements for seaf-fsck
* [fix, important] Improve I/O error handling for file operations on web interface
* Update shared information when a sub-folder is renamed
* [fix] Fix bug of list file revisions
* Update translations
* [UI] Small improvements
* [fix] Fix api error in opCopy/opMove
* Old library page (used by admin in admin panel): removed 'thumbnail' & 'preview' for image files
* [fix] Fix modification operations for system default library by admin

### 4.3.1 (2015.07.29)

* [fix] Fix generating image thumbnail
* [UI] Improve UI for sharing link page, login page, file upload link page
* [security] Clean web sessions when reset an user's password
* Delete the user's libraries when deleting an user
* Show link expiring date in sharing link management page
* [admin] In a user's admin page, showing libraries' size and last modify time

### 4.3.0 (2015.07.21)

Usability Improvement

* [UI] Improve ui for file view page
* [UI] Improve ui for sorting files and libraries
* Redesign sharing dialog
* Enable generating random password for sharing link
* Remove private message module
* Remove direct *single* file sharing between users (You can still sharing folders)
* Change "Quit" to "Leave group" in group members page

Others

* Improve user management for LDAP
* [fix] Fix a bug that client can't detect a library has been deleted in the server
* [security] Improve permission check in image thumbnail
* [security] Regenerate Seahub secret key, the old secret key lack enough randomness
* Remove the support of ".seaf" format
* [API] Add API for generating sharing link with password and expiration
* [API] Add API for generating uploading link
* [API] Add API for link files in sharing link
* Don't listen in 10001 and 12001 by default.
* Add an option to disable sync with any folder feature in clients
* Change the setting of THUMBNAIL_DEFAULT_SIZE from string to number, i.e., use `THUMBNAIL_DEFAULT_SIZE = 24`, instead of `THUMBNAIL_DEFAULT_SIZE = '24'`

## 4.2

Note when upgrade to 4.2 from 4.1:

If you deploy Seafile in a non-root domain, you need to add the following extra settings in seahub_settings.py:

```
COMPRESS_URL = MEDIA_URL
STATIC_URL = MEDIA_URL + '/assets/'
```

### 4.2.3 (2015.06.18)

* Add global address book and remove the contacts module (You can disable it if you use CLOUD_MODE by adding ENABLE_GLOBAL_ADDRESSBOOK = False in seahub_settings.py)
* Use image gallery module in sharing link for folders containing images
* [fix] Fix missing library names (show as none) in 32bit version
* [fix] Fix viewing sub-folders for password protected sharing
* [fix] Fix viewing starred files
* [fix] Fix supporting of uploading multi-files in clients' cloud file browser
* Improve security of password resetting link


### 4.2.2 (2015.05.29)

* [fix] Fix picture preview in sharing link of folders
* Improve add library button in organization tab

### 4.2.1 (2015.05.27)

* Add direct file download link
* [fix] Fix group library creation bug
* [fix] Fix library transfer bug
* [fix] Fix markdown file/wiki bug
* Don't show generating sharing link for encrypted libraries
* Don't show the list of sub-libraries if user do not enable sub-library
* Enable adding existing libraries to organization
* Add loading tip in picture preview page

### 4.2.0 beta (2015.05.13)

Usability

* Remove showing of library description
* Don't require library description
* Keep left navigation bar when navigate into a library
* Generate share link for the root of a library

Security Improvement

* Remove access tokens (all clients will log out) when a users password changed
* Temporary file access tokens can only be used once
* sudo mode: confirm password before doing sysadmin work

Platform

* Use HTTP/HTTPS sync only, no longer use TCP sync protocol
* read/write permission on sub-folders (Pro)
* Support byte-range requests
* Automatically clean of trashed libraries
* [LDAP] Save user information into local DB after login via LDAP


## 4.1

### 4.1.2 (2015.03.31)

* [fix] Fix several packaging related bugs (missing some python libraries)
* [fix] Fix webdav issue
* [fix] Fix image thumbnail in sharing link
* [fix] Fix permission mode of seaf-gc.sh
* Show detailed time when mouse over a relative time

### 4.1.1 (2015.03.25)

* Add trashed libraries (deleted libraries will first be put into trashed libraries where system admin can restore)
* [fix] Fix upgrade script for SQLite
* Improve seaf-gc.sh
* Do not support running on CentOS 5.

### 4.1.0 beta (2015.03.18)

* Shibboleth authentication support.
* Redesign fsck.
* Add image thumbnail in folder sharing link
* Add API to support logout/login an account in the desktop client
* Add API to generate thumbnails for images files
* Clean syncing tokens after deleting an account
* Change permission of seahub_settings.py, ccnet.conf, seafile.conf to 0600
* Update Django to v1.5.12

## 4.0

### 4.0.6 (2015.02.04)

Important

* [fix] Fix transfer library error in sysadmin page
* [fix] Fix showing of space used in sysadmin page for LDAP users
* Improved trash listing performance

Small

* [webdav] list organisation public libraries
* Disable non-shibboleth login for shibboleth users
* [fix] Fix wrong timestamp in file view page for files in sub-library
* Add Web API for thumbnail
* Add languages for Thai and Turkish, update a few translations


### 4.0.5 (2015.01.14)

Important

* [fix] Fix memory leak in HTTP syncing
* Repo owner can restore folders/files from library snapshot
* Update translations
* Only repo owner can restore a library to a snapshot


Small improvements

* [fix] Remote redundant logs in seaf-server
* [fix] Raise 404 when visiting an non-existing folder
* [fix] Enable add admin when LDAP is enabled
* Add API to get server features information (what features are supported by this server)
* [fix] Fix throttle for /api2/ping

### 4.0.4 (2015.01.06)

* [fix] Fix syncing sub-library with HTTP protocol
* [fix] Fix a bug in setup-seafile-mysql.sh

### 4.0.3 (2014.12.30)

* [fix] Fix unable to share library to another user

### 4.0.2 (2014.12.26)

* Add image thumbnail
* Add Shibboleth support (beta)
* [fix] Fix performance problem in listing files API
* [fix] Fix listing files of a large folder
* [fix] Fix folder sharing link with password protection
* [fix] Fix deleting broken libraries in the system admin panel

### 4.0.1 (2014.11.29)

* [fix] Fix bugs in syncing with HTTP protocol
* Add upgrading script (from v3.1 to v4.0)

### 4.0.0 (2014.11.10)

* Add HTTP syncing support
* Merge FileServer into seaf-server

## 3.1

### 3.1.7 (2014.10.20)

* [fix] Fixed performance problem in WebDAV extension
* [fix] Fixed quota check in WebDAV extension
* [fix] Fixed showing libraries with same name in WebDAV extension
* Add "clear" button in a library's trash
* Support upload a folder in web interface when using Chrome
* [fix] Improve small errors when upload files via Web interface
* [fix] Fix moving/coping files when the select all file checkbox is checked

### 3.1.6 (2014.09.11)

* [Fix] Fix bug in uploading >1GB files via Web
* [Fix] Remove assert in Ccnet to avoid denial-of-service attack
* Revert the work "access token generated by FileServer can only be used once" because this leads to several problems


### 3.1.5 (2014.08.29)

* [Fix] Fix multi-file upload in upload link and library page
* [Fix] Fix libreoffice file online view
* Add 'back to top' for pdf file view.
* [Fix] Fix "create sub-library" button under some language
* [Fix popup] Fix bug in set single notice as read.

### 3.1.4 (2014.08.26)

* [Fix, security] Fix permission check for PDF full screen view
* [Fix] Fix copy/move multiple files in web
* Improve UI for group reply notification
* Improve seaf-fsck, seaf-fsck now can fix commit missing problem
* [Security improve] Access token generated by FileServer can only be used once.

### 3.1.3 (2014.08.18)

* [Fix] fix memory leak
* [Fix] fix a memory not initialized problem which may cause sync problem under heavy load.
* [Fix] fix creating personal wiki

### 3.1.2 (2014.08.07)

* Use unix domain socket in ccnet to listen for local connections. This isolates the access to ccnet daemon for different users. Thanks to Kimmo Huoman and Henri Salo for reporting this issue.

### 3.1.1 (2014.08.01)

* Add a bash wrapper for seafile-gc
* [Fix] fix listing libraries when some libraries are broken
* Remove simplejson dependency
* Update translations
* Add "Back to Top" button in file view page
* Improve page refreshing after uploading files

### 3.1.0 (2014.07.24)

Syncing

* Improve performance: easily syncing 10k+ files in a library.
* Don't need to download files if they are moved to another directory.

Platform

* Rename HttpServer to FileServer to remove confusing.
* Support log rotate
* Delete old PID files when stop Seafile

Web

* Enable deleting of personal messages
* Improved notification
* Upgrade pdf.js
* Password protection for sharing links
* [Admin] Create multi-users by uploading a CSV file
* Sort libraries by name/date
* Enable users to put an additional message when sending a sharing link
* Expiring time for sharing links
* [fix] Send notification to all users participating a group discussion
* Redesigned file viewing page
* Remove simplejson dependency
* Disable the ability to make a group public by default (admin can turn it on in settings)


## 3.0

### 3.0.4 (2014.06.07)

* [API] Add replace if exist into upload-api
* Show detailed error message when Gunicorn failed to start
* Improve object and block writting performance
* Add retry when failed getting database connection
* [fix] Use hash value for avatar file names to avoid invalid file name
* [fix] Add cache for repo_crypto.js to improve page speed
* [fix] Show error message when change/reset password of LDAP users
* [fix] Fix "save to my library" when viewing a shared file
* [fix, API] Fix rename file names with non-ascii characters


### 3.0.3

* [fix] Fix an UI bug in selecting multiple contacts in sending message
* Library browser page: Loading contacts asynchronously to improve initial loading speed

### 3.0.2

* [fix] Fix a bug in writing file metadata to disk, which causing "file information missing error" in clients.
* [fix] Fix API for uploading files from iOS in an encrypted library.
* [fix] Fix WebDAV
* [fix] Fix API for getting groups messages containing multiple file attachments
* [fix] Fix bug in HttpServer when file block is missing
* [fix] Fix login error for some kind of Android

### 3.0.1

* [fix] Fix showing bold/italic text in .seaf format
* [fix] Fix UI problem when selecting contacts in personal message send form
* [fix] Add nickname check and escape nickname to prevent XSS attack
* [fix] Check validity of library name (only allow a valid directory name).

### 3.0.0

Web

* Lots of small improvements in UI
* Translations
* [fix] Handle loading avatar exceptions to avoid 500 error

Platform

* Use random salt and PBKDF2 algorithm to store users' password. (You need to manually upgrade the database if you using 3.0.0 beta2 with MySQL backend.)

### 3.0.0 beta2

Web

* Handle 413 error of file upload
* Support cross library files copy/move
* Fixed a few api errors

Platform

* Allow config httpserver bind address
* [fix] Fix file ID calculation
* Improved device (desktop and mobile clients) management
* Add back webdav support
* Add upgrade script

### 3.0.0 beta

Platform

* Separate the storage of libraries
* Record files' last modification time directly
* Keep file timestamp during syncing
* Allow changing password of an encrypted library

Web

* Redesigned UI
* Improve page loading speed

## 2.2

### 2.2.1

* [fix] Fixed creation of admin account

### 2.2.0

* Add more checking for the validity of users' Email
* Use random salt and PBKDF2 algorithm to store users' password.


## 2.1

### 2.1.5

* Add correct mime types for mp4 files when downloading
* [fix] [Important] set correct file mode bit after uploading a file from web.
* Show meaningful message instead of "auto merged by system" for file merges
* Improve file history calculation for files which were renamed

WebDAV

* Return last modified time of files



### 2.1.4

* [fix] Fix file share link download issue on some browsers.
* [wiki] Enable create index for wiki.
* Hide email address in avatar.
* Show "create library" button on Organization page.
* [fix] Further improve markdown filter to avoid XSS attack.

### 2.1.3

* [api] Add more web APIs
* Incorporate Viewer.js to display opendocument formats
* [fix] Add user email validation to avoid SQL injection
* [fix] Only allow `<a>, <table>, <img>` and a few other html elements in markdown to avoid XSS attack.  
* Return sub-libraries to the client when the feature is enabled.

### 2.1.2

* [fix] Fixed a bug in update script

### 2.1.1


* Allow the user to choose the expiration of the session when login
* Change default session expiration age to 1 day
* [fix] Fixed a bug of copying/moving files on web browsers
* [fix] Don't allow script in markdown files to avoid XSS attacks
* Disable online preview of SVG files to avoid potential XSS attacks
* [custom] Support specify the width of height of custom LOGO
* Upgrade scripts support MySQL databases now


### 2.1.0

Platform

* Added FUSE support, currently read-only
* Added WebDAV support
* A default library would be created for new users on first login to seahub

Web

* Redesigned Web UI
* Redesigned notification module
* Uploadable share links
* [login] Added captcha to prevent brute force attack
* [fix] Fixed a bug of "trembling" when scrolling file lists
* [sub-library] User can choose whether to enable sub-library
* Improved error messages when upload fails
* Set default browser file upload size limit to unlimited

Web for Admin

* Improved admin UI
* More flexible customization options
* Online help is now bundled within Seahub

## 2.0

### 2.0.4

* [fix] set the utf8 charset when connecting to database
* Getting users from both database and LDAP
* [web] List all contacts when sharing libraries
* [admin] List database and LDAP users in sysadmin


### 2.0.3

* [fix] Speed up file syncing when there are lots of small files

### 2.0.2

* [fix] Fix CIFS support.
* [fix] Support special characters like '@' in MySQL password
* [fix] Fix create library from desktop client when deploy Seafile with Apache.
* [fix] Fix sql syntax error in ccnet.log, issue #400 (https://github.com/haiwen/seafile/issues/400).
* [fix] Return organization libraries to the client.
* Update French, German and Portuguese (Brazil) languages.

### 2.0.1

* [fix] Fix a bug in sqlite3 upgrade script
* Add Chinese translation


### 2.0.0

Platform

* New crypto scheme for encrypted libraries
* A fsck utility for checking data integrity

Web

* Change owner of a library/group
* Move/delete/copy multiple files
* Automatically save draft during online editing  
* Add "clear format" to .seaf file online editing
* Support user delete its own account
* Hide Wiki module by default
* Remove the concept of sub-library

Web for Admin

* Change owner of a library
* Search user/library

API

* Add list/add/delete user API


## 1.8

### 1.8.5

* [bugfix] Fix "can't input space" bug in .seaf files
* Add pagination for online file browsing

### 1.8.3


* [bugfix] Fix bug in setup-seafile-mysql.sh
* Make reset-admin script work for MySQL
* Remove redundant log messages
* Fixed bugs in web API


### 1.8.2

* Add script for setting up MySQL
* [bugfix] Fixed a bug when sharing a library to another user without sending HTTP_REFERER

### 1.8.1

* [bugfix] Fixed a bug when generating shared link

### 1.8.0

Web

* Improve online file browsing and uploading
    - Redesigned interface
    - Use ajax for file operations
    - Support selecting of multiple files in uploading
    - Support drag/drop in uploading
* Improve file syncing and sharing
    - Syncing and sharing a sub-directory of an existing library.
    - Directly sharing files between two users (instead of generating public links)
    - User can save shared files to one's own library
* [wiki] Add frame and max-width to images
* Use 127.0.0.1 to read files (markdown, txt, pdf) in file preview
* [bugfix] Fix pagination in library snapshot page
* Set the max length of message reply from 128 characters to 2000 characters.
* Improved performance for home page and group page
* [Admin] Add administration of public links

API

* Add creating/deleting library API

Platform

* Improve HTTPS support, now HTTPS reverse proxy is the recommend way.
* Add LDAP filter and multiple DN
* Case insensitive login
* Move log files to a single directory
* [security] Add salt when saving user's password
* [bugfix] Fix a bug in handling client connection


## 1.7

### 1.7.0.2 for Linux 32 bit

* [bugfix] Fix "Page Unavailable" when view doc/docx/ppt.

### 1.7.0.1 for Linux 32 bit

* [bugfix] Fix PostgreSQL support.

### 1.7.0

Web

* Upgrade to Django 1.5
* Add personal messaging
* Support cloud_mode to hide the "organization" tab
* Support listing/revoking syncing clients
* [bugfix] Fix a bug in Markdown undo/redo
* [pro-edition] Searching in a library
* [pro-edition] Redesign file activities
* [pro-edition] Redesign doc/ppt/pdf preview with pdf2htmlEX

Daemon

* Support PostgreSQL
* [bugfix] fix bugs in GC

## 1.6

### 1.6.1

Web

* [bugfix] Fix showing personal Wiki under French translation
* [bugfix] Fix showing markdown tables in Wiki
* [bugfix] Fixed wiki link parsing bug when page alias contains dot.
* Disable sharing link for encrypted libraries
* [admin] improved user-add, set/revoke admin, user-delete

Daemon

* [controller] Add monitor for httpserver

### 1.6.0

Web

* Separate group functions into Library/Discuss/Wiki tabs
* Redesign Discussion module
* Add Wiki module
* Improve icons
* Can make a group public
* [editing] Add toolbar and help page for Markdown files
* [editing] A stable rich document editor for .seaf files
* [bugfix] Keep encryption property when change library name/desc.


For Admin

* Add --dry-run option to seafserv-gc.
* Support customize seafile-data location in seafile-admin
* Do not echo the admin password when setting up Seafile server
* seahub/seafile no longer check each other in start/stop scripts


API

* Show file modification time
* Add update file API

## 1.5

### 1.5.2

* [daemon] Fix problem in DNS lookup for LDAP server

### 1.5.1

* [web] Fix password reset bug in Seafile Web
* [daemon] Fix memory leaks in Seafile server

### 1.5.0

Seafile Web

* Video/Audio playback with MediaElement.js (Contributed by Phillip Thelen)
* Edit library title/description
* Public Info & Public Library page are combined into one
* Support selection of file encoding when viewing online
* Improved online picture view (Switch to prev/next picture with keyboard)
* Fixed a bug when doing diff for a newly created file.
* Sort starred files by last-modification time.

Seafile Daemon

* Fixed bugs for using httpserver under https
* Fixed performance bug when checking client's credential during sync.
* LDAP support
* Enable setting of the size of the thread pool.

API

* Add listing of shared libraries
* Add unsharing of a library.
