from bowling import Game

def testSpare():
   rolls = []
   Game.roll(Game, 5, rolls)
   Game.roll(Game, 5, rolls)
   assert Game.spare(Game, 0, rolls)

def testSpare2():
   rolls = []
   Game.roll(Game, 2, rolls)
   Game.roll(Game, 8, rolls)
   assert Game.spare(Game, 0, rolls)

def testStrike():
    rolls = []
    Game.roll(Game, 10, rolls)
    assert Game.strike(Game, 0, rolls)

def test_gutter_game():
    rolls = []
    Game.muchos_rolls(Game, 0, 20, rolls)
    assert Game.scoreFinal(Game, rolls) == 0 

def testPosicion():
    rolls = []
    Game.roll(Game, 10, rolls)
    assert Game.pinsEnPosicion(Game, 0, rolls)

def testScore():
    rolls = []
    Game.muchos_rolls(Game, 6, 20, rolls)
    assert (Game.scoreFinal(Game, rolls)==120)

def testUnos():
        rolls = []
        Game.muchos_rolls(Game, 1, 20, rolls)
        assert Game.scoreFinal(Game, rolls) == 20

def test_muchos_strikes():
    rolls = []
    Game.roll(Game, 10, rolls)
    Game.roll(Game, 7, rolls)
    Game.roll(Game, 3, rolls)
    Game.muchos_rolls(Game, 1, 17, rolls)
    assert Game.scoreFinal(Game, rolls) == 47


def testPuntajePerfecto():
    rolls = []
    Game.muchos_rolls(Game, 10, 12, rolls)
    assert (Game.scoreFinal(Game, rolls)==300)

def testRandom():
    rolls = []
    for pins in [1, 5, 7, 2, 9, 0, 8, 1,
                     10, 3, 2, 5, 3, 4, 1, 1, 1, 1, 1]:
            Game.roll(Game, pins, rolls)
    assert Game.scoreFinal(Game, rolls) == 70
    
def testRandom2():
    rolls = []
    for pins in [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 
                5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5 ]:
            Game.roll(Game, pins, rolls)
    assert Game.scoreFinal(Game, rolls) == 150
    assert Game.juegoTerminado

