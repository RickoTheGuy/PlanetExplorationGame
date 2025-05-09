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
        self.planet_log = []
        self.planet_log.append(self.current_planet.name)


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

    def mine_elements(self):
        print("\n🔧 Mining elements...")
        
        # Mine current planet's elements
        for element in self.current_planet.elements:
            self.inventory[element] = self.inventory.get(element, 0) + 1

        self.fuel -= 10

        # Emergency fuel tank if fuel hits zero
        if self.fuel <= 0 and not self.emergency_used:
            print("🚨 Emergency fuel tank activated! +15 fuel.")
            self.fuel = 15
            self.emergency_used = True

        # Fuel bonus for safe, low-hazard planets
        if self.current_planet.hazard_level == "LOW":
            self.fuel += 3
            print("⛽ Efficient mining! Recovered 3 fuel from stable terrain.")

        # Rare element jackpot chance
        if random.random() < 0.03:
            rare = random.choice(["Au", "Pt", "Un"])
            self.inventory[rare] = self.inventory.get(rare, 0) + 1
            print(f"💎 JACKPOT! You struck {rare}!")

        # Alien artifact find
        if random.random() < 0.05:
            self.inventory["Alien Artifact"] = self.inventory.get("Alien Artifact", 0) + 1
            print("🛸 You found a mysterious Alien Artifact...")

        # Element fusion if enough of one kind is gathered
        for elem, qty in list(self.inventory.items()):
            if qty >= 3:
                fusion = f"{elem}X"
                self.inventory[fusion] = self.inventory.get(fusion, 0) + 1
                self.inventory[elem] -= 3
                if self.inventory[elem] <= 0:
                    del self.inventory[elem]
                print(f"⚗️ Fusion Complete! {elem} → {fusion}")
                break  # One fusion per trip

        # Hazard-based item loss
        if self.current_planet.hazard_level == "HIGH" and random.random() < 0.3:
            if self.inventory:
                lost = random.choice(list(self.inventory.keys()))
                self.inventory[lost] -= 1
                if self.inventory[lost] <= 0:
                    del self.inventory[lost]
                print(f"🔥 Mining accident! You lost some {lost}.")

        # Mined elements confirmation
        print(f"✅ Mined {', '.join(self.current_planet.elements)}!\n")


        self.fuel -= 10
        print(f"✅ Mined {', '.join(self.current_planet.elements)}!\n")

    def scan_next_planet(self):
        print("\n🔭 Scanning new planet...")

        # Fuel-efficient scan perk (25% chance scan is free)
        if random.random() < 0.25:
            print("🔋 Your scanner ran in eco-mode! No fuel used.")
        else:
            self.fuel -= 5

        # Emergency fuel tank if fuel hits zero
        if self.fuel <= 0 and not self.emergency_used:
            print("🚨 Emergency fuel tank activated! +15 fuel.")
            self.fuel = 15
            self.emergency_used = True

        self.current_planet = self.generate_planet()

        # Bonus intel from scanner
        if random.random() < 0.25:
            print("📡 Scanner Bonus: Rich mineral veins detected!")
        elif self.current_planet.hazard_level == "HIGH" and random.random() < 0.25:
            print("⚠️ Warning: Hazard levels off the charts. Proceed with caution.")


    def view_inventory(self):
        print("\n📦 Inventory:")
        if not self.inventory:
            print("  (Empty)")
        else:
            for elem, qty in self.inventory.items():
                print(f"  {elem}: {qty}")
        print()

if __name__ == "__main__":
    game = GameUI()
    game.main_menu()