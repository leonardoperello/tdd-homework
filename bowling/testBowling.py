

from bowling import Game

def muchos_rolls(pins, num):
    for i in range(num):
       Game.roll(Game, pins)

def testStrike():
      Game.roll(Game, 10)
      assert Game.strike(Game, 0)

def testSpare():

   Game.roll(Game, 5)
   Game.roll(Game, 5)
   assert Game.spare(Game, 1) == True
'''
def test_gutter_game():
    Game.muchos_rolls(Game, 0, 20)
    assert Game.scoreFinal(Game) == 0

def testPuntajePerfecto():
    assert (Game.puntajePerfecto(Game)== True)
'''
def testRandom():
    #for pins in [1, 4, 4, 5, 6, 4, 5, 5,
          #           7, 0, 1, 7, 3, 6, 4, 8, 2, 8, 6]:
         #   Game.roll(Game,pins)
    Game.muchos_rolls(Game, 1, 20)
    assert Game.scoreFinal(Game) == 6