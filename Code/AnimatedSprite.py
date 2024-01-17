import pygame
import sys

pygame.init()

# Initialisation de Pygame
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Chargement de la spritesheet
spritesheet = pygame.image.load('Code/35063.png')



class AnimatedSprite:
    def __init__(self, image, frame_width, frame_height):
        self.frame_width, self.frame_height = frame_width, frame_height
        self.frames = []
        for row in range(0, image.get_height() - self.frame_height + 1, self.frame_height):
            for col in range(0, image.get_width() - self.frame_width + 1, self.frame_width):
                frame = image.subsurface(pygame.Rect(col, row, frame_width, frame_height))
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

'''
# Création de l'objet AnimatedSprite
animated_sprite = AnimatedSprite(spritesheet,40,39)
animated_sprite.rect.topleft = (WIDTH // 2, HEIGHT // 2)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    animated_sprite.update()

    screen.fill((255, 255, 255))
    animated_sprite.draw(screen)

    pygame.display.flip()
    clock.tick(5)  # Réglez la vitesse de l'animation en ajustant cet argument'''
