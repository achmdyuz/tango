#!/usr/bin/env python3
#-*- coding: utf-8 -*- # Setup characters encode to "UTF-8"

import sqlite3

# SQLiteデータベースに接続します (Connect to the SQLite database)
conn = sqlite3.connect('db/tango.db')
cursor = conn.cursor()

# 日記「にっき」ルテーブルが存在しない場合は作成します (Create the tango table if it doesn't exist)

cursor.execute ( ''' CREATE TABLE IF NOT EXISTS tango (
                     tango_id INTEGER PRIMARY KEY AUTOINCREMENT,
                     tango VARCHAR NOT NULL UNIQUE,
                     yomiKata VARCHAR,
                     imi VARCHAR,
                     nichiji VARCHAR
                     );''')

def tangoWoIrete():
    # ユーザーからの入力を受け取ります (Prompt the user for input)

    tango = input('単語「たんご」は？ ')
    yomiKata = input('読み方「よみかた」は？ ')
    imi = input('意味「いみ」は？ ')
    nichiji = input('日時「にちじ」は？ ')

        # エントリをデータベースに挿入します (Insert the entry into the database)
    cursor.execute("INSERT INTO tango (tango, yomiKata, imi, nichiji) VALUES (?, ?, ?, ?)", (tango, yomiKata, imi, nichiji))
    conn.commit()
    print("エントリが正常に作成されました！ (Entry created successfully!)")

def tangoWoYomu():
    # データベースからすべてのエントリを取得します (Retrieve all entries from the database)
    cursor.execute("SELECT * FROM tango")
    entries = cursor.fetchall()

    if entries:
        for tango in entries:
            tango_id, tango, yomiKata, imi, nichiji = tango
            print(f"ID: {tango_id}\n単語: {tango}\n読み方: {yomiKata}\n意味: {imi}\n日時: {nichiji}\n")

def tangoWoKousin():
    tango_id = input('更新「こうしん」するエントリのIDを入力「にゅうりょく」して下さい「ください」 ')
    tango = input('更新「こうしん」するエントリの単語「たんご」の内容「ないよう」を入力「にゅうりょく」して下さい「ください」 ')
    yomiKata = input('更新「こうしん」するエントリの読み方「よみかた」の内容「ないよう」を入力「にゅうりょく」して下さい「ください」 ')
    imi = input('更新「こうしん」するエントリの意味「いみ」の内容「ないよう」を入力「にゅうりょく」して下さい「ください」 ')
    nichiji = input('更新「こうしん」するエントリの日時「にちじ」の内容「ないよう」を入力「にゅうりょく」して下さい「ください」 ')

    cursor.execute("UPDATE tango SET tango = ?, yomiKata = ?, imi = ?, nichiji = ?  WHERE tango_id = ?", (tango, yomiKata, imi, nichiji, tango_id))
    conn.commit()
    print("エントリが正常に更新されました！ (Entry updated successfully!)")

def tangoWoSakujyosuru():
    tango_id = input("削除するエントリのIDを入力してください:  ")

    cursor.execute("DELETE FROM tango WHERE tango_id = ?", (tango_id,))
    conn.commit()
    print("エントリが正常に削除されました！ (Entry deleted successfully!)")

# 2023年08月01日「火曜日」13時16分
def entoriWoKazoeru():
    # データベース内「ない」のエントリの数「かず」を取得「しゅとく」する
    # Get the count of the database entries
    cursor.execute("SELECT COUNT(*) FROM tango")
    count =  cursor.fetchone()[0]
    print(f"データベース内「ない」のエントリ数「かず」：{count}件「けん」\n")
                
# メインのプログラムループ (Main program loop)

# 2023年08月01日「火曜日」13時25分
entoriWoKazoeru()

while True:
    print("1. エントリの作成「さくせい」 (Create entry)")
    print("2. エントリの表示「ひょうじ」 (Read entries)")
    print("3. エントリの更新「こうしん」 (Update entry)")
    print("4. エントリの削除「さくじょ」 (Delete entry)")
    print("5. 終了「しゅうりょう」 (Quit)")

    choice = input("選択肢「せんたくし」を入力「にゅうりょく」してください (Enter your choice): ")

    if choice == '1':
        tangoWoIrete()
    elif choice == '2':
        tangoWoYomu()
    elif choice == '3':
        tangoWoKousin()
    elif choice == '4':
        tangoWoSakujyosuru()
    elif choice == '5':
        break
    else:
        print("無効な「むこうな」選択肢「せんたくし」です。もう一度お試しください「おためしください」。 (Invalid choice. Please try again.)")

# データベース接続を閉じます (Close the database connection)
conn.close()

