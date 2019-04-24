import turtle
import time

def nullstilla(x, y, skjaldbaka):
    skjaldbaka.penup()
    skjaldbaka.setposition(x, y)
    skjaldbaka.pendown()

class Fani():
    def __init__(self, h, l, b, hnit=[]):
        self.l = l
        self.b = b
        self.h = h
        self.w = 200 / l * b
        self.hh = h / 2
        self.hw = self.w / 2
        self.cord = hnit

        self.teiknari = turtle.Turtle()
        self.teiknari.speed(0)
        self.teiknari.hideturtle()

    def cordgenerator(self):
        if len(self.cord[0]) == 5:
            l, b = self.cord[0], self.cord[1]
            hnit1 = []
            hnit2 = []
            hnit1.append([l[0],    0])     
            hnit1.append([l[0], b[0]])
            hnit1.append([0   , b[0]])    
            hnit1.append([0   , b[3]]) 
            hnit1.append([l[0], b[3]])
            hnit1.append([l[0], b[4]])        
            hnit1.append([l[3], b[4]])       
            hnit1.append([l[3], b[3]])
            hnit1.append([l[4], b[3]])
            hnit1.append([l[4], b[0]])
            hnit1.append([l[3], b[0]])
            hnit1.append([l[3],    0])
            hnit1.append([l[0],    0])

            hnit2.append([l[1],    0])
            hnit2.append([l[1], b[1]])
            hnit2.append([0   , b[1]])
            hnit2.append([0   , b[2]])
            hnit2.append([l[1], b[2]])
            hnit2.append([l[1], b[4]])
            hnit2.append([l[2], b[4]])
            hnit2.append([l[2], b[2]])
            hnit2.append([l[4], b[2]])
            hnit2.append([l[4], b[1]])
            hnit2.append([l[2], b[1]])
            hnit2.append([l[2],    0])
            hnit2.append([l[1],    0])

            self.cord = []
            self.cord.append(hnit1)
            self.cord.append(hnit2)
        else:
            hnit = []
            l, b = self.cord[0], self.cord[1]
            hnit.append([l[0],    0])
            hnit.append([l[0], b[0]])
            hnit.append([0  ,  b[0]])
            hnit.append([0  ,  b[1]])
            hnit.append([l[0], b[1]])
            hnit.append([l[0], b[2]])
            hnit.append([l[1], b[2]])
            hnit.append([l[1], b[1]])
            hnit.append([l[2], b[1]])
            hnit.append([l[2], b[0]])
            hnit.append([l[1], b[0]])
            hnit.append([l[1],    0])
            hnit.append([l[0],    0])
            self.cord = hnit

    def bakgrunnur(self, litur):
        nullstilla(self.hw * -1, self.hh * -1, self.teiknari)
        self.teiknari.color(litur)
        self.teiknari.begin_fill()
        for x in range(2):
            self.teiknari.forward(self.w)
            self.teiknari.left(90)
            self.teiknari.forward(self.h)
            self.teiknari.left(90)
        self.teiknari.end_fill()

    def kross(self, litur1, litur2=""):
        litir = [litur1, litur2]
        teljari = 0
        self.teiknari.penup()
        if len(self.cord) <= 2:
            for i in self.cord:
                self.teiknari.color(litir[teljari])
                self.teiknari.begin_fill()
                teljari += 1
                for x, y in i:
                    x *= self.h / self.l
                    y *= self.w / self.b
                    self.teiknari.setposition(x - self.hw, y - 100)
                    self.teiknari.pendown()
                self.teiknari.end_fill()

        else:
            self.teiknari.begin_fill()
            self.teiknari.color(litur1)
            for x, y in self.cord:
                x *= self.h / self.l
                y *= self.w / self.b
                self.teiknari.setposition(x - self.hw, y - 100)
                self.teiknari.pendown()
            self.teiknari.end_fill()
        skjar.update()
        time.sleep(3)
        self.teiknari.clear()

    def tricolour(self, l1, l2, l3):
        litir = [l1, l2, l3]
        skipting = self.w / 3
        for teljari, litur in enumerate(litir):
            x = self.teiknari.xcor()
            nullstilla((self.hw*-1)+skipting*teljari, -100, self.teiknari)
            self.teiknari.color(litur)
            self.teiknari.begin_fill()
            for i in range(2):
                self.teiknari.forward(skipting)
                self.teiknari.left(90)
                self.teiknari.forward(200)
                self.teiknari.left(90)
            self.teiknari.end_fill()
        skjar.update()
        time.sleep(3)
        self.teiknari.clear()


    def eyda(self):
        self.teiknari.clear()

skjar = turtle.Screen()
skjar.setup(800, 800)
skjar.bgcolor("black")
skjar.tracer(0)

# Þrílitafánar
franski = Fani(200, 2, 3)
franski.tricolour("blue", "white", "red")

rumenski = Fani(200, 2, 3)
rumenski.tricolour("darkblue", "yellow", "red")

nigeriski = Fani(200, 2, 3)
nigeriski.tricolour("green", "white", "green")

filabeins = Fani(200, 2, 3)
filabeins.tricolour("orange", "white", "green")

italiski = Fani(200, 2, 3)
italiski.tricolour("green", "white", "red")

irski = Fani(200, 2, 3)
irski.tricolour("green", "white", "orange")

mali = Fani(200, 2, 3)
mali.tricolour("green", "yellow", "red")

belgiski = Fani(200, 2, 3)
belgiski.tricolour("black", "yellow", "crimson")

guinea = Fani(200, 2, 3)
guinea.tricolour("red", "yellow", "green")

# Norðurlandafánar
hlutfoll = [[7, 8, 10, 11, 25], [7, 8, 10, 11, 18]]
islenski = Fani(200, 18, 25, hlutfoll)
islenski.cordgenerator()
islenski.bakgrunnur("blue")
islenski.kross("white", "red")
islenski.eyda()

hlutfoll = [[5, 7, 16], [4, 6, 10]]
saenski = Fani(200, 10, 16, hlutfoll)
saenski.cordgenerator()
saenski.bakgrunnur("blue")
saenski.kross("yellow")
saenski.eyda()

hlutfoll = [[6, 7, 9, 10, 22], [6, 7, 9, 10, 16]]
norski = Fani(200, 16, 22, hlutfoll)
norski.cordgenerator()
norski.bakgrunnur("red")
norski.kross("white", "blue")
norski.eyda()

input()