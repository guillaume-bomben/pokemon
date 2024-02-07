import pygame
import random 

from entity import Entity
from keylistener import Keylistener
from screen import Screen
from switch import Switch

class Player(Entity):
    def __init__(self, keylistener: Keylistener, screen: Screen, map, x: int, y: int):
        super().__init__(keylistener, screen, x, y) #Appel au constructeur de la classe parente (Entity)
        self.pokedollars = 0 #Argent du joueur

        #Chargement de la feuille de sprites pour le vélo 
        self.spritesheet_bike: pygame.image = pygame.image.load("assets/sprite/hero_01_red_m_cycle_roll.png")
        self.map = map #Carte sur laquelle le joueur est placé 
        self.switchs: list[Switch] | None = None #Interrupteurs pour le changement de carte
        self.collisions: list[pygame.Rect] | None = None #Zone de collision 
        self.change_map: Switch | None = None #interrupteur pour le changement de carte actuel 
        self.in_combat = False #Indicateur si le joueur est en combat
        self.last_tile = (x, y) #Dernière position du joueur 

    def update(self):
        self.check_input() #Vérification des entrées clavier
        self.check_move() #Vérification des mouvements
        super().update() #Mise à jour de l'entité (classe parente)

    def on_grass_tile(self):
        #Vérifie si le joueur est sur une zone d'herbe
        for grass_zone in self.map.grass_zones:
            if self.hitbox.colliderect(grass_zone):
                return True
        return False

    def check_for_encounters(self):
        #Vérifie les rencontres aléatoires dans l'herbe 
        if self.on_grass_tile():
            x = random.random()
            print(x)
            if x < 0.1: #Probabilité de 10% de rencontrer un pokémon
                return True
        return False


    
    def set_map(self, map_object):
        #définit la carte sur laquelle le joueur se trouve 
        self.map = map_object

    def check_move(self):
        #Vérifie les mouvements possibles en fonction des entrées clavier
        #...(code pour vérifier les mouvements dans toutes les directions et gérer les collisions )
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
        #Ajoute les interrupteurs de changement de carte au joueur 
        self.switchs = switchs
    
    def check_collisions_switchs(self, temp_hitbox):
        #Vérifie les collisions avec les interrupteurs de changement de carte 
        #...(code pour gérer les collisions avec les interrupteurs)
        if self.switchs:
            for switch in self.switchs:
                if switch.check_collisions(temp_hitbox):
                    self.change_map = switch
            return None
        
    def add_collisions(self, collisions):
        #Ajoute les zones de collision à vérifier 
        self.collisions = collisions

    def check_collisions(self, temp_hitbox: pygame.Rect):
        #Vérifie les collisions avec les zones de collision
        #...(code pour gérer les collisions avec les zones définies)
        for collision in self.collisions:
            if temp_hitbox.colliderect(collision):
                return True
        return False
    
    def check_input(self):
        #Vérifie les entrées clavier pour des actions spécifiques (comme changer de vélo)
        if self.keylistener.key_pressed(pygame.K_b):
            self.switch_bike()

    def switch_bike(self, deactive=False):
        #Active ou désactive le vélo, changeant la vitesse et les sprites du joueur 
        if self.speed == 1 and not deactive:
            self.speed = 2 #Augmente la vitesse
            self.all_images = self.get_all_images(self.spritesheet_bike)
        else:
            self.speed = 1 #Rétablit la vitesse normale 
            self.all_images = self.get_all_images(self.spritesheet)
        self.keylistener.remove_key(pygame.K_b) #Supprime la touche de vélo des entrées enregistrées
        