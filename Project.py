import random
import sys

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
planet4 = Worlds("Umbara", "Shadow World", "Doonium Ore")


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
        return "the explorer {name} who specializes in {skills} and has an inventory of {fish} Fish, {fuel_cells} Fuel Cells, {crystals} Crystals, and {doonium} Doonium Ore.".format(
            name=self.name, skills=self.skills, fish=self.fish, fuel_cells=self.fuel_cells, crystals=self.crystals,
            doonium=self.doonium)

    def select_activity(self):
        asteroid_chance = random.randint(1, 5)
        # if the random number is 1, the character is hit by an asteroid and ends the game
        if asteroid_chance == 1:
            print(
                f"\n OH NOO! An asteroid has hit {self.name} when they were trying to mine resources!! {self.name} has died!!")
            print('''
              ____    _    __  __ _____    _____     _______ ____  
             / ___|  / \  |  \/  | ____|  / _ \ \   / / ____|  _ \ 
            | |  _  / _ \ | |\/| |  _|   | | | \ \ / /|  _| | |_) |
            | |_| |/ ___ \| |  | | |___  | |_| |\ V / | |___|  _ < 
             \____/_/   \_\_|  |_|_____|  \___/  \_/  |_____|_| \_\                                            
            '''
                  )
            sys.exit()

        actions = ["Mine Fuel Cells", "Fishing", "Mine Doonium Ore", "Mine Crystals"]
        print(""
              "")
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
        world_list = [planet1, planet2, planet3, planet4]
        chosen_planet = None

        while chosen_planet is None:
            print("\nWhere would you like to travel to today? Your current choices are:")
            for i, world in enumerate(world_list, start=1):
                print(str(i) + ". " + world.name)

            try:
                travel_worlds = int(input())
                chosen_planet = world_list[travel_worlds - 1]
                print('\n' + chosen_planet.name + " is a great destination! ")
                print(str(chosen_planet))
                print("\n")
            except (IndexError, ValueError):
                print("Sorry, this destination is not available!")

            cont = input("Would you like to enter another destination? (yes/no) ")
            if not cont.lower() in ['yes', 'y']:
                break
            else:
                chosen_planet = None  # reset to None so user can choose again

        selected_character.select_activity()

    def mine_crystals(self):
        mined_crystals = random.randint(0, 20)  # Random amount of crystals mined
        self.crystals += mined_crystals
        self.crystal_inventory.append(mined_crystals)
        print(""
              "")
        print(f"******{self.name} mined {mined_crystals} crystals!******")
        print(""
              "")

    def mine_fish(self):
        mined_fish = random.randint(0, 20)  # Random amount of fish mined
        self.fish += mined_fish
        self.fish_inventory.append(mined_fish)
        print(""
              "")
        print(f"******{self.name} caught {mined_fish} fish!******")
        print(""
              "")

    def mine_doonium(self):
        mined_doonium = random.randint(0, 20)  # Random amount of Doonium mined
        self.doonium += mined_doonium
        self.doonium_inventory.append(mined_doonium)
        print(""
              "")
        print(f"******{self.name} mined {mined_doonium} Doonium Ore!******")
        print(""
              "")

    def mine_fuel_cells(self):
        mined_fuel_cells = random.randint(0, 20)  # Random amount of fuel cells mined
        self.fuel_cells += mined_fuel_cells
        self.fuel_inventory.append(mined_fuel_cells)
        print(""
              "")
        print(f"******{self.name} mined {mined_fuel_cells} fuel cells!******")
        print(""
              "")


character1 = Explorers("Aesira", "Fishing")
character2 = Explorers("Evren", "Fuel Cell Mining")
character3 = Explorers("Kamari", "Crystal Mining")
character4 = Explorers("Arik", "Doonium Mining")

characters = [character1, character2, character3, character4]
print(
    '''
 #####                            #                                                           
#     # #####   ##   #####       # #   #####  #    # ###### #    # ##### #    # #####  ###### 
#         #    #  #  #    #     #   #  #    # #    # #      ##   #   #   #    # #    # #      
 #####    #   #    # #    #    #     # #    # #    # #####  # #  #   #   #    # #    # #####  
      #   #   ###### #####     ####### #    # #    # #      #  # #   #   #    # #####  #      
#     #   #   #    # #   #     #     # #    #  #  #  #      #   ##   #   #    # #   #  #      
 #####    #   #    # #    #    #     # #####    ##   ###### #    #   #    ####  #    # ###### 
 '''
)
print("Welcome to Star Adventures! \n")
print("Can you obtain all 4 resources without getting hit by an asteroid??  Lets Play! \n")
print("Choose a character:")
for index, character in enumerate(characters):
    print(f"{index + 1}. {character.name}")

choice = int(input("Enter the number of the character you want to choose: ")) - 1

# Added actions loop

if choice in range(len(characters)):
    selected_character = characters[choice]
    print(f"\n You have selected {selected_character}")

    selected_character.travel()

    game_is_running = True  # flag indicating whether the game is running

    while game_is_running:
        selected_character.select_activity()  # Use new method here

        # Inside main game loop:

        cont = input("Would you like to perform another activity? (yes/no)")
        if cont.lower() == 'yes' or cont.lower() == 'y':
            pass
        elif cont.lower() == 'no' or cont.lower() == 'n':
            while True:
                print("\n What would you like to do? \n")

                print("1. Quit Game")
                print("2. Travel to a Different Planet")
                print("3. Select Another Activity")
                next_action = input("Enter the number of your choice: ")

                if next_action == "1":
                    print(""
                          "")
                    print(f"{selected_character.name} ended the game with the following inventory: \n ")

                    print(
                        f"******Fish: {selected_character.fish}, Fuel cells: {selected_character.fuel_cells}, Crystals: {selected_character.crystals}, Doonium Ore: {selected_character.doonium}******")
                    if selected_character.fish > 0 and selected_character.fuel_cells > 0 and selected_character.crystals > 0 and selected_character.doonium > 0:
                        print(f"\n Congratulations {selected_character.name}!, You are THE Star Adventurer!! \n")
                        print('''
                    ____    ____  ______    __    __     ____    __    ____  __  .__   __.  __  
                    \   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / |  | |  \ |  | |  | 
                     \   \/   / |  |  |  | |  |  |  |     \   \/    \/   /  |  | |   \|  | |  | 
                      \_    _/  |  |  |  | |  |  |  |      \            /   |  | |  . `  | |  | 
                        |  |    |  `--'  | |  `--'  |       \    /\    /    |  | |  |\   | |__| 
                        |__|     \______/   \______/         \__/  \__/     |__| |__| \__| (__) 
                                                                            
                                           
                        ''')
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
