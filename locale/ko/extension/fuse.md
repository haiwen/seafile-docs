# FUSE 확장 기능

Seafile 시스템의 파일은 블록 단위로 쪼개져있으며, Seafile 서버에 들어간 파일은 완전한 파일이 아닌 블록으로 저장했다는 의미입니다. 이 설계 수단은 데이터 중복 방지에 효과적입니다.

그러나 관리자는 때로 서버의 파일에 바로 접근하고 싶을 때가 있습니다. 이 때 seaf-fuse를 사용할 수 있습니다.

`Seaf-fuse`는 [FUSE](http://fuse.sourceforge.net) 가상 파일 시스템 구현체입니다. 말 그대로, 모든 Seafile의 파일을 폴더로 마운트('''마운트 지점'''이라 함)하여, 서버에서 일반 폴더에 접근하는 방식으로 Seafile 서버에서 관리하는 모든 파일에 접근할 수 있습니다.

참고:

* 암호화 폴더는 seaf-fuse로 접근할 수 없습니다.
* 현재 구현체는 '''읽기 전용''' 이며, 마운트한 폴더의 파일을 수정할 수 없음을 의미합니다.
* Debian/CentOS 시스템에서 FUSE 폴더 마운트 권한을 취득하려면 "fuse" 그룹에 들어가야합니다.

### seaf-fuse 시작 방법

`/data/seafile-fuse`에 마운트한다고 가정해보겠습니다.

##### 마운트 지점 폴더 만들기

<pre>
mkdir -p /data/seafile-fuse
</pre>

##### 스크립트로 seaf-fuse 시작하기

참고: seaf-fuse를 시작하기 전에 `./seafile.sh start`로 Seafile 서버를 시작해야합니다.

<pre>
./seaf-fuse.sh start /data/seafile-fuse
</pre>

커뮤니티 서버 4.2.1 및 전문가 서버 4.2.0부터, FUSE용 표준 마운트 옵션 스크립트를 지원합니다. 예를 들면, 마운트한 폴더의 소유 권한을 지정할 수 있습니다:

```
./seaf-fuse.sh start -o uid=<uid> /data/seafile-fuse
```

`man fuse`에서 지원 옵션 전부를 확인해볼 수 있습니다.

##### seaf-fuse 멈추기

<pre>
./seaf-fuse.sh stop
</pre>

### 마운트한 폴더의 내용

##### 최상위 폴더

`/data/seafile-fuse`의 내용을 확인해볼 수 있습니다.

<pre>
$ ls -lhp /data/seafile-fuse

drwxr-xr-x 2 root root 4.0K Jan  1  2015 abc@abc.com/
drwxr-xr-x 2 root root 4.0K Jan  4  2015 foo@foo.com/
drwxr-xr-x 2 root root 4.0K Jan  1  2015 plus@plus.com/
drwxr-xr-x 2 root root 4.0K Jan  1  2015 sharp@sharp.com/
drwxr-xr-x 2 root root 4.0K Jan  3  2015 test@test.com/
</pre>

* 최상위 폴더에는 여러가지 하위 폴더가 들어있는데, 이 폴더는 각 사용자의 저장 내용이 들어있습니다

##### 각 사용자 별 폴더

<pre>
$ ls -lhp /data/seafile-fuse/abc@abc.com

drwxr-xr-x 2 root root  924 Jan  1  1970 5403ac56-5552-4e31-a4f1-1de4eb889a5f_Photos/
drwxr-xr-x 2 root root 1.6K Jan  1  1970 a09ab9fc-7bd0-49f1-929d-6abeb8491397_My Notes/
</pre>

위에서 보신 바와 같이, 사용자의 라이브러리로 보이는 하위 폴더가 있는 사용자의 폴더는 '''{library_id}-{library-name}''' 형식의 이름이 달려있습니다.

##### 라이브러리용 폴더

<pre>
$ ls -lhp /data/seafile-fuse/abc@abc.com/5403ac56-5552-4e31-a4f1-1de4eb889a5f_Photos/

-rw-r--r-- 1 root root 501K Jan  1  2015 image.png
-rw-r--r-- 1 root root 501K Jan  1  2015 sample.jpng
</pre>

##### "Permission denied" 오류가 떴다면

`./seaf-fuse.sh start`를 실행할 때 "Permission denied" 오류 메시지가 뜬다면 대부분의 경우 "fuse 그룹"에 속해있지 않기 때문입니다. 다음 과정을 진행하십시오:

* fuse 그룹에 사용자 자신을 추가하십시오
<pre>
sudo usermod -a -G fuse <your-user-name>
</pre>

* 쉘에서 로그아웃 한 다음 다시 로그인해보십시오
* 이제 `./seaf-fuse.sh start <path>`명령을 다시 실행해보십시오.

