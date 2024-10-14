"""
This code is a simple image slider application implemented using the Tkinter library in Python. It allows the user
to select a folder containing PNG images and then displays the images one by one in a window with navigation buttons
to move between images.

The code starts by importing the necessary libraries: os for operating system-related
functions, tkinter for creating the GUI, filedialog from tkinter for opening a file dialog box, and Image and ImageTk
from the PIL (Python Imaging Library) for image handling.

The get_image_list function takes a folder path as input and returns a list of file names that end with '.png' in the
specified folder. This function is used to filter out only PNG images from the selected folder.

The ImageSliderApp class is defined. It serves as the main application class and contains all the functionality for
loading and displaying images.

In the __init__ method of ImageSliderApp, the GUI window is created and configured. The title of the window is set to
'Image Slider'. Several buttons and a canvas widget are created and packed into the window.

The load_images method is called when the "Load Images" button is clicked. It opens a folder dialog box using
filedialog.askdirectory and allows the user to select a folder containing images. If a folder is selected,
it calls the get_image_list function to get the list of PNG images from the folder. If the list is not empty,
it shows the first image using the show_image method. Otherwise, it displays a message indicating that no images were
found.

The show_image method takes an image file name as input and displays the image on the canvas. It opens the image
using Image.Open from PIL, resizes it to 512x512 pixels, creates a PhotoImage object from the resized image using
ImageTk.PhotoImage, and then uses the create_image method of the canvas to display the image.

The show_next_image and show_previous_image methods are called when the "Next" and "Previous" buttons are clicked,
respectively. These methods check if there is a valid image list and if the current image index allows moving to the
next or previous image. If so, they update the current image index and call the show_image method with the
corresponding image from the image list.

The show_message method is used to display text messages on the canvas. It clears the canvas using delete('all') and
then creates a text object at the center of the canvas with the specified message.

Finally, the code checks if the current module is being run as the main program (not imported as a module). If so,
it creates an instance of the Tk class, which represents the main window of the application, and an instance of the
ImageSliderApp class, passing the Tk object as the master. The mainloop method is called to start the event loop and
keep the application running.

When you run this code, a window will appear with a "Load Images" button. Clicking this button will open a folder
selection dialog. After selecting a folder, the first image in the folder will be displayed on the canvas. You can
navigate between images using the "Next" and "Previous" buttons. If there are no more images, or you are at the
beginning, a corresponding message will be shown on the canvas.
"""

import os
import tkinter as tk
from tkinter import filedialog

from PIL import Image, ImageTk

folder_path = ""


def get_image_list(folder_path):
    return [f for f in os.listdir(folder_path) if f.endswith('.png')]


class ImageSliderApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Image Slider')
        self.image_list = []
        self.current_image_index = 0
        self.load_images_button = tk.Button(self.master, text='Load Images', command=self.load_images)
        self.load_images_button.pack()
        self.canvas = tk.Canvas(self.master, width=512, height=512)
        self.canvas.pack()
        self.prev_button = tk.Button(self.master, text='Previous', command=self.show_previous_image)
        self.prev_button.pack(side=tk.LEFT)
        self.next_button = tk.Button(self.master, text='Next', command=self.show_next_image)
        self.next_button.pack(side=tk.RIGHT)

    def load_images(self):
        global folder_path
        folder_path = filedialog.askdirectory(title='Select Folder with Images', mustexist=True)
        if folder_path:
            self.image_list = get_image_list(folder_path)
            if self.image_list:
                self.show_image(self.image_list[0])
            else:
                self.show_message('No images found in the selected folder.')

    def show_image(self, image_file):
        global folder_path
        image = Image.open(os.path.join(folder_path, image_file))
        image = image.resize((512, 512))
        self.current_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.current_image)

    def show_next_image(self):
        if self.image_list and self.current_image_index < len(self.image_list) - 1:
            self.current_image_index += 1
            self.show_image(self.image_list[self.current_image_index])
        else:
            self.show_message('There is no more image.')

    def show_previous_image(self):
        if self.image_list and self.current_image_index > 0:
            self.current_image_index -= 1
            self.show_image(self.image_list[self.current_image_index])
        else:
            self.show_message('You are at the beginning.')

    def show_message(self, message):
        self.canvas.delete('all')
        self.canvas.create_text(256, 256, text=message)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSliderApp(root)
    root.mainloop()
