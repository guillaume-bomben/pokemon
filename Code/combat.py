import json
from pokemon import pokemon
import pygame

class Combat:
    def __init__(self,PpokName,EpokName):
        self.fond = pygame.image.load('assets/Combat/Image/Combat Background.png')  
        self.joueur = pygame.transform.scale(pygame.image.load(f'assets/Pokemon/Back/{PpokName}.png'),(250,250))
        self.adversaire = pygame.transform.scale(pygame.image.load(f'assets/Pokemon/Face/{EpokName}.png') ,(250,250))
        self.position_joueur = (45, 280)
        self.position_adversaire = (470, 140)
        
        self.player = pokemon(PpokName)
        self.ennemy = pokemon(EpokName)
        
        self.vert = (0, 255, 0)
        self.blanc = (255, 255, 255)
        self.noir = (0, 0, 0)
        self.longeur_life_player = 168
        self.longeur_life_ennemy = 168

        self.ecran = pygame.display.set_mode((800, 600))

        self.tour_joueur = True
        self.font = pygame.font.Font(None, 36)
        with open(f'assets/Combat/Json atk/{PpokName}.json', 'r') as file:
            self.attacks_player = json.load(file)



    def afficher(self):
        self.ecran.blit(self.fond, (0, 0))  # Afficher le fond du combat
        self.ecran.blit(self.joueur, self.position_joueur)  # Afficher le joueur
        self.ecran.blit(self.adversaire, self.position_adversaire)  # Afficher l'adversaire
        
        # Dessiner la barre de vie du joueur
        pygame.draw.rect(self.ecran, self.vert, (571, 428, self.longeur_life_player, 13))
        pygame.draw.rect(self.ecran, self.noir, (571, 428, 168, 13), 2)  # Bordure

        # Dessiner la barre de vie de l'adversaire
        pygame.draw.rect(self.ecran, self.vert, (131,140, self.longeur_life_ennemy, 12))
        pygame.draw.rect(self.ecran, self.noir, (131, 140, 168, 12), 2)  # Bordure

    def afficher_menu(self):
        batk = pygame.image.load("assets/Combat/Image/Batk basse.png")
        batk = pygame.transform.scale(batk,(265,50))
        self.ecran.blit(batk,(85,495))
        self.ecran.blit(batk,(85,550))
        self.ecran.blit(batk,(440,495))
        self.ecran.blit(batk,(440,550))
        
        for i, attack_key in enumerate(self.attacks_player.keys()):
            attack_name = self.attacks_player[attack_key]["Name"]
            text_surface = self.font.render(attack_name, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(225 if i < 2 else 575, 520 if i % 2 == 0 else 575))
            self.ecran.blit(text_surface, text_rect)

'''    def attaquer(self):
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
                    self.attaquer()'''