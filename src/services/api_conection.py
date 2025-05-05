import requests
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import messagebox
from customtkinter import CTkImage

class ApiConnection:
    def __init__(self, url):
        self.url = url

    def getPokemonData(self, pokemon):
        try:
            response = requests.get(self.url + pokemon)
            return response.json()
        except Exception as e:
            return None
    
    def getPokemonImage(self, pokemon):
        try:
            response = requests.get(self.url + pokemon)
            response = requests.get(response.json()["sprites"]["front_default"])
            response.raise_for_status()
            img_data = BytesIO(response.content)
            return img_data
        except Exception as e:
            return None
        
    def updateDisplay(self, pokemon, informations):
        try:
            pokemon_data = self.getPokemonData(pokemon)
            informations[0].configure(image=self.image(self.getPokemonImage(pokemon.lower()), (245, 245))[0])
            informations[1].configure(text=f"{pokemon_data["name"].title()} Nª {pokemon_data["id"]}")
            informations[2].configure(text=f"{pokemon_data["height"]} m")
            informations[3].configure(text=f"{pokemon_data["weight"]} kg")
            informations[4].configure(text=f"{pokemon_data["types"][0]["type"]["name"]}")
            informations[5].configure(text=f"{pokemon_data["stats"][1]["base_stat"]}")
            informations[6].configure(text=f"{pokemon_data["stats"][2]["base_stat"]}")
            informations[7].configure(text=f"{pokemon_data["stats"][5]["base_stat"]}")
            informations[8].configure(text=f"{pokemon_data["stats"][0]["base_stat"]}")
            informations[9].configure(text=f"{pokemon_data["stats"][3]["base_stat"]}")
            informations[10].configure(text=f"{pokemon_data["stats"][4]["base_stat"]}")
            informations[11].configure(text=f"Capturar por P$ {pokemon_data['base_experience'] * 100}")
            return [pokemon_data["name"], pokemon_data["id"], pokemon_data["types"][0]["type"]["name"]]
        except Exception as e:
            messagebox.showerror("Error", f"Pokemon não encontrado: {e}")

    @staticmethod
    def image(file, size):
        try:
            img = CTkImage(light_image=Image.open(file), dark_image=Image.open(file), size=size)
        except FileNotFoundError:
            img = CTkImage(light_image=Image.open("assets/pokebola_pixelada.png"), dark_image=Image.open("assets/pokebola_pixelada.png"), size=size)
        return [img, file]
