# Seafile 데스크톱 개별 설정

## Seafile 데스크톱 클라이언트에 나타나는 로고 및 이름 개별 설정(Seafile 전문가판 전용)

참고: 이 기능은 Seafile 데스크톱 클라이언트 4.4.0 이상에서만 가능합니다.

기본적으로 "Seafile"을 Seafile 데스크톱 클라이언트 창 상단에 로고와 함께 나타냅니다. 개별 설정하려면, `seahub_settings.py`의 `DESKTOP_CUSTOM_LOGO` 및 `DESKTOP_CUSTOM_BRAND` 값을 설정하십시오.

![desktop-customization](../images/desktop-customization.png)

그림 크기는 `24x24`여야 하며, 보통 `custom` 폴더에 그림을 복사해야합니다.

```python
DESKTOP_CUSTOM_LOGO = 'custom/desktop-custom-logo.png'
DESKTOP_CUSTOM_BRAND = 'Seafile For My Company'
```

## 모든 윈도우 PC에 Seafile 클라이언트 자동 설치

윈도우 도메인 컨트롤러의 그룹 정책 객체(GPO)를 설정하여 회사 네트워크의 모든 윈도우 PC에 Seafile 클라이언트를 자동으로 설치하도록 할 수 있습니다. Seafile 클라이언트는 MSI 설치 관리자로 제공합니다. 따라서 클라이언트를 자동으로 설치하려면 [마이크로소프트 문서](https://support.microsoft.com/en-us/kb/816102)를 따라가시면 됩니다.

## 모든 윈도우 PC에 맞게 Seafile 클라이언트 미리 설정하기

Seafile 클라이언트의 일부 동작은 윈도우의 레지스트리 항목으로 설정할 수 있습니다. 따라서, 그룹 정책 객체(GPO)로 집중화 방식을 통해 클라이언트의 동작을 관리할 수 있습니다.

Seafile 클라이언트에서 사용하는 레지스트리 항목은 [이 문서](https://github.com/haiwen/seafile-user-manual/blob/master/en/faq.md)에서 설명합니다. 윈도우의 이 레지스트리 항목으로 GPO를 설정하려면, [마이크로소프트 문서](https://technet.microsoft.com/en-us/library/cc753092.aspx)를 참고하십시오.

