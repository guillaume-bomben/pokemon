class Keylistener:
    def __init__(self):
        #Initialisation d'une liste pour stocker les touches appuyées
        self.keys: list[int] = []

    def add_keys(self, key):
        #Ajoute une touche à la liste si elle n'est pas déjà présente 
        if key not in self.keys:
            self.keys.append(key)

    def remove_key(self, key):
        #Retire une touche de la liste si elle y est présente
        if key in self.keys:
            self.keys.remove(key)

    def key_pressed(self, key):
        #Retourne True si la touche spécifiée est dans la liste des touches appuyées
        return key in self.keys
    
    def clear(self):
        #Vide la liste des touches appuyées
        self.keys.clear()