import csv
from pokemon import pokemon
import random
import pygame

pygame.init()
# Définition de certaines constantes pour l'écran
largeur_ecran = 800
hauteur_ecran = 600
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
pygame.display.set_caption("Combat Pokémon")
# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Classe pour gérer l'écran de combat
class Combat:
    def __init__(self,PpokName,EpokName):
        self.fond = pygame.image.load('assets/Combat/Combat Background.png')  # Charger l'image de fond du combat
        Ijoueur = pygame.image.load(f'assets/Pokemon/Back/{PpokName}.png')  # Charger l'image du joueur
        self.joueur = pygame.transform.scale(Ijoueur,(270,270))
        Iadversaire = pygame.image.load(f'assets/Pokemon/Face/{EpokName}.png')  # Charger l'image de l'adversaire
        self.adversaire = pygame.transform.scale(Iadversaire,(270,270))
        self.position_joueur = (45, 280)  # Position du joueur
        self.position_adversaire = (470, 140)  # Position de l'adversaire
        
        #player = None
        #ennemy = None
        
        with open("pokemon_liste.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == PpokName:
                    player = pokemon(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7],row[8])
                if row[0] == EpokName:
                    ennemy = pokemon(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7],row[8])
        
        self.player = player
        self.ennemy = ennemy
        
        self.couleur_vie = (0, 255, 0)

        self.tour_joueur = True
        self.afficher_menu = True


    def afficher(self):
        ecran.blit(self.fond, (0, 0))  # Afficher le fond du combat
        ecran.blit(self.joueur, self.position_joueur)  # Afficher le joueur
        ecran.blit(self.adversaire, self.position_adversaire)  # Afficher l'adversaire
        
        # Dessiner la barre de vie du joueur
        pygame.draw.rect(ecran, self.couleur_vie, (571, 428, 168, 13))
        pygame.draw.rect(ecran, noir, (571, 428, 168, 13), 2)  # Bordure

        # Dessiner la barre de vie de l'adversaire
        pygame.draw.rect(ecran, self.couleur_vie, (131,140, 168, 12))
        pygame.draw.rect(ecran, noir, (131, 140, 168, 12), 2)  # Bordure
        

    def attaquer(self):
        if self.tour_joueur:
            self.ennemy.ppv = int(self.ennemy.ppv)
            self.ennemy.ppv -= 20
            self.tour_joueur = False
            self.afficher_menu = False

    
    def attaquer_adversaire(self):
        # Simuler une attaque de l'adversaire (pour l'exemple, cela réduit de manière aléatoire la vie du joueur)
        if int(self.player.ppv) > 0:  # Vérifier si le joueur est toujours en vie
            degats = random.randint(10, 25)  # Dégâts aléatoires pour l'attaque de l'adversaire
            self.player.ppv = int(self.ennemy.ppv)
            self.player.ppv -= degats  # Réduire les points de vie du joueur
            self.tour_joueur = True  # Passer au tour du joueur
        
    def gerer_evenements(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.afficher_menu:
                if self.bouton_attaque_pos[0] <= mouse_x <= self.bouton_attaque_pos[0] + self.bouton_attaque_pos[2] \
                        and self.bouton_attaque_pos[1] <= mouse_y <= self.bouton_attaque_pos[1] + self.bouton_attaque_pos[3]:
                    self.attaquer()


    def update(self):
        # Mettre à jour l'état du jeu
        pass  # Pour l'instant, il n'y a pas de mises à jour à faire

