import pygame 

from choixPokemon import choixPokemon
from pokedex import pokedex
from addpokemon import addpokemon

pygame.mixer.init()

class Menu:
    def __init__(self):
        #Initialisation des composants du menu
        self.background = pygame.image.load("assets/Menu/Background menu.png")
        self.m2 = pygame.image.load("assets/Menu/bmenu.png")
        self.m2_size = (220, 40)
        #Image agrandie pour l'effet de survol de la souris 
        self.m2_hover = pygame.transform.scale(self.m2, (int(self.m2_size[0]*1.2), int(self.m2_size[1]*1.2)))  # Image agrandie pour la souris

        #Chargement et réglage du volume de la musique 
        pygame.mixer.music.load("assets/remix.mp3")
        pygame.mixer.music.set_volume(0.1)

        #Configuration de l'écran et de la police
        self.ecran = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font(None, 36)
        self.is_hovered = [False, False, False]  # Un tableau pour stocker l'état de survol des images
      
        #Boucle principale du menu 
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEMOTION:
                    self.gerer_survol(event.pos) #Gestion du survol des boutons 
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.gerer_clic(event.pos) #Gestion des clics sur les boutons 
            self.afficher() #Affichage du menu 
            pygame.display.flip()

        pygame.quit()
        
        
    def gerer_survol(self, mouse_pos):
        # Affichage du fond et des boutons 
        for i in range(3):
            image_rect = self.m2.get_rect(center=(400, 300 + i * 100))
            self.is_hovered[i] = image_rect.collidepoint(mouse_pos)

    def afficher(self):
        self.ecran.blit(self.background, (0, 0))

        for i in range(3):
            if self.is_hovered[i]:
                self.ecran.blit(self.m2_hover, self.m2_hover.get_rect(center=(400, 300 + i * 100)))
            else:
                self.ecran.blit(self.m2, self.m2.get_rect(center=(400, 300 + i * 100)))

        #Affichage du texte des boutons 
        b1 = self.font.render("Jouer", True, (255, 255, 255))
        b1_pos = b1.get_rect(center=(400, 300))
        self.ecran.blit(b1, b1_pos)

        b2 = self.font.render("Add Pokemon", True, (255, 255, 255))
        b2_pos = b2.get_rect(center=(400, 400))
        self.ecran.blit(b2, b2_pos)

        b3 = self.font.render("Pokedex", True, (255, 255, 255))
        b3_pos = b3.get_rect(center=(400, 500))
        self.ecran.blit(b3, b3_pos)

    def gerer_clic(self, mouse_pos):
        #Gestion des clics sur les boutons 
        b1_rect = pygame.Rect(400 - 110, 300 - 18, 220, 36)
        b2_rect = pygame.Rect(400 - 110, 400 - 18, 220, 36)  # Bouton Add Pokemon
        b3_rect = pygame.Rect(400 - 110, 500 - 18, 220, 36)  # Bouton Pokedex
        
        if b1_rect.collidepoint(mouse_pos):
            self.lancer_jeu()
        elif b2_rect.collidepoint(mouse_pos):
            self.lancer_addPokemon()
        elif b3_rect.collidepoint(mouse_pos):
            self.lancer_pokedex()

    def lancer_jeu(self):
        #Lancement du jeu 
        pygame.mixer.music.play(-1)
        choix = choixPokemon()

    def lancer_pokedex(self):
        #Lancement du pokédex
        pdex = pokedex()
    
    def lancer_addPokemon(self):
        #Lancement de l'interface d'ajout de Pokemon 
        add = addpokemon()
        add.run()