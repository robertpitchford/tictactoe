import os

class BoardRendererCli(object):
    def __init__(self, output):
        self.output = output

    def message(self, msg):
        self.output.write(msg + os.linesep)

    def show_board(self, board):
        self.render_column_headings()
        self.render_row("1", board[0:3])
        self.render_row_separator()
        self.render_row("2", board[3:6])
        self.render_row_separator()
        self.render_row("3", board[6:9])

    def render_column_headings(self):
        self.output.write("  A B C" + os.linesep)

    def render_row(self, row_id, cells):
        reps = self.get_representations(cells)
        self.output.write(row_id + " " + reps[0] + "|" + reps[1] + "|" + reps[2] + os.linesep)

    def get_representations(self, cells):
        return cells.replace(".", " ")

    def render_row_separator(self):
        self.output.write("  -+-+-\n")
