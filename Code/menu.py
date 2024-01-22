import pygame 

class Menu:
    def __init__(self):
        self.background = pygame.image.load("assets/Menu/Background menu.png")
        self.ecran = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font(None, 36)
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
            self.afficher()
            pygame.display.flip() 
        
        
    def afficher(self):
        self.ecran.blit(self.background,(0,0))
        
        b1 = self.font.render("menu 1",True,(255,255,255))
        b1_pos = b1.get_rect(midbottom=(400,300))
        self.ecran.blit(b1,b1_pos)
        b2 = self.font.render("menu 2",True,(255,255,255))
        b2_pos = b2.get_rect(midbottom=(400,400))
        self.ecran.blit(b2,b2_pos)
        b3 = self.font.render("menu 3",True,(255,255,255))
        b3_pos = b3.get_rect(midbottom=(400,500))
        self.ecran.blit(b3,b3_pos)