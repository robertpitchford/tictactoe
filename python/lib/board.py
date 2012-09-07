import re

class MoveSyntaxError(Exception):
    pass

class MoveSpaceTakenError(Exception):
    pass

TOTAL_COLUMNS = 3
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = "."
EMPTY_BOARD = EMPTY*9

class board(object):
    def __init__(self, reporter):
        self.board = EMPTY_BOARD
        self.reporter = reporter
        self.reporter.message("Welcome to T3!\n")
        self.reporter.show_board(self.board)

    def move(self, player, location):
        position = self.get_position(location)
        self.board = self.add_player_at_position(position, player)
        self.reporter.show_board(self.board)

    def get_position(self, location):
        location = location.upper()
        column = self.get_zero_based_column(location)
        row = self.get_zero_based_row(location)
        return TOTAL_COLUMNS * row + column

    def get_zero_based_column(self, location):
        try:
            id = re.findall('[a-cA-C]', location)[0]
        except IndexError:
            raise MoveSyntaxError("Invalid column in '{location}'".format(location=location))
        return ord(id) - ord('A')

    def get_zero_based_row(self, location):
        try:
            id = re.findall('[1-3]', location)[0]
        except IndexError:
            raise MoveSyntaxError("Invalid row in '{location}'".format(location=location))
        return int(id) - 1

    def add_player_at_position(self, position, player):
        if self.board[position] == EMPTY:
            return self.board[:position] + player + self.board[position + 1:]
        else:
            raise MoveSpaceTakenError("Space already taken")

    def winner(self):
        b = self.board
        winning_combinations = ["012", "345", "678", "048", "642", "036", "147", "258"]
        for c in winning_combinations:
            c0, c1, c2 = int(c[0]), int(c[1]), int(c[2])
            if b[c0] != EMPTY and b[c0] == b[c1] and b[c1] == b[c2]:
                return True
        return False

    def draw(self):
        return "." not in self.board and not self.winner()