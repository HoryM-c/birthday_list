from tkinter import *
from tkinter import ttk
from image_file import ImageFile
from widget_create import WidgetCreate

class Application(ImageFile):
    def __init__(self, master, style=None):
        super().__init__()                
        #TOP画面を作成
        master.title('誕生日リスト')
        master.geometry('610x300+250+100')
        self.main_frame = Frame(master)
        self.main_frame.pack(pady=10)
        #画像
        self.image_file = ImageFile()
        self.cake_image = self.image_file.cake_img()
        self.image_label = Label(self.main_frame, image=self.cake_image)
        self.image_label.grid(column=0, rowspan=2, row=0, padx=20, pady=15, ipady=5)
        #Widgetの作成
        my_widget = WidgetCreate(belong=self.main_frame, style='MyWidgets4.TFrame')
        my_widget.button_create(master=root, my_style='ButtonStyle.TButton')

if __name__ == '__main__':
    root = Tk()
    s = ttk.Style()
    s.configure('MyWidgets.TFrame',background='systemTransparent', relief=FLAT)
    s.configure('MyWidgets4.TFrame',background='systemTransparent', relief=SUNKEN)
    s.configure('MyWidgets2.TLabel', background='systemTransparent', relief=FLAT)
    s.configure('ButtonStyle.TButton', foreground='#FF0000')

    app = Application(master=root, style='MyWidgets4.TFrame')

    root.mainloop()

