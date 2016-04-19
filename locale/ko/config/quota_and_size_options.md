# 용량 제한 및 기타 설정 항목

**참고**: Seafile 서버 5.0.0 부터 모든 설정 파일은 **conf** 폴더로 옮겨 모아놓습니다. [좀 더 읽어보십시오](../deploy/new_directory_layout_5_0_0.md).

#### 용량 제한

모든 사용자에 대해 기본 제한 용량(2GB)을 설정할 수 있습니다. 이 제한 용량을 설정하려면 [seafile.conf](../config/seafile-conf.md) 파일에 다음 줄을 추가하십시오.

<pre>
[quota]
# default user quota in GB, integer only
default = 2
</pre>

커뮤니티판 5.0.5 이후에는 KB, MB, GB, TB 단위로 기본 제한 용량을 설정할 수 있습니다. 예를 들면,

```
[quota]
default = 200MB
```

참고로 1TB = 1000GB = 1000*1000MB 등 입니다.

이 설정은 모든 사용자에게 적용합니다. 특정 사용자에게 제한 용량을 설정하려면, Seahub 웹사이트에 관리자 권한으로 설정한 후 "시스템 관리자" 페이지에서 설정하십시오.

#### 기본 기록 분량 제한(seafile.conf)

모든 파일 리비전 기록을 유지하고 싶지 않다면 모든 라이브러리의 기본 기록 제한 분량을 설정할 수 있습니다. `seafile.conf`에서:

<pre>
[history]
keep_days = days of history to keep
</pre>


#### 업로드/다운로드 파일 크기 제한 설정 값 바꾸기

`seafile.conf`에서:

<pre>
[fileserver]
# Set maximum upload file size to 200M.
max_upload_size=200

# Set maximum download directory size to 200M.
max_download_dir_size=200
</pre>

