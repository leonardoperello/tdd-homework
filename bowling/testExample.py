from bowling import Game

def testStrike():
    rolls = []
    Game.roll(Game, 10, rolls)
    assert Game.strike(Game, 0, rolls)