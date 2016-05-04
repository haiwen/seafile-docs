# 웹 API (Seafile 서버 v5.1.0 이상)


<p>
<div class="toc">
<ul>

<li>
<a href="#seafile-web-api">Seafile 웹 API</a>
<ul>

    <li><a href="#api-basics">API 기본</a></li>
    <li><a href="#status-code">상태 코드</a></li>
    <li><a href="#quick-start">간편 시작</a></li>

    <li>
        <a href="#account">계정</a>
        <ul>
            <li><a href="#check-account-info">계정 정보 확인</a></li>
            <li><a href="#server-info">서버 정보 확인</a></li>
        </ul>
    </li>

    <li>
        <a href="#starred-files">별표 표시 파일</a>
        <ul>
            <li><a href="#list-starred-files">별표 표시 파일 조회</a></li>
            <li><a href="#star-a-file">파일 별표 표시</a></li>
            <li><a href="#unstar-a-file">파일 별표 표시 해제</a></li>
        </ul>
    </li>

    <li>
        <a href="#group">그룹 </a>
        <ul>
            <li><a href="#list-groups">그룹 조회</a></li>
            <li><a href="#add-a-group">그룹 추가</a></li>
            <li><a href="#get-info-of-a-group">그룹 정보 확인</a></li>
            <li><a href="#rename-a-group">그룹 이름 바꾸기</a></li>
            <li><a href="#transfer-a-group">그룹 양도</a></li>
            <li><a href="#delete-a-group">그룹 삭제</a></li>
            <li><a href="#quit-group">그룹 탈퇴</a></li>
            <li>
                <a href="#group-member">그룹 구성원</a>
                <ul>
                    <li><a href="#list-group-members">그룹 구성원 조회</a></li>
                    <li><a href="#add-a-group-member">그룹 구성원 추가 </a></li>
                    <li><a href="#bulk-add-group-members">여러 그룹 구성원 추가</a></li>
                    <li><a href="#get-info-of-a-group-member">그룹 구성원 정보 확인</a></li>
                    <li><a href="#set-a-group-member-admin">그룹 구성원 관리자 설정</a></li>
                    <li><a href="#unset-a-group-member-admin">그룹 구성원 관리자 설정 해제</a></li>
                    <li><a href="#delete-a-group-member">그룹 구성원 삭제</a></li>
                </ul>
            </li>
            <li>
                <a href="#group-message">그룹 메시지</a>
                <ul>
                    <li><a href="#get-group-messages">그룹 메시지 확인</a></li>
                    <li><a href="#get-group-message-detail">그룹 메시지 세부 정보 확인</a></li>
                    <li><a href="#send-a-group-message">그룹 메시지 보내기</a></li>
                    <li><a href="#reply-a-group-message">그룹 메시지 답장</a></li>
                    <li><a href="#get-group-message-replies">그룹 메시지 답장 확인</a></li>
                </ul>
            </li>
        </ul>
    </li>

    <li>
        <a href="#share">공유</a>
        <ul>
            <li>
                <a href="#share-link">공유 링크 </a>
                <ul>
                    <li><a href="#list-share-links">공유 링크 확인</a></li>
                    <li><a href="#create-share-link">공유 링크 만들기</a></li>
                    <li><a href="#delete-share-link">공유 링크 삭제</a></li>
                    <li><a href="#send-share-link-email">공유 링크 전자메일로 보내기</a></li>
                    <li><a href="#list-direntry-in-dir-download-link">디렉터리 다운로드 링크에서 디렉터리 항목 조회</a></li>
                </ul>
            </li>
            <li>
                <a href="#upload-link">업로드 링크</a>
                <ul>
                    <li><a href="#list-upload-links">업로드 링크 조회</a></li>
                    <li><a href="#create-upload-link">업로드 링크 만들기</a></li>
                    <li><a href="#delete-upload-link">업로드 링크 삭제</a></li>
                    <li><a href="#send-upload-link-email">업로드 링크 전자메일로 보내기</a></li>
                </ul>
            </li>
            <li>
                <a href="#shared-libraries">공유 라이브러리</a>
                <ul>
                    <li><a href="#list-shared-libraries">공유 라이브러리 조회</a></li>
                    <li><a href="#list-be-shared-libraries">공유한 라이브러리 조회</a></li>
                    <li><a href="#share-a-library">라이브러리 공유</a></li>
                    <li><a href="#unshare-a-library">라이브러리 공유 해제</a></li>
                </ul>
            </li>
        </ul>
    </li>

    <li>
        <a href="#library">라이브러리</a>
        <ul>
            <li><a href="#get-default-lib">기본 라이브러리 확인</a></li>
            <li><a href="#create-default-lib">기본 라이브러리 만들기</a></li>
            <li><a href="#list-libraries">라이브러리 조회</a></li>
            <li><a href="#get-library-info">라이브러리 정보 확인</a></li>
            <li><a href="#get-library-owner">라이브러리 소유자 확인</a></li>
            <li><a href="#get-library-history">라이브러리 기록 확인</a></li>
            <li><a href="#get-library-history-limit-days">라이브러리 기록 유지 제한 기간 확인</a></li>
            <li><a href="#set-library-history-limit-days">라이브러리 기록 유지 제한 기간 설정</a></li>
            <li><a href="#create-library">라이브러리 만들기</a></li>
            <li><a href="#check/create-sub-library">하위 라이브러리/검사만들기</a></li>
            <li><a href="#delete-library">라이브러리 삭제</a></li>
            <li><a href="#rename-library">라이브러리 이름 바꾸기</a></li>
            <li><a href="#transfer-library">라이브러리 양도</a></li>
            <li><a href="#decrypt-library">라이브러리 해독</a></li>
            <li><a href="#create-public-lib">공개 라이브러리 만들기</a></li>
            <li><a href="#remove-public-lib">공개 라이브러리 제거</a></li>
            <li><a href="#fetch-library-download-info">라이브러리 다운로드 정보 가져오기</a></li>
            <li><a href="#list-virtual-libraries">가상 라이브러리 조회</a></li>
            <li><a href="#search-libraries">라이브러리 검색</a></li>
            <li><a href="#get-library-download-links">라이브러리 다운로드 링크 확인</a></li>
            <li><a href="#get-library-upload-links">라이브러리 업로드 링크 확인</a></li>
            <li><a href="#delete-library-download-link">라이브러리 다룬로드 링크 삭제</a></li>
            <li><a href="#delete-library-upload-link">라이브러리 업로드 링크 삭제</a></li>
        </ul>
    </li>

    <li>
        <a href="#file">파일</a>
        <ul>
            <li><a href="#view-file-through-owa">오피스 웹 앱으로 파일 보기</a></li>
            <li><a href="#download-file">파일 다운로드</a></li>
            <li><a href="#get-file-detail">파일 세부 정보 확인</a></li>
            <li><a href="#get-file-history">파일 기록 확인</a></li>
            <li><a href="#download-file-revision">파일 특정 리비전 다운로드</a></li>
            <li><a href="#create-file">Create File</a></li>
            <li><a href="#rename-file">파일 이름 바꾸기</a></li>
            <li><a href="#lock-file">파일 잠금</a></li>
            <li><a href="#unlock-file">파일 잠금 해제</a></li>
            <li><a href="#move-file">파일 이동</a></li>
            <li><a href="#copy-file">파일 복사</a></li>
            <li><a href="#revert-file">파일 복원</a></li>
            <li><a href="#delete-file">파일 삭제</a></li>
            <li>
                <a href="#upload-file">파일 업로드 </a>
                <ul>
                    <li><a href="#get-upload-link">업로드 링크 확인</a></li>
                    <li><a href="#upload-file-1">파일 업로드</a></li>
                </ul>
            </li>
            <li>
                <a href="#update-file">파일 업데이트</a>
                <ul>
                    <li><a href="#get-update-link">업데이트 링크 확인</a></li>
                    <li><a href="#update-file-1">파일 업데이트</a></li>
                </ul>
            </li>
            <li><a href="#get-upload-blocks-link">블록 업로드 링크 확인</a></li>
            <li><a href="#get-update-blocks-link">블록 업데이트 링크 확인</a></li>
        </ul>
    </li>

    <li>
        <a href="#directory">디렉터리</a>
        <ul>
            <li><a href="#list-directory-entries">디렉터리 항목 조회</a></li>
            <li><a href="#create-new-directory">새 디렉터리 만들기</a></li>
            <li><a href="#rename-directory">디렉터리 이름 바꾸기 </a></li>
            <li><a href="#delete-directory">디렉터리 삭제</a></li>
            <li><a href="#download-directory">디렉터리 다운로드</a></li>
            <li><a href="#share-directory">디렉터리 공유</a></li>
        </ul>
    </li>

    <li>
        <a href="#multiple-files-directories">다중 파일 / 디렉터리</a>
        <ul>
            <li><a href="#multiple-files-directories-copy">복사</a></li>
            <li><a href="#multiple-files-directories-move">이동</a></li>
            <li><a href="#multiple-files-directories-delete">삭제</a></li>
        </ul>
    </li>

    <li>
        <a href="#avatar">아바타</a>
        <ul>
            <li><a href="#get-user-avatar">사용자 아바타 확인</a></li>
            <li><a href="#get-group-avatar">그룹 아바타 확인</a></li>
        </ul>
    </li>

    <li>
        <a href="#devices">장치</a>
        <ul>
            <li><a href="#get-user-devices">사용자 장치 확인</a></li>
            <li><a href="#unlink-user-device">사용자 장치 연결 해제</a></li>
        </ul>
    </li>

    <li><a href="#get-file-activities">파일 확동 확인</a></li>
    <li><a href="#get-thumbnail-image">썸네일 그림 확인</a></li>
    <li><a href="#add-organization">조직 추가</a></li>

</ul>
</li>

<li>
<a href="#admin-only">관리자 전용</a>
<ul>
    <li>
        <a href="#admin-only-account">계정</a>
        <ul>
            <li><a href="#admin-only-list-accounts">계정 조회</a></li>
            <li><a href="#admin-only-get-account">계정 정보 확인</a></li>
            <li><a href="#admin-only-create-account">계정 만들기</a></li>
            <li><a href="#admin-only-update-account">계정 업데이트</a></li>
            <li><a href="#admin-only-migrate-account">계정 이전</a></li>
            <li><a href="#admin-only-delete-account">계정 삭제</a></li>
        </ul>
    </li>

    <li>
        <a href="#admin-only-devices">장치</a>
        <ul>
            <li><a href="#admin-only-get-desktop-devices">데스크톱 장치 확인</a></li>
            <li><a href="#admin-only-get-mobile-devices">모바일 장치 확인</a></li>
            <li><a href="#admin-only-unlink-user-device">사용자 장치 연결 해제[</a></li>
            <li><a href="#admin-only-get-device-errors">장치 오류 확인</a></li>
            <li><a href="#admin-only-clean-device-errors">장치 오류 삭제</a></li>
        </ul>
    </li>

    <li>
        <a href="#admin-only-log">로그</a>
        <ul>
            <li><a href="#admin-only-get-login-log">로그인 로그 확인</a></li>
            <li><a href="#admin-only-get-file-audit-log">파일 감사 로그 확인</a></li>
            <li><a href="#admin-only-get-file-update-log">파일 업데이트 로그 확인</a></li>
            <li><a href="#admin-only-get-perm-audit-log">권한 감사 로그 확인</a></li>
        </ul>
    </li>
</ul>
</li>

</ul>
</div>
</p>

# <a id="seafile-web-api"></a>Seafile 웹 API #

## <a id="api-basics"></a>API 기본 ##

모든 API 호출은 유효한 Seafile API 키로 인증해야합니다.

    curl -H 'Authorization: Token 24fd3c026886e3121b2ca630805ed425c272cb96' https://cloud.seafile.com/api2/auth/ping/

API 키는 Auth API에서 제공할 수 있습니다. 자세한 내용은 <a href="#quick-start">간편 시작</a>을 참고하십시오.

각각의 API에서, 사용법을 `curl` 예제로 보여드립니다. `python` 및 `javascript` 예제도 보여드립니다. 자세한 내용은 https://github.com/haiwen/webapi-examples 를 참고하십시오.

## <a id="status-code"></a>상태 코드 ##

- 200: OK
- 201: CREATED
- 202: ACCEPTED
- 301: MOVED_PERMANENTLY
- 400: BAD_REQUEST
- 403: FORBIDDEN
- 404: NOT_FOUND
- 409: CONFLICT
- 429: TOO_MANY_REQUESTS
- 440: REPO_PASSWD_REQUIRED
- 441: REPO_PASSWD_MAGIC_REQUIRED
- 500: INTERNAL_SERVER_ERROR
- 520: OPERATION_FAILED

## <a id="quick-start"></a>간편 시작 ##

**ping**

    curl https://cloud.seafile.com/api2/ping/

    "pong"

**obtain auth token**

    curl -d "username=username@example.com&password=123456" https://cloud.seafile.com/api2/auth-token/

    {"token": "24fd3c026886e3121b2ca630805ed425c272cb96"}

**auth ping**

    curl -H 'Authorization: Token 24fd3c026886e3121b2ca630805ed425c272cb96' https://cloud.seafile.com/api2/auth/ping/

    "pong"

## <a id="account"></a>계정 ##

### <a id="check-account-info"></a>계정 정보 확인 ###

**GET** https://cloud.seafile.com/api2/account/info/

**예제 요청**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/account/info/

**예제 응답**

    {
    "usage": 26038531,
    "total": 104857600,
    "email": "user@example.com"
    }

**오류**

* 403 잘못된 토큰

### <a id="server-info"></a>서버 정보 조회 ###

**GET** https://cloud.seafile.com/api2/server-info

*참고*:

- 인증 불필요.
- Seafile 커뮤니티판 서버 `4.0.5` 또는 전문가판 서버 `4.0.3`에 추가했습니다

**예제 요청**

    curl https://cloud.seafile.com/api2/server-info/

**예제 응답**

Seafile 커뮤니티판 서버 응답 예제:

    {
        "version": "4.0.6",
        "features": [
        "seafile-basic",
        ]
    }

Seafile 전문가판 서버 응답 예제:

    {
        "version": "4.0.6",
        "features": [
        "seafile-basic",
        "seafile-pro",
        "office-preview",
        "file-search"
        ]
    }

## <a id="starred-files"></a>별표 표시한 파일 ##

### <a id="list-starred-files"></a>별표 표시 파일 조회

**GET** https://cloud.seafile.com/api2/starredfiles/


**예제 요청**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e6199b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/starredfiles/

**예제 응답**

    [
    {
        "repo": "99b758e6-91ab-4265-b705-925367374cf0",
        "mtime": 1355198150,
        "org": -1,
        "path": "/foo/bar.doc",
        "dir": false,
        "size": 0
    },
    {
        "repo": "99b758e6-91ab-4265-b705-925367374cf0",
        "mtime": 1353751237,
        "org": -1,
        "path": "/add_folder-blue.png",
        "dir": false,
        "size": 3170
    }
    ]

### <a id="star-a-file"></a>파일 별표 표시

**POST** https://cloud.seafile.com/api2/starredfiles/

**요청 매개변수**

* repo_id (post)
* p (post)

**예제 요청**

    curl -v -d "repo_id=dae8cecc-2359-4d33-aa42-01b7846c4b32&p=/foo.md" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/starredfiles/

**예제 응답**

    ...
    < HTTP/1.0 201 CREATED
    < Location: https://cloud.seafile.com/api2/starredfiles/
    ...
    "success"

**성공**

   Response code is 201(Created) and Location header provides url of starred file list.

**오류**

* 400 `repo_id` 또는 `p` 값이 빠지거나, `p`에 부적절한 파일 경로(e.g. /foo/bar/).

### <a id="unstar-a-file"></a>파일

**DELETE** https://cloud.seafile.com/api2/starredfiles/

**요청 매개변수**

* repo_id
* p

**예제 요청**

    curl -X DELETE -v  -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' 'https://cloud.seafile.com/api2/starredfiles/?repo_id=dae8cecc-2359-4d33-aa42-01b7846c4b32&p=/foo.md'

**예제 응답**

    ...
    < HTTP/1.0 200 OK
    ...
    "success"

**성공**

   응답 코드는 200(OK) 이며, "success" 문자열을 반환합니다.

**오류**

* 400 `repo_id` 또는 `p` 값이 빠지거나, `p`에 부적절한 파일 경로(e.g. /foo/bar/).

## <a id="group"></a>그룹 ##

### <a id="list-groups"></a>그룹 조회 ###

**GET** https://cloud.seafile.com/api2/groups/


**예제 요청**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/groups/"

**예제 응답**

    {
        "replynum": 0,
        "groups": [
            {
                "ctime": 1398134171327948,
                "creator": "user@example.com",
                "msgnum": 0,
                "mtime": 1398231100,
                "id": 1,
                "name": "lian"
            },
            {
                "ctime": 1398236081042441,
                "creator": "user@example.com",
                "msgnum": 0,
                "mtime": 0,
                "id": 2,
                "name": "123"
            }
        ]
    }

### <a id="add-a-group"></a>그룹 추가 ###

**POST** https://cloud.seafile.com/api/v2.1/groups/

**요청 매개변수**

* name (새 그룹 이름)

**예제 요청**

```
curl -d "name=new_group_name" -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/
```

**예제 응답**

```
{
    "name": "new_group_name",
    "owner": "lian@lian.com",
    "created_at": "2015-12-17T10:29:57+0800",
    "admins": ["lian@lian.com"],
    "avatar_url": "https://cloud.seafile.com/media/avatars/groups/default.png",
    "id": 773
}
```

### <a id="get-info-of-a-group"></a>그룹 정보 확인 ###

**GET** https://cloud.seafile.com/api/v2.1/groups/772/

**요청 매개변수**

* avatar_size
* with_repos (그룹 라이브러리 정보를 반환하는 경우 0 또는 1. 기본값은 0이며 어떤 repo도 반환하지 않음)

**예제 요청**

```
curl -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/772/
```

**예제 응답**

```
{
    "name": "rename_group_name",
    "owner": "lian@lian.com",
    "created_at": "2015-12-17T10:29:57+0800",
    "admins": ["lian@lian.com"],
    "avatar_url": "https://cloud.seafile.com/media/avatars/groups/default.png",
    "id": 772
}
```

### <a id="rename-a-group"></a>그룹 이름 바꾸기 ###

**PUT** https://cloud.seafile.com/api/v2.1/groups/772/

**요청 매개변수**

* name (새 그룹 이름)

**예제 요청**

```
curl -X PUT -d "name=rename_group_name" -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/772/
```

**예제 응답**

```
{
    "name": "rename_group_name",
    "owner": "lian@lian.com",
    "created_at": "2015-12-17T10:29:57+0800",
    "admins": ["lian@lian.com"],
    "avatar_url": "https://cloud.seafile.com/media/avatars/groups/default.png",
    "id": 772
}
```

### <a id="transfer-a-group"></a>그룹 양도 ###

**PUT** https://cloud.seafile.com/api/v2.1/groups/772/

**요청 매개변수**

* owner (그룹 새 소유자, 전자메일 주소여야 함.)

**예제 요청**

```
curl -X PUT -d "owner=new_owner@new_owner.com" -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/772/
```

**예제 응답**

```
{
    "name": "rename_group_name",
    "owner": "new_owner@new_owner.com",
    "created_at": "2015-12-17T10:29:57+0800",
    "admins": ["lian@lian.com", "new_owner@new_owner.com"],
    "avatar_url": "https://cloud.seafile.com/media/avatars/groups/default.png",
    "id": 772
}
```

### <a id="delete-a-group"></a> 그룹 삭제 ###

**DELETE** https://cloud.seafile.com/api/v2.1/groups/772/

**예제 요청**

```
curl -X DELETE -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/772/
```

**예제 응답**

```
{"success":true}
```

### <a id="quit-group"></a> 그룹 나가기 ###

**DELETE** https://cloud.seafile.com/api/v2.1/groups/770/members/myself@email.com/

**예제 요청**

```
curl -X DELETE -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/770/members/myself@email.com/
```

**예제 응답**

```
{"success":true}
```

### <a id="group-member"></a>그룹 구성원 ###

#### <a id="list-group-members"></a>모든 그룹 구성원 조회 ###

**GET** https://cloud.seafile.com/api/v2.1/groups/770/members/

**요청 매개변수**

* avatar_size
* is_admin (그룹 관리자를 반환할 경우에만 `true`/`false`. 기본 값은 모든 구성원을 반환하는 `false`)

**예제 요청**

```
curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api/v2.1/groups/770/members/"
```

**예제 응답**

```
[
    {
        "login_id": "",
        "name": "nickname-of-lian",
        "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
        "is_admin": true,
        "contact_email": "lian_contact@email.com",
        "email": "lian@lian.com"
    },
    {
        "login_id": "",
        "name": "1",
        "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
        "is_admin": false,
        "contact_email": "1@1.com",
        "email": "1@1.com"
    }
]
```

#### <a id="add-a-group-member"></a>그룹 구성원 추가 ###

**POST** https://cloud.seafile.com/api/v2.1/groups/770/members/

**요청 매개변수**

* email

**예제 요청**

```
curl -d "email=new-member@email.com" -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/770/members/
```

**예제 응답**

```
{
    "login_id": "",
    "name": "new-member",
    "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
    "is_admin": false,
    "contact_email": "new-member@email.com",
    "email": "new-member@email.com"
}
```

#### <a id="bulk-add-group-members"></a>여러 그룹 구성원 한 번에 추가 ###

**POST** https://cloud.seafile.com/api/v2.1/groups/770/members/bulk/

**요청 매개변수**

* emails

**예제 요청**

```
curl -d "emails=new-member-1@email.com,new-member-2@email.com,new-member-3@email.com" -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/770/members/bulk/
```

**예제 응답**

```
{
    "failed":[
        {
            "error_msg": "Invalid email",
            "email": "new-member-3@email.com"
        },
        {
            "error_msg": "Is already group member",
            "email": "new-member-4@email.com"
        }
    "success":[
        {
            "login_id": "",
            "name": "new-member-1",
            "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
            "is_admin": false,
            "contact_email": "new-member-1@email.com",
            "email": "new-member-1@email.com"
        },
        {
            "login_id": "",
            "name": "new-member-2",
            "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
            "is_admin": false,
            "contact_email": "new-member-2@email.com",
            "email": "new-member-2@email.com"
        }
    ]
}

```

#### <a id="get-info-of-a-group-member"></a>그룹 구성원 정보 확인 ###

**GET** https://cloud.seafile.com/api/v2.1/groups/770/members/group-member@email.com/

**예제 요청**

```
curl -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/770/members/group-member@email.com/
```

**요청 매개변수**

* avatar_size

**예제 응답**

```
{
    "login_id": "",
    "name": "group-member",
    "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
    "is_admin": false,
    "contact_email": "group-member@email.com",
    "email": "group-member@email.com"
}
```

#### <a id="set-a-group-member-admin"></a>그룹 구성원을 관리자로 설정 ###

**PUT** https://cloud.seafile.com/api/v2.1/groups/770/members/group-member@email.com/

**요청 매개변수**

* is_admin=true

**예제 요청**

```
curl -X PUT -d "is_admin=true" -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/770/members/group-member@email.com/
```

**예제 응답**

```
{
    "login_id": "",
    "name": "group-member",
    "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
    "is_admin": true,
    "contact_email": "group-member@email.com",
    "email": "group-member@email.com"
}
```

#### <a id="unset-a-group-member-admin"></a>그룹 구성원 관리자 해임 ###

**PUT** https://cloud.seafile.com/api/v2.1/groups/770/members/group-member@email.com/

**요청 매개변수**

* is_admin=false

**예제 요청**

```
curl -X PUT -d "is_admin=false" -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/770/members/group-member@email.com/
```

**예제 응답**

```
{
    "login_id": "",
    "name": "group-member",
    "avatar_url": "https://cloud.seafile.com/media/avatars/default.png",
    "is_admin": false,
    "contact_email": "group-member@email.com",
    "email": "group-member@email.com"
}
```

#### <a id="delete-a-group-member"></a> 그룹 구성원 삭제 ###

**DELETE** https://cloud.seafile.com/api/v2.1/groups/770/members/group-member@email.com/

**예제 요청**

```
curl -X DELETE -H 'Authorization: Token 444d2bbf1fc78ffbeedc4704c9f41e32d926ac94' https://cloud.seafile.com/api/v2.1/groups/770/members/group-member@email.com/
```

**예제 응답**

```
{"success":true}
```

### <a id="group-message"></a>그룹 메시지 ###

#### <a id="get-group-messages"></a>그룹 메시지 확인 ####

**GET** https://cloud.seafile.com/api2/group/msgs/{group_id}/

**요청 매개변수**

* group_id

**예제 요청**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/group/msgs/1/"

**예제 응답**

    {
        "next_page": -1,
        "msgs": [
            {
                "reply_cnt": 0,
                "timestamp": 1398230602,
                "replies": [],
                "from_email": "user@example.com",
                "msgid": 1,
                "msg": "test discuss",
                "nickname": "user"
            }
        ]
    }

#### <a id="get-group-message-detail"></a>그룹 메시지 세부정보 확인 ####

**GET** https://cloud.seafile.com/api2/group/{group_id}/msg/{msg_id}/

**요청 매개변수**

* group_id
* msg_id

**예제 요청**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/group/1/msg/1/"

**예제 응답**

    {
        "reply_cnt": 2,
        "timestamp": 1398230602,
        "replies": [
            {
                "msg": "this is another test",
                "timestamp": 1398232319,
                "nickname": "user",
                "msgid": 1,
                "from_email": "user@example.com"
            },
            {
                "msg": "this is another test",
                "timestamp": 1398232508,
                "nickname": "user",
                "msgid": 3,
                "from_email": "user@example.com"
            }
        ],
        "from_email": "user@example.com",
        "msgid": 1,
        "msg": "test discuss",
        "nickname": "user"
    }

**오류**

* 404 메시지 없음

#### <a id="send-a-group-message"></a>그룹 메시지 보내기 ####

**POST** https://cloud.seafile.com/api2/group/msgs/{group_id}/

**요청 매개변수**

* message
* group_id
* repo_id(선택)
* path(선택)

**예제 요청**

    curl -d "message=this is another test&repo_id=c7436518-5f46-4296-97db-2fcba4c8c8db&path=/123.md" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/group/msgs/1/"

**예제 응답**

    {
        "msgid": 3
    }

#### <a id="reply-a-group-message"></a>그룹 메시지 답장 ####

**POST** https://cloud.seafile.com/api2/group/{group_id}/msg/{msg_id}

**요청 매개변수**

* group_id
* msg_id
* message

**예제 요청**

    curl -d "message=this is a reply" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/group/1/msg/1/"

**예제 응답**

    {
        "msgid": 3
    }

**오류**

* 404 메시지 없음

#### <a id="get-group-message-replies"></a>그룹 메시지 답장 확인 ####

**GET** https://cloud.seafile.com/api2/new_replies/


**예제 요청**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/new_replies/"

**예제 응답**

    [
        {
            "reply_cnt": 1,
            "timestamp": 1398231100,
            "replies": [
                {
                    "msg": "@user test reply",
                    "timestamp": 1398234493,
                    "nickname": "123",
                    "msgid": 5,
                    "from_email": "user@example.com"
                }
            ],
            "from_email": "user@example.com",
            "att": {
                "repo": "c7436518-5f46-4296-97db-2fcba4c8c8db",
                "path": "/123.md",
                "type": "file",
                "src": "recommend"
            },
            "msgid": 3,
            "msg": "this is another test",
            "nickname": "user"
        }
    ]

## <a id="share"></a>공유

### <a id="share-link"></a>파일 공유 링크 ###

#### <a id="list-share-links"></a>공유 링크 조회 ####

**GET** https://cloud.seafile.com/api/v2.1/share-links/

**예제 요청**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api/v2.1/share-links/"

**예제 응답**

    [{"username":"lian@lian.com","view_cnt":0,"ctime":"2016-02-26T16:20:36.894","token":"4cbd625c5e","repo_id":"62ca6cf9-dab6-47e5-badc-bab13d9220ce","link":"https://cloud.seafile.com/f/4cbd625c5e/","expire_date":null,"path":"/file.md","is_expired":false},{"username":"lian@lian.com","view_cnt":0,"ctime":"2016-03-04T03:54:58.279","token":"8dc1e04ddd","repo_id":"62ca6cf9-dab6-47e5-badc-bab13d9220ce","link":"https://cloud.seafile.com/d/8dc1e04ddd/","expire_date":null,"path":"/","is_expired":false}]

#### <a id="create-share-link"></a>공유 링크 만들기 ####

**POST** https://cloud.seafile.com/api/v2.1/share-links/

**요청 매개변수**

* repo-id
* path (파일/폴더 경로)
* password (필요하지 않음)
* expire_date (필요하지 않음)

**예제 요청**

파일 다운로드 링크를 만듭니다

    curl -d "path=/foo.md&repo_id=62ca6cf9-dab6-47e5-badc-bab13d9220ce" -H 'Authorization: Token ef12bf1e66a1aa797a1d6556fdc9ae84f1e9249f' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/share-links/

디렉터리 다운로드 링크에 암호를 걸고 유효 기간을 설정하여 만듭니다

    curl -d "path=/bar/&repo_id=62ca6cf9-dab6-47e5-badc-bab13d9220ce&password=password&expire_date=6" -H 'Authorization: Token ef12bf1e66a1aa797a1d6556fdc9ae84f1e9249f' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/share-links/

**예제 응답**

```
{
    "username": "lian@lian.com",
    "view_cnt": 0,
    "ctime": "2016-03-04T04:06:35.477",
    "token": "409f5aa54a",
    "repo_id": "62ca6cf9-dab6-47e5-badc-bab13d9220ce",
    "link": "https://cloud.seafile.com/f/409f5aa54a/",
    "expire_date": null,
    "path": "/foo.md",
    "is_expired": false
}
```

```
{
    "username": "lian@lian.com",
    "view_cnt": 0,
    "ctime": "2016-03-04T04:12:48.959",
    "token": "db1a50e686",
    "repo_id": "62ca6cf9-dab6-47e5-badc-bab13d9220ce",
    "link": "https://cloud.seafile.com/d/db1a50e686/",
    "expire_date": null,
    "path": "/bar/",
    "is_expired": false
}
```

**오류**

* 400 잘못된 경로/repo_id
* 403 권한 거부.
* 404 파일/폴더/라이브러리 없음.
* 500 내부 서버 오류

#### <a id="delete-share-link"></a>공유 링크 삭제 ####

**DELETE** https://cloud.seafile.com/api/v2.1/share-links/{token}/

**예제 요청**

    curl -X DELETE -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api/v2.1/share-links/0ae587a7d1/"

**예제 응답**

    {"success":true}

#### <a id="send-share-link-email"></a>공유 링크 전자메일로 보내기 ####

**POST** https://cloud.seafile.com/api2/send-share-link/

**요청 매개변수**

* token
* email
* extra_msg (필요하지 않음)

**예제 요청**

    curl -d "email=sample@eamil.com,invalid-email&token=4cbd625c5e" -H 'Authorization: Token ef12bf1e66a1aa797a1d6556fdc9ae84f1e9249f' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/send-share-link/

**예제 응답**

```
{
    "failed": [
        {
            "email": "invalid-email",
            "error_msg": "email invalid."
        }
    ],
    "success": [
        "sample@eamil.com"
    ]
}
```

**오류**

* 400 잘못된 토큰/repo_id invalid
* 403 권한 거부.
* 403 공유 링크 전송 실패. 전자메일 서비스를 제대로 설정하지 않았으니 관리자에게 연락하십시오.
* 404 토큰/라이브러리 없음

#### <a id="list-direntry-in-dir-download-link"></a>디렉터리 다운로드 링크의 디렉터리 항목 조회 ####

**GET** https://cloud.seafile.com/api2/d/{token}/dir/

**요청 매개변수**

* token (업로드 링크 토큰)
* p (하위 폴더 경로)
* 암호(링크를 암호화 했다면)

**예제 요청**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/d/3af7c46595/dir/?p=/subfolder/"

**예제 응답**

    [{"mtime": 1436846750, "type": "dir", "name": "sadof", "id": "1806dbdb700b7bcd49e6275107c7ccf7b3ea1776"}, {"id": "bdb06f6de972c42893fda590ac954988b562429c", "mtime": 1436431020, "type": "file", "name": "test.mdert", "size": 20}]

### <a id="upload-link"></a>업로드 링크 ###

#### <a id="list-upload-links"></a>업로드 링크 조회 ####

**GET** https://cloud.seafile.com/api/v2.1/upload-links/

**예제 요청**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api/v2.1/upload-links/"

**예제 응답**

    [{"username":"lian@lian.com","repo_id":"62ca6cf9-dab6-47e5-badc-bab13d9220ce","ctime":"2016-03-03T15:26:15.223","token":"9a5d5c8391","link":"https://cloud.seafile.com/u/d/9a5d5c8391/","path":"/"},{"username":"lian@lian.com","repo_id":"78c620ee-2989-4427-8eff-7748f4fbebc0","ctime":"2016-03-04T05:37:17.968","token":"d17d87ea4d","link":"https://cloud.seafile.com/u/d/d17d87ea4d/","path":"/yutong/"}]

#### <a id="create-upload-link"></a>업로드 링크 만들기 ####

**POST** https://cloud.seafile.com/api/v2.1/upload-links/

**요청 매개변수**

* repo-id
* path (파일/폴더 경로)
* password (필요하지 않음)

**예제 요청**

디렉터리 업로드 링크를 암호를 걸어 만듭니다

    curl -d "path=/bar/&repo_id=afc3b694-7d4c-4b8a-86a4-89c9f3261b12&password=password" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/upload-links/

**예제 응답**

```
{
    "username": "lian@lian.com",
    "repo_id": "62ca6cf9-dab6-47e5-badc-bab13d9220ce",
    "ctime": "2016-03-04T05:51:34.022",
    "token": "dce40e8594",
    "link": "https://cloud.seafile.com/u/d/dce40e8594/",
    "path": "/bar/"
}
```

**오류**

* 400 잘못된 경로/repo_id
* 403 권한 거부.
* 500 내부 서버 오류

#### <a id="delete-upload-link"></a>업로드 링크 삭제 ####

**DELETE** https://cloud.seafile.com/api/v2.1/upload-links/{token}/

**예제 요청**

    curl -X DELETE -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api/v2.1/upload-links/0ae587a7d1/"

**예제 응답**

    {"success":true}

#### <a id="send-upload-link-email"></a>업로드 링크 전자메일로 보내기 ####

**POST** https://cloud.seafile.com/api2/send-upload-link/

**요청 매개변수**

* token
* email
* extra_msg (필요하지 않음)

**예제 요청**

    curl -d "email=sample@eamil.com,invalid-email&token=4cbd625c5e" -H 'Authorization: Token ef12bf1e66a1aa797a1d6556fdc9ae84f1e9249f' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/send-upload-link/

**예제 응답**

```
{
    "failed": [
        {
            "email": "invalid-email",
            "error_msg": "email invalid."
        }
    ],
    "success": [
        "sample@eamil.com"
    ]
}
```
* 400 잘못된 토큰/repo_id invalid
* 403 권한 거부.
* 403 공유 링크 전송 실패. 전자메일 서비스를 제대로 설정하지 않았으니 관리자에게 연락하십시오.
* 404 토큰/라이브러리 없음

### <a id="shared-libs"></a>공유 라이브러리 ###

#### <a id="list-shared-libraries"></a>공유 라이브러리 조회 ####

**GET** https://cloud.seafile.com/api2/shared-repos/

**예제 요청**

    curl -v -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/shared-repos/

**예제 응답**

    [{"repo_id": "7d42522b-1f6f-465d-b9c9-879f8eed7c6c", "share_type": "personal", "permission": "rw", "encrypted": false, "user": "user@example.com", "last_modified": 1361072500, "repo_desc": "ff", "group_id": 0, "repo_name": "\u6d4b\u8bd5\u4e2d\u6587pdf"}, {"repo_id": "79bb29cd-b683-4844-abaf-433952723ca5", "share_type": "group", "permission": "rw", "encrypted": false, "user": "user@example.com", "last_modified": 1359182468, "repo_desc": "test", "group_id": 1, "repo_name": "test_enc"}]

#### <a id="list-be-shared-libraries"></a>공유한 라이브러리 조회 ####

**GET** https://cloud.seafile.com/api2/beshared-repos/


**예제 요청**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/beshared-repos/"

**예제 응답**

    "[{"user": "user@example.com", "repo_id": "989e3952-9d6f-4427-ab16-4bf9b53212eb", "share_type": "personal", "permission": "rw", "encrypted": false, "repo_desc": "lib shared to imwhatiam", "enc_version": false, "last_modified": 1398218747, "is_virtual": false, "group_id": 0, "repo_name": "lib shared to imwhatiam"}]"

#### <a id="share-a-library"></a>라이브러리 공유 ####

**PUT** https://cloud.seafile.com/api2/shared-repos/{repo-id}/

**요청 매개변수**

* share_type ('personal', 'group', 'public')
* user (또는 users)
* group_id
* permission

share_type이 'personal'이면 'user' 또는 'users' 매개변수가 필요하며, share_type이 'group'이면 'group_id' 매개변수가 필요합니다. share_type이 'public'이면 필요한 다른 매개 변수는 없습니다.

'user' 또는 'users' 매개 변수는 전자메일 주소를 쉼표로 구분할 수 있으며, 이 경우 더 많은 사용자에게 동시에 공유할 수 있습니다. 다중 사용자 공유에 문제가 발생하면 공유 처리 과정을 중단합니다.

**예제 요청**

    curl -X PUT -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/shared-repos/7d42522b-1f6f-465d-b9c9-879f8eed7c6c/?share_type=group&user=user@example.com&group_id=1&permission=rw"

**예제 응답**

    "success"

#### <a id="unshare-a-library"></a>라이브러리 공유 해제 ####

**DELETE** https://cloud.seafile.com/api2/shared-repos/{repo-id}/

**요청 매개변수**

* share_type ('personal', 'group', 'public')
* user
* group_id

share_type이 'personal'이면 'user' 매개변수가 필요하며, share_type이 'group'이면 'group_id' 매개변수가 필요합니다. share_type이 'public'이면 필요한 다른 매개 변수는 없습니다.

**예제 요청**

    curl -X DELETE -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/shared-repos/7d42522b-1f6f-465d-b9c9-879f8eed7c6c/?share_type=personal&user=user@example.com&group_id=0"

**예제 응답**

    "success"

## <a id="library"></a>라이브러리 ##

### <a id="get-default-lib"></a>기본 라이브러리 확인 ###

**GET** https://cloud.seafile.com/api2/default-repo/

**예제 요청**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/default-repo/"

**예제 응답**

    {
        "repo_id": "691b3e24-d05e-43cd-a9f2-6f32bd6b800e",
        "exists": true
    }

### <a id="create-default-lib"></a>기본 라이브러리 만들기 ###

**POST** https://cloud.seafile.com/api2/default-repo/

**예제 요청**

    curl -X POST -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/default-repo/"

**예제 응답**

    {
        "repo_id": "691b3e24-d05e-43cd-a9f2-6f32bd6b800e",
        "exists": true
    }

### <a id="list-libraries"></a>라이브러리 조회 ###

**GET** https://cloud.seafile.com/api2/repos/

**예제 요청**

    curl -H 'Authorization: Token 24fd3c026886e3121b2ca630805ed425c272cb96' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/

**예제 응답**

    [
    {
        "permission": "rw",
        "encrypted": false,
        "mtime": 1400054900,
        "owner": "user@mail.com",
        "id": "f158d1dd-cc19-412c-b143-2ac83f352290",
        "size": 0,
        "name": "foo",
        "type": "repo",
        "virtual": false,
        "desc": "new library",
        "root": "0000000000000000000000000000000000000000"
    },
    {
        "permission": "rw",
        "encrypted": false,
        "mtime": 1400054802,
        "owner": "user@mail.com",
        "id": "0536b11a-a5fd-4482-9314-728cb3472f54",
        "size": 0,
        "name": "foo",
        "type": "repo",
        "virtual": false,
        "desc": "new library",
        "root": "0000000000000000000000000000000000000000"
    }
    ]

### <a id="get-library-info"></a>라이브러리 정보 확인 ###

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/

**요청 매개변수**

* repo-id

**예제 요청**

    curl -G -H 'Authorization: Token 24fd3c026886e3121b2ca630805ed425c272cb96' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/632ab8a8-ecf9-4435-93bf-f495d5bfe975/

**예제 응답**

    {
    "encrypted": false,
    "password_need": null,
    "mtime": null,
    "owner": "self",
    "id": "632ab8a8-ecf9-4435-93bf-f495d5bfe975",
    "size": 1356155,
    "name": "org",
    "root": "b5227040de360dd22c5717f9563628fe5510cbce",
    "desc": "org file",
    "type": "repo"
    }

### <a id="get-library-owner"></a>라이브러리 소유주 확인 ###

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/owner/

**요청 매개변수**

* repo-id

**예제 요청**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d9b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/owner/

**예제 응답**

    {
    "owner": "user@example.com"
    }

**오류**

* 403 권한 오류(관리자/repo-소유자 만 이 동작을 수행할 수 있습니다).

### <a id="get-library-history"></a>라이브러리 기록 확인 ###

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/history/

**요청 매개변수**

* repo-id

**예제 요청**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d9b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/history/

**예제 응답**

    {"commits": [{"rev_file_size": 0, "rev_file_id": null, "ctime": 1398045167, "creator_name": "imwhatiam123@gmail.com", "creator": "0000000000000000000000000000000000000000", "root_id": "ca2625da6be6e211ddd584615ef3bfaa531e66aa", "rev_renamed_old_path": null, "parent_id": "205c469f0830df09b13024601524058757a43128", "new_merge": false, "repo_id": "691b3e24-d05e-43cd-a9f2-6f32bd6b800e", "desc": "Modified \"api.md\"", "id": "eb62721812e0c3122889b5facde971b353ad176b", "conflict": false, "second_parent_id": null}, {"rev_file_size": 0, "rev_file_id": null, "ctime": 1398045158, "creator_name": "imwhatiam123@gmail.com", "creator": "0000000000000000000000000000000000000000", "root_id": "0b7a31adf4ea8b29ad5a5920420b548da11dd32f", "rev_renamed_old_path": null, "parent_id": "2ba85ee6072efea51a3483843ea7de9b6d1d1eb2", "new_merge": false, "repo_id": "691b3e24-d05e-43cd-a9f2-6f32bd6b800e", "desc": "Added \"api.md\"", "id": "205c469f0830df09b13024601524058757a43128", "conflict": false, "second_parent_id": null}], "page_next": false}

### <a id="get-library-history-limit-days"></a>라이브러리 기록 유지 제한 기간 확인 ###

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/history-limit/

**요청 매개변수**

* repo-id

**예제 요청**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d9b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/history-limit/

**예제 응답**

    {
    "keep_days": -1,
    }

**오류**

* 403 권한 거부.
* 404 라이브러리 없음.
* 500 내부 서버 오류

### <a id="set-library-history-limit-days"></a>라이브러리 기록 유지 제한 기간 설정 ###

**PUT** https://cloud.seafile.com/api2/repos/{repo-id}/history-limit/

**요청 매개변수**

* repo-id
* keep_days. -1은 전체 기록 유지, 0은 기록 유지 안함, 양의 정수는 기록 유지 제한 기간입니다.

**예제 요청**

    curl -v -X PUT -d "keep_days=4" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/history-limit/

**예제 응답**

    {
    "keep_days": 4,
    }

**오류**

* 400 잘못된 keep_days 값.
* 403 권한 거부.
* 404 라이브러리 없음.
* 500 내부 서버 오류
* 520 라이브러리 기록 한계 설정 실패.

### <a id="create-library"></a>라이브러리 만들기 ###

**POST** https://cloud.seafile.com/api2/repos/

**요청 매개변수**

* name
* desc (기본값 "새 저장소")
* passwd (암호화 라이브러리에서 필요함)

**예제 요청**

    curl -v -d "name=foo&desc=new library" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/

**예제 응답**

    {
    "encrypted": "",
    "enc_version": 0,
    "repo_id": "f15811fd-5c19-412c-b143-2ac83f352290",
    "magic": "",
    "relay_id": "c5e41170db250ea497075e2911104faf0105b7fb",
    "repo_version": 1,
    "relay_addr": "cloud.seafile.com",
    "token": "c1f3defe9ba408cd7964427ec276843e9d10c23b",
    "relay_port": "10001",
    "random_key": "",
    "email": "user@mail.com",
    "repo_name": "foo"
    }

**성공**

   응답 코드 200를 반환하고 새로 만든 라이브러리 정보를 반환합니다.

**오류**

* 400 라이브러리 이름 빠짐.
* 520 처리 실패.

### <a id="check/create-sub-library"></a>하위 라이브러리 검사/만들기 ###

각각의 sub_repo에 디렉터리가 있는지 확인하고, 없으면 새로 만듭니다

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/dir/sub_repo/?p=/\&name=sub_lib

**요청 매개변수**

* repo-id
* p
* name

**예제 요청**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d9b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/dir/sub_repo/?p=/\&name=sub_lib

**예제 응답**

    {"sub_repo_id": "c0a3283c-013c-4a7c-8f68-006f06fa6dec"}

**오류**

* 400 인자 빠짐
* 500 내부 서버 오류

### <a id="delete-library"></a>라이브러리 삭제 ###

**DELETE** https://cloud.seafile.com/api2/repos/{repo-id}/

**예제 요청**

    curl -v -X DELETE -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/8f5f2222-72a8-454f-ac40-8397c5a556a8/

**예제 응답**

"success"

**오류**

* 400 라이브러리 없음.

* 403 라이브러리 소유자만 동작 수행 가능.

### <a id="rename-library"></a>라이브러리 이름 바꾸기 ###

**POST** https://cloud.seafile.com/api2/repos/{repo-id}/?op=rename

**예제 요청**

    curl -d "repo_name=new-repo-name"  -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/8f5f2222-72a8-454f-ac40-8397c5a556a8/op=rename

**예제 응답**

"success"

**오류**

* 404 라이브러리 없음.
* 403 라이브러리 이름 바꾸기 권한 없음.
* 500 라이브러리 이름 바꿀 수 없음

### <a id="transfer-library"></a>라이브러리 양도 ###

**PUT** https://cloud.seafile.com/api2/repos/{repo-id}/owner/

**요청 매개변수**

* repo-id
* owner

**예제 요청**

    curl -v -X PUT -d "owner=new@owner.com" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d9b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/owner/

**예제 응답**

    {
    "success": True
    }

**오류**

* 440 잘못된 전자메일 주소.
* 403 권한 오류(관리자/repo-소유자 만 이 동작을 수행할 수 있습니다).
* 404 라이브러리 없음.
* 404 사용자 없음.

### <a id="decrypt-library"></a>라이브러리 해독 ###

**POST** https://cloud.seafile.com/api2/repos/{repo-id}/

**요청 매개변수**

* password

**예제 요청**

    curl -v -d "password=123" -H 'Authorization: Token e6a33d61954f219a96b60f635cf02717964e4385' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/0c2465a5-4753-4660-8a22-65abec9ec8d0/

**예제 응답**

"success"

**오류**

* 400 잘못된 암호
* 409 암호화 하지 않은 Repo
* 500 내부 서버 오류

### <a id="create-public-lib"></a>공개 라이브러리 만들기 ###

**POST** https://cloud.seafile.com/api2/repos/{repo-id}/public/

**요청 매개변수**

* repo-id

**예제 요청**

    curl -X POST -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d9b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/public/

**예제 응답**

    ...
    < HTTP/1.0 200 OK
    ...

**성공**

    응답 코드는 200(OK) 이며, "success" 문자열을 반환합니다.

**오류**

* 404 Repo 없음
* 403 이 repo 접근 금지
* 500 내부 서버 오류, 공개 repo를 만들 수 없음

### <a id="remove-public-lib"></a>공개 라이브러리 제거 ###

**DELETE** https://cloud.seafile.com/api2/repos/{repo-id}/public/

**요청 매개변수**

* repo-id

**예제 요청**

    curl -X DELETE -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d9b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/public/

**예제 응답**

    ...
    < HTTP/1.0 200 OK
    ...

**성공**

    응답 코드는 200(OK) 이며, "success" 문자열을 반환합니다.

**오류**

* 404 Repo 없음
* 403 이 repo 접근 금지
* 500 내부 서버 오류, 공개 repo를 제거할 수 없음

### <a id="fetch-library-download-info"></a>라이브러리 다운로드 정보 가져오기 ###

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/download-info/

**요청 매개변수**

* repo-id

**예제 요청**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d9b477fd' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/download-info/

**예제 응답**

    {
    "applet_root": "https://localhost:13420",
    "relay_addr": "localhost",
    "token": "46acc4d9ca3d6a5c7102ef379f82ecc1edc629e1",
    "repo_id": "dae8cecc-2359-4d33-aa42-01b7846c4b32",
    "relay_port": "10002",
    "encrypted": "",
    "repo_name": "test",
    "relay_id": "8e4b13b49ca79f35732d9f44a0804940d985627c",
    "email": "user@example.com"
    }

### <a id="list-virtual-libraries"></a>가상 라이브러리 조회 ###

**GET** https://cloud.seafile.com/api2/virtual-repos/

**예제 요청**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/virtual-repos/"

**예제 응답**

    {"virtual-repos":
        [
            {"virtual_perm": "rw", "store_id": null, "worktree_invalid": false, "encrypted": false, "origin_repo_name": "lian", "last_modify": 0, "no_local_history": false, "head_branch": null, "last_sync_time": 0, "id": "51344de8-456f-4dc7-ac08-718827994252", "size": 0, "share_permission": null, "worktree_changed": false, "worktree_checktime": 0, "origin_path": "/lian", "is_virtual": true, "origin_repo_id": "a582d3bc-bcf5-421e-9125-741fa56d18d4", "version": 1, "random_key": null, "is_original_owner": true, "shared_email": null, "enc_version": 0, "head_cmmt_id": "bc666fdc60d2352b9f6a0324ac64168d43724eed", "desc": null, "index_corrupted": false, "magic": null, "name": "lian", "worktree": null, "auto_sync": false, "relay_id": null},
            {"virtual_perm": "rw", "store_id": null, "worktree_invalid": false, "encrypted": false, "origin_repo_name": "lian", "last_modify": 0, "no_local_history": false, "head_branch": null, "last_sync_time": 0, "id": "c0a3283c-013c-4a7c-8f68-006f06fa6dec", "size": 0, "share_permission": null, "worktree_changed": false, "worktree_checktime": 0, "origin_path": "/", "is_virtual": true, "origin_repo_id": "a582d3bc-bcf5-421e-9125-741fa56d18d4", "version": 1, "random_key": null, "is_original_owner": true, "shared_email": null, "enc_version": 0, "head_cmmt_id": "ff18229aadc9acc73ad481278d5b4c42b3353aa0", "desc": null, "index_corrupted": false, "magic": null, "name": "123", "worktree": null, "auto_sync": false, "relay_id": null}
        ]
    }

### <a id="search-libraries"></a>라이브러리 검색 ###

**GET** https://cloud.seafile.com/api2/search/

**요청 매개변수**

* q
* per_page (선택)

**예제 요청**

    curl -G -H 'Authorization: Token 24fd3c026886e3121b2ca630805ed425c272cb96' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/search/?q=keyword

**예제 응답**

    {
        "has_more": false,
        "total": 3,
        "results": [
            {
                "repo_id": "691b3e24-d05e-43cd-a9f2-6f32bd6b800e",
                "name": "api.md",
                "oid": "8ea78453bb474359cd9d8e2c4c4d8d9cbdcef0a2",
                "last_modified": 1398045167,
                "fullpath": "/api.md",
                "size": 18939
            },
            {
                "repo_id": "c5509062-9bca-4933-a7e0-c6da1d5f82be",
                "name": "home.md",
                "oid": "dda57aaffa5179829e064c7d0c142f47a8a65d3b",
                "last_modified": 1397096831,
                "fullpath": "/home.md",
                "size": 1954
            },
            {
                "repo_id": "c5509062-9bca-4933-a7e0-c6da1d5f82be",
                "name": "\u5e38\u89c1\u5b89\u88c5\u95ee\u9898.md",
                "oid": "8573f982eeb478b932a55ec13218f4f90a7c5a27",
                "last_modified": 1397188959,
                "fullpath": "/\u5e38\u89c1\u5b89\u88c5\u95ee\u9898.md",
                "size": 1050
            }
        ]
    }

**오류**

* 404 검색 기능 지원 안함.
* 400 q 인자 빠짐.

### <a id="get-library-download-links"></a>라이브러리 다운로드 링크 확인 ###

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/download-shared-links/

**요청 매개변수**

* repo-id

**예제 요청**

    curl -H 'Authorization: Token 24fd3c026886e3121b2ca630805ed425c272cb96' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/632ab8a8-ecf9-4435-93bf-f495d5bfe975/download-shared-links/

**예제 응답**

    [
        {
            "view_count": 0,
            "name": "/",
            "share_type": "d",
            "creator_name": "lian",
            "create_by": "lian@lian.com",
            "token": "105f108fb6",
            "create_time": "2016-01-18T15:03:10+0800",
            "path": "/",
            "size": ""
        },
        {
            "view_count": 3,
            "name": "1.md",
            "share_type": "f",
            "creator_name": "lian",
            "create_by": "lian@lian.com",
            "token": "a626012c1b",
            "create_time": "2016-01-19T11:27:43+0800",
            "path": "/1.md",
            "size": "4"
        }
    ]

**오류**

* 403 권한 거부.
* 404 라이브러리 없음.

#### <a id="get-library-upload-links"></a>라이브러리 업로드 링크 확인 ###

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/upload-shared-links/

**요청 매개변수**

* repo-id

**예제 요청**

    curl -H 'Authorization: Token 24fd3c026886e3121b2ca630805ed425c272cb96' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/632ab8a8-ecf9-4435-93bf-f495d5bfe975/upload-shared-links/

**예제 응답**

    [
        {
            "view_count": 3,
            "name": "/",
            "creator_name": "lian",
            "create_by": "lian@lian.com",
            "token": "43340efca5",
            "create_time": "2016-01-18T15:03:12+0800",
            "path": "/"
        },
        {
            "view_count": 8,
            "name": "a&b",
            "creator_name": "lian",
            "create_by": "lian@lian.com",
            "token": "f1e49d445a",
            "create_time": "2016-01-18T15:03:18+0800",
            "path": "/a&b/"
        }
    ]

**오류**

* 403 권한 거부.
* 404 라이브러리 없음.

#### <a id="delete-library-download-link"></a>라이브러리 다운로드 링크 삭제 ###

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/download-shared-links/{token}/

**요청 매개변수**

* repo-id
* token

**예제 요청**

    curl -X DELETE -H 'Authorization: Token 24fd3c026886e3121b2ca630805ed425c272cb96' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/632ab8a8-ecf9-4435-93bf-f495d5bfe975/download-shared-links/105f108fb6/

**예제 응답**

    {"success": true}

**오류**

* 403 권한 거부.
* 404 라이브러리 없음.
* 404 링크 없음.

#### <a id="delete-library-upload-link"></a>라이브러리 업로드 링크 삭제 ###

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/upload-shared-links/{token}/

**요청 매개변수**

* repo-id
* token

**예제 요청**

    curl -X DELETE -H 'Authorization: Token 24fd3c026886e3121b2ca630805ed425c272cb96' -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/632ab8a8-ecf9-4435-93bf-f495d5bfe975/upload-shared-links/f1e49d445a/

**예제 응답**

    {"success": true}

**오류**

* 403 권한 거부.
* 404 라이브러리 없음.
* 404 링크 없음.

## <a id="file"></a>파일 ##

### <a id="view-file-through-owa"></a>오피스 웹 앱으로 파일 보기 ###

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/owa-file/?path=/foo.docx

**요청 매개변수**

* repo-id
* path

**예제 요청**

    curl  -v  -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' 'https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/owa-file/?path=/foo.docx'

**예제 응답**

```
{
    "access_token": "7decacff-6e55-4856-9734-01aaab26ef45",
    "action_url": "http://off1.off.com/wv/wordviewerframe.aspx?WOPIsrc=http%3A%2F%2F192.168.1.124%3A8000%2Fapi2%2Fwopi%2Ffiles%2F2b0750085925fa85238e5f64cfd13ed6f1076bfd%2F",
    "access_token_ttl": 1456906784000
}
```

**응답을 받은 후**

오피스 온라인 프로그램을 예로 들어 설명하자면, 호스트에서 WOPI 동작 URL을 가리키는 iframe 구성 요소가 들어간 개별 HTML 페이지를 만들어야합니다. 다음, form 구성 요소를 활용하여 `access_token` 및 `access_token_ttl`값으로 오피스 온라인에 POST 요청 처리합니다.

자세한 내용은 [공식 문서](http://wopi.readthedocs.org/en/latest/hostpage.html)를 참고할 수 있습니다.

**오류**

* 400 잘못된 경로.
* 403 권한 거부.
* 403 라이브러리 암호화함.
* 403 오피스 웹 앱 기능 활성화 안함.
* 403 오피스 웹 앱 기능은 전문가판에서만 지원함.
* 404 파일/라이브러리 없음.
* 500 내부 서버 오류

### <a id="download-file"></a>파일 다운로드 ###

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/file/?p=/foo

**요청 매개변수**

* repo-id
* p
* reuse(선택): 만든 다운로드 링크를 한시간 이상 접근할 수 있게 하려면 `reuse`를 `1`로 설정하십시오.

**예제 요청**

    curl  -v  -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' 'https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/?p=/foo.c&reuse=1'

**예제 응답**

    "https://cloud.seafile.com:8082/files/adee6094/foo.c"

**오류**

* 400 경로 빠짐
* 404 파일 없음
* 520 처리 실패.

### <a id="get-file-detail"></a>파일 정보 확인 ###

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/file/detail/?p=/foo.c

* repo-id
* p

**예제 요청**

    curl -H 'Authorization: Token f2210dacd3606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/detail/?p=/foo.c

**예제 응답**

    {
    "id": "013d3d38fed38b3e8e26b21bb3463eab6831194f",
    "mtime": 1398148877,
    "type": "file",
    "name": "foo.py",
    "size": 22
    }

**오류**

* 400 경로 빠짐
* 520 처리 실패.

### <a id="get-file-history"></a>파일 기록 확인 ###

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/file/history/?p=/foo.c

**요청 매개변수**

* repo-id
* p

**예제 요청**

    curl -H 'Authorization: Token f2210dacd3606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/history/?p=/foo.c

**예제 응답**

    {
    "commits":
        [
            {
            "rev_file_size": 0,
            "repo_id": "a582d3bc-bcf5-421e-9125-741fa56d18d4",
            "ctime": 1398149763,
            "creator_name": "user@example.com",
            "creator": "0000000000000000000000000000000000000000",
            "root_id": "b64d413d9894c9206beac3faf9c2a0d75b4a8ebf",
            "rev_renamed_old_path": null,
            "parent_id": "8e546762e1657ab22dad83e9cb1e5ea31a767c9a",
            "new_merge": false,
            "version": 1,
            "conflict": false,
            "desc": "Added \"foo.c\"",
            "id": "9464f7499bfa7363d563282361339eaf96a93318",
            "rev_file_id": "0000000000000000000000000000000000000000",
            "second_parent_id": null
            },
            {
            "rev_file_size": 0,
            "repo_id": "a582d3bc-bcf5-421e-9125-741fa56d18d4",
            "ctime": 1398146059,
            "creator_name": "user@example.com",
            "creator": "0000000000000000000000000000000000000000",
            "root_id": "572413414257c76039897e00aeb35f819471206b",
            "rev_renamed_old_path": null,
            "parent_id": "f977bdb0ebb205645c3b42216c2817e511c3f68f",
            "new_merge": false,
            "version": 1,
            "conflict": false,
            "desc": "Added \"foo.c\"",
            "id": "a1ec20709675f4dc8db825cdbca296be245d189b",
            "rev_file_id": "0000000000000000000000000000000000000000",
            "second_parent_id": null
            }
        ]
    }

**오류**

* 400 경로 빠짐
* 404 파일 없음

### <a id="download-file-revision"></a>파일 특정 리비전 다운로드 ###

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/file/revision/?p=/foo.c&commit_id=a1ec20709675f4dc8db825cdbca296be245d189b

**요청 매개변수**

* repo-id
* p
* commit_id

**예제 요청**

    curl -H 'Authorization: Token f2210dacd3606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/revision/?p=/foo.c\&commit_id=a1ec20709675f4dc8db825cdbca296be245d189b

**예제 응답**

    "https://cloud.seafile.com:8082/files/adee6094/foo.c"

**오류**

* 400 경로 빠짐
* 404 리비전 없음

### <a id="create-file"></a>파일 만들기 ###

**POST** https://cloud.seafile.com/api2/repos/{repo-id}/file/?p=/foo.c

**요청 매개변수**

* repo-id
* p
* operation

**예제 요청**

    curl -v -d "operation=create" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/?p=/foo.c

**예제 응답**

    ...
    < HTTP/1.1 201 CREATED
    ...
    "success"

**성공**

   응답 코드는 201이며, `"success"` 문자열을 반환합니다.

**오류**

* 403 금지된 동작, 파일 이동 권한 없음
* 520 처리 실패, 파일 만들기 실패

### <a id="rename-file"></a>파일 이름 바꾸기 ###

**POST** https://cloud.seafile.com/api2/repos/{repo-id}/file/?p=/foo.c

**요청 매개변수**

* repo-id
* p
* operation=rename
* newname

**예제 요청**

    curl -v -d "operation=rename&newname=newfoo.c" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/?p=/foo.c

**예제 응답**

    ...
    < HTTP/1.1 301 MOVED PERMANENTLY
    ...
    "success"

**성공**

   응답 코드는 301이며, `"success"` 문자열을 반환합니다.

**오류**

* 400 잘못된 요청, 경로가 빠졌거나 잘못되었거나(예: p=/) 새 이름이 빠짐(새 이름이 너무 김)
* 403 금지됨, 파일 이름 바꾸기 권한 없음
* 404 찾을 수 없음, repo 없음
* 409 중복, 새 이름이 기존 이름과 동일
* 520 처리 실패, 파일 이름 바꾸기 실패

### <a id="lock-file"></a>파일 잠금 ###

**PUT** https://cloud.seafile.com/api2/repos/{repo-id}/file/

**요청 매개변수**

* repo-id
* p
* operation

**예제 요청**

    curl -v -X PUT -d "operation=lock&p=/foo.c" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/

**예제 응답**

    ...
    < HTTP/1.0 200 OK
    ...
    "success"

**성공**

   응답 코드는 200이며, `"success"` 문자열을 반환합니다.

**오류**

* 400 잘못된 요청, 경로가 빠졌거나 잘못됨(예: p=/)
* 403 금지된 동작, 파일 잠금 권한 없음
* 404 찾을 수 없음, repo 없음
* 520 처리 실패, 파일 잠금 실패

### <a id="unlock-file"></a>파일 잠금 해제 ###

**PUT** https://cloud.seafile.com/api2/repos/{repo-id}/file/

**요청 매개변수**

* repo-id
* p
* operation

**예제 요청**

    curl -v -X PUT -d "operation=unlock&p=/foo.c" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/

**예제 응답**

    ...
    < HTTP/1.0 200 OK
    ...
    "success"

**성공**

   응답 코드는 200이며, `"success"` 문자열을 반환합니다.

**오류**

* 400 잘못된 요청, 경로가 빠졌거나 잘못됨(예: p=/)
* 403 금지된 동작, 파일 잠금 권한 없음
* 404 찾을 수 없음, repo 없음
* 520 처리 실패, 파일 잠금 해제 실패

### <a id="move-file"></a>파일 이동 ###

**POST** https://cloud.seafile.com/api2/repos/{repo-id}/file/?p=/foo.c

**요청 매개변수**

* repo-id
* p
* operation
* dst_repo
* dst_dir

**예제 요청**

    curl -v -d "operation=move&dst_repo=affc837f-7fdd-4e91-b88a-32caf99897f2&dst_dir=/" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/?p=/foo.c

**예제 응답**

    ...
    < HTTP/1.1 301 MOVED PERMANENTLY
    ...
    "success"

**성공**

   응답 코드는 301이며, `"success"` 문자열을 반환합니다.

**오류**

* 400 잘못된 요청, 경로가 빠졌거나 잘못됨(예: p=/)
* 403 금지된 동작, 파일 이동 권한 없음
* 404 찾을 수 없음, repo 없음
* 500 내부 서버 오류

### <a id="copy-file"></a>파일 복사 ###

**POST** https://cloud.seafile.com/api2/repos/{repo-id}/file/?p=/foo.c

**요청 매개변수**

* repo-id
* p
* operation
* dst_repo
* dst_dir

**예제 요청**

    curl -v -d "dst_repo=73ddb2b8-dda8-471b-b7a7-ca742b07483c&dst_dir=/&file_names=foo.c" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' https://cloud.seafile.com/api2/repos/c7436518-5f46-4296-97db-2fcba4c8c8db/file/?p=/foo.c

**예제 응답**

    ...
    < HTTP/1.1 200 OK
    ...
    "success"

**성공**

   응답 코드는 200이며, `"success"` 문자열을 반환합니다.

**오류**

* 400 잘못된 요청, 경로가 빠졌거나 잘못됨(예: p=/)
* 403 금지된 동작, 파일 복사 권한 없음
* 500 내부 서버 오류

### <a id="revert-file"></a>파일 복원 ###

**PUT** https://cloud.seafile.com/api2/repos/{repo_id}/file/revert/

**요청 매개변수**

* repo_id
* p
* commit_id

**예제 요청**

    curl -v -X PUT -d "commit_id=a1ec20709675f4dc8db825cdbca296be245d189b&p=/foo.c" -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/8f5f2222-72a8-454f-ac40-8397c5a556a8/file/revert/

**예제 응답**

    ...
    < HTTP/1.0 200 OK
    ...

    {"ret": 0}

**성공**

    Response code 200(OK) is returned.

**오류**

* 400 경로 빠짐

### <a id="delete-file"></a>파일 삭제 ###

**DELETE** https://cloud.seafile.com/api2/repos/{repo-id}/file/?p=/foo

**요청 매개변수**

* repo-id
* p

**예제 요청**

    curl -X DELETE -v  -H 'Authorization: Token f2210dacd3606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/file/?p=/foo.c

**예제 응답**

    ...
    < HTTP/1.0 200 OK
    ...
    "success"

**오류**

* 400 경로 빠짐
* 520 처리 실패.

**참고**

   디렉터리를 삭제할 수도 있습니다.

### <a id="upload-file"></a>파일 업로드 ###

#### <a id="get-upload-link"></a>업로드 링크 확인

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/upload-link/?p=/upload-dir

**요청 매개변수**

* repo-id
* p ('/'를 기본값으로 사용)

**예제 요청**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" https://cloud.seafile.com/api2/repos/99b758e6-91ab-4265-b705-925367374cf0/upload-link/

**예제 응답**

    "http://cloud.seafile.com:8082/upload-api/73c5d117-3bcf-48a0-aa2a-3f48d5274ae3"

**오류**

    403 권한 거부.
    500 제한 용량 초과

#### <a id="upload-file-1"></a>파일 업로드

업로드 링크를 확인하고 나면, 업로드할 파일에 이 링크로 POST 요청을 보냅니다.

**POST** http://cloud.seafile.com:8082/upload-api/73c5d117-3bcf-48a0-aa2a-3f48d5274ae3

**오류**

    400 잘못된 요청
    440 잘못된 파일 이름
    500 내부 서버 오류

**예제 요청**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -F file=@test.txt -F filename=test.txt -F parent_dir=/ http://cloud.seafile.com:8082/upload-api/73c5d117-3bcf-48a0-aa2a-3f48d5274ae3

**예제 응답**

    "adc83b19e793491b1c6ea0fd8b46cd9f32e592fc"

**참고**

- 이미 상위 디렉터리에 'test.txt'가 있으면 새로 업로드한 파일 이름은 'test(1).txt'가 됩니다

- 파이썬 클라이언트 업로딩은 <https://github.com/haiwen/webapi-examples/blob/master/python/upload-file.py>, 더 쉽고 우아한 [python-requests 라이브러리](http://docs.python-requests.org/en/latest/)로 처리할 수 있습니다. <https://github.com/haiwen/webapi-examples/blob/master/python/upload-file2.py>를 참고하십시오.

### <a id="update-file"></a>파일 업데이트 ###

#### <a id="get-update-link"></a>업데이트 링크 확인

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/update-link/?p=/update-dir

**요청 매개변수**

* repo-id
* p ('/'를 기본값으로 사용)

**예제 요청**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" https://cloud.seafile.com/api2/repos/99b758e6-91ab-4265-b705-925367374cf0/update-link/

**예제 응답**

    "http://cloud.seafile.com:8082/update-api/e69e5ee7-9329-4f42-bf1b-12879bd72c28"

**오류**

    403 권한 거부.
    500 제한 용량 초과

#### <a id="update-file-1"></a>파일 업데이트

업데이트 링크를 확인하고 나면, 업데이트할 파일에 이 링크로 POST 요청을 보냅니다.

**POST** http://cloud.seafile.com:8082/update-api/e69e5ee7-9329-4f42-bf1b-12879bd72c28

**요청 매개변수**

* target_file

**예제 요청**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -F file=@test.txt -F filename=test.txt -F target_file=/test.txt http://cloud.seafile.com:8082/update-api/e69e5ee7-9329-4f42-bf1b-12879bd72c28

**반환**

업데이트한 파일의 ID

**예제 응답**

    "adc83b19e793491b1c6ea0fd8b46cd9f32e592fc"

**오류**

- 400 잘못된 요청
- 440 잘못된 파일 이름
- 500 내부 서버 오류

### <a id="get-upload-blks-link"></a>블록 업로드 링크 확인

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/upload-blks-link/

**요청 매개변수**

* repo-id

**예제 요청**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" https://cloud.seafile.com/api2/repos/99b758e6-91ab-4265-b705-925367374cf0/upload-blks-link/

**예제 응답**

    "https://cloud.seafile.com/seafhttp/upload-blks-api/569213db-7297-457a-907d-e2259a277c05"

**오류**

- 403 repo에 접근할 수 없음
- 520 제한 용량 초과

### <a id="get-update-blks-link"></a>블록 업데이트 링크 확인

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/update-blks-link/

**요청 매개변수**

* repo-id

**예제 요청**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" https://cloud.seafile.com/api2/repos/99b758e6-91ab-4265-b705-925367374cf0/update-blks-link/

**예제 응답**

    "https://cloud.seafile.com/seafhttp/update-blks-api/402c6d48-fe52-4592-97dd-85f462f03d66"

**오류**

- 403 repo에 접근할 수 없음
- 520 제한 용량 초과

## <a id="directory">디렉터리 ##

### <a id="list-directory-entries"></a>디렉터리 항목 조회 ###

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/dir/

* repo-id
* p(선택): 디렉터리 경로. `p`가 빠지면, 최상단 디렉터리 '/' 값을 기본값으로 설정합니다.
* oid(선택): 디렉터리의 객체 ID. 객체 ID는 디렉터리 내용의 체크섬입니다.
* t(선택): `t` 인자를 `f`로 설정하면 파일 항목만,  `d`로 설정하면 디렉터리 항목만 반환합니다.
* recursive (optional): `t` 인자를 `d`로 설정 **하고** `recursive` 인자를 `1`로 설정하면, 모든 디렉터리 항목을 재귀적으로 찾아 반환합니다

**예제 요청**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d9b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/repos/99b758e6-91ab-4265-b705-925367374cf0/dir/?p=/foo

**예제 응답**

   OID가 현재 디렉터리의 OID와 동일하면 `"uptodate"` 를, 그렇지 않으면 다음을 반환합니다

    [
    {
        "id": "0000000000000000000000000000000000000000",
        "type": "file",
        "name": "test1.c",
        "size": 0
    },
    {
        "id": "e4fe14c8cda2206bb9606907cf4fca6b30221cf9",
        "type": "dir",
        "name": "test_dir"
    }
    ]

**오류**

* 404 경로 없음.
* 440 암호화 한 Repo에 암호 제시 안함.
* 520 처리 실패.

### <a id="create-new-directory"></a>새 디렉터리 만들기 ###

**POST** https://cloud.seafile.com/api2/repos/{repo-id}/dir/

* repo-id
* p
* operation=mkdir (post)

**예제 요청**

    curl -d  "operation=mkdir" -v  -H 'Authorization: Tokacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/dir/?p=/foo

**예제 응답**

    ...
    < HTTP/1.0 201 CREATED
    < Location: https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/dir/?p=/foo
    ...

    "success"

**성공**

   응답 코드 201(Created)를 반환하고, Location 헤더에 만든 디렉터리 주소를 제공합니다.

**오류**

* 400 경로가 빠졌거나 잘못됨(e.g. p=/)
* 520 처리 실패.

**참고**

   같은 이름을 가진 디렉터리가 있으면 새로 만든 디렉터리 이름을 바꿉니다.

### <a id="rename-directory"></a>디렉터리 이름 바꾸기 ###

**POST** https://cloud.seafile.com/api2/repos/{repo-id}/dir/?p=/foo

**매개변수**

* repo-id
* p (경로)
* operation=rename
* newname (디렉터리 새 이름)

**예제 요청**

    curl -d  "operation=rename&newname=pinkfloyd_newfolder" -v  -H 'Authorization: Tokacd9c6ccb8133606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/dir/?p=/foo

**성공**

   응답 코드 200, 모든 동작 정상 처리

**오류**

* 403 폴더 이름 바꾸기 권한 없음
* 400 새 이름 설정 안함
* 520 디렉터리 이름 바꾸기 실패(일반적인 문제)

**참고**

   이전 이름과 새 이름이 같으면 동작을 수행하지 않습니다.

### <a id="delete-directory"></a>디렉터리 삭제 ###

**DELETE** https://cloud.seafile.com/api2/repos/{repo-id}/dir/

* repo-id
* p

**예제 요청**

    curl -X DELETE -v  -H 'Authorization: Token f2210dacd3606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/dir/?p=/foo

**예제 응답**

    ...
    < HTTP/1.0 200 OK
    ...
    "success"

**성공**

   응답 코드는 200(OK) 이며, `"success"` 문자열을 반환합니다.

**오류**

* 400 경로가 빠졌거나 잘못됨(e.g. p=/)
* 520 처리 실패.

**참고**

   파일을 삭제할 때도 사용할 수 있습니다.

### <a id="Download-directory"></a>디렉터리 다운로드 ###

**GET** https://cloud.seafile.com/api2/repos/{repo-id}/dir/download/?p=/foo

* repo-id
* p

**예제 요청**

    curl -H 'Authorization: Token f2210dacd3606d94ff8e61d99b477fd' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/dae8cecc-2359-4d33-aa42-01b7846c4b32/dir/?p=/foo

**예제 응답**

    "https://cloud.seafile.com:8082/files/adee6094/foo"

**오류**

* 400 경로가 빠졌거나 잘못되었거나(예: p=/), 크기가 너무 커서 디렉터리를 다운로드할 수 없음
* 404 Repo(path) 없음
* 520 처리 실패.

### <a id="share-directory"></a>디렉터리 공유 ###

**PUT** https://cloud.seafile.com/api2/repos/{repo-id}/dir/shared_items/?p={path}

* repo-id
* path
* permission, `r`/`rw`
* share_type, `user`/`group`
* username, share_type이 user면 필요합니다
* group_id, share_type이 group이면 필요합니다

**사용자 대상 폴더 공유 요청 예제**

    curl -X PUT -d "username=2@1.com&share_type=user&&perm=r" -H 'Authorization: Token ef12bf1e66a1aa797a1d6556fdc9ae84f1e9249f' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/78c620ee-2989-4427-8eff-7748f4fbebc0/dir/shared_items/?p=/q

**사용자 대상 폴더 공유 응답 예제**

    {"failed": [], "success": [{"user_info": {"nickname": "2", "name": "2@1.com"}, "share_type": "user", "permission": "r"}]}

**그룹 대상 폴더 공유 요청 예제**

    curl -X PUT -d "group_id=772&share_type=group&&perm=rw" -H 'Authorization: Token ef12bf1e66a1aa797a1d6556fdc9ae84f1e9249f' -H 'Accept: application/json; charset=utf-8; indent=4' https://cloud.seafile.com/api2/repos/78c620ee-2989-4427-8eff-7748f4fbebc0/dir/shared_items/?p=/q

**그룹 대상 폴더 공유 응답 예제**

    {"failed": [], "success": [{"group_info": {"id": 772, "name": "group-2"}, "share_type": "group", "permission": "r"}]}

**오류**

* 400 잘못된 share_type/permission/group_id 값.
* 403 권한 거부.
* 404 라이브러리/폴더/그룹 없음.
* 500 하위 repo 확인 실패.

## <a id="multiple-files-directories">다중 파일 / 디렉터리 ##

### <a id="multiple-files-directories-copy"></a>복사 ###

**POST** https://cloud.seafile.com/api2/repos/{repo_id}/fileops/copy/

**요청 매개변수**

* p: 원본 폴더 경로. 기본값 `"/"`
* file_names: 복사할 파일/폴더 목록. 다중 파일/폴더 이름을 `:`으로 구분할 수 있습니다.
* dst_repo: 대상 repo ID
* dst_dir: `dst_repo`의 대상 폴더

**예제 요청**

    curl -d "dst_repo=73ddb2b8-dda8-471b-b7a7-ca742b07483c&dst_dir=/&file_names=foo.c:bar.c:dir1:dir2" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' https://cloud.seafile.com/api2/repos/c7436518-5f46-4296-97db-2fcba4c8c8db/fileops/copy/

**예제 응답**

    "success"

**오류**

* 400 인자 빠짐
* 403 파일 복사 권한 없음
* 404 repo 없음
* 502 파일 복사 실패

### <a id="multiple-files-directories-move"></a>이동 ###

**POST** https://cloud.seafile.com/api2/repos/{repo_id}/fileops/move/

**요청 매개변수**

* p: 원본 폴더 경로. 기본값 `"/"`
* file_names: 옮길 파일/폴더 이름 목록. 다중 파일/폴더 이름은 세미콜론으로 구분할 수 있습니다.
* dst_repo: 대상 repo ID
* dst_dir: `dst_repo`의 대상 폴더

**예제 요청**

    curl -d "dst_repo=73ddb2b8-dda8-471b-b7a7-ca742b07483c&dst_dir=/&file_names=foo.c:bar.c:dir1:dir2" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' https://cloud.seafile.com/api2/repos/c7436518-5f46-4296-97db-2fcba4c8c8db/fileops/move/

**예제 응답**

    "success"

**오류**

* 400 인자 빠짐
* 403 파일 이동 권한 없음
* 404 repo 없음
* 502 파일 이동 실패

### <a id="multiple-files-directories-delete"></a>삭제 ###

**POST** https://cloud.seafile.com/api2/repos/{repo_id}/fileops/delete/

**요청 매개변수**

* p: 원본 폴더 경로. 기본값 `"/"`
* file_names: 삭제할 파일/폴더 이름 목록. 다중 파일/폴더 이름은 세미콜론으로 구분할 수 있습니다.

**예제 요청**

    curl -d "file_names=foo.c:bar.c:dir1:dir2" -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' https://cloud.seafile.com/api2/repos/c7436518-5f46-4296-97db-2fcba4c8c8db/fileops/delete/

**예제 응답**

    "success"

**오류**

* 400 인자 빠짐
* 403 파일 삭제 권한 없음
* 404 repo 없음
* 502 파일 삭제 실패

## <a id="avatar"></a>아바타 ##

### <a id="get-user-avatar"></a>사용자 아바타 확인 ##

**GET** https://cloud.seafile.com/api2/avatars/user/{user}/resized/{size}/

**요청 매개변수**

* user
* size

**예제 요청**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/avatars/user/user@example.com/resized/80/"

**예제 응답**

    {
        "url": "http://127.0.0.1:8000/media/avatars/default.png",
        "is_default": true,
        "mtime": 0
    }

### <a id="get-group-avatar"></a>그룹 아바타 확인 ##

**GET** https://cloud.seafile.com/api2/avatars/group/{group_id}/resized/{size}/

**요청 매개변수**

* group_id
* size

**예제 요청**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/avatars/group/1/resized/80/"

**예제 응답**

    {
        "url": "http://127.0.0.1:8000/media/avatars/groups/default.png",
        "is_default": true,
        "mtime": 0
    }

## <a id="devices"></a>장치 ##

### <a id="get-user-devices"></a>사용자 장치 확인 ##

**GET** https://cloud.seafile.com/api2/devices/

**예제 요청**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/devices/

**예제 응답**

```
[
    {
        "synced_repos": [
            {
                "repo_id": "47945b31-dedb-4b92-a048-32bf825595ce",
                "sync_time": 1458008928,
                "repo_name": "wopi"
            },
            {
                "repo_id": "78c620ee-2989-4427-8eff-7748f4fbebc0",
                "sync_time": 1457943466,
                "repo_name": "lib-of-lian"
            }
        ],
        "last_accessed": "2016-03-15T10:28:48+08:00",
        "device_name": "lian",
        "platform_version": "",
        "platform": "linux",
        "user": "lian@lian.com",
        "key": "99abe1a7cc7d614db0bfa19db81e42ef675abe4f",
        "client_version": "5.0.0",
        "last_login_ip": "192.168.1.16",
        "device_id": "be10980211752515053bf9036a13139375de0cc8"
    },
    {
        "last_accessed": "2016-03-15T13:59:51+08:00",
        "device_name": "PLK-AL10",
        "platform_version": "5.0.2",
        "platform": "android",
        "user": "lian@lian.com",
        "key": "067051c94163ed193f2131d48c61882daa7cb238",
        "client_version": "2.0.3",
        "last_login_ip": "192.168.1.208",
        "device_id": "4a0d62c1f27b3b74"
    }
]
```

**오류**

* 401 인증하지 않음

### <a id="unlink-user-device"></a>사용자 장치 연결 해제 ##

**DELETE** https://cloud.seafile.com/api2/devices/

**요청 매개변수**

* platform
* device_id

**예제 요청**

    curl -X DELETE -d "platform=linux&device_id=be10980211752515053bf9036a13139375de0cc8" -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/devices/

**예제 응답**

    {"success": true}

**오류**

* 400 잘못된 플랫폼
* 400 잘못된 device_id 값
* 500 내부 서버 오류

## <a id="get-file-activities"></a>파일 활동 확인 ###

**GET** https://cloud.seafile.com/api2/events/

**요청 매개변수**

이 API는 전체 활동 내역 레코드 중 첫 15개만 반환합니다. 더 많은 레코드를 가져오려면 `start` 매개변수 값을 전달하십시오

* start (기본값 0)

**예제 요청**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/events/"

**예제 응답**


     {"more_offset": 15, "events":[{"repo_id": "6f3d28a4-73ae-4d01-a727-26774379dcb9", "author": "mysnowls@163.com", "nick": "lins05", "time": 1398078909, "etype": "repo-update", "repo_name": "Downloads", "desc": "Added \"seafile-cli_3.0.2_i386.tar.gz\"."},{"repo_id": "6f3d28a4-73ae-4d01-a727-26774379dcb9", "author": "mysnowls@163.com", "nick": "lins05", "time": 1398075540, "etype": "repo-update", "repo_name": "Downloads", "desc": "Added \"seafile-server_3.0.0_x86-64.tar.gz\"."}], "more": false}

**더 많은 활동 요청 예제**

    curl -H 'Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd' "https://cloud.seafile.com/api2/events/?start=15"

**더 많은 활동 응답 예제**

     {"more_offset": 30, "events":[{"repo_id": "6f3d28a4-73ae-4d01-a727-26774379dcb9", "author": "mysnowls@163.com", "nick": "lins05", "time": 1398078909, "etype": "repo-update", "repo_name": "Downloads", "desc": "Added \"seafile-cli_3.0.2_i386.tar.gz\"."},{"repo_id": "6f3d28a4-73ae-4d01-a727-26774379dcb9", "author": "mysnowls@163.com", "nick": "lins05", "time": 1398075540, "etype": "repo-update", "repo_name": "Downloads", "desc": "Added \"seafile-server_3.0.0_x86-64.tar.gz\"."}], "more": false}

## <a id="get-thumbnail-image"></a>썸네일 그림 확인 ##

**GET** https://cloud.seafile.com/api2/repos/{repo_id}/thumbnail/

**요청 매개변수**

* repo_id
* p
* size

**예제 요청**

    curl -H 'Authorization: Token 40f9a510a0629430865dc199a3880898ad2e48fc' https://cloud.seafile.com/api2/repos/fbead5d0-4817-4446-92f3-7ac8e6a8e5f5/thumbnail/?p=/5.jpg\&size=123 > thumbnail.png

## <a id="add-organization"></a>조직 추가 ##

이 API는 seaclud.cc에서 조직 계정을 만들때만 내부적으로 사용합니다.

**POST** https://cloud.seafile.com/api2/organization/

**요청 매개변수**

* username
* password
* org_name
* prefix
* quota
* member_limit

**예제 요청**

    curl -v -X POST -d "username=example@example.com&password=example&org_name=example&prefix=example&quota=100&member_limit=10" -H "Authorization: Token ccdff90e4d1efe76b2b3d91c06b027a5cff189d4" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/organization/

**예제 응답**

    "success"


참고: 다음 API는 Seafile v5.1부터 사용할 수 있습니다.

# <a id="admin-only"></a>관리자 전용 ##

## <a id="admin-only-account"></a>계정 ##

### <a id="admin-only-list-accounts"></a>계정 조회 ###

**GET** https://cloud.seafile.com/api2/accounts/

**요청 매개변수**

* start (기본값 0)
* limit (기본값 100)
* scope (기본값 없음, 유효값: 'LDAP'/'DB')

모든 사용자를 가져오려면 `start`와 `limit`를 `-1`로 설정하십시오.

범위 매개 변수를 전달했다면, 지정 범위 내에서 계정을 검색합니다. 범위 값을 전달하지 않으면 종전 방식대로 진행합니다: 우선 LDAP를, 계정이 없으면 그 다음 DB를 검색합니다.

**예제 요청**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/accounts/

**예제 응답**

    [
    {
        "email": "foo@foo.com"
    },
    {
        "email": "bar@bar.com"
    }
    ]

**오류**

* 403 권한 오류. 관리자만 이 동작을 진행할 수 있습니다

### <a id="admin-only-get-account"></a>계정 정보 확인 ###

**GET** https://cloud.seafile.com/api2/accounts/{email}/

**요청 매개변수**

**예제 요청**

    curl -v -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/accounts/user@mail.com/

**예제 응답**

    {
    "is_staff": false,
    "is_active": true,
    "id": 2,
    "create_time": 1356061187741686,
    "usage": 651463187,
    "total": 107374182400,
    "email": "user@mail.com"
    }

**오류**

* 403 권한 오류. 관리자만 이 동작을 진행할 수 있습니다

### <a id="admin-only-create-account"></a>계정 만들기 ###

**PUT** https://cloud.seafile.com/api2/accounts/{email}/

**요청 매개변수**

* password
* is_staff (기본값 False)
* is_active (기본값 True)

**예제 요청**

    curl -v -X PUT -d "password=123456" -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/accounts/newaccount@gmail.com/

**예제 응답**

    ...
    < HTTP/1.0 201 CREATED
    < Location: https://cloud.seafile.com/api2/accounts/newaccount@gmail.com/
    ...

    "success"

**성공**

    응답 코드 201(만듬)를 반환하며 Location 헤더에 공유 링크를 제공합니다.

**오류**

* 403 권한 오류. 관리자만 이 동작을 진행할 수 있습니다

### <a id="admin-only-update-account"></a>계정 업데이트 ###

**PUT** https://cloud.seafile.com/api2/accounts/{email}/

**요청 매개변수**

최소한 다음 중 하나는 있어야합니다:

* password
* is_staff
* is_active
* name
* note
* storage

**예제 요청**

    curl -v -X PUT -d "password=654321&is_staff=true&storage=1073741824" -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/accounts/user@mail.com/

**예제 응답**

    ...
    < HTTP/1.0 200 OK
    ...

    "success"

**성공**

    Response code 200(OK) is returned.

**오류**

* 400 잘못된 요청. 키워드 암호가 필요합니다
* 403 권한 오류. 관리자만 이 동작을 진행할 수 있습니다

### <a id="admin-only-migrate-account"></a>계정 이전 ###

**POST** https://cloud.seafile.com/api2/accounts/{email}/

**요청 매개변수**

* op
* to_user 이 사용자는 반드시 있어야합니다

**예제 요청**

    curl -v -d "op=migrate&to_user=user2@mail.com" -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/accounts/user@mail.com/

**예제 응답**

    ...
    < HTTP/1.0 200 OK
    ...

    "success"

**성공**

    Response code 200(OK) is returned.

**오류**

* 400 잘못된 요청, 인자가 빠졌거나 잘못되었습니다
* 403 권한 오류. 관리자만 이 동작을 진행할 수 있습니다

### <a id="admin-only-delete-account"></a>계정 삭제 ###

**DELETE** https://cloud.seafile.com/api2/accounts/{email}/


**예제 요청**

    curl -v -X DELETE -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api2/accounts/newaccount@gmail.com/

**예제 응답**

    "success"

**오류**

* 403 권한 오류. 관리자만 이 동작을 진행할 수 있습니다

## <a id="admin-only-devices"></a>장치 ##

### <a id="admin-only-get-desktop-devices"></a>데스크톱 장치 확인 ##

데스크톱 장치의 첫 페이지(페이지당 레코드 50개)를 확인합니다.

**GET** https://cloud.seafile.com/api/v2.1/admin/devices/?platform=desktop&page=1&per_page=50

**예제 요청**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/devices/?platform=desktop&page=1&per_page=50

**예제 응답**

```
[
    {'has_next_page': False},
    [
        {
            'last_accessed': '2016-04-11T18:24:29+08:00',
            'last_login_ip': u'192.168.1.210',
            'platform': u'linux',
            'user': u'1@1.com',
            'client_version': u'2.0.4',
            'device_name': u'PLK-AL10',
            'device_id': u'4a0d62c1f27b3b74'
        }
    ]
]
```

**오류**

* 403 권한 오류. 관리자만 이 동작을 진행할 수 있습니다

### <a id="admin-only-get-mobile-devices"></a>모바일 장치 확인 ##

모바일 장치의 첫 페이지(페이지당 레코드 50개)를 확인합니다.

**GET** https://cloud.seafile.com/api/v2.1/admin/devices/?platform=mobile&page=1&per_page=50

**예제 요청**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/devices/?platform=mobile&page=1&per_page=50

**예제 응답**

```
[
    {'has_next_page': False},
    [
        {
            'last_accessed': '2016-04-11T18:24:29+08:00',
            'last_login_ip': u'192.168.1.210',
            'platform': u'ios',
            'user': u'1@1.com',
            'client_version': u'2.0.4',
            'device_name': u'PLK-AL10',
            'device_id': u'4a0d62c1f27b3b74'
        }
    ]
]
```

**오류**

* 403 권한 오류. 관리자만 이 동작을 진행할 수 있습니다

### <a id="admin-only-unlink-user-device"></a>사용자 장치 연결 끊기 ##

**DELETE** https://cloud.seafile.com/api/v2.1/admin/devices/

**요청 매개변수**

* platform
* device_id
* user

**예제 요청**

    curl -X DELETE -d "platform=linux&device_id=be10980211752515053bf9036a13139375de0cc8&user=1@1.com" -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/devices/

**예제 응답**

    {"success": true}

**오류**

* 400 잘못된 플랫폼
* 400 잘못된 device_id 값
* 400 잘못된 사용자
* 500 내부 서버 오류

### <a id="admin-only-get-device-errors"></a>장치 오류 확인 ##

**GET** https://cloud.seafile.com/api/v2.1/admin/device-errors/

**예제 요청**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/device-errors/

**예제 응답**

```
[
    {
        'repo_id': u'47945b31-dedb-4b92-a048-32bf825595ce',
        'device_ip': u'192.168.1.124',
        'error_time': '2016-04-13T17:49:11+08:00',
        'device_name': u'lian-ubuntu-1404-64',
        'email': u'1@1.com',
        'client_version': u'5.0.6',
        'error_msg': u'No permission.',
        'repo_name': u'wopi'
    }
]
```

**오류**

* 403 기능 비활성화.
* 500 내부 서버 오류

**참고** 이 API는 전문가판에서만 지원합니다.

### <a id="admin-only-clean-device-errors"></a>장치 오류 정리 ##

**DELETE** https://cloud.seafile.com/api/v2.1/admin/device-errors/

**예제 요청**

    curl -X DELETE -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/device-errors/

**예제 응답**

```
{"success":true}
```

**오류**

* 403 기능 비활성화.
* 500 내부 서버 오류

**참고** 이 API는 전문가판에서만 지원합니다.

## <a id="admin-only-log"></a>관리자 로그 ##

### <a id="admin-only-get-login-log"></a>로그인 로그 확인 ##

**GET** https://cloud.seafile.com/api/v2.1/admin/logs/login/?start=2016-03-20&end=2016-03-31

**예제 요청**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/logs/login/?start=2016-03-20&end=2016-03-31

**예제 응답**

```
[
    {
        'email': u'lian@lian.com',
        'login_ip': u'192.168.1.124',
        'name': u'lian',
        'login_time': '2016-03-31T14:42:23+08:00'
    },
    {
        'email': u'org@org.com',
        'login_ip': u'192.168.1.124',
        'name': u'org',
        'login_time': '2016-03-31T14:39:08+08:00'
    }
]
```

**오류**

* 400 개시 또는 종료 일자 올바르지 않음.
* 403 기능 비활성화.

**참고** 이 API는 전문가판에서만 지원합니다.

### <a id="admin-only-get-file-audit-log"></a>파일 감사 로그 확인 ##

**GET** https://cloud.seafile.com/api/v2.1/admin/logs/file-audit/?start=2016-03-20&end=2016-03-31

**예제 요청**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/logs/file-audit/?start=2016-03-20&end=2016-03-31

**예제 응답**

```
[
    {
        'repo_id': u'4929d0df-8c6c-43cb-8edf-40a8489689fb',
        'time': '2016-03-31T05:46:03+08:00',
        'etype': u'file-download-web',
        'ip': u'192.168.1.124',
        'user_name': u'org',
        'file_path': u'/earth.jpg',
        'user_email': u'org@org.com',
        'repo_name': ''
    },
    {
        'repo_id': u'513cd72c-c54a-463e-a18f-841efe91bd61',
        'time': '2016-03-31T06:25:22+08:00',
        'etype': u'file-download-web',
        'ip': u'192.168.1.124',
        'user_name': u'org',
        'file_path': u'/kj.md',
        'user_email': u'org@org.com',
        'repo_name': u'new-lib-of-org-1'
    }
]
```

**오류**

* 400 개시 또는 종료 일자 올바르지 않음.
* 403 기능 비활성화.

**참고** 이 API는 전문가판에서만 지원합니다.

### <a id="admin-only-get-file-update-log"></a>파일 업데이트 로그 확인 ##

**GET** https://cloud.seafile.com/api/v2.1/admin/logs/file-update/?start=2016-03-20&end=2016-03-31

**예제 요청**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/logs/file-update/?start=2016-03-20&end=2016-03-31

**예제 응답**

```
[
    {
        'commit_id': u'55ec5350b16d6c72a044b5a9cd9b2d62ad439364',
        'file_operation': u'Added "user.csv".',
        'repo_id': u'513cd72c-c54a-463e-a18f-841efe91bd61',
        'repo_name': u'new-lib-of-org-1',
        'time': '2016-03-31T06:25:15+08:00',
        'user_email': u'org@org.com',
        'user_name': u'org'
    },
    {
        'commit_id': u'6820d809481e3c9fb856d0650ac73a09b570a301',
        'file_operation': u'Added "kj.md"',
        'repo_id': u'513cd72c-c54a-463e-a18f-841efe91bd61',
        'repo_name': u'new-lib-of-org-1',
        'time': '2016-03-31T06:25:21+08:00',
        'user_email': u'org@org.com',
        'user_name': u'org'
    }
]
```

**오류**

* 400 개시 또는 종료 일자 올바르지 않음.
* 403 기능 비활성화.

**참고** 이 API는 전문가판에서만 지원합니다.

### <a id="admin-only-get-perm-audit-log"></a>감사 로그 권한 확인 ##

**GET** https://cloud.seafile.com/api/v2.1/admin/logs/perm-audit/?start=2016-03-20&end=2016-03-31

**예제 요청**

    curl -H "Authorization: Token f2210dacd9c6ccb8133606d94ff8e61d99b477fd" -H 'Accept: application/json; indent=4' https://cloud.seafile.com/api/v2.1/admin/logs/perm-audit/?start=2016-03-20&end=2016-03-31

**예제 응답**

```
[
    {
        'etype': u'add-repo-perm',
        'file_path': u'/<img onerror=alert(1) src=a>_"_\u2126_%2F_W_#_12_\u8fd9',
        'from_email': u'org3@org3.com',
        'from_name': u'org3',
        'permission': u'rw',
        'repo_id': u'a84544e5-0b84-459d-b1e6-0399dabc76a0',
        'repo_name': '',
        'time': '2016-03-31T06:21:50+08:00',
        'to': u'org@org.com'
    },
    {
        'etype': u'add-repo-perm',
        'file_path': u'/<img onerror=alert(1) src=a>_"_\u2126_%2F_W_#_12_\u8fd9',
        'from_email': u'org3@org3.com',
        'from_name': u'org3',
        'permission': u'rw',
        'repo_id': u'a84544e5-0b84-459d-b1e6-0399dabc76a0',
        'repo_name': '',
        'time': '2016-03-31T06:21:53+08:00',
        'to': u'777'
    }
]
```

**오류**

* 400 개시 또는 종료 일자 올바르지 않음.
* 403 기능 비활성화.

**참고** 이 API는 전문가판에서만 지원합니다.

