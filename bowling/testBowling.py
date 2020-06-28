from bowling import Game


'''
#def testStrike():
#    Game.roll(Game, 10)
#    assert Game.strike(Game, 0)

#def testSpare():
#   Game.roll(Game, 5)
#   Game.roll(Game, 5)
#   assert Game.spare(Game, 0)

#def test_gutter_game():
#    Game.muchos_rolls(Game, 0, 20)
#   assert Game.scoreFinal(Game) == 0 

#def testRandom():
#    for pins in [10, 10, 10, 10, 10, 10, 10, 10,
#                     10, 10, 10, 10]:
#            Game.roll(Game,pins)
    #Game.muchos_rolls(Game, 10, 12)
#    assert Game.scoreFinal(Game) == 300

def testScore():
    Game.muchos_rolls(Game, 10, 12)
    assert (Game.scoreFinal(Game)==300)
'''
#def testUnos():
#        Game.muchos_rolls(Game, 1, 20)
#        assert Game.scoreFinal(Game) == 20

def test_muchos_strikes():
    Game.roll(Game, 10)
    Game.roll(Game, 7)
    Game.roll(Game, 3)
    Game.muchos_rolls(Game, 1, 10)
    assert Game.scoreFinal(Game) == 49

#def testPuntajePerfecto():
#    Game.muchos_rolls(Game, 10, 12)
#    assert (Game.scoreFinal(Game)==300)
