import pygame
import os
import json
import shutil
from tkinter import filedialog
from tkinter import Tk

# Constants for the dimensions and positions
BUTTON_SIZE = (200, 50)

class addpokemon:
    def __init__(self):
        pygame.init()
        self.window_size = (800,600)
        self.screen = pygame.display.set_mode(self.window_size)
        self.input_boxes_width = 100
        self.input_boxes_height = 32
        self.white = (255, 255, 255)
        self.black = (0,0,0)

        self.background = pygame.image.load("assets/Menu/add pokemon fond.png")
        self.font = pygame.font.Font(None, 24)

        # Define the positions for input boxes and buttons
        self.name_box_pos   = (800 * 0.12, 600 * 0.1)
        self.pv_box_pos     = (800 * 0.12, 600 * 0.2)
        self.type1_box_pos  = (800 * 0.12, 600 * 0.3)
        self.type2_box_pos  = (800 * 0.12, 600 * 0.4)
        self.atk_box_pos    = (800 * 0.12, 600 * 0.5)
        self.atk_spe_box_pos= (800 * 0.12, 600 * 0.6)
        self.def_box_pos    = (800 * 0.12, 600 * 0.7)
        self.def_spe_box_pos= (800 * 0.12, 600 * 0.8)
        self.vit_box_pos    = (800 * 0.12, 600 * 0.9)
        
        self.n1_box_pos     = (800 * 0.42 , 600 * 0.3)
        self.tn1_box_pos    = (800 * 0.42 , 600 * 0.4)
        self.pn1_box_pos    = (800 * 0.42 , 600 * 0.5)
        self.tcn1_box_pos   = (800 * 0.42 , 600 * 0.6)
        
        self.n2_box_pos     = (800 * 0.42 + 110 , 600 * 0.3)
        self.tn2_box_pos    = (800 * 0.42 + 110 , 600 * 0.4)
        self.pn2_box_pos    = (800 * 0.42 + 110 , 600 * 0.5)
        self.tcn2_box_pos   = (800 * 0.42 + 110 , 600 * 0.6)
        
        self.n3_box_pos     = (800 * 0.42 + 220 , 600 * 0.3)
        self.tn3_box_pos    = (800 * 0.42 + 220 , 600 * 0.4)
        self.pn3_box_pos    = (800 * 0.42 + 220 , 600 * 0.5)
        self.tcn3_box_pos   = (800 * 0.42 + 220 , 600 * 0.6)
        
        self.n4_box_pos     = (800 * 0.42 + 330 , 600 * 0.3)
        self.tn4_box_pos    = (800 * 0.42 + 330 , 600 * 0.4)
        self.pn4_box_pos    = (800 * 0.42 + 330 , 600 * 0.5)
        self.tcn4_box_pos   = (800 * 0.42 + 330 , 600 * 0.6)
        
        self.select_sprite_button_pos = (800 * 0.3, 600 * 0.7)
        self.save_button_pos = (800 * 0.3, 600 * 0.8)

        # Create input boxes
        self.input_boxes = {
            'name':    pygame.Rect(self.name_box_pos,    (self.input_boxes_width, self.input_boxes_height)),
            'pv':      pygame.Rect(self.pv_box_pos,      (self.input_boxes_width, self.input_boxes_height)),
            'type1':   pygame.Rect(self.type1_box_pos,   (self.input_boxes_width, self.input_boxes_height)),
            'type2':   pygame.Rect(self.type2_box_pos,   (self.input_boxes_width, self.input_boxes_height)),
            'atk':     pygame.Rect(self.atk_box_pos,     (self.input_boxes_width, self.input_boxes_height)),
            'def':     pygame.Rect(self.def_box_pos,     (self.input_boxes_width, self.input_boxes_height)),
            'atk_spe': pygame.Rect(self.atk_spe_box_pos, (self.input_boxes_width, self.input_boxes_height)),
            'def_spe': pygame.Rect(self.def_spe_box_pos, (self.input_boxes_width, self.input_boxes_height)),
            'vitesse': pygame.Rect(self.vit_box_pos,     (self.input_boxes_width, self.input_boxes_height)),
            
            'n1':      pygame.Rect(self.n1_box_pos,      (self.input_boxes_width, self.input_boxes_height)),
            'tn1':     pygame.Rect(self.tn1_box_pos,     (self.input_boxes_width, self.input_boxes_height)),
            'pn1':     pygame.Rect(self.pn1_box_pos,     (self.input_boxes_width, self.input_boxes_height)),
            'tcn1':    pygame.Rect(self.tcn1_box_pos,    (self.input_boxes_width, self.input_boxes_height)),
            
            'n2':      pygame.Rect(self.n2_box_pos,      (self.input_boxes_width, self.input_boxes_height)),
            'tn2':     pygame.Rect(self.tn2_box_pos,     (self.input_boxes_width, self.input_boxes_height)),
            'pn2':     pygame.Rect(self.pn2_box_pos,     (self.input_boxes_width, self.input_boxes_height)),
            'tcn2':    pygame.Rect(self.tcn2_box_pos,    (self.input_boxes_width, self.input_boxes_height)),
            
            'n3':      pygame.Rect(self.n3_box_pos,      (self.input_boxes_width, self.input_boxes_height)),
            'tn3':     pygame.Rect(self.tn3_box_pos,     (self.input_boxes_width, self.input_boxes_height)),
            'pn3':     pygame.Rect(self.pn3_box_pos,     (self.input_boxes_width, self.input_boxes_height)),
            'tcn3':    pygame.Rect(self.tcn3_box_pos,    (self.input_boxes_width, self.input_boxes_height)),
            
            'n4':      pygame.Rect(self.n4_box_pos,      (self.input_boxes_width, self.input_boxes_height)),
            'tn4':     pygame.Rect(self.tn4_box_pos,     (self.input_boxes_width, self.input_boxes_height)),
            'pn4':     pygame.Rect(self.pn4_box_pos,     (self.input_boxes_width, self.input_boxes_height)),
            'tcn4':    pygame.Rect(self.tcn4_box_pos,    (self.input_boxes_width, self.input_boxes_height))
        }

        # Create buttons
        self.buttons = {
            'select_sprite': pygame.Rect(self.select_sprite_button_pos, (200, 50)),
            'save': pygame.Rect(self.save_button_pos, (200, 50))
        }

        # Input data
        # Données d'entrée
        self.input_data = {
            'name': '',
            'type1': '','type2': '',
            'pv': '',
            'atk': '',
            'def': '',
            'atk_spe': '',
            'def_spe': '',
            'vitesse': '',
            'n1': '','tn1': '','pn1': '','tcn1': '',
            'n2': '','tn2': '','pn2': '','tcn2': '',
            'n3': '','tn3': '','pn3': '','tcn3': '',
            'n4': '','tn4': '','pn4': '','tcn4': '',
            'sprite': None
        }
        self.active_input = None


    def render_labels(self):
        labels = {
            'name': 'NAME :', 'pv':'PV :',
            'type1': 'TYPE 1 :','type2': 'TYPE 2 :',
            'atk': 'ATK :','atk_spe': 'ATK SPE :',
            'def': 'DEF :','def_spe': 'DEF SPE :',
            'vitesse':'VITESSE :',
            'n1':'Nom :', 'tn1':'TYPE CAP :', 'pn1':'PUISS :', 'tcn1':'SPE/PHY :',
            'x':'CAP 1 :','n2':'CAP 2 :','n3':'CAP 3 :','n4':'CAP 4 :',
        }
        for key, label in labels.items():
            label_surface = self.font.render(label, True, self.black)
            label_rect = label_surface.get_rect()
            if label not in ['CAP 1 :','CAP 2 :','CAP 3 :','CAP 4 :']:
                # Place the label to the left of the input box
                label_rect.topleft = (self.input_boxes[key].x - label_surface.get_width() - 10, self.input_boxes[key].y + 10)
            elif label == 'CAP 1 :':
                label_rect.topleft = (self.input_boxes['n1'].x , self.input_boxes['n1'].y - 20)
            else:
                label_rect.topleft = (self.input_boxes[key].x , self.input_boxes[key].y - 20)
            self.screen.blit(label_surface, label_rect.topleft)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 1 is the mouse left button
                    self.handle_click(event.pos)
                    # Set the active input box
                    for input_name, input_box in self.input_boxes.items():
                        if input_box.collidepoint(event.pos):
                            self.active_input = input_name
                            break
                    else:
                        self.active_input = None  # Clicked outside any box, so deselect
            elif event.type == pygame.KEYDOWN:
                if self.active_input:
                    if event.key == pygame.K_BACKSPACE:
                        self.input_data[self.active_input] = self.input_data[self.active_input][:-1]
                    elif event.key == pygame.K_RETURN:
                        self.active_input = None  # Deselect input box when enter is pressed
                    else:
                        self.input_data[self.active_input] += event.unicode
        return True


    def handle_click(self, position):
        # Check if any of the buttons were clicked
        for button_name, button_rect in self.buttons.items():
            if button_rect.collidepoint(position):
                if button_name == 'select_sprite':
                    self.select_sprite()
                elif button_name == 'save':
                    self.save_pokemon()
                break  # If a button was clicked, no need to check the others


    # Placeholder methods for select_sprite and save_pokemon
    def select_sprite(self):
        # Open a file dialog to select a sprite
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        sprite_path = filedialog.askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        if sprite_path:
            self.input_data['sprite'] = sprite_path 


    def save_pokemon(self):
        print("Attempting to save the pokemon...")  # Debug print
        # Check if all fields are filled
        if not all(self.input_data.values()):
            print("Some fields are missing.")
            return

        # Move the sprite image to the pkmnsprites directory
        try:
            if self.input_data['sprite']:
                sprite_filename = os.path.basename(self.input_data['sprite'])
                sprite_destination = os.path.join("assets/Pokemon/Back", sprite_filename)
                sprite_destination2 = os.path.join("assets/Pokemon/Face", sprite_filename)
                shutil.copy(self.input_data['sprite'], sprite_destination)
                shutil.copy(self.input_data['sprite'], sprite_destination2)
                print(f"Sprite moved to {sprite_destination} and {sprite_destination2}")
        except Exception as e:
            print(f"An error occurred while moving the sprite: {e}")
            return

    # Construire la structure de données pour le fichier JSON
        pokemon_data = {
            "Name": self.input_data["name"],
            "Stat": {
                "PV": self.input_data["pv"],  
                "Attaque": int(self.input_data["atk"]),
                "Defense": int(self.input_data["def"]),
                "Attaque_Speciale": self.input_data["atk_spe"],  
                "Defense_Speciale": self.input_data["def_spe"],  
                "Vitesse": self.input_data["vitesse"]
            },
            "Type": {
                "Type1": self.input_data["type1"],
                "Type2": self.input_data["type2"]
            },
            "atk1": {
                "Name": self.input_data["n1"], "type": self.input_data["tn1"], "power": self.input_data["pn1"], "precision": 100, "tcap": self.input_data["tcn1"]
            },
            "atk2": {
                "Name": self.input_data["n2"], "type": self.input_data["tn2"], "power": self.input_data["pn2"], "precision": 100, "tcap": self.input_data["tcn2"]
            },
            "atk3": {
                "Name": self.input_data["n3"], "type": self.input_data["tn3"], "power": self.input_data["pn3"], "precision": 100, "tcap": self.input_data["tcn3"]
            },
            "atk4": {
                "Name": self.input_data["n4"], "type": self.input_data["tn4"], "power": self.input_data["pn4"], "precision": 100, "tcap": self.input_data["tcn4"]
            },
            "scale": {
                "width": 150, "height": 150
            },
            "cut": {
                "width": 150, "height": 150
            }
        }

        try:
            pokemon_list = []
            pokemon_list.append(pokemon_data)

            with open(f"assets/Pokemon/Json add/{self.input_data["name"]}.json", 'w') as file:
                json.dump(pokemon_list, file, indent=4)
            
            print("Pokemon saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving the Pokemon: {e}")

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            # Clear the screen and draw the background
            self.screen.blit(self.background, (0, 0))
            # Render labels for input boxes
            self.render_labels()
            # Draw input boxes and text within them
            for key, box in self.input_boxes.items():
                text_surface = self.font.render(self.input_data[key], True, self.black)
                # Adjust the width of the box if the text is too long
                box.w = max(self.input_boxes_width, text_surface.get_width() + 10)
                # Draw the input box
                pygame.draw.rect(self.screen, self.white, box)
                pygame.draw.rect(self.screen, self.black, box, 2)  # Border for the box
                # Blit the text surface onto the screen at the position of the input box
                self.screen.blit(text_surface, (box.x + 5, box.y + 5))

            # Draw buttons
            for button_name, button_rect in self.buttons.items():
                button_text = self.font.render(button_name.replace('_', ' ').title(), True, self.black)
                pygame.draw.rect(self.screen,  self.white, button_rect)
                pygame.draw.rect(self.screen, self.black, button_rect, 2)  # Border for the button
                # Center the text on the button
                self.screen.blit(button_text, (button_rect.x + (button_rect.width - button_text.get_width()) // 2, 
                                               button_rect.y + (button_rect.height - button_text.get_height()) // 2))
            pygame.display.flip()  # Update the full display Surface to the screen

        pygame.quit()

if __name__ == "__main__":
    pokemon_add_app = addpokemon()
    pokemon_add_app.run()