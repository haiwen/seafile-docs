# Seafile Client Changelog

## 6.2

### 6.2.4 (2018/08/03)

* [fix] Fix a bug that causing Windows Explorer crash

### 6.2.3 (2018/07/30)

* Prevent multiple seaf-daemon running
* [fix] Support preconfigured Shibboleth Url
* Restart seaf-daemon automatically if it is dead

### 6.2.2 6.2.1 Beta (2018/07/13)

* [fix] Fix initialization problem in first time launching
* Improve file syncing notification message

### 6.2.0 Beta (2018/07/03)

* [mac] Add automatical locking support for Office files
* [mac] Don't update local office file if it is editing locally while simultaneously edited remotely  
* [win] Enable using both syncing client and drive client while keep the Explorer file status icon work for both
* [win] Remove ccnet component to make running multiple-instances on a single machine possible
* Don't send unneccesary "api2/events" requests
* [cloud file browser] Fix uploading retrying
* [fix] Fix .eml files can't be deleted

## 6.1

### 6.1.8 (2018/05/08)

* [fix] Fix display of library search box

### 6.1.7 (2018/03/29)

* [fix] Fix file searching
* [cloud file browser] Support showing indexing progress after uploading a large file


### 6.1.6 (2018/03/13)

* [fix] Fix crash during login
* [cloud file browser] Only show search button when the server is pro edition
* Show detailed path when a library can't be synced because a file is locked
* [fix] Fix a crash during file syncing caused by files with illegal file name
* [fix] Fix a bug that causing crash during loading libraries

### 6.1.5 (2018/02/06)

* Add "trust this device" function to two-step authentication
* Add search files inside a library
* Some UI improvements


### 6.1.4 (2017/12/20)

cloud file browser

* Don't use resumable upload feature when updating a file
* Show an icon to indicate that a file is cached
* Show a warning icon when a file failed to upload to the server after changing
* User can re-upload a local modified file that failed to upload
* Add a command to open local cache folder
* Improve error messages when uploading a file or a folder
* [mac] Fix a bug that a doc/xls file uploaded automatically after downloading
* Some ui fixes and improvements

others

* Don't show the connection status of 127.0.0.1
* Disable editing of local syncing path, users can only choose a path
* Some ui fixes and improvements


### 6.1.3 (2017/11/03)

* [fix] Fix system tray icon
* Change "Shibbeloth Login" to "Single Sign On"
* [fix] Fix MacOS client using discrete GPU
* [cloud file browser] Improve file uploading after modification
* [cloud file browser, fix] Don't show quota exceeded when server return 502 error
* [cloud file browser] Show number of files in current folder


### 6.1.2 (2017/10/28)

* [Win] Update system tray icon
* Return error if repo name contains invalid characters when syncing a library
* Update local folder name when repo name is changed.
* Leave a shared library
* [fix] Fix open cloud file browser from activity view
* [fix] Fix loading more events in activity tab
* [fix, cloud file browser] Always watching local cached files after uploading failed when file changed
* [fix, cloud file browser] Use local cached version if it is changed locally

### 6.1.1 (2017/09/20)

* Improve support for syncing EML files (Don't sync EML files if only timestamp changed)
* Improve support for Copy/Paste files in cloud file browser
* [Mac] Fix opening file history from Mac
* [fix] Fix memory leak in Windows extension handler
* [fix] Fix re-login with Shibboleth
* UI/UX improvements for cloud file browser
* [fix, Windows] Fix a bug in detecting whether there is an old instance of Seafile running

### 6.1.0 (2017/08/02)


* [fix] Fix a bug that library name will be changed back when it is changed in the server
* [fix] Fix a bug that uploading progress exceeding 100%.
* [fix] Fix selectively synced subfolder disappear after logout and login again
* Use new library icons
* [fix] Fix showing of avatars
* [fix] Improve UI in Windows with high DPI screens
* Only allow https for Shibboleth login
* Clean unused logs in applet.log
* Remove the function of map a library to a network drive
* [fix] Fix an issue when uploading a deep empty folder like "A/B/C"
* Change default block size to 8MB
* [fix, mac] Popup a notification after user clicking the "Check new version" button in about dialog if the current version is the latest version


## 6.0

### 6.0.7 (2017/06/23)

* [fix] Fix auto-completion in sharing dialog
* Show contact avatars in auto-completion of sharing dialog
* [fix] Fix mis-leading error message when uploading a file to a read-only library via cloud file browser
* Add highlight background color when drag and drop a file/folder to a library
* [fix] Fix connection error in libcurl
* [fix] Fix sorting by time in cloud file browser
* [fix] Fix sorting by name case sensitive in cloud file browser
* [fix] Fix drag more than one folder to cloud file browser
* Add loading more in activity tab and search tab
* "View sync error" can only be clicked when there are sync errors
* Move seafile.log, applet.log to seafile.log.old, applet.log.old if they become too large
* Remove the "?" icon in creating new folder dialog title bar



### 6.0.6 (2017/05/08)

* Sort files by numbers if numbers contained in the file name, so "1, 10, 2, 11, 3" will be sorted as "1, 2, 3, 10, 11".
* Use native system window for Seafile main windown and cloud file browser window.
* Fix progress overflow when uploading large file using cloud file browser
* Improve the tip when removing an account in the client
* Don't show download button when select folders in cloud file browser
* Clean cache data of cloud file browser when logout an account or restart the client
* [fix] Fix display problem for high screen Windows in win10
* [fix] Fix libssl compatibility problem in Debain Stretch
* Add auto-update check

### 6.0.4 (2017/02/21)

* [fix] Fix Shibboleth login support
* Improve network connection check
* Don't log "read pipe error" into log file
* [fix] Fix the link for help page
* Improve library sharing dialog (pro edition only feature)

### 6.0.3 (2017/02/11)

* Add a dialog to list all sync errors
* Don't popup file is locked by other users error message
* Make sync error message more accurate
* [win] Support intermediate CA
* [cloud file browser] Show correct error message when quota is exceeded during file upload
* Show the server address during Shibboleth login
* Support pre-config Shibboleth server address in seafile.ini
* [fix] Show the recent shared user in sharing dialog
* "open folder" changed to "open local folder"


### 6.0.2 (deprecated)

This version has a few bugs. We will fix it soon.

### 6.0.1 (2016/12/07)

* Don't generate case conflict file/folder
* [fix] Fix popup style for Mac Sierra
* Show image thumbnail in cloud file browser
* Change label "organization" to "shared with all", "private shares" to "shared with me"

### 6.0.0 (2016/10/14)

* [fix] Fix a conflict problem with ESET anti-virus program
* Fix client name and add client version in modification history
* Add remote wipe support
* [fix] Fix sub-folder permission support

## 5.1

### 5.1.4 (2016/07/29)

* [fix] Fix seaf-daemon crash if root dir is corrupted
* [fix, pro] Fix auto-completion in sharing a folder to a user if the user name contains a space

### 5.1.3 (2016/06/27)

* Support syncing any sub-folder with a community server
* [fix, win] Fix automatically unlocking office files
* [fix, pro] Fix auto-completion in sharing a folder to a user
* auto-login for open file history in web
* Prevent generating too many "case conflict" files

### 5.1.2 (2016/06/07)

* Add context menu to view file history in web
* [fix, pro] Fix user auto-completion in folder sharing dialog
* [Linux] Fix tray icon not shown in KDE 5 https://github.com/haiwen/seafile-client/issues/697
* [win 10, fix] Fix explorer context menu has no right arrow
* [win, fix] Can't create new files/folders in "My Library" Shortcut
* [win, fix] Fix on Windows 10 sometimes the seafile client main window exceeds the height of the screen.

### 5.1.1 (2016/05/04)

* Add “Groups” category in the client’s library view
* Click notification pop up now open the exact folder containing the modified file.
* Change "Get Seafile Share Link" to "Get Seafile Download Link"
* [Fix] Use case-insensitive sorting in cloud file browser
* [Fix] Don't sync a folder in Windows if it contains invalid characters instead of creating an empty folder with invalid name
* [Fix] Fix a rare bug where sometimes files are synced as zero length files. This happens when another software doesn't change the file timestamp after changing the content of the file.

### 5.1.0 (2016/04/11)

Note: Seafile client now support HiDPI under Windows, you should remove QT_DEVICE_PIXEL_RATIO settings if you had set one previous.

* Update to QT5.6
* Add HiDPI support
* Remove corrupted local metadata when unsync or resync a library

## 5.0

### 5.0.7 (2016/03/29)

* [fix, mac] Enable multi-users running Seafile on Mac
* [win, pro] auto-lock office files (doc/ppt/excel) when open, require Seafile pro edition v5.1.0+
* Enable using system proxy setting
* Auto login when viewing unread notifications
* Record device name to modification history

### 5.0.6 (2016/03/08)

* [fix, mac] Fix deleted folder get re-uploaded if with .DS_Store inside
* [fix] Fix loading proxy configuration during start-up
* [fix] Fix a crash bug when using libcurl with multiplt https connection
* [fix] Fix sync problem when the network connection is slow
* Use GB/MB/KB instead of GiB/MiB/KiB (1GB = 1000MB = 1,000,000KB)
* [fix] Fix disappear of synced sub-folder from the main window
* Small UI improvements

### 5.0.5 (2016/02/20)

* [fix] Fix a crash bug in multi-threaded file download/upload

### 5.0.4 (2016/01/26)

* Add crash report support
* [win] Add mapping a synced library as a network drive

### 5.0.3 (2016/01/13)

* [fix] Fix German translation

### 5.0.2 (2016/01/11)

* [fix] Fix compatibility issue with F-Secure
* Add setting sync interval for a library
* Showing progress when downloading file list during the first-time syncing

### 5.0.1 (2015/12/21)

* [fix] Fix a memory leak
* Show user name instead of email in the profile area
* [pro] For pro users, you can manage the library sharing from the client now.

### 5.0.0 (2015/11/25)

* Show storage usage
* Support login via username
* Set current tab icon color to orange
* Send notifications when sync error happens for some files
* Improve file locking for Microsoft Office files
* [fix] Fix preventing syncing with any folder if it is prevented by the server
* [Windows] Set TCP send buffer size and TCP_NODELAY options
* [fix] Keep ignore files when deleting a folder (https://github.com/haiwen/seafile/issues/1383)


## 4.4

### 4.4.2 (2015/10/20)

* [fix] Fix showing data transfer percentage in syncing.
* Add open containing folder in search result

### 4.4.1 (2015/10/14)

* [fix, win] Fix a rare bug in file sync on Windows related to multi-thread downloading

### 4.4.0 (2015/09/18)

* Fix bugs in file ignore feature
* Fix popup two password input dialogs when visit an encrypted library
* Popup a tip when file conflicts happen
* Don't send the password to server when creating an encrypted library
* [Mac] Fix support for TLS 1.2
* [Win, extension] Add context menu "get internal link"
* Enable uploading of an empty folder in cloud file browser
* [pro] Enable customization of app name and logo for the main window (See https://github.com/haiwen/seafile-docs/blob/master/config/seahub_customization.md#customize-the-logo-and-name-displayed-on-seafile-desktop-clients-seafile-professional-only)
* A few small UI improvements

## 4.3

### 4.3.4 (2015/09/14)

* Fix a bug in refresh file locking status icon
* Use 3 threads instead of 10 threads when syncing files to reduce load on server

### 4.3.3 (2015/08/25)

* Fix one more syncing issues introduced in v4.3.0
* Improve the file lock icon
* Improve cloud file browser
* Fix icon overlay problem in win10
* Add back sync with existing folder

### 4.3.2 (2015/08/19)

* Fix more syncing issues introduced in v4.3.0
* Update translation
* Fix ignore feature
* Add HiDPI icons for cloud file browser

### 4.3.1 (2015/08/11)

* Fix syncing issues.

### 4.3.0 beta (2015/08/03)

* [fix, windows] Fix a bug that causes freeze of Seafile UI
* [sync] Improve index performance after a file is modified
* [sync] Use multi-threads to upload/download file blocks
* [admin] Enable config Seafile via seafile.rc in Mac/Linux or seafile.ini in Windows (https://github.com/haiwen/seafile-user-manual/blob/master/en/faq.md)
* [admin] Enable uninstall Seafile without popup "deleting config files" dialog
* Add file lock
* [mac, extension] Add getting Seafile internal link
* [mac, extension] Improve performance of showing sync status

## 4.2

### 4.2.8 (2015/07/11)

* [win] Another fix on the explorer extension
* Improve the ui for downloading the encrypted library
* filebrowser: fix a crash when closed while context menu pop up
* explorer extension: show read-only badge when a file is read-only


### 4.2.7 (2015/07/08)

* [win] Fixed another bug that will cause crash of explorer extension
* [win] Add executable file version information for the client
* [mac] Use OS X native notification when possible (OS X >= 10.8)
* [mac] Implement sync status improvement for every files
* filebrowser: fix uploading failures in the folders with permission set
* filebrowser: support "save as" multiple files simultaneously
* filebrowser: fix the sorting of folders
* filebrowser: implement get seafile internal link
* shibboleth: popup ShiLoginDialog when doing relogin
* [ui] disable the inputablity of computer name when doing login


### 4.2.6 (2015/06/25)

* [win] Fixed more memory problem that will cause crash of explorer extension

### 4.2.5 (2015/06/24)

* [win] Fixed a possible memory corruption in explorer extension
* [win] Add icon for readonly state in explorer extension
* [win] unconfigured clients now can hide the configuration wizard
* [win] ui: improve set password dialog
* [win] fix broken local DNS resolve
* [mac] add "seafile://" protocol support
* [UI] tweak search tab item padding
* Add a menu item to open seafile folder
* [UI] don't change current account after logout
* [UI] fix some bugs on account-view
* [UI] improve account management
* filebrowser: support readonly directories
* [fix] Fix creating subfolder for password-protected repo
* [fix] Fix file size integer overflow in search results

### 4.2.4 (2015/06/11)

* [win] add workarounds with auto update bugs in cloud browser
* [win] add the missing support for ipv6 (curl)
* [pro] add new tab to searching files
* [osx] fix the regularly disappearance tray icon (Qt5.4.2)
* [win] [osx] fix broken network connection sometimes after resume (Qt5.4.2)
* add an option to syncing with an existing folder with a different name
* avoid race condition when quiting
* fix a bug with opening password-protected repo in cloud browser
* ui: tweak paddings in the event activities
* filebrowser: show file type correctly along with icons
* ui: improve repo item category
* ui: show download link in share link dialog
* ui: enhance event details


### 4.2.3 (2015/05/29)

* Improve self-signed CA support
* Auto login when click "view on cloud"
* [fix] Fix bugs with open directory from modification details dialog (pro)
* [fix] Fix incorrect transfer rates for each sync task
* [fix] Fix auto uploaded modified files in cloud file browser for some office files


### 4.2.2 (2015/05/26)

* [win] Use Openssl to handle HTTPS connection
* [Mac] Load trusted CA certificates from Keychain
* [fix] Fix logout/login issue (libraries stay at waiting for sync)
* [fix] Fix a file deletion problem in Mac client
* Ignore the others of ssl errors if we have dealt with one
* Expand env variable in preconfigure seafile directory
* Hide explorer extension option on other platforms than windows
* Cloud file browser: fix broken title bar when minimized on windows
* Remove unused option in setting dialog


### 4.2.1 (2015/05/14)

* [fix] Fix "Waiting for synchronization" problem
* [win] Fixed encoding problem in the explorer extension
* [win] Prefer home for seafile data dir when it is on the largest drive
* [win] Adopt preconfigure directory for initialization if any
* [win] Adopt preconfigure server addr for adding accounts if any
* [win] Open current repo worktree when clicking ballon message
* [mac] Fix some memory leaks
* Description is no longer required when creating repositories
* [fix] Fix webview url for server version >= 4.2.0
* redesign the event list in activity tab (pro)
* [fix] Fix window focus when creating repository from drag and drop
* [fix] filebrowser: fix sorting column kind for non-English users
* network: disable weak ciphers explicitly
* [fix] Fix a issue synced subfolders are not shown when client starts
* [fix] Remember the used server addresses for convenience
* [fix] Fix the ssl handshake errors with custom CA seafile servers

### 4.2.0 (2015/05/07)

* [win] Support overlay icons for files based on the sync status
* Use http syncing only
* Auto detect existing folders and prompt "syncing with existing folder" in first time syncing
* [win] Open desktop icon popup the main window if Seafile is already running
* Respect umask on Linux
* [fix] Fix main window stay outside screens problem
* [fix] Fix a few small syncing issues.
* [osx] Allow sharing root directory from finder extension
* Auto login from the client when click the server URL (need v4.2 server)
* Auto logout when the authorization is expired (require server supports)
* Auto detect existing folders in first time syncing
* Save server info persistently
* More miscellaneous fixes


## 4.1

### 4.1.6 (2015/04/21)

* [win] add overlay icon to show sync status at the library level
* [win] add an option to enable/disable explorer extension support
* [mac] add finder sync extension (need OSX 10.10.x)
* [mac] fix the broken hide-the-dock option in some cases
* [linux] fix the bug that we have two title bar for some desktop environment
* Update shibboleth support
* [cloud file browser] Pop notifications when new versions of cached files uploaded
* [cloud file browser] Add a save_as action
* [cloud file browser] Improve file browser's UI
* [fix] Fix a rare case of login failure by using complex password, a regression from 4.1.0
* [fix] Fix a rare case of program crash when changing accounts
* Update avatars automatically
* More miscellaneous fixes

### 4.1.5 (2015/04/09)

* Add Shibboleth login support
* Reset local modified files to the state in Server when resyncing a read-only library.
* [fix] Fix unable to unsync a library when it is in the state of uploading files
* [fix, win] handle file/directory locking more gracefully
* Add http user agent for better logging in Apache/Nginx
* [fix] Fix timeout problem in first time syncing for large libraries


### 4.1.4 (2015/03/27)

* [fix, win] Fix Windows explore crash by seafile extension when right clicking on "Libraries->Documents" at the right side

### 4.1.3 (2015/03/23)

* [fix] Fix unable to sync bug (permission denial) if the Windows system user name contains space like "test 123" introduced in v4.1.2
* [win] Update version of OpenSSL to 1.0.2a

### 4.1.2 (2015/03/19) (deprecated)

* Add logout/login support (need server 4.1.0+)
* fix proxy password disappearance after restarting issue
* mask proxy password in the setting dialog
* [Fix] fix unexpected disconnection with proxy servers
* [Fix] fix a conflicting case when we have read-only sharing repository to a group
* update translations
* support darkmode (OS X)
* and other minor fixes


### 4.1.1 (2015/03/03)

* Add network proxy support for HTTP sync
* [Mac] Add more complete support for retina screen
* Improve UI
* Add option for killing old Seafile instance when starting a new one
* Add experimental support for HiDPI screen on Windows and Linux
* Showing shared from for private shared libraries
* Use API token v2 for shibbloeth login
* [fix] Fix some bugs in uploading file from cloud file browser
* fix a bug of uploading directory from cloud file browser (pro version)

### 4.1.0 beta (2015/01/29)

* Add support for HDPI screen by using QT5
* [win] Add context menu for generating share link
* Enable changing of interface language
* Make http syncing the default option (will fall back to non-http sync automatically if the server does not support it)
* [fix] Fix a problem in handling long path in Windows


## 4.0

### 4.0.7 (2015/01/22)

* [win] support for file path greater than 260 characters.

In the old version, you will sometimes see strange directory such as "Documents~1" synced to the server, this because the old version did not handle long path correctly.

### 4.0.6 (2015/01/09)

* [fix] Fix a timeout problem during file syncing (Which also cause program crash sometimes).

### 4.0.5 (2014/12/24)

* [fix] [mac] More on fixing mac syncing problem
* [Linux, Mac] Do not ignore files with invalid name in Windows
* [fix] Fix "sync now"
* [fix] Handle network problems during first time sync
* [file browser] Support create folders
* [file browser] Improve interface
* [file browser] Support multiple file selection and operation

### 4.0.4 (2014/12/15)

* [fix] [mac] Fix a syncing problem when library name contains "è" characters
* [Windows] Gracefully handle file lock issue.

In the previous version, when you open an office file in Windows, it is locked by the operating system. If another person modify this file in another computer, the syncing will be stopped until you close the locked file. In this new version, the syncing process will continue. The locked file will not be synced to local computer, but other files will not be affected.

### 4.0.3 (2014/12/03)

* [fix] [mac] Fix a syncing problem when library name contains "è" characters
* [fix] Fix another bug in syncing with HTTP protocol

### 4.0.2 (2014/11/29)

* [fix] Fix bugs in syncing with HTTP protocol

### 4.0.1 (2014/11/18)

* [fix] Fix crash problem

### 4.0.0 (2014/11/10)

* Add http syncing support
* Add cloud file browser


## 3.1

### 3.1.12 (2014/12/01)

* [fix] Fix a syncing problem for files larger than 100MB.

### 3.1.11 (2014/11/15)

* [fix] Fix "sometimes deleted folder reappearing problem" on Windows.

You have to update all the clients in all the PCs. If one PC does not use the v3.1.11, when the "deleting folder" information synced to this PC, it will fail to delete the folder completely. And the folder will be synced back to other PCs. So other PCs will see the folder reappear again.

### 3.1.10 (2014/11/13)

* [fix] Fix conflict problem when rename the case of a folder
* [fix] Improve the deleted folder reappearing problem if it contains ignored files
* [fix] Add "resync" action


### 3.1.8 (2014/10/28)

* Better support read-only sync. Now local changes will be ignored.
* [Mac,Fix] Fix detection of local changes.

### 3.1.7 (2014/09/28)

* [fix] Fix another not sync problem when adding a big file (>100M) and several other files.


### 3.1.6 (2014/09/19)

* Add option to sync MSOffice/Libreoffice template files
* Add back choosing the "Seafile" directory when install Seafile client.
* Add option to change the address of a server
* Add menu item for open logs directory
* [Mac] Add option for hide dock icon
* Show read-only icon for read-only libraries
* Show detailed information if SSL certification is not valid
* Do not show "Seafile was closed unexpectedly" message when turning down of Windows
* Don't refresh libraries/starred files when the window is not visible
* Move local file to conflict file when syncing with existing folder
* Add more log information when file conflicts happen
* [fix] Fix sync error when deleting all files in a library
* [fix] Fix not sync problem when adding a big file (>100M) and several small files together.
* [fix] Fix Windows client doesn't save advanced settings

### 3.1.5 (2014/08/14)

- Do not ignore libreoffice lock files
- [fix] Fix possible crash when network condition is not good.
- [fix] Fix problem in syncing a large library with an existing folder
- Add option "do not unsync a library even it is deleted in the server"
- [mac] upgrade bundled openssl to 1.0.1i
- [mac] remove unused ossp-uuid dependency
- [mac] fix code sign issue under OSX 10.10


### 3.1.4 (2014/08/05)

* [fix, Mac] Fix case conflict problem under Mac

### 3.1.3 (2014/08/04)

* [fix] Fix showing bubble
* [Mac] More UI improvements
* Do not ignore 'TMP', 'tmp' files

### 3.1.2 (2014/08/01)

* Do not show rotate icon when checking update for a library
* Do not show activity tab if server not supported
* [Mac] show unread messages tray icon on Mac
* [Mac] Improve UI for Mac
* [fix] Support rename files from upper case to lower case or vice versa.

### 3.1.1 (2014/07/28)

* [Win] Fix crash problems
* [Win] Fix interface freeze problem when restoring the window from the minimized state
* Remove the need of selecting Seafile directory

### 3.1.0 (2014/07/24)

* Add starred files and activity history
* Notification on unread messages
* Improve icons for Retina screen
* Load and show avatar from server
* Use new and better icons

## 3.0

### 3.0.4

* [fix] Fix a syncing bug

### 3.0.3

* [fix] Fix syncing problem when update from version 2.x
* [fix] Fix UI when syncing an encrypted library

### 3.0.2

* [fix] Fix a syncing issue.

### 3.0.1

* Improved ssl check
* Imporved ui of sync library dialog
* Send device name to the server
* [fix] Fixed system shutdown problem
* [fix] Fixed duplicate entries in recently updated libraries list
* Remove ongoing library download tasks when removing an account
* Updated translation
* [fix] Fix file ID calculation


### 3.0.0

* Adjust settings dialog hint text size
* Improved login dialog

## 2.2

### 2.2.0

* Add check for the validity of servers' SSL Certification

## 2.1

### 2.1.2


* Show proper error message when failed to login
* Show an error message in the main window when failed to get libraries list
* Open seahub in browser when clicking the account url
* Add an option "Do not automatically unsync a library"
* Improve sync status icons for libraries
* Show correct repo sync status icon even if global auto sync is turned off
* Show more useful notification than "Auto merge by system" when conflicts were merged

### 2.1.1

* Make the main window resizable
* [windows] Improved tray icons
* Show detailed network error when login failed
* Show sub-libraries
* [windows] Use the name of the default library as the name of the virtual disk


### 2.1.0

* Redesigned the UI of the main window
* [windows] Download the default library, and creates a virtual disk for it in "My Computer"
* Support drag and drop a folder to sync
* Automatically check for new version on startup
* Support of file syncing from both inside and outside the LAN
* [fix] Fix a bug of clicking the tray icon during initialization
* [fix] fixed a few bugs in merge and handling of empty folders
* [mac] Fixed the alignment in settings dialog

## 2.0

### 2.0.8

* [fix] Fix UI freeze problem during file syncing
* Improve syncing speed (More improvements will be carried out in our next version)

### 2.0.7 (Don't use it)

Note: This version contains a bug that you can't login into your private servers.

* [fix] Fix a bug which may lead to crash when exiting client
* show library download progress in the library list
* add official server addresses to the login dialog
* improve library sync status icons
* [windows] use the same tray icon for all windows version later than Vista
* translate the bubble notification details to Chinese

### 2.0.6

* [Windows] Fix handling daylight saving time
* Improve library details dialog
* [fix] Fix a bug in api request
* Improve the handling of "Organization" libraries
* [fix] Fix the settings of upload/download rate limit
* [fix] Update French/German translations
* [cli] Support the new encryption scheme

### 2.0.5

* Improve UI
* Fix a bug in French translation

### 2.0.4

* Improve memory usage during syncing
* [Windows] Change system tray icons
* [Windows] Hide seafile-data under Seafile folder
* [fix] Fix remember main window's location
* Improve the dialog for adding account
* Add setting for showing main windows on seafile start up
* Open local folder when double click on a library
* Show warning dialog when login to a server with untrusted ssl certification

### 2.0.3

* sync empty folder
* support seafile crypto v2
* show warning in system tray when some servers not connected
* add German/French/Hungarian translations
* change system tray icons for Windows
* show "recent updated libraries"
* reduce cpu usage
* [fix] fixed a bug when login with password containing characters like "+" "#"
* ask the user about untrusted ssl certs when login
* add Edit->Settings and "view online help" menu item


### 2.0.2

* [Fix] Fix compatibility with server v1.8
* [Fix] the bug of closing the settings dialog
* Add Chinese translation
* Show error detail when login failed
* Remember main window position and size
* Improve library detail dialog
* Add unsync a library

### 2.0.0

* Re-implement GUI with Qt

## 1.8

1.8.1

* [bugfix] Fix a bug in indexing files

1.8.0

* [bugfix] Skip chunking error
* Improve local web interface
* Remove link to official Seafile server
* Ignore all temporary files created by Microsoft Office
* Add French and Slovak translation

## 1.7

1.7.3

* [bugfix] Fix a small syncing bug.

1.7.2

* [bugfix] Fix a bug in un-syncing library. <https://github.com/haiwen/seafile/issues/270>

1.7.1

* [win] Fix selecting of Seafile directory

1.7.0

* [win] Enable selecting of Seafile directory
* Enable setting of upload/download speed
* Use encrypted transfer by default
* Support ignore certain files by seafile-ignore.txt

## 1.6

1.6.2

* [bugfix,mac] Fix a bug in supporting directory names with accents

1.6.1

* [bugfix] Prevent running of multiple seaf-daemon instance
* Improve the efficiency of start-up GC for libraries in merge stage
* [mac,win] Handle case-conflict files by renaming

1.6.0

* [linux,mac] Support symbolic links
* [seaf-cli] clean logs
* Do not re-download file blocks when restart Seafile during file syncing
* [bugfix] Fix treating files as deleted when failed to create it due to reasons like disk full.
* [bugfix] Fix several bugs when shutdown Seafile during some syncing operation.

## 1.5

1.5.3

* Log the version of seafile client when start-up.
* [bugfix] Fix a bug when simultaneously creating an empty folder with same name in server and client.
* [bugfix] Always use IPv4 address to connect a server.

1.5.2

* [bug] Fix a memory-access bug when showing "Auto merge by seafile system" in bubble

1.5.1

* [Seaf-cli] Fix a bug in initializing the config dir.
* [bugfix] Improve the robustness of DNS looking-up.
  Use standard DNS looking-up instead of libevent's non-blocking version.

1.5.0

* Add Seaf-cli
* Check the correctness of password in the beginning of downloading a encrypted library.
* Show detailed information in bubble
* Enable change the server's address in the client
* [Linux] Do not popup the browser when start up
* Remove seafile-web.log
