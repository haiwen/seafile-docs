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

### Customize Seahub CSS

1. Add your css file to `custom/`, for example, `custom.css`
2. Overwrite `BRANDING_CSS` in `seahub_settings.py`

   ```python
   BRANDING_CSS = 'custom/custom.css'
   ```

## Customize footer and other Seahub Pages

**Note:** Since version 2.1.

Create a folder ``templates`` under ``<seafile-install-path>/seahub-data/custom``

### Customize footer

1. Copy ``seahub/seahub/templates/footer.html`` to ``seahub-data/custom/templates``.
2. Modify `footer.html`.

### Customize Download page

1. Copy ``seahub/seahub/templates/download.html`` to ``seahub-data/custom/templates``.
2. Modify `download.html`.

### Customize Help page

1. Copy ``seahub/seahub/help/templates/help`` to ``seahub-data/custom/templates/help``.
2. Modify pages under `help`.
