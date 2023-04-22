import customtkinter as ctk

from panels import SliderPanel

class Menu(ctk.CTkTabview):
    def __init__(self, parent, rotation, zoom):
        super().__init__(master=parent)
        self.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        # Tabs
        self.add('Position')
        self.add('Colors')
        self.add('Effects')
        self.add('Export')

        # Widgets
        PositionFame(self.tab('Position'), rotation, zoom)
        ColorFame(self.tab('Colors'))
        EffectsFame(self.tab('Effects'))
        ExportFame(self.tab('Export'))

        
class PositionFame(ctk.CTkFrame):
    def __init__(self, parent, rotation, zoom):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')

        SliderPanel(self, 'Rotation', rotation, 0, 360)
        SliderPanel(self, 'Zoom', zoom, 0, 100)

class ColorFame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')

class EffectsFame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')

class ExportFame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')