# 11-26-2015
# test_graph.py
# Working design to return value from Entry item

from tkinter import *
import pdb, time, os, sys

class GraphicInterface:
    def __init__(self):
        self.master = Tk()
        # self.master.minsize(width=666, height=333)
        # self.master.configure(bg="grey")
        # self.master.title("Guess the Number")
        self.parent = Frame(self.master)
        self.parent.configure(bg="grey")
        self.parent.master.title("Guess the Number")
        self.parent.pack(fill=BOTH, expand=True)
        self.mouseX = None
        self.mouseY = None
        self.master.bind("<Button-1>", self._onClick)

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
        self.labelMessage = Label(row4, textvariable=self.m, bg="grey", pady=50, font = "Times 20")
        self.labelMessage.pack()

        row5 = Frame(self.parent)
        row5.configure(bg="grey")
        row5.pack()
        self.buttonSubmit = Button(row5, text="Submit", width=15).pack(side=LEFT, padx=70)
        self.buttonPlayAgain = Button(row5, text="Play Again", width=15).pack(side=LEFT, padx=15)
        self.buttonEnd = Button(row5, text="End Game", width=15).pack(side=LEFT, padx=15)

    def close(self):
        self.getMouse()
        self.master.destroy

    def get_guess(self):
        self.e.focus_set()
        self.getMouse()
        guess = self.e.get()
        self.e.delete(0, END)
        return guess

    def getMouse(self):
        """Wait for mouse click and return Point object representing
        the click"""
        self.master.update()      # flush any prior clicks
        self.mouseX = None
        self.mouseY = None
        while self.mouseX == None or self.mouseY == None:
            self.master.update()
            time.sleep(.1) # give up thread

    def _onClick(self, e):
        self.mouseX = e.x
        self.mouseY = e.y

    def play_again(self):
        self.getMouse()

    def show_state(self, guesses):
        guessDisplay = []
        for item in guesses:
            guessDisplay.append(item)
        self.v.set("Your current guesses are: " + " ".join(guessDisplay))

    def messages(self, msg):
        self.m.set(msg)
