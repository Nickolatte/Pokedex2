
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
        new_user_button = ctk.CTkButton(self, text="Create Account", width=75, height=5, fg_color="transparent", text_color='blue',font=("Pokemon GB", 7), command=self.account_creation_window)
        new_user_button.pack(pady=6)
        new_user_button.place(relx=0.42, rely=0.58)

        # function to check account details
    def checkdetails(self, accountpassword, checkaccountpassword):
        if accountpassword.get() == checkaccountpassword.get():
            success_account_creation = ctk.CTkToplevel(self)
            success_account_creation.title("ACCOUNT CREATED")
            success_account_creation.geometry("150x150")

            accountcreation = ctk.CTkLabel(success_account_creation, text="Account successfully created")
            accountcreation.pack()

            
        else:
            error_account_creation = ctk.CTkToplevel(self)
            error_account_creation.title("ERROR")
            error_account_creation.geometry("150x150")

            accountcreation = ctk.CTkLabel(error_account_creation, text="Passwords do not match!")
            accountcreation.pack()

        # Account creation window
    def account_creation_window(self):
        account_creation = ctk.CTkToplevel(self)
        account_creation.title("Create Account")
        account_creation.geometry("650x500")
        account_creation.attributes("-topmost", 1)


        # background
        account_background = Image.open("pokeballpc.png")
        tk_account_background = ImageTk.PhotoImage(account_background)
        account_background = ctk.CTkLabel(account_creation, text="", width=10, height=100, fg_color="transparent", image=tk_account_background)
        account_background.place(relwidth=1, relheight=1)

        



        account_name = ctk.CTkEntry(account_creation, placeholder_text="Enter a username")
        account_name.pack(pady=12, padx=10)
        account_name.place(relx=0.43, rely=0.2)



        accountpassword = ctk.CTkEntry(account_creation, placeholder_text="Enter a Password", show="*")
        accountpassword.pack(pady=12, padx=10)
        accountpassword.place(relx=0.43, rely=0.35)

        checkaccountpassword = ctk.CTkEntry(account_creation, placeholder_text="Re-Enter your Password", show="*")
        checkaccountpassword.pack(pady=12, padx=10)
        checkaccountpassword.place(relx=0.43, rely=0.55)

        account_creation_btn = ctk.CTkButton(account_creation, width=100, height=40, text="Create Account", command=lambda: self.checkdetails(accountpassword, checkaccountpassword))
        account_creation_btn.pack(pady=12, padx=10)
        account_creation_btn.place(relx=0.43, rely=0.65)




    

        # command to open a pokedex window
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
        team_lbl = ctk.CTkLabel (new_window, text="Team", width=150 , height= 30,font=("Pokemon GB",20), fg_color='#3b8ed0')
        team_lbl.pack(pady=10)
        team_lbl.place(relx=0.45, rely=0.3)

        # button to manage team
        team_managebtn = ctk.CTkButton(new_window,text="Manage Team", width= 140, height= 40 , font=("Pokemon GB", 12), command=self.manage_team_window)
        team_managebtn.pack(pady=10)
        team_managebtn.place(relx=0 ,rely=0.36)

        # shows the users profile picture
        self.image2= Image.open('brockpfp2.jpg')
        self.tk_image2 = ImageTk.PhotoImage(self.image2)
        pfp= ctk.CTkLabel(new_window, text="", width=150, height=150, fg_color="transparent", image=self.tk_image2)
        pfp.pack(pady=10)
        pfp.place(relx=0)

        #user name
        usernamelabel= ctk.CTkLabel (new_window,text="Brock",width=170,height=50,fg_color="crimson",font=("Pokemon GB", 15))
        usernamelabel.pack(pady=10)
        usernamelabel.place(relx=0.214)


        #search button

        searchlabel = ctk.CTkButton (new_window,text="Search",width=150,height=30,fg_color="transparent",text_color='black' , font=("Pokemon GB", 15))
        searchlabel.pack(pady=10)
        searchlabel.place(relx=0.7)

        #search button
        self.image3 = Image.open('fixedsearch.png')
        self.tk_image3 = ImageTk.PhotoImage(self.image3)
        searchbtn = ctk.CTkButton(new_window,text='', width=25 , height= 25, image=self.tk_image3,fg_color='transparent')
        searchbtn.pack(pady=10)
        searchbtn.place(relx=0.9)

        #settings button
        self.settingbtn = Image.open('setting2.png')
        self.tk_settingbtn = ImageTk.PhotoImage(self.settingbtn)
        settingbtn = ctk.CTkButton(new_window,text='',image=self.tk_settingbtn,fg_color='transparent',width=30,height=30, command=self.settings_window)
        settingbtn.pack(pady=10)
        settingbtn.place(relx=0.01,rely=0.87)
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


        # function to open the manage team menu
    def manage_team_window (self):

        manage_team_window = ctk.CTkToplevel(self)
        manage_team_window.title ("Manage Team")
        manage_team_window.geometry ("500x500")
        manage_team_window.attributes("-topmost", 1)


        #self.poke1 =Image.open()
        #self.tk_poke1 = ImageTk.PhotoImage()
        poke1btn = ctk.CTkButton(manage_team_window,text="1")
        poke1btn.pack(pady=10)
        poke1btn.place(relx=0.05,rely =0.3)

        # Pokemon 2

        #self.poke2 =Image.open()
        #self.tk_poke2 = ImageTk.PhotoImage()
        poke2btn = ctk.CTkButton(manage_team_window,text="2")
        poke2btn.pack(pady=10)
        poke2btn.place(relx=0.37,rely =0.3)

        # Pokemon 3
        #self.poke3 =Image.open()
        #self.tk_poke3 = ImageTk.PhotoImage()
        poke3btn = ctk.CTkButton(manage_team_window,text="3")
        poke3btn.pack(pady=10)
        poke3btn.place(relx=0.7,rely =0.3)

        # Pokemon 4

        #self.poke4 =Image.open()
        #self.tk_poke4 = ImageTk.PhotoImage()
        poke4btn = ctk.CTkButton(manage_team_window,text="4")
        poke4btn.pack(pady=10)
        poke4btn.place(relx=0.1,rely =0.7)

        # Pokemon 5

        #self.poke5 =Image.open()
        #self.tk_poke5 = ImageTk.PhotoImage()
        poke5btn = ctk.CTkButton(manage_team_window,text="5")
        poke5btn.pack(pady=10)
        poke5btn.place(relx=0.4,rely =0.7)

        # Pokemon 6
        #self.poke6 =Image.open()
        #self.tk_poke6 = ImageTk.PhotoImage()
        poke6btn = ctk.CTkButton(manage_team_window, text="6")
        poke6btn.pack(pady=10)
        poke6btn.place(relx=0.7, rely =0.7)

        # function to open the settings menu
    def settings_window(self):

        settings_window = ctk.CTkToplevel(self)
        settings_window.title("SETTINGS")
        settings_window.geometry('500x500')
        settings_window.attributes("-topmost", 1)

        # funtion to open the search window/menu
    def search_window(self):

        search_window = ctk.CTkToplevel(self)
        search_window.title("SEARCH")
        search_window.geometry('400x400')
        search_window.attributes("-topmost", 1)

    # function to check if details are correct
    
    




# Initialize and run the app

app = App()
app.mainloop()
