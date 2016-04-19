# 자주 묻는 질문

## 파일 동기화 관련 질문

#### 라이브러리를 다운로드할 때 "서버 연결 중"에서 클라이언트가 멈춤

우선 Seafile 클라이언트 로그(리눅스에서는 `~/.ccnet/logs/seafile.log`, 윈도우에서는 `C:/users/your_name/ccnet/logs/seafile.log`)를 확인하여 문제를 살펴볼 수 있습니다.

가능성 있는 이유는 다음과 같습니다:

* 방화벽: 방화벽을 올바르게 설정했는지 확인하십시오. [Seafile 서버용 방화벽 설정](deploy/using_firewall.md)을 참고하십시오

#### 클라이언트 측에서 더 자세한 로그 정보를 추가하는 방법

Seafile 데스크톱 클라이언트를 실행하기 전 `SEAFILE_DEBUG = all` 환경 변수를 설정하십시오. 라눅스에서, 터미널을 열어 다음 명령을 입력할 수 있습니다: 

```
export SEAFILE_DEBUG=all
./seafile-applet
```

## 서버 설정 관련 질문

#### 온라인 파일 업로드/다운로드 실패

* Seafile 파일 서버에 맞춰 방화벽을 열어두었는지 확인하십시오.
* ccnet.conf의 `SERVICE_URL`과 seahub_settings.py의 `FILE_SERVER_ROOT`를 올바르게 설정했는지 확인하십시오.
* 크롬/파이어폭스 디버깅 모드로 다운로드 단추를 눌렀을 때 어떤 링크가 나타나는지 이 링크에 어떤 문제가 있는지 확인하십시오

#### Seafile 서버에서 파이썬 3을 지원하나요?

아니요, 서버에 파이썬 2.6.5 이상 또는 2.7 버전을 설치해야합니다.

#### FreeBSD에서 Seafile 서버를 실행할 수 있을까요?

인터넷에 검증되지 않은 방법이 있으며, 이 방법은 나중에 정리하겠습니다.
(FreeBSD에서 Seafile 설치에 성공하면 설치 과정을 설명할 것.)

#### 웹사이트에 "페이지를 찾을 수 없음"이라고 뜨는데 어떻게 하죠?

* Seahub 로그 파일(`installation folder/logs/seahub_django_request.log`)을 역추적하여 확인할 수 있습니다

* 또한 seahub_settings.py에 <code>DEBUG = True</code> 설정을 추가하고 <code>./seahub.sh restart</code> 명령으로 seahub를 다시 시작한 다음 페이지를 새로 고쳐 모든 디버깅 정보를 화면에 표시하여 디버깅 기능을 활성화할 수 있습니다. ./seahub.sh를 ./seahub.sh start-fastcgi 명령으로 시작했는지 확인하십시오.

#### 아바타 그림이 vanished 됐는데 어떻게 하죠?

* seahub/media/의 "avatars" 심볼릭 링크를 ../../../seahub-data/avatars에 올바르게 연결했는지 확인하십시오. 올바르게 연결하지 않았다면, [Seafile 서버 업그레이드](deploy/upgrade.md)의 "마이너 버전 업그레이드"를 따라 링크를 고쳐야합니다.

* 아바타 링크를 올바르게 연결했고 아바타가 여전히 깨져있으면 `rm -rf /tmp/seahub_archive/*` 명령으로 seahub 캐시를 새로 고치십시오

#### 설치 후 seafile-data 위치를 어떻게 바꾸죠?

ccnet의 seafile.ini 파일을 수정하십시오. 이 파일에 seafile-dasta 위치가 들어있습니다. seafile-data 위치를 `/opt/new/seafile-data`와 같은 다른 위치로 이동하십시오. 그 다음 파일을 올바르게 수정하십시오.

#### 전자메일 전송에 실패했는데 어떻게 하죠?

logs/seahub.log를 확인하십시오.

보통 저지르는 몇가지 실수가 있습니다:

1. `EMAIL_HOST_USER = XXX`와 같은 부분이 `EMAIL_HOST_USER = 'XXX'`로 설정해야 하는 상황에서 작은 따옴표를 빠뜨린 식으로 설정 입력이 잘못되었는지 확인하십시오.
1. 메일 서버가 동작하지 않을 수 있습니다.

#### 업그레이드가 끝난 후 CSS 파일을 불러오지 못하여 웹 UI가 깨집니다

`rm -rf /tmp/seahub_cache/*` 명령으로 캐시를 제거 후 다시 시도하십시오. memcached 를 설정했다면, memcached를 다시 시작한 후 seahub를 다시 시작하십시오.

문제를 해결하지 못했다면 seafile-server-latest 심볼릭 링크가 올바른 폴더를 가리키는지 확인하십시오. 그 다음 `seafile-server-latest/seahub/media/CACHE` 위치를 올바르게 만들었는지 확인하십시오(자동으로 만든 CSS 파일이 들어갑니다).

## 클러스터링 관련 질문

### 첫 노드에만 seahub/media/CACHE를 만들어 페이지 배치가 깨집니다

다음 설정을 추가하십시오

    COMPRESS_CACHE_BACKEND = 'locmem://'

http://manual.seafile.com/deploy_pro/deploy_in_a_cluster.html 문서에 언급한대로 seahub_settings.py를 실행하십시오

이 명령은 모든 노드의 자체 로컬 폴더에 CSS 캐시를 만들도록 지시합니다.


## 서버 운영 관련 질문

### 한 계정에서 다른 계정으로 라이브러리 및 그룹을 어떻게 옮길까요?

4.4.2 버전 부터 시스템 관리자는 [RESTful 웹 API](https://github.com/haiwen/seafile-docs/blob/master/develop/web_api.md#migrate-account)를 활용하여 어떤 계정에서 기존의 다른 계정으로 라이브러리 및 그룹을 옮길 수 있습니다.

### Seafile GC에서 FSCK cannot fix them 오류가 뜹니다

GC는 이전 기록을 검사합니다. 하지만 FSCK는 현재 버전만 검사합니다. 이 오류를 무시할 수 있습니다. 사소한 문제일 뿐입니다.

## LDAP 및 사용자 관리 관련 질문

### AD에서 계정별 Seafile 접근 권한을 제한하는 방법

`ccnet.conf` 에서 LDAP 설정에 FILTER 필드를 사용할 수 있습니다. 예를 들어 다음 필터는 그룹 구성원의 Seafile 접근 권한을 제한합니다.

    FILTER = (memberOf=cn=group,cn=users,DC=x)

AD는 그룹의 그룹 기능을 지원합니다. 다음 필터는 그룹의 구성원/그룹의 Seafile 접근을 제한합니다.

    FILTER = (memberOf:1.2.840.113556.1.4.1941:=cn=group,cn=users,DC=x)

필터 문법 정보는, http://msdn.microsoft.com/en-us/library/aa746475%28VS.85%29.aspx를 참고하십시오

