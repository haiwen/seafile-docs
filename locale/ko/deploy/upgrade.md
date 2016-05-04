# Seafile

## 업그레이드 설명서

이 페이지는 미리 컴파일한 Seafile 서버 꾸러미를 사용하는 사용자가 보는 페이지입니다.

- [소스 코드에서 Seafile 서버를 빌드](../build_seafile/server.md)하려면, 이 페이지 대신 해당 페이지의 **Seafile 서버 업그레이드** 를 보십시오.
- 업그레이드가 끝나면, 원하는 방식으로 [Seahub 캐시](add_memcached.md) 구성이 안되어 있다면 캐시를 정리하는 것이 좋습니다.

**클러스터**를 가동중이면, [Seafile 클러스터](../deploy_pro/upgrade_a_cluster.md) 업그레이드를 읽으십시오.

## 주 버전 업그레이드(2.x에서 3.y로 업그레이드 하는 방식)


2.1.0 버전을 사용중이고 3.1.0 버전으로 업그레이드 할 경우를 가정해보겠습니다. 우선 새 버전을 다운로드하고 압축을 해제하십시오. 디렉터리 배치는 다음과 같습니다:


<pre>
haiwen
   -- seafile-server-2.1.0
   -- seafile-server-3.1.0
   -- ccnet
   -- seafile-data
</pre>


이제 3.1.0 버전으로 업그레이드하십시오.

1. Seafile 서버가 동작중이라면 끄십시오

   ```sh
   cd haiwen/seafile-server-2.1.0
   ./seahub.sh stop
   ./seafile.sh stop
   ```
2. seafile-server-3.1.0 디렉터리의 업그레이드 스크립트를 확인하십시오.

   ```sh
   cd haiwen/seafile-server-3.1.0
   ls upgrade/upgrade_*
   ```

   다음 몇가지 업그레이드 파일을 볼 수 있습니다:

   ```
   ...
   upgrade/upgrade_2.0_2.1.sh
   upgrade/upgrade_2.1_2.2.sh
   upgrade/upgrade_2.2_3.0.sh
   upgrade/upgrade_3.0_3.1.sh
   ```

3. 현재 버전에서 시작하여, 하나하나씩 스크립트를 실행하십시오

   ```
   upgrade/upgrade_2.1_2.2.sh
   upgrade/upgrade_2.2_3.0.sh
   upgrade/upgrade_3.0_3.1.sh
   ```

4. 업그레이드한 새 서버 버전을 시작하십시오

   ```sh
   cd haiwen/seafile-server-3.1.0/
   ./seafile.sh start
   ./seahub.sh start # or "./seahub.sh start-fastcgi" if you're using fastcgi
   ```

## 부 버전 업그레이드(3.0.x에서 3.2.y로 업그레이드 하는 방식)

3.0.0 버전을 사용하고 있고, 3.2.2 버전으로 업그레이드 하려 한다고 가정하겠습니다. 우선 새 버전을 다운로드하고 압축을 풉니다. 디렉터리 배치는 다음과 같아야합니다:


<pre>
haiwen
   -- seafile-server-3.0.0
   -- seafile-server-3.2.2
   -- ccnet
   -- seafile-data
</pre>


이제 3.2.2로 업그레이드하겠습니다.

1. Seafile 서버가 동작중이라면 끄십시오

   ```sh
   cd haiwen/seafile-server-3.0.0
   ./seahub.sh stop
   ./seafile.sh stop
   ```
2. seafile-server-3.2.2 디렉터리의 업그레이드 스크립트를 확인하십시오.

   ```sh
   cd haiwen/seafile-server-3.2.2
   ls upgrade/upgrade_*
   ```

   다음 몇가지 업그레이드 파일을 볼 수 있습니다:

   ```
   ...
   upgrade/upgrade_2.2_3.0.sh
   upgrade/upgrade_3.0_3.1.sh
   upgrade/upgrade_3.1_3.2.sh
   ```

3. 현재 버전에서 시작하여, 하나하나씩 스크립트를 실행하십시오

   ```
   upgrade/upgrade_3.0_3.1.sh
   upgrade/upgrade_3.1_3.2.sh
   ```

4. 업그레이드한 새 서버 버전을 시작하십시오

   ```sh
   cd haiwen/seafile-server-3.2.2/
   ./seafile.sh start
   ./seahub.sh start
   ```


## 관리 버전 업그레이드(3.1.0에서 3.1.2로 업그레이드 하는 방식)

관리 버전 업그레이드는 3.1.0에서 3.1.2로 업그레이드 하는 방식과 같습니다.


1. 업그레이드를 위해 현재 서버를 우선 멈추십시오.
2. 이 방식의 업그레이드 과정에서는 심볼릭 링크만 업데이트하시면 됩니다(아바타 및 일부 기타 폴더용). 제공해드리는 스크립트를 그냥 실행만 하십시오(역사적인 이유로 `minor-upgrade.sh`라고 합니다):

   ```sh
   cd seafile-server-3.1.2
   upgrade/minor-upgrade.sh
   ```

3. 업그레이드한 새 서버 버전을 시작하십시오

4. 새 버전이 잘 동작한다면, 이전 버전을 제거할 수 있습니다

   ```sh
   rm -rf seafile-server-3.1.0
   ```

