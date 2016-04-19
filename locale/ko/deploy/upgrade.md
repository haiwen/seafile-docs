# Seafile

## 업그레이드 설명서

이 페이지는 미리 컴파일한 Seafile 서버 꾸러미를 사용하는 사용자들이 보는 페이지입니다.

- [소스 코드에서 Seafile 서버를 빌드](../build_seafile/server.md)하려면, 이 페이지 대신 해당 페이지의 **Seafile 서버 업그레이드** 를 보십시오.
- After upgrading, you may need to clean [seahub cache](add_memcached.md) if it doesn't behave as expect.

**클러스터**를 가동중이면, [Seafile 클러스터](../deploy_pro/upgrade_a_cluster.md) 업그레이드를 읽으십시오.

## 주 버전 업그레이드 (2.x에서 3.y로 업그레이드 하는 방식)


2.1.0 버전을 사용중이고 3.1.0 버전으로 업그레이드 할 경우를 가정해보겠습니다. 우선 새 버전을 다운로드하고 압축을 해제하십시오. 디렉터리 배치는 다음과 같습니다:


<pre>
haiwen
   -- seafile-server-2.1.0
   -- seafile-server-3.1.0
   -- ccnet
   -- seafile-data
</pre>


이제 3.1.0 버전으로 업그레이드하십시오.

1. Shutdown Seafile server if it's running

   ```sh
   cd haiwen/seafile-server-2.1.0
   ./seahub.sh stop
   ./seafile.sh stop
   ```
2. Check the upgrade scripts in seafile-server-3.1.0 directory.

   ```sh
   cd haiwen/seafile-server-3.1.0
   ls upgrade/upgrade_*
   ```

   You will get a list of upgrade files:

   ```
   ...
   upgrade/upgrade_2.0_2.1.sh
   upgrade/upgrade_2.1_2.2.sh
   upgrade/upgrade_2.2_3.0.sh
   upgrade/upgrade_3.0_3.1.sh
   ```

3. Start from you current version, run the script one by one

   ```
   upgrade/upgrade_2.1_2.2.sh
   upgrade/upgrade_2.2_3.0.sh
   upgrade/upgrade_3.0_3.1.sh
   ```

4. Start the new server version as for any upgrade

   ```sh
   cd haiwen/seafile-server-3.1.0/
   ./seafile.sh start
   ./seahub.sh start # or "./seahub.sh start-fastcgi" if you're using fastcgi
   ```

## 부 버전 업그레이드(3.0.x에서 3.2.y로 업그레이드 하는 방식)

Suppose you are using version 3.0.0 and like to upgrade to version 3.2.2. First download and extract the new version. You should have a directory layout similar to this:


<pre>
haiwen
   -- seafile-server-3.0.0
   -- seafile-server-3.2.2
   -- ccnet
   -- seafile-data
</pre>


이제 3.2.2로 업그레이드하겠습니다.

1. Shutdown Seafile server if it's running

   ```sh
   cd haiwen/seafile-server-3.0.0
   ./seahub.sh stop
   ./seafile.sh stop
   ```
2. Check the upgrade scripts in seafile-server-3.2.2 directory.

   ```sh
   cd haiwen/seafile-server-3.2.2
   ls upgrade/upgrade_*
   ```

   You will get a list of upgrade files:

   ```
   ...
   upgrade/upgrade_2.2_3.0.sh
   upgrade/upgrade_3.0_3.1.sh
   upgrade/upgrade_3.1_3.2.sh
   ```

3. Start from you current version, run the script one by one

   ```
   upgrade/upgrade_3.0_3.1.sh
   upgrade/upgrade_3.1_3.2.sh
   ```

4. Start the new server version as for any upgrade

   ```sh
   cd haiwen/seafile-server-3.2.2/
   ./seafile.sh start
   ./seahub.sh start
   ```


## 관리 버전 업그레이드(3.1.0에서 3.1.2로 업그레이드 하는 방식)

관리 버전 업그레이드는 3.1.0에서 3.1.2로 업그레이드 하는 방식과 같습니다.


1. Stop the current server first as for any upgrade
2. For this type of upgrade, you only need to update the symbolic links (for avatar and a few other folders). We provide a script for you, just run it (For history reason, the script called `minor-upgrade.sh`):

   ```sh
   cd seafile-server-3.1.2
   upgrade/minor-upgrade.sh
   ```

3. Start the new server version as for any upgrade

4. If the new version works file, the old version can be removed

   ```sh
   rm -rf seafile-server-3.1.0
   ```

