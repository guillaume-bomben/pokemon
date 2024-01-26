import pygame
import json
from AnimatedSprite import AnimatedSprite


class pokedex:
    def __init__(self):
        clock = pygame.time.Clock()
        self.ecran = pygame.display.set_mode((800, 600))
        self.fond = pygame.image.load("assets/Menu/Pokedex.png")
        self.font = pygame.font.Font(None, 32)
        self.current_pokemon = "Bulbizarre" 
        
        self.pok = []
        self.rencontre = 0
        with open("assets/pokedex.json","r") as file:
            data = json.load(file)
            for pokemon in data.keys():
                if data[pokemon] == "True":
                    self.rencontre += 1
                    self.pok.append(pokemon)
                else:
                    self.pok.append("unknown")
                self.index_affichage = 5
        self.l_affichage = []
        self.index_page = 1
        self.apok = AnimatedSprite(self.current_pokemon,"Face")
        self.apok.rect.center = (175, 175)
        
        self.running = True
        while self.running:
            self.afficher()
            self.gerer_evenements()
            self.afficher_caracteristiques(self.current_pokemon)
            pygame.display.flip()
            clock.tick(10)


    def gerer_evenements(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Vérifier si le clic est dans la zone du bouton
                x, y = pygame.mouse.get_pos()
                if 680 <= x <= 770 and 45 <= y <= 90:
                    # Changer les cinq prochains Pokémon à afficher
                    self.index_page +=1
                    self.index_affichage += 5
                    if self.index_affichage >= len(self.pok)+1:
                        self.index_affichage = 5
                        self.index_page = 1
                elif 580 <= x <= 670 and 45 <= y <= 90:
                    # Changer les cinq prochains Pokémon à afficher
                    self.index_affichage -= 5
                    self.index_page -= 1
                    if self.index_affichage <= 0:
                        self.index_affichage = len(self.pok)
                        self.index_page = 150//5
                else:
                    for index, nom_pokemon in enumerate(self.l_affichage):
                        y_position = 130 + index * 70
                        if 545 <= x <= 800 and y_position <= y <= y_position + 60:
                            if nom_pokemon != "unknown":
                                # Display characteristics of the clicked Pokemon
                                self.current_pokemon = nom_pokemon
                                self.apok = AnimatedSprite(self.current_pokemon,"Face")
                                self.apok.rect.center = (175, 175)


    def afficher(self):
        self.ecran.blit(self.fond,(0,0))
        self.apok.update()
        self.apok.draw(self.ecran)
        
        self.l_affichage = self.pok.copy()[self.index_affichage - 5 : self.index_affichage]
        for index, nom_pokemon in enumerate(self.l_affichage):
            if nom_pokemon != "unknown":
                texte_surface = self.font.render(nom_pokemon, True, (255, 255, 255))
                y_position = 130 + index * 70  # Ajuster la position en fonction de l'index
                icon_pokemon = pygame.image.load(f"assets/Pokemon/icon/{nom_pokemon}.png")
            else:
                texte_surface = self.font.render("-------", True, (255, 255, 255))
                y_position = 130 + index * 70  # Ajuster la position en fonction de l'index
                icon_pokemon = pygame.image.load(f"assets/Pokemon/icon/unknown.png")
            self.ecran.blit(icon_pokemon, (750, y_position-10))
            self.ecran.blit(texte_surface, (600, y_position))
        
        nbrencontrer = self.font.render(str(self.rencontre),True,(255,255,255))
        self.ecran.blit(nbrencontrer,nbrencontrer.get_rect(center=(710,492)))
        
        nbTotal = self.font.render(str(len(self.pok)),True,(255,255,255))
        self.ecran.blit(nbTotal,nbTotal.get_rect(center=(765,492)))
        
        nbPageTotal = self.font.render("30",True,(255,255,255))
        self.ecran.blit(nbPageTotal,nbPageTotal.get_rect(center=(765,563)))
        
        nbPage = self.font.render(str(self.index_page),True,(255,255,255))
        self.ecran.blit(nbPage,nbPage.get_rect(center=(710,563)))



    def afficher_caracteristiques(self, nom_pokemon):
        if nom_pokemon != "unknown":
            with open(f"assets/Pokemon/Json/{nom_pokemon}.json",'r') as file:
                pokemon_data = json.load(file)
            
            name = self.font.render(f"{nom_pokemon}", True, (255,255,255))
            self.ecran.blit(name,name.get_rect(midbottom=(420, 105)))
            self.ecran.blit(pygame.transform.scale(pygame.image.load(f"assets/Menu/{pokemon_data["Type"]["Type1"]} icon.png"),(175,40)),(330,180))
            self.ecran.blit(pygame.transform.scale(pygame.image.load(f"assets/Menu/{pokemon_data["Type"]["Type2"]} icon.png"),(175,40)),(330,230))
            
            pygame.draw.rect(self.ecran, (0,255,0),(70,365,pokemon_data["Stat"]["PV"],10))
            pygame.draw.rect(self.ecran, (0,255,0),(70,395,pokemon_data["Stat"]["Attaque"],10))
            pygame.draw.rect(self.ecran, (0,255,0),(70,425,pokemon_data["Stat"]["Defense"],10))
            pygame.draw.rect(self.ecran, (0,255,0),(330,365,pokemon_data["Stat"]["Vitesse"],10))
            pygame.draw.rect(self.ecran, (0,255,0),(330,395,pokemon_data["Stat"]["Attaque_Speciale"],10))
            pygame.draw.rect(self.ecran, (0,255,0),(330,425,pokemon_data["Stat"]["Defense_Speciale"],10))
            
            self.ecran.blit(pygame.transform.scale(pygame.image.load(f"assets/Combat/Image/Batk {pokemon_data["atk1"]["type"]}.png"),(215,50)),(35,470))
            n1 = self.font.render(pokemon_data["atk1"]["Name"],True,(255,255,255))
            self.ecran.blit(n1,n1.get_rect(center=(142.5,495)))
            
            self.ecran.blit(pygame.transform.scale(pygame.image.load(f"assets/Combat/Image/Batk {pokemon_data["atk2"]["type"]}.png"),(215,50)),(35,530))
            n2 = self.font.render(pokemon_data["atk2"]["Name"],True,(255,255,255))
            self.ecran.blit(n2,n2.get_rect(center=(142.5,555)))
            
            self.ecran.blit(pygame.transform.scale(pygame.image.load(f"assets/Combat/Image/Batk {pokemon_data["atk3"]["type"]}.png"),(215,50)),(275,470))
            n3 = self.font.render(pokemon_data["atk3"]["Name"],True,(255,255,255))
            self.ecran.blit(n3,n3.get_rect(center=(382.5,495)))
                    
            self.ecran.blit(pygame.transform.scale(pygame.image.load(f"assets/Combat/Image/Batk {pokemon_data["atk4"]["type"]}.png"),(215,50)),(275,530))
            n4 = self.font.render(pokemon_data["atk4"]["Name"],True,(255,255,255))
            self.ecran.blit(n4,n4.get_rect(center=(382.5,555)))
        
