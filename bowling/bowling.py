
class Game:
    # rolls deberia tener entre 20 y 22 elementos ya que representa a los turnos para tirar
    # y cada posicion deberia tener el numero de pinos que se tiraron en ese turno
    current_score = 0
    totalPins = 10
    rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def scoreFinal(self):
        rollsPrincipales = 20
        actualRoll = 0
        self.rolls[rollsPrincipales]
        for x in range(10):
            if(self.strike(actualRoll)):
                current_score += 10 + self.rolls[actualRoll+1] + self.rolls[actualRoll+2]
                actualRoll += 1
            elif (self.spare(actualRoll)):
                current_score += 10 + self.rolls[actualRoll+2]
                actualRoll += 2
            else:
                current_score += self.rolls[actualRoll] + self.rolls[actualRoll+1]
                actualRoll += 2

    #metodo spare
    def spare(self, roll_):
        return(self.rolls[roll_] + self.rolls[roll_+1] == self.totalPins)

    def strike(self, roll_):
        #if(self.rolls[roll_] == self.totalPins):
        #    return True
        return self.rolls[roll_] == 10

    def pinsEnPosicion(self, roll_):
        return self.rolls[roll_]
    
    #determina si termino el juego (iniciado, por eso entre el self) o no
    def juegoTerminado(self):
        return((len(self.rolls)==20) | len(self.rolls)==22)

    #el puntaje perfecto es 300
    def puntajePerfecto(self):
        return(self.current_score==300)

    def muchos_rolls(self, pins, num):
        for i in range(num):
            self.roll(Game,pins)

    