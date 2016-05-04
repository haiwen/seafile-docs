# 다중 조직/단체 사용자 관리

버전 5.1부터 Seafile에 단체를 추가하고 사용자를 단체에 할당할 수 있습니다. 각 단체에는 하나 이상의 관리자를 확보할 수 있습니다. 이 기능은 가중 조직(대학교)에서 단일 Seafile 인스턴스를 공유할 때 사용자 관리를 용이하게 합니다. 다중 임차 구조와는 달리, 사용자는 특정 조직에 제한적으로 묶이지 않습니다. 한 단체의 사용자는 다른 단체로 파일을 공유할 수 있습니다.

## 기능 활성화

`seahub_settings.py`에서, `MULTI_INSTITUTION = True` 설정을 추가하여 다중 단체 기능을 활성화하십시오. 그리고

```
EXTRA_MIDDLEWARE_CLASSES += (
    'seahub.institutions.middleware.InstitutionMiddleware',
)
```

또는

```
EXTRA_MIDDLEWARE_CLASSES = (
    'seahub.institutions.middleware.InstitutionMiddleware',
)
```

를 `EXTRA_MIDDLEWARE_CLASSES`를 정의하지 않았을 경우 추가하십시오.

## 단체 및 단체 관리자 추가

서비스를 다시 시작하고 나면, 시스템 관리자는 관리자 창에서 단체 이름을 추가하여 단체를 추가할 수 있습니다. 또한 단체를 눌러 들어가서 `profile.institution`과 이름이 일치하는 단체의 사용자를 볼 수 있습니다.

## 사용자를 단체에 할당

시볼레스 인증 기능을 사용한다면, 시볼레스 속성을 단체에 대응할 수 있습니다. 예를 들어 다음 설정은 조직 속성을 단체에 대응합니다.

```
SHIBBOLETH_ATTRIBUTE_MAP = {
    "givenname": (False, "givenname"),
    "sn": (False, "surname"),
    "mail": (False, "contact_email"),
    "organization": (False, "institution"),
}
```

