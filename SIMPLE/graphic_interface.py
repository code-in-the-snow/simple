# 04-22-2016
# graphic_interface.py

from tkinter import *
import time, os, sys

class GraphicInterface:
    def __init__(self):
        self.master = Tk()
        self.master.minsize(width=666, height=333)
        self.parent = Frame(self.master)
        self.parent.configure(bg="grey")
        self.parent.master.title("Guess the Number")
        self.parent.pack(fill=BOTH, expand=True)

        self.clicked = False
        self.playAgainVar = None
        self.submitVar = None
        self.master.bind("<Button-1>", self._onClick)

        row = Frame(self.parent)
        row.configure(bg="grey", height=30)
        row.pack()

        row1 = Frame(self.parent)
        row1.configure(bg="grey")
        row1.pack(fill=X)
        INTRO = "Welcome! You will have 7 chances to Guess the Number."
        Label(row1, text=INTRO, bg="grey", font="Times 20").pack()

        row2 = Frame(self.parent)
        row2.configure(background="grey")
        row2.pack(fill=X)
        self.v = StringVar()
        labelShowState = Label(row2, textvariable=self.v, bg="grey", font="Times 20")
        labelShowState.pack()

        row3 = Frame(self.parent)
        row3.configure(bg="grey")
        row3.pack()
        MSG_PROMPT = "Enter an integer from 1 to 10,000: "
        labelPrompt = Label(row3,text=MSG_PROMPT, bg="grey", font="Times 20")
        self.e = Entry(row3)
        labelPrompt.pack(side=LEFT)
        self.e.pack(side=RIGHT)

        row4 = Frame(self.parent)
        row4.configure(bg="grey")
        row4.pack(fill=X)
        self.m = StringVar()
        Label(row4, textvariable=self.m, bg="grey", pady=50, font = "Times 20").pack()

        self.drawButtons()

    def _onClick(self, e):
        self.clicked = True

    def _onEnd(self):
        self.playAgainVar = False

    def _onPlayAgain(self):
        self.messages(" ")
        self.playAgainVar = True

    def _onSubmit(self):
        self.submitVar = True

    def drawButtons(self):
        row5 = Frame(self.parent)
        row5.configure(bg="grey")
        row5.pack(fill=X)
        self.buttonSubmit = Button(row5, text="Submit", width=15, command=self._onSubmit).pack(side=LEFT, padx=65)
        self.buttonPlayAgain = Button(row5, text="Play Again", width=15, command=self._onPlayAgain).pack(side=LEFT)
        self.buttonEnd = Button(row5, text="End Game", width=15, command=self._onEnd).pack(side=LEFT, padx=65)

    def close(self):
        self.master.destroy

    def get_guess(self):
        self.e.focus_set()
        self.submitVar = None
        while self.submitVar == None:
            self.getMouse()
        guess = self.e.get()
        self.e.delete(0, END)
        return guess

    def getMouse(self):
        self.master.update()    
        self.clicked = False
        while self.clicked == False:
            self.master.update()
            time.sleep(.1)

    def play_again(self):
        self.playAgainVar = None
        while self.playAgainVar == None:
            self.getMouse()
        return self.playAgainVar

    def show_state(self, guesses):
        guessDisplay = []
        for item in guesses:
            guessDisplay.append(item)
        self.v.set("Your current guesses are: " + " ".join(guessDisplay))

    def messages(self, msg):
        self.m.set(msg)
