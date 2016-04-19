# Seahub 개별 설정

## Seahub 로고 및 CSS 개별 설정

``<seafile-install-path>/seahub-data/custom`` 폴더를 만드십시오. `ln -s ../../../seahub-data/custom custom` 명령으로 `seafile-server-latest/seahub/media` 심볼릭 링크를 만드십시오.

업그레이드 과정에서, Seafile 업그레이드 스크립트는 개별 설정을 보존하면서 심볼릭 링크를 자동으로 만듭니다.

### 로고 개별 설정

1. `custom/`에 로고 파일을 추가하십시오
2. `seahub_settings.py`에 `LOGO_PATH`값을 덮어쓰십시오

   ```python
   LOGO_PATH = 'custom/mylogo.png'
   ```

3. 로고의 기본 너비와 높이 값은 149px 및 32px 입니다. 상황에 따라 바꿔야합니다.

   ```python
   LOGO_WIDTH = 149
   LOGO_HEIGHT = 32
   ```

### Seahub CSS 개별 설정

1. `custom/`에 `custom.css` 같은 CSS 파일을 추가하십시오
2. `seahub_settings.py`에 `BRANDING_CSS` 값을 덮어쓰십시오

   ```python
   BRANDING_CSS = 'custom/custom.css'
   ```

## 푸터 및 기타 Seahub 페이지 개별 설정

**참고:** 2.1 버전 부터.

``<seafile-install-path>/seahub-data/custom``에 ``templates``  폴더를 만드십시오

### 푸터 개별 설정

1. ``seahub-data/custom/templates``에  ``seahub/seahub/templates/footer.html`` 파일을 복사하십시오.
2. `footer.html`을 수정하십시오.

### 다운로드 페이지 개별 설정

1. ``seahub-data/custom/templates``에 ``seahub/seahub/templates/download.html`` 파일을 복사하십시오.
2. `download.html`을 수정하십시오.

### 도움말 페이지 개별 설정

1. ``seahub-data/custom/templates/help``에 ``seahub/seahub/help/templates/help`` 디렉터리를 복사하십시오.
2. `help` 아래의 페이지를 수정하십시오.

