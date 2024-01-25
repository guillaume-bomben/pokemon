import json
import pygame
from game import Game

class choixPokemon:
    def __init__(self) -> None:
        self.ecran = pygame.display.set_mode((800, 600))
        self.fond = pygame.image.load("assets/Menu/add pokemon fond.png")
        
        self.pok = []
        with open("Code/pokedex.json","r") as file:
            data = json.load(file)
            for pokemon in data.keys():
                if data[pokemon] == "False":
                    self.pok.append("unknown")
                else:
                    self.pok.append(pokemon)
                self.index_affichage = 50
        self.l_affichage = []
        
        self.colonnes = 15
        self.largeur_image = 40
        self.espace_entre_lignes = 10
        
        self.running = True
        while self.running:
            self.afficher()
            self.gerer_evenements()
            pygame.display.flip()
    
    def afficher(self):
        self.ecran.blit(self.fond,(0,0))
        
        self.l_affichage = self.pok.copy()
        lignes = (len(self.l_affichage) + self.colonnes - 1) // self.colonnes
        for i in range(lignes):
            for j in range(self.colonnes):
                index = i * self.colonnes + j
                if index < len(self.l_affichage):
                    pokemon = self.l_affichage[index]
                    image = pygame.image.load(f"assets/Pokemon/icon/{pokemon}.png")
                    x = j * (self.largeur_image + self.espace_entre_lignes) + 30
                    y = i * (self.largeur_image + self.espace_entre_lignes) + 100
                    self.ecran.blit(image, (x, y))


    def gerer_evenements(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button clicked
                x, y = event.pos
                clicked_pokemon = self.get_clicked_pokemon(x, y)
                if clicked_pokemon:
                    self.update_player_pokemon(clicked_pokemon)
                    jeu = Game()
                    jeu.run()

    def get_clicked_pokemon(self, x, y):
        for i in range(len(self.l_affichage)):
            pokemon = self.l_affichage[i]
            image_rect = pygame.Rect(
                i % self.colonnes * (self.largeur_image + self.espace_entre_lignes) + 30,
                i // self.colonnes * (self.largeur_image + self.espace_entre_lignes) + 100,
                self.largeur_image,
                self.largeur_image
            )
            if image_rect.collidepoint(x, y):
                return pokemon
        return None

    def update_player_pokemon(self, selected_pokemon):
        with open("Code/pokemon_player.json", "r") as file:
            player_data = json.load(file)

        # Update the player's Pokemon data with the selected Pokemon
        player_data["selected_pokemon"] = selected_pokemon

        with open("Code/pokemon_player.json", "w") as file:
            json.dump(player_data, file)