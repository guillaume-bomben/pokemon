import pygame
import sys
import json

class AnimatedSprite:
    def __init__(self, pokemon, orientation):
                
        ## Charger les données du Pokémon à partir d'un fichier JSON
        with open(f"assets/Pokemon/Json/{pokemon}.json") as f:
            data = json.load(f)
            ## Récupérer les dimensions pour le découpage et la mise à l'échelle des frames
            self.frame_width = data["cut"]["width"] ; self.frame_height = data["cut"]["height"]
            self.scale_width = data["scale"]["width"] ; self.scale_height = data["scale"]["height"]
            
        ## Charger et mettre à l'échelle l'image de base du Pokémon
        self.image_base = pygame.transform.scale(pygame.image.load(f'assets/Pokemon/{orientation}/{pokemon}.png') ,(self.scale_width,self.scale_height))
        
        ## Découpage de l'image en frames individuelles        
        self.frames = []
        for row in range(0, self.image_base.get_height() - self.frame_height + 1, self.frame_height):
            for col in range(0, self.image_base.get_width() - self.frame_width + 1, self.frame_width):
                frame = self.image_base.subsurface(pygame.Rect(col, row, self.frame_width, self.frame_height))
                self.frames.append(frame)

         ## Vérification pour s'assurer que des frames ont été correctement découpées       
        if not self.frames:
            print("Aucune frame n'a été découpée. Vérifiez les dimensions de découpage.")
            pygame.quit()
            sys.exit()
        
        ## Initialisation de l'index de frame et de l'image courante
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    def update(self):

        ## Mise à jour de l'index de frame pour l'animation
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.image = self.frames[self.frame_index]

    def draw(self, surface):
        ## Dessiner l'image actuelle sur la surface donnée
        surface.blit(self.image, self.rect)

