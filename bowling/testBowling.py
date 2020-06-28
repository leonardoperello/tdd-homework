

from bowling import Game

def muchos_rolls(pins, num):
    for i in range(num):
        Game.roll(Game, pins)

#def testStrike():
 #   Game.roll(Game, 10)
  #  assert Game.strike(Game, 0) == 10 

#def testSpare():
 #   Game.roll(Game, 5)
 #   Game.roll(Game, 5)
 #   assert Game.spare(Game, 1) == True

def test_gutter_game():
    muchos_rolls(0, 20)
    assert Game.strike(Game, 20) == 0