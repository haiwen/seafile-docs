# Seafile 네트워크 설정(ccnet.conf)

**참고**: Seafile 서버 5.0.0 부터 모든 설정 파일은 **conf** 폴더로 옮겨 모아놓습니다. [좀 더 읽어보십시오](../deploy/new_directory_layout_5_0_0.md).

`ccnet.conf` 파일을 수정하여 Seafile의 네트워크 설정 항목 값을 바꿀 수 있습니다. 예쩨를 통해 설정 항목을 차근차근 살펴보겠습니다.

<pre>
[General]

# Used internally. Don't delete.
ID=eb812fd276432eff33bcdde7506f896eb4769da0

# Used internally. Don't delete.
NAME=example

# This is outside URL for Seahub(Seafile Web). 
# The domain part (i.e., www.example.com) will be used in generating share links and download/upload file via web.
# Note: Outside URL means "if you use Nginx, it should be the Nginx's address"
SERVICE_URL=http://www.example.com:8000


[Network]
# Not used anymore
PORT=10001

[Client]
# Not used anymore
PORT=13419

</pre>

**참고**: 바꾼 설정 항목 값을 적용하려면 Seafile을 다시 시작해야합니다.

<pre>
cd seafile-server
./seafile.sh restart
</pre>

## MySQL 연결 풀 크기 설정 바꾸기

MySQL을 사용하도록 Seafile 서버를 설정할 때 기본 연결 풀 갯수는 100이며, 대부분의 경우 충분합니다. ccnet.conf에 다음 옵션을 추가하여 이 값을 바꿀 수 있습니다:

```
[Database]
......
# Use larger connection pool
MAX_CONNECTIONS = 200
```

