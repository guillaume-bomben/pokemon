class Pokemon:
    def __init__(self,name,PV,Attaque,Defense,Attaque_Speciale,Defense_Speciale,Vitesse):
        self.name = name
        self.pv = PV
        self.attaque = Attaque
        self.defence = Defense
        self.attaque_special = Attaque_Speciale
        self.defence_special = Defense_Speciale
        self.vitesse = Vitesse
    
    def __str__(self):
        return f"{self.name}: HP-{self.pv}, Attaque-{self.attaque}, Défense-{self.defence}, Attaque Spé-{self.attaque_special}, Défense Spé-{self.defence_special}, Vitesse-{self.vitesse}"


    '''
    def learn_attack(self, attack_name):
        self.attacks.append(attack_name)
        

    def increase_level(self):
        self.level += 1
        self.evolve()

    def gain_experience(self, exp_points):
        self.xp += exp_points
        while self.xp >= 50:
            self.increase_level()
            self.xp -= 50

    def evolve(self):
        if self.level >= self.level_required:
            # Évoluer le Pokémon
            self.name = self.evolved_form
            print(f"{self.name} a évolué en {self.evolved_form.name} !")
        else:
            print(f"{self.name} n'a pas atteint le niveau requis pour évoluer en {self.evolved_form.name}.")
'''