class pokemon_Liste:
    def __init__(self,name,PV,Attaque,Defense,Attaque_Speciale,Defense_Speciale,Vitesse,type1,type2):
        self.name = name
        self.pv = PV
        self.attaque = Attaque
        self.defence = Defense
        self.attaque_special = Attaque_Speciale
        self.defence_special = Defense_Speciale
        self.vitesse = Vitesse
        self.type1 = type1
        self.type2 = type2
    
    def __str__(self):
        return f"{self.name}: HP-{self.pv}, Attaque-{self.attaque}, Défense-{self.defence}, Attaque Spé-{self.attaque_special}, Défense Spé-{self.defence_special}, Vitesse-{self.vitesse}, Type1-{self.type1}, Type2-{self.type2}"
