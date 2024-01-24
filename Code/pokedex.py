import pygame
import json

class pokedex:
    def __init__(self):
        self.ecran = pygame.display.set_mode((800, 600))
        self.fond = pygame.image.load("assets/Menu/Pokedex.png")
        self.font = pygame.font.Font(None, 32)
        
        self.pok = []
        with open("Code/pokedex.json","r") as file:
            data = json.load(file)
            for pokemon in data.keys():
                self.pok.append(pokemon)
                self.index_affichage = 5
        self.l_affichage = []
        
        self.running = True
        while self.running:
            self.afficher()
            self.gerer_evenements()
            pygame.display.flip()

    def gerer_evenements(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Vérifier si le clic est dans la zone du bouton
                x, y = pygame.mouse.get_pos()
                if 680 <= x <= 770 and 45 <= y <= 90:
                    # Changer les cinq prochains Pokémon à afficher
                    self.index_affichage += 5
                    if self.index_affichage >= len(self.pok)+1:
                        self.index_affichage = 5
                if 580 <= x <= 670 and 45 <= y <= 90:
                    # Changer les cinq prochains Pokémon à afficher
                    self.index_affichage -= 5
                    if self.index_affichage <= 0:
                        self.index_affichage = 150

    def afficher(self):
        self.ecran.blit(self.fond,(0,0))
        
        self.l_affichage = self.pok.copy()[self.index_affichage - 5 : self.index_affichage]
        for index, nom_pokemon in enumerate(self.l_affichage):
            texte_surface = self.font.render(nom_pokemon, True, (255, 255, 255))
            y_position = 130 + index * 70  # Ajuster la position en fonction de l'index
            self.ecran.blit(texte_surface, (600, y_position))