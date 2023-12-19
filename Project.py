import random

character_list = ("Aesira", "Evrin", "Kamari", "Arik")


class Worlds:
    def __init__(self, name, types, resources):
        self.name = name
        self.types = types
        self.resources = resources

    def __repr__(self):
        return "Welcome to the planet {name}! This planet is a {types} planet, rich in {resources}.".format(
            name=self.name, types=self.types, resources=self.resources)


planet_list = ("Naboo", "Bespin", "Iium", "Umbara")

planet1 = Worlds("Naboo", "Swampland", "Fishing")
planet2 = Worlds("Bespin", "Gas Giant", "Fuel")
planet3 = Worlds("Iium", "Rocky", "Crystals")
planet4 = Worlds("Umbara", "Shadow World", "Doonium")


class Explorers:
    def __init__(self, name, skills, num_fish=0, num_fuel_cells=0, num_crystals=0, num_doonium=0):
        self.name = name
        self.skills = skills
        self.fish = num_fish
        self.fuel_cells = num_fuel_cells
        self.crystals = num_crystals
        self.doonium = num_doonium
        self.fish_inventory = []
        self.fuel_inventory = []
        self.crystal_inventory = []
        self.doonium_inventory = []

    def __repr__(self):
        return "the explorer {name} who specializes in {skills} and has an inventory of {fish} Fish, {fuel_cells} Fuel Cells, {crystals} Crystals, and {doonium} Doonium Ores.".format(
            name=self.name, skills=self.skills, fish=self.fish, fuel_cells=self.fuel_cells, crystals=self.crystals,
            doonium=self.doonium)

    def select_activity(self):
        actions = ["Mine Fuel Cells", "Fishing", "Mine Doonium", "Mine Crystals"]
        print("What activity would you like to do?")
        for i, action in enumerate(actions, 1):
            print(f"{i}. {action}")
        activity = int(input("Enter the number of the activity: ")) - 1

        if activity == 0:
            self.mine_fuel_cells()
        elif activity == 1:
            self.mine_fish()
        elif activity == 2:
            self.mine_doonium()
        elif activity == 3:
            self.mine_crystals()
        else:
            print("Invalid activity.")

    def travel(self):
        while True:
            travel_worlds = input(
                "Where would you like to travel to today? Your current choices are " + str(planet_list) + " ")
            if str(travel_worlds) == "Naboo":
                print(travel_worlds + " is a great destination! " + str(planet1))
            elif str(travel_worlds) == "Bespin":
                print(travel_worlds + " is a great destination! " + str(planet2))
            elif str(travel_worlds) == "Iium":
                print(travel_worlds + " is a great destination! " + str(planet3))
            elif str(travel_worlds) == "Umbara":
                print(travel_worlds + " is a great destination! " + str(planet4))
            else:
                print("Sorry this destination is not available!")

            cont = input("Would you like to enter another destination? (yes/no)")
            if cont.lower() != 'yes':
                break

    def mine_crystals(self):
        mined_crystals = random.randint(0, 20)  # Random amount of crystals mined
        self.crystals += mined_crystals
        self.crystal_inventory.append(mined_crystals)
        print(f"{self.name} mined {mined_crystals} crystals!")

    def mine_fish(self):
        mined_fish = random.randint(0, 20)  # Random amount of fish mined
        self.fish += mined_fish
        self.fish_inventory.append(mined_fish)
        print(f"{self.name} mined {mined_fish} fish!")

    def mine_doonium(self):
        mined_doonium = random.randint(0, 20)  # Random amount of Doonium mined
        self.doonium += mined_doonium
        self.doonium_inventory.append(mined_doonium)
        print(f"{self.name} mined {mined_doonium} Doonium!")

    def mine_fuel_cells(self):
        mined_fuel_cells = random.randint(0, 20)  # Random amount of fuel cells mined
        self.fuel_cells += mined_fuel_cells
        self.fuel_inventory.append(mined_fuel_cells)
        print(f"{self.name} mined {mined_fuel_cells} fuel cells!")


character1 = Explorers("Aesira", "Fishing")
character2 = Explorers("Evren", "Fuel Cell Mining")
character3 = Explorers("Kamari", "Crystal Mining")
character4 = Explorers("Arik", "Doonium Mining")

characters = [character1, character2, character3, character4]

print("Welcome to Star Adventures!")
print("Choose a character:")
for index, character in enumerate(characters):
    print(f"{index + 1}. {character.name}")

choice = int(input("Enter the number of the character you want to choose: ")) - 1

# Added actions loop

if choice in range(len(characters)):
    selected_character = characters[choice]
    print(f"You have selected {selected_character}")

    selected_character.travel()

    game_is_running = True  # flag indicating whether the game is running

    while game_is_running:
        selected_character.select_activity()  # Use new method here

        # Inside main game loop:

        cont = input("Would you like to perform another activity? (yes/no)")
        if cont.lower() == 'yes':
            # continue with your code
            pass
        elif cont.lower() == 'no':
            while True:
                print("What would you like to do?")
                print("1. Quit Game")
                print("2. Travel to a Different Planet")
                print("3. Select Another Activity")
                next_action = input("Enter the number of your choice: ")

                if next_action == "1":
                    print(f"{selected_character.name} ended the game with the following inventory:")
                    print(
                        f"Fish: {selected_character.fish}, Fuel cells: {selected_character.fuel_cells}, Crystals: {selected_character.crystals}, Doonium: {selected_character.doonium}")
                    game_is_running = False  # stop the game
                    break
                elif next_action == "2":
                    selected_character.travel()
                elif next_action == "3":
                    selected_character.select_activity()
                else:
                    print("Invalid selection.")
        else:
            print("Invalid selection.")
