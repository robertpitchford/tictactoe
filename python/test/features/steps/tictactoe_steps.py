#noinspection PyUnresolvedReferences
from should_dsl.dsl import should
import test_helper
from behave import step
from mockito import *
import board

@step(u't3 is not running')
def game_is_not_running(context):
    pass

@step(u'I start a new game')
def I_start_a_new_game(context):
    context.game = board.board(mock())

@step(u'I should see "{msg}"')
def I_should_see(context, msg):
    verify(context.game.reporter).message(contains("Welcome to T3!"))

@step(u'I am asked for my move')
def I_am_asked_for_my_move(context):
    verify(context.game.reporter).message(contains("Your move:"))

@step(u'I should see an empty board')
def I_should_see_an_empty_board(context):
    verify(context.game.reporter).show_board(".........")

@step(u't3 is running')
def t3_is_running(context):
    context.execute_steps(u'When I start a new game')

@step(u'I make a move')
def I_make_a_move(context):
    context.game.reporter = reset_mock()
    context.game.move("X", "A1")

@step(u'I should see that move')
def I_should_see_that_move(context):
    verify(context.game.reporter).show_board("X........")

@step(u'I make a winning move')
def I_make_a_winning_move(context):
    context.game.reporter = reset_mock()
    context.game.board = "..X.X...."
    context.game.move("X", "A3")

@step('I should win the game')
def I_should_sin_the_game(context):
    context.game |should| be_winner

def reset_mock():
    return mock()




