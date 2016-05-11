# Seafile
## Fuse 활용

Seafile 시스템의 파일은 블록 단위로 나뉘어 있으며, 완전한 파일이 아닌 블록 단위로 Seafile 서버에 저장해둠을 의미합니다. 이 설계 수단은 데이터 중복 방지에 효과적입니다.

그러나, 가끔 관리자는 서버의 파일에 바로 접근하고 싶을 때가 있습니다. 이 때 seaf-fuse를 사용할 수 있습니다.

<code>Seaf-fuse</code>는 [http://fuse.sourceforge.net FUSE] 가상 파일 시스템의 구현체입니다. 말 그대로, 모든 Seafile 파일을 폴더('''마운트 지점''')에 마운트하여, 서버의 일반 폴더에 접근하는 것처럼 Seafile 서버가 관리하는 모든 파일에 접근할 수 있습니다.

Seaf-fuse는 Seafile 서버 '''2.1.0'''부터 추가했습니다.

'''참고:'''
* 암호화 폴더는 seaf-fuse로 접근할 수 없습니다.
* 현재 구현체는 '''읽기 전용'''이며, 마운트한 폴더의 파일을 수정할 수 없습니다.
* 데비안/CentOS 시스템에서 FUSE 폴더의 접근 권한을 취하려면 해당 사용자를 "fuse" 그룹에 넣어야합니다.

## seaf-fuse 시작 방법

<code>/data/seafile-fuse</code>에 마운드해보겠다고 가정하겠습니다.

#### 마운트 지점 폴더 만들기

<pre>
mkdir -p /data/seafile-fuse
</pre>

#### 스크립트로 seaf-fuse 시작하기

'''Note:''' seaf-fuse를 시작하기 전, <code>./seafile.sh start</code> 명령으로 Seafile 서버를 시작해야합니다.

<pre>
./seaf-fuse.sh start /data/seafile-fuse
</pre>

#### seaf-fuse 중단

<pre>
./seaf-fuse.sh stop
</pre>

## 마운트한 폴더 내용

#### 최상위 단계 폴더

이제 <code>/data/seafile-fuse</code>의 내용을 살펴볼 수 있습니다.

<pre>
$ ls -lhp /data/seafile-fuse

drwxr-xr-x 2 root root 4.0K Jan  1  1970 abc@abc.com/
drwxr-xr-x 2 root root 4.0K Jan  1  1970 foo@foo.com/
drwxr-xr-x 2 root root 4.0K Jan  1  1970 plus@plus.com/
drwxr-xr-x 2 root root 4.0K Jan  1  1970 sharp@sharp.com/
drwxr-xr-x 2 root root 4.0K Jan  1  1970 test@test.com/
</pre>

* 최상위 폴더에는 여러가지 하위 폴더가 있는데, 이 하위 폴더는 각 사용자와 관련이 있습니다
* 파일 및 폴더의 타임스탬프는 보존하지 않습니다.

#### 사용자별 폴더

<pre>
$ ls -lhp /data/seafile-fuse/abc@abc.com

drwxr-xr-x 2 root root  924 Jan  1  1970 5403ac56-5552-4e31-a4f1-1de4eb889a5f_Photos/
drwxr-xr-x 2 root root 1.6K Jan  1  1970 a09ab9fc-7bd0-49f1-929d-6abeb8491397_My Notes/
</pre>

위 목록에서 보신 바와 같이, 사용자 폴더 아래에 하위 폴더가 있는데 각 폴더는 사용자의 라이브러리를 나타내며, '''{library_id}-{library-name}''' 형식의 이름이 갖춰져 있습니다.

#### 라이브러리용 폴더

<pre>
$ ls -lhp /data/seafile-fuse/abc@abc.com/5403ac56-5552-4e31-a4f1-1de4eb889a5f_Photos/

-rw-r--r-- 1 root root 501K Jan  1  1970 image.png
-rw-r--r-- 1 root root 501K Jan  1  1970 sample.jpng
</pre>

#### "Permission denied" 오류 발생시

<code>./seaf-fuse.sh start</code> 명령을 실행할 때 "Permission denied" 오류 메시지가 나타난다면, 대부분 여러분이 "fuse 그룹"에 속해있지 않았기 때문일지도 모릅니다. 다음 과정을 진행하십시오:

* fuse 그룹에 자신을 추가하십시오
<pre>
sudo usermod -a -G fuse <your-user-name>
</pre>
* 쉘에서 로그아웃 후 다시 로그인하십시오
* 이제<code>./seaf-fuse.sh start <path></code> 명령을 다시 실행해보십시오.

