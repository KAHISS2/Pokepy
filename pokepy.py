from src.gui.UIComponents import *
from src.services.clicker import Clicker
from src.services.api_conection import ApiConnection
from src.services.sound import Sound
from PIL import Image
from random import randint
from src.repository.databaseConnection import DataBase
from src.repository.query import *

class App(UIComponents):
    def __init__(self):
        # init app ============================================================
        self.clicker = Clicker(100000, 1, 0, 15, 100, 0, 1)
        self.api = ApiConnection("https://pokeapi.co/api/v2/pokemon/")
        self.sound = Sound()
        self.database = DataBase("database/pokedex.db")
        self.sound.musicBackground("assets/sounds/background.mp3")
        self.loadWindow()
        self.clicker.init([
            self.points,
            self.points_per_second_label,
            self.points_per_click_label,
            self.buy_level_up_click,
            self.buy_level_up_auto_click
        ])
        self.clicker.autoClick(self.root, self.points)
        super().__init__()
        self.root.mainloop()

    def loadWindow(self):
        # window config ========================================================
        self.root = CTk()
        self.root.title("Pokepy")
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")
        self.labels(self.root, "", 0, 0, 1, 1, '#1b2e4d', '#1b2e4d', photo=self.image("assets/images/scene.jpg", (self.root.winfo_screenwidth(), self.root.winfo_screenheight()))[0])

        # main content =======================================================
        self.pointsContainer()
        self.pokedexContainer()
        pass

    def pointsContainer(self):
        # container ===========================================================
        main_container = self.frame(self.root, 0.01, 0.02, 0.4, 0.97, '#1b2e4d', '#ffff00', 2, 10, 'default')
        button_container = self.frame(main_container, 0.04, 0.03, 0.92, 0.7, '#1b2e4d', '#ffff00', 2, 10, 'default')
        search_container = self.frame(main_container, 0.04, 0.75, 0.92, 0.2, '#1b2e4d', '#1b2e4d', 2, 10, 'default')

        # labels =============================================================
        points_label = self.labels(button_container, "PokeDollars(P$):", 0.01, 0.02, 0.98, 0.09, '#ffff00', '#1b2e4d')
        self.points = self.labels(button_container, "", 0.01, 0.1, 0.98, 0.09, '#ffff00', '#1b2e4d', size=23)
        self.points_per_second_label = self.labels(button_container, "", 0.01, 0.19, 0.98, 0.04, '#bfaf00', '#1b2e4d', size=18)
        self.points_per_click_label = self.labels(button_container, "", 0.01, 0.25, 0.98, 0.04, '#bfaf00', '#1b2e4d', size=18)
        self.buy_level_up_click = self.button(
            button_container, "", 0.2, 0.75, 0.6, 0.09, background="#1b2e4d", color="#ffff00", hover_cursor="#8f8a01",
            function=lambda: [
                self.clicker.buy_click([self.points, self.points_per_click_label], self.buy_level_up_click),
                self.sound.soundClick("assets/sounds/click.wav")
            ]
        )
        self.buy_level_up_auto_click = self.button(
            button_container, "", 0.2, 0.87, 0.6, 0.09, background="#1b2e4d", color="#ffff00", hover_cursor="#8f8a01",
            function=lambda: [
                self.clicker.buy_auto_clicker([self.points, self.points_per_second_label], self.buy_level_up_auto_click),
                self.sound.soundClick("assets/sounds/click.wav")
            ]
        )

        # entry ==============================================================
        self.name_field = self.entry(search_container, 0.15, 0.19, 0.7, 0.3, type_entry='entry', position=CENTER, background="#233b63", border_color="#ffff00")

        # buttons ============================================================
        increment_button = self.button(button_container, '', 0.36, 0.34, 0.3, 0.3, background="#1b2e4d", color="#ffff00", hover_cursor="#1b2e4d", photo=self.image('assets/images/pokebola.png', (120, 120))[0], type_btn='buttonPhoto', function=lambda : [self.clicker.increment(self.points), self.sound.soundClick("assets/sounds/click2.wav")])
        search_button = self.button(
            search_container, 'Buscar', 0.16, 0.55, 0.33, 0.3, background="#1b2e4d", color="#ffff00", hover_cursor="#8f8a01",
            function=lambda: [
                self.sound.soundClick("assets/sounds/click.wav"),
                self.api.updateDisplay(
                    self.name_field.get(),
                    [
                        self.pokemon_image,
                        self.pokemon_name,
                        self.pokemon_height,
                        self.pokemon_weight,
                        self.pokemon_type,
                        self.pokemon_attack,
                        self.pokemon_defense,
                        self.pokemon_speed,
                        self.pokemon_hp,
                        self.pokemon_special_attack,
                        self.pokemon_special_defense,
                        self.buy_button
                    ]
                )
            ]
        )
        random_button = self.button(
            search_container, 'Random', 0.51, 0.55, 0.33, 0.3, background="#1b2e4d", color="#ffff00", hover_cursor="#8f8a01", 
            function=lambda: [
                self.sound.soundClick("assets/sounds/click.wav"),
                self.api.updateDisplay(
                    str(randint(1, 1000)),
                    [
                        self.pokemon_image,
                        self.pokemon_name,
                        self.pokemon_height,
                        self.pokemon_weight,
                        self.pokemon_type,
                        self.pokemon_attack,
                        self.pokemon_defense,
                        self.pokemon_speed,
                        self.pokemon_hp,
                        self.pokemon_special_attack,
                        self.pokemon_special_defense,
                        self.buy_button
                    ]
                )
            ]
        )
        pause_button = self.button(
            main_container, '', 0.01, 0.92, 0.1, 0.06, background="#1b2e4d", color="#ffff00", hover_cursor="#8f8a01", photo=self.image('assets/images/som_ativo.png', (30, 30))[0], type_btn='buttonPhoto',
            function=lambda: [
                self.sound.soundPause(),
                self.sound.soundClick("assets/sounds/click.wav")
            ]
        )


    def pokedexContainer(self):
        # container ===========================================================
        main_container = self.frame(self.root, 0.42, 0.02, 0.57, 0.97, '#e04136', '#a30000', 4, 10, 'default')
        screen_container = self.frame(main_container, 0.05, 0.05, 0.9, 0.4, '#f0f0f0', '#b8b8b8', 4, 10, 'default')
        scene_container = self.frame(screen_container, 0.05, 0.10, 0.42, 0.79, '#00779c', '#b8b8b8', 4, 0, 'default')
        list_container = self.frame(main_container, 0.05, 0.48, 0.9, 0.485, '#43b7fa', '#b8b8b8', 4, 10, 'default')

        # images ==============================================================
        self.pokemon_image = self.labels(scene_container, "", 0.09, 0.02, 0.8, 0.96, '#00779c', '#00779c', photo=self.image("assets/images/pokebola_pixelada.png", (245, 245))[0])

        # fixed labels ==============================================================
        hight_label = self.labels(screen_container, "Hight", 0.50, 0.2, 0.1, 0.09, 'black', '#f0f0f0')
        weight_label = self.labels(screen_container, "Weight", 0.68, 0.2, 0.1, 0.09, 'black', '#f0f0f0')
        type_label = self.labels(screen_container, "Type", 0.85, 0.2, 0.1, 0.09, 'black', '#f0f0f0')
        attack_label = self.labels(screen_container, "Attack", 0.495, 0.39, 0.11, 0.09, 'black', '#f0f0f0')
        defense_label = self.labels(screen_container, "Defense", 0.67, 0.39, 0.12, 0.09, 'black', '#f0f0f0')
        speed_label = self.labels(screen_container, "Speed", 0.85, 0.39, 0.1, 0.09, 'black', '#f0f0f0')
        hp_label = self.labels(screen_container, "HP", 0.495, 0.58, 0.11, 0.09, 'black', '#f0f0f0')
        special_attack_label = self.labels(screen_container, "S/Attack", 0.67, 0.58, 0.12, 0.09, 'black', '#f0f0f0')
        special_defense_label = self.labels(screen_container, "S/Defense", 0.82, 0.58, 0.15, 0.09, 'black', '#f0f0f0')

        # Changed labels ==============================================================
        self.pokemon_name = self.labels(screen_container, "--------", 0.53, 0.04, 0.42, 0.09, 'gray', '#f0f0f0')
        self.pokemon_height = self.labels(screen_container, "---- m", 0.475, 0.29, 0.15, 0.07, 'gray', '#f0f0f0', size=18)
        self.pokemon_weight = self.labels(screen_container, "---- kg", 0.655, 0.29, 0.15, 0.07, 'gray', '#f0f0f0', size=18)
        self.pokemon_type = self.labels(screen_container, "-----", 0.825, 0.29, 0.15, 0.07, 'gray', '#f0f0f0', size=18)
        self.pokemon_attack = self.labels(screen_container, "---", 0.475, 0.48, 0.15, 0.07, 'gray', '#f0f0f0', size=18)
        self.pokemon_defense = self.labels(screen_container, "---", 0.655, 0.48, 0.15, 0.07, 'gray', '#f0f0f0', size=18)
        self.pokemon_speed = self.labels(screen_container, "---", 0.825, 0.48, 0.15, 0.07, 'gray', '#f0f0f0', size=18)
        self.pokemon_hp = self.labels(screen_container, "---", 0.475, 0.67, 0.15, 0.07, 'gray', '#f0f0f0', size=18)
        self.pokemon_special_attack = self.labels(screen_container, "---", 0.655, 0.67, 0.15, 0.07, 'gray', '#f0f0f0', size=18)
        self.pokemon_special_defense = self.labels(screen_container, "---", 0.825, 0.67, 0.15, 0.07, 'gray', '#f0f0f0', size=18)

        # buttons ==============================================================
        self.buy_button = self.button(
            screen_container, "Capturar por P$", 0.51, 0.78, 0.45, 0.16, background="#e04136", color="#fff", hover_cursor="#333", border_color="#a30000", 
            function=lambda: [
                    self.clicker.buyPokemon(self.points, self.buy_button),
                    self.database.insertPokemonToDatabase(
                        registerPokemon.format(
                            self.pokemon_name.cget("text").split(" ")[0],
                            int(self.pokemon_name.cget("text").split(" ")[-1]),
                            self.pokemon_type.cget("text")
                        ),
                    ),
                    self.database.searchPerPokemons(searchPokemon, self.treeview),
                ]
            )

        # treeview ==============================================================
        self.treeview = self.treeview(list_container, ["Name", "Number", "Type"])

        # search pokemon ==============================================================
        self.database.searchPerPokemons(searchPokemon, self.treeview)

if __name__ == "__main__":
    App()