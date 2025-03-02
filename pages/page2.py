import customtkinter as ctk

class page2(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.place(relwidth=1, relheight=1)

        ctk.CTkLabel(self, text="To jest podstrona 2", font=("Arial", 20)).pack(pady=20)
        ctk.CTkButton(self, text="Powrót", command=lambda: parent.show_frame("home")).pack(pady=10)
