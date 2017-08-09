# Mac版 IPMsg Log Converter

- [Mac版のIPMsg](http://ishwt.net/software/ipmsg/)のログは標準だとエディタでみるだけです。
- そこでsqlite3.db形式に整形するスクリプトをつくりました。
- 各種sqliteビューアで見ることができます。

## 必要な環境(mac os)

- 下記環境で作成しました。
    1. nkf (2.1.4 brewでインストールできます)
    1. python3 (pyenvなどで)
    1. sqlite3 (3.20.0 brewでインストールできます)
    1. [DB Browser](http://sqlitebrowser.org/)などのsqlite3ビューア

## 使い方

- ダウンロード or git clone してプロジェクトをダウンロード
- convert_ipmsg_log.commandをダブルクリック
    - ipmsgのテキストログファイルをsqlite3.db形式に整形します。
    - 整形したsqlite3.dbファイルを開きます。（デフォルトアプリが起動します。）

- convert_ipmsg_log.commandのエイリアスを作るのがおすすめです。
