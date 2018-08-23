# Web API (For Seafile server v5.1.0+)

<p>
<div class="toc">
<ul>
<li>
<a href="#seafile-web-api">Seafile Web API</a>
<ul>
    <li><a href="#api-basics">API Basics</a></li>
    <li><a href="#status-code">Status Code</a></li>
    <li><a href="#quick-start">Quick Start</a></li>
    <li>
        <a href="#account">Account</a>
        <ul>
            <li><a href="#check-account-info">Check Account Info</a></li>
            <li><a href="#client-login">Get Client Login URL</a></li>
            <li><a href="#server-info">Get Server Information</a></li>
        </ul>
    </li>
    <li>
        <a href="#starred-files">Starred Files</a>
        <ul>
            <li><a href="#list-starred-files">List starred files</a></li>
            <li><a href="#star-a-file">Star A File</a></li>
            <li><a href="#unstar-a-file">Unstar A File</a></li>
        </ul>
    </li>
    <li>
        <a href="#group">Group</a>
        <ul>
            <li><a href="#list-groups">List Groups</a></li>
            <li><a href="#add-a-group">Add a Group</a></li>
            <li><a href="#get-info-of-a-group">Get Info of a Group</a></li>
            <li><a href="#rename-a-group">Rename a Group</a></li>
            <li><a href="#transfer-a-group">Transfer a Group</a></li>
            <li><a href="#delete-a-group">Delete a Group</a></li>
            <li><a href="#quit-group">Quit Group</a></li>
            <li>
                <a href="#group-member">Group Member</a>
                <ul>
                    <li><a href="#list-group-members">List Group Members</a></li>
                    <li><a href="#add-a-group-member">Add a Group Member</a></li>
                    <li><a href="#bulk-add-group-members">Bulk Add Group Members</a></li>
                    <li><a href="#get-info-of-a-group-member">Get Info of a Group Member</a></li>
                    <li><a href="#set-a-group-member-admin">Set a Group Member Admin</a></li>
                    <li><a href="#unset-a-group-member-admin">Unset a Group Member Admin</a></li>
                    <li><a href="#delete-a-group-member">Delete a Group Member</a></li>
                </ul>
            </li>
            <li>
                <a href="#group-message">Group Message</a>
                <ul>
                    <li><a href="#get-group-messages">Get Group Messages</a></li>
                    <li><a href="#send-a-group-message">Send A Group Message</a></li>
                    <li><a href="#delete-a-group-message">Delete A Group Message</a></li>
                </ul>
            </li>
            <li>
                <a href="#group-owned-libraries">Group Owned Libraries</a>
                <ul>
                    <li><a href="#add-group-owned-library">Add Group Owned Library</a></li>
                    <li><a href="#delete-group-owned-library">Delete Group Owned Library</a></li>
                    <li><a href="#get-group-owned-library-user-share-info">Get Group Owned Library User Share Info</a></li>
                    <li><a href="#share-group-owned-library-to-user">Share Group Owned Library to User</a></li>
                    <li><a href="#modify-group-owned-library-user-share-permission">Modify Group Owned Library User Share Permission</a></li>
                    <li><a href="#delete-group-owned-library-user-share">Delete Group Owned Library User Share</a></li>
                    <li><a href="#get-group-owned-library-group-share-info">Get Group Owned Library Group Share Info</a></li>
                    <li><a href="#share-group-owned-library-to-user">Share Group Owned Library to Group</a></li>
                    <li><a href="#modify-group-owned-library-group-share-permission">Modify Group Owned Library Group Share Permission</a></li>
                    <li><a href="#delete-group-owned-library-group-share">Delete Group Owned Library Group Share</a></li>
                    <li><a href="#modify-group-owned-library-sub-folder-permission">Modify Group Owned Library Sub-Folder Permission</a></li>
                </ul>
            </li>
        </ul>
    </li>
    <li>
        <a href="#share">Share</a>
        <ul>
            <li>
                <a href="#share-link">Share Link</a>
                <ul>
                    <li><a href="#list-all-share-links">List all Share Links</a></li>
                    <li><a href="#list-share-links-of-a-library">List Share Links of a Library</a></li>
                    <li><a href="#list-share-link-of-a-folder-file">List Share Link of a Folder(File)</a></li>
                    <li><a href="#create-share-link">Create Share Link</a></li>
                    <li><a href="#delete-share-link">Delete Share Link</a></li>
                    <li><a href="#send-share-link-email">Send Share Link Email</a></li>
                    <li><a href="#list-direntry-in-dir-download-link">List Direntry in Dir Download Link</a></li>
                </ul>
            </li>
            <li>
                <a href="#upload-link">Upload Link</a>
                <ul>
                    <li><a href="#list-upload-links">List Upload Links</a></li>
                    <li><a href="#create-upload-link">Create Upload Link</a></li>
                    <li><a href="#delete-upload-link">Delete Upload Link</a></li>
                    <li><a href="#send-upload-link-email">Send Upload Link Email</a></li>
                </ul>
            </li>
            <li>
                <a href="#shared-libraries">Shared Libraries</a>
                <ul>
                    <li><a href="#list-user-shared-libraries">List User Shared Libraries</a></li>
                    <li><a href="#list-group-shared-libraries">List Group Shared Libraries</a></li>
                    <li><a href="#list-be-shared-libraries">List Be Shared Libraries</a></li>
                    <li><a href="#delete-be-shared-library">Delete Be Shared Library</a></li>
                    <li><a href="#share-a-library-to-user">Share a Library to User</a></li>
                    <li><a href="#unshare-a-library-from-user">Unshare a Library from User</a></li>
                    <li><a href="#update-permission-of-user-shared-library">Update Permission of User Shared Library</a></li>
                    <li><a href="#share-a-library-to-group">Share a Library to Group</a></li>
                    <li><a href="#unshare-a-library-from-group">Unshare a Library from Group</a></li>
                    <li><a href="#update-permission-of-group-shared-library">Update Permission of Group Shared Library</a></li>
                    <li><a href="#batch-share-libraries-to-user">Batch Share Libraries to User</a></li>
                    <li><a href="#batch-share-libraries-to-group">Batch Share Libraries to Group</a></li>
                </ul>
            <li>
                <a href="#shared-folders">Shared Folders</a>
                <ul>
                    <li><a href="#share-a-folder">Share A Folder</a></li>
                    <li><a href="#list-shared-folders">List Shared Folders</a></li>
                    <li><a href="#update-shared-folder-permission">Update Shared Folder Permission</a></li>
                    <li><a href="#unshare-a-folder">Unshare A Folder</a></li>
                </ul>
            </li>
            </li>
        </ul>
    </li>
    <li>
        <a href="#folder-permission">Folder Permission</a>
        <ul>
            <li>
                <a href="#user-folder-permission">User Folder Permission</a>
                <ul>
                    <li><a href="#get-user-folder-permission">Get User Folder Permission</a></li>
                    <li><a href="#set-user-folder-permission">Set User Folder Permission</a></li>
                    <li><a href="#modify-user-folder-permission">Modify User Folder Permission</a></li>
                    <li><a href="#delete-user-folder-permission">Delete User Folder Permission</a></li>
                </ul>
            </li>
            <li>
                <a href="#group-folder-permission">Group Folder Permission</a>
                <ul>
                    <li><a href="#get-group-folder-permission">Get Group Folder Permission</a></li>
                    <li><a href="#set-group-folder-permission">Set Group Folder Permission</a></li>
                    <li><a href="#modify-group-folder-permission">Modify Group Folder Permission</a></li>
                    <li><a href="#delete-group-folder-permission">Delete Group Folder Permission</a></li>
                </ul>
            </li>
        </ul>
    </li>
    <li>
        <a href="#library">Library</a>
        <ul>
            <li><a href="#get-default-lib">Get Default Library</a></li>
            <li><a href="#create-default-lib">Create Default Library</a></li>
            <li><a href="#list-libraries">List Libraries</a></li>
            <li><a href="#get-library-info">Get Library Info</a></li>
            <li><a href="#get-library-owner">Get Library Owner</a></li>
            <li><a href="#get-library-history">Get Library History</a></li>
            <li><a href="#get-library-history-limit-days">Get Library History Limit Days</a></li>
            <li><a href="#set-library-history-limit-days">Set Library History Limit Days</a></li>
            <li><a href="#create-library">Create Library</a></li>
            <li><a href="#check/create-sub-library">Check/Create Sub Library</a></li>
            <li><a href="#delete-library">Delete Library</a></li>
            <li><a href="#rename-library">Rename Library</a></li>
            <li><a href="#transfer-library">Transfer Library</a></li>
            <li><a href="#decrypt-library">Decrypt Library</a></li>
            <li><a href="#create-public-lib">Create Public Library</a></li>
            <li><a href="#set-exist-lib-as-public-lib">Set Exist Lib as Public Library</a></li>
            <li><a href="#remove-public-lib">Remove Public Library</a></li>
            <li><a href="#fetch-library-download-info">Fetch library download info</a></li>
            <li><a href="#search-files-in-libraries">Search Files in Libraries</a></li>
            <li><a href="#get-library-download-links">Get Library Download Links</a></li>
            <li><a href="#get-library-upload-links">Get Library Upload Links</a></li>
            <li><a href="#delete-library-download-link">Delete Library Download Link</a></li>
            <li><a href="#delete-library-upload-link">Delete Library Upload Link</a></li>
            <li><a href="#search-library-by-name">Search Library By Name</a></li>
        </ul>
    </li>
    <li>
        <a href="#file">File</a>
        <ul>
            <li><a href="#view-file-through-owa">View File Through Owa</a></li>
            <li><a href="#download-file">Download File</a></li>
            <li><a href="#get-file-detail">Get File Detail</a></li>
            <li><a href="#get-file-history">Get File History</a></li>
            <li><a href="#restore-file-from-history">Restore File From History</a></li>
            <li><a href="#download-file-revision">Download File From a Revision</a></li>
            <li><a href="#create-file">Create File</a></li>
            <li><a href="#rename-file">Rename File</a></li>
            <li><a href="#lock-file">Lock File</a></li>
            <li><a href="#unlock-file">Unlock File</a></li>
            <li><a href="#move-file">Move File</a></li>
            <li><a href="#copy-file">Copy File</a></li>
            <li><a href="#revert-file">Revert File</a></li>
            <li><a href="#delete-file">Delete File</a></li>
            <li>
                <a href="#upload-file">Upload File</a>
                <ul>
                    <li><a href="#get-upload-link">Get Upload Link</a></li>
                    <li><a href="#upload-file-1">Upload File</a></li>
                </ul>
            </li>
            <li>
                <a href="#resumable-upload-file">Resumable Upload File</a>
                <ul>
                    <li><a href="#resumable-check-if-enabled">Check If Enable Resumable Upload</a></li>
                    <li><a href="#resumable-get-upload-link">Get Upload Link</a></li>
                    <li><a href="#resumable-get-bytes-already-upload">Get Bytes Already Uploaded</a></li>
                    <li><a href="#resumable-upload-file-1">Upload File</a></li>
                </ul>
            </li>
            <li>
                <a href="#update-file">Update File</a>
                <ul>
                    <li><a href="#get-update-link">Get Update Link</a></li>
                    <li><a href="#update-file-1">Update File</a></li>
                </ul>
            </li>
            <li><a href="#get-upload-blocks-link">Uploading Large File in Blocks</a></li>
            <li><a href="#get-update-blocks-link">Get Update Blocks Link</a></li>
            <li>
                <a href="#file-comments">File Comment</a>
                <ul>
                    <li><a href="#get-comment">Get Comment</a></li>
                    <li><a href="#delete-comment">Delete Comment</a></li>
                    <li><a href="#list-comments">List Comments</a></li>
                    <li><a href="#post-comments">Post Comments</a></li>
                    <li><a href="#get-number-of-comments">Get Number of Comments</a></li>
                </ul>
            </li>
            <li><a href="#get-smart-link-for-a-file">Get Smart Link for a File</a></li>
        </ul>
    </li>
    <li>
        <a href="#directory">Directory</a>
        <ul>
            <li><a href="#list-directory-entries">List Directory Entries</a></li>
            <li><a href="#get-directory-detail">Get Directory Detail</a></li>
            <li><a href="#create-new-directory">Create New Directory</a></li>
            <li><a href="#rename-directory">Rename Directory</a></li>
            <li><a href="#delete-directory">Delete Directory</a></li>
            <li><a href="#download-directory">Download Directory</a></li>
            <li><a href="#revert-directory">Revert Directory</a></li>
        </ul>
    </li>
    <li>
        <a href="#asynchronously-copy-move-file-directory">Asynchronously Copy/Move File/Directory</a>
        <ul>
            <li><a href="#asynchronously-copy-move-file-directory-get-task-id">Get Task Id</a></li>
            <li><a href="#asynchronously-copy-move-file-directory-cancel-task">Cancel Task</a></li>
            <li><a href="#asynchronously-copy-move-file-directory-query-progress">Query Progress</a></li>
        </ul>
    </li>
    <li>
        <a href="#multiple-files-directories">Multiple Files / Directories</a>
        <ul>
            <li><a href="#multiple-files-directories-copy">Copy</a></li>
            <li><a href="#multiple-files-directories-move">Move</a></li>
            <li><a href="#multiple-files-directories-delete">Delete</a></li>
            <li><a href="#multiple-files-directories-download">Download</a></li>
        </ul>
    </li>
    <li>
        <a href="#avatar">Avatar</a>
        <ul>
            <li><a href="#update-user-avatar">Update User Avatar</a></li>
            <li><a href="#get-user-avatar">Get User Avatar</a></li>
            <li><a href="#get-group-avatar">Get Group Avatar</a></li>
        </ul>
    </li>
    <li>
        <a href="#devices">Devices</a>
        <ul>
            <li><a href="#get-user-devices">Get User Devices</a></li>
            <li><a href="#unlink-user-device">Unlink User Device</a></li>
        </ul>
    </li>
    <li>
        <a href="#snapshot-label">Snapshot Label</a>
        <ul>
            <li><a href="#get-snapshot-label">Get Snapshot Label</a></li>
            <li><a href="#create-new-snapshot-label">Create New Snapshot Label</a></li>
            <li><a href="#update-snapshot-label">Update Snapshot Label</a></li>
            <li><a href="#delete-snapshot-label">Delete Snapshot Label</a></li>
        </ul>
    </li>
    <li><a href="#get-file-activities">Get File Activities</a></li>
    <li><a href="#get-thumbnail-image">Get Thumbnail Image</a></li>
    <li><a href="#search-user">Search User</a></li>
</ul>
</li>
<li>
<a href="#admin-only">Admin Only</a>
<ul>
    <li>
        <a href="#admin-only-account">Account</a>
        <ul>
            <li><a href="#admin-only-list-accounts">List Accounts</a></li>
            <li><a href="#admin-only-get-account">Get Account Info</a></li>
            <li><a href="#admin-only-create-account">Create Account</a></li>
            <li><a href="#admin-only-update-account">Update Account</a></li>
            <li><a href="#admin-only-migrate-account">Migrate Account</a></li>
            <li><a href="#admin-only-delete-account">Delete Account</a></li>
        </ul>
    </li>
    <li>
        <a href="#admin-only-devices">Devices</a>
        <ul>
            <li><a href="#admin-only-get-desktop-devices">Get Desktop Devices</a></li>
            <li><a href="#admin-only-get-mobile-devices">Get Mobile Devices</a></li>
            <li><a href="#admin-only-unlink-user-device">Unlink User Device</a></li>
            <li><a href="#admin-only-get-device-errors">Get Device Errors</a></li>
            <li><a href="#admin-only-clean-device-errors">Clean Device Errors</a></li>
        </ul>
    </li>
    <li>
        <a href="#admin-only-get-snapshots-by-label">Get Snapshots by Label</a>
    </li>
    <li>
        <a href="#admin-only-default-library">Default Library</a>
        <ul>
            <li><a href="#admin-only-get-user-default-library">Get User Default Library</a></li>
            <li><a href="#admin-only-create-user-default-library">Create User Default Library</a></li>
        </ul>
    </li>
    <li>
        <a href="#admin-only-libraries">Librairies</a>
        <ul>
            <li><a href="#admin-only-get-all-libraries">Get all Libraries</a></li>
            <li><a href="#admin-only-search-library-by-name">Search Library by Name</a></li>
            <li><a href="#admin-only-search-library-by-owner">Search Library by Owner</a></li>
            <li><a href="#admin-only-delete-a-library">Delete a Library</a></li>
            <li><a href="#admin-only-transfer-a-library">Transfer a Library</a></li>
            <li><a href="#admin-only-get-library-dirents">Get Library Dirents</a></li>
            <li><a href="#admin-only-get-all-deleted-librares">Get All Deleted Libraries</a></li>
            <li><a href="#admin-only-get-deleted-librares-by-owner">Get Deleted Libraries by Owner</a></li>
            <li><a href="#admin-only-clean-deleted-library">Clean Deleted Library</a></li>
            <li><a href="#admin-only-restore-deleted-library">Restore Deleted Library</a></li>
            <li><a href="#admin-only-clean-all-deleted-libraries">Clean ALl Deleted Libraries</a></li>
        </ul>
    </li>
    <li>
        <a href="#admin-only-shares">Shares</a>
        <ul>
            <li><a href="#admin-only-get-repo-user-shares">Get Repo User Shares</a></li>
            <li><a href="#admin-only-get-repo-group-shares">Get Repo Group Shares</a></li>
            <li><a href="#admin-only-share-repo-to-user">Share Repo to User</a></li>
            <li><a href="#admin-only-share-repo-to-group">Share Repo to Group</a></li>
            <li><a href="#admin-only-modify-repo-user-share-permission">Modify Repo User Share Permission</a></li>
            <li><a href="#admin-only-modify-repo-group-share-permission">Modify Repo Group Share Permission</a></li>
            <li><a href="#admin-only-delete-repo-user-share">Delete Repo User Share</a></li>
            <li><a href="#admin-only-delete-repo-group-share">Delete Repo Group Share</a></li>
        </ul>
    </li>
    <li>
        <a href="#admin-only-groups">Groups</a>
        <ul>
            <li><a href="#admin-only-get-all-groups">Get all Groups</a></li>
            <li><a href="#admin-only-delete-a-group">Delete a Group</a></li>
            <li><a href="#admin-only-transfer-a-group">Transfer a Group</a></li>
            <li><a href="#admin-only-set-group-quota">Set Group Quota</a></li>
            <li><a href="#admin-only-get-group-libraries">Get Group Libraries</a></li>
            <li><a href="#admin-only-delete-group-library">Delete Group Library</a></li>
            <li><a href="#admin-only-get-group-members">Get Group Members</a></li>
            <li><a href="#admin-only-delete-group-member">Delete Group Member</a></li>
            <li><a href="#admin-only-add-group-member">Add Group Member</a></li>
            <li><a href="#admin-only-update-group-member-role">Update Group Member Role</a></li>
            <li><a href="#admin-only-add-group-owned-library">Add Group Owned Library</a></li>
            <li><a href="#admin-only-delete-group-owned-library">Delete Group Owned Library</a></li>
            <li><a href="#admin-only-modify-group-owned-library-sub-folder-permission">Modify Group Owned Library Sub-Folder Permission</a></li>
        </ul>
    </li>
    <li>
        <a href="#admin-only-shared-links">Shared Links</a>
        <ul>
            <li>
                <a href="#admin-only-download-links">Download Links</a>
                <ul>
                    <li><a href="#admin-only-download-link-get-shared-file-dir-info">Get Shared File/Dir Info</a></li>
                    <li><a href="#admin-only-download-link-get-dirents-in-shared-dir">Get Sub File/Dir List in Shared Dir</a></li>
                    <li><a href="#admin-only-download-link-download">Download File/Dir</a></li>
                    <li><a href="#admin-only-download-link-check-password">Check Password</a></li>
                </ul>
                <a href="#admin-only-upload-links">Upload Links</a>
                <ul>
                    <li><a href="#admin-only-upload-link-get-shared-dir-info">Get Shared Dir Info</a></li>
                    <li><a href="#admin-only-upload-link-upload">Upload File</a></li>
                    <li><a href="#admin-only-upload-link-check-password">Check Password</a></li>
                </ul>
            </li>
        </ul>
    </li>
    <li>
        <a href="#admin-only-log">Log</a>
        <ul>
            <li><a href="#admin-only-get-login-log">Get Login Log</a></li>
            <li><a href="#admin-only-get-file-audit-log">Get File Audit Log</a></li>
            <li><a href="#admin-only-get-file-update-log">Get File Update Log</a></li>
            <li><a href="#admin-only-get-perm-audit-log">Get Permission Audit Log</a></li>
        </ul>
    </li>
    <li>
        <a href="#admin-only-organization">Organization</a>
        <ul>
            <li><a href="#admin-only-add-organization">Add Organization</a></li>
            <li><a href="#admin-only-add-organization-user">Add Organization User</a></li>
            <li><a href="#admin-only-get-organization-user-info">Get Organization User Info</a></li>
            <li><a href="#admin-only-update-organization-user-info">Update Organization User Info</a></li>
            <li><a href="#admin-only-delete-organization-user">Delete Organization User</a></li>
        </ul>
    </li>
    <li>
        <a href="#admin-only-department">Department</a>
        <ul>
            <li><a href="#admin-only-list-departments">List departments</a></li>
            <li><a href="#admin-only-list-departments-groups">List groups and members in a department</a></li>
            <li><a href="#admin-only-create-department">Create department</a></li>
            <li><a href="#admin-only-dismiss-department">Dismiss department</a></li>
        </ul>
    </li>
</ul>
</li>
</ul>
</div>
</p>

# <a id="seafile-web-api"></a>Seafile Web API

## <a id="api-basics"></a>API Basics

All API calls must be authenticated with a valid Seafile API key.

    curl -H 'Authorization: Token 24fd3c026886e3121b2ca630805ed425c272cb96' https://cloud.seafile.com/api2/auth/ping/

The api key can be retrieved by the obtain auth api. See the <a href="#quick-start">Quick Start</a> for details.

For each API, we provide `curl` examples to illustrate the usage. We also provide `python` and `javascript` examples, please refer to https://github.com/haiwen/webapi-examples for details.

## <a id="status-code"></a>Status Code

- 200: OK
- 201: CREATED
- 202: ACCEPTED
- 301: MOVED_PERMANENTLY
- 400: BAD_REQUEST
- 403: FORBIDDEN
- 404: NOT_FOUND
- 409: CONFLICT
- 429: TOO_MANY_REQUESTS
- 440: REPO_PASSWD_REQUIRED
- 441: REPO_PASSWD_MAGIC_REQUIRED
- 500: INTERNAL_SERVER_ERROR
- 520: OPERATION_FAILED

## <a id="quick-start"></a>Quick Start

**ping**

    curl https://cloud.seafile.com/api2/ping/

    "pong"

**obtain auth token**

    curl -d "username=username@example.com&password=123456" https://cloud.seafile.com/api2/auth-token/

    {"token": "24fd3c026886e3121b2ca630805ed425c272cb96"}


you should use `--data-urlencode` if you want to process some special characters properly.

    curl --data-urlencode username=user+name@example.com -d password=123456 https://cloud.seafile.com/api2/auth-token/

    {"token":"265757b0a5aaf5d6b2e266d0c21791121ce6cdec"}

**auth ping**

    curl -H 'Authorization: Token 24fd3c026886e3121b2ca630805ed425c272cb96' https://cloud.seafile.com/api2/auth/ping/

    "pong"

## <a id="account"></a>Account

### <a id="check-account-info"></a>Check Account Info

**GET** https://cloud.seafile.com/api2/account/info/

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/account/info/

**Sample response**

    {
    "usage": 26038531,
    "total": 104857600,
    "email": "user@example.com"
    }

**Errors**

* 403 Invalid token

### <a id="client-login"></a>Get Client Login URL

**GET** https://cloud.seafile.com/api2/client-login/

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" https://cloud.seafile.com/api2/client-login/

**Sample response**

*Note*:

- If the user has two way authentication enabled, the server will respond with an empty JSON object (`{}`).

```
"https://cloud.seafile.com/client-login/?token=000f1f83d612836c65fed087fb9c4ca40852d0f9"
```

**Errors**

* 403 Invalid token

### <a id="server-info"></a>Get Server Information

**GET** https://cloud.seafile.com/api2/server-info

*Note*:

- No authentication required.
- Added in seafile community edition server `4.0.5` or pro edition server `4.0.3`

**Sample request**

    curl https://cloud.seafile.com/api2/server-info/

**Sample response**

Sample response from a seafile community edition server:

    {
        "version": "4.0.6",
        "features": [
        "seafile-basic",
        ]
    }

Sample response from a seafile pro edition server:

    {
        "version": "4.0.6",
        "features": [
        "seafile-basic",
        "seafile-pro",
        "office-preview",
        "file-search"
        ]
    }

## <a id="starred-files"></a>Starred Files

### <a id="list-starred-files"></a>List starred files

**GET** https://cloud.seafile.com/api2/starredfiles/


**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e6199b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/starredfiles/

**Sample response**

    [
    {
        "repo": "99b758e6-91ab-4265-b705-925367374cf0",
        "mtime": 1355198150,
        "org": -1,
        "path": "/foo/bar.doc",
        "dir": false,
        "size": 0
    },
    {
        "repo": "99b758e6-91ab-4265-b705-925367374cf0",
        "mtime": 1353751237,
        "org": -1,
        "path": "/add_folder-blue.png",
        "dir": false,
        "size": 3170
    }
    ]

### <a id="star-a-file"></a>Star A File

**POST** https://cloud.seafile.com/api2/starredfiles/

**Request parameters**

* repo_id (post)
* p (post)

**Sample request**

    curl -v -d "repo_id=dae8cecc-2359-4d33-aa42-01b7846c4b32&p=/foo.md" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/starredfiles/

**Sample response**

    ...
    < HTTP/1.0 201 CREATED
    < Location: https://cloud.seafile.com/api2/starredfiles/
    ...
    "success"

**Success**

   Response code is 201(Created) and Location header provides url of starred file list.

**Errors**

* 400 `repo_id` or `p` is missing, or `p` is not valid file path(e.g. /foo/bar/).

### <a id="unstar-a-file"></a>Unstar A File

**DELETE** https://cloud.seafile.com/api2/starredfiles/

**Request parameters**

* repo_id
* p

**Sample request**

    curl -X DELETE -v  -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' 'https://cloud.seafile.com/api2/starredfiles/?repo_id=dae8cecc-2359-4d33-aa42-01b7846c4b32&p=/foo.md'

**Sample response**

    ...
    < HTTP/1.0 200 OK
    ...
    "success"

**Success**

   Response code is 200(OK), and a string named "success" is returned.

**Errors**

* 400 `repo_id` or `p` is missing, or `p` is not valid file path(e.g. /foo/bar/).

## <a id="group"></a>Group

### <a id="list-groups"></a>List Groups

**GET** https://cloud.seafile.com/api2/groups/


**Sample request**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/groups/"

**Sample response**

    {
        "replynum": 0,
        "groups": [
            {
                "ctime": 1398134171327948,
                "creator": "user@example.com",
                "msgnum": 0,
                "mtime": 1398231100,
                "id": 1,
                "name": "lian"
            },
            {
                "ctime": 1398236081042441,
                "creator": "user@example.com",
                "msgnum": 0,
                "mtime": 0,
                "id": 2,
                "name": "123"
            }
        ]
    }

### <a id="add-a-group"></a>Add a Group

**POST** https://cloud.seafile.com/api/v2.1/groups/

**Request parameters**

* name (name of new group)

**Sample request**

```
curl -d "name=new_group_name" -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/
```

**Sample response**

```
{
    "name": "new_group_name",
    "owner": "lian@lian.com",
    "created_at": "2015-12-17T10:29:57+0800",
    "admins": ["lian@lian.com"],
    "avatar_url": "https://cloud.seafile.com/media/avatars/groups/default.png",
    "id": 773
}
```

### <a id="get-info-of-a-group"></a>Get Info of a Group

**GET** https://cloud.seafile.com/api/v2.1/groups/772/

**Request parameters**

* avatar_size
* with_repos (0 or 1, if return library info of group. default 0 not return)

**Sample request**

```
curl -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/772/
```

**Sample response**

```
{
    "name": "rename_group_name",
    "owner": "lian@lian.com",
    "created_at": "2015-12-17T10:29:57+0800",
    "admins": ["lian@lian.com"],
    "avatar_url": "https://cloud.seafile.com/media/avatars/groups/default.png",
    "id": 772
}
```

### <a id="rename-a-group"></a>Rename a Group

**PUT** https://cloud.seafile.com/api/v2.1/groups/772/

**Request parameters**

* name (name of new group)

**Sample request**

```
curl -X PUT -d "name=rename_group_name" -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/772/
```

**Sample response**

```
{
    "name": "rename_group_name",
    "owner": "lian@lian.com",
    "created_at": "2015-12-17T10:29:57+0800",
    "admins": ["lian@lian.com"],
    "avatar_url": "https://cloud.seafile.com/media/avatars/groups/default.png",
    "id": 772
}
```

### <a id="transfer-a-group"></a> Transfer a Group

**PUT** https://cloud.seafile.com/api/v2.1/groups/772/

**Request parameters**

* owner (new owner of this group, should be an email.)

**Sample request**

```
curl -X PUT -d "owner=new_owner@new_owner.com" -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/772/
```

**Sample response**

```
{
    "name": "rename_group_name",
    "owner": "new_owner@new_owner.com",
    "created_at": "2015-12-17T10:29:57+0800",
    "admins": ["lian@lian.com", "new_owner@new_owner.com"],
    "avatar_url": "https://cloud.seafile.com/media/avatars/groups/default.png",
    "id": 772
}
```

### <a id="delete-a-group"></a> Delete a Group

**DELETE** https://cloud.seafile.com/api/v2.1/groups/772/

**Sample request**

```
curl -X DELETE -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/772/
```

**Sample response**

```
{"success":true}
```

### <a id="quit-group"></a> Quit Group

**DELETE** https://cloud.seafile.com/api/v2.1/groups/770/members/myself@email.com/

**Sample request**

```
curl -X DELETE -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/770/members/myself@email.com/
```

**Sample response**

```
{"success":true}
```

### <a id="group-member"></a>Group Member

#### <a id="list-group-members"></a>List All Group Members

**GET** https://cloud.seafile.com/api/v2.1/groups/770/members/

**Request parameters**

* avatar_size
* is_admin (`true` or `false`, if ONLY return admin members of group. default `false` return all members)

**Sample request**

```
curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api/v2.1/groups/770/members/"
```

**Sample response**

```
[
    {
        "login_id": "",
        "name": "nickname-of-lian",
        "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
        "is_admin": true,
        "contact_email": "lian_contact@email.com",
        "email": "lian@lian.com"
    },
    {
        "login_id": "",
        "name": "1",
        "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
        "is_admin": false,
        "contact_email": "1@1.com",
        "email": "1@1.com"
    }
]
```

#### <a id="add-a-group-member"></a>Add a Group Member

**POST** https://cloud.seafile.com/api/v2.1/groups/770/members/

**Request parameters**

* email

**Sample request**

```
curl -d "email=new-member@email.com" -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/770/members/
```

**Sample response**

```
{
    "login_id": "",
    "name": "new-member",
    "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
    "is_admin": false,
    "contact_email": "new-member@email.com",
    "email": "new-member@email.com"
}
```

#### <a id="bulk-add-group-members"></a>Bulk Add Group Members

**POST** https://cloud.seafile.com/api/v2.1/groups/770/members/bulk/

**Request parameters**

* emails

**Sample request**

```
curl -d "emails=new-member-1@email.com,new-member-2@email.com,new-member-3@email.com" -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/770/members/bulk/
```

**Sample response**

```
{
    "failed":[
        {
            "error_msg": "Invalid email",
            "email": "new-member-3@email.com"
        },
        {
            "error_msg": "Is already group member",
            "email": "new-member-4@email.com"
        }
    "success":[
        {
            "login_id": "",
            "name": "new-member-1",
            "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
            "is_admin": false,
            "contact_email": "new-member-1@email.com",
            "email": "new-member-1@email.com"
        },
        {
            "login_id": "",
            "name": "new-member-2",
            "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
            "is_admin": false,
            "contact_email": "new-member-2@email.com",
            "email": "new-member-2@email.com"
        }
    ]
}
```

#### <a id="get-info-of-a-group-member"></a>Get Info of a Group Member

**GET** https://cloud.seafile.com/api/v2.1/groups/770/members/group-member@email.com/

**Sample request**

```
curl -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/770/members/group-member@email.com/
```

**Request parameters**

* avatar_size

**Sample response**

```
{
    "login_id": "",
    "name": "group-member",
    "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
    "is_admin": false,
    "contact_email": "group-member@email.com",
    "email": "group-member@email.com"
}
```

#### <a id="set-a-group-member-admin"></a>Set a Group Member Admin

**PUT** https://cloud.seafile.com/api/v2.1/groups/770/members/group-member@email.com/

**Request parameters**

* is_admin=true

**Sample request**

```
curl -X PUT -d "is_admin=true" -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/770/members/group-member@email.com/
```

**Sample response**

```
{
    "login_id": "",
    "name": "group-member",
    "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
    "is_admin": true,
    "contact_email": "group-member@email.com",
    "email": "group-member@email.com"
}
```

#### <a id="unset-a-group-member-admin"></a>Unset a Group Member Admin

**PUT** https://cloud.seafile.com/api/v2.1/groups/770/members/group-member@email.com/

**Request parameters**

* is_admin=false

**Sample request**

```
curl -X PUT -d "is_admin=false" -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/770/members/group-member@email.com/
```

**Sample response**

```
{
    "login_id": "",
    "name": "group-member",
    "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
    "is_admin": false,
    "contact_email": "group-member@email.com",
    "email": "group-member@email.com"
}
```

#### <a id="delete-a-group-member"></a> Delete a Group Member

**DELETE** https://cloud.seafile.com/api/v2.1/groups/770/members/group-member@email.com/

**Sample request**

```
curl -X DELETE -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/770/members/group-member@email.com/
```

**Sample response**

```
{"success":true}
```

### <a id="group-message"></a>Group Message

#### <a id="get-group-messages"></a>Get Group Messages

**GET** https://cloud.seafile.com/api2/groups/{group_id}/discussions/

**Request parameters**

* group_id
* page (default 1)
* per_page (default 20)
* avatar_size (default 80)

**Sample request**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/groups/772/discussions/"

**Sample response**

```
{'current_page': 1,
 'msgs': [{'avatar_url': 'https://cloud.seafile.com/media/avatars/default.png',
           'content': u'test',
           'created_at': '2016-07-11T09:18:20+08:00',
           'group_id': 772,
           'id': 1,
           'user_email': u'lian@lian.com',
           'user_login_id': '',
           'user_name': u'name-of-lian'}],
 'page_num': 1}
```

#### <a id="send-a-group-message"></a>Send A Group Message

**POST** https://cloud.seafile.com/api2/groups/{group_id}/discussions/

**Request parameters**

* group_id
* content
* avatar_size (default 80)

**Sample request**

    curl -d "content=this is another test" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/groups/772/discussions/"

**Sample response**

```
{'avatar_url': 'https://cloud.seafile.com/media/avatars/default.png',
 'content': u'this is another test',
 'created_at': '2016-07-11T09:27:49+08:00',
 'group_id': 772,
 'id': 3,
 'user_email': u'lian@lian.com',
 'user_login_id': '',
 'user_name': u'name-of-lian'}
```

#### <a id="delete-a-group-message"></a>Delete A Group Message

**DELETE** https://cloud.seafile.com/api2/groups/772/discussions/3/

**Request parameters**

* group_id
* discuss_id

**Sample request**

    curl -v -X DELETE -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/groups/772/discussions/3/"

**sample response**

```
...
< http/1.0 204 no content
...
```

**Errors**

* 400 Discussion id not found.
* 403 Permission denied.

### <a id="group-owned-libraries"></a>Group Owned Libraries

#### <a id="add-group-owned-library"></a>Add Group Owned Library

**POST** http://192.168.1.113:8000/api/v2.1/groups/{group_id}/group-owned-libraries/

**Request parameters**

* `group_id`
* `repo_name`
* `password`
* `permission`, default `rw`.

**Sample request**

```
curl -d "repo_name=group-owned-repo-4&permission=r" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "http://192.168.1.113:8000/api/v2.1/groups/53/group-owned-libraries/"
```

**sample response**

```
{
    "repo_id": "9bc59af9-265e-4110-a0e2-619450a5cb35",
    "permission": "r",
    "encrypted": false,
    "owner_email": "53@seafile_group",
    "mtime": "2018-04-23T17:25:37+08:00",
    "repo_name": "group-owned-repo-4",
    "size": 0
}
```

**Errors**

* 400 repo_name/permission invalid.
* 403 NOT allow to create encrypted library..
* 403 Permission denied.
* 403 No group quota.
* 404 Group not found.

#### <a id="delete-group-owned-library"></a>Delete Group Owned Library

**DELETE** http://192.168.1.113:8000/api/v2.1/groups/{group_id}/group-owned-libraries/{repo_id}/

**Request parameters**

* `group_id`
* `repo_id`

**Sample request**

```
curl -X DELETE -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "http://192.168.1.113:8000/api/v2.1/groups/53/group-owned-libraries/9bc59af9-265e-4110-a0e2-619450a5cb35/"
```

**sample response**

```
{"success":true}
```

**Errors**

* 403 Permission denied.
* 404 Group/Library not found.
* 500 Internal Server Error

#### <a id="get-group-owned-library-user-share-info"></a>Get Group Owned Library User Share Info

**GET** http://192.168.1.113:8000/api/v2.1/group-owned-libraries/{repo_id}/user-share/

**Request parameters**

* `repo_id`

**Sample request**

```
curl -H 'Authorization: Token 5eba8c2f983404e33b140b13a1d050b9a4440e03' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.113:8000/api/v2.1/group-owned-libraries/4902dcc7-29be-4020-81e9-4e512f97db1e/user-share/"
```

**sample response**

```
[
    {
        "permission": "rw",
        "user_name": "1",
        "user_email": "1@1.com",
        "user_contact_email": "1@1.com"
    },
    {
        "permission": "rw",
        "user_name": "1",
        "user_email": "1@111.com",
        "user_contact_email": "1@111.com"
    },
    {
        "permission": "rw",
        "user_name": "10",
        "user_email": "10@10.com",
        "user_contact_email": "10@10.com"
    }
]
```

**Errors**

* 403 Permission denied.
* 404 Group/Library not found.

#### <a id="share-group-owned-library-to-user"></a>Share Group Owned Library to User

**POST** http://192.168.1.113:8000/api/v2.1/group-owned-libraries/{repo_id}/user-share/

**Request parameters**

* `repo_id`
* `permission`, `r` or `rw`.
* `username`

**Sample request**

```
curl -d "permission=r&username=1@1.com&username=2@1.com" -H 'Authorization: Token 5eba8c2f983404e33b140b13a1d050b9a4440e03' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.113:8000/api/v2.1/group-owned-libraries/4902dcc7-29be-4020-81e9-4e512f97db1e/user-share/"
```

**sample response**

```
{
    "failed": [
        {
            "email": "2@1.com",
            "error_msg": "User 2@1.com not found."
        }
    ],
    "success": [
        {
            "permission": "r",
            "user_name": "1",
            "user_email": "1@1.com",
            "user_contact_email": "1@1.com"
        }
    ]
}
```

**Errors**

* 400 permission invalid.
* 403 Permission denied.
* 404 Group/Library not found.

#### <a id="modify-group-owned-library-user-share-permission"></a>Modify Group Owned Library User Share Permission

**PUT** http://192.168.1.113:8000/api/v2.1/group-owned-libraries/{repo_id}/user-share/

**Request parameters**

* `repo_id`
* `permission`, `r` or `rw`.
* `username`

**Sample request**

```
curl -X PUT -d "permission=rw&username=1@1.com" -H 'Authorization: Token 5eba8c2f983404e33b140b13a1d050b9a4440e03' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.113:8000/api/v2.1/group-owned-libraries/4902dcc7-29be-4020-81e9-4e512f97db1e/user-share/"
```

**sample response**

```
{
    "success": true
}
```

**Errors**

* 400 permission invalid.
* 403 Permission denied.
* 404 Group/Library not found.

#### <a id="delete-group-owned-library-user-share"></a>Delete Group Owned Library User Share

**DELETE** http://192.168.1.113:8000/api/v2.1/group-owned-libraries/{repo_id}/user-share/

**Request parameters**

* `repo_id`
* `username`

**Sample request**

```
curl -X DELETE -d "username=1@1.com" -H 'Authorization: Token 5eba8c2f983404e33b140b13a1d050b9a4440e03' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.113:8000/api/v2.1/group-owned-libraries/4902dcc7-29be-4020-81e9-4e512f97db1e/user-share/"
```

**sample response**

```
{
    "success": true
}
```

**Errors**

* 403 Permission denied.
* 404 Group/Library not found.

#### <a id="get-group-owned-library-group-share-info"></a>Get Group Owned Library Group Share Info

**GET** http://192.168.1.113:8000/api/v2.1/group-owned-libraries/{repo_id}/group-share/

**Request parameters**

* `repo_id`

**Sample request**

```
curl -H 'Authorization: Token 5eba8c2f983404e33b140b13a1d050b9a4440e03' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.113:8000/api/v2.1/group-owned-libraries/4902dcc7-29be-4020-81e9-4e512f97db1e/group-share/"
```

**sample response**

```
[
    {
        "permission": "r",
        "group_id": 71,
        "group_name": "asd"
    },
    {
        "permission": "r",
        "group_id": 70,
        "group_name": "group-of-lian"
    }
]
```

**Errors**

* 403 Permission denied.
* 404 Group/Library not found.

#### <a id="share-group-owned-library-to-group"></a>Share Group Owned Library to Group

**POST** http://192.168.1.113:8000/api/v2.1/group-owned-libraries/{repo_id}/group-share/

**Request parameters**

* `repo_id`
* `permission`, `r` or `rw`.
* `group_id`

**Sample request**

```
curl -d "permission=r&group_id=89&group_id=71&group_id=70" -H 'Authorization: Token 5eba8c2f983404e33b140b13a1d050b9a4440e03' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.113:8000/api/v2.1/group-owned-libraries/4902dcc7-29be-4020-81e9-4e512f97db1e/group-share/"
```

**sample response**

```
{
    "failed": [
        {
            "error_msg": "Group 89 not found"
        },
        {
            "error_msg": "This item has been shared to asd.",
            "group_name": "asd"
        }
    ],
    "success": [
        {
            "permission": "r",
            "group_id": 70,
            "group_name": "group-of-lian"
        }
    ]
}
```

**Errors**

* 400 permission invalid.
* 403 Permission denied.
* 404 Group/Library not found.

#### <a id="modify-group-owned-library-group-share-permission"></a>Modify Group Owned Library Group Share Permission

**PUT** http://192.168.1.113:8000/api/v2.1/group-owned-libraries/{repo_id}/group-share/

**Request parameters**

* `repo_id`
* `permission`, `r` or `rw`.
* `group_id`

**Sample request**

```
curl -X PUT -d "permission=rw&group_id=70" -H 'Authorization: Token 5eba8c2f983404e33b140b13a1d050b9a4440e03' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.113:8000/api/v2.1/group-owned-libraries/4902dcc7-29be-4020-81e9-4e512f97db1e/group-share/"
```

**sample response**

```
{
    "success": true
}
```

**Errors**

* 400 permission invalid.
* 403 Permission denied.
* 404 Group/Library not found.

#### <a id="delete-group-owned-library-group-share"></a>Delete Group Owned Library Group Share

**DELETE** http://192.168.1.113:8000/api/v2.1/group-owned-libraries/{repo_id}/group-share/

**Request parameters**

* `repo_id`
* `group_id`

**Sample request**

```
curl -X DELETE -d "group_id=71" -H 'Authorization: Token 5eba8c2f983404e33b140b13a1d050b9a4440e03' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.113:8000/api/v2.1/group-owned-libraries/4902dcc7-29be-4020-81e9-4e512f97db1e/group-share/"
```

**sample response**

```
{
    "success": true
}
```

**Errors**

* 403 Permission denied.
* 404 Group/Library not found.

#### <a id="modify-group-owned-library-sub-folder-permission"></a>Modify Group Owned Library Sub-Folder Permission

**PUT** http://192.168.1.113:8000/api/v2.1/groups/{group_id}/group-owned-libraries/{repo_id}/

**Request parameters**

* `group_id`
* `repo_id`
* `path`, path of sub folder.
* `permission`: `r` or `rw`.

**Sample request**

```
curl -X PUT -d "path=/tmp/&permission=r" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "http://192.168.1.113:8000/api/v2.1/groups/53/group-owned-libraries/9bc59af9-265e-4110-a0e2-619450a5cb35/"
```

**sample response**

```
{"success":true}
```

**Errors**

* 400 path/permission invalid.
* 403 Permission denied.
* 404 Group/Library/Folder not found.
* 500 Internal Server Error

## <a id="share"></a>Share

### <a id="share-link"></a>File Share Link

#### <a id="list-all-share-links"></a>List all Share Links

This api will list all folder/file download share links in all libraries created by user.

**GET** https://cloud.seafile.com/api/v2.1/share-links/

**Sample request**

    curl -H 'Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a' -H 'Accept: application/json; charset=utf-8; indent=4' "https://cloud.seafile.com/api/v2.1/share-links/"

**Sample response**
```
[
    {
        "username": "lian@lian.com",
        "repo_id": "c474a093-19dc-4ddf-b0b0-72b33214ba33",
        "ctime": "2017-04-01T02:35:57+00:00",
        "expire_date": "",
        "token": "6afa667ff2c248378b70",
        "view_cnt": 0,
        "link": "https://cloud.seafile.com/d/6afa667ff2c248378b70/",
        "obj_name": "/",
        "path": "/",
        "is_dir": true,
        "is_expired": false,
        "repo_name": "seacloud.cc.124"
    },
    {
        "username": "lian@lian.com",
        "repo_id": "104f6537-b3a5-4d42-b8b5-8e47e494e4cf",
        "ctime": "2017-04-01T02:35:29+00:00",
        "expire_date": "",
        "token": "0c4eb0cb104a43caaeef",
        "view_cnt": 0,
        "link": "https://cloud.seafile.com/d/0c4eb0cb104a43caaeef/",
        "obj_name": "folder",
        "path": "/folder/",
        "is_dir": true,
        "is_expired": false,
        "repo_name": "for-test-web-api"
    },
    {
        "username": "lian@lian.com",
        "repo_id": "104f6537-b3a5-4d42-b8b5-8e47e494e4cf",
        "ctime": "2017-04-01T02:35:35+00:00",
        "expire_date": "",
        "token": "8c05a00c44db4764b3a5",
        "view_cnt": 0,
        "link": "https://cloud.seafile.com/f/8c05a00c44db4764b3a5/",
        "obj_name": "tmp.md",
        "path": "/tmp.md",
        "is_dir": false,
        "is_expired": false,
        "repo_name": "for-test-web-api"
    }
]
```

**Errors**

* 403 Permission denied.
* 500 Internal Server Error

#### <a id="list-share-links-of-a-library"></a>List Share Links of a Library

This api will list all folder/file download share links in a specific library.

**GET** https://cloud.seafile.com/api/v2.1/share-links/?repo_id={repo_id}

**Request parameters**

* repo-id

**Sample request**

    curl -H 'Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a' -H 'Accept: application/json; charset=utf-8; indent=4' "https://cloud.seafile.com/api/v2.1/share-links/?repo_id=104f6537-b3a5-4d42-b8b5-8e47e494e4cf"

**Sample response**
```
[
    {
        "username": "lian@lian.com",
        "repo_id": "104f6537-b3a5-4d42-b8b5-8e47e494e4cf",
        "ctime": "2017-04-01T02:35:29+00:00",
        "expire_date": "",
        "token": "0c4eb0cb104a43caaeef",
        "view_cnt": 0,
        "link": "https://cloud.seafile.com/d/0c4eb0cb104a43caaeef/",
        "obj_name": "folder",
        "path": "/folder/",
        "is_dir": true,
        "is_expired": false,
        "repo_name": "for-test-web-api"
    },
    {
        "username": "lian@lian.com",
        "repo_id": "104f6537-b3a5-4d42-b8b5-8e47e494e4cf",
        "ctime": "2017-04-01T02:35:35+00:00",
        "expire_date": "",
        "token": "8c05a00c44db4764b3a5",
        "view_cnt": 0,
        "link": "https://cloud.seafile.com/f/8c05a00c44db4764b3a5/",
        "obj_name": "tmp.md",
        "path": "/tmp.md",
        "is_dir": false,
        "is_expired": false,
        "repo_name": "for-test-web-api"
    }
]
```

**Errors**

* 403 Permission denied.
* 404 library not found.
* 500 Internal Server Error

#### <a id="list-share-link-of-a-folder-file"></a>List Share Link of a Folder(File)

This api will list download share link info of a specific folder/file.

**GET** https://cloud.seafile.com/api/v2.1/share-links/?repo_id={rpeo_id}&path={path}

**Request parameters**

* repo-id
* path, could be path of a foler or a file.

**Sample request**

Get folder download share link.

    curl -H 'Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a' -H 'Accept: application/json; charset=utf-8; indent=4' "https://cloud.seafile.com/api/v2.1/share-links/?repo_id=104f6537-b3a5-4d42-b8b5-8e47e494e4cf&path=/folder/"

**Sample response**
```
[
    {
        "username": "lian@lian.com",
        "repo_id": "104f6537-b3a5-4d42-b8b5-8e47e494e4cf",
        "ctime": "2017-04-01T02:35:29+00:00",
        "expire_date": "",
        "token": "0c4eb0cb104a43caaeef",
        "view_cnt": 0,
        "link": "https://cloud.seafile.com/d/0c4eb0cb104a43caaeef/",
        "obj_name": "folder",
        "path": "/folder/",
        "is_dir": true,
        "is_expired": false,
        "repo_name": "for-test-web-api"
    }
]
```

or a empty list `[]` if this folder has no download share link.

Get file download share link.

    curl -H 'Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a' -H 'Accept: application/json; charset=utf-8; indent=4' "https://cloud.seafile.com/api/v2.1/share-links/?repo_id=104f6537-b3a5-4d42-b8b5-8e47e494e4cf&path=/tmp.md"

**Sample response**
```
[
    {
        "username": "lian@lian.com",
        "repo_id": "104f6537-b3a5-4d42-b8b5-8e47e494e4cf",
        "ctime": "2017-04-01T02:35:35+00:00",
        "expire_date": "",
        "token": "8c05a00c44db4764b3a5",
        "view_cnt": 0,
        "link": "https://cloud.seafile.com/f/8c05a00c44db4764b3a5/",
        "obj_name": "tmp.md",
        "path": "/tmp.md",
        "is_dir": false,
        "is_expired": false,
        "repo_name": "for-test-web-api"
    }
]
```

or a empty list `[]` if this file has no download share link.

**Errors**

* 403 Permission denied.
* 404 folder/library not found.
* 500 Internal Server Error

#### <a id="create-share-link"></a>Create Share Link

**POST** https://cloud.seafile.com/api/v2.1/share-links/

**Request parameters**

* repo-id
* path (file/folder path)
* password (not necessary)
* expire_days (not necessary)

**Sample request**

Create download link for file

    curl -d "path=/foo.md&repo_id=62ca6cf9-dab6-47e5-badc-bab13d9220ce" -H 'Authorization: Token ef12bf1e66a1aa797a1d6556fdc9ae84f1e9249f' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/share-links/

Create download link for directory with password and expire date

    curl -d "path=/bar/&repo_id=62ca6cf9-dab6-47e5-badc-bab13d9220ce&password=password&expire_days=6" -H 'Authorization: Token ef12bf1e66a1aa797a1d6556fdc9ae84f1e9249f' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/share-links/

**Sample response**

```
{
    "username": "lian@lian.com",
    "view_cnt": 0,
    "ctime": "2016-03-04T04:06:35.477",
    "token": "409f5aa54a",
    "repo_id": "62ca6cf9-dab6-47e5-badc-bab13d9220ce",
    "link": "https://cloud.seafile.com/f/409f5aa54a/",
    "expire_date": null,
    "path": "/foo.md",
    "is_expired": false
}
```

```
{
    "username": "lian@lian.com",
    "view_cnt": 0,
    "ctime": "2016-03-04T04:12:48.959",
    "token": "db1a50e686",
    "repo_id": "62ca6cf9-dab6-47e5-badc-bab13d9220ce",
    "link": "https://cloud.seafile.com/d/db1a50e686/",
    "expire_date": null,
    "path": "/bar/",
    "is_expired": false
}
```

**Errors**

* 400 path/repo_id invalid
* 403 Permission denied.
* 404 file/folder/library not found.
* 500 Internal Server Error

#### <a id="delete-share-link"></a>Delete Share Link

**DELETE** https://cloud.seafile.com/api/v2.1/share-links/{token}/

**Sample request**

    curl -X DELETE -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api/v2.1/share-links/0ae587a7d1/"

**Sample response**

    {"success":true}

#### <a id="send-share-link-email"></a>Send Share Link Email

**POST** https://cloud.seafile.com/api2/send-share-link/

**Request parameters**

* token
* email
* extra_msg (not necessary)

**Sample request**

    curl -d "email=sample@eamil.com,invalid-email&token=4cbd625c5e" -H 'Authorization: Token ef12bf1e66a1aa797a1d6556fdc9ae84f1e9249f' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/send-share-link/

**Sample response**

```
{
    "failed": [
        {
            "email": "invalid-email",
            "error_msg": "email invalid."
        }
    ],
    "success": [
        "sample@eamil.com"
    ]
}
```

**Errors**

* 400 token/repo_id invalid
* 403 Permission denied.
* 403 Sending shared link failed. Email service is not properly configured, please contact administrator.
* 404 token/library not found

#### <a id="list-direntry-in-dir-download-link"></a>List Direntry in Dir Download Link

**GET** https://cloud.seafile.com/api2/d/{token}/dir/

**Request parameters**

* token (upload link token)
* p (sub folder path)
* password (if link is encrypted)

**Sample request**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/d/3af7c46595/dir/?p=/subfolder/"

**Sample response**

    [{"mtime": 1436846750, "type": "dir", "name": "sadof", "id": "1806dbdb700b7bcd49e6275107c7ccf7b3ea1776"}, {"id": "bdb06f6de972c42893fda590ac954988b562429c", "mtime": 1436431020, "type": "file", "name": "test.mdert", "size": 20}]

### <a id="upload-link"></a>Upload Link

#### <a id="list-upload-links"></a>List Upload Links

**GET** https://cloud.seafile.com/api/v2.1/upload-links/

**Sample request**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api/v2.1/upload-links/"

**Sample response**

    [{"username":"lian@lian.com","repo_id":"62ca6cf9-dab6-47e5-badc-bab13d9220ce","ctime":"2016-03-03T15:26:15.223","token":"9a5d5c8391","link":"https://cloud.seafile.com/u/d/9a5d5c8391/","path":"/"},{"username":"lian@lian.com","repo_id":"78c620ee-2989-4427-8eff-7748f4fbebc0","ctime":"2016-03-04T05:37:17.968","token":"d17d87ea4d","link":"https://cloud.seafile.com/u/d/d17d87ea4d/","path":"/yutong/"}]

#### <a id="create-upload-link"></a>Create Upload Link

**POST** https://cloud.seafile.com/api/v2.1/upload-links/

**Request parameters**

* repo-id
* path (file/folder path)
* password (not necessary)

**Sample request**

Create upload link for directory with password

    curl -d "path=/bar/&repo_id=afc3b694-7d4c-4b8a-86a4-89c9f3261b12&password=password" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/upload-links/

**Sample response**

```
{
    "username": "lian@lian.com",
    "repo_id": "62ca6cf9-dab6-47e5-badc-bab13d9220ce",
    "ctime": "2016-03-04T05:51:34.022",
    "token": "dce40e8594",
    "link": "https://cloud.seafile.com/u/d/dce40e8594/",
    "path": "/bar/"
}
```

**Errors**

* 400 path/repo_id invalid
* 403 Permission denied.
* 500 Internal Server Error

#### <a id="delete-upload-link"></a>Delete Upload Link

**DELETE** https://cloud.seafile.com/api/v2.1/upload-links/{token}/

**Sample request**

    curl -X DELETE -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api/v2.1/upload-links/0ae587a7d1/"

**Sample response**

    {"success":true}

#### <a id="send-upload-link-email"></a>Send Upload Link Email

**POST** https://cloud.seafile.com/api2/send-upload-link/

**Request parameters**

* token
* email
* extra_msg (not necessary)

**Sample request**

    curl -d "email=sample@eamil.com,invalid-email&token=4cbd625c5e" -H 'Authorization: Token ef12bf1e66a1aa797a1d6556fdc9ae84f1e9249f' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/send-upload-link/

**Sample response**

```
{
    "failed": [
        {
            "email": "invalid-email",
            "error_msg": "email invalid."
        }
    ],
    "success": [
        "sample@eamil.com"
    ]
}
```
* 400 token/repo_id invalid
* 403 Permission denied.
* 403 Sending shared link failed. Email service is not properly configured, please contact administrator.
* 404 token/library not found

### <a id="shared-libraries"></a>Shared Libraries

#### <a id="list-user-shared-libraries"></a>List User Shared Libraries

**GET** https://cloud.seafile.com/api2/repos/7460f7ac-a0ff-4585-8906-bb5a57d2e118/dir/shared_items/?p=/&share_type=user

**Request parameters**

* p, `/` means the **root** folder, which is equivalent to the library.
* share_type, `user`

**Sample request**

    curl -v -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/7460f7ac-a0ff-4585-8906-bb5a57d2e118/dir/shared_items/?p=/&share_type=user

**Sample response**

```
[
    {"user_info": {"nickname": "5", "name": "5@1.com"}, "share_type": "user", "permission": "r"},
    {"user_info": {"nickname": "name of 4", "name": "4@1.com"}, "share_type": "user", "permission": "r"}
]
```

**Errors**

* 400 share_type invalid.
* 403 Permission denied.
* 404 Library not found.

#### <a id="list-group-shared-libraries"></a>List Group Shared Libraries

**GET** https://cloud.seafile.com/api2/repos/7460f7ac-a0ff-4585-8906-bb5a57d2e118/dir/shared_items/?p=/&share_type=group

**Request parameters**

* p, `/` means the **root** folder, which is equivalent to the library.
* share_type, `group`

**Sample request**

    curl -v -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/7460f7ac-a0ff-4585-8906-bb5a57d2e118/dir/shared_items/?p=/&share_type=group

**Sample response**

```
[
    {"group_info": {"id": 65, "name": "group"}, "share_type": "group", "permission": "r"},
    {"group_info": {"id": 395, "name": "lsd"}, "share_type": "group", "permission": "rw"}
]
```

**Errors**

* 400 share_type invalid.
* 403 Permission denied.
* 404 Library not found.

#### <a id="list-be-shared-libraries"></a>List Be Shared Libraries

**GET** https://cloud.seafile.com/api2/beshared-repos/

**Sample request**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/beshared-repos/"

**Sample response**

    "[{"user": "user@example.com", "repo_id": "989e3952-9d6f-4427-ab16-4bf9b53212eb", "share_type": "personal", "permission": "rw", "encrypted": false, "repo_desc": "lib shared to imwhatiam", "enc_version": false, "last_modified": 1398218747, "is_virtual": false, "group_id": 0, "repo_name": "lib shared to imwhatiam"}]"

#### <a id="delete-be-shared-library"></a>Delete Be Shared Library

**DELETE** https://cloud.seafile.com/api2/beshared-repos/{repo_id}/?share_type=personal&from=from_user@name.com

**Sample request**

    curl -X DELETE -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/beshared-repos/{repo_id}/?share_type=personal&from=from_user@name.com

**Sample response**

    {"success": true}

**Errors**

* 400 Invalid argument
* 400 Library does not exist

#### <a id="share-a-library-to-user"></a>Share a Library to User

**PUT** https://cloud.seafile.com/api2/repos/{repo_id}/dir/shared_items/?p=/

**Request parameters**

* p, `/` means the **root** folder, which is equivalent to the library.
* share_type, `user`
* username, a email string or a list contains multi emails
* permission, `r`, `rw` or `admin`, default `r`.

**Sample request**

    curl -X PUT -d "share_type=user&username=4@1.com&username=5@1.com&username=invalid@email.com&permission=r" -H 'Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/7460f7ac-a0ff-4585-8906-bb5a57d2e118/dir/shared_items/?p=/

**Sample response**

```
{
    "failed": [
        {"email": "invalid@email.com", "error_msg": "User invalid@email.com not found."}
    ],
    "success": [
        {"user_info": {"nickname": "name of 4", "name": "4@1.com"}, "share_type": "user", "permission": "r"},
        {"user_info": {"nickname": "5", "name": "5@1.com"}, "share_type": "user", "permission": "r"}
    ]
}
```

**Errors**

* 400 permission invalid.
* 400 share_type invalid.
* 403 Permission denied.
* 404 Library not found.

#### <a id="unshare-a-library-from-user"></a>Unshare a Library from User

**DELETE** https://cloud.seafile.com/api2/repos/{repo_id}/dir/shared_items/?p=/&share_type=user&username=5@1.com

**Request parameters**

* p, `/` means the **root** folder, which is equivalent to the library.
* share_type, `user`
* username, a email string

**Sample request**

    curl -X DELETE -H 'Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a' -H 'Accept: application/json; charset=utf-8; indent=4' "https://cloud.seafile.com/api2/repos/7460f7ac-a0ff-4585-8906-bb5a57d2e118/dir/shared_items/?p=/&share_type=user&username=5@1.com"

**Sample response**

```
{"success": true}
```

**Errors**

* 400 share_type invalid.
* 400 email invalid.
* 403 Permission denied.
* 404 Library not found.

#### <a id="update-permission-of-user-shared-library"></a>Update Permission of User Shared Library

**POST** https://cloud.seafile.com/api2/repos/{repo_id}/dir/shared_items/?p=/&share_type=user&username=5@1.com

**Request parameters**

* p, `/` means the **root** folder, which is equivalent to the library.
* share_type, `user`
* username, a email string
* permisson, `r` or `rw`

**Sample request**

    curl -d "permission=r" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; indent=4' "https://cloud.seafile.com/api2/repos/2deffbac-d7be-4ace-b406-efb799083ee9/dir/shared_items/?p=/&share_type=user&username=5@1.com"

**Sample response**

```
{"success": true}
```

**Errors**

* 400 share_type invalid.
* 403 permission invalid.
* 403 Permission denied.
* 404 Library not found.
* 404 Folder not found.

#### <a id="share-a-library-to-group"></a>Share a Library to Group

**PUT** https://cloud.seafile.com/api2/repos/{repo_id}/dir/shared_items/?p=/

**Request parameters**

* p, `/` means the **root** folder, which is equivalent to the library.
* share_type, `group`
* group_id , an integer or a list contains multi integers
* permission, `r`, `rw` or `admin`, default `r`.

**Sample request**

    curl -X PUT -d "share_type=group&group_id=65&group_id=395&group_id=invalid_group_id&group_id=111&permission=rw" -H 'Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/7460f7ac-a0ff-4585-8906-bb5a57d2e118/dir/shared_items/?p=/

**Sample response**

```
{
    "failed": [],
    "success": [
        {"group_info": {"id": 65, "name": "group"}, "share_type": "group", "permission": "rw"},
        {"group_info": {"id": 395, "name": "lsd"}, "share_type": "group", "permission": "rw"}
    ]
}
```

**Errors**

* 400 permission invalid.
* 400 group_id invalid.
* 400 share_type invalid.
* 403 Permission denied.
* 404 Library not found.

#### <a id="unshare-a-library-from-group"></a>Unshare a Library from Group

**DELETE** https://cloud.seafile.com/api2/repos/{repo_id}/dir/shared_items/?p=/&share_type=group&group=65

**Request parameters**

* p, `/` means the **root** folder, which is equivalent to the library.
* share_type, `group`
* group_id , an integer

**Sample request**

    curl -X DELETE -H 'Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a' -H 'Accept: application/json; charset=utf-8; indent=4' "https://cloud.seafile.com/api2/repos/7460f7ac-a0ff-4585-8906-bb5a57d2e118/dir/shared_items/?p=/&share_type=group&group_id=65"

**Sample response**

```
{"success": true}
```

**Errors**

* 400 share_type invalid.
* 400 group_id invalid.
* 403 Permission denied.
* 404 Library not found.

#### <a id="update-permission-of-group-shared-library"></a>Update Permission of Group Shared Library

**POST** https://cloud.seafile.com/api2/repos/{repo_id}/dir/shared_items/?p=/&share_type=group&group_id=65

**Request parameters**

* p, `/` means the **root** folder, which is equivalent to the library.
* share_type, `group`
* group_id , an integer
* permisson, `r` or `rw`

**Sample request**

    curl -d "permission=r" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; indent=4' "https://cloud.seafile.com/api2/repos/2deffbac-d7be-4ace-b406-efb799083ee9/dir/shared_items/?p=/&share_type=group&group_id=65"

**Sample response**

```
{"success": true}
```

**Errors**

* 400 share_type invalid.
* 403 permission invalid.
* 403 Permission denied.
* 404 Library not found.

#### <a id="batch-share-libraries-to-user"></a>Batch Share Libraries to User

**POST** https://cloud.seafile.com/api/v2.1/repos/batch/

**Request parameters**

* operation, `share`
* share_type, `user`
* username, email of a user
* permission, default is `rw`
* repo_id

**Sample request**

    curl -d "operation=share&share_type=user&username=2@org.com&repo_id=b6cfa05d-07af-422b-924e-45202dc1cbb5&repo_id=48aa475d-deb0-40f0-ab9b-22ec84989a58" -H 'Authorization: Token 40c89d06a2beeec672d091156de4cc163c6aa31a' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api/v2.1/repos/batch/

**Sample response**

```
{
    "failed": [
        {"repo_id": "3761ade3-100b-4c3b-9508-79b3a510e6f6", "error_msg": "This item has been shared to 1@1.com."}
    ],
    "success": [
        {"username": "1@1.com", "repo_id": "f820bd12-0511-4542-b14b-3e48d8efc294", "permission": "rw"}
    ]
}
```

**Errors**

* 400 permission invalid.
* 400 share_type invalid.
* 403 Permission denied.
* 404 Library not found.
* 404 User not found.
* 500 Internal Server Error

#### <a id="batch-share-libraries-to-group"></a>Batch Share Libraries to Group

**POST** https://cloud.seafile.com/api/v2.1/repos/batch/

**Request parameters**

* operation, `share`
* share_type, `group`
* group_id
* permission, default is `rw`
* repo_id

**Sample request**

    curl -d "operation=share&share_type=group&group_id=540&repo_id=b6cfa05d-07af-422b-924e-45202dc1cbb5&repo_id=48aa475d-deb0-40f0-ab9b-22ec84989a58" -H 'Authorization: Token 40c89d06a2beeec672d091156de4cc163c6aa31a' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api/v2.1/repos/batch/

**Sample response**

```
{
    "failed": [
        {"repo_id": "f820bd12-0511-4542-b14b-3e48d8efc294", "error_msg": "This item has been shared to group-of-lian."}
    ],
    "success": [
        {"permission": "rw", "repo_id": "3761ade3-100b-4c3b-9508-79b3a510e6f6", "group_id": 65, "group_name": "group-of-lian"}
    ]
}
```

**Errors**

* 400 permission invalid.
* 400 share_type invalid.
* 403 Permission denied.
* 404 Library not found.
* 404 Group not found.
* 500 Internal Server Error

### <a id="shared-folders"></a>Shared Folders

#### <a id="share-a-folder"></a>Share A Folder

**PUT** https://cloud.seafile.com/api2/repos/{repo-id}/dir/shared_items/?p={path}

* repo-id
* path
* permission, `r` or `rw`
* share_type, `user` or `group`
* username, necessary if share_type is user
* group_id, necessary if share_type is group

**Sample request for share folder to user**

    curl -X PUT -d "username=2@1.com&share_type=user&permission=r" -H 'Authorization: Token ef12bf1e66a1aa797a1d6556fdc9ae84f1e9249f' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/78c620ee-2989-4427-8eff-7748f4fbebc0/dir/shared_items/?p=/q

**Sample response for share folder to user**

    {"failed": [], "success": [{"user_info": {"nickname": "2", "name": "2@1.com"}, "share_type": "user", "permission": "r"}]}

**Sample request for share folder to group**

    curl -X PUT -d "group_id=772&share_type=group&permission=rw" -H 'Authorization: Token ef12bf1e66a1aa797a1d6556fdc9ae84f1e9249f' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/78c620ee-2989-4427-8eff-7748f4fbebc0/dir/shared_items/?p=/q

**Sample response for share folder to group**

    {"failed": [], "success": [{"group_info": {"id": 772, "name": "group-2"}, "share_type": "group", "permission": "rw"}]}

**Errors**

* 400 share_type/permission/group_id invalid.
* 403 Permission denied.
* 404 Library/Folder/Group not found.
* 500 Failed to get sub repo.

#### <a id="list-shared-folders"></a>List Shared Folders

**GET** https://cloud.seafile.com/api/v2.1/shared-folders/

**Sample request**

    curl -v -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/shared-folders/

**Sample response**

```
[
    {
        "share_permission": "rw",
        "repo_id": "2deffbac-d7be-4ace-b406-efb799083ee9",
        "share_type": "personal",
        "folder_name": "asd",
        "path": "/asd",
        "user_name": "1",
        "contact_email": "contact@email.com",
        "user_email": "1@1.com"
    },
    {
        "share_permission": "r",
        "repo_id": "2deffbac-d7be-4ace-b406-efb799083ee9",
        "share_type": "group",
        "group_name": "test_group",
        "folder_name": "asd",
        "path": "/asd",
        "group_id": 1448
    }
]
```

**Errors**

* 500 Internal Server Error

#### <a id="update-shared-folder-permission"></a>Update Shared Folder Permission

**POST** https://cloud.seafile.com/api2/repos/2deffbac-d7be-4ace-b406-efb799083ee9/dir/shared_items/?p=/asd&share_type=user&username=1@1.com

**Sample request**

    curl -d "permission=r" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/2deffbac-d7be-4ace-b406-efb799083ee9/dir/shared_items/?p=/asd&share_type=user&username=1@1.com

**Sample response**

```
{"success":true}
```

**Errors**

* 400 permission invalid.
* 400 Email invalid.
* 403 Permission denied.
* 404 Library not found.
* 404 Folder not found.
* 500 Internal Server Error

#### <a id="#unshare-a-folder"></a>Unshare A Folder

**POST** https://cloud.seafile.com/api2/repos/2deffbac-d7be-4ace-b406-efb799083ee9/dir/shared_items/?p=/asd&share_type=group&group_id=1448

**Sample request**

    curl -X DELETE -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/2deffbac-d7be-4ace-b406-efb799083ee9/dir/shared_items/?p=/asd&share_type=group&group_id=1448

**Sample response**

```
{"success":true}
```

**Errors**

* 400 Email invalid.
* 403 Permission denied.
* 404 Library not found.
* 404 Folder not found.
* 500 Internal Server Error

## <a id="folder-permission"></a>Folder Permission

### <a id="user-folder-permission"></a>User Folder Permission

#### <a id="get-user-folder-permission"></a>Get User Folder Permission

**GET** http://192.168.1.124:8000/api2/repos/{repo_id}/user-folder-perm/?folder_path=/123

**Request parameters**

* repo_id
* folder_path

**Sample request**

```
curl -H 'Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.124:8000/api2/repos/bdf816e6-aba8-468c-962f-77c2fcfd1d1c/user-folder-perm/?folder_path=/123"
```

**Sample response**

```
    [
        {
        "repo_id": "bdf816e6-aba8-468c-962f-77c2fcfd1d1c",
        "folder_path": "/123",
        "permission": "r",
        "folder_name": "123",
        "user_name": "1",
        "user_email": "1@1.com"
    },
    {
        "repo_id": "bdf816e6-aba8-468c-962f-77c2fcfd1d1c",
        "folder_path": "/123",
        "permission": "rw",
        "folder_name": "123",
        "user_name": "2",
        "user_email": "2@1.com"
    }
]
```

**Errors**

* 403 Permission denied.
* 404 Library not found.

#### <a id="set-user-folder-permission"></a>Set User Folder Permission

**POST** http://192.168.1.124:8000/api2/repos/{repo_id}/user-folder-perm/

**Request parameters**

* repo_id
* folder_path
* user_email
* permission, `r` or `rw`

**Sample request**

```
curl -d "folder_path=/123&permission=rw&user_email=3@1.com&user_email=2@1.com" -H 'Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.124:8000/api2/repos/bdf816e6-aba8-468c-962f-77c2fcfd1d1c/user-folder-perm/"
```

**Sample response**

```
{
    "failed": [
        {
            "error_msg": "Permission already exists.",
            "user_email": "2@1.com"
        }
    ],
    "success": [
        {
            "repo_id": "bdf816e6-aba8-468c-962f-77c2fcfd1d1c",
            "folder_path": "/123",
            "permission": "rw",
            "folder_name": "123",
            "user_name": "3",
            "user_email": "3@1.com"
        }
    ]
}
```

**Errors**

* 400 folder_path invalid.
* 400 permission invalid.
* 403 Permission denied.
* 404 Library not found.
* 404 Folder not found.

#### <a id="modify-user-folder-permission"></a>Modify User Folder Permission

**PUT** http://192.168.1.124:8000/api2/repos/{repo_id}/user-folder-perm/

**Request parameters**

* repo_id
* folder_path
* user_email
* permission, `r` or `rw`

**Sample request**

```
curl -X PUT -d "folder_path=/123&permission=r&user_email=3@1.com" -H 'Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.124:8000/api2/repos/bdf816e6-aba8-468c-962f-77c2fcfd1d1c/user-folder-perm/"
```

**Sample response**

```
{
    "repo_id": "bdf816e6-aba8-468c-962f-77c2fcfd1d1c",
    "folder_path": "/123",
    "permission": "r",
    "folder_name": "123",
    "user_name": "3",
    "user_email": "3@1.com"
}
```

**Errors**

* 400 folder_path invalid.
* 400 permission invalid.
* 400 user_email invalid.
* 403 Permission denied.
* 404 Library not found.
* 404 Folder not found.
* 404 User not found.
* 404 Folder permission not found.
* 500 Internal Server Error

#### <a id="delete-user-folder-permission"></a>Delete User Folder Permission

**DELETE** http://192.168.1.124:8000/api2/repos/{repo_id}/user-folder-perm/

**Request parameters**

* repo_id
* folder_path
* user_email

**Sample request**

```
curl -X DELETE -d "folder_path=/123&user_email=3@1.com" -H 'Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.124:8000/api2/repos/bdf816e6-aba8-468c-962f-77c2fcfd1d1c/user-folder-perm/"
```

**Sample response**

```
{
    "success": true
}
```

**Errors**

* 400 user_email invalid.
* 400 folder_path invalid.
* 403 Permission denied.
* 404 Library not found.
* 404 User not found.
* 500 Internal Server Error

### <a id="group-folder-permission"></a>Group Folder Permission

#### <a id="get-group-folder-permission"></a>Get Group Folder Permission

**GET** http://192.168.1.124:8000/api2/repos/{repo_id}/group-folder-perm/?folder_path=/123

**Request parameters**

* repo_id
* folder_path

**Sample request**

```
curl -H 'Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.124:8000/api2/repos/bdf816e6-aba8-468c-962f-77c2fcfd1d1c/group-folder-perm/?folder_path=/123"
```

**Sample response**

```
[
    {
        "repo_id": "bdf816e6-aba8-468c-962f-77c2fcfd1d1c",
        "folder_path": "/123",
        "permission": "rw",
        "group_name": "group-2-of-lian",
        "folder_name": "123",
        "group_id": 586
    },
    {
        "repo_id": "bdf816e6-aba8-468c-962f-77c2fcfd1d1c",
        "folder_path": "/123",
        "permission": "r",
        "group_name": "group-of-lian",
        "folder_name": "123",
        "group_id": 65
    }
]
```

**Errors**

* 403 Permission denied.
* 404 Library not found.

#### <a id="set-group-folder-permission"></a>Set Group Folder Permission

**POST** http://192.168.1.124:8000/api2/repos/{repo_id}/group-folder-perm/

**Request parameters**

* repo_id
* folder_path
* group_id
* permission, `r` or `rw`

**Sample request**
```
curl -d "folder_path=/123&permission=rw&group_id=586&group_id=65" -H 'Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.124:8000/api2/repos/bdf816e6-aba8-468c-962f-77c2fcfd1d1c/group-folder-perm/"
```

**Sample response**

```
{
    "failed": [
        {
            "group_id": 65,
            "error_msg": "Permission already exists."
        }
    ],
    "success": [
        {
            "repo_id": "bdf816e6-aba8-468c-962f-77c2fcfd1d1c",
            "folder_path": "/123",
            "permission": "rw",
            "group_name": "group-2-of-lian",
            "folder_name": "123",
            "group_id": 586
        }
    ]
}
```

**Errors**

* 400 folder_path invalid.
* 400 permission invalid.
* 403 Permission denied.
* 404 Library not found.
* 404 Folder not found.

#### <a id="modify-group-folder-permission"></a>Modify Group Folder Permission

**PUT** http://192.168.1.124:8000/api2/repos/{repo_id}/group-folder-perm/

**Request parameters**

* repo_id
* folder_path
* group_id
* permission, `r` or `rw`

**Sample request**

```
curl -X PUT -d "folder_path=/123&permission=rw&group_id=65" -H 'Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.124:8000/api2/repos/bdf816e6-aba8-468c-962f-77c2fcfd1d1c/group-folder-perm/"
```

**Sample response**

```
{
    "repo_id": "bdf816e6-aba8-468c-962f-77c2fcfd1d1c",
    "folder_path": "/123",
    "permission": "rw",
    "group_name": "group-of-lian",
    "folder_name": "123",
    "group_id": 65
}
```

**Errors**

* 400 folder_path invalid.
* 400 permission invalid.
* 400 group_id invalid.
* 403 Permission denied.
* 404 Library not found.
* 404 Folder not found.
* 404 Group not found.
* 404 Folder permission not found.
* 500 Internal Server Error

#### <a id="delete-group-folder-permission"></a>Delete Group Folder Permission

**DELETE** http://192.168.1.124:8000/api2/repos/{repo_id}/group-folder-perm/

**Request parameters**

* repo_id
* folder_path
* group_id

**Sample request**

    curl -X DELETE -d "folder_path=/123&group_id=65" -H 'Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.124:8000/api2/repos/bdf816e6-aba8-468c-962f-77c2fcfd1d1c/group-folder-perm/"

**Sample response**

    {
        "success": true
    }

**Errors**

* 400 group_id invalid.
* 400 folder_path invalid.
* 403 Permission denied.
* 404 Library not found.
* 404 Group not found.
* 500 Internal Server Error

## <a id="library"></a>Library

### <a id="get-default-lib"></a>Get Default Library

**GET** https://cloud.seafile.com/api2/default-repo/

**Sample request**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/default-repo/"

**Sample response**

    {
        "repo_id": "691b3e24-d05e-43cd-a9f2-6f32bd6b800e",
        "exists": true
    }

### <a id="create-default-lib"></a>Create Default Library

**POST** https://cloud.seafile.com/api2/default-repo/

**Sample request**

    curl -X POST -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/default-repo/"

**Sample response**

    {
        "repo_id": "691b3e24-d05e-43cd-a9f2-6f32bd6b800e",
        "exists": true
    }

### <a id="list-libraries"></a>List Libraries

**GET** https://cloud.seafile.com/api2/repos/?type={type}

**Request parameters**

* type
    * `mine`, get my owned libraries.
    * `shared`, get libraries shared to me.
    * `group`, get group libraries.
    * `org`, get public libraires.

NOTE: If no `type` parameter contained in the url, this api will return all libraries user can access.

**Sample request for get all libraries I can accessed**

```
curl -H 'Authorization: Token 24fd3c026886e3121b2ca630805ed425c272cb96' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/
```

**Sample response for get all libraries I can accessed**

```
[
    {
        "permission": "rw",
        "encrypted": false,
        "mtime_relative": "<time datetime=\"2017-08-12T10:48:42\" is=\"relative-time\" title=\"Sat, 12 Aug 2017 10:48:42 +0800\" >1 minute ago</time>",
        "mtime": 1502506122,
        "owner": "1@1.com",
        "root": "",
        "id": "b8c8eeaf-a62f-4ece-a2cb-e1c67f49f881",
        "size": 0,
        "name": "group-lib",
        "type": "repo",
        "virtual": false,
        "version": 1,
        "head_commit_id": "b0a8c797972b83af1054428a397f843612257425",
        "size_formatted": "0 bytes"
    },
    {
        "permission": "rw",
        "encrypted": false,
        "mtime_relative": "<time datetime=\"2017-08-03T17:42:49\" is=\"relative-time\" title=\"Thu, 3 Aug 2017 17:42:49 +0800\" >8 days ago</time>",
        "mtime": 1501753369,
        "owner": "1@1.com",
        "root": "",
        "id": "cd0df3ce-7e1b-4fc3-9b76-714c48db47d7",
        "size": 1449,
        "name": "My Library",
        "type": "repo",
        "virtual": false,
        "version": 1,
        "head_commit_id": "9d47232bb87d39dbbba54fb8f09f9795b2d396e4",
        "size_formatted": "1.4 KB"
    },
    {
        "owner_nickname": "lian",
        "permission": "rw",
        "encrypted": false,
        "mtime_relative": "<time datetime=\"2017-08-12T10:44:07\" is=\"relative-time\" title=\"Sat, 12 Aug 2017 10:44:07 +0800\" >6 minutes ago</time>",
        "mtime": 1502505847,
        "owner": "lian@lian.com",
        "root": "",
        "id": "c474a093-19dc-4ddf-b0b0-72b33214ba33",
        "size": 708833229,
        "name": "seacloud.cc.124",
        "share_type": "personal",
        "type": "srepo",
        "version": 1,
        "head_commit_id": "0b11fc08518d0c9acfd15e95a580664896484336",
        "size_formatted": "676.0 MB"
    },
    {
        "permission": "rw",
        "encrypted": false,
        "mtime": 1502506122,
        "owner": "asdf",
        "id": "b8c8eeaf-a62f-4ece-a2cb-e1c67f49f881",
        "size": 0,
        "name": "group-lib",
        "root": "",
        "version": 1,
        "head_commit_id": "b0a8c797972b83af1054428a397f843612257425",
        "type": "grepo",
        "groupid": 1675
    },
    {
        "share_from": "lian@lian.com",
        "permission": "rw",
        "encrypted": false,
        "mtime_relative": "<time datetime=\"2017-08-12T10:33:47\" is=\"relative-time\" title=\"Sat, 12 Aug 2017 10:33:47 +0800\" >16 minutes ago</time>",
        "mtime": 1502505227,
        "owner": "Organization",
        "root": "",
        "id": "050ef344-45fb-49b6-80e6-e1bf094ab7bd",
        "size": 0,
        "name": "public-repo",
        "share_type": "public",
        "type": "grepo",
        "version": 1,
        "head_commit_id": "b71a95373896eb52e2971d72a869b7c413791b0b",
        "size_formatted": "0 bytes"
    }
]
```

**Sample request for get my owned libraries**

```
curl -H "Authorization: Token 8cc0e7085a24b6abfee721e758b6aab4a90e7321" -H 'Accept: application/json; indent=4' "http://192.168.1.124:8000/api2/repos/?type=mine"
```

**Sample response for get my owned libraries**

```
[
    {
        "permission": "rw",
        "encrypted": false,
        "mtime_relative": "<time datetime=\"2017-08-12T10:48:42\" is=\"relative-time\" title=\"Sat, 12 Aug 2017 10:48:42 +0800\" >19 minutes ago</time>",
        "mtime": 1502506122,
        "owner": "1@1.com",
        "root": "",
        "id": "b8c8eeaf-a62f-4ece-a2cb-e1c67f49f881",
        "size": 0,
        "name": "group-lib",
        "type": "repo",
        "virtual": false,
        "version": 1,
        "head_commit_id": "b0a8c797972b83af1054428a397f843612257425",
        "size_formatted": "0 bytes"
    },
    {
        "permission": "rw",
        "encrypted": false,
        "mtime_relative": "<time datetime=\"2017-08-03T17:42:49\" is=\"relative-time\" title=\"Thu, 3 Aug 2017 17:42:49 +0800\" >8 days ago</time>",
        "mtime": 1501753369,
        "owner": "1@1.com",
        "root": "",
        "id": "cd0df3ce-7e1b-4fc3-9b76-714c48db47d7",
        "size": 1449,
        "name": "My Library",
        "type": "repo",
        "virtual": false,
        "version": 1,
        "head_commit_id": "9d47232bb87d39dbbba54fb8f09f9795b2d396e4",
        "size_formatted": "1.4 KB"
    }
]
```

### <a id="get-library-info"></a>Get Library Info

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/

**Request parameters**

* repo-id

**Sample request**

    curl -G -H 'Authorization: Token 24fd3c026886e3121b2ca630805ed425c272cb96' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/632ab8a8-ecf9-4435-93bf-f495d5bfe975/

**Sample response**

    {
    "encrypted": false,
    "password_need": null,
    "mtime": null,
    "owner": "self",
    "id": "632ab8a8-ecf9-4435-93bf-f495d5bfe975",
    "size": 1356155,
    "name": "org",
    "root": "b5227040de360dd22c5717f9563628fe5510cbce",
    "desc": "org file",
    "type": "repo"
    }

### <a id="get-library-owner"></a>Get Library Owner

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/owner/

**Request parameters**

* repo-id

**Sample request**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d9b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/owner/

**Sample response**

    {
    "owner": "user@example.com"
    }

**Errors**

* 403 Permission error(only administrator/repo-owner can perform this action).

### <a id="get-library-history"></a>Get Library History

**GET** https://cloud.seafile.com/api/v2.1/repos/{repo_id}/history/


**Request parameters**

* repo_id
* page, default 1
* per_page, default 100

**Sample request**

    curl -H 'Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a' -H 'Accept: application/json; charset=utf-8; indent=4' "https://cloud.seafile.com/api/v2.1/repos/7460f7ac-a0ff-4585-8906-bb5a57d2e118/history/"

**Sample response**
```
{
    "data": [
        {
            "commit_id": "2b1313e4bbce2b938403c829b114b12b549128a3",
            "time": "2017-04-10T03:24:09+00:00",
            "description": "Recovered deleted directory \"456\"",
            "creator": "lian@lian.com"
        },
        {
            "commit_id": "0be8bba456ece31598557d9f3d5471b5b4d9d7c0",
            "time": "2017-04-10T03:23:49+00:00",
            "description": "Removed directory \"456\"",
            "creator": "lian@lian.com"
        },
        {
            "commit_id": "e6f21a80d60b7f1797434fdab622e562af937f81",
            "time": "2017-04-10T03:23:45+00:00",
            "description": "Deleted \"empty.docx\"",
            "creator": "lian@lian.com"
        },
        {
            "commit_id": "0bddb7401a75a9799209a24fb118e8d49151b6d6",
            "time": "2017-04-10T03:23:41+00:00",
            "description": "Deleted \"QQ_account_manager.png\"",
            "creator": "lian@lian.com"
        }
    ],
    "more": false
}
```

**Errors**

* 403 Permission denied.
* 404 Library not found.
* 500 Internal Server Error

### <a id="get-library-trash"></a>Get Library Trash

**GET** https://cloud.seafile.com/api/v2.1/repos/{repo_id}/trash/


**Request parameters**

* repo_id
* path, default '/'.
* per_page, default 100.
* scan_stat, An opaque status returned by the last call. In the first call, None must be passed. The last entry of the result list contains a 'scan_stat' attribute. In the next call, pass in the returned 'scan_stat'.

**Sample request**

    curl -H 'Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a' -H 'Accept: application/json; charset=utf-8; indent=4' "https://cloud.seafile.com/api/v2.1/repos/7460f7ac-a0ff-4585-8906-bb5a57d2e118/trash/"

**Sample response**
```
{
    "scan_stat": "2b1313e4bbce2b938403c829b114b12b549128a3",
    "data": [
        {
            "commit_id": "2364981a2bef50c16281a664df55af209019a88c",
            "scan_stat": null,
            "obj_id": "f86ef37332e89d6a132e27ce857c76e15971b227",
            "deleted_time": "2017-04-10T03:23:41+00:00",
            "obj_name": "QQ_account_manager.png",
            "is_dir": false,
            "parent_dir": "/",
            "size": 77970
        },
        {
            "commit_id": "0bddb7401a75a9799209a24fb118e8d49151b6d6",
            "scan_stat": null,
            "obj_id": "10ae7309338efe92d9ceddb9d6835463d277da34",
            "deleted_time": "2017-04-10T03:23:45+00:00",
            "obj_name": "empty.docx",
            "is_dir": false,
            "parent_dir": "/456/",
            "size": 10682
        }
        ...
    ],
    "more": true
}
```

Get more trash items.

**Sample request**

    curl -H 'Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a' -H 'Accept: application/json; charset=utf-8; indent=4' "https://cloud.seafile.com/api/v2.1/repos/7460f7ac-a0ff-4585-8906-bb5a57d2e118/trash/?scan_stat=2b1313e4bbce2b938403c829b114b12b549128a3"

**Sample response**
```
{
    "scan_stat": null,
    "data": [
        {
            "commit_id": "726d2ce009df9176592ab88eca297b5e50c15639",
            "scan_stat": null,
            "obj_id": "cfc5e4299a862b366c98eeb7f5a8a1f689d2916a",
            "deleted_time": "2017-04-10T09:11:02+00:00",
            "obj_name": "empty.xlsx",
            "is_dir": false,
            "parent_dir": "/456/",
            "size": 8176
        },
        {
            "commit_id": "2b1313e4bbce2b938403c829b114b12b549128a3",
            "scan_stat": null,
            "obj_id": "414a75f5c67ca56c480ca2ae9137b7812940c3ce",
            "deleted_time": "2017-04-10T09:11:01+00:00",
            "obj_name": "empty.pptx",
            "is_dir": false,
            "parent_dir": "/456/",
            "size": 40506
        }
    ],
    "more": false
}
```

**Errors**

* 403 Permission denied.
* 404 Library not found.
* 500 Internal Server Error

### <a id="get-library-history-limit-days"></a>Get Library History Limit Days

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/history-limit/

**Request parameters**

* repo-id

**Sample request**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d9b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/history-limit/

**Sample response**

    {
    "keep_days": -1,
    }

**Errors**

* 403 Permission denied.
* 404 Library not found.
* 500 Internal Server Error

### <a id="set-library-history-limit-days"></a>Set Library History Limit Days

**PUT** https://cloud.seafile.com/api2/repos/{repo-id}/history-limit/

**Request parameters**

* repo-id
* keep_days. -1 for keep full history; 0 for do not keep history; positive number for keep a period of limit days.

**Sample request**

    curl -v -X PUT -d "keep_days=4" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/history-limit/

**Sample response**

    {
    "keep_days": 4,
    }

**Errors**

* 400 keep_days invalid.
* 403 Permission denied.
* 404 Library not found.
* 500 Internal Server Error
* 520 Failed to set library history limit.

### <a id="create-library"></a>Create Library

**POST** https://cloud.seafile.com/api2/repos/

**Request parameters**

* name
* desc (defaults to "new repo")
* passwd (needed by encrypt library)

**Sample request**

    curl -v -d "name=foo&desc=new library" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/

**Sample response**

    {
    "encrypted": "",
    "enc_version": 0,
    "repo_id": "f15811fd-5c19-412c-b143-2ac83f352290",
    "magic": "",
    "relay_id": "c5e41170db250ea497075e2911104faf0105b7fb",
    "repo_version": 1,
    "relay_addr": "cloud.seafile.com",
    "token": "c1f3defe9ba408cd7964427ec276843e9d10c23b",
    "relay_port": "10001",
    "random_key": "",
    "email": "user@mail.com",
    "repo_name": "foo"
    }

**Success**

   Response code 200 and newly created library information are returned.

**Errors**

* 400 Library name missing.
* 520 Operation failed.

### <a id="check/create-sub-library"></a>Check/Create Sub Library

check if a dir has a corresponding sub_repo, if it does not have, create one

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/dir/sub_repo/?p=/\&name=sub_lib

**Request parameters**

* repo-id
* p
* name

**Sample request**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d9b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/dir/sub_repo/?p=/\&name=sub_lib

**Sample response**

    {"sub_repo_id": "c0a3283c-013c-4a7c-8f68-006f06fa6dec"}

**Errors**

* 400 Argument missing
* 500 INTERNAL SERVER ERROR

### <a id="delete-library"></a>Delete Library

**DELETE** https://cloud.seafile.com/api2/repos/{repo-id}/

**Sample request**

    curl -v -X DELETE -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/8f5f2222-72a8-454f-ac40-8397c5a556a8/

**Sample response**

"success"

**Errors**

* 400 Library does not exist.

* 403 Only library owner can perform this operation.

### <a id="rename-library"></a>Rename Library

**POST** https://cloud.seafile.com/api2/repos/{repo-id}/?op=rename

**Sample request**

    curl -d "repo_name=new-repo-name"  -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/8f5f2222-72a8-454f-ac40-8397c5a556a8/op=rename

**Sample response**

"success"

**Errors**

* 404 Library not found.
* 403 You do not have permission to rename this library.
* 500 Unable to rename library

### <a id="transfer-library"></a>Transfer Library

**PUT** https://cloud.seafile.com/api2/repos/{repo-id}/owner/

**Request parameters**

* repo-id
* owner

**Sample request**

    curl -v -X PUT -d "owner=new@owner.com" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d9b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/owner/

**Sample response**

    {
    "success": True
    }

**Errors**

* 440 Email invalid.
* 403 Permission error(only administrator/repo-owner can perform this action).
* 404 Library not found.
* 404 User not found.

### <a id="decrypt-library"></a>Decrypt Library

**POST** https://cloud.seafile.com/api2/repos/{repo-id}/

**Request parameters**

* password

**Sample request**

    curl -v -d "password=123" -H 'Authorization: Token e6a33d61954f219a96b60f635cf02717964e4385' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/0c2465a5-4753-4660-8a22-65abec9ec8d0/

**Sample response**

"success"

**Errors**

* 400 Incorrect password
* 409 Repo is not encrypt
* 500 Internal server error

### <a id="create-public-lib"></a>Create Public Library

**POST** https://cloud.seafile.com/api2/repos/public/

**Request parameters**

* name
* permission, `r` or `rw`, default `r`.
* passwd (optional).

**Sample request**, create an encrypted public repo with `rw` permission

    curl -X POST -d "name=test-public-repo&permission=rw&passwd=password" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d9b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/public/

**Sample response**

```
{
    "owner_nickname": "lian",
    "permission": "rw",
    "encrypted": true,
    "mtime_relative": "<time datetime=\"2016-05-31T12:01:49\" is=\"relative-time\" title=\"Tue, 31 May 2016 12:01:49 +0800\" >1 second ago</time>",
    "mtime": 1464667309,
    "owner": "lian@lian.com",
    "id": "6553fd8b-bf3e-41ad-a481-90c8523d3b4a",
    "size": 0,
    "name": "test-public-repo",
    "desc": "",
    "size_formatted": "0 bytes"
}
```

**Errors**

* 400 Library name is required.
* 400 Invalid permission
* 403 You do not have permission to create library.
* 403 NOT allow to create encrypted library.

### <a id="set-exist-lib-as-public-lib"></a>Set Exist Lib as Public Library

**PUT** https://cloud.seafile.com/api2/shared-repos/{repo-id}/?share_type=public

**Request parameters**

* repo_id
* share_type, must be `public`
* permission, `r` or `rw`.

**Sample request**, create an encrypted public repo with `rw` permission

    curl -X PUT -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d9b477fd' -H 'Accept: application/json; indent=4' 'https://cloud.seafile.com/api2/shared-repos/2deffbac-d7be-4ace-b406-efb799083ee9/?share_type=public&permission=rw'

**Sample response**

```
success
```

**Errors**

* 400 Permission need to be rw or r.
* 403 You do not have permission to share library.
* 500 Failed to share library to public.

### <a id="remove-public-lib"></a>Remove Public Library

**DELETE** https://cloud.seafile.com/api2/shared-repos/{repo-id}/?share_type=public

**Request parameters**

* repo-id
* share_type

**Sample request**

    curl -X DELETE -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d9b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/shared-repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/?share_type=public

**Success**

    "success"

**Errors**

* 400 Share type is required.
* 400 Share type can only be personal or group or public.
* 403 You do not have permission to unshare library.

### <a id="fetch-library-download-info"></a>Fetch library download info

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/download-info/

**Request parameters**

* repo-id

**Sample request**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d9b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/download-info/

**Sample response**

    {
    "applet_root": "https://localhost:13420",
    "relay_addr": "localhost",
    "token": "46acc4d9ca3d6a5c7102ef379f82ecc1edc629e1",
    "repo_id": "dae8cecc-2359-4d33-aa42-01b7846c4b32",
    "relay_port": "10002",
    "encrypted": "",
    "repo_name": "test",
    "relay_id": "8e4b13b49ca79f35732d9f44a0804940d985627c",
    "email": "user@example.com"
    }

### <a id="search-files-in-libraries"></a>Search Files in Libraries

**GET** https://cloud.seafile.com/api2/search/

**Request parameters**

* `q`, keyword for searching.

* `page`, optional, a number greater than or equal to **1**.

* `per_page`, optional.

* `search_repo`, `all`, `mine`, `shared`, `group`, `public` or a *repo_id*, (`all` for searching in all libraries, etc.), optional. For searching in shared libraries, you can also pass `shared_from` or `not_shared_from` parameter beside `shared` to filter shared libraries.

* `search_path`, path of specifiy library.(This option works only when search_repo is a single repo_id.)

* `search_ftypes`, `all` or `custom`, (`all` for searching all file types, `custom` for only searching the specific file types you defined in `ftype` and `input_fexts`).

* `ftype`, must be in (`Text`, `Document`, `Image`, `Video`, `Audio`, `PDF`, `Markdown`).

> TEXT: ('ac', 'am', 'bat', 'c', 'cc', 'cmake', 'cpp', 'cs', 'css', 'diff', 'el', 'h', 'html', 'htm', 'java', 'js', 'json', 'less', 'make', 'org', 'php', 'pl', 'properties', 'py', 'rb', 'scala', 'script', 'sh', 'sql', 'txt', 'text', 'tex', 'vi', 'vim', 'xhtml', 'xml', 'log', 'csv', 'groovy', 'rst', 'patch', 'go'),
>
> DOCUMENT: ('doc', 'docx', 'ppt', 'pptx', 'odt', 'fodt', 'odp', 'fodp'),
>
> IMAGE: ('gif', 'jpeg', 'jpg', 'png', 'ico', 'bmp', 'tif', 'tiff', 'eps'),
>
> VIDEO: ('mp4', 'ogv', 'webm', 'mov'),
>
> AUDIO: ('mp3', 'oga', 'ogg'),
>
> PDF: ('pdf',),
>
> MARKDOWN: ('markdown', 'md'),

* `input_fexts`, file extensions manually specific.

* `with_permission`, `true` or `false`. Whether return permission info of the file or not, default is `false`.

**Sample request**
```
curl -H 'Authorization: Token 076de58233c09f19e7a5179abff14ad55987350e' -H 'Accept: application/json; charset=utf-8; indent=4' "https://cloud.seafile.com/api2/search/?q=seafile&search_repo=all&search_ftypes=custom&ftype=Document&input_fexts=md,png&per_page=3&page=3&with_permission=true"
```

**Sample response**
```
{
    "has_more": true,
    "total": 336,
    "results": [
        {
            "repo_id": "040a8aad-5646-4c68-ba8a-73f90c60089f",
            "name": "seafile \u8fd0\u7ef4.docx",
            "permission": "r",
            "oid": "ecba7db3d6b818873bf94cb1f2161f6a0fc22494",
            "last_modified": 1482910730,
            "content_highlight": "... .<b>seafile</b>.com...",
            "fullpath": "/\u4e1c\u98ce\u65e5\u4ea7/Archived/seafile \u8fd0\u7ef4.docx",
            "repo_name": "\u4ee3\u7ef4\u5ba2\u6237",
            "is_dir": false,
            "repo_type": 'mine',
            "size": 494490
        },
        {
            "repo_id": "233191c7-8e33-4fd2-b0a3-e480363d8e0d",
            "name": "seafile-tutorial.doc",
            "permission": "rw",
            "oid": "1066014004ad479dd7f3cc0a12462c3f1fd2edeb",
            "last_modified": 1389771193,
            "content_highlight": "...A Brief Tour of <b>Seafile</b> <b>Seafile</b> is a file m...",
            "fullpath": "/\u4ea7\u54c1\u4f7f\u7528\u6587\u6863/seafile-tutorial.doc",
            "repo_name": "seafile-dev",
            "is_dir": false,
            "repo_type": 'mine',
            "size": 414208
        },
        {
            "repo_id": "233191c7-8e33-4fd2-b0a3-e480363d8e0d",
            "name": "seafile_vm.md",
            "permission": "rw",
            "oid": "66c8dbe139333ead26b4878340da486fffdc5330",
            "last_modified": 1439277140,
            "content_highlight": "...<b>Seafile</b> server VM...",
            "fullpath": "/\u90e8\u7f72\u548c\u8fd0\u7ef4/seafile_vm.md",
            "repo_name": "seafile-dev",
            "is_dir": false,
            "repo_type": 'shared',
            "size": 3255
        }
    ]
}
```

**Sample request**

    Search for files in a library specified directory.
    
    curl -H 'Authorization: Token 076de58233c09f19e7a5179abff14ad55987350e' -H 'Accept: application/json; charset=utf-8; indent=4' "https://cloud.seafile.com/api2/search/?q=a&search_repo=2628a63b-cfad-41f5-a748-392ec9287686&search_path=/testtest"

**Sample response**

    {
        "has_more": false,
        "total": 2,
        "results": [
            {
                "repo_owner_name": "admin",
                "repo_id": "2628a63b-cfad-41f5-a748-392ec9287686",
                "name": "3a",
                "repo_owner_contact_email": "admin@admin.com",
                "repo_owner_email": "admin@admin.com",
                "last_modified": 1520836447,
                "content_highlight": "",
                "fullpath": "/testtest/3a",
                "repo_name": "dev",
                "is_dir": false,
                "size": 0
            },
            {
                "repo_owner_name": "admin",
                "repo_id": "2628a63b-cfad-41f5-a748-392ec9287686",
                "name": "1a",
                "repo_owner_contact_email": "admin@admin.com",
                "repo_owner_email": "admin@admin.com",
                "last_modified": 1520836462,
                "content_highlight": "",
                "fullpath": "/testtest/1a",
                "repo_name": "dev",
                "is_dir": false,
                "size": 0
            }
        ]
    }

**Errors**

* 404 Search not supported.
* 400 Missing argument q.

### <a id="get-library-download-links"></a>Get Library Download Links

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/download-shared-links/

**Request parameters**

* repo-id

**Sample request**

    curl -H 'Authorization: Token 24fd3c026886e3121b2ca630805ed425c272cb96' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/632ab8a8-ecf9-4435-93bf-f495d5bfe975/download-shared-links/

**Sample response**

    [
        {
            "view_count": 0,
            "name": "/",
            "share_type": "d",
            "creator_name": "lian",
            "create_by": "lian@lian.com",
            "token": "105f108fb6",
            "create_time": "2016-01-18T15:03:10+0800",
            "path": "/",
            "size": ""
        },
        {
            "view_count": 3,
            "name": "1.md",
            "share_type": "f",
            "creator_name": "lian",
            "create_by": "lian@lian.com",
            "token": "a626012c1b",
            "create_time": "2016-01-19T11:27:43+0800",
            "path": "/1.md",
            "size": "4"
        }
    ]

**Errors**

* 403 Permission denied.
* 404 Library not found.

#### <a id="get-library-upload-links"></a>Get Library Upload Links

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/upload-shared-links/

**Request parameters**

* repo-id

**Sample request**

    curl -H 'Authorization: Token 24fd3c026886e3121b2ca630805ed425c272cb96' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/632ab8a8-ecf9-4435-93bf-f495d5bfe975/upload-shared-links/

**Sample response**

    [
        {
            "view_count": 3,
            "name": "/",
            "creator_name": "lian",
            "create_by": "lian@lian.com",
            "token": "43340efca5",
            "create_time": "2016-01-18T15:03:12+0800",
            "path": "/"
        },
        {
            "view_count": 8,
            "name": "a&b",
            "creator_name": "lian",
            "create_by": "lian@lian.com",
            "token": "f1e49d445a",
            "create_time": "2016-01-18T15:03:18+0800",
            "path": "/a&b/"
        }
    ]

**Errors**

* 403 Permission denied.
* 404 Library not found.

#### <a id="delete-library-download-link"></a>Delete Library Download Link

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/download-shared-links/{token}/

**Request parameters**

* repo-id
* token

**Sample request**

    curl -X DELETE -H 'Authorization: Token 24fd3c026886e3121b2ca630805ed425c272cb96' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/632ab8a8-ecf9-4435-93bf-f495d5bfe975/download-shared-links/105f108fb6/

**Sample response**

    {"success": true}

**Errors**

* 403 Permission denied.
* 404 Library not found.
* 404 Link not found.

#### <a id="delete-library-upload-link"></a>Delete Library Upload Link

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/upload-shared-links/{token}/

**Request parameters**

* repo-id
* token

**Sample request**

    curl -X DELETE -H 'Authorization: Token 24fd3c026886e3121b2ca630805ed425c272cb96' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/632ab8a8-ecf9-4435-93bf-f495d5bfe975/upload-shared-links/f1e49d445a/

**Sample response**

    {"success": true}

**Errors**

* 403 Permission denied.
* 404 Library not found.
* 404 Link not found.

#### <a id="search-library-by-name"></a>Search Library By Name

**GET** https://cloud.seafile.com/api2/repos/

**Request parameters**

* type (optional)
* nameContains (optional)

**Sample request**

    Search the all library

    curl -H 'Authorization: Token 24fd3c026886e3121b2ca630805ed425c272cb96' -sS 'https://cloud.seafile.com/api2/repos/?nameContains=T'

**Sample response**

    [
        {
            "root": "",
            "modifier_email": null,
            "name": "TEST",
            "permission": "rw",
            "size_formatted": "424.6 MB",
            "virtual": false,
            "mtime_relative": "<time datetime=\"2017-07-04T08:30:33\" is=\"relative-time\" title=\"Tue, 4 Jul 2017 08:30:33 +0000\" >2017-07-04</time>",
            "head_commit_id": "05418e616a5325b3f0ccfaf7d4c54c803b8168de",
            "encrypted": false,
            "version": 1,
            "mtime": 1499157033,
            "owner": "admin@admin.com",
            "modifier_contact_email": "",
            "type": "repo",
            "id": "a9025464-2c72-4b9c-9cdd-6de62e56f696",
            "modifier_name": "",
            "size": 445243555
        }
    ]

**Sample request**

    Search the specified library

    curl -H 'Authorization: Token 24fd3c026886e3121b2ca630805ed425c272cb96' -sS 'https://cloud.seafile.com/api2/repos/?type=mime&nameContains=T'

**Sample response**

    []


**Errors**

None

## <a id="file"></a>File

### <a id="view-file-through-owa"></a>View File Through Owa

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/owa-file/?path=/foo.docx

**Request parameters**

* repo-id
* path
* action, `view` or `edit`, default value is `view`;

**Sample request for view**

    curl  -v  -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' 'https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/owa-file/?path=/foo.docx'

**Sample response for view**

```
{
    "access_token": "7decacff-6e55-4856-9734-01aaab26ef45",
    "action_url": "http://off1.off.com/wv/wordviewerframe.aspx?WOPIsrc=http%3A%2F%2F192.168.1.124%3A8000%2Fapi2%2Fwopi%2Ffiles%2F2b0750085925fa85238e5f64cfd13ed6f1076bfd%2F",
    "access_token_ttl": 1456906784000
}
```

**Sample request for edit**

    curl  -v  -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' 'https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/owa-file/?path=/foo.docx&action=edit'

**Sample response for edit**

```
{
    "access_token": "bb80a7934b42454189ade73bdfba7f62",
    "action_url": "http://off1.off.com/we/wordeditorframe.aspx?WOPISrc=http%3A%2F%2F192.168.1.227%3A8000%2Fapi2%2Fwopi%2Ffiles%2F1ef1da7af8dc2d02f85f156dba779a31ff1db9f7&ui=zh-CN&rs=zh-CN",
    "access_token_ttl": 1496925674000
}
```

**After get response**

In order to instantiate the Office Online applications, a host must create an HTML page that will host an iframe element within it pointing to a particular WOPI action URL. And then use a form element and POST the `access_token` and `access_token_ttl` values to the Office Online.

For more info, you can see [this official docs](http://wopi.readthedocs.org/en/latest/hostpage.html).

**Errors**

* 400 path invalid.
* 403 permission denied.
* 403 Library encrypted.
* 403 Office Web App feature not enabled.
* 403 Office Web App feature only supported in professional edition.
* 404 File/Library not found.
* 500 Internal Server Error

### <a id="download-file"></a>Download File

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/file/?p=/foo

**Request parameters**

* repo-id
* p
* reuse (optional): Set `reuse` to `1` if you want the generated download link can be accessed more than once in one hour.

**Sample request**

    curl  -v  -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' 'https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/?p=/foo.c&reuse=1'

**Sample response**

    "https://cloud.seafile.com:8082/files/adee6094/foo.c"

**Errors**

* 400 Path is missing
* 404 File not found
* 520 Operation failed.

### <a id="get-file-detail"></a>Get File Detail

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/file/detail/?p=/foo.c

* repo-id
* p

**Sample request**

    curl -H 'Authorization: Token f2210dacd3606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/detail/?p=/foo.c

**Sample response**

    {
    "id": "013d3d38fed38b3e8e26b21bb3463eab6831194f",
    "mtime": 1398148877,
    "type": "file",
    "name": "foo.py",
    "size": 22
    }

**Errors**

* 400 Path is missing
* 520 Operation failed.

### <a id="get-file-history"></a>Get File History

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/file/history/?p=/foo.c

**Request parameters**

* repo-id
* p

**Sample request**

    curl -H 'Authorization: Token f2210dacd3606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/history/?p=/foo.c

**Sample response**

    {
    "commits":
        [
            {
            "rev_file_size": 0,
            "repo_id": "a582d3bc-bcf5-421e-9125-741fa56d18d4",
            "ctime": 1398149763,
            "creator_name": "user@example.com",
            "creator": "0000000000000000000000000000000000000000",
            "root_id": "b64d413d9894c9206beac3faf9c2a0d75b4a8ebf",
            "rev_renamed_old_path": null,
            "parent_id": "8e546762e1657ab22dad83e9cb1e5ea31a767c9a",
            "new_merge": false,
            "version": 1,
            "conflict": false,
            "desc": "Added \"foo.c\"",
            "id": "9464f7499bfa7363d563282361339eaf96a93318",
            "rev_file_id": "0000000000000000000000000000000000000000",
            "second_parent_id": null
            },
            {
            "rev_file_size": 0,
            "repo_id": "a582d3bc-bcf5-421e-9125-741fa56d18d4",
            "ctime": 1398146059,
            "creator_name": "user@example.com",
            "creator": "0000000000000000000000000000000000000000",
            "root_id": "572413414257c76039897e00aeb35f819471206b",
            "rev_renamed_old_path": null,
            "parent_id": "f977bdb0ebb205645c3b42216c2817e511c3f68f",
            "new_merge": false,
            "version": 1,
            "conflict": false,
            "desc": "Added \"foo.c\"",
            "id": "a1ec20709675f4dc8db825cdbca296be245d189b",
            "rev_file_id": "0000000000000000000000000000000000000000",
            "second_parent_id": null
            }
        ]
    }

**Errors**

* 400 Path is missing
* 404 File not found

### <a id="restore-file-from-history"></a>Restore File From History

**POST** https://cloud.seafile.com/api/v2.1/repos/7460f7ac-a0ff-4585-8906-bb5a57d2e118/file/?p=/1.md

**Request parameters**

* repo_id
* p
* operation
* commit_id

**Sample request**

    curl -d "operation=revert&commit_id=7ed3ccdc7559d1afddb95bc050230e3d54bbffef" -H "Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a" -H 'Accept: application/json; indent=4' "https://cloud.seafile.com/api/v2.1/repos/7460f7ac-a0ff-4585-8906-bb5a57d2e118/file/?p=/1.md"

**Sample response**
```
{
    "success": true
}
```

**Errors**

* 400 commit_id invalid.
* 403 Permission denied.
* 403 File is locked
* 500 Internal Server Error
* 500 Check file lock error

### <a id="download-file-revision"></a>Download File From a Revision

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/file/revision/?p=/foo.c&commit_id=a1ec20709675f4dc8db825cdbca296be245d189b

**Request parameters**

* repo-id
* p
* commit_id

**Sample request**

    curl -H 'Authorization: Token f2210dacd3606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/revision/?p=/foo.c\&commit_id=a1ec20709675f4dc8db825cdbca296be245d189b

**Sample response**

    "https://cloud.seafile.com:8082/files/adee6094/foo.c"

**Errors**

* 400 Path is missing
* 404 Revision not found

### <a id="create-file"></a>Create File

**POST** https://cloud.seafile.com/api/v2.1/repos/{repo_id}/file/?p={file_path}

**Request parameters**

* repo-id
* p
* operation

**Sample request**
```
curl -d 'operation=create' -H 'Authorization: Token c5de3074be40861f399f02c65149c6460bbf073f' "https://cloud.seafile.com/api/v2.1/repos/7460f7ac-a0ff-4585-8906-bb5a57d2e118/file/?p=/test.xlsx"
```

**Sample response**
```
{
    'is_locked': False,
    'mtime': '2017-09-12T14:57:42+08:00',
    'obj_id': u'44bdca6005429390d1ecc6943b05c821bd30917a',
    'obj_name': u'test.xlsx',
    'parent_dir': u'/',
    'repo_id': u'7460f7ac-a0ff-4585-8906-bb5a57d2e118',
    'size': 7631,
    'type': 'file'
}
```

**Errors**

* 400 operation/name invalid.
* 400 operation can only be 'create', 'rename', 'move', 'copy' or 'revert'.
* 404 Library/Folder not found.
* 403 Permission denied.
* 500 Internal Server Error

### <a id="rename-file"></a>Rename File

**POST** https://cloud.seafile.com/api2/repos/{repo-id}/file/?p=/foo.c

**Request parameters**

* repo-id
* p
* operation=rename
* newname

**Sample request**

    curl -v -d "operation=rename&newname=newfoo.c" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/?p=/foo.c

**Sample response**

    ...
    < HTTP/1.1 301 MOVED PERMANENTLY
    ...
    "success"

**Success**

   Response code is 301, and a string `"success"` is returned.

**Errors**

* 400 BAD REQUEST, Path is missing or invalid(e.g. p=/) or newname is missing(newname too long)
* 403 FORBIDDEN, You do not have permission to rename file
* 404 NOT FOUND, repo not found
* 409 CONFLICT, the newname is the same to the old
* 520 OPERATION FAILED, fail to rename file

### <a id="lock-file"></a>Lock File

**PUT** https://cloud.seafile.com/api2/repos/{repo-id}/file/

**Request parameters**

* repo-id
* p
* operation

**Sample request**

    curl -v -X PUT -d "operation=lock&p=/foo.c" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/

**Sample response**

    ...
    < HTTP/1.0 200 OK
    ...
    "success"

**Success**

   Response code is 200, and a string `"success"` is returned.

**Errors**

* 400 BAD REQUEST, Path is missing or invalid(e.g. p=/)
* 403 FORBIDDEN, You do not have permission to lock file
* 404 NOT FOUND, repo not found
* 520 OPERATION FAILED, fail to lock file

### <a id="unlock-file"></a>Unlock File

**PUT** https://cloud.seafile.com/api2/repos/{repo-id}/file/

**Request parameters**

* repo-id
* p
* operation

**Sample request**

    curl -v -X PUT -d "operation=unlock&p=/foo.c" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/

**Sample response**

    ...
    < HTTP/1.0 200 OK
    ...
    "success"

**Success**

   Response code is 200, and a string `"success"` is returned.

**Errors**

* 400 BAD REQUEST, Path is missing or invalid(e.g. p=/)
* 403 FORBIDDEN, You do not have permission to lock file
* 404 NOT FOUND, repo not found
* 520 OPERATION FAILED, fail to unlock file

### <a id="move-file"></a>Move File

**POST** https://cloud.seafile.com/api2/repos/{repo-id}/file/?p=/foo.c

**Request parameters**

* repo-id
* p
* operation
* dst_repo
* dst_dir

**Sample request**

    curl -v -d "operation=move&dst_repo=affc837f-7fdd-4e91-b88a-32caf99897f2&dst_dir=/123" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/?p=/foo.c

**Sample response**

    ...
    < HTTP/1.1 301 MOVED PERMANENTLY
    ...
    {
        "repo_id": "affc837f-7fdd-4e91-b88a-32caf99897f2",
        "parent_dir": "/123",
        "obj_name": "foo.c"
    }

**Success**

   Response code is 301, and a string `"success"` is returned.

**Errors**

* 400 BAD REQUEST, Path is missing or invalid(e.g. p=/)
* 403 FORBIDDEN, You do not have permission to move file
* 404 NOT FOUND, repo not found
* 500 INTERNAL SERVER ERROR

### <a id="copy-file"></a>Copy File

**POST** https://cloud.seafile.com/api2/repos/{repo-id}/file/?p=/foo.c

**Request parameters**

* repo-id
* p
* operation
* dst_repo
* dst_dir

**Sample request**

    curl -v -d "operation=copy&dst_repo=73ddb2b8-dda8-471b-b7a7-ca742b07483c&dst_dir=/123" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/c7436518-5f46-4296-97db-2fcba4c8c8db/file/?p=/foo.c

**Sample response**

    ...
    < HTTP/1.1 200 OK
    ...
    {
        "repo_id": "73ddb2b8-dda8-471b-b7a7-ca742b07483c",
        "parent_dir": "/123",
        "obj_name": "foo.c"
    }

**Success**

   Response code is 200, and a string `"success"` is returned.

**Errors**

* 400 BAD REQUEST, Path is missing or invalid(e.g. p=/)
* 403 FORBIDDEN, You do not have permission to copy file
* 500 INTERNAL SERVER ERROR

### <a id="revert-file"></a>Revert File

**PUT** https://cloud.seafile.com/api2/repos/{repo_id}/file/revert/

**Request parameters**

* repo_id
* p
* commit_id

**Sample request**

    curl -v -X PUT -d "commit_id=a1ec20709675f4dc8db825cdbca296be245d189b&p=/foo.c" -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/8f5f2222-72a8-454f-ac40-8397c5a556a8/file/revert/

**Sample response**

    ...
    < HTTP/1.0 200 OK
    ...

    {"ret": 0}

**Success**

    Response code 200(OK) is returned.

**Errors**

* 400 Path is missing

### <a id="delete-file"></a>Delete File

**DELETE** https://cloud.seafile.com/api2/repos/{repo-id}/file/?p=/foo

**Request parameters**

* repo-id
* p

**Sample request**

    curl -X DELETE -v  -H 'Authorization: Token f2210dacd3606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/?p=/foo.c

**Sample response**

    ...
    < HTTP/1.0 200 OK
    ...
    "success"

**Errors**

* 400 Path is missing
* 520 Operation failed.

**Note**

   This can also be used to delete directory.

### <a id="upload-file"></a>Upload File

#### <a id="get-upload-link"></a>Get Upload Link

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/upload-link/?p=/upload-dir

**Request parameters**

* repo-id
* p (use '/' as default)

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" https://cloud.seafile.com/api2/repos/99b758e6-91ab-4265-b705-925367374cf0/upload-link/

**Sample response**

    "http://cloud.seafile.com:8082/upload-api/73c5d117-3bcf-48a0-aa2a-3f48d5274ae3"

**Errors**

    403 Permission denied.
    500 Run out of quota

#### <a id="upload-file-1"></a>Upload File

After getting the upload link, POST to this link for uploading files.

**POST** http://cloud.seafile.com:8082/upload-api/73c5d117-3bcf-48a0-aa2a-3f48d5274ae3

**Request parameters**

* file: local file path.
* parent_dir : path in your Seafile repo that you want to upload local file to.
* relative_path: sub path of "parent_dir", if this sub path does not exist, Seafile will create it recursively.
* ret-json: returns a json array including file info if set to `1`.

> NOTE:
> 1. `parent_dir` must endswith `/`
> 1. `relative_path` must NOT startswith `/`

**Sample request**

upload file to `/path-in-seafile-repo/`:

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -F file=@local-folder/test.txt -F parent_dir=/path-in-seafile-repo/ http://cloud.seafile.com:8082/upload-api/73c5d117-3bcf-48a0-aa2a-3f48d5274ae3

**Sample response for no `ret-json` parameter**

    "adc83b19e793491b1c6ea0fd8b46cd9f32e592fc"

upload file to `/path-in-seafile-repo/sub_path_1/sub_path_2/`, Seafile will create `sub_path_1/sub_path_2/` recursively if it does not exist:

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -F file=@local-folder/test.txt -F file=@1.jpg -F parent_dir=/path-in-seafile-repo/ -F relative_path=sub_path_1/sub_path_2/ http://cloud.seafile.com:8082/upload-api/73c5d117-3bcf-48a0-aa2a-3f48d5274ae3?ret-json=1

**Sample response for with `?ret-json=1` parameter**
```
[
    {
        "name": "test.txt",
        "id": "4ccd37916552e2943314027931edd0b45240be7c",
        "size": 2987
    },
    {
        "name": "1.jpg",
        "id": "12e07dd00c124fa7ea3b645ff9fe183f73eab2a1",
        "size": 1699246
    }
]
```

**Note**

- New uploaded file name will be 'test(1).text' if a file with name 'test.txt' already exists in parent directory

- For python client uploading, see <https://github.com/haiwen/webapi-examples/blob/master/python/upload-file.py>, or it can be done much more easily with elegant [python requests library](http://docs.python-requests.org/en/latest/), see <https://github.com/haiwen/webapi-examples/blob/master/python/upload-file2.py>

**Errors**

    400 Bad request
    440 Invalid filename
    500 Internal server error

### <a id="resumable-upload-file"></a>Resumable Upload File

Can only be used when size of file to be uploaded bigger than 100MB.

#### <a id="resumable-check-if-enabled"></a>Check If Enable Resumable Upload

**GET** http://192.168.1.113:8000/api/v2.1/repos/{repo_id}/file-uploaded-bytes/?parent_dir={parent_dir}&file_name={file_name}

**Request parameters**

* repo_id
* parent_dir
* file_name

**Sample request**

```
curl -v -H 'Authorization: Token e71c00e93af863ba9bcddb61a46bb4de11d713fc' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.113:8000/api/v2.1/repos/09b7d3c0-5f0d-49be-9318-7ca136f386cd/file-uploaded-bytes/?parent_dir=/&file_name=test.md"
```

**Sample response**

```
*   Trying 192.168.1.113...
* Connected to 192.168.1.113 (192.168.1.113) port 8000 (#0)
> GET /api/v2.1/repos/09b7d3c0-5f0d-49be-9318-7ca136f386cd/file-uploaded-bytes/?parent_dir=/&file_name=test.md HTTP/1.1
> Host: 192.168.1.113:8000
> User-Agent: curl/7.50.1
> Authorization: Token e71c00e93af863ba9bcddb61a46bb4de11d713fc
> Accept: application/json; charset=utf-8; indent=4
>
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Date: Fri, 01 Jun 2018 08:59:27 GMT
< Server: WSGIServer/0.1 Python/2.7.12+
< Content-Length: 26
< Content-Language: en
< Accept-Ranges: bytes
< Vary: Accept, Accept-Language, Cookie
< Allow: GET, HEAD, OPTIONS
< Content-Type: application/json; charset=utf-8; indent=4
<
{
    "uploadedBytes": 0
* Closing connection 0
}
```

If the response has this header `Accept-Ranges: bytes`, means that Seafile server supports resumable upload file.

**Errors**

- 400 parent_dir/file_name invalid.
- 404 Library/Folder not found.
- 500 Internal server error

#### <a id="resumable-get-upload-link"></a>Get Upload Link

Same as <a href="#get-upload-link">Get Upload Link</a>

#### <a id="resumable-get-bytes-already-upload"></a>Get Bytes Already Uploaded

**GET** http://192.168.1.113:8000/api/v2.1/repos/{repo_id}/file-uploaded-bytes/?parent_dir={parent_dir}&file_name={file_name}

**Request parameters**

* repo_id
* parent_dir
* file_name

**Sample request**

```
curl -v -H 'Authorization: Token e71c00e93af863ba9bcddb61a46bb4de11d713fc' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.113:8000/api/v2.1/repos/09b7d3c0-5f0d-49be-9318-7ca136f386cd/file-uploaded-bytes/?parent_dir=/path-in-seafile-repo/&file_name=test.md"
```

**Sample response**

File has not been uploaded before.

```
{
    "uploadedBytes": 0
}
```

File has already been uploaded 149946368 bytes. If you want to continue uploading this file, upload it begin with 149946368 bytes.

```
{
    "uploadedBytes": 149946368
}
```

**Errors**

- 400 parent_dir/file_name invalid.
- 404 Library/Folder not found.
- 500 Internal server error

#### <a id="resumable-upload-file-1"></a>Upload File

After getting the upload link and `uploadedBytes`, POST to this link for uploading files.

**POST** http://cloud.seafile.com:8082/upload-api/73c5d117-3bcf-48a0-aa2a-3f48d5274ae3

**Request parameters**

* file: local file path.
* parent_dir : path in your Seafile repo that you want to upload local file to.

**Sample request**

upload file to `/path-in-seafile-repo/`:

```
curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H "Content-Range: bytes 149946368-150994943/1587609600" -F file=@test.md -F parent_dir=/path-in-seafile-repo/ http://cloud.seafile.com:8082/upload-api/73c5d117-3bcf-48a0-aa2a-3f48d5274ae3
```

* `149946368-150994943` means is now uploading 149946368-150994943 bytes.
* `1587609600` is file's total bytes.

Example of Request Payload

```
------WebKitFormBoundaryiUPBhwtLnoqOBFlA
Content-Disposition: form-data; name="parent_dir"

/
------WebKitFormBoundaryiUPBhwtLnoqOBFlA
Content-Disposition: form-data; name="file"; filename="ubuntu-16.04.3-desktop-amd64.iso"
Content-Type: application/x-cd-image

...file content...
```

**Sample response**

```
{
    "success": true
}
```

After the whole file is uploaded, Seafile will do some background index task for this file, it will take time if the file is very large.

If you don't want to wait, you can pass a `need_idx_progress` parameter when you send file upload request.

**Sample request**

upload file to `/path-in-seafile-repo/`:

```
curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H "Content-Range: bytes 149946368-150994943/1587609600" -F file=@test.md -F parent_dir=/path-in-seafile-repo/ "http://cloud.seafile.com:8082/upload-api/73c5d117-3bcf-48a0-aa2a-3f48d5274ae3?need_idx_progress=true"
```

A task id will be returned.

```
b6a30c27-73ea-415f-bff1-cd4025585b00
```

Then, you can use this task id to check the background index task progress.

```
{
    "indexed":602,
    "total":602,
    "status":0,
    "ret_json":"[
        {
            \"name\": \"book.json\",
            \"id\": \"dfb70f907118e0a96c249316281de429d485d8b2\",
            \"size\": 602
        }
    ]"
}
```

Note: You should upload up to 1MB of file content every request.

**Errors**

```
400 Bad request
440 Invalid filename
500 Internal server error
```

### <a id="update-file"></a>Update file

#### <a id="get-update-link"></a>Get Update Link

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/update-link/?p=/update-dir

**Request parameters**

* repo-id
* p (use '/' as default)

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" https://cloud.seafile.com/api2/repos/99b758e6-91ab-4265-b705-925367374cf0/update-link/

**Sample response**

    "http://cloud.seafile.com:8082/update-api/e69e5ee7-9329-4f42-bf1b-12879bd72c28"

**Errors**

    403 Permission denied.
    500 Run out of quota

#### <a id="update-file-1"></a>Update File

After getting the update link, POST to this link for updating files.

**POST** http://cloud.seafile.com:8082/update-api/e69e5ee7-9329-4f42-bf1b-12879bd72c28

**Request parameters**

* target_file

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -F file=@test.txt -F filename=test.txt -F target_file=/test.txt http://cloud.seafile.com:8082/update-api/e69e5ee7-9329-4f42-bf1b-12879bd72c28

**Returns**

The id of the updated file

**Sample response**

    "adc83b19e793491b1c6ea0fd8b46cd9f32e592fc"

**Errors**

- 400 Bad request
- 440 Invalid filename
- 500 Internal server error

### <a id="get-upload-blocks-link"></a>Uploading Large File in Blocks

#### Step 1, POST the block list to Seahub

**POST** https://cloud.seafile.com/api2/repos/{repo-id}/upload-blks-link/?p=/parent-folder-path

**Request parameters**

* `repo-id`.
* `p`, parent folder path, default is `/`.
* `blklist`: string of block ids, seperated by `,`, for example:

**Sample request**

```
curl -H "Authorization: Token 2bac21cab9eb0c4baac10d1e6fc3cf590f0dcf17" -d 'blklist=1faee57feb464aa1f61165722c93a5075d1993ff,0cfc000bbde26a7b9d4754103501af76a7a' http://192.168.1.113:8000/api2/repos/d4f596ed-09ea-4ac6-8d59-12acbd089097/upload-blks-link/?p=/
```

**Sample response**

The response is in json format containing the following fields:

* rawblksurl: the url to upload raw blocks to file server
* commiturl: the url to commit file in file server
* blklist: the block id list of the missing blocks


```
{
    "blklist": [
        "1faee57feb464aa1f61165722c93a5075d1993ff",
        "0cfc000bbde26a7b9d4754103501af76a7a"],
    "commiturl": "http://192.168.1.113:8082/upload-blks-api/8bd0ae30-e543-4e03-84ce-03a3cc79e14a?commitonly=true&ret-json=true",
    "rawblksurl": "http://192.168.1.113:8082/upload-raw-blks-api/8bd0ae30-e543-4e03-84ce-03a3cc79e14a"
}
```

**Errors**

* 403 Permission denied.
* 404 Folder not found.
* 404 Library not found.
* 443 Out of quota.
* 500 Internal Server Error

#### Step 2, upload missing blocks to rawblksurl

```
POST http://server-address:8082/upload-raw-blks-api/<token>
```

**Request parameters**

* filename: file block id.

The content of the request is in multipart form-data format.

```
------WebKitFormBoundaryWWPdItXjNGBDlSuZ
Content-Disposition: form-data; name="file"; filename=<block id>
Content-Type: text/xml


------WebKitFormBoundaryWWPdItXjNGBDlSuZ--
```

Each block is sent in a file field. You should set `filename` attribute to the id of each block.

**Sample request**

```
curl -F file=@1.txt -F filename=1faee57feb464aa1f61165722c93a5075d1993ff https://dev.seafile.com/seafhttp/upload-raw-blks-api/389479a2-01fb-4073-8cd3-8f5115e78fc9
```

**Success**

   Response code 200 if everything is ok

**Errors**

* 400 Invalid URL | Access denied | Duplicate progress id | Invalid Seafile-Content-Range
* 440 Invalid filename
* 441 File already exists
* 442 File size is too large
* 443 Out of quota
* 500 Internal error

### Step 3, let the server to commit the file

```
POST commiturl: `http://server-address:8082/upload-blks-api/<token>?commitonly=true&ret-json=true`
```

The content is in multipart form-data format. Fields and corresponding values are:

**Request parameters**

* parent_dir: parent directory path
* file_name: file name
* file_size: file size in bytes
* replace: whether overwrite file with the same name. 1 for replace, 0 for not replace.
* blockids: block id list of the file in JSON list format

**Sample request**

```
curl -d "parent_dir=/&file_name=1.md&file_size=1234&replace=0&blockids=["1faee57feb464aa1f61165722c93a5075d1993ff","0cfc000bbde26a7b9d4754103501af76a7a36f89"]" -H 'Accept: application/json; charset=utf-8; indent=4' https://dev.seafile.com/seafhttp/upload-blks-api/389479a2-01fb-4073-8cd3-8f5115e78fc9?commitonly=true&ret-json=true
```

**Sample response**

If you set 'ret-json' into url arguments, new_file_id will be returned

```
{
    "id": "4ccd37916552e2943314027931edd0b45240be7c"
}
```

**Errors**

* 400 Invalid URL | Access denied | Duplicate progress id | Invalid Seafile-Content-Range
* 440 Invalid filename
* 441 File already exists
* 442 File size is too large
* 443 Out of quota
* 446 Block missing
* 403 Permission denied
* 500 Internal error

### <a id="get-update-blks-link"></a>Get Update Blocks Link

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/update-blks-link/

**Request parameters**

* repo-id

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" https://cloud.seafile.com/api2/repos/99b758e6-91ab-4265-b705-925367374cf0/update-blks-link/

**Sample response**

    "https://cloud.seafile.com/seafhttp/update-blks-api/402c6d48-fe52-4592-97dd-85f462f03d66"

**Errors**

- 403 Can not access repo
- 520 above quota

### <a id="file-comments"></a>File Comments

#### <a id="get-comment"></a>Get Comment

**GET** https://cloud.seafile.com/api2/repos/{repo_id}/file/comments/{pk}/

* rpeo_id
* pk

**Sample request**

    curl -H "Authorization: Token 05b05e30ee979e333ff33a437988820494fb0afd"  https://cloud.seafile.com/api2/repos/4674c2bb-3702-4dd0-b768-8952db27ac87/file/comments/1/

**Sample response**

    {
        "comment": "welcome",
        "repo_id": "4674c2bb-3702-4dd0-b768-8952db27ac87",
        "item_name": "q",
        "created_at": "2017-10-10T02:42:20+00:00",
        "parent_path": "/",
        "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
        "user_name": "admin",
        "id": 3,
        "user_email": "admin@admin.com",
        "user_contact_email": "admin@admin.com"
    }

**Errors**

* 400 Wrong comment id
* 403 Can not access repo

#### <a id="delete-comment"></a>Delete Comment

**Delete** https://cloud.seafile.com/api2/repos/{repo_id}/file/comments/{pk}/

* rpeo_id
* pk

**Sample request**

    curl -X DELETE -H "Authorization: Token 05b05e30ee979e333ff33a437988820494fb0afd"  https://cloud.seafile.com/api2/repos/4674c2bb-3702-4dd0-b768-8952db27ac87/file/comments/1/

**Sample response**

    None

**Errors**

* 400 Wrong comment id
* 403 Can not access repo
* 403 Permission denied

#### <a id="list-comments"></a>List Comments

**GET** https://cloud.seafile.com/api2/repos/{repo_id}/file/comments/?p=/doc/doc

* rpeo_id
* p

**Sample request**

    curl -H "Authorization: Token 05b05e30ee979e333ff33a437988820494fb0afd"  https://cloud.seafile.com/api2/repos/4674c2bb-3702-4dd0-b768-8952db27ac87/file/comments/?p=%2Fdoc%2Fdoc

**Sample response**

    {
        "comments": [
            {
                "comment": "word",
                "repo_id": "4674c2bb-3702-4dd0-b768-8952db27ac87",
                "item_name": "doc",
                "created_at": "2017-10-11T02:49:42+00:00",
                "parent_path": "/doc",
                "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
                "user_name": "admin",
                "id": 7,
                "user_email": "admin@admin.com",
                "user_contact_email": "admin@admin.com"
            },
            {
                "comment": "help",
                "repo_id": "4674c2bb-3702-4dd0-b768-8952db27ac87",
                "item_name": "doc",
                "created_at": "2017-10-11T02:49:44+00:00",
                "parent_path": "/doc",
                "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
                "user_name": "admin",
                "id": 8,
                "user_email": "admin@admin.com",
                "user_contact_email": "admin@admin.com"
            },
            {
                "comment": "test",
                "repo_id": "4674c2bb-3702-4dd0-b768-8952db27ac87",
                "item_name": "doc",
                "created_at": "2017-10-11T03:32:37+00:00",
                "parent_path": "/doc",
                "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
                "user_name": "admin",
                "id": 10,
                "user_email": "admin@admin.com",
                "user_contact_email": "admin@admin.com"
            }
        ]
    }

**Errors**

* 400 Wrong path
* 403 Can not access repo

#### <a id="post-comments"></a>Post Comments

**POST** https://cloud.seafile.com/api2/repos/{repo_id}/file/comments/?p=/doc/doc

* rpeo_id
* p
* comment

**Sample request**

    curl -X POST -d "comment=hello" -H "Authorization: Token 05b05e30ee979e333ff33a437988820494fb0afd"  https://cloud.seafile.com/api2/repos/4674c2bb-3702-4dd0-b768-8952db27ac87/file/comments/?p=%2Fdoc%2Fdoc

**Sample response**

    {
        "comment": "hello",
        "repo_id": "4674c2bb-3702-4dd0-b768-8952db27ac87",
        "item_name": "doc",
        "created_at": "2017-10-11T06:43:31+00:00",
        "parent_path": "/doc",
        "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
        "user_name": "admin",
        "id": 11,
        "user_email": "admin@admin.com",
        "user_contact_email": "admin@admin.com"
    }

**Errors**

* 400 Wrong path
* 400 Comment can not be empty
* 403 Can not access repo
* 404 File not found
* 500 Internal error


#### <a id="get-number-of-comments"></a>Get Number of Comments

**GET** https://cloud.seafile.com/api2/repos/{repo_id}/file/comments/counts/?p=/doc

* rpeo_id
* p

**Sample request**

`get the number of file comment correspoding to the file under the folder`

    curl -H "Authorization: Token 05b05e30ee979e333ff33a437988820494fb0afd"  -sS 'https://cloud.seafile.com/api2/repos/4674c2bb-3702-4dd0-b768-8952db27ac87/file/comments/counts/?p=/doc'

**Sample response**

    [
        {
            "doc": 3
        },
        {
            "pdfs": 1
        }
    ]

**Errors**

* 400 Wrong path
* 403 Can not access repo
* 404 Folder not found
* 500 Internal error

### <a id="get-smart-link-for-a-file"></a>Get Smart Link for a File

**GET** "http://192.168.1.113:8000/api/v2.1/smart-link/?repo_id={repo_id}&path={path}&is_dir={is_dir}"

**Request parameters**

* `repo_id`
* `path`, path of file/folder.
* `is_dir`, `true` or `false`.

**Sample request for view**

```
curl -H "Authorization: Token 1cb7908b876d9b1708c757a347f2e6346456ab91" -H 'Accept: application/json; indent=4' "http://192.168.1.113:8000/api/v2.1/smart-link/?repo_id=d4f596ed-09ea-4ac6-8d59-12acbd089097&path=/8.md&is_dir=false"
```

**Sample response**

```
{
    "smart_link": "http://192.168.1.113:8000/smart-link/3eb1657f-db82-4329-a05e-9c087022fb2f/8.md"
}
```

**Errors**

* 400 repo_id/path/is_dir invalid.
* 400 is_dir can only be 'true' or 'false'.
* 403 Permission denied.
* 404 Library/Foldef/File/ not found.
* 500 Internal Server Error

## <a id="directory"></a>Directory

### <a id="list-directory-entries"></a>List Directory Entries

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/dir/

* repo-id
* p (optional): The path to a directory. If `p` is missing, then defaults to '/' which is the top directory.
* oid (optional): The object id of the directory. The object id is the checksum of the directory contents.
* t (optional): If set `t` argument as `f`, will only return file entries, and `d` for only dir entries.
* recursive (optional): If set `t` argument as `d` **AND** `recursive` argument as `1`, return all dir entries recursively

**Sample request**

request file/dir list of a folder.

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d9b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/99b758e6-91ab-4265-b705-925367374cf0/dir/?p=/foo

**Sample response**

   If oid is the same as the current oid of the directory, returns `"uptodate"` , else returns

    [
    {
        "id": "0000000000000000000000000000000000000000",
        "type": "file",
        "name": "test1.c",
        "size": 0
    },
    {
        "id": "e4fe14c8cda2206bb9606907cf4fca6b30221cf9",
        "type": "dir",
        "name": "test_dir"
    }
    ]

**Sample request**

request recursive dir list of a folder.

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d9b477fd" -H 'Accept: application/json; indent=4' 'https://cloud.seafile.com/api2/repos/99b758e6-91ab-4265-b705-925367374cf0/dir/?t=d&recursive=1'

**Sample response**

```
[{'id': u'5e307101cad46398fb5fe52d9177836f73c4bae8',
  'mtime': 1471490386,
  'name': u'123',
  'parent_dir': u'/video',
  'permission': u'rw',
  'type': 'dir'},
 {'id': u'0000000000000000000000000000000000000000',
  'mtime': 1471490391,
  'name': u'123-2',
  'parent_dir': u'/video',
  'permission': u'rw',
  'type': 'dir'},
 {'id': u'0000000000000000000000000000000000000000',
  'mtime': 1471490379,
  'name': u'456',
  'parent_dir': u'/video/123',
  'permission': u'rw',
  'type': 'dir'},
 {'id': u'0000000000000000000000000000000000000000',
  'mtime': 1471490386,
  'name': u'456-2',
  'parent_dir': u'/video/123',
  'permission': u'rw',
  'type': 'dir'},
 {'id': u'd8f5f80fbd89bf5634dcf9e21b569c487541d34e',
  'mtime': 1471490391,
  'name': u'video',
  'parent_dir': '/',
  'permission': u'rw',
  'type': 'dir'}
]
```

**Errors**

* 404 The path is not exist.
* 440 Repo is encrypted, and password is not provided.
* 520 Operation failed..

### <a id="get-directory-detail"></a>Get Directory Detail

**GET** http://192.168.1.113:8000/api/v2.1/repos/{repo_id}/dir/detail/?path={path}

* repo_id
* path, should not be `/`.

**Sample request**

```
curl -H "Authorization: Token e71c00e93af863ba9bcddb61a46bb4de11d713fc" -H 'Accept: application/json; indent=4' "http://192.168.1.113:8000/api/v2.1/repos/d4f596ed-09ea-4ac6-8d59-12acbd089097/dir/detail/?path=Develop"
```

**Sample response**

```
{
    "repo_id": "d4f596ed-09ea-4ac6-8d59-12acbd089097",
    "name": "Develop",
    "file_count": 4,
    "dir_count": 1,
    "mtime": "2018-01-05T17:45:41+08:00",
    "path": "/Develop/",
    "size": 397888
}
```

**Errors**

* 400 path invalid.
* 403 Permission denied.
* 404 Folder not found.
* 404 Library not found.
* 500 Internal Server Error

### <a id="create-new-directory"></a>Create New Directory

**POST** https://cloud.seafile.com/api2/repos/{repo-id}/dir/

* repo-id
* p
* operation=mkdir (post)

**Sample request**

    curl -d "operation=mkdir" -v -H 'Authorization: Token 076de58233c09f19e7a5179abff14ad55987350e' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/21b941c2-5411-4372-a514-00b62ab99ef2/dir/?p=/foo

**Sample response**

    ...
    < HTTP/1.0 201 CREATED
    < Location: https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/dir/?p=/foo
    ...

    "success"

**Success**

   Response code 201(Created) is returned, and Location header provides the url of created directory.

**Errors**

* 400 Path is missing or invalid(e.g. p=/)
* 520 Operation failed.

**Notes**

   Newly created directory will be renamed if the name is duplicated.

### <a id="rename-directory"></a>Rename Directory

**POST** https://cloud.seafile.com/api2/repos/{repo-id}/dir/?p=/foo

**Parameters**

* repo-id
* p (path)
* operation=rename
* newname (the new name of the directory)

**Sample request**

    curl -d  "operation=rename&newname=pinkfloyd_newfolder" -v  -H 'Authorization: Tokacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/dir/?p=/foo

**Success**

   Response code 200 if everything is ok

**Errors**

* 403 if You do not have permission to rename a folder
* 400 if newname is not given
* 520 if Failed to rename directory (generic problem)

**Notes**

   If the new name is the same of the old name no operation will be done.

### <a id="delete-directory"></a>Delete Directory

**DELETE** https://cloud.seafile.com/api2/repos/{repo-id}/dir/

* repo-id
* p

**Sample request**

    curl -X DELETE -v  -H 'Authorization: Token f2210dacd3606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/dir/?p=/foo

**Sample response**

    ...
    < HTTP/1.0 200 OK
    ...
    "success"

**Success**

   Response code is 200(OK), and a string `"success"` is returned.

**Errors**

* 400 Path is missing or invalid(e.g. p=/)
* 520 Operation failed.

**Note**

   This can also be used to delete file.

### <a id="download-directory"></a>Download Directory

Perform the following two steps to download directory

##### <a id="download-directory-get-tast-toke"></a>Get Task Token

**GET** https://cloud.seafile.com/api/v2.1/repos/{repo-id}/zip-task/?parent_dir={parent_dir}&dirents={dir}

* repo-id
* parent_dir
* dirents

**Sample request**

    curl -H 'Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a' -H 'Accept: application/json; charset=utf-8; indent=4' "https://cloud.seafile.com/api/v2.1/repos/7460f7ac-a0ff-4585-8906-bb5a57d2e118/zip-task/?parent_dir=/&dirents=my_dir_name"

**Sample response**

    {
        "zip_token": "b2272645-35ee-44ce-8f68-07c022107015"
    }

**Errors**

* 400 parent_dir/dirents invalid.
* 400 Unable to download directory: size is too large.
* 404 Library/Folder not found.
* 403 Permission denied.
* 500 Internal Server Error

### <a id="revert-directory"></a>Revert Directory

**PUT** https://cloud.seafile.com/api2/repos/7460f7ac-a0ff-4585-8906-bb5a57d2e118/dir/revert/

* repo_id
* p
* commit_id

**Sample request**

    curl -X PUT -d "p=/456&commit_id=b1a33768517f65ac7d618ff078dd27855374c7e0" -H 'Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a' -H 'Accept: application/json; charset=utf-8; indent=4' "https://cloud.seafile.com/api2/repos/7460f7ac-a0ff-4585-8906-bb5a57d2e118/dir/revert/"

**Sample response**
```
{
    "success": true
}
```

**Errors**

* 400 path invalid.
* 400 commit_id invalid.
* 404 Library/Folder not found.
* 403 Permission denied.
* 500 Internal Server Error

##### <a id="download-directory-query-task-progress"></a>Query Task Progress

Use the token returned from previous request to check if task progress finished.

**GET** https://cloud.seafile.com/api/v2.1/query-zip-progress/?token={token}

* token

**Sample request**

    curl -H 'Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a' -H 'Accept: application/json; charset=utf-8; indent=4' "https://cloud.seafile.com/api/v2.1/query-zip-progress/?token=b2272645-35ee-44ce-8f68-07c022107015"

**Sample response**

If `zipped` is equal to `total`, means task finished.

    {
        "zipped":2,
        "total":2
    }

**Errors**

* 400 token invalid.
* 500 Internal Server Error

After the task finished, you can manually generate directory download url with the `zip_token`:

    FILE_SERVER_ROOT/zip/{zip_token}

For example, `https://cloud.seafile.com/seafhttp/zip/b2272645-35ee-44ce-8f68-07c022107015` is the final url here.

## <a id="asynchronously-copy-move-file-directory"></a>Asynchronously Copy/Move File/Directory

### <a id="asynchronously-copy-move-file-directory-get-task-id"></a>Get Task Id

**POST** https://cloud.seafile.com/api/v2.1/copy-move-task/

**Request parameters**

* src_repo_id
* src_parent_dir
* src_dirent_name
* dst_repo_id
* dst_parent_dir
* operation, `copy` or `move`
* dirent_type, `file` or `dir`

**Sample request**

Sample for copy file.

```
curl -d "src_repo_id=534258e2-761b-465c-9e2c-56e021d3853f&src_parent_dir=/&src_dirent_name=file.md&dst_repo_id=a3fa768d-0f00-4343-8b8d-07b4077881db&dst_parent_dir=/&operation=copy&dirent_type=file" -H 'Authorization: Token ae265ae599a29c238ca25fb63087859798d5f55d' -H 'Accept: application/json; charset=utf-8; indent=4' 'http://192.168.1.124:8000/api/v2.1/copy-move-task/'
```

**Sample response**

```
{
    "task_id": "d1ca2b8c-8ab8-4dd4-8ad7-842130764484"
}
```

**Errors**

* 400 path/operation/dirent_type invalid.
* 404 Library/Folder not found.
* 403 Permission denied.
* 500 Internal Server Error

### <a id="asynchronously-copy-move-file-directory-cancel-task"></a>Cancel Task

**DELETE** https://cloud.seafile.com/api/v2.1/copy-move-task/

**Request parameters**

* task_id

**Sample request**

```
curl -X DELETE -d "task_id=d1ca2b8c-8ab8-4dd4-8ad7-842130764484" -H 'Authorization: Token ae265ae599a29c238ca25fb63087859798d5f55d' -H 'Accept: application/json; charset=utf-8; indent=4' 'http://192.168.1.124:8000/api/v2.1/copy-move-task/'
```

**Sample response**

```
{
    "success": true
}
```

**Errors**

* 400 task_id invalid.
* 500 Internal Server Error

### <a id="asynchronously-copy-move-file-directory-query-progress"></a>Query Progress

**GET** https://cloud.seafile.com/api/v2.1/query-copy-move-progress/

**Request parameters**

* task_id

**Sample request**

```
curl -H 'Authorization: Token ae265ae599a29c238ca25fb63087859798d5f55d' -H 'Accept: application/json; charset=utf-8; indent=4' 'http://192.168.1.124:8000/api/v2.1/query-copy-move-progress/?task_id=d1ca2b8c-8ab8-4dd4-8ad7-842130764484'
```

**Sample response**

```
{
    "successful": true,
    "canceled": false,
    "total": 1,
    "done": 1,
    "failed": false
}
```

**Errors**

* 400 task_id invalid.
* 500 Internal Server Error

## <a id="multiple-files-directories"></a>Multiple Files / Directories

### <a id="multiple-files-directories-copy"></a>Copy

**POST** https://cloud.seafile.com/api2/repos/{repo_id}/fileops/copy/

**Request parameters**

* p: source folder path, defaults to `"/"`
* file_names: list of file/folder names to copy. Multiple file/folder names can be seperated by `:`.
* dst_repo: the destination repo id
* dst_dir: the destination folder in `dst_repo`

**Sample request**

    curl -d "dst_repo=bdf816e6-aba8-468c-962f-77c2fcfd1d1c&dst_dir=/1&file_names=1.md:2.md:test" -H 'Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154' -H 'Accept: application/json; indent=4' "https://cloud.seafile.com/api2/repos/bdf816e6-aba8-468c-962f-77c2fcfd1d1c/fileops/copy/?p=/1/test-2"

**Sample response**
```
[
    {
        "repo_id": "bdf816e6-aba8-468c-962f-77c2fcfd1d1c",
        "parent_dir": "/1",
        "obj_name": "1 (2).md"
    },
    {
        "repo_id": "bdf816e6-aba8-468c-962f-77c2fcfd1d1c",
        "parent_dir": "/1",
        "obj_name": "2 (2).md"
    },
    {
        "repo_id": "bdf816e6-aba8-468c-962f-77c2fcfd1d1c",
        "parent_dir": "/1",
        "obj_name": "test (2)"
    }
]
```

**Errors**

* 400 missing argument
* 403 You do not have permission to copy file
* 404 repo not found
* 502 failed to copy file

### <a id="multiple-files-directories-move"></a>Move

**POST** https://cloud.seafile.com/api2/repos/{repo_id}/fileops/move/

**Request parameters**

* p: source folder path, defaults to `"/"`
* file_names: list of file/folder names to move. Multiple file/folder names can be seperated by `:`.
* dst_repo: the destination repo id
* dst_dir: the destination folder in `dst_repo`

**Sample request**

    curl -d "dst_repo=bdf816e6-aba8-468c-962f-77c2fcfd1d1c&dst_dir=/1&file_names=1.md:2.md:test" -H 'Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154' -H 'Accept: application/json; indent=4' "https://cloud.seafile.com/api2/repos/bdf816e6-aba8-468c-962f-77c2fcfd1d1c/fileops/move/?p=/1/test-2"

**Sample response**
```
[
    {
        "repo_id": "bdf816e6-aba8-468c-962f-77c2fcfd1d1c",
        "parent_dir": "/1",
        "obj_name": "1 (3).md"
    },
    {
        "repo_id": "bdf816e6-aba8-468c-962f-77c2fcfd1d1c",
        "parent_dir": "/1",
        "obj_name": "2 (3).md"
    },
    {
        "repo_id": "bdf816e6-aba8-468c-962f-77c2fcfd1d1c",
        "parent_dir": "/1",
        "obj_name": "test (3)"
    }
]
```

**Errors**

* 400 missing argument
* 403 You do not have permission to move file
* 404 repo not found
* 502 failed to move file

### <a id="multiple-files-directories-delete"></a>Delete

**POST** https://cloud.seafile.com/api2/repos/{repo_id}/fileops/delete/

**Request parameters**

* p: source folder path, defaults to `"/"`
* file_names: list of file/folder names to delete. Multiple file/folder names can be seperated by `:`.

**Sample request**

    curl -d "file_names=foo.c:bar.c:dir1:dir2" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' https://cloud.seafile.com/api2/repos/c7436518-5f46-4296-97db-2fcba4c8c8db/fileops/delete/?p=src_path

**Sample response**

    "success"

**Errors**

* 400 missing argument
* 403 You do not have permission to delete file
* 404 repo not found
* 502 failed to delete file

### <a id="multiple-files-directories-download"></a>Download

Perform the following two steps to download multiple files and directories.

##### <a id="multiple-files-directories-get-tast-toke"></a>Get Task Token

**GET** https://cloud.seafile.com/api/v2.1/repos/{repo-id}/zip-task/?parent_dir={parent_dir}&dirents={dir,file}

* repo-id
* parent_dir
* dirents

**Sample request**

    curl -H 'Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a' -H 'Accept: application/json; charset=utf-8; indent=4' "https://cloud.seafile.com/api/v2.1/repos/7460f7ac-a0ff-4585-8906-bb5a57d2e118/zip-task/?parent_dir=/&dirents=my_dir_name&dirents=my_file_name"

**Sample response**

    {
        "zip_token": "b2272645-35ee-44ce-8f68-07c022107015"
    }

**Errors**

* 400 parent_dir/dirents invalid.
* 400 Unable to download directory: size is too large.
* 404 Library/Folder not found.
* 403 Permission denied.
* 500 Internal Server Error

##### <a id="multiple-files-directories-query-task-progress"></a>Query Task Progress

Use the token returned from previous request to check if task progress finished.

**GET** https://cloud.seafile.com/api/v2.1/query-zip-progress/?token={token}

* token

**Sample request**

    curl -H 'Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a' -H 'Accept: application/json; charset=utf-8; indent=4' "https://cloud.seafile.com/api/v2.1/query-zip-progress/?token=b2272645-35ee-44ce-8f68-07c022107015"

**Sample response**

If `zipped` is equal to `total`, means task finished.

    {
        "zipped":2,
        "total":2
    }

**Errors**

* 400 token invalid.
* 500 Internal Server Error

After the task finished, you can manually generate directory download url with the `zip_token`:

    FILE_SERVER_ROOT/zip/{zip_token}

For example, `https://cloud.seafile.com/seafhttp/zip/b2272645-35ee-44ce-8f68-07c022107015` is the final url here.

## <a id="avatar"></a>Avatar

### <a id="update-user-avatar"></a>Update User Avatar

**POST** https://cloud.seafile.com/api/v2.1/user-avatar/

**Request parameters**

* `avatar`: image file

**Sample request**

    curl -H "Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154" -F "avatar=@1.jpg" https://cloud.seafile.com/api/v2.1/user-avatar/

**Sample response**

    {"success": true}

**Errors**

* 400 invalid file extension
* 400 file is too big
* 500 Internal Server Error

### <a id="get-user-avatar"></a>Get User Avatar

**GET** https://cloud.seafile.com/api2/avatars/user/{user}/resized/{size}/

**Request parameters**

* user
* size

**Sample request**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/avatars/user/user@example.com/resized/80/"

**Sample response**

    {
        "url": "http://127.0.0.1:8000/media/avatars/default.png",
        "is_default": true,
        "mtime": 0
    }

### <a id="get-group-avatar"></a>Get Group Avatar

**GET** https://cloud.seafile.com/api2/avatars/group/{group_id}/resized/{size}/

**Request parameters**

* group_id
* size

**Sample request**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/avatars/group/1/resized/80/"

**Sample response**

    {
        "url": "http://127.0.0.1:8000/media/avatars/groups/default.png",
        "is_default": true,
        "mtime": 0
    }

## <a id="devices"></a>Devices

### <a id="get-user-devices"></a>Get User Devices

**GET** https://cloud.seafile.com/api2/devices/

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/devices/

**Sample response**

```
[
    {
        "synced_repos": [
            {
                "repo_id": "47945b31-dedb-4b92-a048-32bf825595ce",
                "sync_time": 1458008928,
                "repo_name": "wopi"
            },
            {
                "repo_id": "78c620ee-2989-4427-8eff-7748f4fbebc0",
                "sync_time": 1457943466,
                "repo_name": "lib-of-lian"
            }
        ],
        "last_accessed": "2016-03-15T10:28:48+08:00",
        "device_name": "lian",
        "platform_version": "",
        "platform": "linux",
        "user": "lian@lian.com",
        "key": "99abe1a7cc7d614db0bfa19db81e42ef675abe4f",
        "client_version": "5.0.0",
        "last_login_ip": "192.168.1.16",
        "device_id": "be10980211752515053bf9036a13139375de0cc8"
    },
    {
        "last_accessed": "2016-03-15T13:59:51+08:00",
        "device_name": "PLK-AL10",
        "platform_version": "5.0.2",
        "platform": "android",
        "user": "lian@lian.com",
        "key": "067051c94163ed193f2131d48c61882daa7cb238",
        "client_version": "2.0.3",
        "last_login_ip": "192.168.1.208",
        "device_id": "4a0d62c1f27b3b74"
    }
]
```

**Errors**

* 401 UNAUTHORIZED

### <a id="unlink-user-device"></a>Unlink User Device

**DELETE** https://cloud.seafile.com/api2/devices/

**Request parameters**

* platform
* device_id

**Sample request**

    curl -X DELETE -d "platform=linux&device_id=be10980211752515053bf9036a13139375de0cc8" -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/devices/

**Sample response**

    {"success": true}

**Errors**

* 400 platform invalid
* 400 device_id invalid
* 500 Internal Server Error

## <a id="snapshot-label"></a>Snapshot Label

### <a id="get-snapshot-label"></a>Get Snapshot Label

**GET** https://cloud.seafile.com/api/v2.1/revision-tags/tag-names/

**Sample request**

Sample for get snapshot label

```
curl -H 'Authorization: Token 88aaa1e6fe35d0444868b4c67f8ca1766cf82f55' -H 'Accept: application/json; indent=4' http://cloud.seafile.com/api/v2.1/revision-tags/tag-names/
```

**Sample response**

```
[
    "q1",
    "qwe",
    "qwe",
    "qwe_-.12",
    "qwe_-1.",
    "r",
    "r",
    "v3",
    "\u4e2d\u6587",
    "\u82f1\u6587"
]
```

### <a id="create-new-snapshot-label"></a>Create New Snapshot Label

**POST** https://cloud.seafile.com/api/v2.1/revision-tags/tagged-items/

**Request parameters**
* repo_id
* commit_id, optional
* tag_names

**Sample request**

Sample for create snapshot label.

```
curl -d "repo_id=7377c95d-b303-4914-a555-306651cc4cbf&commit_id=4c03938da11e83d6c1d3e8ff469e92f46a80eeaf&tag_names=v2.1,v2.2" -H 'Authorization: Token 88aaa1e6fe35d0444868b4c67f8ca1766cf82f55' -H 'Accept: application/json; indent=4' http://cloud.seafile.com/api/v2.1/revision-tags/tagged-items/
```

**Sample response**

```
{
    "revisionTags": [
        {
            "tag": "v2.1",
            "tag_creator": "foo@foo.com",
            "revision": {
                "commit_id": "4c03938da11e83d6c1d3e8ff469e92f46a80eeaf",
                "repo_id": "7377c95d-b303-4914-a555-306651cc4cbf",
                "contact_email": "foo@foo.com",
                "name": "foo",
                "time": "2017-09-13T15:20:54+08:00",
                "link": "/repo/history/view/7377c95d-b303-4914-a555-306651cc4cbf/?commit_id=4c03938da11e83d6c1d3e8ff469e92f46a80eeaf",
                "email": "foo@foo.com",
                "description": "Added \"ca (1).js\"."
            }
        },
        {
            "tag": "v2.2",
            "tag_creator": "foo@foo.com",
            "revision": {
                "commit_id": "4c03938da11e83d6c1d3e8ff469e92f46a80eeaf",
                "repo_id": "7377c95d-b303-4914-a555-306651cc4cbf",
                "contact_email": "foo@foo.com",
                "name": "foo",
                "time": "2017-09-13T15:20:54+08:00",
                "link": "/repo/history/view/7377c95d-b303-4914-a555-306651cc4cbf/?commit_id=4c03938da11e83d6c1d3e8ff469e92f46a80eeaf",
                "email": "foo@foo.com",
                "description": "Added \"ca (1).js\"."
            }
        }
    ]
}
```

**Errors**

* 400 repo_id/commit_id/tag_names invalid.
* 403 Permission denied(need rw permission).

### <a id="update-snapshot-label"></a>Update Snapshot Label

**PUT** https://cloud.seafile.com/api/v2.1/revision-tags/tagged-items/

**Request parameters**
* repo_id
* commit_id(default is head commit if commit_id is empty)
* tag_names

**Sample request**

Sample for update snapshot label.

```
curl -X PUT -d "repo_id=7377c95d-b303-4914-a555-306651cc4cbf&commit_id=4c03938da11e83d6c1d3e8ff469e92f46a80eeaf&tag_names=v3" -H 'Authorization: Token 88aaa1e6fe35d0444868b4c67f8ca1766cf82f55' -H 'Accept: application/json; indent=4' http://cloud.seafile.com/api/v2.1/revision-tags/tagged-items/
```

**Sample response**

```
{
    "revisionTags": [
        {
            "tag": "v3",
            "tag_creator": "foo@foo.com",
            "revision": {
                "commit_id": "4c03938da11e83d6c1d3e8ff469e92f46a80eeaf",
                "repo_id": "7377c95d-b303-4914-a555-306651cc4cbf",
                "contact_email": "foo@foo.com",
                "name": "foo",
                "time": "2017-09-13T15:20:54+08:00",
                "link": "/repo/history/view/7377c95d-b303-4914-a555-306651cc4cbf/?commit_id=4c03938da11e83d6c1d3e8ff469e92f46a80eeaf",
                "email": "foo@foo.com",
                "description": "Added \"ca (1).js\"."
            }
        }
    ]
}
```

**Errors**

* 400 repo_id/commit_id/tag_names invalid.
* 403 Permission denied(need rw permission).

### <a id="delete-snapshot-label"></a>Delete Snapshot Label
**Delete** https://cloud.seafile.com/api/v2.1/revision-tags/tagged-items/

**Request parameters**
* repo_id
* tag_name

**Sample request**

Sample for update snapshot label.

```
curl -X DELETE -H 'Authorization: Token 88aaa1e6fe35d0444868b4c67f8ca1766cf82f55' -H 'Accept: application/json; indent=4' -sS 'http://cloud.seafile.com/api/v2.1/revision-tags/tagged-items/?repo_id=7377c95d-b303-4914-a555-306651cc4cbf&tag_names=v3'
```

**Sample response**

```
{}
```

**Errors**

* 400 repo_id/tag_names invalid.
* 403 Permission denied(need rw permission).

## <a id="get-file-activities"></a>Get File Activities

**GET** https://cloud.seafile.com/api2/events/

**Request parameters**

this api will only return first 15 records of activities. if want get more, pass `start` parameter

* start (default 0)
* size (size of user avatar, default 36)

**Sample request**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/events/"

**Sample response**

```
{'events': [{'author': u'lian@lian.com',
             'avatar': '<img src="/media/avatars/default.png" width="36" height="36" class="avatar" />',
             'avatar_url': 'https://cloud.seafile.com/media/avatars/default.png',
             'date': '2016-05-06',
             'etype': u'repo-delete',
             'name': u'lian',
             'nick': u'lian',
             'repo_id': u'13e2ae06-8927-465b-8f57-319b3a7cfbdd',
             'repo_name': u'2',
             'time': 1462552942,
             'time_relative': u'<time datetime="2016-05-06T16:42:22.967104" is="relative-time" title="Fri, 6 May 2016 16:42:22 +0800" >19 hours ago</time>'},
            {'author': u'lian@lian.com',
             'avatar': '<img src="/media/avatars/default.png" width="36" height="36" class="avatar" />',
             'avatar_url': 'https://cloud.seafile.com/media/avatars/default.png',
             'commit_id': u'1be92d40a1b526863bbf39e8abdae7d317a1195f',
             'converted_cmmt_desc': u'Modified "<a href="/convert_cmmt_desc_link/?repo_id=47945b31-dedb-4b92-a048-32bf825595ce&cmmt_id=1be92d40a1b526863bbf39e8abdae7d317a1195f&nm=excel-view.xlsx" class="normal">excel-view.xlsx</a>"',
             'date': '2016-04-25',
             'desc': u'Modified "excel-view.xlsx"',
             'etype': u'repo-update',
             'more_files': False,
             'name': u'lian',
             'nick': u'lian',
             'repo_encrypted': False,
             'repo_id': u'47945b31-dedb-4b92-a048-32bf825595ce',
             'repo_name': u'wopi',
             'time': 1461569125,
             'time_relative': u'<time datetime="2016-04-25T15:25:25" is="relative-time" title="Mon, 25 Apr 2016 15:25:25 +0800" >11 days ago</time>'}
             ...
             ],
 'more': True,
 'more_offset': 15}
 ```

**Sample request for more activities**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/events/?start=15"

**Sample response for more activities**

```
{'events': [{'author': u'lian@lian.com',
             'avatar': '<img src="/media/avatars/default.png" width="36" height="36" class="avatar" />',
             'avatar_url': 'https://cloud.seafile.com/media/avatars/default.png',
             'date': '2016-05-06',
             'etype': u'repo-delete',
             'name': u'lian',
             'nick': u'lian',
             'repo_id': u'13e2ae06-8927-465b-8f57-319b3a7cfbdd',
             'repo_name': u'2',
             'time': 1462552942,
             'time_relative': u'<time datetime="2016-05-06T16:42:22.967104" is="relative-time" title="Fri, 6 May 2016 16:42:22 +0800" >19 hours ago</time>'},
            {'author': u'lian@lian.com',
             'avatar': '<img src="/media/avatars/default.png" width="36" height="36" class="avatar" />',
             'avatar_url': 'https://cloud.seafile.com/media/avatars/default.png',
             'commit_id': u'1be92d40a1b526863bbf39e8abdae7d317a1195f',
             'converted_cmmt_desc': u'Modified "<a href="/convert_cmmt_desc_link/?repo_id=47945b31-dedb-4b92-a048-32bf825595ce&cmmt_id=1be92d40a1b526863bbf39e8abdae7d317a1195f&nm=excel-view.xlsx" class="normal">excel-view.xlsx</a>"',
             'date': '2016-04-25',
             'desc': u'Modified "excel-view.xlsx"',
             'etype': u'repo-update',
             'more_files': False,
             'name': u'lian',
             'nick': u'lian',
             'repo_encrypted': False,
             'repo_id': u'47945b31-dedb-4b92-a048-32bf825595ce',
             'repo_name': u'wopi',
             'time': 1461569125,
             'time_relative': u'<time datetime="2016-04-25T15:25:25" is="relative-time" title="Mon, 25 Apr 2016 15:25:25 +0800" >11 days ago</time>'}
             ...
             ],
 'more': True,
 'more_offset': 30}
 ```

## <a id="get-thumbnail-image"></a>Get Thumbnail Image

**GET** https://cloud.seafile.com/api2/repos/{repo_id}/thumbnail/

**Request parameters**

* repo_id
* p
* size

**Sample request**

    curl -H 'Authorization: Token 40f9a510a0629430865dc199a3880898ad2e48fc' https://cloud.seafile.com/api2/repos/fbead5d0-4817-4446-92f3-7ac8e6a8e5f5/thumbnail/?p=/5.jpg\&size=123 > thumbnail.png

### <a id="search-user"></a>Search User

**GET** https://cloud.seafile.com/api2/search-user/?q=foo

**Request parameters**

* q

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/search-user/?q=foo

**Sample response**

```
[
    {'avatar_url': 'https://cloud.seafile.com/media/avatars/default.png',
      'contact_email': u'foo@foo.com',
      'email': u'foo@foo.com',
      'name': 'foo'},
    {'avatar_url': 'https://cloud.seafile.com/media/avatars/default.png',
     'contact_email': u'foo-bar@foo-bar.com',
     'email': u'foo-bar@foo-bar.com',
     'name': 'foo-bar'}
]
```

**Errors**

* 400 Argument missing.
* 403 Guest user can not use global address book.


Note: The following APIs are only available since Seafile v5.1.

# <a id="admin-only"></a>Admin Only

## <a id="admin-only-account"></a>Account

### <a id="admin-only-list-accounts"></a>List Accounts

**GET** https://cloud.seafile.com/api2/accounts/

**Request parameters**

* start (default to 0)
* limit (default to 100)
* scope (default None, accepted values: 'LDAP' or 'DB' or 'LDAPImport')

To retrieve all users, just set both `start` and `limit` to `-1`.

If scope parameter is passed then accounts will be searched inside the specific scope, otherwise it will be used the old approach: first LDAP and, if no account is found, DB.

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/accounts/

**Sample response**

    [
    {
        "email": "foo@foo.com"
    },
    {
        "email": "bar@bar.com"
    }
    ]

**Errors**

* 403 Permission error, only administrator can perform this action

### <a id="admin-only-get-account"></a>Get Account Info

**GET** https://cloud.seafile.com/api2/accounts/{email}/

**Request parameters**

**Sample request**

    curl -v -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/accounts/user@mail.com/

**Sample response**

    {
    "is_staff": false,
    "is_active": true,
    "id": 2,
    "create_time": 1356061187741686,
    "usage": 651463187,
    "total": 107374182400,
    "email": "user@mail.com"
    }

**Errors**

* 403 Permission error, only administrator can perform this action

### <a id="admin-only-create-account"></a>Create Account

**PUT** https://cloud.seafile.com/api2/accounts/{email}/

**Request parameters**

* password
* is_staff (defaults to False)
* is_active (defaults to True)

**Sample request**

    curl -v -X PUT -d "password=123456" -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/accounts/newaccount@gmail.com/

**Sample response**

    ...
    < HTTP/1.0 201 CREATED
    < Location: https://cloud.seafile.com/api2/accounts/newaccount@gmail.com/
    ...

    "success"

**Success**

    Response code 201(Created) is returned and the Location header provides shared link.

**Errors**

* 403 Permission error, only administrator can perform this action

### <a id="admin-only-update-account"></a>Update Account

**PUT** https://cloud.seafile.com/api2/accounts/{email}/

**Request parameters**

At least one of followings:

* password
* is_staff
* is_active
* name
* note
* storage, the unit is MB.
* role.

**Sample request**

    curl -v -X PUT -d "password=654321&is_staff=true&storage=100&role=guest" -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/accounts/user@mail.com/

**Sample response**

    ...
    < HTTP/1.0 200 OK
    ...

    "success"

**Success**

    Response code 200(OK) is returned.

**Errors**

* 400 Bad Request, keyword password is required
* 403 Permission error, only administrator can perform this action

### <a id="admin-only-migrate-account"></a>Migrate Account

**POST** https://cloud.seafile.com/api2/accounts/{email}/

**Request parameters**

* op
* to_user this user must exist

**Sample request**

    curl -v -d "op=migrate&to_user=user2@mail.com" -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/accounts/user@mail.com/

**Sample response**

    ...
    < HTTP/1.0 200 OK
    ...

    "success"

**Success**

    Response code 200(OK) is returned.

**Errors**

* 400 Bad Request, arguments are missing or invalid
* 403 Permission error, only administrator can perform this action

### <a id="admin-only-delete-account"></a>Delete Account

**DELETE** https://cloud.seafile.com/api2/accounts/{email}/


**Sample request**

    curl -v -X DELETE -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/accounts/newaccount@gmail.com/

**Sample response**

    "success"

**Errors**

* 403 Permission error, only administrator can perform this action

## <a id="admin-only-devices"></a>Devices

### <a id="admin-only-get-desktop-devices"></a>Get Desktop Devices

Get first page (50 records per page) of desktop devices.

**GET** https://cloud.seafile.com/api/v2.1/admin/devices/?platform=desktop&page=1&per_page=50

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/devices/?platform=desktop&page=1&per_page=50

**Sample response**

```
[
    {'has_next_page': False},
    [
        {
            'last_accessed': '2016-04-11T18:24:29+08:00',
            'last_login_ip': u'192.168.1.210',
            'platform': u'linux',
            'user': u'1@1.com',
            'client_version': u'2.0.4',
            'device_name': u'PLK-AL10',
            'device_id': u'4a0d62c1f27b3b74'
        }
    ]
]
```

**Errors**

* 403 Permission error, only administrator can perform this action

### <a id="admin-only-get-mobile-devices"></a>Get Mobile Devices

Get first page (50 records per page) of mobile devices.

**GET** https://cloud.seafile.com/api/v2.1/admin/devices/?platform=mobile&page=1&per_page=50

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/devices/?platform=mobile&page=1&per_page=50

**Sample response**

```
[
    {'has_next_page': False},
    [
        {
            'last_accessed': '2016-04-11T18:24:29+08:00',
            'last_login_ip': u'192.168.1.210',
            'platform': u'ios',
            'user': u'1@1.com',
            'client_version': u'2.0.4',
            'device_name': u'PLK-AL10',
            'device_id': u'4a0d62c1f27b3b74'
        }
    ]
]
```

**Errors**

* 403 Permission error, only administrator can perform this action

### <a id="admin-only-unlink-user-device"></a>Unlink User Device

**DELETE** https://cloud.seafile.com/api/v2.1/admin/devices/

**Request parameters**

* platform
* device_id
* user

**Sample request**

    curl -X DELETE -d "platform=linux&device_id=be10980211752515053bf9036a13139375de0cc8&user=1@1.com" -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/devices/

**Sample response**

    {"success": true}

**Errors**

* 400 platform invalid
* 400 device_id invalid
* 400 user invalid
* 500 Internal Server Error

### <a id="admin-only-get-device-errors"></a>Get Device Errors

This api is only supported in pro edition.

**GET** https://cloud.seafile.com/api/v2.1/admin/device-errors/

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/device-errors/

**Sample response**

```
[
    {
        'repo_id': u'47945b31-dedb-4b92-a048-32bf825595ce',
        'device_ip': u'192.168.1.124',
        'error_time': '2016-04-13T17:49:11+08:00',
        'device_name': u'lian-ubuntu-1404-64',
        'email': u'1@1.com',
        'client_version': u'5.0.6',
        'error_msg': u'No permission.',
        'repo_name': u'wopi'
    }
]
```

**Errors**

* 403 Feature disabled.
* 500 Internal Server Error

### <a id="admin-only-clean-device-errors"></a>Clean Device Errors

This api is only supported in pro edition.

**DELETE** https://cloud.seafile.com/api/v2.1/admin/device-errors/

**Sample request**

    curl -X DELETE -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/device-errors/

**Sample response**

```
{"success":true}
```

**Errors**

* 403 Feature disabled.
* 500 Internal Server Error

## <a id="admin-only-get-snapshots-by-label"></a>Get Snapshots by Label

**GET** https://cloud.seafile.com/api/v2.1/admin/revision-tags/tagged-items/

**Request parameters**
* user, optional
* repo_id, optional
* tag_name, optional
* tag_contains, optional

**Sample request**

Sample for get snapshots by label

```
curl -H 'Authorization: Token 88aaa1e6fe35d0444868b4c67f8ca1766cf82f55' -H 'Accept: application/json; indent=4' http://cloud.seafile.com/api/v2.1/admin/revision-tags/tagged-items/?repo_id=7377c95d-b303-4914-a555-306651cc4cbf&tag_contains=v
```

**Sample response**

```
[
    {
        "tag": "v3",
        "tag_creator": "foo@foo.com",
        "revision": {
            "commit_id": "4c03938da11e83d6c1d3e8ff469e92f46a80eeaf",
            "repo_id": "7377c95d-b303-4914-a555-306651cc4cbf",
            "contact_email": "foo@foo.com",
            "name": "foo",
            "time": "2017-09-13T15:20:54+08:00",
            "link": "/repo/history/view/7377c95d-b303-4914-a555-306651cc4cbf/?commit_id=4c03938da11e83d6c1d3e8ff469e92f46a80eeaf",
            "email": "foo@foo.com",
            "description": "Added \"ca (1).js\"."
        }
    }
]
```

## <a id="admin-only-default-library"></a>Default Library

### <a id="admin-only-get-user-default-library"></a>Get User Default Library

Available for Seafile v6.0.9+

**GET** https://cloud.seafile.com/api/v2.1/admin/default-library/{user_email}

**Sample request**

    curl -H 'Authorization: Token 024692f8411a656baa2cc2d5ed4cd46177b3b3d0' "https://cloud.seafile.com/api/v2.1/admin/default-library/?user_email=foo@foo.com"

**Sample response**

```
{
    "repo_id":"9e58655f-d2a2-4df9-baa2-5ca50698ad98",
    "exists":true,
    "user_email":"lian@lian.com"
}
```

**Errors**

* 400 user_email invalid.
* 404 User not found.
* 403 Permission error, only administrator can perform this action.
* 500 Internal Server Error

### <a id="admin-only-create-user-default-library"></a>Create User Default Library

Available for Seafile v6.0.9+

**POST** https://cloud.seafile.com/api/v2.1/admin/default-library/

**Sample request**

    curl -d "user_email=foo@foo.com" -H 'Authorization: Token 024692f8411a656baa2cc2d5ed4cd46177b3b3d0' "https://cloud.seafile.com/api/v2.1/admin/default-library/"

**Sample response**

```
{
    "repo_id":"9e58655f-d2a2-4df9-baa2-5ca50698ad98",
    "exists":true,
    "user_email":"lian@lian.com"
}
```

**Errors**

* 400 user_email invalid.
* 403 Permission error, only administrator can perform this action.
* 403 Permission error, user can not create library.
* 404 User not found.
* 500 Internal Server Error

## <a id="admin-only-libraries"></a>Libraries

### <a id="admin-only-get-all-libraries"></a>Get all Libraries

Available for Seafile v6.0.0+

**GET** https://cloud.seafile.com/api/v2.1/admin/libraries/?page=1&per_page=100

Get first page (100 records per page) of libraries.

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/libraries/?page=1&per_page=100

**Sample response**

```
{
    "page_info": {
        "current_page": 1,
        "has_next_page": true
    },
    "repos": [
        {
            "name": null,
            "encrypted": false,
            "file_count": 0,
            "owner": "lian@lian.com",
            "size_formatted": "0 bytes",
            "id": "04df5005-1dfc-4e30-ae55-95ed6559583f",
            "size": 0
        },
        {
            "name": "My Library",
            "encrypted": false,
            "file_count": 161,
            "owner": "lian@lian.com",
            "size_formatted": "25.4 MB",
            "id": "2deffbac-d7be-4ace-b406-efb799083ee9",
            "size": 26617460
        }
        ...
    ]
}
```

**Errors**

* 403 Permission error, only administrator can perform this action

### <a id="admin-only-search-library-by-name"></a>Search Library by Name

Available for Seafile v6.0.0+

**GET** https://cloud.seafile.com/api/v2.1/admin/libraries/?name=file

**Request parameters**

* name

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/libraries/?name=file

**Sample response**
```
{
    "owner": "",
    "repos": [
        {
            "name": "file-preview",
            "encrypted": false,
            "file_count": 25,
            "owner": "lian@lian.com",
            "size_formatted": "10.9 MB",
            "id": "6ce1383b-ed1c-45c7-ab31-a13b64471e64",
            "size": 11437897
        }
    ],
    "name": "file"
}
```

**Errors**

* 403 Permission error, only administrator can perform this action


### <a id="admin-only-search-library-by-owner"></a>Search Library by Owner

Available for Seafile v6.0.0+

**GET** https://cloud.seafile.com/api/v2.1/admin/libraries/?owner=lian@lian.com

**Request parameters**

* owner

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/libraries/?owner=lian@lian.com

**Sample response**
```
{
    "owner": "lian@lian.com",
    "repos": [
        {
            "name": "lib-of-lian",
            "encrypted": false,
            "file_count": 0,
            "owner": "lian@lian.com",
            "size_formatted": "16.5 KB",
            "id": "78c620ee-2989-4427-8eff-7748f4fbebc0",
            "size": 16883
        },
        {
            "name": "encrypted",
            "encrypted": true,
            "file_count": 0,
            "owner": "lian@lian.com",
            "size_formatted": "18.1 MB",
            "id": "47695bb8-3364-4274-939d-3c5a0df9710c",
            "size": 18997225
        },
        ...
    ],
    "name": ""
}
```

**Errors**

* 403 Permission error, only administrator can perform this action

### <a id="admin-only-delete-a-library"></a>Delete a Library

Available for Seafile v6.0.0+

**DELETE** https://cloud.seafile.com/api/v2.1/admin/libraries/{repo_id}/

**Sample request**

    curl -X DELETE -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/admin/libraries/ee3b2d19-1a06-47f0-bbfa-554cab3bdedc/

**Sample response**

```
{"success":true}
```

**Errors**

* 403 Permission error, only administrator can perform this action


### <a id="admin-only-transfer-a-library"></a>Transfer a Library

Available for Seafile v6.0.0+

**PUT** https://cloud.seafile.com/api/v2.1/admin/libraries/{repo_id}/

**Sample request**

    curl -X PUT -d "owner=1@1.com" -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/admin/libraries/ee3b2d19-1a06-47f0-bbfa-554cab3bdedc/

**Sample response**

```
{
    "name": "test-repo",
    "encrypted":false,
    "file_count":0,
    "owner":"1@1.com",
    "size_formatted":"0 bytes",
    "id":"ee3b2d19-1a06-47f0-bbfa-554cab3bdedc",
    "size":0
}
```

**Errors**

* 400 owner invalid.
* 403 Permission error, only administrator can perform this action
* 404 User not found.
* 404 Library not found.
* 500 Internal Server Error

### <a id="admin-only-get-library-dirents"></a>Get Library Dirents

**GET** https://cloud.seafile.com/api/v2.1/admin/libraries/{repo_id}/dirents/?parent_dir={parent_dir}

* repo-id
* parent_dir

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/libraries/104f6537-b3a5-4d42-b8b5-8e47e494e4cf/dirents/?parent_dir=/asd

**Sample response**

```
{
    "repo_id": "c474a093-19dc-4ddf-b0b0-72b33214ba33",
    "dirent_list": [
        {
            "file_size": "",
            "last_update": "2016-12-19T03:35:14+00:00",
            "is_file": false,
            "obj_name": "book"
        },
        {
            "file_size": "",
            "last_update": "2016-10-12T07:43:32+00:00",
            "is_file": false,
            "obj_name": "image"
        },
        {
            "file_size": "47.0 KB",
            "last_update": "2017-02-13T02:41:05+00:00",
            "is_file": true,
            "obj_name": "123.md"
        }
    ],
    "is_system_library": false,
    "repo_name": "seacloud.cc.124"
}
```

**Errors**

* 400 parent_dir invalid.
* 403 Feature disabled.
* 403 Permission error, only administrator can perform this action
* 404 Library not found.
* 404 Folder not found.
* 500 Internal Server Error

### <a id="admin-only-get-all-deleted-librares"></a>Get All Deleted Libraries

**GET** http://192.168.1.113:8000/api/v2.1/admin/trash-libraries/

* `page`, default 1.
* `per_page`, default 100.

**Sample request**

```
curl -H 'Authorization: Token 2bac21cab9eb0c4baac10d1e6fc3cf590f0dcf17' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.113:8000/api/v2.1/admin/trash-libraries/"
```

**Sample response**

```
{
    "page_info": {
        "current_page": 1,
        "has_next_page": false
    },
    "repos": [
        {
            "owner": "1@1.com",
            "delete_time": "2018-06-04T17:24:55+08:00",
            "name": "a-stor-2",
            "id": "ed46b580-8df7-4a2b-bb45-c3d179cfc668"
        },
        {
            "owner": "1@1.com",
            "delete_time": "2018-06-04T17:24:54+08:00",
            "name": "a-st",
            "id": "560d9b7b-fd24-4ce3-9e4a-20a953bee1b9"
        },
        {
            "owner": "lian@lian.com",
            "delete_time": "2018-06-04T17:21:35+08:00",
            "name": "dst",
            "id": "09b7d3c0-5f0d-49be-9318-7ca136f386cd"
        },
        {
            "owner": "lian@lian.com",
            "delete_time": "2018-06-04T17:21:32+08:00",
            "name": "k",
            "id": "fbf4b69c-5a46-41a3-a9a3-58c1274ec536"
        },
        {
            "owner": "lian@lian.com",
            "delete_time": "2018-06-04T17:21:29+08:00",
            "name": "src",
            "id": "d4aac5b9-28d4-4372-a4b3-d6de171402df"
        }
    ]
}
```

**Errors**

* 403 Permission error, only administrator can perform this action
* 500 Internal Server Error


### <a id="admin-only-get-deleted-librares-by-owner"></a>Get Deleted Libraries by Owner

**GET** http://192.168.1.113:8000/api/v2.1/admin/trash-libraries/?owner={owner}

* `owner`, library owner's email.

**Sample request**

```
curl -H 'Authorization: Token 2bac21cab9eb0c4baac10d1e6fc3cf590f0dcf17' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.113:8000/api/v2.1/admin/trash-libraries/?owner=1@1.com"
```

**Sample response**

```
{
    "repos": [
        {
            "owner": "1@1.com",
            "delete_time": "2018-06-04T17:24:55+08:00",
            "name": "a-stor-2",
            "id": "ed46b580-8df7-4a2b-bb45-c3d179cfc668"
        },
        {
            "owner": "1@1.com",
            "delete_time": "2018-06-04T17:24:54+08:00",
            "name": "a-st",
            "id": "560d9b7b-fd24-4ce3-9e4a-20a953bee1b9"
        }
    ],
    "search_owner": "1@1.com"
}
```

**Errors**

* 403 Permission error, only administrator can perform this action
* 500 Internal Server Error

### <a id="admin-only-clean-deleted-library"></a>Clean Deleted Library

**DELETE** http://192.168.1.113:8000/api/v2.1/admin/trash-libraries/{repo_id}/

* `repo_id`, deleted library's id.

**Sample request**

```
curl -X DELETE -H 'Authorization: Token 2bac21cab9eb0c4baac10d1e6fc3cf590f0dcf17' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.113:8000/api/v2.1/admin/trash-libraries/560d9b7b-fd24-4ce3-9e4a-20a953bee1b9/"
```

**Sample response**

```
{
    "success": true
}
```

**Errors**

* 403 Permission error, only administrator can perform this action
* 500 Internal Server Error

### <a id="admin-only-restore-deleted-library"></a>Restore Deleted Library

**PUT** http://192.168.1.113:8000/api/v2.1/admin/trash-libraries/d4aac5b9-28d4-4372-a4b3-d6de171402df/

* `repo_id`, deleted library's id.

**Sample request**

```
curl -X PUT -H 'Authorization: Token 2bac21cab9eb0c4baac10d1e6fc3cf590f0dcf17' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.113:8000/api/v2.1/admin/trash-libraries/d4aac5b9-28d4-4372-a4b3-d6de171402df/"
```

**Sample response**

```
{
    "success": true
}
```

**Errors**

* 403 Permission error, only administrator can perform this action
* 404 Library does not exist in trash.
* 500 Internal Server Error

### <a id="admin-only-clean-all-deleted-libraries"></a>Clean ALl Deleted Libraries

**DELETE** http://192.168.1.113:8000/api/v2.1/admin/trash-libraries/

**Sample request**

```
curl -X DELETE -H 'Authorization: Token 2bac21cab9eb0c4baac10d1e6fc3cf590f0dcf17' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.113:8000/api/v2.1/admin/trash-libraries/"
```

**Sample response**

```
{
    "success": true
}
```

**Errors**

* 403 Permission error, only administrator can perform this action
* 500 Internal Server Error

## <a id="admin-only-shares"></a>Shares

### <a id="admin-only-get-repo-user-shares"></a>Get Repo User Shares

Available for Seafile v6.0.1+

**GET** https://cloud.seafile.com/api/v2.1/admin/shares/?repo_id={repo_id)&share_type={share_type}

**Request parameters**

* repo_id
* share_type

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' 'https://cloud.seafile.com/api/v2.1/admin/shares/?repo_id=ddd42241-e003-425d-960e-0f9f7144866f&share_type=user'

**Sample response**

```
[
    {
        "repo_id": "ddd42241-e003-425d-960e-0f9f7144866f",
        "share_type": "user",
        "permission": "r",
        "path": "/",
        "user_name": "name of user 2",
        "user_email": "2@2.com"
    }
]
```

**Errors**

* 400 repo_id invalid.
* 400 share_type invalid.
* 403 Permission denied.
* 404 Library not found.
* 404 Folder not found.
* 500 Internal Server Error

### <a id="admin-only-get-repo-group-shares"></a>Get Repo Group Shares

Available for Seafile v6.0.1+

**GET** https://cloud.seafile.com/api/v2.1/admin/shares/?repo_id={repo_id)&share_type={share_type}

**Request parameters**

* repo_id
* share_type

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' 'https://cloud.seafile.com/api/v2.1/admin/shares/?repo_id=ddd42241-e003-425d-960e-0f9f7144866f&share_type=group'

**Sample response**

```
[
    {
        "repo_id": "ddd42241-e003-425d-960e-0f9f7144866f",
        "share_type": "group",
        "permission": "rw",
        "group_name": "group-of-lian-2",
        "path": "/",
        "group_id": 2
    }
]
```

**Errors**

* 400 repo_id invalid.
* 400 share_type invalid.
* 403 Permission denied.
* 404 Library not found.
* 404 Folder not found.
* 500 Internal Server Error

### <a id="admin-only-share-repo-to-user"></a>Share Repo to User

Available for Seafile v6.0.1+

**POST** https://cloud.seafile.com/api/v2.1/admin/shares/

**Request parameters**

* repo_id
* share_type
* share_to (user email)
* permission

**Sample request**

    curl -d "repo_id=ddd42241-e003-425d-960e-0f9f7144866f&share_type=user&permission=r&share_to=1@1.com&share_to=invalid@email.com" -H "Authorization: Token 9c845638b855e549c07ff81be2a0471aa52810d7" -H 'Accept: application/json; indent=4' 'https://cloud.seafile.com/api/v2.1/admin/shares/'

**Sample response**

```
{
    "failed": [
        {
            "error_msg": "User invalid@email.com not found.",
            "user_email": "invalid@email.com"
        }
    ],
    "success": [
        {
            "repo_id": "ddd42241-e003-425d-960e-0f9f7144866f",
            "share_type": "user",
            "permission": "r",
            "path": "/",
            "user_name": "name of user 1",
            "user_email": "1@1.com"
        }
    ]
}
```

**Errors**

* 400 repo_id invalid.
* 400 share_type invalid.
* 403 Permission denied.
* 404 Library not found.
* 404 Folder not found.
* 500 Internal Server Error

### <a id="admin-only-share-repo-to-group"></a>Share Repo to Group

Available for Seafile v6.0.1+

**POST** https://cloud.seafile.com/api/v2.1/admin/shares/

**Request parameters**

* repo_id
* share_type
* share_to (group_id)
* permission

**Sample request**

    curl -d "repo_id=ddd42241-e003-425d-960e-0f9f7144866f&share_type=group&permission=r&share_to=1&share_to=1232" -H "Authorization: Token 9c845638b855e549c07ff81be2a0471aa52810d7" -H 'Accept: application/json; indent=4' 'https://cloud.seafile.com/api/v2.1/admin/shares/'

**Sample response**

```
{
    "failed": [
        {
            "group_id": 1232,
            "error_msg": "Group %s not found"
        }
    ],
    "success": [
        {
            "repo_id": "ddd42241-e003-425d-960e-0f9f7144866f",
            "share_type": "group",
            "permission": "r",
            "group_name": "group-of-lian",
            "path": "/",
            "group_id": 1
        }
    ]
}
```

**Errors**

* 400 repo_id invalid.
* 400 share_type invalid.
* 403 Permission denied.
* 404 Library not found.
* 404 Folder not found.
* 500 Internal Server Error

### <a id="admin-only-modify-repo-user-share-permission"></a>Modify Repo User Share Permission

Available for Seafile v6.0.1+

**PUT** https://cloud.seafile.com/api/v2.1/admin/shares/

**Request parameters**

* repo_id
* share_type
* share_to (user email)
* permission

**Sample request**

    curl -X PUT -d "repo_id=ddd42241-e003-425d-960e-0f9f7144866f&share_type=user&permission=rw&share_to=1@1.com" -H "Authorization: Token 9c845638b855e549c07ff81be2a0471aa52810d7" -H 'Accept: application/json; indent=4' 'https://cloud.seafile.com/api/v2.1/admin/shares/'

**Sample response**

```
{
    "repo_id": "ddd42241-e003-425d-960e-0f9f7144866f",
    "share_type": "user",
    "permission": "rw",
    "path": "/",
    "user_name": "name of user 1",
    "user_email": "1@1.com"
}
```

**Errors**

* 400 repo_id invalid.
* 400 share_type invalid.
* 403 Permission denied.
* 404 Library not found.
* 404 Folder not found.
* 500 Internal Server Error

### <a id="admin-only-modify-repo-group-share-permission"></a>Modify Repo Group Share Permission

Available for Seafile v6.0.1+

**PUT** https://cloud.seafile.com/api/v2.1/admin/shares/

**Request parameters**

* repo_id
* share_type
* share_to (group_id)
* permission

**Sample request**

    curl -X PUT -d "repo_id=ddd42241-e003-425d-960e-0f9f7144866f&share_type=group&permission=rw&share_to=1" -H "Authorization: Token 9c845638b855e549c07ff81be2a0471aa52810d7" -H 'Accept: application/json; indent=4' 'https://cloud.seafile.com/api/v2.1/admin/shares/'

**Sample response**

```
{
    "repo_id": "ddd42241-e003-425d-960e-0f9f7144866f",
    "share_type": "group",
    "permission": "rw",
    "group_name": "group-of-lian",
    "path": "/",
    "group_id": 1
}
```

**Errors**

* 400 repo_id invalid.
* 400 share_type invalid.
* 403 Permission denied.
* 404 Library not found.
* 404 Folder not found.
* 500 Internal Server Error

### <a id="admin-only-delete-repo-user-share"></a>Delete Repo User Share

Available for Seafile v6.0.1+

**DELETE** https://cloud.seafile.com/api/v2.1/admin/shares/

**Request parameters**

* repo_id
* share_type
* share_to (user email)

**Sample request**

    curl -X DELETE -d "repo_id=ddd42241-e003-425d-960e-0f9f7144866f&share_type=user&share_to=1@1.com" -H "Authorization: Token 9c845638b855e549c07ff81be2a0471aa52810d7" -H 'Accept: application/json; indent=4' 'https://cloud.seafile.com/api/v2.1/admin/shares/'

**Sample response**

```
{
    "success": true
}
```

**Errors**

* 400 repo_id invalid.
* 400 share_type invalid.
* 403 Permission denied.
* 404 Library not found.
* 404 Folder not found.
* 500 Internal Server Error

### <a id="admin-only-delete-repo-group-share"></a>Delete Repo Group Share

Available for Seafile v6.0.1+

**DELETE** https://cloud.seafile.com/api/v2.1/admin/shares/

**Request parameters**

* repo_id
* share_type
* share_to (group id)

**Sample request**

    curl -X DELETE -d "repo_id=ddd42241-e003-425d-960e-0f9f7144866f&share_type=group&share_to=1" -H "Authorization: Token 9c845638b855e549c07ff81be2a0471aa52810d7" -H 'Accept: application/json; indent=4' 'https://cloud.seafile.com/api/v2.1/admin/shares/'

**Sample response**

```
{
    "success": true
}
```

**Errors**

* 400 repo_id invalid.
* 400 share_type invalid.
* 403 Permission denied.
* 404 Library not found.
* 404 Folder not found.
* 500 Internal Server Error

## <a id="admin-only-groups"></a>Groups

### <a id="admin-only-get-all-groups"></a>Get all groups

Available for Seafile v6.0.0+

**GET** https://cloud.seafile.com/api/v2.1/admin/groups/?page=1&per_page=100

Get first page (100 records per page) of groups.

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/groups/?page=1&per_page=100

**Sample response**

```
{
    "page_info": {
        "current_page": 1,
        "has_next_page": true
    },
    "groups": [
        {
            "owner": "test@test.com",
            "created_at": "2016-08-01T16:58:14+08:00",
            "id": 1476,
            "name": "test_group"
        },
        {
            "owner": "1@1.com",
            "created_at": "2016-08-02T16:48:14+08:00",
            "id": 1486,
            "name": "group"
        }
        ...
    ]
}
```

**Errors**

* 403 Permission error, only administrator can perform this action

### <a id="admin-only-delete-a-group"></a>Delete a Group

Available for Seafile v6.0.0+

**DELETE** https://cloud.seafile.com/api/v2.1/admin/groups/{group_id}/

**Sample request**

    curl -X DELETE -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/admin/groups/1486/

**Sample response**

```
{"success":true}
```

**Errors**

* 403 Permission error, only administrator can perform this action

### <a id="admin-only-transfer-a-group"></a>Transfer a Group

Available for Seafile v6.0.0+

**PUT** https://cloud.seafile.com/api/v2.1/admin/groups/{group_id}/

**Sample request**

    curl -X PUT -d "new_owner=1@1.com" -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/admin/groups/1528/

**Sample response**

```
{
    "owner": "1@1.com",
    "created_at": "2016-08-04T17:34:05+08:00",
    "id": 1528,
    "name": "test_group"
}
```

**Errors**

* 403 Permission error, only administrator can perform this action
* 404 User not found.
* 500 Internal Server Error

### <a id="admin-only-set-group-quota"></a>Set Group Quota

Available for Seafile v6.3

**PUT** https://cloud.seafile.com/api/v2.1/admin/groups/{group_id}/

**Request parameters**

* `quota`: integer, `-2` means no quota limit.

**Sample request**

    curl -X PUT -d "quota=100" -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/admin/groups/1528/

**Sample response**

```
{
    "owner": "1@1.com",
    "created_at": "2016-08-04T17:34:05+08:00",
    "id": 1528,
    "name": "test_group",
    "quota": 100
}
```

**Errors**

* 400 Quota invalid.
* 403 Permission error, only administrator can perform this action
* 500 Internal Server Error

### <a id="admin-only-get-group-libraries"></a>Get Group Libraries

Available for Seafile v6.0.0+

**GET** https://cloud.seafile.com/api/v2.1/admin/groups/{group_id}/libraries/

Get all libraries of a group.

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/groups/64/libraries/

**Sample response**

```
[
    {
        "repo_id":"7460f7ac-a0ff-4585-8906-bb5a57d2e118",
        "name":"My Library",
        "permission":"rw",
        "group_id":65,
        "shared_by":"lian@lian.com",
        "size":97662
    }
]
```

**Errors**

* 403 Permission error, only administrator can perform this action
* 404 Group not found.

### <a id="admin-only-delete-group-library"></a>Delete Group Library

Available for Seafile v6.0.0+

**DELETE** https://cloud.seafile.com/api/v2.1/admin/groups/{group_id}/libraries/{repo_id}/

**Sample request**

    curl -X DELETE -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/admin/groups/64/libraries/7460f7ac-a0ff-4585-8906-bb5a57d2e118/

**Sample response**

```
{"success":true}
```

**Errors**

* 403 Permission error, only administrator can perform this action
* 404 Library/Group not found.
* 500 Internal Server Error

### <a id="admin-only-get-group-members"></a>Get Group Members

Available for Seafile v6.0.0+

**GET** https://cloud.seafile.com/api/v2.1/admin/groups/{group_id}/members/

Get all members of a group.

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/groups/64/members/

**Sample response**

```
[
    {
        "login_id":"",
        "avatar_url":"https://cloud.seafile.com/media/avatars/0/1/a72299021077701e7c522c46fdaa87/resized/80/6ad30837f69ea7ef234dc272fb15e9e9.png",
        "contact_email":"lian@lian.com",
        "name":"name of lian",
        "is_admin":true,
        "role":"Owner",
        "group_id":65,
        "email":"lian@lian.com"
    },
    {
        "login_id":"",
        "avatar_url":"https://cloud.seafile.com/media/avatars/default.png",
        "contact_email":"1@1.com",
        "name":"123",
        "is_admin":false,
        "role":"Member",
        "group_id":65,
        "email":"1@1.com"
    }
]
```

**Errors**

* 403 Permission error, only administrator can perform this action
* 404 Group not found.

### <a id="admin-only-delete-group-member"></a>Delete Group Member

Available for Seafile v6.0.0+

**DELETE** https://cloud.seafile.com/api/v2.1/admin/groups/{group_id}/members/{email}/

**Sample request**

    curl -X DELETE -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/admin/groups/64/members/foo@foo.com/

**Sample response**

```
{"success":true}
```

**Errors**

* 403 Permission error, only administrator can perform this action
* 403 foo@foo.com is group owner, can not be removed.
* 404 Group not found.
* 500 Internal Server Error

### <a id="admin-only-add-group-member"></a>Add Group Member

Available for Seafile v6.0.8+

**POST** https://cloud.seafile.com/api/v2.1/admin/groups/{group_id}/members/

**Sample request**

    curl -d "email=1@1.com&email=2@1.com" -H 'Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a' https://cloud.seafile.com/api/v2.1/admin/groups/65/members/

**Sample response**

```
{
    "failed":[
        {
            "email":"2@1.com","error_msg":"User 2@1.com is already a group member."
        }
    ],
    "success":[
        {
            "login_id":"",
            "avatar_url":"https://cloud.seafile.com/media/avatars/default.png",
            "contact_email":"8@1.com",
            "name":"name of 8",
            "is_admin":0,
            "role":"Member",
            "group_id":65,
            "email":"8@1.com"
        }
    ]
}
```

**Errors**

* 400 email invalid.
* 404 Group not found.

### <a id="admin-only-update-group-member-role"></a>Update Group Member Role

Available for Seafile v6.0.8+

##### Set a group member as admin

**PUT** https://cloud.seafile.com/api/v2.1/admin/groups/{group_id}/members/{email}

**Sample request**

    curl -X PUT -d "is_admin=true" -H 'Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a' https://cloud.seafile.com/api/v2.1/admin/groups/65/members/3@1.com/

**Sample response**

```
{
    "login_id":"",
    "avatar_url":"https://cloud.seafile.com/media/avatars/default.png",
    "contact_email":"3@1.com",
    "name":"update name of 3",
    "is_admin":1,
    "role":"Admin",
    "group_id":65,
    "email":"3@1.com"
}
```

**Errors**

* 400 email invalid.
* 400 is_admin invalid.
* 404 Group/User not found.
* 500 Internal Server Error

### <a id="admin-only-add-group-owned-library"></a>Add Group Owned Library

**POST** http://192.168.1.113:8000/api/v2.1/admin/groups/{group_id}/group-owned-libraries/

**Request parameters**

* `group_id`
* `repo_name`
* `password`
* `permission`, default `rw`.

**Sample request**

```
curl -d "repo_name=group-owned-repo-4&permission=r" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "http://192.168.1.113:8000/api/v2.1/amdin/groups/53/group-owned-libraries/"
```

**sample response**

```
{
    "repo_id": "9bc59af9-265e-4110-a0e2-619450a5cb35",
    "permission": "r",
    "encrypted": false,
    "owner_email": "53@seafile_group",
    "mtime": "2018-04-23T17:25:37+08:00",
    "repo_name": "group-owned-repo-4",
    "size": 0
}
```

**Errors**

* 400 repo_name/permission invalid.
* 403 NOT allow to create encrypted library..
* 403 Permission denied.
* 403 No group quota.
* 404 Group not found.

### <a id="admin-only-delete-group-owned-library"></a>Delete Group Owned Library

**DELETE** http://192.168.1.113:8000/api/v2.1/admin/groups/{group_id}/group-owned-libraries/{repo_id}/

**Request parameters**

* `group_id`
* `repo_id`

**Sample request**

```
curl -X DELETE -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "http://192.168.1.113:8000/api/v2.1/admin/groups/53/group-owned-libraries/9bc59af9-265e-4110-a0e2-619450a5cb35/"
```

**sample response**

```
{"success":true}
```

**Errors**

* 403 Permission denied.
* 404 Group/Library not found.
* 500 Internal Server Error

#### <a id="admin-only-modify-group-owned-library-sub-folder-permission"></a>Modify Group Owned Library Sub-Folder Permission

**PUT** http://192.168.1.113:8000/api/v2.1/admin/groups/{group_id}/group-owned-libraries/{repo_id}/

**Request parameters**

* `group_id`
* `repo_id`
* `path`, path of sub folder.
* `permission`: `r` or `rw`.

**Sample request**

```
curl -X PUT -d "path=/tmp/&permission=r" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "http://192.168.1.113:8000/api/v2.1/admin/groups/53/group-owned-libraries/9bc59af9-265e-4110-a0e2-619450a5cb35/"
```

**sample response**

```
{"success":true}
```

**Errors**

* 400 path/permission invalid.
* 403 Permission denied.
* 404 Group/Library/Folder not found.
* 500 Internal Server Error

##### Unset a group member as admin

**PUT** https://cloud.seafile.com/api/v2.1/admin/groups/{group_id}/members/{email}

**Sample request**

    curl -X PUT -d "is_admin=false" -H 'Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a' https://cloud.seafile.com/api/v2.1/admin/groups/65/members/3@1.com/

**Sample response**

```
{
    "login_id":"",
    "avatar_url":"https://cloud.seafile.com/media/avatars/default.png",
    "contact_email":"3@1.com",
    "name":"update name of 3",
    "is_admin":0,
    "role":"Member",
    "group_id":65,
    "email":"3@1.com"
}
```

**Errors**

* 400 email invalid.
* 400 is_admin invalid.
* 404 Group/User not found.
* 500 Internal Server Error

## <a id="admin-only-shared-links"></a>Shared Links

### <a id="admin-only-download-links"></a>Download Links

#### <a id="admin-only-download-link-get-shared-file-dir-info"></a>Get Shared File/Dir Info

**GET** http://192.168.1.124:8000/api/v2.1/admin/share-links/{token}/

**Request parameters**

* token

**Sample request**
```
curl -H 'Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.124:8000/api/v2.1/admin/share-links/db62f56baf1b4460996e/"
```

**Sample response**
```
{
    "repo_id": "0a5647c8-7708-445a-bd80-49f04b85b153",
    "ctime": "2017-06-20T08:37:13+00:00",
    "creator_name": "name of lian",
    "creator_email": "lian@lian.com",
    "obj_name": "asdf",
    "token": "db62f56baf1b4460996e",
    "view_cnt": 8,
    "link": "http://192.168.1.124:8000/d/db62f56baf1b4460996e/",
    "expire_date": "2017-06-23T08:37:13+00:00",
    "path": "/asdf/",
    "creator_contact_email": "lian@lian.com",
    "is_dir": true,
    "permissions": {
        "can_preview": true,
        "can_download": true
    },
    "is_expired": false,
    "repo_name": "sadfdaa"
}
```

**Errors**

* 403 Permission denied.
* 404 Share link not found.

#### <a id="admin-only-download-link-get-dirents-in-shared-dir"></a>Get Sub File/Dir List in Shared Dir

**GET** http://192.168.1.124:8000/api/v2.1/admin/share-links/{token}/dirents/

**Request parameters**

* token
* path, sub-folder of shared dir, default is `/`.

**Sample request**
```
curl -H 'Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.124:8000/api/v2.1/admin/share-links/db62f56baf1b4460996e/dirents/?path=/sdf"
```

**Sample response**
```
[
    {
        "path": "/sdf/1122",
        "is_dir": true,
        "size": 0,
        "last_modified": "2017-06-21T02:18:40+00:00",
        "obj_name": "1122"
    },
    {
        "path": "/sdf/12.docx",
        "is_dir": false,
        "size": 457426,
        "last_modified": "2017-06-20T10:09:53+00:00",
        "obj_name": "12.docx"
    },
    {
        "path": "/sdf/slack-desktop-2.3.3-amd64.deb",
        "is_dir": false,
        "size": 47434600,
        "last_modified": "2017-06-20T10:27:47+00:00",
        "obj_name": "slack-desktop-2.3.3-amd64.deb"
    }
]
```

**Errors**

* 403 Permission denied.
* 404 Share link not found.

#### <a id="admin-only-download-link-download"></a>Download File/Dir

**GET** http://192.168.1.124:8000/api/v2.1/admin/share-links/{token}/download/

**Request parameters**

* token
* type, only used for download (sub) file/folder of shared dir, `file` or `folder`.
* path, only used for download (sub) file/folder of shared dir.

**Sample request for download (sub) folder in shared dir**
```
curl -H 'Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.124:8000/api/v2.1/admin/share-links/db62f56baf1b4460996e/download/?path=/sdf&type=folder"
```

**Sample response for download (sub) folder in shared dir**
```
{
    "download_link": "http://192.168.1.124:8082/zip/395e0ea8-3936-4084-b650-64a93d8a313d"
}
```

After you get the download link for the (sub) folder, you should use the token in the download link (here's `395e0ea8-3936-4084-b650-64a93d8a313d`) to check if the background compression packaging has been completed by [Query Task Progress](#download-directory-query-task-progress), once it is finished, you can use the download link to download the (sub) folder.

**Sample request for download (sub) file in shared dir**
```
curl -H 'Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.124:8000/api/v2.1/admin/share-links/db62f56baf1b4460996e/download/?path=/sdf/12.docx&type=file"
```

**Sample response for download (sub) file in shared dir**
```
{
    "download_link": "http://192.168.1.124:8082/files/2fec8ae7-ffd5-4586-b125-7234e7a69656/12.docx"
}
```

**Sample request for download shared file**
```
curl -H 'Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.124:8000/api/v2.1/admin/share-links/dac219add64f4a4b9c51/download/"
```

**Sample response for download shared file**
```
{
    "download_link": "http://192.168.1.124:8082/files/a34af6cb-4762-4eea-b5a4-0b924e6767d0/excel-view.xlsx"
}
```

**Errors**

* 403 Permission denied.
* 404 Share link not found.
* 404 File not found.
* 404 Folder not found.
* 404 Library not found.
* 500 Internal Server Error

#### <a id="admin-only-download-link-check-password"></a>Check Password

**GET** http://192.168.1.124:8000/api/v2.1/admin/share-links/{token}/check-password/

**Request parameters**

* token
* password

**Sample request**
```
curl -d 'password=11111111' -H 'Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.124:8000/api/v2.1/admin/share-links/db62f56baf1b4460996e/check-password/"
```

**Sample response**
```
{
    "success": true
}
```

**Errors**

* 400 Share link is not encrypted.
* 400 password invalid.
* 403 Permission denied.
* 403 Password is not correct.
* 404 Share link not found.

### <a id="admin-only-upload-links"></a>Upload Links

#### <a id="admin-only-upload-link-get-shared-dir-info"></a>Get Shared Dir Info

**GET** http://192.168.1.124:8000/api/v2.1/admin/upload-links/{token}/

**Request parameters**

* token

**Sample request**
```
curl -H 'Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.124:8000/api/v2.1/admin/upload-links/360fe7d6dc684045b7f6/"
```

**Sample response**
```
{
    "view_cnt": 0,
    "ctime": "2017-06-20T08:37:22+00:00",
    "creator_name": "name of lian",
    "creator_email": "lian@lian.com",
    "creator_contact_email": "lian@lian.com",
    "token": "360fe7d6dc684045b7f6",
    "repo_id": "0a5647c8-7708-445a-bd80-49f04b85b153",
    "link": "http://192.168.1.124:8000/u/d/360fe7d6dc684045b7f6/",
    "obj_name": "asdf",
    "path": "/asdf/",
    "repo_name": "sadfdaa"
}
```

**Errors**

* 403 Permission denied.
* 404 Upload link not found.

#### <a id="admin-only-upload-link-upload"></a>Upload

**GET** http://192.168.1.124:8000/api/v2.1/admin/upload-links/{token}/upload/

**Request parameters**

* token

**Sample request**
```
curl -H 'Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.124:8000/api/v2.1/admin/upload-links/360fe7d6dc684045b7f6/upload/"
```

**Sample response**
```
{
    "upload_link": "http://192.168.1.124:8082/upload-api/b08b20e4-beb2-4c7a-af03-fed6be859330"
}
```

After get upload link, you can upload file to the shared dir, for more info, please see [Upload File](#upload-file-1).

**Errors**

* 403 Permission denied.
* 404 Upload link not found.
* 404 Folder not found.

#### <a id="admin-only-upload-link-check-password"></a>Check Password

**GET** http://192.168.1.124:8000/api/v2.1/admin/upload-links/{token}/check-password/

**Request parameters**

* token
* password

**Sample request**
```
curl -d 'password=11111111' -H 'Authorization: Token cbd7705c06846425ed5c46ae0313d5b098d24154' -H 'Accept: application/json; charset=utf-8; indent=4' "http://192.168.1.124:8000/api/v2.1/admin/upload-links/360fe7d6dc684045b7f6/check-password/"
```

**Sample response**
```
{
    "success": true
}
```

**Errors**

* 400 Upload link is not encrypted.
* 400 password invalid.
* 403 Permission denied.
* 403 Password is not correct.
* 404 Upload link not found.

## <a id="admin-only-log"></a>Admin Log

### <a id="admin-only-get-login-log"></a>Get Login Log

This api is only supported in pro edition.

**GET** https://cloud.seafile.com/api/v2.1/admin/logs/login/?start=2016-03-20&end=2016-03-31

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/logs/login/?start=2016-03-20&end=2016-03-31

**Sample response**

```
[
    {
        'email': u'lian@lian.com',
        'login_ip': u'192.168.1.124',
        'name': u'lian',
        'login_time': '2016-03-31T14:42:23+08:00'
    },
    {
        'email': u'org@org.com',
        'login_ip': u'192.168.1.124',
        'name': u'org',
        'login_time': '2016-03-31T14:39:08+08:00'
    }
]
```

**Errors**

* 400 start or end date invalid.
* 403 Feature disabled.

### <a id="admin-only-get-file-audit-log"></a>Get File Audit Log

This api is only supported in pro edition.

**GET** https://cloud.seafile.com/api/v2.1/admin/logs/file-audit/?start=2016-03-20&end=2016-03-31

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/logs/file-audit/?start=2016-03-20&end=2016-03-31

**Sample response**

```
[
    {
        'repo_id': u'4929d0df-8c6c-43cb-8edf-40a8489689fb',
        'time': '2016-03-31T05:46:03+08:00',
        'etype': u'file-download-web',
        'ip': u'192.168.1.124',
        'user_name': u'org',
        'file_path': u'/earth.jpg',
        'user_email': u'org@org.com',
        'repo_name': ''
    },
    {
        'repo_id': u'513cd72c-c54a-463e-a18f-841efe91bd61',
        'time': '2016-03-31T06:25:22+08:00',
        'etype': u'file-download-web',
        'ip': u'192.168.1.124',
        'user_name': u'org',
        'file_path': u'/kj.md',
        'user_email': u'org@org.com',
        'repo_name': u'new-lib-of-org-1'
    }
]
```

**Errors**

* 400 start or end date invalid.
* 403 Feature disabled.

### <a id="admin-only-get-file-update-log"></a>Get File Update Log

This api is only supported in pro edition.

**GET** https://cloud.seafile.com/api/v2.1/admin/logs/file-update/?start=2016-03-20&end=2016-03-31

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/logs/file-update/?start=2016-03-20&end=2016-03-31

**Sample response**

```
[
    {
        'commit_id': u'55ec5350b16d6c72a044b5a9cd9b2d62ad439364',
        'file_operation': u'Added "user.csv".',
        'repo_id': u'513cd72c-c54a-463e-a18f-841efe91bd61',
        'repo_name': u'new-lib-of-org-1',
        'time': '2016-03-31T06:25:15+08:00',
        'user_email': u'org@org.com',
        'user_name': u'org'
    },
    {
        'commit_id': u'6820d809481e3c9fb856d0650ac73a09b570a301',
        'file_operation': u'Added "kj.md"',
        'repo_id': u'513cd72c-c54a-463e-a18f-841efe91bd61',
        'repo_name': u'new-lib-of-org-1',
        'time': '2016-03-31T06:25:21+08:00',
        'user_email': u'org@org.com',
        'user_name': u'org'
    }
]
```

**Errors**

* 400 start or end date invalid.
* 403 Feature disabled.

### <a id="admin-only-get-perm-audit-log"></a>Get Permission Audit Log

This api is only supported in pro edition.

**GET** https://cloud.seafile.com/api/v2.1/admin/logs/perm-audit/?start=2016-03-20&end=2016-03-31

**Sample request**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/logs/perm-audit/?start=2016-03-20&end=2016-03-31

**Sample response**

```
[
    {
        'etype': u'add-repo-perm',
        'file_path': u'/folder',
        'from_email': u'org3@org3.com',
        'from_name': u'org3',
        'permission': u'rw',
        'repo_id': u'a84544e5-0b84-459d-b1e6-0399dabc76a0',
        'repo_name': '',
        'time': '2016-03-31T06:21:50+08:00',
        'to': u'org@org.com'
    },
    {
        'etype': u'add-repo-perm',
        'file_path': u'/folder',
        'from_email': u'org3@org3.com',
        'from_name': u'org3',
        'permission': u'rw',
        'repo_id': u'a84544e5-0b84-459d-b1e6-0399dabc76a0',
        'repo_name': '',
        'time': '2016-03-31T06:21:53+08:00',
        'to': u'777'
    }
]
```

**Errors**

* 400 start or end date invalid.
* 403 Feature disabled.

## <a id="admin-only-organization"></a>Organization

### <a id="admin-only-add-organization"></a>Add Organization

This api is only supported in pro edition.

**POST** https://cloud.seafile.com/api2/organization/

**Request parameters**

* username
* password
* org_name
* prefix
* quota
* member_limit

**Sample request**

    curl -v -X POST -d "username=example@example.com&password=example&org_name=example&prefix=example&quota=100&member_limit=10" -H "Authorization: Token ccdff90e4d1efe76b2b3d91c06b027a5cff189d4" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/organization/

**Sample response**

    "success"

### <a id="admin-only-add-organization-user"></a>Add Organization User

This api is only supported in pro edition (since 6.0.9).

**POST** https://cloud.seafile.com/api/v2.1/admin/organizations/{org_id}/users/

**Request parameters**

* org_id
* email
* password

**Sample request**
    curl -d "username=1@org-3.com&password=1&org_name=org-3&prefix=org-3&quota=100&member_limit=10" -H "Authorization: Token 3f1e23157c3a1fd740e9dc1c5d748929fe319b95" -H 'Accept: application/json; indent=4' http://192.168.1.165/api2/organization/

**Sample response**
```
{
    "quota_usage": 0,
    "name": "6",
    "org_id": 1,
    "contact_email": "6@org.com",
    "active": true,
    "quota_total": -1,
    "email": "6@org.com"
}
```

**Errors**

* 400 org_id invalid.
* 400 email invalid.
* 400 password invalid.
* 400 User already exists.
* 403 The number of users exceeds the limit.
* 403 Failed. You can only invite %d members.
* 404 Organization not found.
* 500 Fail to add user.
* 500 Internal Server Error

### <a id="admin-only-get-organization-user-info"></a>Get Organization User Info

This api is only supported in pro edition (since 6.1.5).

**GET** https://cloud.seafile.com/api/v2.1/admin/organizations/{org_id}/users/{email}/

**Request parameters**

* org_id
* email

**Sample request**

    curl -H "Authorization: Token 3f1e23157c3a1fd740e9dc1c5d748929fe319b95" -H 'Accept: application/json; indent=4' http://192.168.1.165/api/v2.1/admin/organizations/1/users/6@org.com/

**Sample response**
```
{
    "quota_usage": 0,
    "name": "6",
    "org_id": 1,
    "contact_email": "6@org.com",
    "active": true,
    "quota_total": -1,
    "email": "6@org.com"
}
```

**Errors**

* 400 org_id invalid.
* 400 User is not member of organization.
* 404 Organization not found.
* 404 User not found.
* 500 Internal Server Error

### <a id="admin-only-update-organization-user-info"></a>Updage Organization User Info

This api is only supported in pro edition (since 6.1.5).

**PUT** https://cloud.seafile.com/api/v2.1/admin/organizations/{org_id}/users/{email}/

**Request parameters**

* org_id
* email
* active, `true` or `false`
* name
* contact_email
* quota_total, integer greater than 0, unit is MB.

**Sample request**

    curl -X PUT -d "active=false&name=name-of-6&contact_email=6-contact@email.com&quota_total=23" -H "Authorization: Token 3f1e23157c3a1fd740e9dc1c5d748929fe319b95" -H 'Accept: application/json; indent=4' http://192.168.1.165/api/v2.1/admin/organizations/1/users/6@org.com/

**Sample response**
```
{
    "quota_usage": 0,
    "name": "name-of-6",
    "org_id": 1,
    "contact_email": "6-contact@email.com",
    "active": false,
    "quota_total": 23,
    "email": "6@org.com"
}
```

**Errors**

* 400 org_id invalid.
* 400 active invalid, should be 'true' or 'false'.
* 400 Failed to set quota.
* 404 Organization not found.
* 404 User not found.
* 500 Internal Server Error

### <a id="admin-only-delete-organization-user"></a>Delete Organization User

This api is only supported in pro edition (since 6.0.9).

**DELETE** https://cloud.seafile.com/api/v2.1/admin/organizations/{org_id}/users/{email}/

**Request parameters**

* org_id
* email

**Sample request**

    curl -X DELETE -H "Authorization: Token 0eb24ce5db35a31f70171eca2f760f03f59fa09a" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/organizations/160/users/6@org.com/

**Sample response**

```
{
    "success": true
}
```

**Errors**

* 400 org_id invalid.
* 403 Failed to delete: is an organization creator.
* 404 Organization not found.
* 404 User not found.
* 500 Internal Server Error

## <a id="admin-only-department"></a>Department

### <a id="admin-only-list-departments"></a> List departments

**GET** http://192.168.1.113:8000/api/v2.1/admin/address-book/groups/

**Sample request**

```
curl -H 'Authorization: Token 2bac21cab9eb0c4baac10d1e6fc3cf590f0dcf17' -H 'Accept: application/json; charset=utf-8; indent=4' http://192.168.1.113:8000/api/v2.1/admin/address-book/groups/
```

**Sample response**

```
{
  "data": [
    {
      "name": "test-xxx",
      "created_at": "2018-06-05T10:45:45+08:00",
      "quota": -2,
      "parent_group_id": -1,
      "owner": "system admin",
      "id": 176
    },
    {
      "name": "\u7814\u53d1\u90e8",
      "created_at": "2018-05-24T23:30:07+08:00",
      "quota": -2,
      "parent_group_id": -1,
      "owner": "system admin",
      "id": 172
    },
    {
      "name": "test1",
      "created_at": "2018-05-15T11:57:16+08:00",
      "quota": 1000000000,
      "parent_group_id": -1,
      "owner": "system admin",
      "id": 168
    }
  ]
}
```

### <a id="admin-only-list-departments-groups"></a> List groups and members in a department

**GET** http://192.168.1.113:8000/api/v2.1/admin/address-book/groups/{group_id}/?return_ancestors=true

**Request parameters**

* return_ancestors (true or false, defaults to false)

**Sample request**

```
curl -H 'Authorization: Token 2bac21cab9eb0c4baac10d1e6fc3cf590f0dcf17' -H 'Accept: application/json; charset=utf-8; indent=4' http://192.168.1.113:8000/api/v2.1/admin/address-book/groups/172/?return_ancestors=true
```

**Sample response**

```
{
  "id": 172
  "name": "\u7814\u53d1\u90e8",
  "created_at": "2018-05-24T23:30:07+08:00",
  "quota": -2,
  "members": [
    {
      "login_id": "",
      "avatar_url": "http://192.168.1.113:8000/image-view\/avatars\/9\/3\/45638f87b4642ce4820dbe65e3438d\/resized\/80\/dfad850ea93d405f6e6cf51a9f1e36bf_GrrNVeZ.png",
      "contact_email": "xxx@gmail.com",
      "name": "xxx",
      "is_admin": true,
      "role": "Admin",
      "group_id": 172,
      "email": "xxx@gmail.com"
    }
  ],
  "parent_group_id": -1,
  "groups": [
    {
      "name": "\u5ba2\u6237\u7aef\u7ec4",
      "created_at": "2018-05-24T23:30:32+08:00",
      "quota": 5000000000,
      "parent_group_id": 172,
      "owner": "system admin",
      "id": 173
    },
    {
      "name": "\u670d\u52a1\u5668\u5f00\u53d1\u7ec4",
      "created_at": "2018-05-25T11:55:17+08:00",
      "quota": -2,
      "parent_group_id": 172,
      "owner": "system admin",
      "id": 174
    },
  ],
  "owner": "system admin",
  "ancestor_groups": [
    
  ],
}
```

### <a id="admin-only-create-department"></a> Create department

**POST** http://192.168.1.113:8000/api/v2.1/admin/address-book/groups/

**Request parameters**

* `group_name`
* `group_owner`	(defaults to '')
* `parent_group` (Positive Integer, defaults to -1)

**Sample request**

```
curl -v -d "group_name=xxx&group_owner=system admin" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' http://192.168.1.113:8000/api/v2.1/admin/address-book/groups/
```

**Sample response**

```
{
  "name": "xxx",
  "created_at": "2018-06-05T10:45:45+08:00",
  "quota": -2,
  "parent_group_id": -1,
  "owner": "system admin",
  "id": 176
}
```

**Errors**

* 400 `group_name` or `parent_group` invalid

### <a id="admin-only-dismiss-department"></a> Dismiss department

**DELETE** http://192.168.1.113:8000/api/v2.1/admin/address-book/groups/{group_id}/

**Sample request**

```
curl -X DELETE -v  -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' http://192.168.1.113:8000/api/v2.1/admin/address-book/groups/176/
```

**Sample response**

```
{"success":true}
```

