# 서버 설정 일반 문제

#### Seafile을 초기화할 때 "Error when calling the metaclass bases" 오류 발생

Seafile은 파이썬 2.6.5 이상이 필요한 장고 1.5를 사용합니다. 파이썬 버전이 2.7인지 확인하십시오.

#### 다음 에러 메시지를 출력하며 Seahub.sh를 시작할 수 없음: "Could not import settings 'seahub.settings', libpython2.7.so.1.0: can not open shared object file"

아마도 우분투 14.04에서 나타나는 문제인 것 같습니다. Seafile 전문가판에서는 libpython2.6이 필요합니다. 다음 명령으로 설치하십시오:

```
sudo apt-get install libpython2.7
```

#### 온라인 파일 업로드/다운로드 실패

* ccnet.conf의 SERVICE_URL 설정과 seahub_settings.py의 FILE_SERVER_ROOT 설정을 확인하십시오
* Seafile 파일 서버의 포트를 방화벽에서 열어두었는지 확인하십시오.
* 크롬/파이어폭스 디버깅 모드를 활용하여 다운로드 단추를 눌렀을 때 어떤 링크가 나타나고 링크에 어떤 문제가 있는지 확인하십시오


#### Apache 로그 오류가 있습니다: "File does not exist: /var/www/seahub.fcgi"

httpd.conf 또는 apache2.conf에서 "FastCGIExternalServer /var/www/seahub.fcgi -host 127.0.0.1:8000" 설정을 사용했는지, "/var/www/seahub.fcgi" 부분을 적어두었는지 확인하십시오.

#### 아파치 로그에 다음 오류가 있음: "FastCGI: comm with server "/var/www/seahub.fcgi" aborted: idle timeout (30 sec)"

큰 규모의 라이브러리에서 파일 기록에 접근할 때 HTTP 500 오류가 발생하는 경우입니다.

해결책:

httpd.conf 또는 apache2.conf에서 "FastCGIExternalServer /var/www/seahub.fcgi -host 127.0.0.1:8000"을 "FastCGIExternalServer /var/www/seahub.fcgi -host 127.0.0.1:8000 -idle-timeout 60"으로 바꾸십시오

#### Apache/https로 동작하는 Seafile이 텍스트만 나타남(CSS 포매팅/그림 없음)

media 폴더(우분투에서 /etc/apache2/sites-enabled/000-default에 지정한 Alias 위치)에 부적절한 권한을 부여했기 때문일 수도 있습니다

해결책:

1. 비 루트 사용자로 설치 스크립트를 실행하십시오.
2. /media 폴더를 /var/www로 복사하고 /etc/apache2/sites-enabled/000-default 설정 파일의 Alias 위치를 편집하십시오

