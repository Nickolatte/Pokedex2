import customtkinter as ctk
from PIL import Image
import requests
from io import BytesIO

def load_pokemon_sprite(pokemon_id):
    """Fetch Pokémon sprite from PokéAPI."""
    url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"
    response = requests.get(url)
    if response.status_code == 200:
        img_data = Image.open(BytesIO(response.content))
        return ctk.CTkImage(light_image=img_data, size=(64, 64))  # Resize if needed
    return None  # Return None if sprite not found

def search_window(self):
    search_window = ctk.CTkToplevel(self)
    search_window.title("SEARCH")
    search_window.geometry('800x600')
    search_window.attributes("-topmost", 1)

    searchentry = ctk.CTkEntry(search_window, placeholder_text="Search by Name or Number",
                               width=400, height=30, text_color='black', font=("Pokemon GB", 15))
    searchentry.place(relx=0.26, rely=0.03)

    submitbtn = ctk.CTkButton(search_window, text="ENTER", 
                              command=lambda: self.search_pokemon(searchentry))
    submitbtn.place(relx=0.6, rely=0.09)

    # Pokémon buttons with images
    positions = [(0.025, 0.3), (0.30, 0.3), (0.55, 0.3), (0.8, 0.3),
                 (0.025, 0.55), (0.30, 0.55), (0.55, 0.55), (0.8, 0.55),
                 (0.025, 0.8), (0.3, 0.8), (0.55, 0.8), (0.8, 0.8)]
    
    for i in range(12):  # First 12 Pokémon
        pokemon_id = i + 1
        sprite = load_pokemon_sprite(pokemon_id)
        btn = ctk.CTkButton(search_window, text=str(pokemon_id), image=sprite, compound="top", 
                            command=lambda pid=pokemon_id: self.show_pokemon_info(pid))
        btn.place(relx=positions[i][0], rely=positions[i][1])

    search_window.mainloop()