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

        return Planet(
            name=random.choice(names),
            terrain=random.choice(terrains),
            hazard_level=random.choice(hazards),
            elements=selected_elements
        )

    def display_status(self):
        p = self.current_planet
        print("\n=== GALACTIC SCAVENGER: ELEMENTUM ===")
        print(f"🪐 Planet: {p.name}")
        print(f"🌎 Terrain: {p.terrain}")
        print(f"⚠️ Hazard Level: {p.hazard_level}")
        print(f"🧪 Elements Detected: {', '.join(p.elements)}")
        print(f"⛽ Fuel Remaining: {self.fuel} units\n")

    def main_menu(self):
        while True:
            self.display_status()
            print("[1] Land and Mine")
            print("[2] Scan Next Planet")
            print("[3] View Inventory")
            print("[4] Return to Base")
            print("[5] Quit")

            choice = input("\nChoose an action: ")
            if choice == "1":
                self.mine_elements()
            elif choice == "2":
                self.scan_next_planet()
            elif choice == "3":
                self.view_inventory()
            elif choice == "4":
                print("🚀 Returning to base...")
                break
            elif choice == "5":
                print("👋 Goodbye, explorer.")
                break
            else:
                print("Invalid choice.")