import os, inspect, sys
sys.path.append(os.path.dirname(inspect.getfile(inspect.currentframe())) + "/../lib")

import tictactoe
import cli_renderer

tictactoe.tictactoe(cli_renderer.BoardRendererCli(sys.stdout))