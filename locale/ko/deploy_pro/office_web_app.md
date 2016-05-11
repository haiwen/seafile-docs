# 오피스 웹 앱

전문가 버전 4.4.0(이상) 에서는 온라인 에서 문서를 미리볼 때 마이크로소프트 오피스 웹 앱을 활용할 수 있습니다. 오피스 웹 앱에서는 모든 오피스 형식 파일을 가장 멋지게 미리볼 수 있습니다. 마이크로소프트 오피스 볼륨 라이선스를 보유한 조직에서는 오피스 웹 앱을 무료로 사용할 수 있습니다. 오피스 웹 앱 추가 정보와 구동 방법은 https://technet.microsoft.com/en-us/library/jj219456.aspx 주소를 참고하십시오.

Seafile의 자체 오피스 파일 미리 보기는 여전히 기본 기능입니다. 오피스 웹 앱 을 미리보기 기능에 사용하려면 seahub_settings.py에 다음 설정을 추가하십시오.

``` python
# Enable Office Web App
ENABLE_OFFICE_WEB_APP = True

# Url of Office Web App's discovery page
# The discovery page tells Seafile how to interact with Office Web App when view file online
# You should change `http://example.office-web-app.com` to your actual Office Web App server address
OFFICE_WEB_APP_BASE_URL = 'http://example.office-web-app.com/hosting/discovery'

# Expiration of WOPI access token
# WOPI access token is a string used by Seafile to determine the file's
# identity and permissions when use Office Web App view it online
# And for security reason, this token should expire after a set time period
WOPI_ACCESS_TOKEN_EXPIRATION = 30 * 60 # seconds

# Tuple of file format that you want to view through Office Web App
# You can change this value according to your preferences
# And of course you should make sure your Office Web App support to preview
# the specified extension file you add below
OFFICE_WEB_APP_FILE_EXTENSION = ('ods', 'xls', 'xlsb', 'xlsm', 'xlsx','ppsx', 'ppt',
    'pptm', 'pptx', 'doc', 'docm', 'docx')

# Enable edit file through Office Web App
ENABLE_OFFICE_WEB_APP_EDIT = True

# Currently we only support `xlsx` and `pptx`
# type of file editing through Office Web App
OFFICE_WEB_APP_EDIT_FILE_EXTENSION = ('xlsx', 'pptx')

```

그 다음 다시 시작하십시오

```
./seafile.sh restart
./seahub.sh restart
```

seahub_settings.py에 지정한 문서를 누르고 나면 새 미리보기 페이지가 뜹니다.

![office-web-app](../images/office-web-app.png)

## 문제 해결

웹 앱 통합 동작 방식를 이해하면 문제를 찾는데 도움이 됩니다. 사용자가 파일 페이지에 방문했을 때:

1. (seahub->브라우저) Seahub는 iframe에 들어간 페이지를 만들고 브라우저에 보냅니다
2. (브라우저->오피스 웹 앱) iframe으로 브라우저에서 오피스 웹 앱의 파일 미리보기 페이지를 불러옵니다
3. (오피스 웹 앱->Seahub) 오피스 웹 앱에서 요청을 받고 Seahub에 파일 내용 요청을 보냅니다
4. (오피스 웹 앱->브라우저) 오피스 웹 앱에서 브라우저로 파일 미리보기 페이지를 보냅니다.

Seahub(3단계 과정) 및 오피스 웹 앱 처리 단계중 어떤 단계에 문제가 있는지는 Nginx 로그를 확인하십시오.

