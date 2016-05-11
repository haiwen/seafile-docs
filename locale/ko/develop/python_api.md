# 파이썬 API

<p><div class="toc">
<ul>
<li><a href="#Seafile Python API">Seafile 파이썬 API</a></li>
<li><a href="#Install Seafile Server">Seafile 서버 설치</a></li>
<li><a href="#Example: Copy Library">예제: 라이브러리 복사</a></li>
  <ul>
  <li><a href="#Set Environment Variable">환경 변수 설정</a></li>
  <li><a href="#Copy Library">라이브러리 복사</a></li>
  <li><a href="#List Of Seafile-API">Seafile-API 목록</a></li>
  </ul>
</ul>
</p>


#<a id="Seafile Python API"></a>Seafile 파이썬 API#

이 지침은 seafile-api 사용법을 보여드리며, **우분투**에서 "라이브러리 복사" 예로 보여드리겠습니다.

##<a id="Install Seafile Server"></a>Seafile 서버 설치##

우선, [Seafile 서버를 다운로드하고 설치](https://github.com/haiwen/seafile/wiki/Download-and-setup-seafile-server) 했는지 확인하십시오. 디렉터리 배치는 다음과 같습니다:

    # tree . -L 3
    .
    ├── ccnet
    │   ├── ccnet.conf
    │   ├── ......
    │......
    ├── seafile-server-3.0.3
    │   ├── seafile
    │   ├── seafile.sh
    │   ├── seahub
    │   ├── seahub.sh
    │   ├── setup-seafile.sh
    │   ├── upgrade
    │       ├── README
    │       ├── seaf_migrate_3.py
    │       ├── seaf_migrate_3.sh
    │       ├── ......
    │   ├── ......
    │......

##<a id="Example: Copy Library"></a>예제: 라이브러리 복사
이 예제에서 `seaf_migrate_3.sh`와  `seaf_migrate_3.py` 스크립트 파일을 사용하겠습니다. 위와 같이 **upgrade** 디렉터리에 복사하겠습니다.

###<a id="Set Environment Variable"></a>환경 변수 설정
Seafile-API를 사용하려면 환경 변수를 우선 설정해야합니다. `seaf_migrate_3.sh`가 하는 일입니다:

1. ccnet/seafile 설정 파일 경로를 가져와서 export 합니다
2. 파이썬 경로를 export 합니다
3. `seaf_migrate_3.py`를 호출합니다.

예제 코드
```sh
#!/bin/bash

#get path of ccnet.conf
SCRIPT=$(readlink -f "$0") # haiwen/seafile-server-3.0.3/upgrade/seaf_migrate_3.sh
UPGRADE_DIR=$(dirname "$SCRIPT") # haiwen/seafile-server-3.0.3/upgrade/
INSTALLPATH=$(dirname "$UPGRADE_DIR") # haiwen/seafile-server-3.0.3/
TOPDIR=$(dirname "${INSTALLPATH}") # haiwen/
default_ccnet_conf_dir=${TOPDIR}/ccnet

#get path of seafile.conf
function read_seafile_data_dir () {
    seafile_ini=${default_ccnet_conf_dir}/seafile.ini
    if [[ ! -f ${seafile_ini} ]]; then
        echo "${seafile_ini} not found. Now quit"
        exit 1
    fi
    seafile_data_dir=$(cat "${seafile_ini}")
    if [[ ! -d ${seafile_data_dir} ]]; then
        echo "Your seafile server data directory \"${seafile_data_dir}\" is invalid or doesn't exits."
        echo "Please check it first, or create this directory yourself."
        echo ""
        exit 1;
    fi

    export SEAFILE_CONF_DIR=$seafile_data_dir
}

export CCNET_CONF_DIR=${default_ccnet_conf_dir}
read_seafile_data_dir;

export PYTHONPATH=${INSTALLPATH}/seafile/lib/python2.6/site-packages:${INSTALLPATH}/seafile/lib64/python2.6/site-packages:${INSTALLPATH}/seafile/lib/python2.7/site-packages:${INSTALLPATH}/seahub/thirdpart:$PYTHONPATH
export PYTHONPATH=${INSTALLPATH}/seafile/lib/python2.7/site-packages:${INSTALLPATH}/seafile/lib64/python2.7/site-packages:$PYTHONPATH

function usage () {
    echo "Usage: `basename $0` <repo-id>"
    echo "exit."
    exit 1
}
if [ $# != 1 ]; then
    usage
fi

python seaf_migrate_3.py $1
```

> **참고:**
> Seahub 주소 표시줄 또는 [Seafile 웹 API](https://github.com/haiwen/seafile/wiki/Seafile-web-API#list-libraries)에서 `repo_id`를 찾을 수 있습니다

###<a id="Copy Library"></a>라이브러리 복사
다음, `seaf_migrate_3.py`으로 라이브러리를 복사하는 Seafile-API를 호출하겠습니다:

1. 입력에서 라이브러리 ID를 가져옵니다.
2. origin_repo 객체를 가져옵니다.
3. 새 라이브러리를 만들고, 이름, 설명, 소유자를 설정합니다.
4. 이전 라이브러리의 내용을 새 라이브러리에 복사합니다.

예제 코드
```python
#!/usr/bin/env python

import os
import stat
import sys
from seaserv import seafile_api

def count_files_recursive(repo_id, path='/'):
    num_files = 0
    for e in seafile_api.list_dir_by_path(repo_id, path):
        if stat.S_ISDIR(e.mode):
            num_files += count_files_recursive(repo_id,
                                               os.path.join(path, e.obj_name))
        else:
            num_files += 1
    return num_files

#Get library ID from input
origin_repo_id = sys.argv[1]

#Get origin_repo object
origin_repo = seafile_api.get_repo(origin_repo_id)
username = seafile_api.get_repo_owner(origin_repo_id)

#Create a new library, set name, desc and owner
new_repo_id = seafile_api.create_repo(name=origin_repo.name,
                                      desc=origin_repo.desc,
                                      username=username, passwd=None)

#Copy stuffs from old library to new library
dirents = seafile_api.list_dir_by_path(origin_repo_id, '/')
for e in dirents:
    print "copying: " + e.obj_name
    obj_name = e.obj_name
    seafile_api.copy_file(origin_repo_id, '/', obj_name, new_repo_id, '/',
                          obj_name, username, 0, 1)

print "*" * 60
print "OK, verifying..."
print "Origin library(%s): %d files. New Library(%s): %d files." % (
    origin_repo_id[:8], count_files_recursive(origin_repo_id),
    new_repo_id[:8], count_files_recursive(new_repo_id))
print "*" * 60
```

스크립트 파일 실행에 성공하면 다음 출력 내용이 나타나며, 물론 Seahub의 내 페이지에 새 라이브러리가 뜹니다.

    foo@foo:~/haiwen/seafile-server-3.0.3/upgrade$ ./seaf_migrate_test.sh c8bbb088-cbaf-411d-8bd8-9870763f0e5f
    Loading ccnet config from /home/foo/haiwen/ccnet
    Loading seafile config from /home/foo/haiwen/seafile-data
    copying: test.html
    copying: test-dir-2
    copying: test-dir
    copying: solar.html
    copying: examples.desktop
    ************************************************************
    OK, verifying...
    Origin library(c8bbb088): 10 files. New Library(4d6f4837): 10 files.
    ************************************************************

##<a id="List Of Seafile-API"></a>Seafile-API 목록
이 목록은 **seafile-server-3.0.3**을 기반으로 하며, 매개변수는 생략했습니다.

Seafile-API에 대한 세부 사항은 [api.py](https://github.com/haiwen/seafile/blob/master/python/seaserv/api.py)를 참고하십시오.

> - seafile_api.add_inner_pub_repo()
> - seafile_api.cancel_copy_task()
> - seafile_api.change_repo_passwd()
> - seafile_api.check_passwd()
> - seafile_api.check_permission()
> - seafile_api.check_quota()
> - seafile_api.check_repo_access_permission()
> - seafile_api.copy_file()
> - seafile_api.count_inner_pub_repos()
> - seafile_api.create_enc_repo()
> - seafile_api.create_repo()
> - seafile_api.create_virtual_repo()
> - seafile_api.del_file()
> - seafile_api.delete_repo_token()
> - seafile_api.delete_repo_tokens_by_peer_id()
> - seafile_api.diff_commits()
> - seafile_api.edit_repo()
> - seafile_api.generate_repo_token()
> - seafile_api.get_commit_list()
> - seafile_api.get_copy_task()
> - seafile_api.get_decrypt_key()
> - seafile_api.get_deleted()
> - seafile_api.get_dir_id_by_commit_and_path()
> - seafile_api.get_dir_id_by_path()
> - seafile_api.get_file_id_by_commit_and_path()
> - seafile_api.get_file_id_by_path()
> - seafile_api.get_file_revisions()
> - seafile_api.get_file_size()
> - seafile_api.get_files_last_modified()
> - seafile_api.get_group_repo_list()
> - seafile_api.get_group_repoids()
> - seafile_api.get_group_repos_by_owner()
> - seafile_api.get_fileserver_access_token()
> - seafile_api.get_inner_pub_repo_list()
> - seafile_api.get_orphan_repo_list()
> - seafile_api.get_owned_repo_list()
> - seafile_api.get_repo()
> - seafile_api.get_repo_list()
> - seafile_api.get_repo_owner()
> - seafile_api.get_repo_size()
> - seafile_api.get_share_in_repo_list()
> - seafile_api.get_share_out_repo_list()
> - seafile_api.get_shared_groups_by_repo()
> - seafile_api.get_user_quota()
> - seafile_api.get_user_self_usage()
> - seafile_api.get_user_share_usage()
> - seafile_api.get_virtual_repo()
> - seafile_api.get_virtual_repos_by_owner()
> - seafile_api.group_share_repo()
> - seafile_api.group_unshare_repo()
> - seafile_api.is_inner_pub_repo()
> - seafile_api.is_password_set()
> - seafile_api.is_repo_owner()
> - seafile_api.is_valid_filename()
> - seafile_api.list_dir_by_commit_and_path()
> - seafile_api.list_dir_by_dir_id()
> - seafile_api.list_dir_by_path()
> - seafile_api.list_file_by_file_id()
> - seafile_api.list_repo_tokens()
> - seafile_api.list_repo_tokens_by_email()
> - seafile_api.move_file()
> - seafile_api.post_dir()
> - seafile_api.post_empty_file()
> - seafile_api.post_file()
> - seafile_api.put_file()
> - seafile_api.query_fileserver_access_token()
> - seafile_api.remove_inner_pub_repo()
> - seafile_api.remove_repo()
> - seafile_api.remove_share()
> - seafile_api.rename_file()
> - seafile_api.revert_dir()
> - seafile_api.revert_file()
> - seafile_api.revert_repo()
> - seafile_api.set_group_repo_permission()
> - seafile_api.set_passwd()
> - seafile_api.set_repo_owner()
> - seafile_api.set_share_permission()
> - seafile_api.set_user_quota()
> - seafile_api.share_repo()
> - seafile_api.unset_passwd()

