# 11-26-2015
# test_graph.py
# Working design to return value from Entry item

from tkinter import *
import pdb, time, os, sys

class GraphicInterface:
    def __init__(self):
        self.master = Tk()
        self.master.minsize(width=666, height=666)
        self.master.configure(bg="grey")
        self.master.title("Guess the Number")
        self.mouseX = None
        self.mouseY = None
        self.master.bind("<Button-1>", self._onClick)

        INTRO = "Welcome! You will have 7 chances to Guess the Number."
        Label(self.master, text=INTRO, bg="grey", font="Times 20").pack()

        separator1 = Frame(height=2)
        separator1.pack(padx=3, pady=3)

        self.v = StringVar()
        self.labelShowState = Label(self.master, textvariable=self.v, bg="grey", font="Times 20")
        self.labelShowState.pack()

        separator2 = Frame(height=4)
        separator2.pack(padx=3, pady=3)

        MSG_PROMPT = "Enter an integer from 1 to 10,000: "
        row1 = Frame()
        self.labelPrompt = Label(row1,text=MSG_PROMPT, bg="grey", font="Times 20")
        self.e = Entry(row1)
        row1.pack(side=TOP)
        self.labelPrompt.pack(side=LEFT)
        self.e.pack(side=RIGHT)

        separator = Frame(height=2)
        separator.pack(padx=3, pady=3)

        self.buttonSubmit = Button(self.master, text="Submit", width=10)
        self.buttonEnd = Button(self.master, text="End Game", width=10)
        self.buttonSubmit.pack(side=LEFT)
        self.buttonEnd.pack(side=LEFT)

        self.m = StringVar()
        self.labelMessage = Label(self.master, textvariable=self.m, bg="grey", pady=50, font = "Times 20")
        self.labelMessage.pack()

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
            #if self.isClosed(): raise GraphicsError("getMouse in closed window")
            time.sleep(.1) # give up thread

    def _onClick(self, e):
        self.mouseX = e.x
        self.mouseY = e.y

    def play_again(self):
        pass

    def show_state(self, guesses):
        guessDisplay = []
        for item in guesses:
            guessDisplay.append(item)
        self.v.set("Your current guesses are: " + " ".join(guessDisplay))

    def messages(self, msg):
        self.m.set(msg)
