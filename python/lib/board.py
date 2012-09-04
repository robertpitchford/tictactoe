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

    def winner(self):
        b = self.board
        winning_combinations = ["012", "345", "678", "048", "642", "036", "147", "258"]
        for c in winning_combinations:
            c0, c1, c2 = int(c[0]), int(c[1]), int(c[2])
            if b[c0] != EMPTY and b[c0] == b[c1] and b[c1] == b[c2]:
                return True
        return False