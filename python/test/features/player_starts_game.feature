Feature: Running t3

  As a player
  I want to start a game
  So that I can try and beat the computer

  Scenario: start a game
    Given t3 is not running
    When I start a new game
    Then I should see "Welcome to T3!"
    And  I should see an empty board