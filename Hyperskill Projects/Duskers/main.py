import random
import sys
import json
from datetime import datetime


class DuskersGame:
    TITLE_BANNER = """+=============================================================================+
     ######*   ##*   ##*  #######*  ##*  ##*  #######*  ######*   #######*
     ##*  ##*  ##*   ##*  ##*       ##* ##*   ##*       ##*  ##*  ##*
     ##*  ##*  ##*   ##*  #######*  #####*    #####*    ######*   #######*
     ##*  ##*  ##*   ##*       ##*  ##* ##*   ##*       ##*  ##*       ##*
     ######*    ######*   #######*  ##*  ##*  #######*  ##*  ##*  #######*
                         (Survival ASCII Strategy Game)
+=============================================================================+"""

    ROBOT_ASCII = ["  $   $$$$$$$   $",
                   "  $$$$$     $$$$$",
                   "      $$$$$$$    ",
                   "     $$$   $$$   ",
                   "     $       $   "]

    DEFAULT_LOCATIONS = ["Nuclear_power_plant_wreckage", "Old_beach_bar", "Abandoned_factory", "Empty_warehouse"]

    def __init__(self):
        self.player_name = ""
        self.titanium = 0
        self.robots = 3
        self.locations = []
        self.available_locations = []
        self.initialize_game_settings()
        self.upgrades = [False, False]

    def save_game(self, slot):
        save_data = {
            "player_name": self.player_name,
            "titanium": self.titanium,
            "robots": self.robots,
            "upgrades": self.upgrades,
            "save_time": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        filename = f"save_file_{slot}.json"
        with open(filename, 'w') as f:
            json.dump(save_data, f)

        print("                        |==============================|")
        print("                        |    GAME SAVED SUCCESSFULLY   |")
        print("                        |==============================|")

    def load_game(self, slot):
        filename = f"save_file_{slot}.json"
        try:
            with open(filename, 'r') as f:
                save_data = json.load(f)
                self.player_name = save_data["player_name"]
                self.titanium = save_data["titanium"]
                self.upgrades = save_data["upgrades"]
                self.robots = save_data["robots"]

                print("                        |==============================|")
                print("                        |    GAME LOADED SUCCESSFULLY  |")
                print("                        |==============================|")
                print(f" Welcome back, commander {self.player_name}!")
                return True
        except FileNotFoundError:
            print("Empty slot!\n")
            return False

    @staticmethod
    def display_save_slots():
        print("   Select save slot:")
        for slot in range(1, 4):
            filename = f"save_file_{slot}.json"
            try:
                with open(filename, 'r') as f:
                    save_data = json.load(f)
                    print(f"    [{slot}] {save_data['player_name']} "
                          f"Titanium: {save_data['titanium']} "
                          f"Robots: {save_data['robots']} "
                          f"Last save: {save_data['save_time']}")
            except FileNotFoundError:
                print(f"    [{slot}] empty")

        print("\nYour command:")

    def handle_save_command(self):
        self.display_save_slots()
        while True:
            command = input().lower()
            if command == "back":
                return False
            if command in ["1", "2", "3"]:
                self.save_game(command)
                return True
            print("Invalid input")

    def handle_load_command(self):
        while True:
            self.display_save_slots()
            command = input().lower()
            if command == "back":
                return False
            if command in ["1", "2", "3"]:
                if self.load_game(command):
                    self.display_hub()
                    return True
            else:
                print("Invalid input")

    def initialize_game_settings(self):
        if len(sys.argv) > 4:
            random.seed(sys.argv[1])
            self.locations = sys.argv[4].split(',')
        else:
            random.seed()
            self.locations = self.DEFAULT_LOCATIONS

    def handle_exploration(self):
        num_locations = random.randint(1, 9)
        self.available_locations = []
        print("Searching...")
        location = random.choice(self.locations)
        self.available_locations.append((location, random.randint(10, 100), random.random()))
        self.display_available_locations()

        while True:
            command = input().lower()

            if command == "back":
                self.display_hub()
                return

            if command.isdigit():
                location_num = int(command)
                if 1 <= location_num <= len(self.available_locations):
                    self.explore_location(location_num - 1)
                    return
                print("Invalid input")
                continue

            if command != "s":
                print("Invalid input")
                continue

            if len(self.available_locations) >= num_locations:
                print("Nothing more in sight.")
                print("       [Back]")
                print("\nYour command:")
                continue

            print("Searching...")
            location = random.choice(self.locations)
            self.available_locations.append((location, random.randint(10, 100), random.random()))
            self.display_available_locations()

    def display_available_locations(self):
        for i, (location, titanium, encounter_rate) in enumerate(self.available_locations, 1):
            print(f"[{i}] {location}", end=" ")
            if self.upgrades[0]:
                print("Titanium:", titanium, end=" ")
            if self.upgrades[1]:
                print(f"Encounter rate: {round(encounter_rate * 100)}%", end="")
            print()
        print("\n[S] to continue searching")

    def explore_location(self, index):
        location, titanium, encounter_rate = self.available_locations[index]
        encounter_chance = random.random()
        print("Deploying robots")
        if encounter_chance < encounter_rate:
            print("Enemy encounter!!!")
            self.robots -= 1
            if self.robots == 0:
                print("Mission aborted, the last robot lost...")
                self.handle_game_over()
            else:
                print(f"{location} explored successfully, 1 robot lost...")
        else:
            print(f"{location} explored successfully, with no damage taken.")
        print(f"Acquired {titanium} lumps of titanium")
        self.titanium += titanium

    def display_hub(self):
        print("+==============================================================================+")
        for i in range(5):
            print(self.ROBOT_ASCII[i] * bool(self.robots) + (self.robots - 1) * ( "  |" + self.ROBOT_ASCII[i]))
        print("+==============================================================================+")
        print(f"| Titanium: {self.titanium}" + " " * (67 - len(str(self.titanium))) + "|")
        print("+==============================================================================+")
        print("|                  [Ex]plore                          [Up]grade                |")
        print("|                  [Save]                             [M]enu                   |")
        print("+==============================================================================+")
        print("\nYour command:")

    def handle_game_over(self):
        print("                        |==============================|")
        print("                        |          GAME OVER!          |")
        print("                        |==============================|")

        filename = "high_scores.json"
        try:
            with open(filename, 'r') as f:
                save_data = json.load(f)
            with open(filename, 'w') as f:
                save_data[f"{len(save_data)}"] = [self.player_name, self.titanium]
                json.dump(save_data, f)
        except FileNotFoundError:
            save_data = {"0": [self.player_name, self.titanium]}
            with open(filename, 'w') as f:
                json.dump(save_data, f)
        self.robots = 3
        self.titanium = 0
        self.upgrades = [False, False]
        self.run()

    def handle_high_scores(self):
        filename = "high_scores.json"
        try:
            with open(filename, 'r') as f:
                save_data = json.load(f)

            save_data = dict(sorted(save_data.items(), key=lambda x: x[1][1], reverse=True))
            print("High Scores:\n")
            for i, (name, titanium) in enumerate(save_data.values(), 1):
                print(f"{i}. {name} - {titanium} lumps of titanium")
                if i == 10:
                    break
        except FileNotFoundError:
            print("No scores to display.")

    def handle_hub_commands(self):
        while True:
            command = input().lower()

            if command == "m":
                while True:
                    self.display_game_menu()
                    menu_command = input().lower()

                    if menu_command == "back":
                        self.display_hub()
                        break
                    elif menu_command == "main":
                        return "main"
                    elif menu_command == "exit":
                        print("\nThanks for playing, bye!")
                        return "exit"
                    elif menu_command == "save":
                        if self.handle_save_command():
                            print("\nThanks for playing!")
                            return "exit"
                    else:
                        print("Invalid input")
                        print("\nYour command:")
            elif command == "ex":
                self.handle_exploration()
                self.display_hub()
            elif command == "save":
                if self.handle_save_command():
                    self.display_hub()
            elif command == "up":
                self.display_upgrade_menu()
                while True:
                    menu_command = input().lower()
                    if menu_command == "back":
                        break
                    elif menu_command == "1":
                        if self.titanium < 250:
                            print("Not enough titanium!")
                            print("\nYour command:")
                            continue
                        self.titanium -= 250
                        self.upgrades[0] = True
                        print("Purchase successful. You can now see how much titanium you can get from each found location.")
                    elif menu_command == "2":
                        if self.titanium < 500:
                            print("Not enough titanium!")
                            print("\nYour command:")
                            continue
                        self.titanium -= 500
                        self.upgrades[1] = True
                        print("Purchase successful. You will now see how likely you will encounter an enemy at each found location.")
                    elif menu_command == "3":
                        if self.titanium < 1000:
                            print("Not enough titanium!")
                            print("\nYour command:")
                            continue
                        self.titanium -= 1000
                        self.robots += 1
                        print("Purchase successful. You now have an additional robot")
                    else:
                        print("Invalid input")
                        print("\nYour command:")
                        continue
                    break
                self.display_hub()
            else:
                print("Invalid input")
                print("\nYour command:")

    @staticmethod
    def display_title():
        print(DuskersGame.TITLE_BANNER)

    @staticmethod
    def display_main_menu():
        print("\n[New]  Game")
        print("[Load] Game")
        print("[High] Scores")
        print("[Help]")
        print("[Exit]")
        print("\nYour command:")

    @staticmethod
    def display_game_menu():
        print("                          |==========================|")
        print("                          |            MENU          |")
        print("                          |                          |")
        print("                          | [Back] to game           |")
        print("                          | Return to [Main] Menu    |")
        print("                          | [Save] and exit          |")
        print("                          | [Exit] game              |")
        print("                          |==========================|")
        print("\nYour command:")

    @staticmethod
    def display_upgrade_menu():
        print("                       |================================|")
        print("                       |          UPGRADE STORE         |")
        print("                       |                         Price  |")
        print("                       | [1] Titanium Scan         250  |")
        print("                       | [2] Enemy Encounter Scan  500  |")
        print("                       | [3] New Robot            1000  |")
        print("                       |                                |")
        print("                       | [Back]                         |")
        print("                       |================================|")
        print("\nYour command:")

    @staticmethod
    def display_help_menu():
        print("DUSKERS - HELP")
        print("\nAbout:")
        print("     Duskers is a survival strategy game where you control robots to explore")
        print("     dangerous locations and collect titanium. Watch out for enemy encounters!")
        print("\nGame Controls:")
        print("     - [Ex]plore: Search new locations")
        print("     - [Up]grade: Visit the upgrade store")
        print("     - [S]: Continue searching while exploring")
        print("\nTips:")
        print("     - Buy upgrades to see titanium amounts and enemy encounter rates")
        print("     - More robots mean more chances to survive")
        print("     - High encounter rates are dangerous but might be worth the risk")
        print("\n[Back]")
        print("\nYour command:")

    def handle_play(self):
        print("\nEnter your name:")
        self.player_name = input()
        print(f"\nWelcome, commander {self.player_name}!")

        while True:
            print("Are you ready to begin?")
            print("[Yes] [No] Return to Main[Menu]")
            print("\nYour command:")

            command = input().lower()

            if command == "menu":
                print()
                return "main"
            elif command == "yes":
                self.titanium = 0
                self.robots = 3
                self.upgrades = [False, False]
                self.display_hub()
                return self.handle_hub_commands()
            elif command == "no":
                print("\nHow about now.")
            else:
                print("Invalid input")

    def run(self):
        while True:
            self.display_title()
            self.display_main_menu()
            command = input().lower()

            if command == "exit":
                print("\nThanks for playing, bye!")
                break
            elif command == "help":
                self.display_help_menu()
                while True:
                    back_command = input().lower()
                    if back_command == "back":
                        print()
                        break
                    print("Invalid input")
                    print("\nYour command:")
            elif command == "high":
                self.handle_high_scores()
                print("\t[Back]")
                while True:
                    back_command = input().lower()
                    if back_command == "back":
                        print()
                        break
                    print("Invalid input")
                    print("\nYour command:")
            elif command == "new":
                result = self.handle_play()
                if result in ["exit", "main"]:
                    if result == "main":
                        continue
                    break
            elif command == "load":
                if self.handle_load_command():
                    result = self.handle_hub_commands()
                    if result == "exit":
                        break
                    elif result == "main":
                        continue
            else:
                print("Invalid input")


if __name__ == "__main__":
    game = DuskersGame()
    game.run()
