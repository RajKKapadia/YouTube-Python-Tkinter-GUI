import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window()
window.title('Layouts')
window.geometry('600x600')

# Widgets
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text='First label', background='red')
label2 = ttk.Label(top_frame, text='Label 2', background='blue')

label3 = ttk.Label(window, text='Another label', background='green')

bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text='Last of the label', background='orange')
button = ttk.Button(bottom_frame, text='Button')
button2 = ttk.Button(bottom_frame, text='Another Button')

right_frame = ttk.Frame(bottom_frame)
button3 = ttk.Button(right_frame, text='Button 1')
button4 = ttk.Button(right_frame, text='Button 2')
button5 = ttk.Button(right_frame, text='Button 3')

# Layouts
label1.pack(expand=True, fill='both')
label2.pack(expand=True, fill='both')
top_frame.pack(expand=True, fill='both')

label3.pack(expand=True)

button.pack(side='left', expand=True, fill='both')
label4.pack(side='left', expand=True, fill='both')
button2.pack(side='left', expand=True, fill='both')
bottom_frame.pack(expand=True, fill='both', padx=20, pady=20)

button3.pack(expand=True, fill='both')
button4.pack(expand=True, fill='both')
button5.pack(expand=True, fill='both')
right_frame.pack(side='left', expand=True, fill='both')

window.mainloop()