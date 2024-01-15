import pygame
from pygame.locals import *
from io import BytesIO
from PIL import Image

class GifPlayer:
    def __init__(self, chemin_gif,windows):
        pygame.init()
        self.fenetre = windows
        self.image_pillow = Image.open(chemin_gif)
        self.frames = []
        self.durees = []
        self.index_image = 0
        self.temps_ecoule = 0
        self.initialiser_gif()

    def initialiser_gif(self):
        try:
            while True:
                frame = self.image_pillow.convert("RGBA")
                data = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode)
                self.frames.append(data)
                self.durees.append(self.image_pillow.info['duration'])
                self.image_pillow.seek(self.image_pillow.tell() + 1)
        except EOFError:
            pass

    def afficher_image(self):
        image = self.frames[self.index_image]
        #self.fenetre.fill((255, 255, 255))
        self.fenetre.blit(image, (0, 0))
        pygame.display.flip()

    def jouer_gif(self):
        continuer = True
        horloge = pygame.time.Clock()

        while continuer:
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = False

            self.temps_ecoule += horloge.get_time()

            if self.temps_ecoule >= self.durees[self.index_image]:
                self.afficher_image()
                self.temps_ecoule = 0
                self.index_image += 1

                if self.index_image == len(self.frames):
                    self.index_image = 0

            horloge.tick(30)

        pygame.quit()


'''largeur, hauteur = 500, 500
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("GIF avec Pygame")
# Exemple d'utilisation :
chemin_gif = "Code/umbreon.gif"
lecteur_gif = GifPlayer(chemin_gif,fenetre)
lecteur_gif.jouer_gif()'''
