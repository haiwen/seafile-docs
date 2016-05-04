# Seafile 커뮤니티 서버에서 이전

## <a id="wiki-restriction"></a>제한사항 ##

Seafile 커뮤니티판 서버를 가동중이고, [전문가판 서버](http://seafile.com/en/product/private_server/) 또는 그 반대로 전환하고 싶을 경우가 있습니다. 그런데, 몇가지 제한 사항이 있습니다:

- 커뮤니티 서버 및 전문가 서버의 부 버전이 같을 때만 전환할 수 있습니다.

그러니까 커뮤니티 서버 1.6을 사용하고 전문가 서버 1.7로 이전하려면 커뮤니티 서버를 1.7로 우선 업그레이드 하고 전문가 서버 1.7로 전환하는 지시 사항을 따라야합니다(1.7.x에서 마지막의 가장 작은 버전 숫자는 중요하지 않습니다).

## <a id="wiki-preparation"></a>준비 ##

### 자바 런타임 환경(JRE) 설치 ###

Java 7 이상이 필요합니다.

우분투/데비안:
```
sudo apt-get install openjdk-7-jre
```

CentOS/레드햇:
```
sudo yum install java-1.7.0-openjdk
```

*참고*: 3.1.12 버전부터 자바 1.7이 필요합니다. `java -version` 명령으로 자바 버전을 확인하십시오. 1.7이 아니면 [기본 자바 버전을 변경하십시오](./change_default_java.md).

### poppler-utils 설치 ###

pdf 파일에서 완전한 문구 검색을 처리하려면 poppler-utils가 필요합니다.

우분투/데비안:
```
sudo apt-get install poppler-utils
```

CentOS/레드햇:
```
sudo yum install poppler-utils
```

## <a id="wiki-do-migration"></a>이전 작업 진행 ##

`/data/haiwen/seafile-server-1.8.0`에 Seafile 커뮤니티판 서버 1.8.0을 가동중이라고 가정하겠습니다.


### 라이선스 취득 ###


Seafile 설치 최상위 디렉터리에 라이선스 파일을 복사하십시오, 최상위 디렉터리 예는 `/data/haiwen`입니다.


### <a id="wiki-download-and-uncompress"></a>Seafile 전문가판 서버 다운로드/압축 해제 ###


설치본의 최상위 디렉터리에 타르볼 압축을 해제해야합니다. 예를 들면 `/data/haiwen`입니다.

```
tar xf seafile-pro-server_1.8.0_x86-64.tar.gz
```

이제 다음 파일 및 디렉터리가 나타납니다:

```
haiwen
├── seafile-license.txt
├── seafile-pro-server-1.8.0/
├── seafile-server-1.8.0/
├── ccnet/
├── seafile-data/
├── seahub-data/
├── seahub.db
└── seahub_settings.py


```

-----------

커뮤니티판 서버와 전문가판 서버의 이름이 다르다는 점에 주목하십시오. 1.8.0 64비트 버전을 예로 들어보겠습니다:

- Seafile 커뮤니티판 서버 타르볼은 `seafile-server_1.8.0_x86-86.tar.gz`이며, 압축을 해제하면 `seafile-server-1.8.0` 폴더가 나옵니다
- Seafile 전문가판 서버 타르볼은 `seafile-pro-server_1.8.0_x86-86.tar.gz`이며, 압축을 해제하면 `seafile-pro-server-1.8.0` 폴더가 나옵니다

-----------


### 이전 작업 진행 ###

- Seafile 커뮤니티판 서버를 실행중이면 멈추십시오
```
cd haiwen/seafile-server-1.8.0
./seafile.sh stop
./seahub.sh stop
```
- 이전 스크립트를 실행하십시오
```
cd haiwen/seafile-pro-server-1.8.0/
./pro/pro.py setup --migrate
```

이전 스크립트에서는 다음 과정을 진행합니다:

- 준비 조건을 모두 만족했는지 확인합니다
- 필요한 추가 설정을 만듭니다
- 아바타 디렉터리를 업데이트합니다
- 추가 데이터베이스 테이블을 만듭니다  


이제 다음 파일 및 디렉터리가 나타납니다:

<blockquote>
haiwen<br/>
├── seafile-license.txt<br/>
├── seafile-pro-server-1.8.0/<br/>
├── seafile-server-1.8.0/<br/>
├── ccnet/<br/>
├── seafile-data/<br/>
├── seahub-data/<br/>
├── seahub.db<br/>
├── seahub_settings.py<br/>
└── <span style="color:green;font-weight:bold;">pro-data/</span><br/>
</blockquote>

### Seafile 전문가판 서버 시작 ###

```
cd haiwen/seafile-pro-server-1.8.0
./seafile.sh start
./seahub.sh start
```


## <a id="wiki-switch-back"></a>커뮤니티판 서버로 돌아가기 ##

- Seafile 전문가판 서버를 실행 중이면 멈추십시오
```
cd haiwen/seafile-pro-server-1.8.0/
./seafile.sh stop
./seahub.sh stop
```
- [부 버전(minor) 업그레이드](https://github.com/haiwen/seafile/wiki/Upgrading-Seafile-Server#minor-upgrade-like-from-150-to-151)와 같이 아바타 디렉터리 링크를 업데이트하십시오
```
cd haiwen/seafile-server-1.8.0/
./upgrade/minor-upgrade.sh
```
- Seafile 커뮤니티판 서버를 시작하십시오
```
cd haiwen/seafile-server-1.8.0/
./seafile.sh start
./seahub.sh start
```

