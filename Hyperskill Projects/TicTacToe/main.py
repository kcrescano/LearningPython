# write your code here
class TicTacToe:
    combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6)]

    def __init__(self):
        self.board = list(' ' * 9)
        self.player = 'X'
        self.winner = ''
        self.print_board()

    def make_move(self):
        try:
            x, y = [int(x) - 1 for x in input().split()]
            i = x * 3 + y
            if x not in range(3) or y not in range(3):
                print('Coordinates should be from 1 to 3!')
            elif self.board[i] == ' ':
                self.board[i] = self.player
            else:
                print('This cell is occupied! Choose another one!')
        except ValueError:
            print('You should enter numbers!')
        else:
            self.print_board()
            self.check_winner()

    def check_winner(self):
        if any(self.board[i] == self.board[j] == self.board[k] != ' ' for i, j, k in self.combinations):
            self.winner = f'{self.player} wins'
        elif ' ' not in self.board:
            self.winner = 'Draw'
        else:
            self.player = 'O' if self.player == 'X' else 'X'

    def print_board(self):
        print('-' * 9)
        for i in range(3):
            print('|', *self.board[i * 3:i * 3 + 3], '|')
        print('-' * 9)

game = TicTacToe()
while game.winner == '':
    game.make_move()
print(game.winner)
