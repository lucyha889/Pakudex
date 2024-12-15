class Pakuri:
    def __init__(self, species):
        #Initialize Pakuri attributes
        self.species = species
        self.attack = len(species) * 7 + 9
        self.defense = len(species) * 5 + 17
        self.speed = len(species) * 6 + 13

    def get_species(self):
        #Return species name
        return self.species

    def get_attack(self):
        #Return attack value
        return self.attack

    def get_defense(self):
        #Return defense value
        return self.defense

    def get_speed(self):
        #Return speed value
        return self.speed

    def set_attack(self, new_attack):
        #Update attack value
        self.attack = new_attack

    def evolve(self):
        #Evolve Pakuri
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3 