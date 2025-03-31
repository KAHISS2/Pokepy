from UIComponents import *
from PIL import Image

class Interface:
    def __init__(self):
        self.root = CTk()
        self.root.title("Interface")
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")
        self.loadContents()
        self.root.mainloop()

    def loadContents(self):
        self.pointsContainer()
        self.pokedexContainer()
        pass

    def pointsContainer(self):
        # container ===========================================================
        main_container = UIComponents.frame(self.root, 0.01, 0.02, 0.4, 0.97, 'black', '#b59b50', 2, 10, 'default')
        button_container = UIComponents.frame(main_container, 0.04, 0.03, 0.92, 0.3, 'black', '#b59b50', 2, 10, 'default')

        pass

    def pokedexContainer(self):
        # container ===========================================================
        main_container = UIComponents.frame(self.root, 0.42, 0.02, 0.57, 0.97, '#e04136', '#a30000', 4, 10, 'default')
        screen_container = UIComponents.frame(main_container, 0.05, 0.07, 0.9, 0.4, '#f0f0f0', '#b8b8b8', 4, 10, 'default')
        scene_container = UIComponents.frame(screen_container, 0.05, 0.10, 0.42, 0.79, '#43b7fa', '#b8b8b8', 4, 0, 'default')

        # images ==============================================================
        self.pokemon_image = UIComponents.labels(scene_container, "", 0.13, 0.02, 0.8, 0.96, '#4327fa', '#43b7fa', photo=self.image('assets/pikachu.png', (218, 218))[0])

        # labels ==============================================================
        pokemon_name = UIComponents.labels(screen_container, "Pikachu Nº 0025", 0.54, 0.04, 0.38, 0.09, 'black', '#f0f0f0')
    
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