# Seafile GC

Seafile은 저장소 사용을 줄이는 저장장치 중복 방지 기술을 사용합니다. 파일 또는 라이브러리를 삭제하고 나서도 기반 데이터 블록을 바로 제거하지 않습니다. 결과적으로 사용하지 않는 여러 데이터 블록은 Seafile 서버에서 계속 늘어납니다.

사용하지 않은 블록이 차지하는 저장 공간을 확보하려면 "가비지 수집" 프로그램을 실행하여 서버에서 사용하지 않는 블록을 정리해야합니다.

GC 프로그램에서는 사용하지 않는 두가지 형식의 블록을 정리합니다:

1. 삭제한 라이브러리에 있던, 어떤 라이브러리에서도 참조하지 않는 블록
2. 일부 라이브러리의 기록 분량 제한 값을 설정하면, 이 라이브러리의 오래된 블록도 제거합니다.

**GC를 실행하기 전, 커뮤니티판을 사용한다면 서버에서 실행중인 Seafile 프로그램 가동을 멈춰야합니다. 전문가판에서는 3.1.11부터 온라인 GC 처리를 지원합니다. 전문가판을 사용한다면 MySQL또는 PostgreSQL을 데이터베이스로 사용할 때 Seafile 프로그램의 가동을 멈출 필요가 없습니다.** 왜냐면 GC를 실행하는 동안 Seafile에서 기록한 새 블록은 GC 프로그램에서 실수로 삭제할 수 있기 때문입니다.

## 버전 4.1.1 이상에서 GC 실행

커뮤니티판 4.1.1 및 전문가판 4.1.0에서 GC 프로그램 명령행 메시지 및 출력 내용을 개선했습니다.

### Dry-run 모드

가비지를 제거하지 않고 가비지를 얼마나 많이 수집할 수 있는지 보려면 dry-run 옵션을 사용하십시오:

```
seaf-gc.sh --dry-run [repo-id1] [repo-id2] ...
```

출력 내용은 다음과 같습니다:

```
[03/19/15 19:41:49] seafserv-gc.c(115): GC version 1 repo My Library(ffa57d93)
[03/19/15 19:41:49] gc-core.c(394): GC started. Total block number is 265.
[03/19/15 19:41:49] gc-core.c(75): GC index size is 1024 Byte.
[03/19/15 19:41:49] gc-core.c(408): Populating index.
[03/19/15 19:41:49] gc-core.c(262): Populating index for repo ffa57d93.
[03/19/15 19:41:49] gc-core.c(308): Traversed 5 commits, 265 blocks.
[03/19/15 19:41:49] gc-core.c(440): Scanning unused blocks.
[03/19/15 19:41:49] gc-core.c(472): GC finished. 265 blocks total, about 265 reachable blocks, 0 blocks can be removed.

[03/19/15 19:41:49] seafserv-gc.c(115): GC version 1 repo aa(f3d0a8d0)
[03/19/15 19:41:49] gc-core.c(394): GC started. Total block number is 5.
[03/19/15 19:41:49] gc-core.c(75): GC index size is 1024 Byte.
[03/19/15 19:41:49] gc-core.c(408): Populating index.
[03/19/15 19:41:49] gc-core.c(262): Populating index for repo f3d0a8d0.
[03/19/15 19:41:49] gc-core.c(308): Traversed 8 commits, 5 blocks.
[03/19/15 19:41:49] gc-core.c(264): Populating index for sub-repo 9217622a.
[03/19/15 19:41:49] gc-core.c(308): Traversed 4 commits, 4 blocks.
[03/19/15 19:41:49] gc-core.c(440): Scanning unused blocks.
[03/19/15 19:41:49] gc-core.c(472): GC finished. 5 blocks total, about 9 reachable blocks, 0 blocks can be removed.

[03/19/15 19:41:49] seafserv-gc.c(115): GC version 1 repo test2(e7d26d93)
[03/19/15 19:41:49] gc-core.c(394): GC started. Total block number is 507.
[03/19/15 19:41:49] gc-core.c(75): GC index size is 1024 Byte.
[03/19/15 19:41:49] gc-core.c(408): Populating index.
[03/19/15 19:41:49] gc-core.c(262): Populating index for repo e7d26d93.
[03/19/15 19:41:49] gc-core.c(308): Traversed 577 commits, 507 blocks.
[03/19/15 19:41:49] gc-core.c(440): Scanning unused blocks.
[03/19/15 19:41:49] gc-core.c(472): GC finished. 507 blocks total, about 507 reachable blocks, 0 blocks can be removed.

[03/19/15 19:41:50] seafserv-gc.c(124): === Repos deleted by users ===
[03/19/15 19:41:50] seafserv-gc.c(145): === GC is finished ===

[03/19/15 19:41:50] Following repos have blocks to be removed:
repo-id1
repo-id2
repo-id3
```

라이브러리 ID를 지정하면, 해당 라이브러리만 검사합니다. 그렇지 않으면 모든 라이브러리를 검사합니다.

출력 마지막 부분에 "repos have blocks to be removed" 섹션이 있습니다. 여기에는 가비지 블록이 있는 라이브러리 목록이 나타납니다. 그 다음 --dry-run 옵션을 빼고 GC를 실행할 때, GC 프로그램의 입력 인자로 출력에 나타난 라이브러리 ID를 넣을 수 있습니다.

### 쓸모 없는 파일 제거

실제로 가비지 블록을 제거하려면 --dry-run 옵션 없이 실행하십시오:

```
seaf-gc.sh [repo-id1] [repo-id2] ...
```

라이브러리 ID를 지정하면, 해당 라이브러리만 가비지 검사를 합니다.

이전에 설명한 바와 같이, 제거할 가비지 블록 형식은 두가지가 있습니다. 사용하지 않는 블록의 첫번째 형식을 제거하는 것만드로도(삭제한 라이브러리의 소유) 충분할 수도 있습니다. 이 경우 GC 프로그램에서는 오래된 기록 블록의 라이브러리 검사 동작으로 사용자를 귀찮게 하지 않습니다. "-r" 옵션은 다음 기능을 수행합니다:

```
seaf-gc.sh -r
```

**Seafile 버전 4.1.1 이후에서는, 사용자가 삭제한 라이브러리를 시스템에서 바로 제거하지 않습니다. 시스템 관리자 페이지의 "휴지통"에 이동합니다. 휴지동에서 완전히 지우기 전, 해당 블록은 가비지 수집 과정에서 정리하지 않습니다.**

### GC 다중 스레드 활용

전문가판 서버 5.1.0부터, GC 스레드 갯수를 지정할 수 있습니다. 기본적으로,

- 저장소 백엔드가 S3/Swift/Ceph라면, GC 동작에 스레드 10개를 시작합니다.
- 저장소 백엔드가 파일 시스템이라면, 스레드 하나만 시작합니다.

"-t" 옵션을 사용하여 스레드 갯수를 지정할 수 있습니다. "-t" 옵션은 다른 옵션과 함께 사용할 수 있습니다. 각 스레드는 라이브러리에 대해 GC 작업을 수행합니다. 예를 들어, 다음 명령은 모든 라이브러리에 대해 GC 작업을 수행하는데 스레드 20개를 사용합니다:

```
seaf-gc.sh -t 20
```

스레드는 동시 처리 작업이므로, 각 스레드 출력은 서로 섞일 수 있습니다. 라이브러리 ID는 각 줄 마다 나타납니다.

## 이전 버전(4.1.1 이전)에서 GC 실행

GC 프로그램을 실행하려면

    ./seaf-gc.sh run

데이터를 제거하기 전 상태를 검사한다면 --dry-run 옵션을 사용할 수 있습니다

    ./seaf-gc.sh dry-run

전체 블록 수와 제거 블록 갯수를 보여줍니다.

GC 실행 후 데이터 무결성을 검사한다면 [seaf-fsck](seafile_fsck.md)를 활용할 수 있습니다

