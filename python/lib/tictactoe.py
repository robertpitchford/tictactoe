TOTAL_COLUMNS = 3
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY_BOARD = "."*9

class tictactoe(object):
    def __init__(self, reporter):
        self.board = EMPTY_BOARD
        self.reporter = reporter
        self.reporter.message("Welcome to T3!\n")
        self.reporter.message("Your move:\n")
        self.reporter.show_board(self.board)

    def move(self, player, location):
        position = self.get_position(location)
        self.board = self.add_player_at_position(position, player)
        self.reporter.show_board(self.board)

    def get_position(self, location):
        zero_based_column = ord(location[0]) - ord('A')
        zero_based_row = int(location[1])-1
        return TOTAL_COLUMNS * zero_based_row + zero_based_column

    def add_player_at_position(self, position, player):
        return self.board[:position] + player + self.board[position + 1:]
