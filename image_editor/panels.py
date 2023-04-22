import customtkinter as ctk

from settings import *

class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(fill='x', pady=4, ipady=8)

class SliderPanel(Panel):
    def __init__(self, parent, text, data_var, from_, to):
        super().__init__(parent=parent)

        # Layout
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure((0, 1), weight=1)

        ctk.CTkLabel(self, text=text).grid(row=0, column=0, sticky='w', padx=5, pady=5)

        self.label = ctk.CTkLabel(self, text=data_var.get())
        self.label.grid(row=0, column=1, sticky='e', padx=5, pady=5)
        
        ctk.CTkSlider(self, fg_color=SLIDER_BG, variable=data_var, from_=from_, to=to, command=self.update_label).grid(row=1, column=0, sticky='ew', columnspan=2, padx=5, pady=5)

    def update_label(self, value):
        self.label.configure(text=f'{round(value, 2)}')
