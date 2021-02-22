from tkinter import *
from tkinter import ttk

class ImageFile():
    def __init__(self):
        self.f = 'image_birthday/calender_woman.png'
        self.f2 = 'お誕生日リスト/birthday_list/image_birthday/sweets_cake_pavlova.png'
        self.f3 = 'お誕生日リスト/birthday_list/image_birthday/search_mushimegane2-2.png'
        
    def calender_img(self):
        self.calender_image = PhotoImage(file=self.f)
        return self.calender_image
        
    def cake_img(self):
        self.cake_image = PhotoImage(file=self.f2)
        return self.cake_image

    def search_img(self):
        self.search_image = PhotoImage(file=self.f3)
        return self.search_image

if __name__ == '__main__':
    ImageFile()
    