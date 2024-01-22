import pygame
import sys
import json

pygame.init()

largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Menu Pokémon")

pygame.mixer.music.load("son/pokemon_theme.mp3")
pygame.mixer.music.set_volume(0.5)
son_clic = pygame.mixer.Sound("son/pet.mp3")
volume_bruitage = 1

noir = (0, 0, 0)


class MenuPrincipal:
    def __init__(self):
        self.image_fond = pygame.image.load("images/PokemonFond.png")
        self.image_fond = pygame.transform.scale(self.image_fond, (largeur_fenetre, hauteur_fenetre))
        self.image_titre = pygame.image.load("images/Logo.png")
        self.image_titre = pygame.transform.scale(self.image_titre, (400, 100))
        self.police_titre = pygame.font.Font("polices/Pokemon Solid.ttf", 60)
        self.police_texte = pygame.font.Font("polices/Pokemon Solid.ttf", 30)
        self.options = ["Nouvelle Partie", "Continuer", "Paramètres", "Crédits", "Ajouter Pokémon", "Pokedex"]
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
                        elif self.options[self.option_selectionnee] == "Crédits":
                            menu_credits.afficher_menu_credits()
                        elif self.options[self.option_selectionnee] == "Ajouter Pokémon":
                            self.ajouter_pokemon()
                        elif self.options[self.option_selectionnee] == "Voir Pokémon":
                            self.afficher_pokemon()

            fenetre.blit(self.image_fond, (0, 0))
            fenetre.blit(self.image_titre, (largeur_fenetre // 2 - 200, hauteur_fenetre // 4 - 50))

            for i, option in enumerate(self.options):
                texte_option = self.police_texte.render(option, True, noir)
                texte_rect_option = texte_option.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 2 + i * 40))
                fenetre.blit(texte_option, texte_rect_option)

            pygame.draw.line(fenetre, noir, (largeur_fenetre // 2 - 70, hauteur_fenetre // 2 + self.option_selectionnee * 40 + 10),
                             (largeur_fenetre // 2 + 70, hauteur_fenetre // 2 + self.option_selectionnee * 40 + 10), 2)

            pygame.display.flip()

    def ajouter_pokemon(self):
        saisie_active = True
        nom_pokemon = ""
        type_pokemon = ""
        phase_saisie = 1  # 1 pour le nom, 2 pour le type

        while saisie_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if phase_saisie == 1:
                            phase_saisie = 2
                        elif nom_pokemon:  # Vérifiez si nom_pokemon n'est pas vide
                            saisie_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        if phase_saisie == 1:
                            nom_pokemon = nom_pokemon[:-1]
                        else:
                            type_pokemon = type_pokemon[:-1]
                    else:
                        if phase_saisie == 1:
                            nom_pokemon += event.unicode
                        else:
                            type_pokemon += event.unicode

            fenetre.fill((0, 0, 0))  # Efface l'écran
            texte_saisi = self.police_texte.render(f"Nom: {nom_pokemon}" if phase_saisie == 1 else f"Type: {type_pokemon}", True, noir)
            fenetre.blit(texte_saisi, (100, 100))  # Ajustez la position selon vos besoins
            pygame.display.flip()

        # Enregistrement du Pokémon
        nouveau_pokemon = {"nom": nom_pokemon, "type": type_pokemon}
        with open("pokemons.json", "a") as fichier_json:
            json.dump(nouveau_pokemon, fichier_json)
            fichier_json.write("\n")

        print("Pokémon ajouté : ", nouveau_pokemon)  # Pour la confirmation

    def afficher_pokemon(self):
        with open("assets/Pokemon/Json/pokemons.json", "r") as fichier_json:
            pokemons = json.load(fichier_json)

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

            fenetre.fill((0, 0, 0))  # Efface l'écran

            y_position = hauteur_fenetre // 2
            for pokemon in pokemons:
                texte_pokemon = self.police_texte.render(f"Nom: {pokemon['nom']}, Type: {pokemon['type']}", True, noir)
                texte_rect_pokemon = texte_pokemon.get_rect(center=(largeur_fenetre // 2, y_position))
                fenetre.blit(texte_pokemon, texte_rect_pokemon)
                y_position += 40

            pygame.display.flip()


class MenuOptions:
    def __init__(self):
        self.police_titre = pygame.font.Font("polices/Pokemon Solid.ttf", 60)
        self.police_texte = pygame.font.Font("polices/Pokemon Solid.ttf", 30)

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

            texte_titre_options = self.police_titre.render("Menu Options", True, noir)
            texte_rect_titre_options = texte_titre_options.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 4))
            fenetre.blit(texte_titre_options, texte_rect_titre_options)

            texte_volume = self.police_texte.render(f"Volume des bruitages: {int(volume_bruitage * 100)}%", True, noir)
            texte_rect_volume = texte_volume.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 2))
            fenetre.blit(texte_volume, texte_rect_volume)

            pygame.display.flip()


class MenuCredits:
    def __init__(self):
        self.police_titre = pygame.font.Font("polices/Pokemon Solid.ttf", 60)
        self.police_texte = pygame.font.Font("polices/Pokemon Solid.ttf", 30)
        self.credits = [
            "Développeur 1 : Tommy Le Bg",
            "Développeur 2 : Guillaume La RTX",
            "Développeur 3 : Val avec son bateau nul",
        ]

    def afficher_menu_credits(self):
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

            texte_titre_credits = self.police_titre.render("Crédits", True, noir)
            texte_rect_titre_credits = texte_titre_credits.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 4))
            fenetre.blit(texte_titre_credits, texte_rect_titre_credits)

            y_position = hauteur_fenetre // 2
            for ligne_credit in self.credits:
                texte_credit = self.police_texte.render(ligne_credit, True, noir)
                texte_rect_credit = texte_credit.get_rect(center=(largeur_fenetre // 2, y_position))
                fenetre.blit(texte_credit, texte_rect_credit)
                y_position += 40

            pygame.display.flip()


class Jeu:
    def __init__(self):
        pass

    def lancer_jeu(self):
        pygame.mixer.music.stop()
        print("Nouvelle partie !")


# Instanciation des classes
menu_principal = MenuPrincipal()
menu_options = MenuOptions()
menu_credits = MenuCredits()

# Exécution du menu principal
menu_principal.afficher_menu()
