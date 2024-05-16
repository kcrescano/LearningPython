# Write your code here
import random

domino_set = [[x, y] for x in range(7) for y in range(x, 7)]
computer, player = [], []
for _ in range(0, 7):
    computer.append(domino_set.pop(random.randint(0, len(domino_set)-1)))
    player.append(domino_set.pop(random.randint(0, len(domino_set)-1)))
snake = [max([*player, *computer])]
status = ''
pass_ = 0
number_count = dict.fromkeys(range(1, 7), 0)


for item in player:
    if item == snake[0]:
        player.pop(player.index(item))
        status = 'computer'
for item in computer:
    if item == snake[0]:
        computer.pop(computer.index(item))
        status = 'player'

while True:
    
    print('=' * 70)        
    print('Stock size:', len(domino_set))
    print('Computer pieces:', len(computer))
    
    if len(snake) <= 6:
        print('\n',*snake, sep='')
    else:
        print('\n',snake[0],snake[1],snake[2],'...',snake[-3],snake[-2],snake[-1], sep='')
        
    print('\nYour pieces:')
    for piece in player:
        print(f'{player.index(piece)+1}:{piece}')

    if not player:
        print('Status: The game is over. You won!')
        break
    if not computer:
        print('Status: The game is over. The computer won!')
        break
        
    if not domino_set:
        if pass_ >= 1:
            print("Status: The game is over. It's a draw!")
            break
    snake_count = [y for x in snake for y in x]
    if snake[0][0] == snake[-1][1]:
        if snake.count(snake[0][0]) >= 8:
            print("Status: The game is over. It's a draw!")
            break
    
    if status == 'player':
        print("\nStatus: It's your turn to make a move. Enter your command.")
        while True:
            try:
                turn = int(input())
                if abs(turn) <= len(player) and abs(turn) >= 0:
                    snake_tail_head = [snake[0][0], snake[-1][1]]
                    if turn == 0:
                        if domino_set:
                            player.append(domino_set.pop(random.randint(0, len(domino_set) - 1)))
                        pass_ += 1
                    elif turn > 0:
                        if snake_tail_head[1] in player[abs(turn) - 1]:
                            player_piece = player.pop((abs(turn))-1)
                            if snake_tail_head[1] == player_piece[1]:
                                player_piece.reverse()
                            snake.append(player_piece)
                            pass_ = 0
                        else:
                            print('Illegal move. Please try again.')
                            continue
                    else:
                        if snake_tail_head[0] in player[abs(turn) - 1]:
                            player_piece = player.pop((abs(turn))-1)
                            if snake_tail_head[0] == player_piece[0]:
                                player_piece.reverse()
                            snake.insert(0, player_piece)
                            pass_ = 0
                        else:
                            print('Illegal move. Please try again.')
                            continue

                    status = 'computer'
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Invalid input. Please try again.')
    else:
        print("\nStatus: Computer is about to make a move. Press Enter to continue...")
        enter = input()
        snake_tail_head = [snake[0][0], snake[-1][1]]
        computer_piece = []
        computer_set = {y for x in computer for y in x}
        
        computer_point = [y for x in computer for y in x]
        move_point = {i: computer_point.count(i) for i in range(7)}
        
        computer2 = computer.copy()
        computer_point = [y for x in computer for y in x]
        snake_point = [y for x in snake for y in x]
        computer_point.extend(computer_point)
        
        if set(snake_tail_head).intersection(computer_set):
            while computer2:
                summ = 0
                for i in range(len(computer2)):
                    if summ <= move_point[computer2[i][0]] + move_point[computer2[i][1]]:
                        summ = move_point[computer2[i][0]] + move_point[computer2[i][1]]
                        computer_piece = computer2[i]
        
                if snake_tail_head[0] in computer_piece:
                    if snake_tail_head[0] == computer_piece[0]:
                        computer_piece.reverse()
                    snake.insert(0, computer.pop(computer.index(computer_piece)))
                    status = 'player'
                    pass_ = 0
                    break
                elif snake_tail_head[1] in computer_piece:
                    if snake_tail_head[1] == computer_piece[1]:
                        computer_piece.reverse()
                    snake.append(computer.pop(computer.index(computer_piece)))
                    status = 'player'
                    pass_ = 0
                    break
                else:
                    computer2.pop(computer2.index(computer_piece))
                
        else:
            if domino_set:
                computer.append(domino_set.pop(random.randint(0, len(domino_set) - 1)))
            status = 'player'
            pass_ += 1
        
