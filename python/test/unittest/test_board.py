#noinspection PyUnresolvedReferences
from should_dsl.matchers import be, equal_to
from should_dsl import *
import test_helper
from nose.tools import with_setup, raises
import board
from mockito import *

class TestStartup(object):
    def setup(self):
        self.reporter = mock()
        self.t3 = board.board(self.reporter)

    @with_setup(setup)

    def test_welcome_message(self):
        verify(self.reporter).message(contains("Welcome to T3!"))

    def test_empty_board_shown(self):
        verify(self.reporter).show_board("."*9)

class TestAddMoveToBoard(object):
    def setup(self):
        self.reporter = mock()
        self.t3 = board.board(self.reporter)

    def test_get_position(self):
        positions = \
           [("A1", 0),
            ("B1", 1),
            ("1c", 2),
            ("2A", 3),
            ("b2", 4),
            ("C2", 5),
            ("a3", 6),
            ("B3", 7),
            ("3C", 8),
        ]
        for position in positions:
            (location, index) = position
            yield self.assert_position, location, index

    def test_get_position_throws_exception(self):
        positions = [
            ("A4"),
            ("A0"),
            ("Z1"),
            ("Z9"),
            ("$1"),
            ("A%"),
            ("AA"),
            ("11"),
        ]
        for position in positions:
            location = position
            yield self.assert_position_failure, location

    def assert_position(self, location, expected_index):
        self.t3.get_position(location) |should| be(expected_index)

    @raises(board.MoveSyntaxError)
    def assert_position_failure(self, location):
        self.assert_position(location, 0)

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

class TestDetectWinner(object):
    def test_empty_board_should_not_be_winner(self):
        t3 = board.board(mock())
        t3 |should_not| be_winner

    def test_should_identify_winner(self):
        scenarios = [
            ("XX."
             "..."
             "...", "C1"), # first row
            ("..."
             "X.X"
             "...", "B2"), # second row
            ("..."
             "..."
             ".XX", "A3"), # third row
            ("X.."
             ".X."
             "...", "C3"), # TL-BR
            ("..X"
             "..."
             "X..", "B2"), # BL-TR
            ("X.."
             "X.."
             "...", "A3"), # first column
            (".X."
             "..."
             ".X.", "B2"), # second column
            ("..."
             "..X"
             "..X", "C1"), # third column
        ]
        for scenario in scenarios:
            yield self.assert_winner, scenario

    def assert_winner(self, scenario):
        (starting_board, move) = scenario
        t3 = board.board(mock())
        t3.board = starting_board
        t3 | should_not | be_winner
        # when
        t3.move(board.PLAYER_X, move)
        # then
        t3 | should | be_winner

    def test_should_not_identify_winner_when_there_is_no_winner(self):
        scenarios = [
            ("XO."
             "..."
             "...", "C1"),
            ("OXO"
             "XOX"
             ".OX", "A3"),
        ]
        for scenario in scenarios:
            yield self.assert_not_winner, scenario

    def assert_not_winner(self, scenario):
        (starting_board, move) = scenario
        t3 = board.board(mock())
        t3.board = starting_board
        t3.move(board.PLAYER_X, move)
        t3 | should_not | be_winner
