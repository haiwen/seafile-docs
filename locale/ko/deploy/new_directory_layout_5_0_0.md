# Seafile 서버 5.0.0에서 바뀐 설정 파일 위치

Seafile 서버는 각자 설정 파일을 보유한 다양한 구성 요소가 있습니다. 이 파일은 관리하기 불편한 다른 디렉터리에 있었습니다.

Seafile 서버 5.0.0 전의 디렉터리 배치는 다음과 같습니다:

```sh
└── seahub_settings.py
└── ccnet/
    └── ccnet.conf
└── seafile/
    └── seafile.conf
└── conf/
    └── seafdav.conf
└── pro-data/
    └── seafevents.conf # (전문가판 전용)
└── seafile-server-latest/
```

Seafile 서버 5.0.0 부터 모든 설정 파일을 **conf** 폴더로 이동했습니다:

```sh
└── conf/
    └── ccnet.conf
    └── seafile.conf
    └── seafdav.conf
    └── seahub_settings.py
    └── seafevents.conf # (전문가판 전용)
└── ccnet/
└── seafile/
└── pro-data/
```

이런식으로 모든 파일을 동일한 위치에서 찾을 수 있어 설정을 더욱 쉽게 관리할 수 있습니다.

Seafile 5.0.0으로 업그레이드하면, 업그레이드 스크립트는 **conf/** 폴더에 이 설정 파일을 한데 모아놓습니다.

