from tkinter import *
from tkinter import ttk

class TopLevelCreate():
    def __init__(self, image=None, title=None):
        #Toplevel
        self.my_win = Toplevel()
        self.my_win.title(title)
        self.my_win.geometry('400x400+300+120')
        self.my_win.resizable(0,1)
        #Flame
        self.image_frame = ttk.Frame(self.my_win, padding=15)
        self.image_frame.pack()
        #画像を用意
        self.search_label = Label(self.image_frame, image=image)
        self.search_label.pack()
        #メッセージ
        self.info_label = Label(self.image_frame, text='★データが10件以上の場合はスクロールして下さい★', pady=5, padx=5)
        self.info_label.pack()
    def button_create(self):
        #ボタンを作成
        self.xlx_button = Button(self.image_frame, text='Excel出力')
        self.xlx_button.pack()