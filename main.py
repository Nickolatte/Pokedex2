
# imports for the start
import customtkinter as ctk  # pip install customtkinter
from tkinter import PhotoImage
from PIL import Image, ImageTk, ImageFont  # pip install Pillow
import pyglet, tkinter
import pandas as pd     # pip install pandas
import csv
import requests

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
        self.user_entry = ctk.CTkEntry(self, placeholder_text="Username")
        self.user_entry.pack(pady=12, padx=10)
        self.user_entry.place(relx=0.43, rely=0.2)

        # password entry
        self.user_pass = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.user_pass.pack(pady=12, padx=10)
        self.user_pass.place(relx=0.43, rely=0.35)

        # button for login
        identify_button = ctk.CTkButton(self, text="Login", width=150, height=30, fg_color="#ee5351", command=self.loginsystem)
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
                success_account_creation.geometry("400x70")

                accountcreation = ctk.CTkLabel(success_account_creation, text="Account successfully created", font=("Pokemon GB", 10),width=150,height=50)
                accountcreation.pack(pady=10, padx=10)
                accountcreation.place(relx=0.2, rely=0.25)
                
                success_account_creation.after(3000, success_account_creation.destroy)

        else:
            error_account_creation = ctk.CTkToplevel(self)
            error_account_creation.title("ERROR")
            error_account_creation.geometry("400x70")

            erroraccountcreation = ctk.CTkLabel(error_account_creation, text="Passwords do not match! Try again",font=("Pokemon GB", 10),width=150,height=50)
            erroraccountcreation.pack(pady=10, padx=10)
            erroraccountcreation.place(relx=0.1, rely=0.25)
            error_account_creation.after(3000, error_account_creation.destroy)

            

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
        
    def loginsystem(self):

        user = self.user_entry.get()
        passw = self.user_pass.get()



        df = pd.read_csv('user_data.csv')

        matching_creds = (len(df[(df.username == user) & (df.password == passw)]) > 0)
        
        if matching_creds:
            print('success')
            self.pokedex_menu()
        else:
            noaccount =ctk.CTkToplevel(self)
            noaccount.title("ERROR")
            noaccount.geometry('600x70')
            noaccount.attributes("-topmost",1)

            error_lbl = ctk.CTkLabel(noaccount,text="Your Account is not registered or details are incorrect",font=("Pokemon GB",10))
            error_lbl.pack(pady=10)
            error_lbl.place(relx=0.02,rely=0.1)

            tryagain_lbl = ctk.CTkLabel(noaccount,text="Please try again",font=("Pokemon GB",10))
            tryagain_lbl.pack(pady=5)
            tryagain_lbl.place (relx=0.35,rely=0.5)
            noaccount.after(4000, noaccount.destroy)




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

        

        #user name
        df = pd.read_csv('user_data.csv')
        usernamelabel= ctk.CTkLabel (new_window,text=self.user_entry.get(),width=170,height=50,fg_color="crimson",font=("Pokemon GB", 15))
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

        submitbtn =ctk.CTkButton (search_window,text="ENTER", command=lambda:self.search_pokemon(searchentry)) #command=self.searchpokemonfunctions(searchentry)
        submitbtn.pack(pady=5)
        submitbtn.place(relx=0.6,rely=0.09)

        nextpagebtn = ctk.CTkButton(search_window, text="---->")
        nextpagebtn.pack(pady=10)
        nextpagebtn.place(relx= 0.8 , rely = 0.03)
        
        previouspagebtn = ctk.CTkButton(search_window,text="<----")
        previouspagebtn.pack(pady=10)
        previouspagebtn.place(relx=0.05, rely= 0.03)


        self.pokemon_images = [] 
        for i in range(12):
            pokemon_id = i + 1  

            try:
                # gets the sprite from the the API 
                url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"
                response = requests.get(url, stream=True)
                if response.status_code == 200:
                    image = Image.open(response.raw)
                    image = image.resize((64, 64))  
                    sprite = ImageTk.PhotoImage(image)
                    self.pokemon_images.append(sprite)  #
                else:
                    sprite = None
            except Exception as e:
                print(f"Error loading sprite for Pokémon {pokemon_id}: {e}")
                sprite = None

        
            xposition = 0.025 + (i % 4) * 0.275  
            yposition = 0.3 + (i // 4) * 0.25  

            poke_button = ctk.CTkButton(search_window, text=f' {pokemon_id} ', image=sprite, compound="top", width=100, height=100)
            poke_button.pack(pady=10)
            poke_button.place(relx=xposition, rely=yposition)


    def show_pokemon_details(self, pokemon_id):
        details_window = ctk.CTkToplevel(self)
        details_window.title(f"Pokémon #{pokemon_id} Details")
        details_window.geometry("400x500")
        details_window.attributes("-topmost", 1)

        try:
            
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                name = data["name"].capitalize()
                height = data["height"] / 10  
                weight = data["weight"] / 10  
                types = ", ".join(t["type"]["name"].capitalize() for t in data["types"])

                # Get the Pokémon sprite
                sprite_url = data["sprites"]["front_default"]
                sprite_response = requests.get(sprite_url, stream=True)
                if sprite_response.status_code == 200:
                    sprite_image = Image.open(sprite_response.raw)
                    sprite_image = sprite_image.resize((150, 150))
                    sprite_photo = ImageTk.PhotoImage(sprite_image)
                else:
                    sprite_photo = None
            else:
                name, height, weight, types, sprite_photo = "Unknown", "?", "?", "?", None

        except Exception as e:
            print(f"Error fetching Pokémon details: {e}")
            name, height, weight, types, sprite_photo = "Unknown", "?", "?", "?", None

        
        if sprite_photo:
            sprite_label = ctk.CTkLabel(details_window, image=sprite_photo, text="")
            sprite_label.image = sprite_photo  
            sprite_label.pack(pady=10)

        # Display Pokémon Details
        details_text = f"Name: {name}\nHeight: {height} m\nWeight: {weight} kg\nType(s): {types}"
        details_label = ctk.CTkLabel(details_window, text=details_text, font=("Pokemon GB", 15))
        details_label.pack(pady=10)

        
    def search_pokemon(self, search_entry):
        pokemon_name_or_id = search_entry.get().lower()  
        if not pokemon_name_or_id:
            return  

        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name_or_id}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            pokemon_name = data["name"].capitalize()
            pokemon_id = data["id"]
            pokemon_sprite = data["sprites"]["front_default"]
            pokemon_types = [t["type"]["name"].capitalize() for t in data["types"]]

        
            self.display_pokemon_results(pokemon_name, pokemon_id, pokemon_sprite, pokemon_types)

        else:
            print("Pokemon not found!")

    def display_pokemon_results(self, name, id, sprite, types):
        
        results_window = ctk.CTkToplevel(self)
        results_window.title(name)
        results_window.geometry("400x400")

        name_label = ctk.CTkLabel(results_window, text=f"Name: {name}")
        name_label.pack(pady=10)

        id_label = ctk.CTkLabel(results_window, text=f"ID: {id}")
        id_label.pack(pady=10)

        type_label = ctk.CTkLabel(results_window, text=f"Type: {', '.join(types)}")
        type_label.pack(pady=10)

    
        response = requests.get(sprite, stream=True)
        img = Image.open(response.raw)
        img = img.resize((100, 100))
        img = ImageTk.PhotoImage(img)

        image_label = ctk.CTkLabel(results_window, image=img, text="")
        image_label.image = img  
        image_label.pack(pady=10)







# Initialize and run the app

app = App()
app.mainloop()
