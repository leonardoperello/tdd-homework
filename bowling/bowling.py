
class Game:
    # rolls deberia tener entre 20 y 22 elementos ya que representa a los turnos para tirar
    # y cada posicion deberia tener el numero de pinos que se tiraron en ese turno
    
    totalPins = 10
    rolls = []
        
    def roll(self, pins, rolls):
        rolls.append(pins)

    def scoreFinal(self, rolls):
        current_score = 0
        actualRoll = 0
        for x in range(10):
            if(Game.strike(self, actualRoll, rolls)):
                current_score += 10 + rolls[actualRoll+1] + rolls[actualRoll+2]
                actualRoll += 1
            elif (Game.spare(self, actualRoll, rolls)):
                current_score += 10 + rolls[actualRoll+2]
                actualRoll += 2
            else:
                current_score += rolls[actualRoll] + rolls[actualRoll+1]
                actualRoll += 2
        return current_score

    #metodo spare
    def spare(self, roll_, rolls):
        return(rolls[roll_] + rolls[roll_+1] == self.totalPins)

    def strike(self, roll_, rolls):
        #if(self.rolls[roll_] == self.totalPins):
        #    return True
        return rolls[roll_] == 10

    def pinsEnPosicion(self, roll_, rolls):
        return rolls[roll_]
    
    #determina si termino el juego (iniciado, por eso entre el self) o no
    def juegoTerminado(self):
        return((len(self.rolls)==20) | len(self.rolls)==22)

    def muchos_rolls(self, pins, num, rolls):
        for i in range(num):
            Game.roll(self, pins, rolls)

