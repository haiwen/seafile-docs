## Seafile 저장장치 백엔드 암호화

5.1.3 전문가판부터, 저장장치 백엔드 암호화 기능을 지원합니다. 이 기능을 활성화하면 저장장치 백엔드에 기록하기 전에 모든 Seafile 객체(commit, fs, block)을 AES 256 CBC 알고리즘으로 암호화합니다. 현재 지원하는 백엔드는 파일 시스템, Ceph, Swift, S3 입니다.

모든 객체는 동일한 전역 키 및 초기 벡터값 쌍으로 암호화 처리합니다. 키 및 초기화 벡터 쌍은 시스템 관리자가 생성하며 안전하게 보관합니다. 키 및 초기화 벡터 쌍을 잃으면 모든 데이터를 복원할 수 없습니다.

## 저장장치 백엔드 암호화 설정

### 키 및 초기 벡터값 생성

<INSTALL_PATH>/seafile-server-latest 디렉터리로 이동, `./seaf-gen-key.sh -h` 명령을 실행하십시오. 다음 사용법 정보를 출력합니다:

```
usage :
seaf-gen-key.sh
 -p <file path to write key iv, default ./seaf-key.txt>
```

기본적으로 키 및 초기 벡터값은 현재 디렉터리의 seaf-key.txt 파일로 저장합니다. '-p' 옵션으로 경로를 바꿀 수 있습니다.

### 새로 설치한 Seafile 서버 설정

다음 설정 내용을 seafile.conf에 추가하십시오:

```
[store_crypt]
key_path = <the key file path generated in previous section>
```

이제 암호화 기능이 동작해야합니다.

### 기존 Seafile 서버 이전

Seafile 서버에 이미 데이터가 있다면 기존 데이터를 이전하거나 암호화해야합니다. **데이터를 이전하기 전, Seafile 서버를 멈추십시오.**

#### 암호화 데이터 디렉터리 만들기

암호화 데이터를 둘 새 설정과 데이터 디렉터리를 만드십시오.

```
cd seafile-server-latest
cp -r conf conf-enc
mkdir seafile-data-enc
cp -r seafile-data/library-template seafile-data-enc
# If you use SQLite database
cp seafile-data/seafile.db seafile-data-enc/
```

#### 설정 파일 편집

S3/Swift/Ceph 백엔드를 설정했다면 <INSTALL_PATH>/conf-enc/seafile.conf를 편집하십시오. 암호화 데이터를 저장할 때 각기 다른 버킷/컨테이너/풀을 사용해야합니다.

이후 다음 설정을 <INSTALL_PATH>/conf-enc/seafile.conf에 추가하십시오

```
[store_crypt]
key_path = <the key file path generated in previous section>
```

#### 데이터 이전

<INSTALL_PATH>/seafile-server-latest 디렉터리로 이동하고, seaf-encrypt.sh 스크립트를 활용하여 데이터를 이전하십시오.

`./seaf-encrypt.sh -f ../conf-enc -e ../seafile-data-enc`를 실행하십시오,

```
Starting seaf-encrypt, please wait ...
[04/26/16 06:59:40] seaf-encrypt.c(444): Start to encrypt 57 block among 12 repo.
[04/26/16 06:59:40] seaf-encrypt.c(444): Start to encrypt 102 fs among 12 repo.
[04/26/16 06:59:41] seaf-encrypt.c(454): Success encrypt all fs.
[04/26/16 06:59:40] seaf-encrypt.c(444): Start to encrypt 66 commit among 12 repo.
[04/26/16 06:59:41] seaf-encrypt.c(454): Success encrypt all commit.
[04/26/16 06:59:41] seaf-encrypt.c(454): Success encrypt all block.
seaf-encrypt run done
Done.
```

seaf-encrypt.sh 실행 후 오류 메시지가 나타났다면 스크립트를 한번 더 실행하여 문제를 해결할 수 있습니다. 이미 이전한 객체는 다시 복사하지 않습니다.

#### 정리

<INSTALL_PATH>로 이동하여 다음 명령을 실행하십시오:

```
mv conf conf-bak
mv seafile-data seafile-data-bak
mv conf-enc conf
mv seafile-data-enc seafile-data
```

Seafile 서버를 다시 시작하십시오. 모든 부분이 잘 동작한다면 백업 디렉터리를 나중에 제거할 수 있습니다.

