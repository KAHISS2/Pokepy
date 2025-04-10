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
        main_container = self.frame(self.root, 0.01, 0.02, 0.4, 0.97, '#1b2e4d', '#b59b50', 2, 10, 'default')
        button_container = self.frame(main_container, 0.04, 0.03, 0.92, 0.3, '#1b2e4d', '#b59b50', 2, 10, 'default')

        pass

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