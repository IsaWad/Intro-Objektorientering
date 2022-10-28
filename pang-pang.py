from ast import Break
import random as rand



class Player():
    def __init__(self, lifes):
        self.lifes = lifes
        self.score = 0
        self.did_hit = False
        self.is_hitted = False

    def fire(self):
        if rand.randint(1,10) in {1, 2, 4, 7, 8, 9}:
            self.did_hit = True
        else:
            self.is_hitted = False
            self.did_hit = False
    def inc_score(self):
        if rand.randint(1,10) in {1, 9}:
            self.score += 2
            print("Headshoot!")
        else:
            self.score += 1
            print("Fienden träffad!")

    def reduce_life(self):
        self.lifes -= 1
        print("Du blev träffad!")    
a_player = Player(3)
a_player.fire

while a_player.lifes != 0:
    input("Tryck Enter för att skjuta")
    #eldgivning = randint(1,10)
    
    a_player.fire()
    if a_player.did_hit:
        a_player.inc_score()
    else:
        a_player.reduce_life()
    print("Score: ", a_player.score)
    print("HP: ", a_player.lifes)
print("Spel avslutats")