import customtkinter as ctk

from panels import SliderPanel, SegmentedPanel, SwitchPanel, DropDownPanel
from settings import *

class Menu(ctk.CTkTabview):
    def __init__(self, parent, pos_vars, color_vars, effect_vars):
        super().__init__(master=parent)
        self.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        # Tabs
        self.add('Position')
        self.add('Colors')
        self.add('Effects')
        self.add('Export')

        # Widgets
        PositionFame(self.tab('Position'), pos_vars)
        ColorFame(self.tab('Colors'), color_vars)
        EffectsFame(self.tab('Effects'), effect_vars)
        ExportFame(self.tab('Export'))

        
class PositionFame(ctk.CTkFrame):
    def __init__(self, parent, pos_vars):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')

        SliderPanel(self, 'Rotation', pos_vars['rotate'], 0, 360)
        SliderPanel(self, 'Zoom', pos_vars['zoom'], 0, 100)
        SegmentedPanel(self, 'Invert', pos_vars['flip'], FLIP_OPTIONS)

class ColorFame(ctk.CTkFrame):
    def __init__(self, parent, color_vars):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')

        SwitchPanel(self, (color_vars['grayscale'], 'B/W'), (color_vars['invert'], 'Invert'))
        SliderPanel(self, 'Brightness', color_vars['brightness'], 0 ,5)
        SliderPanel(self, 'Vibrance', color_vars['vibrance'], 0 ,5)

class EffectsFame(ctk.CTkFrame):
    def __init__(self, parent, effect_vars):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')

        DropDownPanel(self, effect_vars['effects'], EFFECT_OPTIONS)
        SliderPanel(self, 'Blue', effect_vars['blur'], 0 ,3)
        SliderPanel(self, 'Contrast', effect_vars['contrast'], 0 ,10)

class ExportFame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')