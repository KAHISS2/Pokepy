import customtkinter as ctk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Função para obter o sprite do Pokémon
def get_pokemon_sprite(name):
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        sprite_url = data['sprites']['front_default']

        if sprite_url:
            img_response = requests.get(sprite_url)
            img_data = BytesIO(img_response.content)
            img = Image.open(img_data).resize((80, 80))

            return ImageTk.PhotoImage(img)
        else:
            return None
    except Exception as e:
        print(f"Erro ao obter sprite de {name}: {e}")
        return None

# Função para criar o grid de botões com imagens e nomes
def criar_grid_pokemons():
    try:
        # Obter a lista de Pokémons da API
        response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=56")
        response.raise_for_status()
        data = response.json()
        pokemons = data['results']

        # Criar botões dinamicamente
        for i, pokemon in enumerate(pokemons):
            nome = pokemon['name'].capitalize()
            img_tk = get_pokemon_sprite(pokemon['name'])

            if img_tk:
                # Botão com imagem e nome
                botao = ctk.CTkButton(
                    scroll_frame,
                    text=nome,
                    image=img_tk,
                    compound="top",
                    width=100,
                    height=100,
                    command=lambda: print(f"Você clicou em {pokemon["name"]}")
                )
                botao.image = img_tk  # Manter referência para não ser coletado
                botao.grid(row=i // 5, column=i % 5, padx=5, pady=5)
    except Exception as e:
        print(f"Erro ao criar o grid: {e}")

# Configuração da interface CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Pokédex")
root.geometry("600x600")

# Scrollable Frame para os botões
scroll_frame = ctk.CTkScrollableFrame(root, width=500, height=500)
scroll_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Chamar a função para criar o grid
criar_grid_pokemons()

root.mainloop()
