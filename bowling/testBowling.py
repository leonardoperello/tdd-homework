from bowling import Game

def testStrike():
    Game.roll(Game, 10)
    assert Game.strike(Game, 0)

def testSpare():
    Game.roll(Game, 5)
    Game.roll(Game, 5)
    assert Game.spare(Game, 1)

def testPuntajePerfecto():
    assert (Game.puntajePerfecto(Game) == False)

def test_gutter_game():
    Game.muchos_rolls(Game, 0, 20)
    Game.scoreFinal
    assert Game.current_score == 0 

