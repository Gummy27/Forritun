from tkinter import *

win = Tk()

class TheGame():
    def __init__(self):
        self.spilari = 0
        self.takkar = []
        self.leikbord = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        for x in range(3):
            for i in range(3):
                takki = Button(win, width=20, height=10, text="Takki", command=lambda x=x, i=i: self.spila(x, i))
                takki.grid(column=x, row=i)
                self.takkar.append(takki)

    def spila(self, c, r):
        pos = c*3+r

        if self.leikbord[pos] == 0:
            self.takkar[pos].grid_forget()

            if self.spilari % 2 == 0:
                shape = "x"
            else:
                shape = "o"

            self.takkar[pos] = Button(win, text=shape, width=20, height=10).grid(column=c, row=r)

            self.leikbord[pos] = shape
            self.spilari += 1

klasi = TheGame()

win.mainloop()