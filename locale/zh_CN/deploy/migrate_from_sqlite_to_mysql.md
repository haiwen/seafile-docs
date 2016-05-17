# 从 SQLite 迁移到 MySQL

首先请确认 MySQL 的 Python 模块已经安装. Ubuntu 下，安装命令为 `apt-get install python-mysqldb`.

请按以下步骤操作:

0. 停止 Seafile 和 Seahub

1. 下载 [sqlite2mysql.sh](https://raw.github.com/haiwen/seafile/master/scripts/sqlite2mysql.sh) 和 [sqlite2mysql.py](https://raw.github.com/haiwen/seafile/master/scripts/sqlite2mysql.py) 到 Seafile 的安装根目录（/data/haiwen）里.

2. 运行 sqlite2mysql.sh 脚本
```
  chmod +x sqlite2mysql.sh
  ./sqlite2mysql.sh
```
这个脚本将生成三个文件：`ccnet-db.sql`, `seafile-db.sql`, `seahub-db.sql`。

3. 新建3个数据库，分别命名为 `ccnet-db`, `seafile-db`, `seahub-db`.
```
  create database `ccnet-db` character set = 'utf8';
  create database `seafile-db` character set = 'utf8';
  create database `seahub-db` character set = 'utf8';
```

4. Loads the sql files to your MySQL databases. For example:
```
  mysql> use `ccnet-db`
  mysql> source ccnet-db.sql
  mysql> use `seafile-db`
  mysql> source seafile-db.sql
  mysql> use `seahub-db`
  mysql> source seahub-db.sql
```

5. 更改配置

  在 [conf/ccnet.conf](../config/ccnet-conf.md) 中增加以下语句:

        [Database]
        ENGINE=mysql
        HOST=127.0.0.1
        USER=root
        PASSWD=root
        DB=ccnet-db
        CONNECTION_CHARSET=utf8

    注意: 使用 `127.0.0.1`, 不要使用 `localhost`.

    将 `seafile.conf` 中的数据库配置信息更改文以下语句:

        [database]
        type=mysql
        host=127.0.0.1
        user=root
        password=root
        db_name=seafile-db
        CONNECTION_CHARSET=utf8

    在 `seahub_settings.py` 中增加以下语句:

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'USER' : 'root',
                'PASSWORD' : 'root',
                'NAME' : 'seahub-db',
                'HOST' : '127.0.0.1',
                'OPTIONS': {
                    "init_command": "SET storage_engine=INNODB",
                }
            }
        }

6. 重启 Seafile 和 Seahub


**NOTE**

User notifications will be cleared during migration due to the slight difference between MySQL and SQLite, if you only see the busy icon when click the notitfications button beside your avatar, please remove `user_notitfications` table manually by:

    use seahub-db
    delete from notifications_usernotification;

