import tkinter as tk
from tkinter import filedialog, Canvas
import customtkinter as ctk

from settings import *


class ImageImport(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk, import_image) -> None:
        super().__init__(master=parent)
        self.import_image = import_image
        ctk.CTkButton(self, text='Open image', border_width=1, command=self.open_dialog, width=80, height=50).place(
            relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.grid(row=0, column=0, columnspan=2, sticky='nsew')

    def open_dialog(self) -> None:
        path = filedialog.askopenfile().name
        self.import_image(path)


class ImageOutput(Canvas):
    def __init__(self, parent, resize_image):
        super().__init__(master=parent, background=BACKGROUND_COLOR,
                         bd=0, highlightthickness=0, relief='ridge')
        self.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)
        self.bind('<Configure>', resize_image)


class CloseOutput(ctk.CTkButton):
    def __init__(self, parent, close_edit):
        super().__init__(master=parent, text='X', height=30,
                         width=30, text_color=WHITE, fg_color='transparent', command=close_edit)
        self.place(relx=0.99, rely=0.01, anchor='ne')
