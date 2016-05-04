# 설정 항목

**참고**: Seafile 서버 5.0.0부터 모든 설정 파일은 **conf** 폴더로 한 곳에 옮겨 모아둡니다. [더 읽어보십시오](../deploy/new_directory_layout_5_0_0.md).

`seafevents.conf` 파일에서:

```
[Audit]
## Audit log is disabled default.
enabled = true

[INDEX FILES]
## must be "true" to enable search
enabled = true

## The interval the search index is updated. Can be s(seconds), m(minutes), h(hours), d(days)
interval=10m

## If true, index the contents of office/pdf files while updating search index
## Note: If you change this option from "false" to "true", then you need to clear the search index and update the index again. See the FAQ for details.
index_office_pdf=false

[SEAHUB EMAIL]

## must be "true" to enable user email notifications when there are new new unread notifications
enabled = true

## interval of sending seahub email. Can be s(seconds), m(minutes), h(hours), d(days)
interval = 30m


[OFFICE CONVERTER]

## must be "true" to enable office/pdf file online preview
enabled = true

## How many libreoffice worker processes to run concurrenlty
workers = 1

## where to store the converted office/pdf files. Deafult is /tmp/.
outputdir = /tmp/

## how many pages are allowed to be previewed online. Default is 50 pages
max-pages = 50

## the max size of documents to allow to be previewed online, in MB. Default is 2 MB
## Preview a large file (for example >30M) online will freeze the browser.
max-size = 2

```

### <a id="wiki-options-you-may-want-to-modify"></a>수정할 설정 항목

위 섹션에서는 `seafevents.conf`에 있는 모든 옵션을 언급했습니다. 대부분의 경우 기본 설정을 활용할 수 있습니다. 하지만 개별 상황에 맞추어 일부 설정을 수정해야 할 때도 있습니다.

다음 표를 통해 설정 항목을 나열하고 왜 기본값을 사용해야 하는지 언급하겠습니다.

<table>
<tr>
<th>섹션</th>
<th>설정항목</th>
<th>기본값</th>
<th>설명</th>
</tr>

<tr>
<td>INDEX FILES</td>
<td>index_office_pdf</td>
<td>false</td>
<td>
오피스/pdf 문서의 전체 단어 검색은 기본적으로 활성화 상태가 아닙니다. 검색 색인에 약간의 저장장치 공간을 차지하기 때문입니다. 활성화하려면, 이 값을 "true"로 설정하고 검색 색인을 다시 만드십시오. 자세한 내용은 [Seafile 전문가판 서버 자주 묻는 질문](faq_for_seafile_pro_server.md)을 참고하십시오.
</td>
</tr>

<tr>
<td>OFFICE CONVERTER</td>
<td>max-size</td>
<td>2</td>
<td>
온라인 미리보기 파일 최대 허용 크기는 2MB입니다. 미리보기 기능은 오피스/pdf 파일을 HTML로 변환하고 브라우저에 보여줍니다. 파일 크기가 너무 크면 변환에 시간이 오래 걸리고 상당한 용량을 소비합니다
</td>
</tr>

<tr>
<td>OFFICE CONVERTER</td>
<td>max-pages</td>
<td>50</td>
<td>
오피스/pdf 문서를 온라인에서 미리 볼 때, 첫 50 페이지를 보여줍니다. 값이 너무 크면 변환에 시간이 오래 걸리고 상당한 용량을 소비합니다.
</td>
</tr>

</table>

