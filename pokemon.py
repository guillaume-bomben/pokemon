class pokemon:
    def __init__(self, name,lv=1):
        self.lv = lv
        self.xp = 0
        with open(f"{name}.json","r") as pok:
            self.name = pok["Name"]
            self.type1 = pok["type1"]
            self.type2 = pok["type2"]
            
            if lv == 1:
                self.pv = pok["PV"]
                self.attaque = pok["Attaque"]
                self.defense = pok["Defense"]
                self.attaque_special = pok["Attaque_Speciale"]
                self.defence_special = pok["Defense_Speciale"]
                self.vitesse = pok["Vitesse"]
            else:
                self.recalcul_stat()

    def __str__(self):
        return f"{self.name} , LV-{self.lv}: HP-{self.pv}, Attaque-{self.attaque}, Défense-{self.defense}, Attaque Spé-{self.attaque_special}, Défense Spé-{self.defence_special}, Vitesse-{self.vitesse}, Type1-{self.type1}, Type2-{self.type2}"
    
    def recalcul_stat(self):
        with open(f"{self.name}.json","r") as pok:
            self.pv = (2*pok["PV"]) * (self.lv / 100) + self.lv + 10
            self.attaque = (2*pok["Attaque"]) * (self.lv / 100) + self.lv + 10
            self.defense = (2*pok["Defense"]) * (self.lv / 100) + self.lv + 10
            self.attaque_special = (2*pok["Attaque_Speciale"]) * (self.lv / 100) + self.lv + 10
            self.defence_special = (2*pok["Defense_Speciale"]) * (self.lv / 100) + self.lv + 10
            self.vitesse = (2*pok["Vitesse"]) * (self.lv / 100) + self.lv + 10

    def xp_gains(self,xpadd):
        self.xp += xpadd
        if self.xp >= self.lv ** 3:
            self.lv += 1
            self.xp -= self.lv ** 3
            self.recalcul_stat()