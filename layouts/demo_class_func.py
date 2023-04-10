import tkinter as tk
import ttkbootstrap as ttk

class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text):
        super().__init__(parent)

        self.rowconfigure(0, weight=1, uniform='a')
        self.columnconfigure((0, 1, 2), weight=1, uniform='a')

        ttk.Label(self, text=label_text).grid(row=0, column=0, sticky='nsew')
        ttk.Button(self, text=button_text).grid(row=0, column=1, sticky='nsew')

        self.create_box('excercise').grid(row=0, column=2, sticky='nsew')

        self.pack(expand=True, fill='both', padx=10, pady=10)

    def create_box(self, text):
        frame = ttk.Frame(self)
        ttk.Entry(frame).pack(expand=True, fill='both',padx=5, pady=5)
        ttk.Button(frame, text=text).pack(expand=True, fill='both',padx=5, pady=5)
        return frame


window = ttk.Window()
window.title('Layouts')
window.geometry('600x600')

Segment(window, 'label', 'button')
Segment(window, 'test', 'click')
Segment(window, 'hello', 'test')

window.mainloop()
