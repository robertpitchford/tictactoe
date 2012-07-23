import os, inspect, sys
sys.path.append(os.path.dirname(inspect.getfile(inspect.currentframe())) + "/../lib")

import tictactoe

tictactoe.tictactoe(sys.stdout)