# Seahub customization

## Customize Seahub Logo and CSS

Create a folder ``<seafile-install-path>/seahub-data/custom``. Create a symbolic link in `seafile-server-latest/seahub/media` by `ln -s ../../../seahub-data/custom custom`.

During upgrading, Seafile upgrade script will create symbolic link automatically to preserve your customization.

### Customize Logo

1. Add your logo file to `custom/`
2. Overwrite `LOGO_PATH` in `seahub_settings.py`

   ```python
   LOGO_PATH = 'custom/mylogo.png'
   ```

3. Default width and height for logo is 149px and 32px, you may need to change that according to yours.

   ```python
   LOGO_WIDTH = 149
   LOGO_HEIGHT = 32
   ```

### Customize Favicon

1. Add your favicon file to `custom/`
2. Overwrite `FAVICON_PATH` in `seahub_settings.py`


   ```python
   FAVICON_PATH = 'custom/favicon.png'
   ```

### Customize Seahub CSS

1. Add your css file to `custom/`, for example, `custom.css`
2. Overwrite `BRANDING_CSS` in `seahub_settings.py`

   ```python
   BRANDING_CSS = 'custom/custom.css'
   ```

You can find a good example of customized css file here: https://github.com/focmb/seafile_custom_css_green


## Customize help page

**Note:** Since version 2.1.

First go to the custom folder

```
cd <seafile-install-path>/seahub-data/custom
```

then run the following commands

```
mkdir templates
mkdir templates/help
cp ../../seafile-server-latest/seahub/seahub/help/templates/help/install.html templates/help/
```

Modify the `templates/help/install.html` file and save it. You will see the new help page.
