import sys
import re
import json

# ヘッダ部判定文字列
main_line = '====================================='
sub_line = '-------------------------------------'

# ヘッダ部の内容取得正規表現
## From/to、送信者名、グループ
re_fromto = re.compile('^ (From|To): ([^\(]*) \(([^\)]*)\)')
## 発信時刻
re_date = re.compile(
    '^  at (\d{4})[\D]*(\d{1,2})[\D]*(\d{1,2})[\D]*(\d{1,2}:\d{1,2}:\d{1,2})')


# 変数初期化
f_fromto = ''
f_name = ''
f_group = ''
f_datetime = ''
f_msg = ''

buf = ''
i = 0

lines = sys.stdin.readlines()
while i < len(lines):
    # メインの区切り
    l = lines[i].rstrip()
    if l == main_line:
        # サブの区切り
        s = lines[i + 3].rstrip()
        if s == sub_line:
            ft = lines[i + 1].rstrip()  # From/To
            dt = lines[i + 2].rstrip()  # at 送信時刻
            if re_fromto.match(ft) and re_date.match(dt):
                # 最初にメッセージを吐き出す。
                if f_msg != '':
                    db_msg = f_msg.rstrip().replace("'", "''")
                    buf = buf + ("INSERT INTO ipmsg_log(datetime, fromto, name, groupname, msg) VALUES('{0}','{1}','{2}','{3}','{4}');\n".format(
                        f_datetime, f_fromto, f_name, f_group, db_msg))
                    f_msg = ''

                # 記録
                (f_fromto, f_name, f_group) = re_fromto.findall(ft)[0]
                (yyyy, md, dd, dtime) = re_date.findall(dt)[0]
                f_datetime = '{0:04d}-{1:02d}-{2:02d} {3:s}'.format(
                    int(yyyy), int(md), int(dd), dtime)
                i = i + 4

    f_msg = f_msg + lines[i]
    i = i + 1

# 最後にバッファに吐き出す
db_msg = f_msg.rstrip().replace("'", "''")
buf = buf + ("INSERT INTO ipmsg_log(datetime, fromto, name, groupname, msg) VALUES('{0}','{1}','{2}','{3}','{4}');\n".format(
    f_datetime, f_fromto, f_name, f_group, db_msg))

print('BEGIN TRANSACTION;')
print(buf)
print('COMMIT;')
