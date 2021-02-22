import subprocess
import sqlite3
import pandas as pd
import os
import datetime as dt
from tkinter import messagebox as msb

class ExportXlsx():
    def __init__(self, data):
        self.df = pd.DataFrame(data,columns=['姓', '名', '西暦', '月', '日'])
        #Excelファイル名設定
        name = str(dt.datetime.today())
        name = name[:19]
        book_name = name.translate(str.maketrans(':.', '__')) + '.xlsx'
        save_info = ('ファイル名【{}】で保存します。'.format(book_name))
        info_msb = msb.showinfo('info', save_info)
        #保存先の設定
        pwd = os.path.dirname(__file__)
        dir_name = 'ExportData'
        book_path = os.path.join(pwd, dir_name, book_name)
        with pd.ExcelWriter(book_path) as writer:
            self.df.to_excel(writer, index=False)

        subprocess.run(['open', book_path])
