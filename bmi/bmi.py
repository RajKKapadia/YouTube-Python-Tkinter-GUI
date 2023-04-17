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
        self.update_bmi()

        # Tracing
        self.height_int.trace('w', self.update_bmi)
        self.weight_float.trace('w', self.update_bmi)

        # Widgets
        ResultText(self, self.bmi_string)
        WeightInput(self, self.weight_float)
        HeightInput(self, self.height_int)

        # Main loop
        self.mainloop()

    def update_bmi(self, *args):
        height = self.height_int.get() / 100
        weight = self.weight_float.get()
        bmi = weight / (height ** 2)
        self.bmi_string.set(round(bmi, 2))


class ResultText(ctk.CTkLabel):
    def __init__(self, parent, bmi_string):
        font = ctk.CTkFont(FONT, BIG_SIZE, weight='bold')
        super().__init__(master=parent, textvariable=bmi_string, font=font, text_color=WHITE)
        self.grid(row=0, column=0, rowspan=2, sticky='nsew')


class WeightInput(ctk.CTkFrame):
    def __init__(self, parent, weight_float):
        super().__init__(master=parent, fg_color=WHITE)
        self.weight_float = weight_float
        self.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)

        big_font = ctk.CTkFont(FONT, BIG_SIZE, weight='bold')
        small_font = ctk.CTkFont(FONT, SMALL_SIZE, weight='bold')

        # Layout
        self.rowconfigure(0, weight=1, uniform='b')
        self.columnconfigure(0, weight=2, uniform='b')
        self.columnconfigure(1, weight=1, uniform='b')
        self.columnconfigure(2, weight=4, uniform='b')
        self.columnconfigure(3, weight=1, uniform='b')
        self.columnconfigure(4, weight=2, uniform='b')

        self.output_string = ctk.DoubleVar(value=f'{self.weight_float.get()} KG')

        # Widgets
        ctk.CTkButton(self, command=lambda: self.update_weight(('minus', 'large')), text='-', text_color=BLACK, font=big_font, fg_color=LIGHT_GRAY,
                      hover_color=GRAY).grid(row=0, column=0, sticky='ns', padx=5, pady=5)
        ctk.CTkButton(self, text='-', command=lambda: self.update_weight(('minus', 'small')), text_color=BLACK, font=small_font,
                      fg_color=LIGHT_GRAY, hover_color=GRAY).grid(row=0, column=1)
        ctk.CTkLabel(self, textvariable=self.output_string, font=big_font,
                     text_color=BLACK).grid(row=0, column=2)
        ctk.CTkButton(self, text='+', command=lambda: self.update_weight(('plus', 'small')), text_color=BLACK, font=small_font,
                      fg_color=LIGHT_GRAY, hover_color=GRAY).grid(row=0, column=3)
        ctk.CTkButton(self, text='+', command=lambda: self.update_weight(('plus', 'large')), text_color=BLACK, font=big_font, fg_color=LIGHT_GRAY,
                      hover_color=GRAY).grid(row=0, column=4, sticky='nsew', padx=5, pady=5)

    def update_weight(self, info: None):
        amount = 1 if info[1] == 'large' else 0.1

        if info[0] == 'plus':
            self.weight_float.set(self.weight_float.get() + amount)
        else:
            self.weight_float.set(self.weight_float.get() - amount)

        self.output_string.set(f'{round(self.weight_float.get(), 2)} KG')


class HeightInput(ctk.CTkFrame):
    def __init__(self, parent, height_int):
        super().__init__(master=parent, fg_color=WHITE)
        self.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)

        small_font = ctk.CTkFont(FONT, SMALL_SIZE, weight='bold')

        self.output_string = ctk.StringVar(value=f'{height_int.get() / 100} M')

        # Widget
        ctk.CTkSlider(master=self, button_color=GREEN, button_hover_color=GRAY, progress_color=GREEN,
                      fg_color=LIGHT_GRAY, variable=height_int, from_=100, to=250, command=self.update_text).pack(side='left', fill='x', expand=True, padx=10, pady=10)
        ctk.CTkLabel(self, textvariable=self.output_string, text_color=BLACK,
                     font=small_font).pack(side='left', padx=10)

    def update_text(self, amount):
        self.output_string.set(f'{round(amount/100, 2)} M')


if __name__ == '__main__':
    App()
