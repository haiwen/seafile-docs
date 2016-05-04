# 个性化 Seahub

## 个性化 Logo 及 CSS 样式

Create a folder ``<seafile-install-path>/seahub-data/custom``. Create a symbolic link in `seafile-server-latest/seahub/media` by `ln -s ../../../seahub-data/custom custom`.

During upgrading, Seafile upgrade script will create symbolic link automatically to preserve your customization.

### 自定义 Logo

1. 将 Logo 文件放在 seahub/media/custom/ 文件夹下
2. 在 seahub_settings.py 中，重新定义 LOGO_PATH 的值。

   ```python
   LOGO_PATH = 'custom/mylogo.png'
   ```

3. Default width and height for logo is 149px and 32px, you may need to change that according to yours.

   ```python
   LOGO_WIDTH = 149
   LOGO_HEIGHT = 32
   ```

### 自定义 Seahub CSS 样式

1. 在 `seahub/media/custom/` 中新建 CSS 文件，比如： `custom.css`。
2. 在 `seahub_settings.py` 中，重新定义 `BRANDING_CSS` 的值。

   ```python
   BRANDING_CSS = 'custom/custom.css'
   ```

## 个性化 Seahub 页面

**注意:** 仅支持 2.1 及之后的版本

在 ``<seafile-install-path>/seahub-data/custom`` 目录下，新建 ``templates`` 文件夹。

### 个性化“页脚”页面

1. 复制``seahub/seahub/templates/footer.html`` 到 ``seahub-data/custom/templates``。
2. 自行编写 `footer.html`。

### 个性化“下载”页面

1. 复制 ``seahub/seahub/templates/download.html`` 到 ``seahub-data/custom/templates``。
2. 自行编写 `download.html`。

### 个性化“帮助”页面

1. 复制 ``seahub/seahub/help/templates/help.html``到 ``seahub-data/custom/templates``。
2. 自行编写 `help.html`。

