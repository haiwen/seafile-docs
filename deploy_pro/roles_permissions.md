# Roles and Permissions Support

Starting from version 6.0, you can add/edit roles and permission for users. A role is just a group of users with some pre-defined permissions, you can toggle user roles in user list page at admin panel.

In version 6.0, we support 10 permissions, more permissions will be added later.

In version 6.1, we added a new permission `role_quota` which can be used to set quota for a certain role of users. For example, we can set the quota of employee to 100G by adding `'role_quota': '100g'`, and leave other role of users to the default quota.

Since version 6.3.6, we added a new permission `can_add_public_repo`(whether or not you can create a public library, default is "False").

Seafile comes with two build-in roles `default` and `guest`, a default user is a normal user with permissions as followings:
```
    'default': {
        'can_add_repo': True,
        'can_add_group': True,
        'can_view_org': True,
        'can_use_global_address_book': True,
        'can_generate_share_link': True,
        'can_generate_upload_link': True,
        'can_invite_guest': False,
        'can_connect_with_android_clients': True,
        'can_connect_with_ios_clients': True,
        'can_connect_with_desktop_clients': True,
        'role_quota': '',
        'can_publish_repo': True,
    },
```

While a guest user can only read files/folders in the system, here are the permissions for a guest user:
```
    'guest': {
        'can_add_repo': False,
        'can_add_group': False,
        'can_view_org': False,
        'can_use_global_address_book': False,
        'can_generate_share_link': False,
        'can_generate_upload_link': False,
        'can_invite_guest': False,
        'can_connect_with_android_clients': False,
        'can_connect_with_ios_clients': False,
        'can_connect_with_desktop_clients': False,
        'role_quota': '',
        'can_publish_repo': False,
    },
```

## Edit build-in roles

If you want to edit the permissions of build-in roles, e.g. default users can invite guest, guest users can view repos in organization, you can add following lines to `seahub_settings.py` with corresponding permissions set to `True`.

```
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
        'role_quota': '',
        'can_publish_repo': True,
    },
    'guest': {
        'can_add_repo': False,
        'can_add_group': False,
        'can_view_org': True,
        'can_use_global_address_book': False,
        'can_generate_share_link': False,
        'can_generate_upload_link': False,
        'can_invite_guest': False,
        'can_connect_with_android_clients': False,
        'can_connect_with_ios_clients': False,
        'can_connect_with_desktop_clients': False,
        'role_quota': '',
        'can_publish_repo': False,
    }
}
```

### More about guest invitation feature

An user who has `can_invite_guest` permission can invite people outside of the organization as guest.

In order to use this feature, in addition to granting `can_invite_guest` permission to the user, add the  following line to `seahub_settings.py`,

```
ENABLE_GUEST_INVITATION = True
```

After restarting, users who have `can_invite_guest` permission will see "Invite People" section at sidebar of home page.

Users can invite a guest user by providing his/her email address, system will email the invite link to the user.

**Tip:** If you want to block certain email addresses for the invitation, you can define a blacklist, e.g.

```
INVITATION_ACCEPTER_BLACKLIST = ["a@a.com", "*@a-a-a.com", r".*@(foo|bar).com", ]
```

After that, email address "a@a.com", any email address ends with "@a-a-a.com" and any email address ends with "@foo.com" or "@bar.com" will not be allowed.


## Add custom roles

If you want to add a new role and assign some users with this role, e.g. new role `employee` can invite guest and can create public library and have all other permissions a default user has, you can add following lines to `seahub_settings.py`

```
ENABLED_ROLE_PERMISSIONS = {
    'default': {
        'can_add_repo': True,
        'can_add_group': True,
        'can_view_org': True,
        'can_use_global_address_book': True,
        'can_generate_share_link': True,
        'can_generate_upload_link': True,
        'can_invite_guest': False,
        'can_connect_with_android_clients': True,
        'can_connect_with_ios_clients': True,
        'can_connect_with_desktop_clients': True,
        'role_quota': '',
        'can_publish_repo': True,
    },
    'guest': {
        'can_add_repo': False,
        'can_add_group': False,
        'can_view_org': False,
        'can_use_global_address_book': False,
        'can_generate_share_link': False,
        'can_generate_upload_link': False,
        'can_invite_guest': False,
        'can_connect_with_android_clients': False,
        'can_connect_with_ios_clients': False,
        'can_connect_with_desktop_clients': False,
        'role_quota': '',
        'can_publish_repo': False,
    },
    'employee': {
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
        'role_quota': '',
        'can_add_public_repo': True,
        'can_publish_repo': True,
    },
}
```
