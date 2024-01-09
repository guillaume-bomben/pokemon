import pygame
import sys

pygame.init()

largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Menu Pokémon")


pygame.mixer.music.load("son/pokemon_theme.mp3")  
pygame.mixer.music.set_volume(0.5)  
son_clic = pygame.mixer.Sound("son/pet.mp3")
volume_bruitage = 1


blanc = (0, 0, 0)



class MenuPrincipal:
    def __init__(self):
        self.image_fond = pygame.image.load("images/PokemonFond.png")
        self.image_fond = pygame.transform.scale(self.image_fond, (largeur_fenetre, hauteur_fenetre))
        self.image_titre = pygame.image.load("images/Logo.png")
        self.image_titre = pygame.transform.scale(self.image_titre, (400, 100))
        self.police_titre = pygame.font.Font("polices/Pokemon Solid.ttf", 60)  # Remplacez par le chemin de votre police
        self.police_texte = pygame.font.Font("polices/pokemon Solid.ttf", 30)  # Remplacez par le chemin de votre police
        self.options = ["Nouvelle Partie", "Continuer", "Paramètres"]
        self.option_selectionnee = 0  

    def afficher_menu(self):
        pygame.mixer.music.play(-1)  

        while True:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_DOWN:
                        son_clic.play()
                        self.option_selectionnee = (self.option_selectionnee + 1) % len(self.options)
                    elif evenement.key == pygame.K_UP:
                        son_clic.play()
                        self.option_selectionnee = (self.option_selectionnee - 1) % len(self.options)
                    elif evenement.key == pygame.K_RETURN:
                        son_clic.play()
                        if self.options[self.option_selectionnee] == "Nouvelle Partie":
                            Jeu().lancer_jeu()
                        elif self.options[self.option_selectionnee] == "Continuer":
                            print("Continuer la partie")
                        elif self.options[self.option_selectionnee] == "Paramètres":
                            menu_options.afficher_menu_options()

            fenetre.blit(self.image_fond, (0, 0))
            fenetre.blit(self.image_titre, (largeur_fenetre // 2 - 200, hauteur_fenetre // 4 - 50))

            for i, option in enumerate(self.options):
                texte_option = self.police_texte.render(option, True, blanc)
                texte_rect_option = texte_option.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 2 + i * 40))
                fenetre.blit(texte_option, texte_rect_option)

            pygame.draw.line(fenetre, blanc, (largeur_fenetre // 2 - 70, hauteur_fenetre // 2 + self.option_selectionnee * 40 + 10),
                             (largeur_fenetre // 2 + 70, hauteur_fenetre // 2 + self.option_selectionnee * 40 + 10), 2)

            pygame.display.flip()

# Classe pour le menu d'options
class MenuOptions:
    def __init__(self):
        self.police_titre = pygame.font.Font("polices/Pokemon Solid.ttf", 60)  # Remplacez par le chemin de votre police
        self.police_texte = pygame.font.Font("polices/Pokemon Solid.ttf", 30)  # Remplacez par le chemin de votre police

    def afficher_menu_options(self):
        pygame.mixer.music.pause()  

        while True:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_ESCAPE:
                        son_clic.play()
                        pygame.mixer.music.unpause()
                        return

            fenetre.blit(menu_principal.image_fond, (0, 0))

            texte_titre_options = self.police_titre.render("Menu Options", True, blanc)
            texte_rect_titre_options = texte_titre_options.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 4))
            fenetre.blit(texte_titre_options, texte_rect_titre_options)

            texte_volume = self.police_texte.render(f"Volume des bruitages: {int(volume_bruitage * 100)}%", True, blanc)
            texte_rect_volume = texte_volume.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 2))
            fenetre.blit(texte_volume, texte_rect_volume)

            pygame.display.flip()

# Classe pour le jeu
class Jeu:
    def __init__(self):
        pass

    def lancer_jeu(self):
        pygame.mixer.music.stop()
        print("Nouvelle partie !")

# Instanciation des classes
menu_principal = MenuPrincipal()
menu_options = MenuOptions()

# Exécution du menu principal
menu_principal.afficher_menu()

