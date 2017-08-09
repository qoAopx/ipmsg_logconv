#!/bin/bash -eu

cd $(cd $(dirname $0);pwd)

# ログファイルのパス
readonly log_path=~/Documents/ipmsg_log.txt
readonly log_alt_path=~/Documents/ipmsg_alt_log.txt

# テキストファイルをSQLに変換
cat ${log_path} ${log_alt_path} | nkf -w | python convert_ipmsg_log.py > .insert.sql
# sqlite3.dbを作成
cat create_table.sql .insert.sql | sqlite3 ipmsg.log.db
# ファイルを開く
open ipmsg.log.db

exit 0
