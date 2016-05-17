# Seafile 클러스터 및 NFS 설정

Seafile 클러스터에서 Seafile 서버 인스턴스간 데이터를 공유하는 일반적인 방법은 NFS를 사용하는 방법입니다. NFS의 파일 객체만 공유할 수 있어야합니다. 여기서 어떻게 무엇을 공유하는지 지침을 제공해드리겠습니다.

NFS 서버 및 클라이언트 설정 방법은 이 위키 문서의 주제 범위를 벗어납니다. 몇가지 참고 자료가 있습니다:

* 우분투: https://help.ubuntu.com/community/SettingUpNFSHowTo
* CentOS: http://www.centos.org/docs/5/html/Deployment_Guide-en-US/ch-nfs.html

Seafile 서버 설치 디렉터리를 `/data/haiwen`이라고 하고, 설치 스크립트를 실행한 후 `seafile-data` 디렉터리를 해당 디렉터리에 만든다고 가정하겠습니다. 그리고 NFS 드라이브를 `/seafile-nfs`에 마운트한다고 가정하겠습니다. 다음 몇가지 과정을 따라야합니다:

* `seafile-data` 폴더를 `/seafile-nfs`에 옮기십시오:

```
mv /data/haiwen/seafile-data /seafile-nfs/
```


* 클러스터의 모든 노드에 공유 seafile-data 폴더의 심볼릭 링크를 만드십시오 

```
cd /data/haiwen
ln -s /seafile-nfs/seafile-data /data/haiwen/seafile-data
```


이 방법으로 각 인스턴스별로 동일한 `seafile-data` 폴더를 공유합니다. 기타 다른 설정 파일 및 로그 파일은 제각각의 인스턴스에 남습니다.

