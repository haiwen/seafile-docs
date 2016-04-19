# Seafile
## Fuse 활용

Files in the seafile system are split to blocks, which means what are stored on your seafile server are not complete files, but blocks. This design faciliates effective data deduplication.

그러나, 가끔 관리자는 서버의 파일에 바로 접근하고 싶을 때가 있습니다. 이 때 seaf-fuse를 사용할 수 있습니다.

<code>Seaf-fuse</code> is an implementation of the [http://fuse.sourceforge.net FUSE] virtual filesystem. In a word, it mounts all the seafile files to a folder (which is called the '''mount point'''), so that you can access all the files managed by seafile server, just as you access a normal folder on your server.

Seaf-fuse는 Seafile 서버 '''2.1.0''' 부터 추가했습니다:

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

* The top level folder contains many subfolders, each of which corresponds to a user
* The time stamp of files and folders is not preserved.

#### 사용자별 폴더

<pre>
$ ls -lhp /data/seafile-fuse/abc@abc.com

drwxr-xr-x 2 root root  924 Jan  1  1970 5403ac56-5552-4e31-a4f1-1de4eb889a5f_Photos/
drwxr-xr-x 2 root root 1.6K Jan  1  1970 a09ab9fc-7bd0-49f1-929d-6abeb8491397_My Notes/
</pre>

From the above list you can see, under the folder of a user there are subfolders, each of which represents a library of that user, and has a name of this format: '''{library_id}-{library-name}'''.

#### 라이브러리용 폴더

<pre>
$ ls -lhp /data/seafile-fuse/abc@abc.com/5403ac56-5552-4e31-a4f1-1de4eb889a5f_Photos/

-rw-r--r-- 1 root root 501K Jan  1  1970 image.png
-rw-r--r-- 1 root root 501K Jan  1  1970 sample.jpng
</pre>

#### "Permission denied" 오류 발생시

If you get an error message saying "Permission denied" when running <code>./seaf-fuse.sh start</code>, most likely you are not in the "fuse group". You should:

* fuse 그룹에 자신을 추가하십시오
<pre>
sudo usermod -a -G fuse <your-user-name>
</pre>
* 쉘에서 로그아웃 후 다시 로그인하십시오
* Now try <code>./seaf-fuse.sh start <path></code> again.

