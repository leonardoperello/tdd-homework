
class Game():

    def play_bowling(self, current_score, rolls, pins):
        return current_score + rolls * pins 

# If in two tries he knocks them all down, this is called a “spare” and
# his score for the frame is ten plus the number of pins knocked down on his next 
# throw (in his next turn).
    def spare(self, current_score, rolls, pins):
        if(rolls == 2 & pins == 10):
            return True

    def strike(self, current_score, rolls, pins):
        if(rolls == 1 & pins == 10):
            return True

    