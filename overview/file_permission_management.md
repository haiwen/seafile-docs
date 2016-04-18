# File permission management

Seafile manages files into libraries. Every library has an owner, who can share the library to other users or share it into groups. The sharing can be read-only or read-write.

## Read-only syncing

Read-only libraries can be synced to local desktop. The modifications at the client will not be synced back. If an user has modified some file contents, he/she can use "resync" to revert the modifications.


## Cascading permission/Sub-folder permissions (Pro edition)

Sharing controls whether an user/group can see an library, while sub-foler permissions is used to modify permissions on specific folders.

Suppose you share a library as read-only to a group and then want specific sub-folders to be read-write by a few users. You can set permissions on sub-folders for shared users and groups.

Note:

* Setting sub-folder permission for an user without sharing the folder or parent folder to that user will have no effect.
* Sharing a library read-only to an user and then sharing a sub-folder read-write to that user will lead to two shared items for that user. This will cause confusing. Use sub-folder permission instead.
