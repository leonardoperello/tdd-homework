
class Game:
    # rolls deberia tener entre 20 y 22 elementos ya que representa a los turnos para tirar
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
        return self.rolls[roll_] == 10

    def pinsEnPosicion(self, roll_):
        return self.rolls[roll_]
    
    def muchos_rolls(self, pins, num):
        for i in range(num):
            Game.roll(self, pins)

    #determina si termino el juego (iniciado, por eso entre el self) o no
    def juegoTerminado(self):
        return((len(self.rolls)==20) | len(self.rolls)==22)

    #creo que el puntaje perfecto es 300, CREO
    def puntajePerfecto(self):
        return(self.current_score==300)


    