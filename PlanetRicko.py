import random

class Planet:
    def __init__(self, name, terrain, hazard_level, elements):
        self.name = name
        self.terrain = terrain
        self.hazard_level = hazard_level
        self.elements = elements

class GameUI:
    def __init__(self):
        self.fuel = 100
        self.inventory = {}
        self.current_planet = self.generate_planet()

    def generate_planet(self):
        names = ["Crythas IV", "Zoron Beta", "Krelon Prime", "Myrrh 3"]
        terrains = ["Volcanic", "Icy", "Desert", "Toxic Swamp", "Rocky"]
        hazards = ["LOW", "MEDIUM", "HIGH"]
        all_elements = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Fe", "U", "S"]
        selected_elements = random.sample(all_elements, 3)