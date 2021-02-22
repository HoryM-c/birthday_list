from tkinter import *
from tkinter import ttk
from toplevel_create import TopLevelCreate
import sqlite3
from export_xlsx import ExportXlsx

#====検索機能モジュール====
class OpenData(TopLevelCreate):
    def __init__(self, conditions=None, image=None):
        super().__init__(title='指定検索データ', image=image)
        #条件データを受け取る
        full_conditions = conditions
        #条件の入っている列番号(インデックス)
        conditions_index = [index for index,item in enumerate(full_conditions) if item != '']
        #条件から空白を除外
        full_conditions = [elem for elem in full_conditions if elem != '']  
        #----sqlite3操作----
        conn = sqlite3.connect('お誕生日リスト/birthday_list/birthday.db')
        c = conn.cursor()

        c.execute("SELECT * FROM birthday")
        r_tuple = tuple(c.fetchall())

        conn.close
        #---------------------
        #全データから条件に一致するもののみリストに格納
        selection_data = []
        for item in r_tuple:
            select_result = True
            for key, value in enumerate(conditions_index):
                if item[value] != full_conditions[key]:
                    select_result = False
            if select_result == True:
                selection_data.append(item)
        
        data_count = len(selection_data)
        count_info = f'条件一致データ：{data_count}件'
        c_info_label = Label(self.image_frame, text=count_info)
        c_info_label.pack(anchor=W)

        def click_event():
            #Excelに出力＆保存
            xlsx = ExportXlsx(selection_data)
        # Excel出力ボタン
        self.xlsx_button = Button(self.image_frame, text='Excelに出力', command=click_event)
        self.xlsx_button.pack(anchor=W)
        #----データを表示----
        data_frame = ttk.Frame(self.my_win, relief=SOLID, padding=15)
        data_frame.pack()
        final_data = []
        for index, item in enumerate(selection_data):
            final_data.append(
              ' [{}]  {}{}：{}年{}月{}日生まれ'.format(
                    index+1, selection_data[index][0], selection_data[index][1], selection_data[index][2], selection_data[index][3], selection_data[index][4])
            )
        #データ表示用Listbox&Scrollbar
        v = StringVar(value=final_data)
        list_box = Listbox(data_frame, listvariable=v, width=30)
        list_box.grid(row=0, column=0)
        scroll = ttk.Scrollbar(data_frame, orient=VERTICAL, command=list_box.yview)
        list_box['yscrollcommand'] = scroll.set
        scroll.grid(row=0, column=1, sticky=(N, S))
