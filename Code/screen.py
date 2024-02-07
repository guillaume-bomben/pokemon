import pygame

class Screen:
    def __init__(self):
        #Initialisation de l'écran du jeu 
        self.display = pygame.display.set_mode((800, 600)) #Création de la fenêtre de jeu 
        pygame.display.set_caption("Pokémon") # Titre de la fenêtre 
        self.clock = pygame.time.Clock() #Horloge pour contrôler le taux de rafraîchissement
        self.framerate = 144 #Fréquence d'images par seconde
        self.deltatime: float = 0.0 #Temps écoulé entre chaque frame

    def update(self):
        #Mise à jour de l'écran 
        pygame.display.flip() #Met à jour la totalité de l'écran
        pygame.display.update() #Met à jour une partie de l'écran
        self.clock.tick(self.framerate) #Limite le framerate
        self.display.fill((0, 0, 0)) #Efface l'écran avec du noir
        self.deltatime = self.clock.get_time() #Récupère le temps écoulé depuis la dernière mise à jour

    def get_delta_time(self):
        #Renvoie le temps écoulé entre chaque mise à jour
        return self.deltatime

    def get_size(self):
        #Renvoie les dimensions de l'écran
        return self.display.get_size()

    def get_display(self):
        #Renvoie l'objet d'affichage de pygame
        return self.display
    
