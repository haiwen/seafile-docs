# Multiple Storage Backend

There are some use cases that supporting multiple storage backends in Seafile server is needed. Such as:

1. Store different types of files into different storage backends. For example, normal files can be stored in primary storage (disks, SSD); Archived files can be stored in cold storage (tapes or other backup systems).
2. Combine multiple storage backends to extend storage scalability. For example, a single NFS volume may be limited by size; a single S3 bucket of Ceph RGW may suffer performance decrease when the number of objects become very large.

The library data in Seafile server are spreaded into multiple storage backends in the unit of libraries. All the data in a library will be located in the same storage backend. The mapping from library to its storage backend is stored in a database table. Different mapping policies can be chosen based on the use case.

To use this feature, you need to:
1. Define storage classes in seafile.conf.
2. Enable multiple backend feature in seahub and choose a mapping policy.

## Defining Storage Classes

In Seafile server, a storage backend is represented by the concept of "storage class". A storage class is defined by specifying the following information:

- `storage_id`: an internal string ID to identify the storage class. It's not visible to users. For example "primary storage".
- `name`: A user visible name for the storage class.
- `is_default`: whether this storage class is the default. If the chosen mapping policy allows users to choose storage class for a library, this would be the default if the user doesn't choose one.
- `commits`：the storage for storing the commit objects for this class. It can be any storage that Seafile supports, like file system, ceph, s3.
- `fs`：the storage for storing the fs objects for this class. It can be any storage that Seafile supports, like file system, ceph, s3.
- `blocks`：the storage for storing the block objects for this class. It can be any storage that Seafile supports, like file system, ceph, s3.

commit, fs, and blocks can be stored in different storages. This provides the most flexible way to define storage classes.

As Seafile server before 6.3 version doesn't support multiple storage classes, you have to explicitely enable this new feature and define storage classes with a different syntax than how we define storage backend before.

First, you have to enable this feature in seafile.conf.

```
[storage]
enable_storage_classes = true
storage_classes_file = /opt/seafile_storage_classes.json
```
- enable_storage_classes ：If this is set to true, storage class feature is enabled. You have to define the storage classes in a JSON file provided in the next configuration option.
- storage_classes_file：Specifies the path for the JSON file that contains storage class definition.

The JSON file is an array of objects. Each object defines a storage class. The fields in the definition corresponds to the information we need to specify for a storage class. Below is an example:

```
[
{
"storage_id": "hot_storage",
"name": "Hot Storage",
"is_default": true,
"commits": {"backend": "s3", "bucket": "seafile-commits", "key": "ZjoJ8RPNDqP1vcdD60U4wAHwUQf2oJYqxN27oR09", "key_id": "AKIAIOT3GCU5VGCCL44A"},
"fs": {"backend": "s3", "bucket": "seafile-fs", "key": "ZjoJ8RPNDqP1vcdD60U4wAHwUQf2oJYqxN27oR09", "key_id": "AKIAIOT3GCU5VGCCL44A"},
"blocks": {"backend": "s3", "bucket": "seafile-blocks", "key": "ZjoJ8RPNDqP1vcdD60U4wAHwUQf2oJYqxN27oR09", "key_id": "AKIAIOT3GCU5VGCCL44A"}
},

{
"storage_id": "cold_storage",
"name": "Cold Storage",
"is_default": false,
"fs": {"backend": "fs", "dir": "/storage/seafile/seafile-data"},
"commits": {"backend": "fs", "dir": "/storage/seafile/seafile-data"},
"blocks": {"backend": "fs", "dir": "/storage/seafile/seaflle-data"}
},

{
"storage_id": "swift_storage",
"name": "Swift Storage",
"fs": {"backend": "swift", "tenant": "adminTenant", "user_name": "admin", "password": "openstack", "container": "seafile-commits", "auth_host": "192.168.56.31:5000", "auth_ver": "v2.0"},
"commits": {"backend": "swift", "tenant": "adminTenant", "user_name": "admin", "password": "openstack", "container": "seafile-fs", "auth_host": "192.168.56.31:5000", "auth_ver": "v2.0"},
"blocks": {"backend": "swift", "tenant": "adminTenant", "user_name": "admin", "password": "openstack", "container": "seafile-blocks", "auth_host": "192.168.56.31:5000", "auth_ver": "v2.0", "region": "RegionTwo"}
}
]
```

As you may have seen, the `commits`, `fs` and `blocks` information syntax is similar to what used in `[commit_object_backend]`, `[fs_object_backend]` and `[block_backend]` section of seafile.conf.

If you use file system as storage for `fs`, `commits` or `blocks`, you have to explicitely provide the path for the `seafile-data` directory. The objects will be stored in `storage/commits`, `storage/fs`, `storage/blocks` under this path. 

*Note*: Currently file system, S3 and Swift backends are supported. Ceph/RADOS is not supported yet.

## Library Mapping Policies

Library mapping policies decide the storage class a library uses. Currently we provide 3 policies for 3 different use cases. The storage class of a library is decided on creation and stored in a database table. The storage class of a library won't change if the mapping policy is changed later.

Before choosing your mapping policy, you need to enable storage classes feature in seahub_settings.py:

```
ENABLE_STORAGE_CLASSES = True
```

### User Chosen

This policy lets the users to choose which storage class to use when creating a new library. The users can select any storage class that's been defined in the JSON file.

To use this policy, add following options in seahub_settings.py:

```
STORAGE_CLASS_MAPPING_POLICY = 'USER_SELECT'
```

If you enable storage class support but don't explicitely set `STORAGE_CLASS_MAPPING_POLIICY` in seahub_settings.py, this policy is used by default.
 
### Role-based Mapping

Due to storage cost or management consideration, sometimes system admin wants to make different type of users to use different storage backends (or classes). You can configure user's storage classes based on their roles.

A new option `storage_ids` is added to the role configuration in `seahub_settings.py` to assign storage classes to each role. If only one storage class is assigned to a role, the users with this role cannot choose storage class for libraries; otherwise, the users can choose storage class if more than one classes are assigned. If no storage class is assigned to a role, the default class specified in the JSON file will be used. 

Here is sample options in seahub_settings.py to use this policy:
```
ENABLE_STORAGE_CLASSES = True
STORAGE_CLASS_MAPPING_POLICY = 'ROLE_BASED'

ENABLED_ROLE_PERMISSIONS = {
    'default': {
        'can_add_repo': True,
        'can_add_group': True,
        'can_view_org': True,
        'can_use_global_address_book': True,
        'can_generate_share_link': True,
        'can_generate_upload_link': True,
        'can_invite_guest': True,
        'can_connect_with_android_clients': True,
        'can_connect_with_ios_clients': True,
        'can_connect_with_desktop_clients': True,
        'storage_ids': ['old_version_id', 'hot_storage', 'cold_storage', 'a_storage'],
    },
    'guest': {
        'can_add_repo': True,
        'can_add_group': False,
        'can_view_org': False,
        'can_use_global_address_book': False,
        'can_generate_share_link': False,
        'can_generate_upload_link': False,
        'can_invite_guest': False,
        'can_connect_with_android_clients': False,
        'can_connect_with_ios_clients': False,
        'can_connect_with_desktop_clients': False,
        'storage_ids': ['hot_storage', 'cold_storage'],
    },
}
```

### Library ID Based Mapping

This policy maps libraries to storage classes based on its library ID. The ID of a library is an UUID. In this way, the data in the system can be evenly districuted among the storage classes.

Note that this policy is not a designed to be a complete distributed storage solution. It doesn't handle automatical migration of library data between storage classes. If you need to add more storage classes to the configuration, existing libraries will stay in their original storage classes. New libraries can be distributed among the new storage classes (backends). You still have to plan about the total storage capacity of your system at the beginning.

To use this policy, you first add following options in seahub_settings.py:

```
STORAGE_CLASS_MAPPING_POLICY = 'REPO_ID_MAPPING'
```

Then you can add option `for_new_library` to the backends which are expected to store new libraries in json file:

```
[
{
"storage_id": "new_backend",
"name": "New store",
"for_new_library": true,
"is_default": false,
"fs": {"backend": "fs", "dir": "/storage/seafile/new-data"},
"commits": {"backend": "fs", "dir": "/storage/seafile/new-data"},
"blocks": {"backend": "fs", "dir": "/storage/seafile/new-data"}
}
]
```
