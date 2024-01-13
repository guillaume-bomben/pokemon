import csv
import json
import os

def convert_csv_to_json(input_csv_path, output_json_folder):
    # Créer un dossier de sortie s'il n'existe pas
    if not os.path.exists(output_json_folder):
        os.makedirs(output_json_folder)

    # Ouvrir le fichier CSV en mode lecture
    with open(input_csv_path, 'r') as csv_file:
        # Lire le fichier CSV avec DictReader
        csv_reader = csv.reader(csv_file)

        # Parcourir chaque ligne du fichier CSV
        for row in csv_reader:
            # Créer une structure de données pour le fichier JSON
            json_data = {
                "Name": row[0],
                "Stat": {
                    "PV": int(row[1]),
                    "Attaque": int(row[2]),
                    "Defense": int(row[3]),
                    "Attaque_Speciale": int(row[4]),
                    "Defense_Speciale": int(row[5]),
                    "Vitesse": int(row[6])
                },
                "Type": {
                    "Type1": row[7],
                    "Type2": row[8]
                }
            }

            # Créer un nom de fichier unique basé sur le nom du Pokémon
            json_filename = f'{row[0]}.json'

            # Chemin complet pour le fichier JSON de sortie
            json_filepath = os.path.join(output_json_folder, json_filename)

            # Écrire la structure de données dans le fichier JSON
            with open(json_filepath, 'w') as json_file:
                json.dump(json_data, json_file, indent=2)

# Exemple d'utilisation
convert_csv_to_json('pokemon_liste.csv', 'assets/Pokemon/Json')
