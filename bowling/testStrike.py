

from bowling import Game

    
def testStrike():
    Game.roll(None,10)
    assert Game.strike(None, 0) == True 