import customtkinter as ctk
from tkinter import font as tkFont
from PIL import Image, ImageTk

class home(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color="black")

        self.parent = parent
        self.place(relwidth=1, relheight=1)

        custom_font = tkFont.Font(family="ZCOOLKuaiLe-Regular.ttf", size=48)
        self.option_add("*Font", custom_font)

        image = Image.open("assets/image.png")
        image = image.resize((800, 800))
        self.photo = ImageTk.PhotoImage(image)

        image2 = Image.open("assets/Logo.png")
        image2 = image2.resize((800,150))
        self.logo = ImageTk.PhotoImage(image2)




        # Tworzymy Canvas
        self.canvas = ctk.CTkCanvas(self, width=800, height=1000, bg="black", highlightthickness=0)
        self.canvas.create_image(0, 0, anchor="nw", image=self.logo)
        self.canvas.create_image(0, 100, anchor="nw", image=self.photo)
        self.canvas.pack()


        self.canvas.tag_bind(self.canvas.create_polygon(395, 215, 342, 370, 455, 375, outline="", fill="#33B3E6"),
                             "<Button-1>", lambda e: parent.show_frame("page1"))
        self.canvas.tag_bind(self.canvas.create_polygon(200, 780, 256, 630, 310, 780, outline="", fill="#33B3E6"),
                             "<Button-1>", lambda e: parent.show_frame("page2"))
        self.canvas.tag_bind(self.canvas.create_polygon(485, 782, 544, 628, 600, 783, outline="", fill="#33B3E6"),
                             "<Button-1>", lambda e: parent.show_frame("page3"))


        ctk.CTkLabel(self, text="Kliknij w trójkąt, aby przejść na podstronę.", text_color="#33B3E6", font=("Arial", 28)).pack(pady=0)

