# 도입부

Seafile은 파일 암호화 및 그룹 공유 기능을 지원하는 오픈소스 클라우드 저장소 시스템입니다. 

파일 모음은 라이브러리라고 하며, 각 라이브러리별로 동기화할 수 있습니다. 라이브러리는 사용자 지정 암호로 암호화 처리할 수 있습니다. 이 암호는 서버에 저장하지 않으므로, 서버 관리자는 파일의 내용을 볼 수 없습니다.

Seafile에서 사용자는 그룹을 만들고 파일을 동기화하며, 위키, 토론 페이지를 통해 모임에서 활용하는 문서로 협업을 쉽게 진행할 수 있습니다.

## 번역 (작업중)

[gettext](https://en.wikipedia.org/wiki/Gettext) 시스템에 익숙하지 않아도, 간단한 다음의 3단계로 시작할 수 있습니다.

예를 들어 **overview/** 폴더의 파일을 *스페인어*로 번역하려 한다면, 이에 대한 3단계 절차는:

1. **po/overview.pot**를  **po/overview.es.po**로 복사하십시오.
1. **po/overview.es.po** 메시지를 스페인어로 번역하십시오.
1. **po/overview.es.po** 파일 병합을 위해 보내주십시오. 이미 po 파일이 있다면 pull 요청하셔도 됩니다.


POT 및 PO 파일에 익숙하다면, **po/** 폴더의 pot를 골라 사용하시면 됩니다.

## 라이선스

Seafile 서버는 GPLv2에 따라 공개합니다.

Seahub와 같은 Seafile 서버 웹 엔드는 Apache 라이선스에 따라 배포합니다.

## 설명서 정보

이 설명서의 "소스 코드"는 github에서 제공합니다: https://github.com/haiwen/seafile-docs

## 연락 정보

* 트위터: @seafile https://twitter.com/seafile
* 포럼: https://forum.seafile-server.org

## 추가 문서

* [Seafile 일반 정보 위키](https://seacloud.cc/group/3/wiki/)

