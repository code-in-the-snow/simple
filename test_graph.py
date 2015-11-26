# 11-26-2015
# test_graph.py
# Working design to return value from Entry item

from tkinter import *
import pdb

class GraphicInterface:
    def __init__(self):
        self.master = Tk()
        self.master.minsize(width=666, height=666)
        self.master.configure(bg="grey")
        self.master.title("Guess the Number")
        self.v = StringVar()
        self.entry_var = StringVar()

        self.show_state(["_", "_", "_", "_", "_", "_" ]) # for testing
        INTRO = "Welcome! You will have 7 chances to Guess the Number."
        self.messages(INTRO)
        print(self.get_guess()) # for testing
        self.master.mainloop()
        label3.pack()

    def close(self):
        self.master.destroy

    def show_state(self, guesses):
        formatted = []
        for item in guesses:
            item = item + "_"
            formatted.append(item)
        self.label1 = Label(self.master, text="Your current guesses are: " + " ".join(formatted), bg="grey", font = "Times 20")
        self.label1.pack()

    def play_again(self):
        pass

    def entry_callback(self, event):
        self.entry_var.set(self.v.get())


    def get_guess(self):
        row = Frame(self.master)
        msg = "Enter an integer from 1 to 10,000: "
        self.label4 = Label(row,text=msg, bg="grey", font="Times 20")
        self.entry = Entry(row, textvariable=self.v)
        row.pack(side=TOP)
        self.label4.pack(side=LEFT)
        self.entry.pack(side=RIGHT)
        self.entry.bind("<Return>", self.entry_callback)
        return self.entry_var

    def messages(self, msg):
        label3 = Label(self.master, text=msg, bg="grey", pady=50, font = "Times 20")
