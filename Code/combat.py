import json
import random
from pokemon import pokemon
import pygame
from AnimatedSprite import AnimatedSprite

class Combat:
    def __init__(self,PpokName,EpokName):
        clock = pygame.time.Clock()
        self.fond = pygame.image.load('assets/Combat/Image/Combat Background.png')  
        #joueur_image = pygame.transform.scale(pygame.image.load(f'assets/Pokemon/Back/{PpokName}.png'),(250,250))
        #self.joueur = pygame.transform.scale(pygame.image.load(f'assets/Pokemon/Back/{PpokName}.png'),(250,250))
        #adversaire_image = pygame.transform.scale(pygame.image.load(f'assets/Pokemon/Face/{EpokName}.png') ,(250,250))
        #self.adversaire = pygame.transform.scale(pygame.image.load(f'assets/Pokemon/Face/{EpokName}.png') ,(250,250))
        
        #Sprite adversaire
        adversaire_image = pygame.transform.scale(pygame.image.load(f'Code/35063.png') ,(1375,125))
        self.adversaire = AnimatedSprite(adversaire_image,123,125)
        self.adversaire.rect.topleft = (525, 180)
        
        #Sprite Joueur
        joueur_image = pygame.transform.scale(pygame.image.load(f"Code/player.png"), (1250,1375))
        self.joueur =  AnimatedSprite(joueur_image,125,125)
        self.joueur.rect.bottomleft = (125,475)
        
        #self.position_joueur = (45, 280)
        #self.position_adversaire = (470, 140)
        
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
        with open(f'assets/Combat/Json atk/{EpokName}.json', 'r') as file2:
            self.attacks_ennemy = json.load(file2)

        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
            self.gerer_evenements(events)  # Gérer les événements pour le combat

            self.afficher()  
            self.afficher_menu()
            pygame.display.flip() 
            clock.tick(10)  # Réglez la vitesse de l'animation en ajustant cet argument


    def afficher(self):
        self.ecran.blit(self.fond, (0, 0))  # Afficher le fond du combat
        #self.ecran.blit(self.joueur, self.position_joueur)  # Afficher le joueur
        #self.ecran.blit(self.adversaire, self.position_adversaire)  # Afficher l'adversaire
        self.joueur.update()
        self.joueur.draw(self.ecran)
        self.adversaire.update()
        self.adversaire.draw(self.ecran)
        
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
        if self.tour_joueur :
            power_capacite = self.attacks_player[capacite_key]["power"]
            capacite_type = self.attacks_player[capacite_key]["tcap"]
            precision = self.attacks_player[capacite_key]["precision"]
            atk_type = self.attacks_player[capacite_key]["type"]
            
            attaquant = self.player
            defenseur = self.ennemy
        else:
            power_capacite = self.attacks_ennemy[capacite_key]["power"]
            capacite_type = self.attacks_ennemy[capacite_key]["tcap"]
            precision = self.attacks_ennemy[capacite_key]["precision"]
            atk_type = self.attacks_ennemy[capacite_key]["type"]
            
            attaquant = self.ennemy
            defenseur = self.player

        if precision >= random.randint(0,100):
            if capacite_type == "physique":
                degats = int((((((attaquant.lv * 0.4 + 2) * attaquant.attaque * power_capacite) / defenseur.defense) / 50) + 2))
            elif capacite_type == "special":
                degats = int((((((attaquant.lv * 0.4 + 2) *attaquant.attaque_special * power_capacite) / defenseur.defence_special) / 50) + 2))
            
            with open(f"assets/Combat/Json res/{atk_type}.json") as f:
                file = json.load(f)
                multiplicateur = file[defenseur.type1] * file[defenseur.type2]
                print(f"multiplicateur : {multiplicateur}")
            defenseur.pv -= degats * multiplicateur
            # Limiter la vie minimale à 0
            if defenseur.pv < 0:
                defenseur.pv = 0
            print(f"{degats * multiplicateur}")
        else:
            print("La capaciter a rater")
        self.tour_joueur = not self.tour_joueur


    def gerer_evenements(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                rand = random.randint(1,4)
                x, y = pygame.mouse.get_pos()
                # Vérifier si les coordonnées du clic sont sur un bouton capacité
                if 85 <= x <= 350 and 495 <= y <= 545:
                    self.utiliser_capacite("atk1")
                    self.utiliser_capacite(f"atk{rand}")
                    print("cap 1")
                elif 85 <= x <= 350 and 550 <= y <= 600:
                    self.utiliser_capacite("atk2")
                    self.utiliser_capacite(f"atk{rand}")
                    print("cap 2")
                elif 440 <= x <= 705 and 495 <= y <= 545:
                    self.utiliser_capacite("atk3")
                    print("cap 3")
                elif 440 <= x <= 705 and 550 <= y <= 600:
                    self.utiliser_capacite("atk4")
                    self.utiliser_capacite(f"atk{rand}")
                    print("cap 4")
    
    #def win(self):
        
