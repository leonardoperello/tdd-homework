

from bowling import Game

    
def testStrike():
    Game.roll(Game, 10)
    assert Game.strike(Game, 0) == True 