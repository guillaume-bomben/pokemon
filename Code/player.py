import pygame

from entity import Entity
from keylistener import Keylistener
from screen import Screen
from switch import Switch


class Player(Entity):
    def __init__(self, keylistener: Keylistener, screen: Screen, x: int, y: int):
        super().__init__(keylistener, screen, x, y)

        self.pokedollars = 0

        self.switchs: list[Switch] | None = None
        self.collisions: list[pygame.Rect] | None = None
        self.change_map: Switch | None = None

    def update(self):
        self.check_input()
        self.check_move()
        super().update()

    def check_move(self):
        if self.animation_walk is False:
            temp_hitbox = self.hitbox.copy()
            if self.keylistener.key_pressed(pygame.K_q):
                temp_hitbox.x -= 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_left()
                else:
                    self.direction = "left"
            elif self.keylistener.key_pressed(pygame.K_d):
                temp_hitbox.x += 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_right()
                else:
                    self.direction = "right"
            elif self.keylistener.key_pressed(pygame.K_z):
                temp_hitbox.y -= 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_up()
                else:
                    self.direction = "up"
            elif self.keylistener.key_pressed(pygame.K_s):
                temp_hitbox.y += 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_down()
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

    def switch_bike(self):
        if self.speed == 1:
            self.speed = 2
        else:
            self.speed = 1
        self.keylistener.remove_key(pygame.K_b)
