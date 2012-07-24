import cli_renderer
import os
from mockito import *

class StdoutMock(object):
    def __init__(self):
        self.out = ""

    def write(self, line):
        self.out += line

class TestBoardRendererCli(object):
    def test_message(self):
        MSG = "some arbitrary message"
        output = mock()
        r = cli_renderer.BoardRendererCli(output)
        r.message(MSG)

        verify(output).write(MSG + os.linesep)

    def test_show_empty_board(self):
        output = StdoutMock()
        r = cli_renderer.BoardRendererCli(output)
        r.show_board("."*9)

        expected = "  A B C\n1  | | \n  -+-+-\n2  | | \n  -+-+-\n3  | | \n"
        assert output.out == expected, "%s != %s" % (output.out, expected)

    def test_show_populated_board(self):
        output = StdoutMock()
        r = cli_renderer.BoardRendererCli(output)
        r.show_board("XXOOXOXOX")

        expected = "  A B C\n1 X|X|O\n  -+-+-\n2 O|X|O\n  -+-+-\n3 X|O|X\n"
        assert output.out == expected, "%s != %s" % (output.out, expected)
