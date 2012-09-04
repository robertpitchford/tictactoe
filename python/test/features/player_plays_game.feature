Feature: Playing t3

  As a player
  I want to play a game
  So that I can try and beat the computer

  Scenario: make a move
    Given t3 is running
    When  I make a move
    Then  I should see that move

  Scenario: win a game
    Given t3 is running
    When  I make a winning move
    Then  I should win the game