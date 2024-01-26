import json

class pokemon:
    def __init__(self, name,lv=1,xp=0):
        #Initialisation d'un pokémon avec un niveau et une expérience donnés
        self.lv = lv #niveau du Pokémon
        self.xp = xp #Expérience du Pokémon
        with open(f"assets/Pokemon/Json/{name}.json","r") as pok:
            data = json.load(pok)  # Chargement du contenu du fichier JSON
            self.name = data["Name"] #Nom du pokémon
            self.type1 = data["Type"]["Type1"] #Premier type
            self.type2 = data["Type"]["Type2"] #Deuxième type
            self.recalcul_stat() #Calcul initial des statistiques du Pokémon

    def __str__(self):
        #Représentation sous forme de chaîne du Pokémon pour l'affichage 
        return f"{self.name} , LV-{self.lv}: HP-{self.pv}, Attaque-{self.attaque}, Défense-{self.defense}, Attaque Spé-{self.attaque_special}, Défense Spé-{self.defence_special}, Vitesse-{self.vitesse}, Type1-{self.type1}, Type2-{self.type2}"
    
    def recalcul_stat(self):
        #Recalcul des statistiques du Pokémon en fonction de son niveau 
        with open(f"assets/Pokemon/Json/{self.name}.json","r") as pok:
            data = json.load(pok)  # Chargez le contenu du fichier JSON
            #Calcul des statistiques en fonction du niveau et des statistiques de base
            self.pvmax = ((2*data["Stat"]["PV"] * (self.lv) / 100) + self.lv + 10)//1
            self.pv = ((2*data["Stat"]["PV"]) * (self.lv / 100) + self.lv + 10)//1
            self.attaque = ((2*data["Stat"]["Attaque"]) * (self.lv / 100) + self.lv + 10)//1
            self.defense = ((2*data["Stat"]["Defense"]) * (self.lv / 100) + self.lv + 10)//1
            self.attaque_special = ((2*data["Stat"]["Attaque_Speciale"]) * (self.lv / 100) + self.lv + 10)//1
            self.defence_special = ((2*data["Stat"]["Defense_Speciale"]) * (self.lv / 100) + self.lv + 10)//1
            self.vitesse = ((2*data["Stat"]["Vitesse"]) * (self.lv / 100) + self.lv + 10)//1

    def xp_gains(self,xpadd):
        #Gestion de l'ajout d'expérience et de la montée en niveau 
        self.xp += xpadd #Ajout de l'expérience
        #Boucle pour la gestion des montées de niveau  
        while self.xp >= self.lv ** 3:
            if self.xp >= self.lv ** 3:
                self.xp -= self.lv ** 3 #Diminution de l'expérience après la montée de niveau 
                self.lv += 1 #Augmentation du niveau 
                self.recalcul_stat() #Recalcul des statistiques après la montée de niveau 