#!/bin/sh
#
# This shell script uses sqlite3 commands to export data only(no schema) from seafile sqlite3 installation
#
# Setup:
#
#  1. Move this file to the top directory of your Seafile
#     installation path (e.g. /data/haiwen).
#  2. Run: ./sqlite_to_mysql.sh
#  3. Three files(ccnet_db_data.sql, seafile_db_data.sql, seahub_db_data.sql) are created.
#  4. Load these files to MySQL after you load schema
#     example: (mysql> source ccnet_db_data.sql)
#

#Function that generates INSERT statements for all data in given database
#Parameter1 = database_path
Sqlite2MysqlData () {
	echo "SET FOREIGN_KEY_CHECKS=0;"
	for TABLE in $(sqlite3 $1 .tables)
	do
		#get columns and insert ``, around every one
		COLS=$(sqlite3 $1 "PRAGMA table_info('${TABLE}');" | cut -d'|' -f2 | sed 's/^/`/'  | sed 's/$/`, /' )

		#remove comma from last one
		COLS_PURE=$(echo $COLS | sed 's/.$//')

		#generate insertstatemets (via echoMultipleCommands support by sqlite3), does not include column names
		#add one extra parameter for this to be working on Arch distro: "echo -e". Extra parameter breaks this script for other distros.
		echo ".mode insert\nselect * from '${TABLE}';" | sqlite3 $1 |

		#replace 3rd word with columns from above and also add ``:  `TableName`(`col1`, `col2`, `col3`, ...)
		sed "s/[^ ]*[^ ]/\`${TABLE}\` (${COLS_PURE})/3"
	done
	echo "SET FOREIGN_KEY_CHECKS=1;"
}

CCNET_DB='ccnet_db_data.sql'
SEAFILE_DB='seafile_db_data.sql'
SEAHUB_DB='seahub_db_data.sql'

########## ccnet

seafile_path=$(pwd)

if [ -d "${seafile_path}/ccnet" ]; then
    USER_MGR_DB=${seafile_path}/ccnet/PeerMgr/usermgr.db
    GRP_MGR_DB=${seafile_path}/ccnet/GroupMgr/groupmgr.db
else
    echo "${seafile_path}/ccnet does not exists."
    read -p "Please provide your ccnet folder path(e.g. /data/haiwen/ccnet): " ccnet_path
    if [ -d ${ccnet_path} ]; then
        USER_MGR_DB=$(dirname "${ccnet_path}")/PeerMgr/usermgr.db
        GRP_MGR_DB=$(dirname "${ccnet_path}")/GroupMgr/groupmgr.db
    else
        echo "${ccnet_path} does not exists, quit."
        exit 1
    fi
fi

rm -rf ${CCNET_DB}

echo "Start export ccnet data from user"
Sqlite2MysqlData ${USER_MGR_DB} > ${CCNET_DB}

echo "Start export ccnet data from group"
Sqlite2MysqlData ${GRP_MGR_DB} >> ${CCNET_DB}

echo "Done export ccnet data"

########## seafile

if [ -f "${seafile_path}/seafile-data/seafile.db" ]; then
    SEAFILE_SQLITE_DB=${seafile_path}/seafile-data/seafile.db
else
    echo "${seafile_path}/seafile-data/seafile.db does not exists."
    read -p "Please provide your seafile.db path(e.g. /data/haiwen/seafile-data/seafile.db): " seafile_db_path
    if [ -f ${seafile_db_path} ];then
        SEAFILE_SQLITE_DB=${seafile_db_path}
    else
        echo "${seafile_db_path} does not exists, quit."
        exit 1
    fi
fi

rm -rf ${SEAFILE_DB}

echo "Start export seafile data"
Sqlite2MysqlData ${SEAFILE_SQLITE_DB} > ${SEAFILE_DB}

echo "Done export seafile data"

########## seahub

if [ -f "${seafile_path}/seahub.db" ]; then
    SEAHUB_SQLITE_DB=${seafile_path}/seahub.db
else
    echo "${seafile_path}/seahub.db does not exists."
    read -p "Please prove your seahub.db path(e.g. /data/haiwen/seahub.db): " seahub_db_path
    if [ -f ${seahub_db_path} ]; then
        SEAHUB_SQLITE_DB=${seahub_db_path}
    else
        echo "${seahub_db_path} does not exists, quit."
        exit 1
    fi
fi

rm -rf ${SEAHUB_DB}

#delete existed data from `django_content_type`:
echo "DELETE FROM \`django_content_type\`;" > ${SEAHUB_DB}

#delete existed data from `django_migrations`:
echo "DELETE FROM \`django_migrations\`;" >> ${SEAHUB_DB}

echo "Start export seahub data"
Sqlite2MysqlData ${SEAHUB_SQLITE_DB} >> ${SEAHUB_DB}

echo "Done export seahub data"
