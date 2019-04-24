import turtle
import time
import random

staerd = 700

litir = [
    "red",
    "blue",
    "purple",
    "black",
    "pink",
    "brown",
    "orange",
    "green"
]

def nullstilla(x, y, skjaldbaka):
    skjaldbaka.penup()
    skjaldbaka.setposition(x, y)
    skjaldbaka.pendown()


skjar = turtle.Screen()
skjar.setup(width=staerd+100, height=staerd+100)
skjar.tracer(0)

teiknari1 = turtle.Turtle()
teiknari1.speed(0)
teiknari2 = turtle.Turtle()
teiknari2.speed(0)

teiknari1.hideturtle()
teiknari2.hideturtle()

for i in range(7):
    pixlar = 1
    hp = staerd // 2  # Hæsti Punktur
    notudhnit = []
    for x in range(8-i):
        litur = random.choice(litir)
        teiknari1.color(litur)
        teiknari2.color(litur)
        linuHnit = staerd / pixlar

        for x in range(pixlar + 1):
            hnit = linuHnit*x-hp
            if hnit not in notudhnit:
                nullstilla(hnit, hp * -1, teiknari1)
                nullstilla(hp, hnit*-1, teiknari2)
                teiknari1.sety(hp)
                teiknari2.setx(hp*-1)
                notudhnit.append(hnit)

        teiknari1.hideturtle()

        skjar.update()
        time.sleep(0.5)
        pixlar += pixlar
    staerd -= 100
input()

