# 11-14-2015
# graphic_interface.py
# Interface for graphic UI of simple guessing game.

from tkinter import *

class GraphicInterface:
    def __init__(self):
        self.master = Tk()
        self.master.minsize(width=666, height=666)
        self.master.configure(bg="grey")
        self.master.title("Guess the Number")

        self.show_state(["_", "_", "_", "_", "_", "_" ]) # for testing

        INTRO = "Welcome! You will have 7 chances to Guess the Number."
        self.messages(INTRO)

        self.get_guess() # for testing


        self.master.mainloop()



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

    def button_click(self, event):
        # print(e.get())
        # value = e.get()
        # string.set(" ")
        # return value
        return self.entry.get()

    def get_guess(self):
        row = Frame(self.master)
        msg = "Enter an integer from 1 to 10,000: "
        self.label4 = Label(row,text=msg, bg="grey", font="Times 20")
        v = StringVar()
        self.entry = Entry(row, textvariable=v, relief=RAISED)
        self.entry.bind("<Return>", self.button_click)
        row.pack(side=TOP)
        self.label4.pack(side=LEFT)
        self.entry.pack(side=RIGHT)
        Button(self.master, text="Submit", command=self.button_click).pack()

    def messages(self, msg):
        label3 = Label(self.master, text=msg, bg="grey", pady=50, font = "Times 20")

        label3.pack()
