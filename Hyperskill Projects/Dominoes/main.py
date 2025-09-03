import random
from itertools import count


class DominoGame:
    def __init__(self):
        self.dominoes = [[x, y] for x in range(7) for y in range(x, 7)]
        self.domino_snake = []
        self.tail_head = []
        self.computer_pieces = []
        self.player_pieces = []
        self.stock = []
        self.status = ''

    def deal_pieces(self):
        random.shuffle(self.dominoes)
        self.computer_pieces = self.dominoes[:7]
        self.player_pieces = self.dominoes[7:14]
        self.stock = self.dominoes[14:]

    def find_first_double(self):
        for i in range(6, -1, -1):
            self.domino_snake = [[i, i]]
            for pieces, player in [(self.computer_pieces, 'player'), (self.player_pieces, 'computer')]:
                if self.domino_snake[0] in pieces:
                    self.status = player
                    self.tail_head = self.domino_snake[0].copy()
                    pieces.remove(self.domino_snake[0])
                    return True
        return False

    def setup_game(self):
        while not self.domino_snake:
            self.deal_pieces()
            if self.find_first_double():
                break

    def print_game_state(self):
        print('=' * 70)
        print('Stock pieces:', len(self.stock))
        print('Computer pieces:', len(self.computer_pieces), end='\n\n')

        if len(self.domino_snake) <= 6:
            print(*self.domino_snake, sep='', end='\n\n')
        else:
            print(*self.domino_snake[:3], '...', *self.domino_snake[-3:], sep='', end='\n\n')

        print('Your pieces:')
        for i, piece in enumerate(self.player_pieces, 1):
            print(f'{i}:{piece}')

    def make_move(self, move=0):
        valid_moves = self.get_valid_moves(self.status)
        if self.status == 'player':
            if move == 0:
                if self.stock:
                    self.player_pieces.append(random.choice(self.stock))
                    self.stock.remove(self.player_pieces[-1])
                self.status = {'player': 'computer', 'computer': 'player'}[self.status]
            else:
                piece = self.player_pieces[abs(move) - 1]
                if piece in valid_moves:
                    if move < 0:
                        if self.tail_head[0] in piece:
                            if piece[0] == self.tail_head[0]:
                                piece.reverse()
                            self.player_pieces.remove(piece)
                            self.domino_snake.insert(0, piece)
                            self.status = {'player': 'computer', 'computer': 'player'}[self.status]
                        else:
                            print('Illegal move. Please try again.')
                    else:
                        if self.tail_head[1] in piece:
                            if piece[1] == self.tail_head[1]:
                                piece.reverse()
                            self.player_pieces.remove(piece)
                            self.domino_snake.append(piece)
                            self.status = {'player': 'computer', 'computer': 'player'}[self.status]
                        else:
                            print('Illegal move. Please try again.')
                else:
                    print('Illegal move. Please try again.')
        else:
            if valid_moves:
                numbers_count = {i: sum(x.count(i) for x in self.domino_snake) for i in range(7)}
                print(numbers_count)
                # Calculate score for each valid move (sum of its numbers' frequencies)
                move_scores = [(move, numbers_count[move[0]] + numbers_count[move[1]]) for move in valid_moves]
                print(move_scores)
                # Pick the move with highest score
                move = max(move_scores, key=lambda x: x[1])[0]
                print(move)
                self.computer_pieces.remove(move)

                if self.tail_head[0] in move:
                    if move[0] == self.tail_head[0]:
                        move.reverse()
                    self.domino_snake.insert(0, move)
                else:
                    if move[1] == self.tail_head[1]:
                        move.reverse()
                    self.domino_snake.append(move)

            elif self.stock:
                self.computer_pieces.append(self.stock.pop())
            self.status = {'player': 'computer', 'computer': 'player'}[self.status]
        self.tail_head = self.domino_snake[0][0], self.domino_snake[-1][1]

    def get_valid_moves(self, player):
        hand = {'player': self.player_pieces, 'computer': self.computer_pieces}[player]
        valid_moves = []
        for piece in hand:
            if self.tail_head[0] in piece or self.tail_head[1] in piece:
                valid_moves.append(piece)
        return valid_moves

    def check_game_status(self):
        if not game.player_pieces or not game.computer_pieces:
            print(f'Status: The game is over. {'You' if game.status == 'computer' else 'The computer'} won!')
            return False
        if self.tail_head[0] == self.tail_head[1]:
            count = 0
            num = self.tail_head[0]
            for piece in self.domino_snake:
                if num == piece[0]:
                    count += 1
                if num == piece[1]:
                    count += 1
            if count == 8:
                print("Status: The game is over. It's a draw")
                return False
        return True


game = DominoGame()
game.setup_game()
while True:
    game.print_game_state()
    if not game.check_game_status():
        break
    if game.status == 'player':
        print('\nStatus: It\'s your turn to make a move. Enter your command.')
        while True:
            try:
                move = int(input())
                game.make_move(move)
                if game.status == 'computer':
                    break
            except ValueError:
                print('Invalid input. Please enter a number.')
            except IndexError:
                print('Invalid input. Please enter a number.')
    else:
        print('\nStatus: Computer is about to make a move. Press Enter to continue...')
        input()
        game.make_move()
