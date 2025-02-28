
# imports for the start
import customtkinter as ctk  # pip install customtkinter
from tkinter import PhotoImage
from PIL import Image, ImageTk, ImageFont  # pip install Pillow
import pyglet, tkinter
import pandas as pd     # pip install pandas


# Class for the main menu
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Nicholas' Pokedex")
        self.geometry("850x300")

        # title text
        self.image1 = Image.open("pokedexwelcome.png")
        self.tk_image1 = ImageTk.PhotoImage(self.image1)
        label1 = ctk.CTkLabel(self, text="", width=10, height=100, fg_color="transparent", image=self.tk_image1)
        label1.pack(pady=10)
        label1.place(relx=0.25, rely=0.075, anchor='w')

        # username entry
        user_entry = ctk.CTkEntry(self, placeholder_text="Username")
        user_entry.pack(pady=12, padx=10)
        user_entry.place(relx=0.43, rely=0.2)

        # password entry
        user_pass = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        user_pass.pack(pady=12, padx=10)
        user_pass.place(relx=0.43, rely=0.35)

        # button for login
        identify_button = ctk.CTkButton(self, text="Login", width=150, height=30, fg_color="#ee5351", command=self.pokedex_menu)
        identify_button.pack(pady=10)
        identify_button.place(relx=0.51, rely=0.527, anchor='center')

        # new user account button
        new_user_button = ctk.CTkButton(self, text="Create Account", width=75, height=10, fg_color="transparent", text_color='blue')
        new_user_button.pack(pady=10)
        new_user_button.place(relx=0.4, rely=0.61)

    # Method to open a new window
    def pokedex_menu(self):
    
        # Create a new top-level window
        new_window = ctk.CTkToplevel(self)
        new_window.title("Pokedex")
        new_window.geometry('700x500')

        #  Make the window open on top of the other menu
        new_window.attributes("-topmost", 1)

        # hides the login menu
        self.withdraw()

        # shows the teams (from the csv)
        team_button = ctk.CTkButton (new_window, text="Team", width=150 , height= 30,)
        team_button.pack(pady=10)
        team_button.place(relx=0, rely=0.3)

        # shows the users profile picture
        self.image2= Image.open('brockpfp2.jpg')
        self.tk_image2 = ImageTk.PhotoImage(self.image2)
        label2= ctk.CTkLabel(new_window, text="", width=150, height=150, fg_color="transparent", image=self.tk_image2)
        label2.pack(pady=10)
        label2.place(relx=0)








# Initialize and run the app

app = App()
app.mainloop()
