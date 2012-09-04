import os, inspect, sys
sys.path.append(os.path.dirname(inspect.getfile(inspect.currentframe())) + "/../lib")

import board
import cli_renderer

board.board(cli_renderer.BoardRendererCli(sys.stdout))