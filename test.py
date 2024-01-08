from pokemon import Pokemon
import csv

liste = []
with open("pokemon_liste.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        row[0] = Pokemon(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        liste.append(row[0])

for pokemon in liste:
    print(pokemon)


