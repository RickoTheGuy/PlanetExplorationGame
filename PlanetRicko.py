import random

class Planet:
    def __init__(self, name, terrain, hazard_level, elements):
        self.name = name
        self.terrain = terrain
        self.hazard_level = hazard_level
        self.elements = elements