import pygame
import pytmx
import pyscroll

from screen import Screen
from player import Player
from switch import Switch

class Map:
    def __init__(self, screen: Screen):
        #Initialisation des paramètres de base de la carte
        self.screen = screen #Ecran sur lequel la carte sera dessinée 
        self.tmx_data = None #Données de la carte au format TMX
        self.map_layer = None #Couche de carte pour pyscroll
        self.group = None #Groupe pyscroll pour gérer les couches de rendu 
        self.grass_zones = [] #Zones d'herbe sur la carte
        self.switchs: list[Switch] | None = None #Interrupteurs pour changer de carte
        self.collisions: list[pygame.Rect] | None = None  #Zones de collision
        self.player: Player | None = None #Joueur sur la carte
        self.current_map: Switch = Switch("switch", "map_0", pygame.Rect(0, 0, 0, 0), 0)
        self.switch_map(self.current_map) #Initialisation de la carte actuelle
    

    def switch_map(self, switch: Switch):
        #Changement de la carte acutelle 
        self.tmx_data = pytmx.load_pygame(f"assets/map/{switch.name}.tmx")
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 3 #Zoom initial
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=7)
        self.load_grass_zones() #Chargement des zones d'herbes

        #Gestion de la taille de la carte en fonction du type de carte 
        if switch.name.split("_")[0] == "map":
            self.map_layer.zoom = 3
        else:
            self.map_layer.zomm = 10

        #Initialisation des interrupteurs et des collisions 
        self.switchs = []
        self.collisions = []

        for obj in self.tmx_data.objects:
            if obj.name == "collision":
                self.collisions.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.name:
                type = obj.name.split(" ")[0]
                if type == "switch":
                    self.switchs.append(Switch(
                        type, obj.name.split(" ")[1], pygame.Rect(obj.x, obj.y, obj.width, obj.height), int(obj.name.split(" ")[-1])
                    ))
        
        #Positionnement du joueur et ajout des groupes 
        if self.player:
            self.pose_player(switch)
            self.player.align_hitbox()
            self.player.step = 16
            self.player.add_switchs(self.switchs)
            self.player.add_collisions(self.collisions)
            self.group.add(self.player)
            if switch.name.split("_")[0] != "map":
                self.player.switch_bike(True)
        
        self.current_map = switch
        

    def add_player(self, player):
        #Ajout du joueur à la carte 
        self.group.add(player)
        self.player = player
        self.player.align_hitbox()
        self.player.add_switchs(self.switchs)
        self.player.add_collisions(self.collisions)

    def update(self):
        #Mise à jour de la carte 
        if self.player:
            if self.player.change_map and self.player.step >= 8:
                self.switch_map(self.player.change_map)
                self.player.change_map = None
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen.get_display())

    def pose_player(self, switch: Switch):
        #Positionnement du joueur lors du changement de carte 
        position = self.tmx_data.get_object_by_name("spawn " + self.current_map.name + " " + str(switch.port))
        self.player.position = pygame.math.Vector2(position.x, position.y)
    
    def load_grass_zones(self):
        #Chargement des aones d'herbes à partir des données TMX 
        if self.tmx_data is not None:
            for obj in self.tmx_data.objects:
                if obj.type == "grass":
                    self.grass_zones.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    
    