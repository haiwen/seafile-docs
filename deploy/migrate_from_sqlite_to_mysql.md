# Migrate From SQLite to MySQL

**NOTE**: The tutorial is only available for Seafile CE version.

First make sure the python module for MySQL is installed. On Ubuntu, use `sudo apt-get install python-mysqldb` to install it.

Steps to migrate Seafile from SQLite to MySQL:

1. Stop Seafile and Seahub.

1. Download [sqlite_to_mysql.sh](./sqlite_to_mysql.sh)  to the top directory of your Seafile installation path. For example, `/data/haiwen`.

1. Run `sqlite_to_mysql.sh`, this script will produce three files (ccnet_db_data.sql, seafile_db_data.sql, seahub_db_data.sql).

 ```
chmod +x sqlite_to_mysql.sh
./sqlite_to_mysql.sh
```

1. Download these three files to `/data/haiwen`, [ce_ccnet_db.sql](./ce_ccnet_db.sql), [ce_seafile_db.sql](./ce_seafile_db.sql), [mysql.sql](https://raw.githubusercontent.com/haiwen/seahub/master/sql/mysql.sql)(used for create tables in `seahub_db`).

1. Rename `mysql.sql` to `ce_seahub_db.sql`: `mv mysql.sql ce_seahub_db.sql`. Now you should have the following directory layout.

 ```sh
.
└── haiwen
|    ...
|    ...
|    ├── ce_ccnet_db.sql
|    ├── ce_seafile_db.sql
|    ├── ce_seahub_db.sql
|    ├── ccnet_db_data.sql
|    ├── seafile_db_data.sql
|    ├── seahub_db_data.sql
|    ...
|    ├── seafile-data
|    ├── seahub-data
|    ├── seahub.db
|    ...
|    ...
```

1. Create 3 databases ccnet_db, seafile_db, seahub_db and seafile user.

 ```
mysql> create database ccnet_db character set = 'utf8';
mysql> create database seafile_db character set = 'utf8';
mysql> create database seahub_db character set = 'utf8';
```

1. Import ccnet data to MySql.

 ```
mysql> use ccnet_db;
mysql> source ce_ccnet_db.sql;
mysql> source ccnet_db_data.sql;
```

1. Import seafile data to MySql.

 ```
mysql> use seafile_db;
mysql> source ce_seafile_db.sql;
mysql> source seafile_db_data.sql;
```

1. Import seahub data to MySql.

 ```
mysql> use seahub_db;
mysql> source ce_seahub_db.sql;
mysql> source seahub_db_data.sql;
```

1. Modify configure files.

  Append following lines to [ccnet.conf](../config/ccnet-conf.md):

        [Database]
        ENGINE=mysql
        HOST=127.0.0.1
        USER=root
        PASSWD=root
        DB=ccnet_db
        CONNECTION_CHARSET=utf8

    Note: Use `127.0.0.1`, don't use `localhost`.

    Replace the database section in `seafile.conf` with following lines:

        [database]
        type=mysql
        host=127.0.0.1
        user=root
        password=root
        db_name=seafile_db
        connection_charset=utf8

    Append following lines to `seahub_settings.py`:

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'USER' : 'root',
                'PASSWORD' : 'root',
                'NAME' : 'seahub_db',
                'HOST' : '127.0.0.1',
                # This is only needed for MySQL older than 5.5.5.
                # For MySQL newer than 5.5.5 INNODB is the default already.
                'OPTIONS': {
                    "init_command": "SET storage_engine=INNODB",
                }
            }
        }

1. Restart seafile and seahub

**NOTE**

User notifications will be cleared during migration due to the slight difference between MySQL and SQLite, if you only see the busy icon when click the notitfications button beside your avatar, please remove `user_notitfications` table manually by:

    use seahub_db;
    delete from notifications_usernotification;
