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
        
        pourcentage_vie_joueur = (self.player.pv / self.player.pvmax) if self.player.pvmax > 0 else 0
        self.longeur_life_player = int(168 * pourcentage_vie_joueur)
        # Dessiner la barre de vie du joueur
        pygame.draw.rect(self.ecran, self.vert, (571, 428, self.longeur_life_player, 13))
        pygame.draw.rect(self.ecran, self.noir, (571, 428, 168, 13), 2)  # Bordure

        pourcentage_vie_ennemy = (self.ennemy.pv / self.ennemy.pvmax) if self.ennemy.pvmax > 0 else 0
        self.longeur_life_ennemy = int(168 * pourcentage_vie_ennemy)
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


    def utiliser_capacite(self, capacite_key):
        power_capacite = self.attacks_player[capacite_key]["power"]
        capacite_type = self.attacks_player[capacite_key]["tcap"]
        if self.tour_joueur:
            attaquant = self.player
            defenseur = self.ennemy
        else:
            attaquant = self.ennemy
            defenseur = self.player
        if capacite_type == "physique":
            degats = int((((((attaquant.lv * 0.4 + 2) * attaquant.attaque * power_capacite) / defenseur.defense) / 50) + 2))
        elif capacite_type == "special":
            degats = int((((((attaquant.lv * 0.4 + 2) * attaquant.attaque_special * power_capacite) / defenseur.defence_special) / 50) + 2))
            
        defenseur.pv -= degats
        # Limiter la vie minimale à 0
        if defenseur.pv < 0:
            defenseur.pv = 0
        print(f"{degats}")
        # Inverser le tour
        #self.tour_joueur = not self.tour_joueur
    
    def gerer_evenements(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Vérifier si les coordonnées du clic sont sur un bouton capacité
                if 85 <= x <= 350 and 495 <= y <= 545:
                    self.utiliser_capacite("atk1")
                    print("cap 1")
                elif 85 <= x <= 350 and 550 <= y <= 600:
                    self.utiliser_capacite("atk2")
                    print("cap 2")
                elif 440 <= x <= 705 and 495 <= y <= 545:
                    self.utiliser_capacite("atk3")
                    print("cap 3")
                elif 440 <= x <= 705 and 550 <= y <= 600:
                    self.utiliser_capacite("atk4")
                    print("cap 4")
