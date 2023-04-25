import customtkinter as ctk
from PIL import Image, ImageTk, ImageOps

from image_widgets import ImageImport, ImageOutput, CloseOutput
from menu import Menu
from settings import *

class App(ctk.CTk):
    def __init__(self):

        # Setup
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1100x600')
        self.title('Photo editor')
        self.minsize(1100, 600)
        self.init_parameters()

        # Layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')

        # Canvas data
        self.image_width = 0
        self.image_height = 0
        self.canvas_width = 0
        self.canvas_height = 0

        # Widgets
        self.image_import = ImageImport(self, self.import_image)
        
        # Run
        self.mainloop()

    def init_parameters(self):
        self.pos_vars = {
            'rotate': ctk.DoubleVar(value=ROTATE_DEFAULT),
            'zoom': ctk.DoubleVar(value=ZOOM_DEFAULT),
            'flip': ctk.StringVar(value=FLIP_OPTIONS[0])
        }

        self.color_vars = {
            'brightness': ctk.DoubleVar(value=BRIGHTNESS_DEFAULT),
            'grayscale': ctk.BooleanVar(value=GRAYSCALE_DEFAULT),
            'invert': ctk.BooleanVar(value=INVERT_DEFAULT),
            'vibrance': ctk.DoubleVar(value=VIBRANCE_DEFAULT)
        }

        self.effect_vars = {
            'blur': ctk.DoubleVar(value=BLUR_DEFAULT),
            'contrast': ctk.IntVar(value=CONTRAST_DEFAULT),
            'effects': ctk.StringVar(value=EFFECT_OPTIONS[0])
        }

        # Tracing
        for var in self.pos_vars.values():
            var.trace('w', self.manipulate_image)
        for var in self.color_vars.values():
            var.trace('w', self.manipulate_image)
        for var in self.effect_vars.values():
            var.trace('w', self.manipulate_image)

    def manipulate_image(self, *args):
        self.image = self.original.copy()
        self.image = self.image.rotate(self.pos_vars['rotate'].get())
        self.image = ImageOps.crop(image=self.image, border=self.pos_vars['zoom'].get())
        self.place_image()

    def import_image(self, path: str) -> None:
        self.original = Image.open(path)
        self.image = self.original.copy()
        self.image_ratio = self.image.size[0] / self.image.size[1]
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.image_import.grid_forget()
        self.image_output = ImageOutput(self, self.resize_image)
        self.close_button = CloseOutput(self, self.close_edit)
        self.menu = Menu(self, self.pos_vars, self.color_vars, self.effect_vars)

    def close_edit(self):
        self.image_output.grid_forget()
        self.close_button.place_forget()
        self.menu.grid_forget()
        self.image_import = ImageImport(self, self.import_image)

    def resize_image(self, event):
        # Current canvas ration
        canvas_ratio = event.width / event.height

        self.canvas_height = event.height
        self.canvas_width = event.width

        # Resize
        if canvas_ratio > self.image_ratio: # Canvas is wider
            self.image_height = self.canvas_height
            self.image_width = self.image_height * self.image_ratio
        else: # Canvas is taler
            self.image_width = self.canvas_width
            self.image_height = self.image_width / self.image_ratio

        self.place_image()

    def place_image(self):
        self.image_output.delete('all')
        resized_image = self.image.resize((int(self.image_width), int(self.image_height)))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image(self.canvas_width/2, self.canvas_width/2, image=self.image_tk)


if __name__ == '__main__':
    App()