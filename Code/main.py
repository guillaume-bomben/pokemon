from combat import Combat
import pygame
import sys

pygame.init()

blanc = (255, 255, 255)

def main():
    combat = Combat("Salameche","Bulbizarre")
    # Boucle de jeu
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        combat.gerer_evenements(events)  # Gérer les événements pour le combat

        combat.afficher()  
        combat.afficher_menu()
        pygame.display.flip() 

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
