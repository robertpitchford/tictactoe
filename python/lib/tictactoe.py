EMPTY_BOARD = "."*9

class tictactoe(object):
    def __init__(self, reporter):
        self.reporter = reporter
        self.reporter.message("Welcome to T3!\n")
        self.reporter.message("Your move:\n")
        self.reporter.show_board(EMPTY_BOARD)