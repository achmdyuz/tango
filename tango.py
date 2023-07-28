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

    # if entries:
    #     for entry in entries:
    #         entry_id, entry_date, location, entry_text = entry
    #         print(f"ID: {entry_id}\n日付: {entry_date}\n場所: {location}\nエントリ: {entry_text}\n")
    # else:
    #     print("エントリが見つかりませんでした。 (No entries found.)")

    if entries:
        for tango in entries:
            tango_id, tango, yomiKata, imi, nichiji = tango
            print(f"ID: {tango_id}\n単語: {tango}\n読み方: {yomiKata}\n意味: {imi}\n日時: {nichiji}\n")

# def tangoWoKousin():
#     tango_id = input('更新「こうしん」するエントリのIDを入力「にゅうりょく」して下さい「ください」 ')
#     tango
#     yomiKata
#     imi
#     nichiji
#     entry_id = input("更新するエントリのIDを入力してください (Enter the ID of the entry to update): ")
#     entry_text = input("更新後の日記の内容を入力してください (Enter the updated journal entry): ")
#     location = input("更新後の場所を入力してください (Enter the updated location): ")

#     cursor.execute("UPDATE journal SET entry_text = ?, location = ? WHERE id = ?", (entry_text, location, entry_id))
#     conn.commit()
#     print("エントリが正常に更新されました！ (Entry updated successfully!)")

# def delete_entry():
#     entry_id = input("削除するエントリのIDを入力してください (Enter the ID of the entry to delete): ")

#     cursor.execute("DELETE FROM journal WHERE id = ?", (entry_id,))
#     conn.commit()
#     print("エントリが正常に削除されました！ (Entry deleted successfully!)")

# メインのプログラムループ (Main program loop)
while True:
    print("1. エントリの作成 (Create entry)")
    print("2. エントリの表示 (Read entries)")
    print("3. エントリの更新 (Update entry)")
    print("4. エントリの削除 (Delete entry)")
    print("5. 終了 (Quit)")

    choice = input("選択肢を入力してください (Enter your choice): ")

    if choice == '1':
        tangoWoIrete()
    elif choice == '2':
        tangoWoYomu()
    elif choice == '3':
        tangoWoKousin()
    elif choice == '4':
        delete_entry()
    elif choice == '5':
        break
    else:
        print("無効な選択肢です。もう一度お試しください。 (Invalid choice. Please try again.)")

# データベース接続を閉じます (Close the database connection)
conn.close()
