import pygame
import random 

from entity import Entity
from keylistener import Keylistener
from screen import Screen
from switch import Switch

class Player(Entity):
    def __init__(self, keylistener: Keylistener, screen: Screen, map, x: int, y: int):
        super().__init__(keylistener, screen, x, y)
        self.pokedollars = 0

        self.spritesheet_bike: pygame.image = pygame.image.load("assets/sprite/hero_01_red_m_cycle_roll.png")
        self.map = map
        self.switchs: list[Switch] | None = None
        self.collisions: list[pygame.Rect] | None = None
        self.change_map: Switch | None = None
        self.in_combat = False
        self.last_tile = (x, y)

    def update(self):
        self.check_input()
        self.check_move()
        super().update()
 ####   
    def on_grass_tile(self):
        for grass_zone in self.map.grass_zones:
            if self.hitbox.colliderect(grass_zone):
                return True
        return False

    def check_for_encounters(self):
        if self.on_grass_tile():
            x = random.random()
            print(x)
            if x < 0.1:
                return True
        return False


    
    def set_map(self, map_object):
        self.map = map_object
#####

    def check_move(self):
        if self.animation_walk is False:
            temp_hitbox = self.hitbox.copy()
            moved = False

            if self.keylistener.key_pressed(pygame.K_q):
                temp_hitbox.x -= 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_left()
                    moved = True
                else:
                    self.direction = "left"

            elif self.keylistener.key_pressed(pygame.K_d):
                temp_hitbox.x += 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_right()
                    moved = True
                else:
                    self.direction = "right"

            elif self.keylistener.key_pressed(pygame.K_z):
                temp_hitbox.y -= 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_up()
                    moved = True
                else:
                    self.direction = "up"

            elif self.keylistener.key_pressed(pygame.K_s):
                temp_hitbox.y += 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_down()
                    moved = True
                else:
                    self.direction = "down"
            

    def add_switchs(self, switchs: list[Switch]):
        self.switchs = switchs
    
    def check_collisions_switchs(self, temp_hitbox):
        if self.switchs:
            for switch in self.switchs:
                if switch.check_collisions(temp_hitbox):
                    self.change_map = switch
            return None
        
    def add_collisions(self, collisions):
        self.collisions = collisions

    def check_collisions(self, temp_hitbox: pygame.Rect):
        for collision in self.collisions:
            if temp_hitbox.colliderect(collision):
                return True
        return False
    
    def check_input(self):
        if self.keylistener.key_pressed(pygame.K_b):
            self.switch_bike()

    def switch_bike(self, deactive=False):
        if self.speed == 1 and not deactive:
            self.speed = 2
            self.all_images = self.get_all_images(self.spritesheet_bike)
        else:
            self.speed = 1
            self.all_images = self.get_all_images(self.spritesheet)
        self.keylistener.remove_key(pygame.K_b)
        