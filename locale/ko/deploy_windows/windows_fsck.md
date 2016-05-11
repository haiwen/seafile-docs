### 손상 저장소에서 seaf-fsck 실행 ###

윈도우 환경에서 `seaf-fsck.exe`를 실행할 배치 파일이 현재로서는 없습니다.
`seaf-fsck.exe`를 직접 실행하려면 다음 과정을 따르십시오(Seafile 서버를 `X:\Seafile\`에 설치했다고 가정합니다):

1. 다음 *둘 중 한가지* 과정을 따라 명령 프롬프트를 여십시오
- **시작**, **실행**을 누르고 `cmd.exe`를 입력한 후 `cd /d X:\Seafile\seafile-server-5.x.x\seafile\bin` 명령을 입력하여 바이너리 폴더로 들어가십시오
  - 또는 파일 탐색기에서:
    * 바이너리가 있는 폴더(`X:\Seafile\seafile-server-5.x.x\seafile\bin`)로 들어가십시오
    * 빈 공간에 마우스 커서를 대고 Shift 키를 누른 상태에서 오른쪽 단추를 누른 후 단축 메뉴를 띄운 다음 **여기서 명령 창 열기**를 선택하십시오
2. 열어둔 명령 프롬프트 창에 다음 명령을 입력하십시오: `seaf-fsck.exe --repair -c Y:\seafile-user\ccnet -d Y:\seafile-user\seafile-data -F Y:\seafile-user\conf`
  - *seafile-user*는 Seafile 데이터를 저장한 폴더입니다
  - `seaf-fsck.exe`에서 올바른 디렉터리를 가리키는지 확인하십시오: *ccnet*, *seafile-data*, *conf* 폴더가 나타나야합니다
3. `seaf-fsck`가 동작해야합니다

*seaf-fsck*의 사용법과 옵션 문법을 더 자세히 알아보려면, [Seafile FSCK](../maintain/seafile_fsck.md) 장을 참고하십시오.

