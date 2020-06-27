

from bowling import Game

def testStrike():
    Game.roll(Game, 10)
    assert Game.strike(Game, 0) == 10 

def testSpare():
    Game.roll(Game, 5)
    Game.roll(Game, 5)
    assert Game.spare(Game, 1) == True