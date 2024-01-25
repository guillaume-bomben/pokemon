import pygame
import pytmx
import pyscroll

from screen import Screen
from player import Player
from switch import Switch

class Map:
    def __init__(self, screen: Screen):
        self.screen = screen 
        self.tmx_data = None
        self.map_layer = None
        self.group = None
        self.grass_zones = []
        self.switchs: list[Switch] | None = None
        self.collisions: list[pygame.Rect] | None = None 
        self.player: Player | None = None
        self.current_map: Switch = Switch("switch", "map_0", pygame.Rect(0, 0, 0, 0), 0)
        self.switch_map(self.current_map)
    

    def switch_map(self, switch: Switch):
        self.tmx_data = pytmx.load_pygame(f"assets/map/{switch.name}.tmx")
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 3
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=7)
        self.load_grass_zones()

        if switch.name.split("_")[0] == "map":
            self.map_layer.zoom = 3
        else:
            self.map_layer.zomm = 10

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
        self.group.add(player)
        self.player = player
        self.player.align_hitbox()
        self.player.add_switchs(self.switchs)
        self.player.add_collisions(self.collisions)

    def update(self):
        if self.player:
            if self.player.change_map and self.player.step >= 8:
                self.switch_map(self.player.change_map)
                self.player.change_map = None
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen.get_display())

    def pose_player(self, switch: Switch):
        position = self.tmx_data.get_object_by_name("spawn " + self.current_map.name + " " + str(switch.port))
        self.player.position = pygame.math.Vector2(position.x, position.y)
    
    def load_grass_zones(self):
        if self.tmx_data is not None:
            for obj in self.tmx_data.objects:
                if obj.type == "grass":
                    self.grass_zones.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    
    