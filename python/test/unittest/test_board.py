#noinspection PyUnresolvedReferences
from should_dsl.matchers import be, equal_to
from should_dsl import *
import test_helper
from nose.tools import with_setup
import board
from mockito import *

class TestStartup(object):
    def setup(self):
        self.reporter = mock()
        self.t3 = board.board(self.reporter)

    @with_setup(setup)

    def test_welcome_message(self):
        verify(self.reporter).message(contains("Welcome to T3!"))

    def test_next_move_message(self):
        verify(self.reporter).message(contains("Your move:"))

    def test_empty_board_shown(self):
        verify(self.reporter).show_board("."*9)

class TestAddMoveToBoard(object):
    def setup(self):
        self.reporter = mock()
        self.t3 = board.board(self.reporter)

    def test_get_position(self):
        positions = [("A1", 0),
            ("B1", 1),
            ("C1", 2),
            ("A2", 3),
            ("B2", 4),
            ("C2", 5),
            ("A3", 6),
            ("B3", 7),
            ("C3", 8),
        ]
        for position in positions:
            (location, index) = position
            yield self.assert_position, location, index

    def assert_position(self, location, expected_index):
        self.t3.get_position(location) |should| be(expected_index)

    def test_add_player_to_board(self):
        locations = [
            (0, "X........"),
            (4, "....X...."),
            (8, "........X"),
        ]
        for location in locations:
            (location, expected_board) = location
            yield self.assert_player_move_added, location, expected_board

    def assert_player_move_added(self, location, expected_board):
        self.t3.board = board.EMPTY_BOARD
        self.t3.add_player_at_position(location, "X") |should| equal_to(expected_board)

class TestPlayGame(object):
    def test_player_makes_a_move(self):
        self.reporter = mock()
        self.t3 = board.board(self.reporter)
        self.t3.move(board.PLAYER_X, "A1")

        verify(self.reporter, atleast=1).show_board("X" + "."*8)
