import turtle
import time
import random

# Kassastærð = 40

boltar = 1
turn = 1
boltarnir = []
iGangi = 3

class Kassi():
    def __init__(self):
        staerd = 50
        pos = random.randint(0, 7)
        self.h = staerd
        self.w = staerd
        self.kassaTeiknari = turtle.Turtle()
        self.pos = pos
        self.x = [-200+self.h*pos, -200+self.h*pos+50]
        self.y = [250, 300]
        self.hp = 1

        self.kassaTeiknari.penup()
        self.kassaTeiknari.setposition(-200+self.h*pos, 300-self.h)
        self.kassaTeiknari.pendown()
        self.kassaTeiknari.hideturtle()
        self.kassaTeiknari.color("red")

        self.kassaTeiknari.begin_fill()
        for x in range(4):
            self.kassaTeiknari.forward(self.w)
            self.kassaTeiknari.left(90)
        self.kassaTeiknari.end_fill()

    def faeraNidur(self):
        global haetta
        self.kassaTeiknari.clear()
        y = self.kassaTeiknari.ycor()
        self.kassaTeiknari.penup()
        self.kassaTeiknari.sety(y-50)
        self.kassaTeiknari.pendown()
        self.y[0] -= 50
        self.y[1] -= 50

        self.kassaTeiknari.begin_fill()
        for x in range(4):
            self.kassaTeiknari.forward(self.w)
            self.kassaTeiknari.left(90)
        self.kassaTeiknari.end_fill()
        if y-50 <= -300:
            haetta += 1
        return haetta

def buaTilBolta():
    bolti = turtle.Turtle()
    bolti.penup()
    bolti.shape("circle")
    bolti.color("white")
    return bolti

def haegri():
    global iGangi
    if iGangi == 0:
        spilari.right(3)

def vinstri():
    global iGangi
    if iGangi == 0:
        spilari.left(3)

def collistioncalc(turtle, bool=0):
    grada = turtle.heading()

    if bool == 0:
        turtle.setheading(180-grada)
    else:
        turtle.setheading(360-grada)

def collision():
    for bolti in boltarnir:
        # Boltinn er eyðilagður
        if bolti.ycor() < -300:
            collistioncalc(bolti)
            bolti.clear()
            bolti.hideturtle()
            boltarnir.remove(bolti)

        elif bolti.ycor() > 290:
            bolti.sety(290)
            collistioncalc(bolti, 1)
            skjar.update()

        elif bolti.xcor() < -190:
            print("-200")
            bolti.setx(-190)
            collistioncalc(bolti)
            skjar.update()

        elif bolti.xcor() > 190:
            bolti.setx(190)
            collistioncalc(bolti)
            skjar.update()

        else:
            by = bolti.ycor()
            bx = bolti.xcor()
            for kassi in kassar:
                ky = kassi.y
                kx = kassi.x
                if bx+10 > kx[0] and bx-10 < kx[1]:
                    if by+10 > ky[0] and by-10 < ky[1]:
                        if by <= ky[0] or by >= ky[1]:
                            collistioncalc(bolti, 1)
                            kassi.kassaTeiknari.clear()
                            kassar.remove(kassi)
                            try:
                                kassi.kassaTeiknari.clear()
                            except:
                                print("Það virkaði ekki")
                            print("Hérna kom hann að ofan/neðan")

                        else:
                            collistioncalc(bolti)
                            kassi.kassaTeiknari.clear()
                            kassar.remove(kassi)
                            try:
                                kassi.kassaTeiknari.clear()
                            except:
                                print("Það virkaði ekki")
                            print("Hérna kom hann hliðin á")

def faeraBolta():
    for x in range(boltar):
        bolti = buaTilBolta()
        bolti.setheading(spilari.heading())
        bolti.setposition(0, spilari.ycor()+10)
        boltarnir.append(bolti)

def skjota():
    global iGangi
    global turn
    if iGangi == 0:
        hreyfa_start = 0
        faeraBolta()
        iGangi = 1
        while len(boltarnir) >= 1:
            hreyfa_end = time.time()
            if hreyfa_end - hreyfa_start >= 0.001:
                for bolti in boltarnir:
                    bolti.showturtle()
                    bolti.forward(3)
                    hreyfa_start = time.time()
            collision()
            skjar.update()
        iGangi = 2
        turn += 1

skjar = turtle.Screen()
skjar.bgcolor("black")
skjar.setup(500, 700)
skjar.tracer(0)

bob = turtle.Turtle()
bob.penup()
bob.hideturtle()
bob.setposition(-200, -300)
bob.pendown()
bob.color("red")
for x in range(2):
    bob.forward(400)
    bob.left(90)
    bob.forward(600)
    bob.left(90)

spilari = turtle.Turtle()
spilari.penup()
spilari.color("orange")
spilari.shape("classic")
spilari.turtlesize(5)
spilari.setheading(90)
spilari.setposition(0, -250)

skjar.listen()
skjar.onkeypress(haegri, "Right")
skjar.onkeypress(vinstri, "Left")
skjar.onkeypress(skjota, "space")
start = 0

kassar = []
haetta = 0
while True:
    if iGangi == 2:
        for kassi in kassar:
            haetta = kassi.faeraNidur()
        print(haetta)
        iGangi = 3

    if haetta > 0:
        break

    elif iGangi == 3:
        for x in range(3, 7):
            kassar.append(Kassi())
        iGangi = 0
    skjar.update()

print("Leik lokið")