from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msb
import sqlite3
from toplevel_create import TopLevelCreate
from export_xlsx import ExportXlsx
import datetime as dt

#--tkinter部品作成--
class NewWindow(TopLevelCreate):
    def __init__(self, image=None):
        super().__init__(title='全登録データ', image=image)
        #画像を用意
        #--sqlite3の操作--
        conn = sqlite3.connect('お誕生日リスト/birthday_list/birthday.db')
        c = conn.cursor()

        c.execute('SELECT * FROM birthday')
        r_tuple = tuple(c.fetchall())

        conn.close
        #----------------
        data_count = len(r_tuple)
        count_info = f'全データ：{data_count}件'
        c_info_label = Label(self.image_frame, text=count_info)
        c_info_label.pack(anchor=W)
        
        def click_event():
            #Excelに出力＆保存
            xlsx = ExportXlsx(r_tuple)
        # Excel出力ボタン
        self.xlsx_button = Button(self.image_frame, text='Excelに出力', command=click_event)
        self.xlsx_button.pack(anchor=W)
        #----データを表示----
        data_frame = ttk.Frame(self.my_win, relief=SOLID, padding=15)
        data_frame.pack()

        final_data = []
        for index, item in enumerate(r_tuple):
            final_data.append(
              ' [{}]  {}{}：{}年{}月{}日生まれ'.format(
                    index+1, r_tuple[index][0], r_tuple[index][1], r_tuple[index][2], r_tuple[index][3], r_tuple[index][4])
            )

        #データ表示用Listbox&Scrollbar
        v = StringVar(value=final_data)
        list_box = Listbox(data_frame, listvariable=v, width=30)
        list_box.grid(row=0, column=0)
        scroll = ttk.Scrollbar(data_frame, orient=VERTICAL, command=list_box.yview)
        list_box['yscrollcommand'] = scroll.set
        scroll.grid(row=0, column=1, sticky=(N, S))

