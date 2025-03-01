
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
        ctk.set_appearance_mode("light")

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
        new_user_button = ctk.CTkButton(self, text="Create Account", width=75, height=5, fg_color="transparent", text_color='blue',font=("Pokemon GB", 7))
        new_user_button.pack(pady=6)
        new_user_button.place(relx=0.42, rely=0.58)

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
        team_button = ctk.CTkLabel (new_window, text="Team", width=150 , height= 30,font=("Pokemon GB",20), fg_color='#3b8ed0')
        team_button.pack(pady=10)
        team_button.place(relx=0, rely=0.3)

        # button to manage team
        team_managebtn = ctk.CTkButton(new_window,text="Manage Team", width= 150, height= 40 )
        team_managebtn.pack(pady=10)
        team_managebtn.place(relx=0 ,rely=0.36)

        # shows the users profile picture
        self.image2= Image.open('brockpfp2.jpg')
        self.tk_image2 = ImageTk.PhotoImage(self.image2)
        pfp= ctk.CTkLabel(new_window, text="", width=150, height=150, fg_color="transparent", image=self.tk_image2)
        pfp.pack(pady=10)
        pfp.place(relx=0)

        #user name
        usernamelabel= ctk.CTkLabel (new_window,text="Brock",width=150,height=50,fg_color="crimson",font=("Pokemon GB", 15))
        usernamelabel.pack(pady=10)
        usernamelabel.place(relx=0.214)

        #search button
        self.image3 = Image.open('fixedsearch.png')
        self.tk_image3 = ImageTk.PhotoImage(self.image3)
        searchbtn = ctk.CTkButton(new_window,text='', width=25 , height= 25, image=self.tk_image3,fg_color='transparent')
        searchbtn.pack(pady=10)
        searchbtn.place(relx=0.8)

        #pokemon team
        
        # Pokemon 1

        #self.poke1 =Image.open()
        #self.tk_poke1 = ImageTk.PhotoImage()
        poke1btn = ctk.CTkButton(new_window,text="1")
        poke1btn.pack(pady=10)
        poke1btn.place(relx=0.25,rely =0.5)

        # Pokemon 2

        #self.poke2 =Image.open()
        #self.tk_poke2 = ImageTk.PhotoImage()
        poke2btn = ctk.CTkButton(new_window,text="2")
        poke2btn.pack(pady=10)
        poke2btn.place(relx=0.5,rely =0.5)

        # Pokemon 3
        #self.poke3 =Image.open()
        #self.tk_poke3 = ImageTk.PhotoImage()
        poke3btn = ctk.CTkButton(new_window,text="3")
        poke3btn.pack(pady=10)
        poke3btn.place(relx=0.75,rely =0.5)

        # Pokemon 4

        #self.poke4 =Image.open()
        #self.tk_poke4 = ImageTk.PhotoImage()
        poke4btn = ctk.CTkButton(new_window,text="4")
        poke4btn.pack(pady=10)
        poke4btn.place(relx=0.25,rely =0.8)

        # Pokemon 5

        #self.poke5 =Image.open()
        #self.tk_poke5 = ImageTk.PhotoImage()
        poke5btn = ctk.CTkButton(new_window,text="5")
        poke5btn.pack(pady=10)
        poke5btn.place(relx=0.5,rely =0.8)

        # Pokemon 6
        #self.poke6 =Image.open()
        #self.tk_poke6 = ImageTk.PhotoImage()
        poke6btn = ctk.CTkButton(new_window, text="6")
        poke6btn.pack(pady=10)
        poke6btn.place(relx=0.75, rely =0.8)



# Initialize and run the app

app = App()
app.mainloop()
