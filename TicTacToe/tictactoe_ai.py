import random as r


class TicTacToe:

    def __init__(self, player1, player2):
        self.players = {'X': player1, 'O': player2}
        self.turn = 'X'
        self.grid = [['_'] * 3 for _ in range(3)]
        self.game = True

    def play(self):
        while True:
            if self.players[self.turn] in ["easy", "medium", "hard"]:
                print(f'Making move level "{self.players[self.turn]}"')
                self.update_grid(*self.computer_move(), turn=self.turn)
            else:
                self.update_grid(*self.user_move(), turn=self.turn)

            self.turn = 'X' if self.turn == 'O' else 'O'
            game = self.game_grid()
            if game != "Game not finished":
                print(game)
                break

    def update_grid(self, x: int, y: int, turn):
        self.grid[x][y] = turn

    def game_grid(self):
        print("---------")
        for x in range(3):
            print(f"| {self.grid[x][0]} {self.grid[x][1]} {self.grid[x][2]} |")
        print("---------")

        return self.check_status()

    def computer_move(self):
        while True:
            x = r.randint(0, 2)
            y = r.randint(0, 2)
            if self.players[self.turn] in ["medium", "hard"]:
                possible_win = self.win_condition()

                if self.players[self.turn] == "hard":
                    if possible_win[1][1] == '_':
                        x, y = 1, 1
                    elif possible_win[0][0] == '_':
                        x, y = 0, 0
                    elif possible_win[0][2] == '_':
                        x, y = 0, 2
                    elif possible_win[2][0] == '_':
                        x, y = 2, 0
                    elif possible_win[2][2] == '_':
                        x, y = 2, 2

                for chance in possible_win:
                    if (chance.count('X') == 2 or chance.count('O') == 2) and '_' in chance:
                        index = possible_win.index(chance)
                        if index in range(0, 2):
                            x = index
                            y = chance.index('_')
                        elif index in range(3, 5):
                            x = chance.index('_')
                            y = index - 3
                        elif index == 6:
                            x = chance.index('_')
                            y = chance.index('_')
                        elif index == 7:
                            y = chance.index('_')
                            x = abs(y - 2)

            if self.check_grid(x, y):
                return x, y

    def user_move(self):
        while True:
            try:
                move = input("Enter the coordinates: ").split()
                x = int(move[0]) - 1
                y = int(move[1]) - 1

                if x in range(0, 3) and y in range(0, 3):
                    if self.check_grid(x, y):
                        return x, y
                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    print("Coordinates should be from 1 to 3!")
            except ValueError:
                print("You should enter numbers!")

    def check_grid(self, x, y):
        if self.grid[x][y] == '_':
            return True
        return False

    def check_status(self):
        possible_win = self.win_condition()

        if "XXX" in possible_win:
            return "X wins"
        elif "OOO" in possible_win:
            return "O wins"
        elif list(slot for row in self.grid for slot in row).count('_') > 0:
            return "Game not finished"
        else:
            return "Draw"

    def win_condition(self):
        return [self.grid[0][0] + self.grid[0][1] + self.grid[0][2],
                self.grid[1][0] + self.grid[1][1] + self.grid[1][2],
                self.grid[2][0] + self.grid[2][1] + self.grid[2][2],

                self.grid[0][0] + self.grid[1][0] + self.grid[2][0],
                self.grid[0][1] + self.grid[1][1] + self.grid[2][1],
                self.grid[0][2] + self.grid[1][2] + self.grid[2][2],

                self.grid[0][0] + self.grid[1][1] + self.grid[2][2],
                self.grid[2][0] + self.grid[1][1] + self.grid[0][2],]


while True:
    setting = input("Input command: ")

    if setting == "exit":
        break
    else:
        setting = setting.split()
        try:
            match = TicTacToe(setting[1], setting[2])
            match.game_grid()

            match.play()
        except IndexError:
            print("Bad parameters!")
