from UIComponents import *
from PIL import Image

class Interface(UIComponents):
    def __init__(self):
        self.root = CTk()
        self.root.title("Interface")
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")
        self.loadContents()
        super().__init__()
        self.root.mainloop()

    def loadContents(self):
        self.pointsContainer()
        self.pokedexContainer()
        pass

    def pointsContainer(self):
        # container ===========================================================
        main_container = self.frame(self.root, 0.01, 0.02, 0.4, 0.97, '#1b2e4d', '#ffff00', 2, 10, 'default')
        button_container = self.frame(main_container, 0.04, 0.03, 0.92, 0.7, '#1b2e4d', '#ffff00', 2, 10, 'default')
        search_container = self.frame(main_container, 0.04, 0.75, 0.92, 0.2, '#1b2e4d', '#1b2e4d', 2, 10, 'default')

        # labels =============================================================
        points_label = self.labels(button_container, "Pontos:", 0.01, 0.02, 0.98, 0.09, '#ffff00', '#1b2e4d')
        self.points = self.labels(button_container, "1", 0.01, 0.1, 0.98, 0.09, '#ffff00', '#1b2e4d', size=29)
        level_click = self.labels(button_container, "1 ponto por click", 0.01, 0.8, 0.98, 0.09, '#ffff00', '#1b2e4d')

        # entry ==============================================================
        self.name_field = self.entry(search_container, 0.15, 0.19, 0.7, 0.3, type_entry='entry', position=CENTER, background="#233b63", border_color="#ffff00")

        # buttons ============================================================
        increment_button = self.button(button_container, '', 0.36, 0.34, 0.3, 0.3, background="#1b2e4d", color="#ffff00", hover_cursor="#1b2e4d", photo=self.image('assets/pokebola.png', (120, 120))[0], type_btn='buttonPhoto')
        search_button = self.button(search_container, 'Buscar', 0.16, 0.55, 0.33, 0.3, background="#1b2e4d", color="#ffff00", hover_cursor="#8f8a01")
        random_button = self.button(search_container, 'Random', 0.51, 0.55, 0.33, 0.3, background="#1b2e4d", color="#ffff00", hover_cursor="#8f8a01")

    def pokedexContainer(self):
        # container ===========================================================
        main_container = self.frame(self.root, 0.42, 0.02, 0.57, 0.97, '#e04136', '#a30000', 4, 10, 'default')
        screen_container = self.frame(main_container, 0.05, 0.05, 0.9, 0.4, '#f0f0f0', '#b8b8b8', 4, 10, 'default')
        scene_container = self.frame(screen_container, 0.05, 0.10, 0.42, 0.79, '#43b7fa', '#b8b8b8', 4, 0, 'default')
        list_container = self.frame(main_container, 0.05, 0.48, 0.9, 0.485, '#43b7fa', '#b8b8b8', 4, 10, 'default')

        # images ==============================================================
        self.pokemon_image = self.labels(scene_container, "", 0.13, 0.02, 0.8, 0.96, '#4327fa', '#43b7fa', photo=self.image('assets/pikachu.png', (208, 208))[0])

        # fixed labels ==============================================================
        hight_label = self.labels(screen_container, "Hight", 0.50, 0.2, 0.1, 0.09, 'black', '#f0f0f0')
        weight_label = self.labels(screen_container, "Weight", 0.68, 0.2, 0.1, 0.09, 'black', '#f0f0f0')
        type_label = self.labels(screen_container, "Type", 0.85, 0.2, 0.1, 0.09, 'black', '#f0f0f0')
        attack_label = self.labels(screen_container, "Attack", 0.495, 0.39, 0.11, 0.09, 'black', '#f0f0f0')
        defense_label = self.labels(screen_container, "Defense", 0.67, 0.39, 0.12, 0.09, 'black', '#f0f0f0')
        speed_label = self.labels(screen_container, "Speed", 0.85, 0.39, 0.1, 0.09, 'black', '#f0f0f0')

        # Changed labels ==============================================================
        self.pokemon_name = self.labels(screen_container, "Pikachu Nº 0025", 0.535, 0.04, 0.38, 0.09, 'gray', '#f0f0f0')
        self.pokemon_hight = self.labels(screen_container, "0.4 m", 0.475, 0.29, 0.15, 0.05, 'gray', '#f0f0f0', size=18)
        self.pokemon_weight = self.labels(screen_container, "6.0 kg", 0.655, 0.29, 0.15, 0.05, 'gray', '#f0f0f0', size=18)
        self.pokemon_type = self.labels(screen_container, "Elétrico", 0.825, 0.29, 0.15, 0.05, 'gray', '#f0f0f0', size=18)
        self.pokemon_attack = self.labels(screen_container, "55", 0.475, 0.48, 0.15, 0.05, 'gray', '#f0f0f0', size=18)
        self.pokemon_defense = self.labels(screen_container, "40", 0.655, 0.48, 0.15, 0.05, 'gray', '#f0f0f0', size=18)
        self.pokemon_speed = self.labels(screen_container, "90", 0.825, 0.48, 0.15, 0.05, 'gray', '#f0f0f0', size=18)

        # evolution ==============================================================
        evolution_label = self.labels(screen_container, "Evolutions", 0.56, 0.55, 0.34, 0.05, 'black', '#f0f0f0')
        self.first_evolution = self.labels(screen_container, "", 0.475, 0.62, 0.16, 0.3, '#f0f0f0', '#f0f0f0', photo=self.image('assets/pikachu.png', (60, 60))[0])
        self.second_evolution = self.labels(screen_container, "", 0.655, 0.62, 0.16, 0.3, '#f0f0f0', '#f0f0f0', photo=self.image('assets/pikachu.png', (60, 60))[0])
        self.third_evolution = self.labels(screen_container, "", 0.825, 0.62, 0.16, 0.3, '#f0f0f0', '#f0f0f0', photo=self.image('assets/pikachu.png', (60, 60))[0])
        self.first_evolution_label = self.labels(screen_container, "Pikachu", 0.475, 0.9, 0.16, 0.08, 'black', '#f0f0f0', size=14)
        self.second_evolution_label = self.labels(screen_container, "Raichu", 0.655, 0.9, 0.16, 0.08, 'black', '#f0f0f0', size=14)
        self.third_evolution_label = self.labels(screen_container, "Raichu", 0.825, 0.9, 0.16, 0.08, 'black', '#f0f0f0', size=14)

        # treeview ==============================================================
        self.treeview = self.treeview(list_container, ["Name", "Number", "Type"])
    
    @staticmethod
    def image(file, size):
        try:
            img = CTkImage(light_image=Image.open(file), dark_image=Image.open(file), size=size)
        except FileNotFoundError:
            img = CTkImage(light_image=Image.open('assets/corrupted.png'), dark_image=Image.open('assets/corrupted.png'), size=(76, 76))
        return [img, file]

        pass
if __name__ == "__main__":
    Interface()