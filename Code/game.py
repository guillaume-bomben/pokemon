import time
import pygame

from screen import Screen
from map import Map
from entity import Entity
from keylistener import Keylistener
from player import Player
from combat import Combat

class Game:
    def __init__(self):
        self.running = True
        self.in_combat = False
        self.screen = Screen()
        self.keylistener = Keylistener()

        self.map = Map(self.screen)
        self.player = Player(self.keylistener, self.screen, self.map, 0, 0)
        self.map.add_player(self.player)
        self.last_time = time.time()

    def run(self):
        while self.running:
            if not self.in_combat:
                self.handle_input()
                self.map.update()
                self.screen.update()
                
                actual_time = time.time()
                if actual_time - self.last_time >= 0.5:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_z] or keys[pygame.K_q] or keys[pygame.K_s] or keys[pygame.K_d]:
                        #Vérifie les rencontres potentielles
                        if self.player.check_for_encounters():
                            self.combat_screen()
                            self.in_combat = True
                    self.last_time = actual_time
            else:
                self.combat_screen()
                if self.combat_ended():
                    self.in_combat = False

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self.keylistener.add_keys(event.key)
            elif event.type == pygame.KEYUP:
                self.keylistener.remove_key(event.key)
    
    def combat_screen(self):
    # Logique pour afficher l'écran de combat
        player = "Sulfura"
        adversaire = "Sulfura"
        combat = Combat(player,adversaire)


