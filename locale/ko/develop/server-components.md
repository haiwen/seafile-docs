# Seafile 서버 구성 요소

Seafile 서버는 다음 서비스로 이루어져있습니다.

* **Ccnet 데몬** (클라이언트용 ccnet 또는 서버용 ccnet-server)：네트워크 서비스 데몬. 초기 설계에서는, 트래픽 버스처럼 동작했습니다. 클라이언트, 서버, 각각의 구성요소간 자체 트래픽은 ccnet으로 처리합니다. 차후 개발 과정에서 Seafile 데몬 구성요소를 직접 활용하여 파일 전송을 개선할 수 있다는 점을 알아냈습니다.
* **Seafile 데몬**：데이터 서비스 데몬
* **Seahub**：웹사이트. Seafile 서버 꾸러미에는 웹사이트 서비스를 제공하는 경량 파이썬 HTTP 서버 `gunicorn`이 있습니다. Seahub는 gunicorn에서 프로그램을 실행합니다.
* **FileServer**: Seahub의 원시 파일 업로드/다운로드 기능을 처리합니다. gunicorn이 대형 파일 처리 성능이 딸리기 때문에, 원사 피알 업로드/다운로드 기능은 C 프로그래밍 언어로 "FileServer"로 작성했습니다.
* **Controller**: ccnet과 Seafile 데몬 감시 프로그램이며, 필요할 때 다시 시작합니다.

**하단 그림은 Seafile 서버와 Seafile 데스크톱 클라이언트가 어떻게 파일을 동기화하는지 보여줍니다**:

![seafile-sync-arch](../images/seafile-sync-arch.png)

<br/>

**아래 그림은 Seafile 모바일 클라이언트가 Seafile 서버와 서로 동작하는 방식을 보여줍니다**:

![mobile-arch](../images/mobile-arch.png)

<br/>

**하단 그림에서는 Nginx/Apache 후부에 Seafile 서버가 있을 경우 Seafile 모바일 클라이언트와 동작하는 방식을 보여줍니다**:

![mobile-nginx-arch](../images/mobile-nginx-arch.png)

