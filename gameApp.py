# 11-12-2015
# gameApp.py
# This is a class to run a simple guessing game.  OO design.  Meant to be
#    easily extensible to more complicated game.

from random import randint

class GameApp(self):
    def __init__(self, interface):
        self.goal = randint(1, 1001)
        self.guess_count = 0
        self.guesses = [ "_", "_", "_", "_","_" ]

    def run(self):
        while self.guesses < 5 and (self.goal not in self.guesses):
            self.playRound()
        close

    def playRound(self):
        #display initial state
        cur_guess = self.getGuess()
        self.guesses[self.guess_count] = cur_guess

        #display state  pass guesses array for print

        self.guess_count += 1

    def getGuess(self):
        guess = self.guesses[0]
        while guess in self.guesses:
            guess = input("Enter an integer from 1 - 1000: ")
        return guess
