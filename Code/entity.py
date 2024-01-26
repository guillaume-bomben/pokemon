import pygame

from tool import Tool
from screen import Screen
from keylistener import Keylistener

class Entity(pygame.sprite.Sprite):

    def __init__(self, keylistener: Keylistener, screen: Screen, x: int, y: int):
        super().__init__()
        self.screen = screen #Ecran sur lequel l'entité sera dessinée
        self.keylistener = keylistener #Gestionnaire des évènements clavier
        self.spritesheet = pygame.image.load("assets/sprite/hero_01_red_m_walk.png") #Chargement de la feuille de sprites
        self.image = Tool.split_image(self.spritesheet, 0, 0, 24, 32) #Image initiale de l'entité
        self.position: pygame.math.Vector2 = pygame.math.Vector2(x + 232, y + 135) #Position initiale de l'entité
        self.rect: pygame.Rect = self.image.get_rect() #Rectangle de collision de l'entité
        self.all_images = self.get_all_images(self.spritesheet) #Stockage de toutes les images pour l'animation
        self.index_image = 0 #Index de l'image actuelle dans l'animation
        self.image_part = 0 #Partie de l'animation en cours 
        self.reset_animation = False #Indicateur pour réinitialiser l'animation

        self.hitbox: pygame.Rect = pygame.Rect(0, 0, 16, 16) #Hitbox de l'entité pour la détection de collision
        
        self.step: int = 0 #Etape actuelle de l'animation de marche 
        self.animation_walk: bool = False  #Indicateur si l'entité est en train de marcher
        self.direction = "down" #Direction initiale de l'entité 

        self.animation_step_time: float = 0.0 #Temps écoulé depuis la dernière étape de l'animation
        self.action_animation = 16 #Durée de chaque étape de l'animation

        self.speed: int = 1 #Vitesse de déplacement de l'entité 


    def update(self):
        self.animation_sprite() #Mise à jour de l'animation du sprite 
        self.move() #Mise à jour du mouvement
        self.rect.center = self.position #Mise à jour de la position du rectangle de collision 
        self.hitbox.midbottom = self.rect.midbottom #Mise à jour de la position de la hitbox 
        if 0 <= self.index_image < len(self.all_images[self.direction]):
            self.image = self.all_images[self.direction][self.index_image]
        else: 
            self.index_image = 0 #Réinitialisation de l'index d'image si nécessaire

    def move_left(self):
        self.animation_walk = True
        self.direction = "left"
    
    def move_right(self):
        self.animation_walk = True
        self.direction = "right"
    
    def move_up(self):
        self.animation_walk = True
        self.direction = "up"

    def move_down(self):
        self.animation_walk = True
        self.direction = "down"

    def animation_sprite(self):
        #Mise à jour de l'index d'image pour l'animation 
        if int(self.step // 8) + self.image_part >= 4:
            self.image_part = 0
            self.reset_animation = True
        self.index_image = int(self.step // 8) + self.image_part

    def move(self):
        #Mise à jour du mouvement et de l'animation 
        if self.animation_walk:
            self.animation_step_time += self.screen.get_delta_time()
            if self.step < 16 and self.animation_step_time >= self.action_animation:
                self.step += self.speed
                #Mise à jour de la position en fonction de la direction
                if self.direction == "left":
                    self.position.x -= self.speed
                elif self.direction == "right":
                    self.position.x += self.speed
                elif self.direction == "up":
                    self.position.y -= self.speed
                elif self.direction == "down":
                    self.position.y += self.speed
                self.animation_step_time = 0

            elif self.step >= 16:
                self.step = 0 
                self.animation_walk = False
                if self.reset_animation:
                    self.reset_animation = False
                else:
                    if self.image_part == 0:
                        self.image_part = 2
                    else:
                        self.image_part = 0

    def align_hitbox(self):
        #Alignement de la hitbox de l'entité
        self.rect.center = self.position
        self.hitbox.midbottom = self.rect.midbottom
        #Ajutement de la position pour qu'elle soit alignée sur une grille
        while self.hitbox.x % 16 != 0:
            self.rect.x -= 1
            self.hitbox.midbottom = self.rect.midbottom
        while self.hitbox.y % 16 != 0:
            self.rect.y -= 1
            self.hitbox.midbottom = self.rect.midbottom
        self.position = pygame.math.Vector2(self.rect.center)

    
    def get_all_images(self, spritesheet):
        #Récupération de toutes le simages pour les différentes animations 
        all_images = {
            "down": [],
            "left": [],
            "right": [],
            "up": [] 
        }
        
        width: int = spritesheet.get_width() // 4
        height: int = spritesheet.get_height() // 4

        for i in range(4):
            for j, key in enumerate(all_images.keys()):
                all_images[key].append(Tool.split_image(spritesheet, i * width, j * height, 24, 32))
        return all_images
