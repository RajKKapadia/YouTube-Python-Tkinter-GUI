import customtkinter as ctk
from PIL import Image, ImageTk

from image_widgets import ImageImport, ImageOutput, CloseOutput
from menu import Menu

class App(ctk.CTk):
    def __init__(self):

        # Setup
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1100x600')
        self.title('Photo editor')
        self.minsize(900, 600)

        # Layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')

        # Widgets
        self.image_import = ImageImport(self, self.import_image)
        
        # Run
        self.mainloop()

    def import_image(self, path: str) -> None:
        self.image = Image.open(path)
        self.image_ratio = self.image.size[0] / self.image.size[1]
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.image_import.grid_forget()
        self.image_output = ImageOutput(self, self.resize_image)
        self.close_button = CloseOutput(self, self.close_edit)
        self.menu = Menu(self)

    def close_edit(self):
        self.image_output.grid_forget()
        self.close_button.place_forget()
        self.menu.grid_forget()
        self.image_import = ImageImport(self, self.import_image)

    def resize_image(self, event):
        # Current canvas ration
        canvas_ratio = event.width / event.height

        # Resize
        if canvas_ratio > self.image_ratio: # Canvas is wider
            image_height = event.height
            image_width = image_height * self.image_ratio
        else: # Canvas is taler
            image_width = event.width
            image_height = image_width / self.image_ratio

        # Place image
        self.image_output.delete('all')
        resized_image = self.image.resize((int(image_width), int(image_height)))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image(event.width/2, event.height/2, image=self.image_tk)


if __name__ == '__main__':
    App()