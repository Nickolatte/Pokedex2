
# imports for the start
import customtkinter as ctk  # pip install customtkinter
from tkinter import PhotoImage
from PIL import Image, ImageTk, ImageFont  # pip install Pillow
import pyglet, tkinter
import pandas as pd     # pip install pandas
import csv

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
        new_user_button = ctk.CTkButton(self, text="Create Account", width=75, height=7, fg_color="transparent", text_color='blue',font=("Pokemon GB", 9), command=self.account_creation_window)
        new_user_button.pack(pady=6)
        new_user_button.place(relx=0.42, rely=0.58)

        # function to check account details
    def checkdetails(self, accountpassword, checkaccountpassword ,account_name):
        if accountpassword.get() == checkaccountpassword.get():

            df = pd.read_csv('user_data.csv')
            accountusernames =  df["username"].values
            print(accountusernames)
            if account_name.get() in accountusernames:
                print("Username already in use")
                
            else:
                print("New username")

            
                new_account = pd.DataFrame([[account_name.get(), accountpassword.get() ,0,0,0,0,0,0]], columns=["username","password","pok1","pok2","pok3","pok4","pok5","pok6"])
                df = pd.concat([df, new_account], ignore_index=True)
                
                df.to_csv('user_data.csv', index=False)
                print(df)
                
                success_account_creation = ctk.CTkToplevel(self)
                success_account_creation.title("ACCOUNT CREATED")
                success_account_creation.geometry("200x100")

                accountcreation = ctk.CTkLabel(success_account_creation, text="Account successfully created", font=("Pokemon GB", 6),width=150,height=50)
                accountcreation.pack()
                
                success_account_creation.after(4000, success_account_creation.destroy)

        else:
            error_account_creation = ctk.CTkToplevel(self)
            error_account_creation.title("ERROR")
            error_account_creation.geometry("200x100")

            accountcreation = ctk.CTkLabel(error_account_creation, text="Passwords do not match! Try again",font=("Pokemon GB", 6))
            accountcreation.pack()
            
            error_account_creation.after(4000, error_account_creation.destroy)

            
            
            

            





        # Account creation window
    def account_creation_window(self):
        account_creation = ctk.CTkToplevel(self)
        account_creation.title("Create Account")
        account_creation.geometry("300x300")
        account_creation.attributes("-topmost", 1)


        account_name = ctk.CTkEntry(account_creation, placeholder_text="Enter a username", fg_color='transparent', height= 50)
        account_name.pack(pady=10, padx=10)
        account_name.place(relx=0.28, rely=0.07)

        
        accountpassword = ctk.CTkEntry(account_creation, placeholder_text="Enter a Password", show="*", fg_color='transparent', height= 50)
        accountpassword.pack(pady=10, padx=10)
        accountpassword.place(relx=0.28, rely=0.25)

        checkaccountpassword = ctk.CTkEntry(account_creation, placeholder_text="Re-Enter your Password", show="*" , fg_color='transparent', height= 50)
        checkaccountpassword.pack(pady=10, padx=10)
        checkaccountpassword.place(relx=0.28, rely=0.45)

        account_creation_btn = ctk.CTkButton(account_creation,width=150, height=40, text="Create Account", command=lambda:[ self.checkdetails(accountpassword, checkaccountpassword, account_name), account_creation.destroy()])
        account_creation_btn.pack(pady=10, padx=10)
        account_creation_btn.place(relx=0.28, rely=0.65)
        




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

        searchlabel = ctk.CTkLabel (new_window,text="Search",width=150,height=30,fg_color="transparent",text_color='black' , font=("Pokemon GB", 15))
        searchlabel.pack(pady=10)
        searchlabel.place(relx=0.7)

        #search button
        self.image3 = Image.open('fixedsearch.png')
        self.tk_image3 = ImageTk.PhotoImage(self.image3)
        searchbtn = ctk.CTkButton(new_window,text='', width=25 , height= 25, image=self.tk_image3,fg_color='transparent',command=self.search_window)
        searchbtn.pack(pady=10)
        searchbtn.place(relx=0.9)

        #settings button
        self.settingbtn = Image.open('setting2.png')
        self.tk_settingbtn = ImageTk.PhotoImage(self.settingbtn)
        settingbtn = ctk.CTkButton(new_window,text='',image=self.tk_settingbtn,fg_color='transparent',width=30,height=30, command=self.settings_window)
        settingbtn.pack(pady=10)
        settingbtn.place(relx=0.01,rely=0.87)

        # pokemon team
        
        # Pokemon 1
        
        poke1btn = ctk.CTkButton(new_window,text="1")
        poke1btn.pack(pady=10)
        poke1btn.place(relx=0.25,rely =0.5)

        # Pokemon 2

        poke2btn = ctk.CTkButton(new_window,text="2")
        poke2btn.pack(pady=10)
        poke2btn.place(relx=0.5,rely =0.5)

        # Pokemon 3
        
        poke3btn = ctk.CTkButton(new_window,text="3")
        poke3btn.pack(pady=10)
        poke3btn.place(relx=0.75,rely =0.5)

        # Pokemon 4

        poke4btn = ctk.CTkButton(new_window,text="4")
        poke4btn.pack(pady=10)
        poke4btn.place(relx=0.25,rely =0.8)

        # Pokemon 5

        poke5btn = ctk.CTkButton(new_window,text="5")
        poke5btn.pack(pady=10)
        poke5btn.place(relx=0.5,rely =0.8)

        # Pokemon 6

        poke6btn = ctk.CTkButton(new_window, text="6")
        poke6btn.pack(pady=10)
        poke6btn.place(relx=0.75, rely =0.8)


        # function to open the manage team menu
    def manage_team_window (self):

        manage_team_window = ctk.CTkToplevel(self)
        manage_team_window.title ("Manage Team")
        manage_team_window.geometry ("500x500")
        manage_team_window.attributes("-topmost", 1)

        # Add/ Swap Pokemon

        swapbtn = ctk.CTkButton(manage_team_window, width= 150, height= 50,text="Swap Button")
        swapbtn.pack(pady= 10)
        swapbtn.place(relx=0.37 ,rely=0.05)

        nextpagebtn = ctk.CTkButton(manage_team_window, text="---->")
        nextpagebtn.pack(pady=10)
        nextpagebtn.place(relx= 0.7 , rely = 0.05)
        
        previouspagebtn = ctk.CTkButton(manage_team_window,text="<----")
        previouspagebtn.pack(pady=10)
        previouspagebtn.place(relx=0.05, rely= 0.05)

        # Pokemon 1

        mpoke1btn = ctk.CTkButton(manage_team_window,text="1")
        mpoke1btn.pack(pady=10)
        mpoke1btn.place(relx=0.05,rely =0.3)

        # Pokemon 2

    
        mpoke2btn = ctk.CTkButton(manage_team_window,text="2")
        mpoke2btn.pack(pady=10)
        mpoke2btn.place(relx=0.37,rely =0.3)

        # Pokemon 3
    
        mpoke3btn = ctk.CTkButton(manage_team_window,text="3")
        mpoke3btn.pack(pady=10)
        mpoke3btn.place(relx=0.7,rely =0.3)

        # Pokemon 4

        poke4btn = ctk.CTkButton(manage_team_window,text="4")
        poke4btn.pack(pady=10)
        poke4btn.place(relx=0.05,rely =0.7)

        # Pokemon 5

        poke5btn = ctk.CTkButton(manage_team_window,text="5")
        poke5btn.pack(pady=10)
        poke5btn.place(relx=0.37,rely =0.7)

        # Pokemon 6
    
        poke6btn = ctk.CTkButton(manage_team_window, text="6")
        poke6btn.pack(pady=10)
        poke6btn.place(relx=0.7, rely =0.7)




        # function to open the settings menu
    def settings_window(self):

        settings_window = ctk.CTkToplevel(self)
        settings_window.title("SETTINGS")
        settings_window.geometry('300x100')
        settings_window.attributes("-topmost", 1)


        editname_lbl = ctk.CTkLabel(settings_window,text="Edit Name", font=("Pokemon GB",10))
        editname_lbl.pack(pady=10)
        editname_lbl.place(relx=0.04,rely=0.05)

        editname_ent = ctk.CTkEntry(settings_window,placeholder_text="Enter new name",font=("Pokemon GB",10))
        editname_ent.pack(pady=10)
        editname_ent.place(relx=0.35,rely=0.05)

        saveeditname_btn = ctk.CTkButton(settings_window,text="save",width=20,font=("Pokemon GB",10))
        saveeditname_btn.pack(pady=10)
        saveeditname_btn.place(relx=0.82,rely=0.05)

        deleteaccount_lbl = ctk.CTkLabel(settings_window,text="Delete Account",font=("Pokemon GB",10))
        deleteaccount_lbl.pack(pady=10)
        deleteaccount_lbl.place(relx=0.04,rely=0.4)

        deleteaccount_btn = ctk.CTkButton(settings_window,text="DELETE",command=self.confirmaccountdelete,font=("Pokemon GB",10))
        deleteaccount_btn.pack(pady=10)
        deleteaccount_btn.place(relx=0.52,rely=0.4)

    def confirmaccountdelete(self):
        confirmaccountdelete=ctk.CTkToplevel(self)
        confirmaccountdelete.title("Confirm Account Delete")
        confirmaccountdelete.geometry("200x100")
        confirmaccountdelete.attributes("-topmost", 1)

        confirmbutton = ctk.CTkButton (confirmaccountdelete,text="CONFIRM",font=("Pokemon GB",15))
        confirmbutton.pack()
        confirmbutton.place(relx=0.15,rely=0.3)


        # funtion to open the search window/menu
    def search_window(self):

        search_window = ctk.CTkToplevel(self)
        search_window.title("SEARCH")
        search_window.geometry('800x600')
        search_window.attributes("-topmost", 1)
        
        searchentry = ctk.CTkEntry (search_window,placeholder_text="Search by Name or Number",width=400,height=30,text_color='black' , font=("Pokemon GB", 15))
        searchentry.pack(pady=5)
        searchentry.place(relx=0.26,rely=0.03,)

        nextpagebtn = ctk.CTkButton(search_window, text="---->")
        nextpagebtn.pack(pady=10)
        nextpagebtn.place(relx= 0.8 , rely = 0.03)
        
        previouspagebtn = ctk.CTkButton(search_window,text="<----")
        previouspagebtn.pack(pady=10)
        previouspagebtn.place(relx=0.05, rely= 0.03)

        searchpokemonbtn1 = ctk.CTkButton(search_window,text='1')
        searchpokemonbtn1.pack(pady=10)
        searchpokemonbtn1.place(relx=0.025,rely=0.3 )

        searchpokemonbtn2 = ctk.CTkButton(search_window,text='2')
        searchpokemonbtn2.pack(pady=10)
        searchpokemonbtn2.place(relx=0.30 , rely=0.3)

        searchpokemonbtn3 = ctk.CTkButton(search_window,text='3')
        searchpokemonbtn3.pack(pady=10)
        searchpokemonbtn3.place(relx=0.55 , rely=0.3)

        searchpokemonbtn4 = ctk.CTkButton(search_window,text='4')
        searchpokemonbtn4.pack(pady=10)
        searchpokemonbtn4.place(relx=0.8, rely=0.3)

        searchpokemonbtn5 = ctk.CTkButton(search_window,text='5')
        searchpokemonbtn5.pack(pady=10)
        searchpokemonbtn5.place(relx=0.025,rely=0.55)

        searchpokemonbtn6 = ctk.CTkButton(search_window,text='6')
        searchpokemonbtn6.pack(pady=10)
        searchpokemonbtn6.place(relx=0.30,rely=0.55)

        searchpokemonbtn7 = ctk.CTkButton(search_window,text='7')
        searchpokemonbtn7.pack(pady=10)
        searchpokemonbtn7.place(relx=0.55,rely=0.55)

        searchpokemonbtn8 = ctk.CTkButton(search_window,text='8')
        searchpokemonbtn8.pack(pady=10)
        searchpokemonbtn8.place(relx=0.8,rely=0.55)

        searchpokemonbtn9 = ctk.CTkButton(search_window,text='9')
        searchpokemonbtn9.pack(pady=10)
        searchpokemonbtn9.place(relx=0.025,rely=0.8)

        searchpokemonbtn10 = ctk.CTkButton(search_window,text='10')
        searchpokemonbtn10.pack(pady=10)
        searchpokemonbtn10.place(relx=0.3,rely=0.8)

        searchpokemonbtn11 = ctk.CTkButton(search_window,text='11')
        searchpokemonbtn11.pack(pady=10)
        searchpokemonbtn11.place(relx=0.55,rely=0.8)

        searchpokemonbtn12 = ctk.CTkButton(search_window,text='12')
        searchpokemonbtn12.pack(pady=10)
        searchpokemonbtn12.place(relx=0.8,rely=0.8)



# Initialize and run the app

app = App()
app.mainloop()
