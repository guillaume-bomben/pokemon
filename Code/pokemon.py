import json

class pokemon:
    def __init__(self, name,lv=1,xp=0):
        self.lv = lv
        self.xp = xp
        with open(f"assets/Pokemon/Json/{name}.json","r") as pok:
            data = json.load(pok)  # Chargez le contenu du fichier JSON
            self.name = data["Name"]
            self.type1 = data["Type"]["Type1"]
            self.type2 = data["Type"]["Type2"]
            self.recalcul_stat()

    def __str__(self):
        return f"{self.name} , LV-{self.lv}: HP-{self.pv}, Attaque-{self.attaque}, Défense-{self.defense}, Attaque Spé-{self.attaque_special}, Défense Spé-{self.defence_special}, Vitesse-{self.vitesse}, Type1-{self.type1}, Type2-{self.type2}"
    
    def recalcul_stat(self):
        with open(f"assets/Pokemon/Json/{self.name}.json","r") as pok:
            data = json.load(pok)  # Chargez le contenu du fichier JSON
            self.pvmax = ((2*data["Stat"]["PV"] * (self.lv) / 100) + self.lv + 10)//1
            self.pv = ((2*data["Stat"]["PV"]) * (self.lv / 100) + self.lv + 10)//1
            self.attaque = ((2*data["Stat"]["Attaque"]) * (self.lv / 100) + self.lv + 10)//1
            self.defense = ((2*data["Stat"]["Defense"]) * (self.lv / 100) + self.lv + 10)//1
            self.attaque_special = ((2*data["Stat"]["Attaque_Speciale"]) * (self.lv / 100) + self.lv + 10)//1
            self.defence_special = ((2*data["Stat"]["Defense_Speciale"]) * (self.lv / 100) + self.lv + 10)//1
            self.vitesse = ((2*data["Stat"]["Vitesse"]) * (self.lv / 100) + self.lv + 10)//1

    def xp_gains(self,xpadd):
        self.xp += xpadd
        while self.xp >= self.lv ** 3:
            if self.xp >= self.lv ** 3:
                self.xp -= self.lv ** 3
                self.lv += 1
                self.recalcul_stat()