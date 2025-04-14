import pygame

class Sound:
    def __init__(self):
        pygame.mixer.init()
        self.pause_music = False
        

    def musicBackground(self, sound_path):
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.05)

    def soundClick(self, sound_path):
        sound_click = pygame.mixer.Sound(sound_path)
        sound_click.set_volume(0.1)
        sound_click.play()

    def soundPause(self):
        if self.pause_music:
            pygame.mixer.music.unpause()
            self.pause_music = False
        else:
            pygame.mixer.music.pause()
            self.pause_music = True