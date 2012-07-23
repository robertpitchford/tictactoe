#noinspection PyUnresolvedReferences
import test_helper
import tictactoe
from mockito import *

class TestTictactoe(object):

    def test_welcome_message(self):
        reporter = mock()
        t3 = tictactoe.tictactoe(reporter)

        verify(reporter).write(contains("Welcome to T3!"))