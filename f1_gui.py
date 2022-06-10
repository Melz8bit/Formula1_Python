import tkinter as tk
import customtkinter
import formula1 as f1
from tkinter import ttk

BUTTON_WIDTH = 20
APP_FONT = ('Helvetica', 10)

class Formula1(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # UI Options
        paddings = {'padx': 10, 'pady': 10} 

        self.title('Formula 1 Tracker')
        h = 250
        w = 550
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int((ws/2) - (w/2))
        y = int((hs/2) - (h/2)) - 200
        self.geometry(f'{w}x{h}+{x}+{y}')
        self.resizable(0,0) # Disable the maximize button

        self.button = customtkinter.CTkButton(self, text="Create Toplevel", command=self.create_toplevel)
        self.button.grid(row=1, column=1, **paddings, sticky='w')

    def create_toplevel(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("400x200")

        # create label on CTkToplevel window
        label = customtkinter.CTkLabel(window, text="CTkToplevel window")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)


app = Formula1()
app.mainloop()