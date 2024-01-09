from pokemon_Liste import pokemon_Liste

class pokemon(pokemon_Liste):
    def __init__(self, name, PV, Attaque, Defense, Attaque_Speciale, Defense_Speciale, Vitesse,type1,type2,lv=1):
        super().__init__(name, PV, Attaque, Defense, Attaque_Speciale, Defense_Speciale, Vitesse,type1,type2)
        self.name = name
        self.lv = lv
        self.xp = 0
        self.type1 = type1
        self.type2 = type2
        if lv == 1:
            self.ppv = PV
            self.pattaque = Attaque
            self.pdefence = Defense
            self.pattaque_special = Attaque_Speciale
            self.pdefence_speciale = Defense_Speciale
            self.pvitesse = Vitesse
        else:
            self.recalcul_stat()

    def recalcul_stat(self):
        self.ppv = (2*self.pv) * (self.lv / 100) + self.lv + 10
        self.pattaque = (2*self.attaque) * (self.lv / 100) + self.lv + 10
        self.pdefence = (2*self.defence) * (self.lv / 100) + self.lv + 10
        self.pattaque_special = (2*self.attaque_special) * (self.lv / 100) + self.lv + 10
        self.pdefence_speciale = (2*self.defence_special) * (self.lv / 100) + self.lv + 10
        self.pvitesse = (2*self.vitesse) * (self.lv / 100) + self.lv + 10

    def xp_gains(self,xpadd):
        self.xp += xpadd
        if self.xp >= self.lv ** 3:
            self.lv += 1
            self.xp -= self.lv ** 3
            self.recalcul_stat()