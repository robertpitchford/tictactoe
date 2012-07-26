PLAYER_X = "X"
PLAYER_O = "O"
EMPTY_BOARD = list("."*9)

class tictactoe(object):
    def __init__(self, reporter):
        self.board = EMPTY_BOARD[:]
        self.reporter = reporter
        self.reporter.message("Welcome to T3!\n")
        self.reporter.message("Your move:\n")
        self.reporter.show_board(self.board[:])

    def move(self, player, location):
        column = int( (ord(location[0]) - ord('A')) )
        row = int(location[1])
        position = column * row
        self.board[position] = player
        self.reporter.show_board(self.board[:])