import pygame 

from game import Game

pygame.mixer.init()

class Menu:
    def __init__(self):
        self.background = pygame.image.load("assets/Menu/Background menu.png")

        original_image = pygame.image.load("assets/Menu/2.png")
        self.m2_size = (220, 36)
        self.m2 = pygame.transform.scale(original_image, self.m2_size)
        self.m2_hover = pygame.transform.scale(original_image, (int(self.m2_size[0]*1.2), int(self.m2_size[1]*1.2)))  # Image agrandie pour la souris

        pygame.mixer.music.load("assets/remix.mp3")

        self.ecran = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font(None, 36)
        self.is_hovered = [False, False, False]  # Un tableau pour stocker l'état de survol des images
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEMOTION:
                    self.gerer_survol(event.pos)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.gerer_clic(event.pos)
            self.afficher()
            pygame.display.flip()

        pygame.quit()
        
        
    def gerer_survol(self, mouse_pos):
        # Vérifiez si la souris survole l'image
        for i in range(3):
            image_rect = self.m2.get_rect(center=(400, 300 + i * 100))
            self.is_hovered[i] = image_rect.collidepoint(mouse_pos)

    def afficher(self):
        self.ecran.blit(self.background, (0, 0))

        for i in range(3):
            if self.is_hovered[i]:
                self.ecran.blit(self.m2_hover, self.m2_hover.get_rect(center=(400, 300 + i * 100)))
            else:
                self.ecran.blit(self.m2, self.m2.get_rect(center=(400, 300 + i * 100)))

        b1 = self.font.render("Jouer", True, (255, 255, 255))
        b1_pos = b1.get_rect(center=(400, 300))
        self.ecran.blit(b1, b1_pos)

        b2 = self.font.render("Add Pokemon", True, (255, 255, 255))
        b2_pos = b2.get_rect(center=(400, 400))
        self.ecran.blit(b2, b2_pos)

        b3 = self.font.render("Pokedex", True, (255, 255, 255))
        b3_pos = b3.get_rect(center=(400, 500))
        self.ecran.blit(b3, b3_pos)
    
    def gerer_clic(self, mouse_pos):
        b1_rect = pygame.Rect(400 - 110, 300 - 18, 220, 36)
        b2_rect = pygame.Rect(400 - 110, 400 - 18, 220, 36)  # Bouton Add Pokemon
        b3_rect = pygame.Rect(400 - 110, 500 - 18, 220, 36)  # Bouton Pokedex
        
        if b1_rect.collidepoint(mouse_pos):
            self.lancer_jeu()
        elif b2_rect.collidepoint(mouse_pos):
            self.afficher_ecran_couleur((0, 255, 0))  # Vert pour Add Pokemon
        elif b3_rect.collidepoint(mouse_pos):
            self.afficher_ecran_couleur((0, 0, 255))  # Bleu pour Pokedex

    def afficher_ecran_couleur(self, couleur):
        self.ecran.fill(couleur)
        pygame.display.flip()
        pygame.time.wait(2000)  # Attendre 2 secondes avant de revenir au menu

    def lancer_jeu(self):
        # Créez une instance de votre jeu et lancez-le
        pygame.mixer.music.play(-1)
        jeu = Game()
        jeu.run()

