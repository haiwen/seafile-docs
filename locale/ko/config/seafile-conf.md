# Seafile.conf 설정

**참고**: Seafile 서버 5.0.0 부터 모든 설정 파일은 **conf** 폴더로 옮겨 모아놓습니다. [좀 더 읽어보십시오](../deploy/new_directory_layout_5_0_0.md).

## 저장소 용량 제한 설정(seafile.conf)

모든 사용자의 기본 제한 용량(2GB)을 설정할 수 있습니다. 이 제한 용량을 설정하려면 `seafile.conf` 파일에 다음 줄을 추가하십시오

<pre>
[quota]
# default user quota in GB, integer only
default = 2
</pre>

이 설정은 모든 사용자에게 적용합니다. 특정 사용자에게 제한 용량을 설정하려면, Seahub 웹사이트에 관리자 권한으로 설정한 후 "시스템 관리자" 페이지에서 설정하십시오.

## 기본 기록 분량 제한(seafile.conf)

모든 파일 리비전 기록을 유지하고 싶지 않다면, 모든 라이브러리의 기본 기록 제한 분량을 설정할 수 있습니다.

<pre>
[history]
keep_days = days of history to keep
</pre>

## Seafile 파일 서버 설정(seafile.conf)

Seafile 파일 서버의 설정은 `seafile.conf` 파일의 <code>[fileserver]</code> 섹션에 있습니다

<pre>
[fileserver]
# bind address for fileserver, default to 0.0.0.0
host = 0.0.0.0
# tcp port for fileserver
port = 8082
</pre>

업로드/다운로드 설정 바꾸기.

<pre>
[fileserver]
# Set maximum upload file size to 200M.
max_upload_size=200

# Set maximum download directory size to 200M.
max_download_dir_size=200
</pre>

웹 인터페이스 또는 클라이언트 클라우드 파일 브라우저에서 파일을 업로드한 후, 고정 길이 블록으로 나누어 저장소 백엔드에 저장합니다. 이를 "색인 처리" 과정이라고 합니다. 기본적으로 파일 서버는 파일 순차 색인 처리에 스레드 하나를 사용하고 블록을 하나 하나 저장합니다. 대부분의 경우 이런 방식이 적당합니다. 다만 S3/Ceph/Swift 백엔드가 있다면, 여러 블록을 동시에 저장하기 위해 저장소 백엔드에 더 많은 대역폭이 필요합니다. 색인화 과정에서 동시 처리 스레드 수를 지정하는 설정 항목을 제공합니다:

```
[fileserver]
max_indexing_threads = 10
```

Seahub에서 zip 압축 파일로 폴더를 다운로드할 수 있지만, 일부 윈도우용 zip 프로그램에서 UTF-8을 지원하지 않는 경우, "windows_encoding" 설정으로 이 문제를 해결할 수 있습니다.
<pre>
[zip]
# The file name encoding of the downloaded zip file.
windows_encoding = iso-8859-1
</pre>

## MySQL 연결 풀 크기 설정 바꾸기

MySQL을 사용하도록 Seafile 서버를 설정할 때 기본 연결 풀 갯수는 100이며, 대부분의 경우 충분합니다. seafile.conf에 다음 옵션을 추가하여 이 값을 바꿀 수 있습니다:

```
[database]
......
# Use larger connection pool
max_connections = 200
```

**참고**: 바뀐 설정을 다시 적용하려면 Seafile 및 Seahub 를 다시 시작해야합니다.
<pre>
./seahub.sh restart
./seafile.sh restart
</pre>

