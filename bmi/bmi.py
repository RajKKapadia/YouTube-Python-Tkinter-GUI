import tkinter as tk
import customtkinter as ctk

from settings import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=GREEN)

        # Window setup
        self.title('BMI App')
        self.geometry(f'{WIDTH}x{HEIGHT}')
        self.resizable(False, False)

        # Layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')

        # Data
        self.height_int = ctk.IntVar(value=170)
        self.weight_float = ctk.DoubleVar(value=65)
        self.bmi_string = ctk.StringVar()
        

        # Widgets
        ResultText(self)
        WeightInput(self)
        HeightInput(self)

        # Main loop
        self.mainloop()


class ResultText(ctk.CTkLabel):
    def __init__(self, parent):
        font = ctk.CTkFont(FONT, BIG_SIZE, weight='bold')
        super().__init__(master=parent, text=22.5, font=font, text_color=WHITE)
        self.grid(row=0, column=0, rowspan=2, sticky='nsew')


class WeightInput(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=WHITE)
        self.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)

        big_font = ctk.CTkFont(FONT, BIG_SIZE, weight='bold')
        small_font = ctk.CTkFont(FONT, SMALL_SIZE, weight='bold')

        # Layout
        self.rowconfigure(0, weight=1, uniform='b')
        self.columnconfigure(0, weight=2, uniform='b')
        self.columnconfigure(1, weight=1, uniform='b')
        self.columnconfigure(2, weight=3, uniform='b')
        self.columnconfigure(3, weight=1, uniform='b')
        self.columnconfigure(4, weight=2, uniform='b')

        # Widgets
        ctk.CTkButton(self, text='-', text_color=BLACK, font=big_font, fg_color=LIGHT_GRAY, hover_color=GRAY).grid(row=0, column=0, sticky='ns', padx=5, pady=5)
        ctk.CTkButton(self, text='-', text_color=BLACK, font=small_font, fg_color=LIGHT_GRAY, hover_color=GRAY).grid(row=0, column=1)
        ctk.CTkLabel(self, text='70 KG', font=big_font, text_color=BLACK).grid(row=0, column=2)
        ctk.CTkButton(self, text='+', text_color=BLACK, font=small_font, fg_color=LIGHT_GRAY, hover_color=GRAY).grid(row=0, column=3)
        ctk.CTkButton(self, text='+', text_color=BLACK, font=big_font, fg_color=LIGHT_GRAY, hover_color=GRAY).grid(row=0, column=4, sticky='nsew', padx=5, pady=5)


class HeightInput(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=WHITE)
        self.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)

        small_font = ctk.CTkFont(FONT, SMALL_SIZE, weight='bold')

        # Widget
        ctk.CTkSlider(master=self, button_color=GREEN, button_hover_color=GRAY, progress_color=GREEN, fg_color=LIGHT_GRAY).pack(side='left', fill='x', expand=True, padx=10, pady=10)
        ctk.CTkLabel(self, text='1.5 M', text_color=BLACK, font=small_font).pack(side='left', padx=10)


if __name__ == '__main__':
    App()
