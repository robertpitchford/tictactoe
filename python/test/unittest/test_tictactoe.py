#noinspection PyUnresolvedReferences
import sys
import cli_renderer
import test_helper
from nose.tools import with_setup
import tictactoe
from mockito import *

class TestStartup(object):

    def setup(self):
        self.reporter = mock()
        self.t3 = tictactoe.tictactoe(self.reporter)

    @with_setup(setup)

    def test_welcome_message(self):
        verify(self.reporter).message(contains("Welcome to T3!"))

    def test_next_move_message(self):
        verify(self.reporter).message(contains("Your move:"))

    def test_empty_board_shown(self):
        verify(self.reporter).show_board(list("."*9))

class TestPlayGame(object):
    def test_player_makes_a_move(self):
        self.reporter = mock()
        self.t3 = tictactoe.tictactoe(self.reporter)
        player = tictactoe.PLAYER_X
        location = "A1"
        self.t3.move(player, location)

        verify(self.reporter).show_board(list("X" + "."*8))
