import json
import random
from pokemon import pokemon
import pygame
from AnimatedSprite import AnimatedSprite


class Combat:
    def __init__(self,PpokName,EpokName):
        clock = pygame.time.Clock()
        self.fond = pygame.image.load('assets/Combat/Image/Combat Background.png')
        self.fond_win_or_loose = pygame.image.load('assets/Combat/Image/Winner fond.png')  
        
        #Sprite adversaire
        self.adversaire = AnimatedSprite(EpokName,"Face")
        self.adversaire.rect.bottomright = (655, 325)
        
        #Sprite Joueur
        self.joueur =  AnimatedSprite(PpokName,"Back")
        self.joueur.rect.bottomleft = (125,475)
        
        with open("Code/liste_Player_Pokemon.json", "r+") as file0:
            data = json.load(file0)
            if PpokName not in data:
                data[PpokName] = {
                    "LV": 5,
                    "XP": 0
                }
                file0.seek(0)
                json.dump(data, file0, indent=2)
                file0.truncate()
                pokemon_lv = 5
                pokemon_xp = 0
            else:
                pokemon_lv = data[PpokName]["LV"]
                pokemon_xp = data[PpokName]["XP"]
        self.player = pokemon(PpokName,pokemon_lv,pokemon_xp)
        ennemy_lv = random.randint(pokemon_lv-2,pokemon_lv+2)
        self.ennemy = pokemon(EpokName,ennemy_lv)
        self.winner = None
        self.out = False
        
        self.vert = (0, 255, 0)
        self.blanc = (255, 255, 255)
        self.noir = (0, 0, 0)
        self.longeur_life_player = 168
        self.longeur_life_ennemy = 168

        self.ecran = pygame.display.set_mode((800, 600))

        self.tour_joueur = True
        self.win = False
        self.font = pygame.font.Font(None, 36)
        with open(f'assets/Pokemon/Json/{PpokName}.json', 'r') as file1:
            self.attacks_player = json.load(file1)
        with open(f'assets/Pokemon/Json/{EpokName}.json', 'r') as file2:
            self.attacks_ennemy = json.load(file2)
        with open("Code/Pokedex.json", "r+") as file3:
            self.pokedex = json.load(file3)
            self.pokedex[EpokName] = "True"
            file3.seek(0)  # Déplace le curseur au début du fichier
            json.dump(self.pokedex, file3, indent=2)  # Réécrit le fichier avec la mise à jour
            file3.truncate()  # Tronque le fichier à la position actuelle (élimine le contenu excédentaire)

        self.running = True
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            if self.win == False:
                self.gerer_evenements(events)  # Gérer les événements pour le combat
            else:
                self.fin_combat()
            pygame.display.flip() 
            clock.tick(10)  # Réglez la vitesse de l'animation en ajustant cet argument


    def afficher(self):
        self.ecran.blit(self.fond, (0, 0))  # Afficher le fond du combat
        self.joueur.update()
        self.joueur.draw(self.ecran)
        self.adversaire.update()
        self.adversaire.draw(self.ecran)
        
        pourcentage_vie_joueur = (self.player.pv / self.player.pvmax) if self.player.pvmax > 0 else 0
        self.longeur_life_player = int(168 * pourcentage_vie_joueur)
        # Dessiner la barre de vie du joueur
        pygame.draw.rect(self.ecran, self.vert, (571, 428, self.longeur_life_player, 13))
        #pygame.draw.rect(self.ecran, self.noir, (571, 428, 168, 13), 2)  # Bordure

        pourcentage_vie_ennemy = (self.ennemy.pv / self.ennemy.pvmax) if self.ennemy.pvmax > 0 else 0
        self.longeur_life_ennemy = int(168 * pourcentage_vie_ennemy)
        # Dessiner la barre de vie de l'adversaire
        pygame.draw.rect(self.ecran, self.vert, (131,140, self.longeur_life_ennemy, 12))
        #pygame.draw.rect(self.ecran, self.noir, (131, 140, 168, 12), 2)  # Bordure
        
        # afficher le nom du joueur
        joueur_name_surface = self.font.render(f"{self.player.name}", True, self.blanc)
        joueur_name_rect = joueur_name_surface.get_rect(midbottom=(600, 425))
        self.ecran.blit(joueur_name_surface, joueur_name_rect)
        # afficher le niveau du joueur
        joueur_lv_surface = self.font.render(f"{self.player.lv}", True, self.blanc)
        joueur_lv_rect = joueur_lv_surface.get_rect(midbottom=(765, 425))
        self.ecran.blit(joueur_lv_surface, joueur_lv_rect)

        # afficher le nom de l'adversaire
        adversaire_name_surface = self.font.render(f"{self.ennemy.name}", True, self.blanc)
        adversaire_name_rect = adversaire_name_surface.get_rect(midbottom=(150, 135))
        self.ecran.blit(adversaire_name_surface, adversaire_name_rect)
        # afficher le niveau de l'adversaire
        adversaire_lv_surface = self.font.render(f"{self.ennemy.lv}", True, self.blanc)
        adversaire_lv_rect = adversaire_lv_surface.get_rect(midbottom=(325, 135))
        self.ecran.blit(adversaire_lv_surface, adversaire_lv_rect)


    def afficher_menu(self, mouse_pos):
        included_keys = ["atk1", "atk2", "atk3", "atk4"]
        for i, attack_key in enumerate(included_keys):
            attack_name = self.attacks_player[attack_key]["Name"]
            attack_type = self.attacks_player[attack_key]["type"]

            # Vérifiez si la souris survole le bouton
            button_rect = pygame.Rect(85 if i < 2 else 435, 490 if i % 2 == 0 else 545, 265, 50)
            
            if button_rect.collidepoint(mouse_pos):
                # Si survolé, utilisez l'image de survol
                attack_image = pygame.image.load(f"assets/Combat/Image/Batk {attack_type}.png")
                attack_image = pygame.transform.scale(attack_image, (265, 50))
                self.ecran.blit(attack_image, (85 if i < 2 else 435, 490 if i % 2 == 0 else 545))
            else:
                # Sinon, utilisez l'image normale
                batk = pygame.image.load("assets/Combat/Image/Batk basse.png")
                batk = pygame.transform.scale(batk, (265, 50))
                self.ecran.blit(batk, (85 if i < 2 else 435, 490 if i % 2 == 0 else 545))

            # Affichez le texte
            text_surface = self.font.render(attack_name, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(225 if i < 2 else 575, 515 if i % 2 == 0 else 570))
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
            defenseur.pv -= degats * multiplicateur
            
            if defenseur.pv < 0:
                self.win = True
                if self.tour_joueur:
                    attaquant.xp_gains((175*defenseur.lv)/7)
                    with open("Code/liste_Player_Pokemon.json", "r+") as liste:
                        data = json.load(liste)
                        data[attaquant.name]["LV"] = attaquant.lv
                        data[attaquant.name]["XP"] = attaquant.xp
                        liste.seek(0)
                        json.dump(data, liste, indent=2)
                        liste.truncate()

                    print(attaquant.lv)
                    print(attaquant.xp)
                if defenseur == self.player:
                    self.winner = self.adversaire
                else:
                    self.winner = self.joueur
        else:
            print("La capaciter a rater")
        self.tour_joueur = not self.tour_joueur


    def gerer_evenements(self, events):
        self.afficher()
        mouse_pos = pygame.mouse.get_pos()
        self.afficher_menu(mouse_pos)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                rand = random.randint(1,4)
                x, y = pygame.mouse.get_pos()
                # Vérifier si les coordonnées du clic sont sur un bouton capacité
                if 85 <= x <= 350 and 495 <= y <= 545:
                    self.utiliser_capacite("atk1")
                    if not self.win:
                        self.utiliser_capacite(f"atk{rand}")
                elif 85 <= x <= 350 and 550 <= y <= 600:
                    self.utiliser_capacite("atk2")
                    if not self.win:
                        self.utiliser_capacite(f"atk{rand}")
                elif 440 <= x <= 705 and 495 <= y <= 545:
                    self.utiliser_capacite("atk3")
                    if not self.win:
                        self.utiliser_capacite(f"atk{rand}")
                elif 440 <= x <= 705 and 550 <= y <= 600:
                    self.utiliser_capacite("atk4")
                    if not self.win:
                        self.utiliser_capacite(f"atk{rand}")


    def fin_combat(self):
        self.ecran.blit(self.fond_win_or_loose,(0,0))
        self.winner.rect.midbottom = (400,350)
        self.winner.update()
        self.winner.draw(self.ecran)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.running = False