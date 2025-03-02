import customtkinter as ctk
from tkinter import font as tkFont
from home import home
from pages.page1 import page1
from pages.page2 import page2
from pages.page3 import page3

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.title("Aplikacja CTkinter")

        custom_font = tkFont.Font(family="ZCOOLKuaiLe-Regular.ttf", size=48)
        self.option_add("*Font", custom_font)

        self.frames = {}


        for Page in (home, page1, page2, page3):
            page_name = Page.__name__
            self.frames[page_name] = Page(self)

        self.show_frame("home")

    def show_frame(self, page_name):
        """Przełączanie stron"""
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
