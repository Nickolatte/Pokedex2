# imports for the start
import customtkinter as ctk # pip install customtkinter
from tkinter import PhotoImage

from PIL import Image, ImageTk , ImageFont #pip install Pillow
import pyglet,tkinter



# Class for the main menu
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Nicholas' Pokedex")
        self.geometry("900x900")




        # background image 
        self.background_image = Image.open("pokdexmainbg.png")
        self.tk_image = ImageTk.PhotoImage(self.background_image)
        background_label = ctk.CTkLabel(self, image=self.tk_image, text="")
        background_label.pack(pady=20)

        # title text
        self.image1 = Image.open("pokemon-gb.png")
        self.tk_image1 = ImageTk.PhotoImage(self.image1)
        label1 = ctk.CTkLabel ( self,text="", width=150, height= 100 ,fg_color="#ee5351", image=self.tk_image1)

    
        label1.pack(pady=10)
        label1.place(relx=0.5, rely=0.1, anchor='center')

        # button for identification
        identify_button = ctk.CTkButton(self, text="Idenitfy" ,width=100 ,height=50,fg_color="#ee5351")
        identify_button.pack(pady=10)
        identify_button.place(relx=0.5 ,rely=0.21, anchor='center' )



# Initialize and run the app
if __name__ == "__main__":
    app = App()
    app.mainloop()
