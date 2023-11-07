import string
import random

pencils = input("How many pencils would you like to use:")
while not pencils.isnumeric() or int(pencils) == 0:
    if not pencils.isnumeric():
        pencils = input("The number of pencils should be numeric")
    else:
        pencils = input("The number of pencils should be positive")

pencils = int(pencils)

player = input("Who will be the first (John, Jack):")
while player not in ['John', 'Jack']:
    player = input("Choose between 'John' and 'Jack'")

current_player = player
while pencils > 0:
    print("|" * pencils)
    player_pick = 0
    if current_player == 'Jack':
        if pencils == 1:
            player_pick = 1
        elif pencils % 4 == 0:
            player_pick = 3
        elif pencils % 4 == 3:
            player_pick = 2
        elif pencils % 4 == 2:
            player_pick = 1
        else:
            player_pick = random.choice([1, 2, 3])
            
        print("Jack's turn:", player_pick, sep='\n')
    else: 
        player_pick = input("John's turn:")
        while player_pick not in ['1', '2', '3']:
            player_pick = input("Possible values: '1', '2' or '3'")
        while pencils - int(player_pick) < 0:
            player_pick = input("Too many pencils were taken")

        player_pick = int(player_pick)
            
    pencils -= player_pick
    current_player = "John" if current_player == "Jack" else "Jack"
    
    if pencils == 0:
        print(f'{current_player} won!')
