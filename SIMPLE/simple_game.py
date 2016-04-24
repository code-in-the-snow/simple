# 11-12-2015
# simple_game.py
# Script that calls game app and interface.

from gameApp import GameApp
# from graphic_interface import GraphicInterface
#
# interface = GraphicInterface()
# game = GameApp(interface)
# game.run()

def getInterfaceChoice():
    menu = ["Play from the command line.", "Play with a graphical interface."]
    while True:
        print("\n")
        for index, item in enumerate(menu, start=1):
            print(index, "\t", item)
        try:
            choice = int(input("\nChoose a game option: "))
            if choice in [1,2]:
                return choice
            else: print("Choose a number from the listed game options.")
        except ValueError:
            print("Choose the number of a listed game option.")

def executeChoice(choice):
    if choice == 1:
        from text_interface import TextInterface
        interface = TextInterface()
    else:
        from graphic_interface import GraphicInterface
        interface = GraphicInterface()
    game = GameApp(interface)
    game.run()


def main():
    choice = getInterfaceChoice()
    executeChoice(choice)

if __name__ == "__main__": main()
