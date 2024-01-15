import pygame
from pygame.locals import *
from io import BytesIO
from PIL import Image

# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre
largeur, hauteur = 500, 500
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("GIF avec Pygame")

# Charger le GIF avec Pygame et Pillow
chemin_gif = "Code/umbreon.gif"
image_pillow = Image.open(chemin_gif)
frames = []
durees = []

try:
    while True:
        frame = image_pillow.convert("RGBA")
        data = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode)
        frames.append(data)
        durees.append(image_pillow.info['duration'])
        image_pillow.seek(image_pillow.tell() + 1)
except EOFError:
    pass

# Boucle principale
continuer = True
horloge = pygame.time.Clock()
index_image = 0
temps_ecoule = 0

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False

    # Ajouter le temps écoulé depuis la dernière mise à jour d'image
    temps_ecoule += horloge.get_time()

    # Si le temps écoulé est supérieur ou égal à la durée de la frame, mettre à jour l'image
    if temps_ecoule >= durees[index_image]:
        # Récupérer l'image actuelle du GIF
        image = frames[index_image]

        # Effacer l'écran
        fenetre.fill((255, 255, 255))

        # Afficher l'image
        fenetre.blit(image, (0, 0))

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Réinitialiser le temps écoulé
        temps_ecoule = 0

        # Incrémenter l'index de l'image
        index_image += 1

        # Si on atteint la dernière image, réinitialiser l'index
        if index_image == len(frames):
            index_image = 0

    # Contrôler la vitesse de la boucle principale
    horloge.tick(30)

# Quitter Pygame
pygame.quit()
