import json

class pokemon:
    def __init__(self, name,lv=1):
        self.lv = lv
        self.xp = 0
        with open(f"assets/Pokemon/Json/{name}.json","r") as pok:
            data = json.load(pok)  # Chargez le contenu du fichier JSON
            self.name = data["Name"]
            self.type1 = data["Type"]["Type1"]
            self.type2 = data["Type"]["Type2"]

            if lv == 1:
                self.pv = data["Stat"]["PV"]
                self.attaque = data["Stat"]["Attaque"]
                self.defense = data["Stat"]["Defense"]
                self.attaque_special = data["Stat"]["Attaque_Speciale"]
                self.defence_special = data["Stat"]["Defense_Speciale"]
                self.vitesse = data["Stat"]["Vitesse"]
            else:
                self.recalcul_stat()

    def __str__(self):
        return f"{self.name} , LV-{self.lv}: HP-{self.pv}, Attaque-{self.attaque}, Défense-{self.defense}, Attaque Spé-{self.attaque_special}, Défense Spé-{self.defence_special}, Vitesse-{self.vitesse}, Type1-{self.type1}, Type2-{self.type2}"
    
    def recalcul_stat(self):
        with open(f"assets/Pokemon/Json/{self.name}.json","r") as pok:
            data = json.load(pok)  # Chargez le contenu du fichier JSON
            self.pv = (2*data["Stat"]["PV"]) * (self.lv / 100) + self.lv + 10
            self.attaque = (2*data["Stat"]["Attaque"]) * (self.lv / 100) + self.lv + 10
            self.defense = (2*data["Stat"]["Defense"]) * (self.lv / 100) + self.lv + 10
            self.attaque_special = (2*data["Stat"]["Attaque_Speciale"]) * (self.lv / 100) + self.lv + 10
            self.defence_special = (2*data["Stat"]["Defense_Speciale"]) * (self.lv / 100) + self.lv + 10
            self.vitesse = (2*data["Stat"]["Vitesse"]) * (self.lv / 100) + self.lv + 10

    def xp_gains(self,xpadd):
        self.xp += xpadd
        if self.xp >= self.lv ** 3:
            self.lv += 1
            self.xp -= self.lv ** 3
            self.recalcul_stat()