import os, inspect, sys
sys.path.append(os.path.dirname(inspect.getfile(inspect.currentframe())) + "/../lib")

import board
import cli_renderer

t3 = board.board(cli_renderer.BoardRendererCli(sys.stdout))

players = [board.PLAYER_O, board.PLAYER_X]
i = 0

while not t3.winner():
    player = players[i % len(players)]
    i += 1
    location = raw_input("move for {who} ? ".format(who=player))
    t3.move(player, location)
    print