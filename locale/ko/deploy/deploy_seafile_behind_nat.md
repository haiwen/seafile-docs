# NAT 뒤에서 Seafile 가동

대부분의 사용자는 LAN에서 Seafile 서버를 가동하고 WAN에서 접근하려고 합니다.

이 설정을 해결하려면 다음 항목이 필요합니다:

- 포트 포워딩을 지원하는 라우터
- 동적 DNS 서비스 활용
- Seafile 서버 설정 수정

### 목차

- [서버 설치](deploy_Seafile_behind_NAT.md#setup-the-server)
- [라우터에서 포트 포워딩 설정](deploy_Seafile_behind_NAT.md#setup-port-forwarding-in-your-router)
- [동적 DNS 서비스 활용](deploy_Seafile_behind_NAT.md#use-a-dynamic-dns-serivce)
- [Seafile 설정 수정](deploy_Seafile_behind_NAT.md#modify-your-seafile-configuration)


## 서버 설정

우선 [Seafile 서버 다운로드 및 설치](using_sqlite.md)의 안내를 따라 Seafile 서버를 설치하십시오.

계속하기 전, 다음을 확인하십시오:

- Seahub 웹사이트를 볼 수 있는가
- Seafile 클라이언트에서 라이브러리를 다운로드하고 동기화할 수 있는가

## 라우터의 포트 포워딩 설정

### 라우터의 포트 포워딩 기능 지원 확인

우선 라우터에서 포트 포워딩 기능을 지원하는지 확인하십시오.

- 라우터의 웹 관리자 페이지에 로그인하십시오. 어떻게 하는지 모르겠다면 라우터의 설명서 페이지 절차를 찾아보십시오. 설명서가 없다면 XXX 대신의 라우터 브랜드 이름을 넣어 **"XXX 라우터 관리 페이지"** 를 구글에서 검색하십시오.

- 관리자 페이지를 찾아보신 후, "포워딩", "고급"과 같은 단어가 있는 태그가 있는지 확인하십시오. 라우터에서 해당 기능을 지원한다면 포트 포워딩 관련 설정을 찾을 수 있습니다.

### 포트 포워딩 규칙 설정

Seafile 서버는 다양한 구성 요소로 이루어져있습니다. 다음의 모든 항목에 대해 포트 포워딩을 설정해야합니다.

<table>
<tr>
  <th>구성요소</th>
  <th>기본 포트 번호</th>
</tr>
<tr>
  <td>fileserver</td>
  <td>8082</td>
</tr>
<tr>
  <td>seahub</td>
  <td>8000</td>
</tr>
</table>

* Apache/Nginx 뒤에서 Seafile을 가동한다면 8000번과 8002번 포트를 열 필요가 없습니다.
* 기본 포트를 사용하지 않으면 자체 개별 설정에 따라 테이블 설정을 수정해야합니다.

### 포트 포워딩 기능 동작시 시험 방법

라우터의 포트 포워딩 규칙을 설정한 후 다음 절차를 따라 동작 여부를 확인할 수 있습니다:

- 명령 프롬프트를 여십시오
- WAN IP를 조사하십시오. WAN IP를 확인하는 간편한 방법은 WAN IP를 보여주는 `http://who.is`에 방문하는 방편입니다.
- Seahub 서버에 연결해보십시오
````
telnet <Your WAN IP> 8000
```

포트 포워딩이 동작하면 상단 명령이 제대로 동작해야 합니다. 그렇지 않으면 *connection refused* 또는 *connection timeout* 같은 메시지가 나타납니다.

포트 포워딩이 동작하지 않으면, 다음 이유에서일 지도 모릅니다:

- 포트 포워딩을 잘못 설정했습니다
- 라우터를 다시 시작해야합니다
- 네트워크 연결이 끊어졌을 수도 있습니다

### SERVICE_URL 설정

`ccnet.conf`의 "SERVICE_URL"은 파일을 온라인에서 탐색할 때와 파일의 다운로드/업로드 링크를 만들 때 사용합니다. WAN IP로 설정하십시오.

```
SERVICE_URL = http://<Your WAN IP>:8000
```

대부분 라우터에서는 NAT 루프백을 지원합니다. 인트라넷에서 Seafile 웹에 접근한다면 외부 IP를 사용해도 파일 다운로드/업로드는 여전히 동작합니다.

## 동적 DNS 서비스 사용

### 왜 동적 DNS(DDNS) 서비스를 활용하죠?

위 모든 과정이 끝나면 LAN 외부에서 WAN IP로 Seahub 서버에 접근할 수 있어야합니다. 하지만 대부분 사람에게 WAN IP 주소는 보통 이런 접근 방식을 활용하지 못하게 ISP(인터넷 서비스 제공 업체)에서 바꿉니다.

이 문제를 해결할 목적으로 동적 DNS(DDNS) 서비스를 활용할 수 있습니다. 동적 DNS 서비스를 활용하면, (IP 주소 대신)도메인 이름으로 Seahub 사이트에 접근할 수 있으며, IP 주소가 항시 바뀌더라도 도메인 이름을 WAN IP 주소에 항상 매핑할 수 있습니다.

인터넷에 여러 동적 DNS 서비스 제공 업체가 있습니다. 어떤 서비스를 선택할지 모르겠다면, 저희가 테스트 해본 결과 잘 동작하는[www.noip.com](http://www.noip.com)을 추천합니다.

세부 과정은 이 위키의 범위를 벗어납니다. 하지만 기본적으로 다음 과정을 진행해야합니다:

1. DDNS 서비스 제공 업체를 선정하십시오
2. DDNS 서비스 제공 업체 웹사이트에 가입하십시오
3. DDNS 서비스 제공 업체의 클라이언트를 다운로드 받고 WAN IP에 항상 도메인 이름을 매핑한 상태로 유지하십시오

## Seafile 설정 수정

DDNS 서비스 설정이 끝나면, `ccnet.conf` 설정을 수정해야합니다:

```
SERVICE_URL = http://<Your dynamic DNS domain>:8000
```

설정 수정 후 Seafile 서버를 다시 시작하십시오.

