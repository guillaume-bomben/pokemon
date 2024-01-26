import pygame

class Tool:
    
    @staticmethod
    def split_image(spritesheet: pygame.Surface, x: int, y: int, witdh: int, height: int):
       return spritesheet.subsurface(pygame.Rect(x, y, witdh, height))
    #Méthode statique pour découper une image d'une feuille de sprite
    #Retourne une surface Pygame contenant la partie découpée de la feuille de sprites