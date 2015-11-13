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

    def error_messages(self, error, value):
        errors = { "type": "'{}' is not an integer.".format(value),
                   "range": "{} is not in range.".format(str(value)),
                   "dups": "You already guessed {}.".format(str(value)) }
        print(errors[error])

    def check_type(self, guesses):
        value = self.get_guess(guesses)
        try:
            int(value)
        except ValueError:
            self.error_messages("type", value)
            return self.get_guess(guesses)
        return value

    def get_guess(self, guesses):
        return input("Enter an integer from 1 to 10,000: ")

    def result_message(self, msg):
        print(msg)
