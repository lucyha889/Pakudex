from luh_pakuri import Pakuri
class Pakudex:
    #Initialize the Pakudex with a specified capacity with the default being 20
    def __init__(self, capacity= 20):
        self.capacity = capacity
        self.size = 0
        self.pakuri_list = [] 

    def get_size(self):
        #Return the current number of Pakuri in the Pakudex
        return len(self.pakuri_list)

    def get_capacity(self):
        #Return the maximum capacity of the Pakudex
        return self.capacity

    def get_species_array(self):
        #Return a list of species names of the Pakuri in the Pakudex
        if self.pakuri_list:
            return [pakuri.get_species() for pakuri in self.pakuri_list]
        return None

    def get_stats(self, species):
        #Return a list containing the attack, defense, and speed stats of the specified species
        for pakuri in self.pakuri_list:
            if pakuri.get_species() == species:
                return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        return None

    def sort_pakuri(self):
        #Sort the Pakuri in the Pakudex alphabetically by species name
        self.pakuri_list.sort(key=lambda pakuri: pakuri.get_species())

    def add_pakuri(self, species):
        #Add a new Pakuri with the specified species name to the Pakudex and return False if already exists
        if self.size == self.capacity:
            return False
        if any(pakuri.get_species() == species for pakuri in self.pakuri_list):
            return False
        self.pakuri_list.append(Pakuri(species))
        return True

    def evolve_species(self, species):
        #Evolve the specified species of Pakuri in the Pakudex
        for pakuri in self.pakuri_list:
            if pakuri.get_species() == species:
                pakuri.evolve()
                return True
        return False