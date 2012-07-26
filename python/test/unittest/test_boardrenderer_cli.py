from nose.tools import with_setup
import cli_renderer
import os
from mockito import *

class StdoutMock(object):
    def __init__(self):
        self.out = ""

    def write(self, line):
        self.out += line

class TestMessage(object):
    def test_message(self):
        MSG = "some arbitrary message"
        output = mock()
        r = cli_renderer.BoardRendererCli(output)
        r.message(MSG)

        verify(output).write(MSG + os.linesep)

class TestBoardRendering(object):
    def setup(self):
        self.output = StdoutMock()
        self.r = cli_renderer.BoardRendererCli(self.output)

    @with_setup(setup)

    def test_show_empty_board(self):
        self.r.show_board("."*9)

        expected = "  A B C\n1  | | \n  -+-+-\n2  | | \n  -+-+-\n3  | | \n"
        assert self.output.out == expected, "%s != %s" % (self.output.out, expected)

    def test_show_populated_board(self):
        self.r.show_board("XXOOXOXOX")

        expected = "  A B C\n1 X|X|O\n  -+-+-\n2 O|X|O\n  -+-+-\n3 X|O|X\n"
        assert self.output.out == expected, "%s != %s" % (self.output.out, expected)
