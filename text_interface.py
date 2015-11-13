# 11-12-2015
# text_interface.py
# Interface for text UI of simple guessing game.


class TextInterface:
    def __init__(self):
        print("Welcome to Guess an Integer.")
        print("In this game, you have chances to guess a number from 1 to 10,000.\n")

    def close(self):
        print("Thank you for playing!\n")

    def show_state(self, guesses):
        print("Your current guesses are: " + " ".join(guesses) + "\n")

    def play_again(self):
        play_again = input("Do you want to play again? ")
        return play_again[0] in "yY"

    def check_type(self, guesses):
        while True:
            value = self.get_guess(guesses)
            try:
                int(value)
                return value
            except ValueError:
                self.messages("'{}' is not an integer.".format(value))

    def get_guess(self, guesses):
        return input("Enter an integer from 1 to 10,000: ")

    def messages(self, msg):
        print(msg)
