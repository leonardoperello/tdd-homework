
class Game:
    # rolls deberia tener entre 20 y 22 elementos
    # y cada posicion deberia tener el numero de pinos que se tiraron en ese turno
    current_score = 0
    totalPins = 10
    rolls = []

    def roll(self, pins):
        self.rolls.append(pins)
        #metodo spare
    def spare(self, roll_):
        return(self.rolls[roll_] + self.rolls[roll_+1] == self.totalPins)

    def strike(self, roll_):
        #if(self.rolls[roll_] == self.totalPins):
        #    return True
        return self.rolls[roll_]

    