from tkinter import *

win = Tk()

list = [0, 1, 2, 3, 4]
litir = ["Yellow", "Red", "Blue", "Black", "Purple"]
list.sort(reverse=True)

canvas = Canvas(win, width=200, height=100)
canvas.pack()

for nr, (tala, litur) in enumerate(zip(list, litir)):
    sula = canvas.create_rectangle(0+nr*20, 200, 20+nr*20, 0+20*nr, fill=litur)

win.mainloop()
