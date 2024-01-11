import pygame

from tool import Tool
from screen import Screen
from keylistener import Keylistener

class Entity(pygame.sprite.Sprite):

    def __init__(self, keylistener: Keylistener, screen: Screen, x: int, y: int):
        super().__init__()
        self.screen = screen
        self.keylistener = keylistener
        self.spritesheet = pygame.image.load("assets/sprite/hero_01_red_m_walk.png")
        self.image = Tool.split_image(self.spritesheet, 0, 0, 24, 32)
        self.position: pygame.math.Vector2 = pygame.math.Vector2(x + 232, y + 135)
        self.rect: pygame.Rect = self.image.get_rect()
        self.all_images = self.get_all_images()

        self.hitbox: pygame.Rect = pygame.Rect(0, 0, 16, 16)
        
        self.step: int = 0
        self.animation_walk: bool = False
        self.direction = "down"


    def update(self):
        self.rect.center = self.position
        self.hitbox.midbottom = self.rect.midbottom


    def move_left(self):
        self.animation_walk = True
        self.direction = "left"
        self.image = self.all_images["left"][0]
    
    def move_right(self):
        self.animation_walk = True
        self.direction = "right"
        self.image = self.all_images["right"][0]
    
    def move_up(self):
        self.animation_walk = True
        self.direction = "up"
        self.image = self.all_images["up"][0]

    def move_down(self):
        self.animation_walk = True
        self.direction = "down"
        self.image = self.all_images["down"][0]

    def align_hitbox(self):
        self.rect.center = self.position
        self.hitbox.midbottom = self.rect.midbottom
        while self.hitbox.x % 16 != 0:
            self.rect.x -= 1
            self.hitbox.midbottom = self.rect.midbottom
        while self.hitbox.y % 16 != 0:
            self.rect.y -= 1
            self.hitbox.midbottom = self.rect.midbottom
        self.position = pygame.math.Vector2(self.rect.center)

    
    def get_all_images(self):
        all_images = {
            "down": [],
            "left": [],
            "right": [],
            "up": [] 
        }
        
        width: int = self.spritesheet.get_width() // 4
        height: int = self.spritesheet.get_height() // 4

        for i in range(4):
            for j, key in enumerate(all_images.keys()):
                all_images[key].append(Tool.split_image(self.spritesheet, i * width, j * height, 24, 32))
            return all_images
