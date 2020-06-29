from bowling import Game

def testSpare():
   g = Game([]) 
   g.roll(5)
   g.roll(5)
   assert g.spare(0)

def testSpare2():
   g = Game([])
   g.roll(2)
   g.roll(8)
   assert g.spare(0)

def testStrike():
    g = Game([])
    g.roll(10)
    assert g.strike(0)

def test_gutter_game():
    g = Game([])
    g.muchos_rolls(0, 20)
    assert g.scoreFinal() == 0 

def testPosicion():
    g = Game([])
    g.roll(10)
    assert g.pinsEnPosicion(0) == 10

def testScore():
    g = Game([])
    g.muchos_rolls(6, 20)
    assert (g.scoreFinal()==120)

def testUnos():
    g = Game([])
    g.muchos_rolls(1, 20)
    assert g.scoreFinal() == 20

def test_muchos_strikes():
    g = Game([])
    g.roll(10)
    g.roll(7)
    g.roll(3)
    g.muchos_rolls(1, 17)
    assert g.scoreFinal() == 47

def testPuntajePerfecto():
    g = Game([])
    g.muchos_rolls(10, 12)
    assert (g.scoreFinal()==300)

def testRandom():
    g = Game([])
    for pins in [1, 5, 7, 2, 9, 0, 8, 1,
                     10, 3, 2, 5, 3, 4, 1, 1, 1, 1, 1]:
            g.roll(pins)
    assert g.scoreFinal() == 70
    
def testRandom2():
    g = Game([])
    for pins in [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 
                5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5 ]:
            g.roll(pins)
    assert g.scoreFinal() == 150
    assert g.juegoTerminado

