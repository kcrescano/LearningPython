# Write your code here
import datetime
import json
import os
import sys
import random

system_commands = {'new': {'cmd': '[New] Game', 'action': lambda: new_game()},
                   'load': {'cmd': '[Load] Game', 'action': lambda: save_menu("main", "loaded")},
                   'high': {'cmd': '[High] Scores', 'action': lambda: high_scores()},
                   'help': {'cmd': '[Help]', 'action': lambda: help_section()},
                   'exit': {'cmd': '[Exit]', 'action': lambda: end()}}
game_commands = {'ex': {'action': lambda: exploration()},
                 'up': {'action': lambda: upgrade()},
                 'save': {'action': lambda: save_menu("game")},
                 'm': {'action': lambda: settings()}}
menu_settings = {'back': {'action': lambda: game()},
                 'main': {'action': lambda: system_start()},
                 'save': {'action': lambda: save_menu("menu")},
                 'exit': {'action': lambda: end()}}
explored_locations = []
user_data = {'Name': '', 'Titanium': 0, 'Robots': 3, 'Last save': '',
             'Upgrades': [False, False]}
max_location = 9


def system_ui():
    print("+=======================================================================+",
          "  ######*   ##*   ##*  #######*  ##*  ##*  #######*  ######*   #######*",
          "  ##*  ##*  ##*   ##*  ##*       ##* ##*   ##*       ##*  ##*  ##*",
          "  ##*  ##*  ##*   ##*  #######*  #####*    #####*    ######*   #######*",
          "  ##*  ##*  ##*   ##*       ##*  ##* ##*   ##*       ##*  ##*       ##*",
          "  ######*    ######*   #######*  ##*  ##*  #######*  ##*  ##*  #######*",
          "                      (Survival ASCII Strategy Game)",
          "+=======================================================================+", sep="\n")
    for command in system_commands.values():
        print(command['cmd'])


def game_ui():
    extra_space = " " * (37 - len(str(user_data['Titanium'])))
    robot = ["  $   $$$$$$$   $",
             "  $$$$$     $$$$$",
             "      $$$$$$$    ",
             "     $$$   $$$   ",
             "     $       $   "]
    print("+==============================================================================+"),
    for line in robot:
        print("  |".join([line] * user_data['Robots']))
    print("+==============================================================================+",
          f"| Titanium: {user_data['Titanium']}{extra_space}                              |",
          "+==============================================================================+",
          "|                  [Ex]plore                          [Up]grade                |",
          "|                  [Save]                             [M]enu                   |",
          "+==============================================================================+", sep="\n")


def upgrade_menu():
    print("                       |================================|",
          "                       |          UPGRADE STORE         |",
          "                       |                         Price  |",
          "                       | [1] Titanium Scan         250  |",
          "                       | [2] Enemy Encounter Scan  500  |",
          "                       | [3] New Robot            1000  |",
          "                       |                                |",
          "                       | [Back]                         |",
          "                       |================================|", sep='\n')


def game_menu():
    print("                          |==========================|",
          "                          |            MENU          |",
          "                          |                          |",
          "                          | [Back] to game           |",
          "                          | Return to [Main] Menu    |",
          "                          | [Save] and exit          |",
          "                          | [Exit] game              |",
          "                          |==========================|", sep='\n')


def system_start():
    system_ui()
    while True:
        try:
            cmd = user_input()
            system_commands[cmd]['action']()
        except (KeyError, ValueError):
            print('Invalid input')


def new_game():
    msg = "\nAre you ready to begin?\n[Yes] [No] Return to Main[Menu]"
    user_data['Name'] = input("\nEnter your name: ")
    user_data['Titanium'] = 0

    print(f"\nGreetings, commander {user_data['Name']}!", msg, sep="")
    while (play := user_input()) != 'yes':
        if play == 'no':
            print("\nHow about now.", msg, sep="")
        elif play == 'menu':
            system_start()
            break
        else:
            print('Invalid input')
    game()


def save_menu(screen, action="saved"):
    global user_data
    saved_data = []

    for i in range(1, 4):
        if os.path.isfile(f"save_file{i}.json"):
            with open(f"save_file{i}.json", 'r') as file:
                data = json.load(file)
                saved_data.append(data)
        else:
            saved_data.append(None)

    print("   Select save slot:")
    for i in range(3):
        num = i + 1
        if saved_data[i]:
            print(f"    [{num}] {saved_data[i]['Name']} "
                  f"Titanium: {saved_data[i]['Titanium']} "
                  f"Robots: {saved_data[i]['Robots']} "
                  f"Last save: {saved_data[i]['Last save']}")
        else:
            print(f"    [{num}] empty")

    while (cmd := user_input()) != 'back':
        try:
            if action == 'saved':
                with open(f"save_file{int(cmd)}.json", 'w') as file:
                    save_time = datetime.datetime.now()
                    user_data['Last save'] = save_time.strftime("%Y-%m-%d %H:%M")
                    json.dump(user_data, file)
                    break
            if action == 'loaded':
                try:
                    if saved_data[(slot := int(cmd) - 1)]:
                        user_data = saved_data[slot]
                        break
                    else:
                        print("Empty slot!")
                except (ValueError, IndexError):
                    print("Invalid input")
        except KeyError:
            print("Invalid input")
    if cmd == "back":
        system_start()

    game_state_msg(action)
    if screen in ["main", "game"]:
        game()
    system_start()


def game_state_msg(state):
    extra_space = " " if state == "saved" else ""
    print("                        |==============================|")
    print(f"                        |    GAME {state.upper()} SUCCESSFULLY  {extra_space}|")
    print("                        |==============================|")
    if state == "loaded":
        print(f" Welcome back, commander {user_data['Name']}!")


def game():
    game_ui()
    while True:
        try:
            cmd = user_input()
            game_commands[cmd]['action']()
        except (KeyError, ValueError):
            print('Invalid input')


def upgrade():
    global user_data
    upgrade_menu()
    while (cmd := user_input()) != 'back':
        try:
            item = int(cmd)
            ore = user_data['Titanium']
            if item == 1:
                if ore >= 250:
                    print("Purchase successful. "
                          "You can now see how much titanium you can get from each found location.")
                    user_data['Upgrades'][0] = True
                    user_data['Titanium'] -= 250
                    break
                else:
                    print("Not enough titanium!")
            elif item == 2:
                if ore >= 500:
                    print("Purchase successful. "
                          "You will now see how likely you will encounter an enemy at each found location.")
                    user_data['Upgrades'][1] = True
                    user_data['Titanium'] -= 500
                    break
                else:
                    print("Not enough titanium!")
            elif item == 3:
                if ore >= 1000:
                    print("Purchase successful. You now have an additional robot")
                    user_data['Robots'] += 1
                    user_data['Titanium'] -= 1000
                    break
                else:
                    print("Not enough titanium!")
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input")
    game()


def settings():
    game_menu()
    while True:
        try:
            cmd = user_input()
            menu_settings[cmd]['action']()
        except (KeyError, ValueError):
            print('Invalid input')


def exploration():
    global max_location, user_data, explored_locations
    max_location = random.randint(1, 9)
    search_location()

    while (cmd := user_input()) != 'back':
        if cmd == 's':
            search_location()
        elif cmd.isdigit():
            try:
                global explored_locations
                place, ore, rate = explored_locations[int(cmd) - 1]

                print("Deploying robots")
                encounter = random.random()
                if encounter < rate:
                    print("Enemy encounter",
                          f"{place} explored successfully, 1 robot lost..", sep='\n')
                    user_data['Robots'] -= 1
                    if user_data['Robots'] == 0:
                        print("                        |==============================|")
                        print(f"                        |          GAME OVER           |")
                        print("                        |==============================|")
                        explored_locations = []
                        high_scores(True)
                else:
                    print(f"{place} explored successfully, with no damage taken.")

                user_data['Titanium'] += ore
                print(f"Acquired {ore} lumps of titanium")
                break
            except (KeyError, IndexError):
                print("Invalid input")
        else:
            print("Invalid input")
    explored_locations = []
    game()


def search_location():
    print("Searching")
    if locations and len(explored_locations) < max_location:
        random_place = random.choice(locations)
        random_ore = random.randint(10, 100)
        encounter = random.random()
        explored_locations.append([random_place, random_ore, encounter])

    for i in range(len(explored_locations)):
        print(f"[{i + 1}] {explored_locations[i][0]}", end=" ")
        if user_data['Upgrades'][0]:
            print(f"Titanium: {explored_locations[i][1]}", end=" ")
        if user_data['Upgrades'][1]:
            print(f"Encounter rate: {round(explored_locations[i][2] * 100)}%", end=" ")
        print()

    if locations and len(explored_locations) < max_location:
        print('\n[S] to continue searching')
    else:
        print("Nothing more in sight.\n       [Back]")


def high_scores(game_over=False):
    if os.path.isfile(f"high_scores.json"):
        with open(f"high_scores.json", 'r+') as file:
            scores = json.load(file)
            if game_over:
                scores.append({'Name': user_data['Name'], 'Score': user_data['Titanium']})
                file.seek(0)
                json.dump(scores, file)
    else:
        if game_over:
            with open(f"high_scores.json", 'w') as file:
                json.dump([{'Name': user_data['Name'], 'Score': user_data['Titanium']}], file)
        print("No scores to display.")

    if game_over:
        system_start()
    else:
        print("HIGH SCORES")
        top_score = sorted(scores, key=lambda x: -x['Score'])
        for i in range(len(top_score)):
            print(f"({i + 1}) {top_score[i]['Name']} {top_score[i]['Score']}")

    print("	[Back]")
    while (play := user_input()) != 'back':
        print('Invalid input')
    system_start()


def help_section():
    print("Coming SOON! Thanks for playing!")
    exit()


def user_input(msg="Your command"):
    command = input(f"\n{msg}: ").lower()
    return command


def end():
    print("\nThanks for playing, bye!")
    exit()


if len(sys.argv) == 5:
    random.seed(sys.argv[1])
    min_animation = int(sys.argv[2])
    max_animation = int(sys.argv[3])
    locations = [" ".join(place.split('_')) for place in sys.argv[4].split(',')]
else:
    min_animation = 0.1
    max_animation = 1
    locations = ["Amazon Lily", "Kuraigana Island", "Weatheria",
                 "Boin Archipelago", "Kamabakka Kingdom", "Torino Kingdom",
                 "Baltigo", "Karakuri Island", "Namakura Island"]

system_start()
