## Known issues

* In version 0.5.1, we add the feature that the mounted drive is only visible to the current user, so some exe files can't be executed if stored in the drive because it needs admin privilege to run
* In version 0.5.1, rename a non-cached folder or file will lead to sync error.
* In version 0.5.0 Copy exe files to SeaDrive on Win 7 will freeze the explorer

## ChangeLog

### 0.7.0 (2017/06/07)

* Add support for multi-users using SeaDrive on a single desktop. But different users must choose different drive letters.
* Improve write performance
* [fix] When a non-cached file is locked in the server, the "lock" icon will be shown instead of the "cloud" icon.
* Add "automatically login" option in login dialog
* Add file transfer status dialog.

### 0.6.2 (2017/04/22)

* [fix] Fix after moving a file to a newly created sub folder, the file reappear when logout and login
* Refresh current folder and the destination folder after moving files from one library to another library
* [fix] Fix file locking not work
* [fix] Fix sometimes files can't be saved

### 0.6.1 (2017/03/27)

* [fix] Don't show a popup notification to state that a file can't be created in `S:` because a few programs will automatically try to create files in `S:`

### 0.6.0 (2017/03/25)

* Improve syncing status icons
* Show error in the interface when there are syncing errors
* Don't show rorate icon when downloading/uploading metadata
* [fix] Don't download files when the network is not connected


### 0.5.2 (2017/03/09)

* [fix] Rename a non-cached folder or file will lead to sync error.

### 0.5.1 (2017/02/16)

* [fix] Fix copying exe files to SeaDrive on Win 7 will freeze the explorer
* The mounted drive is only visible to the current user
* Add popup notification when syncing is done
* [fix] Fix any change in the settings leads to a drive letter change

### 0.5.0 (2017/01/18)

* Improve stability
* Support file locking
* Support sub-folder permission 
* [fix] Fix 1TB limitation
* User can choose disk letter in settings dialog
* Support remote wipe
* [fix] Use proxy server when login
* Click system tray icon open SeaDrive folder
* Support application auto-upgrade

### 0.4.2 (2016/12/16)

* [fix] Fix SeaDrive initialization error during Windows startup

### 0.4.1 (2016/11/07)

* [fix] Fix a bug that lead to empty S: drive after installation.

### 0.4.0 (2016/11/05)

* [fix] Fix a bug that leads to generation of conflict files when editing
* Add translations
* Update included Dokany library to 1.0
* Don't show encrypted libraries even in command line
* Show permission error when copy a file to the root
* Show permission error when try to modify a read-only folder
* Show permission error when try to delete a folder in the root folder

### 0.3.1 (2016/10/22)

* Fix link for license terms
* Use new system tray icon
* Add notification for cross-libraries file move

### 0.3.0 (2016/10/14)

* Support selecting Drive letter
* Don't create folders like msiS50.tmp on Windows
* [fix] Fix cache size limit settings
* Correctly show the storage space if the space is unlimited on the server side.

### 0.2.0 (2016/09/15)

* Add shibboleth support
* Show a dialog notify the client is downloading file list from the server during initialisation
* Show transfer rate
* [fix] Fix a bug that lead to the file modification time to be empty
* [fix] Fix a bug that lead to files not be uploaded

### 0.1.0 (2016/09/02)

* Initial release