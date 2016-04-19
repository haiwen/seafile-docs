# 구성 요소 둘러보기

Seafile 서버는 다음 항목으로 구성되어 있습니다:

- **Seahub**(장고)：웹사이트입니다.  Seafile 서버에는 웹 사이트를 제공하는 경량 파이썬 HTTP 서버 구니콘이 있습니다. 기본적으로 Seahub는 구니콘의 프로그램으로 동작합니다. nginx 또는 아파치 뒤에서 fast-cgi 모드로 Seahub를 실행하도록 설정할 수 있습니다.
- **Seafile server** (``seaf-server``)：원시 파일의 업로드/다운로드/동기화를 처리하는 데이터 서비스 데몬입니다. Seafile 서버는 기본적으로 8082 포트에서 요청을 대기합니다. nginx/아파치를 설정하여 로컬 8082 포트로 요청을 우회하도록 설정할 수 있습니다.
- **ccnet server** (``ccnet-server``)： 다중 구성요소간 통신을 활성화하는 RPC 서비스 데몬입니다. ccnet은 자체 내부 통신용으로만 사용합니다.

다음 그림은 nginx/아파치 뒤에서 Seafile을 가동하도록 설정했을 때 Seafile 클라이언트의 파일 접근 방식을 나타냅니다.

![Seafile 동기화](../images/seafile-arch-new-http.png)

- Seafile 서비스의 모든 접근(Seahub 및 Seafile 서버 포함) 설정은 nginx 또는 아파치 웹 서버 뒤에서 동작하도록 설정할 수 있습니다. 이 방식으로 서비스로 전달할 모든 네트워크 트래픽을 HTTPS 방식으로 암호화할 수 있습니다.
- 사용자가 Seahub로 접근하면, Seahub는 ccnet RPC를 통해 Seafile 서버의 데이터로 접근합니다.

