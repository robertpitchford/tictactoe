#noinspection PyUnresolvedReferences
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
        verify(self.reporter).show_board("."*9)