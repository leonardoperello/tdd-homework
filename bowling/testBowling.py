from bowling import Game

def testStrike():
      Game.roll(Game, 10)
      assert Game.strike(Game, 0)

def testSpare():
    Game.roll(Game, 5)
    Game.roll(Game, 10)
    assert Game.spare(Game, 1) == True

def testPuntajePerfecto():
    assert (Game.puntajePerfecto(Game)== True)

   Game.roll(Game, 5)
   Game.roll(Game, 5)
   assert Game.spare(Game, 1) == True

def test_gutter_game():
    Game.muchos_rolls(Game, 0, 20)
    assert Game.pinsEnPosicion(Game, 19) == 1 

