import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window()
window.title('Layouts')
window.geometry('400x600')

label1 = ttk.Label(window, text='First label', background='red')
label2 = ttk.Label(window, text='Label 2', background='blue')
label3 = ttk.Label(window, text='Last of the label', background='green')
button = ttk.Button(window, text='Button')

# label1.pack(fill='both')
# label2.pack(expand=True)
# label3.pack(expand=True, fill='both')
# button.pack()

# label1.pack(side='top', expand=True, fill='both', padx=10, pady=10)
# label2.pack(side='left', expand=True, fill='both')
# label3.pack(side='top', expand=True, fill='both')
# button.pack(side='top', expand=True, fill='both')

window.mainloop()