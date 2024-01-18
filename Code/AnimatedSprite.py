import pygame
import sys
import json

class AnimatedSprite:
    def __init__(self, pokemon, orientation):
        with open(f"assets/Pokemon/Json/{pokemon}.json") as f:
            data = json.load(f)
            self.frame_width = data["cut"]["width"] ; self.frame_height = data["cut"]["height"]
            self.scale_width = data["scale"]["width"] ; self.scale_height = data["scale"]["height"]
        self.image_base = pygame.transform.scale(pygame.image.load(f'assets/Pokemon/{orientation}/{pokemon}.png') ,(self.scale_width,self.scale_height))
        #self.frame_width, self.frame_height = frame_width, frame_height
        self.frames = []
        for row in range(0, self.image_base.get_height() - self.frame_height + 1, self.frame_height):
            for col in range(0, self.image_base.get_width() - self.frame_width + 1, self.frame_width):
                frame = self.image_base.subsurface(pygame.Rect(col, row, self.frame_width, self.frame_height))
                self.frames.append(frame)
        
        if not self.frames:
            print("Aucune frame n'a été découpée. Vérifiez les dimensions de découpage.")
            pygame.quit()
            sys.exit()

        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    def update(self):
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.image = self.frames[self.frame_index]

    def draw(self, surface):
        surface.blit(self.image, self.rect)
