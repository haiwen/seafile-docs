# Migrate From SQLite to MySQL

**NOTE**: The tutorial is only available for Seafile CE version.

Steps to migrate Seafile from SQLite to MySQL:

1. Stop Seafile and Seahub.

2. Download 3 files for mysql databases to `/data/haiwen`:

- Option 1 - for Seafile 6.3.x get them here: [ce_ccnet_db.sql](./fresh_db_schema_6.3.x/ce_ccnet_db.sql), [ce_seafile_db.sql](./fresh_db_schema_6.3.x/ce_seafile_db.sql), [ce_seahub_db.sql](./fresh_db_schema_6.3.x/ce_seahub_db.sql).
- Option 2 - for any version (more work): You need to generate all 3 files by yourself by setting up a seperate temporary fresh installation of seafile with mysql which must be the same version as your sqlite installation (you must follow all the way and even start seafile and seahub service of this temp installation so that all databases are set up). Than you have to run this command for each database to generate the files: "mysqldump --no-data -u seafile -p ccnet_db/seafile_db/seahub_db". Open all generated files and just to be on the safe side check that no insert scripts are inside (if they are delete them). Stop this temporary installation and drop all the dababases so that we have a clean mysql server which we can use for our migration: "DROP DATABASE ccnet_db/seafile_db/seahub_db;". 

3. If you went with Option 1 above you now need to set up mysql server (look into manual for mysql installation), if you went with Option 2 you can use that mysql server after you removed existing databases.

4. Download [sqlite_to_mysql.sh](./sqlite_to_mysql.sh) to the top directory of your Seafile installation path (for example, `/data/haiwen`) and run it, this script will produce three files (ccnet_db_data.sql, seafile_db_data.sql, seahub_db_data.sql):

 ```
chmod +x sqlite2mysql.sh
./sqlite2mysql.sh
```
This script will produce three files: `ccnet-db.sql`, `seafile-db.sql`, `seahub-db.sql`.

5. Now you should have the following directory layout.

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

6. Create 3 databases ccnet_db, seafile_db, seahub_db and seafile user.

 ```
mysql> create database ccnet_db character set = 'utf8';
mysql> create database seafile_db character set = 'utf8';
mysql> create database seahub_db character set = 'utf8';
```

7. Import ccnet data to MySql.

 ```
mysql> use ccnet_db;
mysql> source ccnet-db.sql;
```

8. Import seafile data to MySql.

 ```
mysql> use seafile_db;
mysql> source seafile-db.sql;
```

9. Import seahub data to MySql (this one takes the longest).

 ```
mysql> use seahub_db;
mysql> source seahub-db.sql;
```

10. Modify configure files.

Append following lines to [ccnet.conf](../config/ccnet-conf.md):

 ```
[Database]
ENGINE=mysql
HOST=127.0.0.1
USER=root
PASSWD=root
DB=ccnet_db
CONNECTION_CHARSET=utf8
```
Note: Use `127.0.0.1`, don't use `localhost`.

Replace the database section in `seafile.conf` with following lines:

 ```
[database]
type=mysql
host=127.0.0.1
user=root
password=root
db_name=seafile_db
connection_charset=utf8
```

Append following lines to `seahub_settings.py`:

 ```
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
```

11. Restart seafile and seahub
