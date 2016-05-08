# 파일 검색 세부 안내

**참고**: Seafile 서버 5.0.0부터 모든 설정 파일은 **conf** 폴더로 한 곳에 옮겨 모아둡니다. [더 읽어보십시오](../deploy/new_directory_layout_5_0_0.md).

## <a id="search-opt"></a>검색 설정 항목

**seafevents.conf** 파일에 다음 설정 항목을 넣어야 하며, 바꾼 설정을 적용하려면 Seafile과 Seahub를 다시 시작해야합니다.

```
[INDEX FILES]
...
# Enable full-text search for PDF/Word/PPT
index_office_pdf = false

```

## 기존 ElasticSearch 서버 활용

엘리스틱 서치 서버를 사용하는 검색 모듈은 Seafile 전문가판 서버 타르볼에 들어있습니다. 그러나 엘라스틱서치 서버 또는 클러스터가 업체에서 이미 실행중일 지도 모릅니다. 이 상황에서는 기존의 엘라스틱서치 서버 또는 클러스터를 사용하도록 설정 파일을 바꿀 수 있습니다.

이 기능은 `Seafile 전문가판 서버 2.0.5`부터 추가했습니다.

### 참고

- ES 클러스터에 thrift 전송 플러그인을 설치해야 합니다. 설치하지 않았다면, 설치하십시오:

```
bin/plugin -install elasticsearch/elasticsearch-transport-thrift/1.6.0
```

그 다음 ES 서버를 다시 시작하십시오.

- 현재 Seafile 검색 모듈은 ES 서버 설정을 통해 기본 분석 프로그램을 활용합니다. 


### 설정 파일 설정 바꾸기

- `seafevents.conf`를 편집하여 **[INDEX FILES]** 섹션에 지정 ES 서버 호스트 및 포트를 추가하십시오:

```
vim seafevents.conf
```

```
[INDEX FILES]
...
es_host = 192.168.1.101
es_port = 9500
```

- `es_host`: ES 서버의 IP 주소
- `es_port`: Thrift 전송 모듈의 요청 대기 포트. 기본적으로 `9500` 입니다

## <a id="wiki-faq"></a>일반 문제

### <a id="how-to-rebuild-search-index"></a>문제 발생시 색인 재구성 방법

다음 명령으로 검색 색인을 재구성할 수 있습니다:

```
./pro/pro.py search --clear
./pro/pro.py search --update
```

이 명령이 동작하지 않으면 다음 절차를 따라 해결할 수 있습니다:

1. Seafile을 멈추십시오
2. `rm -rf pro-data/search` 명령으로 이전 검색 색인을 제거하십시오
3. Seafile을 다시 시작하십시오
4. 1분 정도 기다린 후 `./pro/pro.py search --update` 명령을 실행하십시오


### <a id="wiki-search-no-result"></a>검색어로 검색할 때 결과가 없음

검색 색인은 기본적으로 매 10분마다 업데이트 합니다. 따라서 색인 업데이트를 처음 수행하기 전에는 어떤 결과도 나타나지 않습니다.

  즉시 검색할 수 있게 하려면,

  - Seafile 서버를 시작했는지 확인하십시오
  - 검색 색인을 직접 업데이트 하십시오:
```
      cd haiwen/seafile-pro-server-2.0.4
     ./pro/pro.py search --update
```

### <a id="wiki-cannot-search-encrypted-files"></a>암호화 파일을 검색할 수 없음

서버에서 암호화한 파일은 그 자체로 암호화 상태이기 때문에 색인 처리할 수 없습니다.

