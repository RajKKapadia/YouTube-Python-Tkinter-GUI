import customtkinter as ctk

from settings import *

class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(fill='x', pady=4, ipady=8)

class SliderPanel(Panel):
    def __init__(self, parent, text):
        super().__init__(parent=parent)

        # Layout
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure((0, 1), weight=1)

        ctk.CTkLabel(self, text=text).grid(row=0, column=0, sticky='w', padx=5, pady=5)
        ctk.CTkLabel(self, text='0.0').grid(row=0, column=1, sticky='e', padx=5, pady=5)
        ctk.CTkSlider(self, fg_color=SLIDER_BG).grid(row=1, column=0, sticky='ew', columnspan=2, padx=5, pady=5)
