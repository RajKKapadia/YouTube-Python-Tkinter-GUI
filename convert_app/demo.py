import tkinter as tk
import ttkbootstrap as ttk

def convert():
    miles = entry_int.get()
    km = miles * 1.61
    output_string.set(f'{km} KiloMeters')

window = ttk.Window()
window.title('Converter')

window_width = 300
window_height = 150
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()
x = int((display_width / 2) - (window_width / 2))
y = int((display_height / 2) - (window_height / 2))
window.geometry(f'{window_width}x{window_height}+{x}+{y}')

title_lable = ttk.Label(window, text='Convert Miles to KiloMeters', font='Calibri 12 bold')
title_lable.pack(pady=10)

input_frame = ttk.Frame(window)
entry_int = tk.IntVar()
entry = ttk.Entry(input_frame, textvariable=entry_int)
button = ttk.Button(input_frame, text='Convert', command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=25)

output_string = tk.StringVar()
output = ttk.Label(window, textvariable=output_string, font='Calibri 12')
output.pack(pady=5)

window.mainloop()
