def tictac_grid(moves):
    grid = []
    counter = 0
    for row in range(5):
        grid.append([])
        for col in range(9):
            if row in [0, 4]:
                grid[row].append('-')
            elif col in [0, 8]:
                grid[row].append('|')
            else:
                grid[row].append(' ')
            
            if row in [1, 2, 3]:
                if col in [2, 4, 6]:
                    grid[row][col] = moves[counter]
                    counter += 1
    
    return grid


def check_status(moves):
    msg = ''
    player_x = moves.count('X')
    player_o = moves.count('O')
    available_move = moves.count(' ')
    possible_win = [moves[0] + moves[1] + moves[2],
                    moves[0] + moves[3] + moves[6],
                    moves[0] + moves[4] + moves[8],
                    moves[1] + moves[4] + moves[7],
                    moves[2] + moves[5] + moves[8],
                    moves[2] + moves[4] + moves[6],
                    moves[3] + moves[4] + moves[5],
                    moves[6] + moves[7] + moves[8]]
                    
    if player_x - player_o > 1 or player_o - player_x > 1:
        msg = "Impossible"
    elif "XXX" in possible_win and "OOO" in possible_win:
        msg = "Impossible"
    elif "XXX" in possible_win and "OOO" not in possible_win:
        msg = "X wins"
    elif "OOO" in possible_win and "XXX" not in possible_win:
        msg = "O wins"
    elif available_move > 0:
        msg = "Game not finished"
    else:
        msg = "Draw"
    return msg

def player_move(grid, moves, player):
    move = []
    while True:
        try:
            move = input().split()
            x = int(move[0])
            y = int(move[1])

            if x not in [1, 2, 3]:
                print("Coordinates should be from 1 to 3!")
            elif y not in [1, 2, 3]:
                print("Coordinates should be from 1 to 3!")
            else:
                if x == 1:
                    y -= 1
                elif x == 2:
                    y += 2
                else:
                    y += 5

                if moves[y] != ' ':
                    print("This cell is occupied! Choose another one!")
                else:
                    moves = list(moves)
                    moves[y] = 'X' if player % 2 == 0 else 'O'
                    moves = "".join(moves)
                    return moves
        except ValueError:
            print("You should enter numbers!")


moves = " " * 9
grid = tictac_grid(moves)
for row in range(5):
    for col in range(9):
        print(grid[row][col], end="")
    print()

player = 0
while check_status(moves) == "Game not finished":
    moves = player_move(grid, moves, player)
    grid = tictac_grid(moves)
    player += 1
    for row in range(5):
        for col in range(9):
            print(grid[row][col], end="")
        print()

print(check_status(moves))
