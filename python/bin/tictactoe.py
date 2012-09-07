import os, inspect, sys
sys.path.append(os.path.dirname(inspect.getfile(inspect.currentframe())) + "/../lib")

import board
import cli_renderer

t3 = board.board(cli_renderer.BoardRendererCli(sys.stdout))

players = [board.PLAYER_O, board.PLAYER_X]
i = 0

while not t3.winner() and not t3.draw():
    player = players[i % len(players)]
    location = raw_input("move for {who} ? ".format(who=player))
    try:
        t3.move(player, location)
    except Exception as e:
        print e.args[0]
        continue
    i += 1
    print

if t3.draw():
    print "Draw!"
else:
    print "{player}'s win!".format(player=player)