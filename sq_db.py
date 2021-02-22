from tkinter import *
from tkinter import messagebox as mb
import sqlite3
import datetime as dt

class DbInto():
    def __init__(self, name_data, birth_data):
        full_name = name_data
        birth_list = birth_data
        if '' in full_name:
            mb.showwarning('空欄エラー', '姓名に空欄があります')
        else:
            try:
                birth_list = [int(i) for i in birth_data]
            except ValueError:
                mb.showerror('空欄エラー', '生年月日を入力してください')
            else:
                try:
                    birthday = dt.date(birth_list[0], birth_list[1], birth_list[2])
                except ValueError:
                    mb.showwarning('入力値エラー', f'{birth_list[1]}月は{birth_list[2]}日までありません')
                else:
                    birthday_info = (
                      '{}{}さんの生年月日を{}年{}月{}日で登録します。'.format(full_name[0], full_name[1], birth_list[0], birth_list[1], birth_list[2])
                      )
                    res = mb.askquestion('結果', birthday_info)
                    if res == 'yes':
                        into_data = [
                          full_name[0], full_name[1], birth_list[0], birth_list[1], birth_list[2]
                        ]
                        self.data_into_db(data=into_data)
                        mb.showinfo('完了', '★登録しました★')

    def data_into_db(self, data):
        #Connectionオブジェクトを作る。
        conn = sqlite3.connect('birthday.db')
        c = conn.cursor()
        #----データの追加----
        c.execute("INSERT INTO birthday VALUES(?, ?, ?, ?, ?)", data)
        #----追加終了----
        #保存する。
        conn.commit()
        #データベースをクローズする。
        conn.close()

