from combat import Combat
import pygame
import sys

pygame.init()

# Définition de certaines constantes pour l'écran
largeur_ecran = 800
hauteur_ecran = 600
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
pygame.display.set_caption("Combat Pokémon")

blanc = (255, 255, 255)

def main():
    combat = Combat("Reptincel","Florizarre")  # Créer une instance de la classe Combat

    # Boucle de jeu
    running = True
    while running:
        ecran.fill(blanc)  # Remplir l'écran en blanc

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #combat.gerer_evenements(event)  # Gérer les événements pour le combat

        combat.update()
        combat.afficher()  # Afficher l'écran de combat

        pygame.display.flip()  # Mettre à jour l'écran

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
