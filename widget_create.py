from tkinter import *
from tkinter import ttk
from image_file import ImageFile
from all_data import NewWindow
from select_db import OpenData
from sq_db import DbInto

class WidgetCreate(ImageFile):
    def __init__(self, belong=None, style=None):
        super().__init__()
        #Frame
        self.sub_frame = ttk.Frame(belong, style=style)
        self.sub_frame.grid(column=1, row=0, ipadx=15, ipady=10)
        self.name_frame = Frame(self.sub_frame)
        self.name_frame.pack(padx=10, pady=20, anchor=W)
        self.birth_frame = Frame(self.sub_frame)
        self.birth_frame.pack(padx=5, anchor=W)
        self.birth_frames = [
          Frame(self.birth_frame) for i in range(3)
        ]
        for item in self.birth_frames:
            item.pack(side=LEFT, padx=5)
        self.i_button_frame = Frame(belong)
        self.i_button_frame.grid(column=0, columnspan=2, row=3)
        self.r_button_frame = Frame(self.sub_frame)
        self.r_button_frame.pack()
        #Label
        self.info_label = Label(self.name_frame, text='★必要事項を入力してください★\n')
        self.info_label.pack(padx=5, anchor=W)
        self.name_lists = ['姓', '名']
        self.date_text = ['西暦', '月', '日']
        self.name_labels = [
          Label(self.name_frame, text=label_item) for label_item in self.name_lists
        ]
        #date_labelをそれぞれのFrameに入れて作成
        self.date_labels = [
          Label(frame_item, text=label_item) for frame_item, label_item in zip(self.birth_frames, self.date_text)
        ]
        #Entryを作成
        self.family_var = StringVar()
        self.first_var = StringVar()
        self.familyname_entry = ttk.Entry(self.name_frame, textvariable=self.family_var, width=10)
        self.firstname_entry = ttk.Entry(self.name_frame, textvariable=self.first_var, width=10)
        self.entry_list = [self.familyname_entry, self.firstname_entry]
        #姓名LabelとEntryをpack
        
        for label, entry in zip(self.name_labels, self.entry_list):
            label.pack(anchor = W, side = LEFT)
            entry.pack(anchor = W, side = LEFT)
        #Comboboxを作成
        self.date_list = [
          [value for value in range(1920, 2021)],
          [value for value in range(1, 13)],
          [value for value in range(1, 32)]
        ]
        self.combo_list = [
          ttk.Combobox(self.birth_frames[i], state='readonly', values=self.date_list[i], width = 5, justify = RIGHT) for i in range(3)
        ]
        #生年月日LabelとComboboxをpack
        for label, combo in zip(self.date_labels, self.combo_list):
            label.pack(anchor = W, side = LEFT)
            combo.pack(anchor = W, side = LEFT)
        
    #----ボタン関連の作成----
    def button_create(self, master, my_style=None):
        #登録ボタンイベント
        def i_button_click():
            #入力値を取得
            full_name = [name.get() for name in self.entry_list]
            birth_list = [var.get() for var in self.combo_list]
            result = DbInto(name_data=full_name, birth_data=birth_list)
            #入力内容のリセット
            for item in self.entry_list:
                item.delete(0,END)
            for item in self.combo_list:
                item.selection_clear()
                item.set('')

        #検索ボタンイベント
        def c_button_click():
            #画像を用意
            self.search_image = ImageFile()
            self.s_image = self.search_image.search_img()
            #入力値を取得
            full_name = [name.get() for name in self.entry_list]
            birth_list = [var.get() for var in self.combo_list]
            #生年月日条件(birth_list)をint型に変換
            for index, item in enumerate(birth_list):
                if item != '':
                    birth_list[index] = int(item)
            sum_item = full_name + birth_list
            #条件設定の有無で分岐
            if any(sum_item) is False:
                all_search = NewWindow(image=self.s_image)
            else:
                condition_data = OpenData(conditions=sum_item, image=self.s_image)
        #名前リセット
        def name_reset():
            for item in self.entry_list:
                item.delete(0,END)
        #生年月日リセット
        def date_reset():
            for item in self.combo_list:
                item.selection_clear()
                item.set('')
        #ボタンを作成
        self.i_button = ttk.Button(self.i_button_frame, text='新規登録', width=9, command=i_button_click)
        self.i_button.pack(side=LEFT)
        self.c_button = ttk.Button(self.i_button_frame, text='データ検索', width=9, command=c_button_click)
        self.c_button.pack(side=LEFT, padx=20)
        self.d_button = ttk.Button(self.i_button_frame, text='× キャンセル ×', style=my_style, width=11, command=master.destroy)
        self.d_button.pack(side=LEFT, padx=10)
        #余白調整のLabel
        self.space_label = Label(self.r_button_frame, text='')
        self.space_label.pack()
        #リセットボタン
        self.nr_button = ttk.Button(self.r_button_frame, text='Name Reset', command=name_reset)
        self.nr_button.pack(side=LEFT)
        self.dr_button = ttk.Button(self.r_button_frame, text='Date Reset', command=date_reset)
        self.dr_button.pack(padx=15, side=LEFT)

