# 11-12-2015
# gameApp.py
# This is a class to run a simple guessing game.  OO design.  Meant to be
#    easily extensible to more complicated game.

from random import randint

class GameApp:
    def __init__(self, interface):
        self.goal = 21 #randint(1, 10001)
        self.guess_count = 0
        self.guesses = [ "_", "_", "_", "_","_" ]
        self.interface = interface

    def run(self):
        self.interface.show_state(self.guesses)
        while self.guess_count < 5 and (str(self.goal) not in self.guesses):
            self.play_round()
        if str(self.goal) in self.guesses:
            msg = "WINNER! The number was {} and you guessed it.".format(str(self.goal))
        else:
            msg = "OUT OF GUESSES. The number was {}.".format(str(self.goal))
        self.interface.messages(msg)
        if self.interface.play_again():
            self.guess_count = 0
            self.guesses = [ "_", "_", "_", "_", "_" ]
            self.run()
        else:
            self.interface.close()

    def input_validation(self):
        value = self.interface.check_type(self.guesses)
        while int(value) < 1 or int(value) > 10000 or value[0] == "0":
            self.interface.messages("{} is not in range.".format(value))
            value = self.interface.check_type(self.guesses)
        while value in self.guesses:
            self.interface.messages("You already guessed {}.".format(value))
            value = self.interface.check_type(self.guesses)
        return value

    def play_round(self):
        cur_guess = self.input_validation()
        self.guesses[self.guess_count] = cur_guess
        self.interface.show_state(self.guesses)
        self.guess_count += 1
