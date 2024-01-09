from pokemon_Liste import pokemon_Liste
import csv

liste = []
i=0
with open("pokemon_liste.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        id = f"id-{i}"
        id = pokemon_Liste(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7],row[8])
        liste.append(id)
        i +=1

for pokemon in liste:
    print(pokemon)


