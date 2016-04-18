# Seafile Desktop customization

## Customize the logo and name displayed on seafile desktop clients (Seafile Professional Only)

Note: The feature is only available in seafile desktop client 4.4.0 and later.

By default, the text "Seafile" is displayed in the top of seafile desktop client window, along side with the seafile logo. To customize them, set `DESKTOP_CUSTOM_LOGO` and `DESKTOP_CUSTOM_BRAND` in `seahub_settings.py`.

![desktop-customization](../images/desktop-customization.png)

The size of the image must be `24x24`, and generally you should put it in the `custom` folder.

```python
DESKTOP_CUSTOM_LOGO = 'custom/desktop-custom-logo.png'
DESKTOP_CUSTOM_BRAND = 'Seafile For My Company'
```

## Auto Install Seafile Client on All Windows PCs

You can setup a group policy object (GPO) in your Windows Domain Controller to auto install seafile client on all Windows PCs in your company network. The Seafile client is provided as an MSI installer. So you just need to following the instructioin on [Microsoft's documentation](https://support.microsoft.com/en-us/kb/816102) to auto install the client.

## Preconfigure Seafile Client for All Windows PCs

Some behavior of the Seafile client can be configured via registry entries on Windows. So it's possible to control the client's behavior in a centralized way, via group policy objects (GPO).

The registry entries used to configure Seafile client are described in [this documentation](https://github.com/haiwen/seafile-user-manual/blob/master/en/faq.md). To setup GPO to set these registry entries on Windows, please refer to [Microsoft's documentation](https://technet.microsoft.com/en-us/library/cc753092.aspx).
