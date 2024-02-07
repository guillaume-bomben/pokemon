import pygame

class Switch:
    def __init__(self, type: str, name: str, hitbox: pygame.Rect, port: int):
        #Initialisation de l'interrupteur (Switch)
        self.type = type #Type de l'interrupteur, utilisé pour déterminer son comportement
        self.name = name #Nome de l'interrupteur, souvent utilisé pour identifier l'interrupteur dans le jeu 
        self.hitbox = hitbox #Hitbox de l'interrupteur pour détecter les collisions
        self.port = port #Numéro de port, utilisé pour identifier où l'interrupteur mène
     
    def check_collisions(self, temp_hitbox):
        #Vérifie si la hitbox de l'interrupteur entre en collision avec une autre hitbox
        #Renvoie True si il y a collision, sinon False
        return self.hitbox.colliderect(temp_hitbox)
