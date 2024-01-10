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
        #self.fond = pygame.image.load('fond combat.jpg')  # Charger l'image de fond du combat
        self.joueur = pygame.image.load('player.png')  # Charger l'image du joueur
        self.adversaire = pygame.image.load('ennemy.png')  # Charger l'image de l'adversaire
        self.position_joueur = (200, 300)  # Position du joueur
        self.position_adversaire = (550, 100)  # Position de l'adversaire
        
        with open("pokemon_liste.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == PpokName:
                    player = pokemon(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7],row[8])
                if row[0] == EpokName:
                    ennemy = pokemon(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7],row[8])
        
        self.couleur_vie = (0, 255, 0)

        self.tour_joueur = True
        self.afficher_menu = True

        self.menu_pos_x = 200
        self.menu_pos_y = 500
        self.menu_largeur = 400
        self.menu_hauteur = 80

        self.bouton_attaque_pos = (self.menu_pos_x + 20, self.menu_pos_y + 20, 100, 40)
        self.bouton_1_pos = (self.menu_pos_x + 20, self.menu_pos_y + 20, 100, 40)
        self.bouton_2_pos = (self.menu_pos_x + 140, self.menu_pos_y + 20, 100, 40)
        self.bouton_3_pos = (self.menu_pos_x + 260, self.menu_pos_y + 20, 100, 40)
        self.bouton_4_pos = (self.menu_pos_x + 380, self.menu_pos_y + 20, 100, 40)


    def afficher(self):
        #ecran.blit(self.fond, (0, 0))  # Afficher le fond du combat
        ecran.blit(self.joueur, self.position_joueur)  # Afficher le joueur
        ecran.blit(self.adversaire, self.position_adversaire)  # Afficher l'adversaire
        
        # Dessiner la barre de vie du joueur
        pygame.draw.rect(ecran, self.couleur_vie, (self.position_joueur[0], self.position_joueur[1] - 20, self.vie_joueur, 10))
        pygame.draw.rect(ecran, noir, (self.position_joueur[0], self.position_joueur[1] - 20, 100, 10), 2)  # Bordure

        # Dessiner la barre de vie de l'adversaire
        pygame.draw.rect(ecran, self.couleur_vie, (self.position_adversaire[0], self.position_adversaire[1] - 20, self.vie_adversaire, 10))
        pygame.draw.rect(ecran, noir, (self.position_adversaire[0], self.position_adversaire[1] - 20, 100, 10), 2)  # Bordure
        
        if self.afficher_menu:
            pygame.draw.rect(ecran, noir, self.bouton_attaque_pos)
            font = pygame.font.SysFont(None, 30)
            text_attaque = font.render("Attaquer", True, noir)
            ecran.blit(text_attaque, (self.bouton_attaque_pos[0] + 10, self.bouton_attaque_pos[1] + 10))
        else:
            pygame.draw.rect(ecran, noir, self.bouton_1_pos)
            pygame.draw.rect(ecran, noir, self.bouton_2_pos)
            pygame.draw.rect(ecran, noir, self.bouton_3_pos)
            pygame.draw.rect(ecran, noir, self.bouton_4_pos)

    def attaquer(self):
        '''
        if self.tour_joueur:
            self.vie_adversaire -= 20  # Réduire les points de vie de l'adversaire lors de l'attaque du joueur
            self.tour_joueur = False  # Passer au tour de l'adversaire
            self.attaquer_adversaire()
        '''
        if self.tour_joueur:
            self.vie_adversaire -= 20
            self.tour_joueur = False
            self.afficher_menu = False

    
    def attaquer_adversaire(self):
        # Simuler une attaque de l'adversaire (pour l'exemple, cela réduit de manière aléatoire la vie du joueur)
        if self.vie_joueur > 0:  # Vérifier si le joueur est toujours en vie
            degats = random.randint(10, 25)  # Dégâts aléatoires pour l'attaque de l'adversaire
            self.vie_joueur -= degats  # Réduire les points de vie du joueur
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

