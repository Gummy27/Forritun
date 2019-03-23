import turtle
import itertools

global flag
global takki
flag = False
takki = 0

bord = ["-", "-", "-","-", "-", "-","-", "-", "-"]
stadsetningar = [[-290, 290], [-90, 290], [110, 290], [-290, 90], [-90, 90], [110, 90], [-290, -110], [-90, -110], [110, -110]]

spilari = itertools.cycle(["x", "y"])

# Skjár
wn = turtle.Screen()
wn.title("Tic Tac Toe by Gummy27")
wn.bgcolor("white")
wn.setup(width=700, height=700)

grid = turtle.Turtle()
grid.speed(0)
grid.pencolor("black")
grid.right(90)

wn.tracer(0)

for x in range(2):
    grid.penup()
    grid.goto(-100+(200*x), 300)
    grid.pendown()
    grid.forward(600)
grid.right(90)
for x in range(2):
    grid.penup()
    grid.goto(300, -100+(200*x))
    grid.pendown()
    grid.forward(600)
grid.hideturtle()
wn.update()

#Teiknari
teiknari = turtle.Turtle()
teiknari.speed(0)
teiknari.pencolor("black")

# Functions
# Innsláttur
#  1 Röð
def grid_1():
    if(bord[0] == "-"):
        global takki
        takki = 0
        teikna()

def grid_2():
    if (bord[1] == "-"):
        global takki
        takki = 1
        teikna()

def grid_3():
    if (bord[2] == "-"):
        global takki
        takki = 2
        teikna()

#2 Röð
def grid_4():
    if (bord[3] == "-"):
        global takki
        takki = 3
        teikna()

def grid_5():
    if (bord[4] == "-"):
        global takki
        takki = 4
        teikna()

def grid_6():
    if (bord[5] == "-"):
        global takki
        takki = 5
        teikna()

#3 Röð
def grid_7():
    if (bord[6] == "-"):
        global takki
        takki = 6
        teikna()

def grid_8():
    if (bord[7] == "-"):
        global takki
        takki = 7
        teikna()

def grid_9():
    if(bord[8] == "-"):
        global takki
        takki = 8
        teikna()


# Gáir hvort að einhver sé búinn að vinna.
def VinnaTjekkari(takn):
    global  flag
    for x in range(3):
        if(bord[0+x*3] == takn and bord[1+x*3] == takn and bord[2+x*3] == takn):
            flag = True
            print("Ragnar")
        elif(bord[0+x] == takn and bord[3+x] == takn and bord[6+x] == takn):
            flag = True
            print("Ragnar")
    if(bord[0] == takn and bord[4] == takn and bord[8] == takn):
        flag = True
        print("Ragnar")
    elif(bord[2] == takn and bord[4] == takn and bord[6] == takn):
        flag = True
        print("Ragnar")
    teljari = 0
    for x in range(9):
        if(bord[x] != "-"):
            teljari += 1
    if(teljari == 9):
        flag = True

# Teikna
def teikna():
    global spilari
    hnit = stadsetningar[takki]

    teiknari.penup()
    teiknari.goto(hnit[0], hnit[1])
    teiknari.pendown()

    global nuverandi
    nuverandi = next(spilari)
    bord[takki] = nuverandi;
    if(nuverandi == "x"):
        # Kross
        x = teiknari.xcor()
        y = teiknari.ycor()
        teiknari.right(45)
        teiknari.forward(260)
        teiknari.right(90)
        teiknari.penup()
        teiknari.goto(x+180, y)
        teiknari.pendown()
        teiknari.forward(260)
        teiknari.left(135)

    else:
        teiknari.penup()
        teiknari.goto(teiknari.xcor()+90, teiknari.ycor()-180)
        teiknari.pendown()
        teiknari.circle(90)
    VinnaTjekkari(nuverandi)


# Lyklaborð
wn.listen()

wn.onkeypress(grid_1, "7")
wn.onkeypress(grid_2, "8")
wn.onkeypress(grid_3, "9")
wn.onkeypress(grid_4, "4")
wn.onkeypress(grid_5, "5")
wn.onkeypress(grid_6, "6")
wn.onkeypress(grid_7, "1")
wn.onkeypress(grid_8, "2")
wn.onkeypress(grid_9, "3")

while(True):
    if(flag != True):
        wn.update()
    else:
        wn.update()
        if(wn.textinput("Leikur kláraður", "Viltu  spila annan leik? : ").lower() == "já"):
            bord = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
            teiknari.reset()
            flag = False

            if(nuverandi == "x"):
                next(spilari)
            wn.listen()

            wn.onkeypress(grid_1, "7")
            wn.onkeypress(grid_2, "8")
            wn.onkeypress(grid_3, "9")
            wn.onkeypress(grid_4, "4")
            wn.onkeypress(grid_5, "5")
            wn.onkeypress(grid_6, "6")
            wn.onkeypress(grid_7, "1")
            wn.onkeypress(grid_8, "2")
            wn.onkeypress(grid_9, "3")
        else:
            wn.done()
            break

wn.mainloop()
