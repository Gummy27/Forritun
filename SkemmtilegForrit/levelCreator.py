import turtle
skjar = turtle.Screen()
teiknari = turtle.Turtle()
class level():
    def __init__(self, l, b, px=0):
        self.lengd = l
        self.breidd = b
        teiknari.penup()
        teiknari.pendown()
        self.px = px

    def __str__(self):
        return(str(self.lengd)+" x "+str(self.breidd))

    def bp(self):
        teiknari.penup()
        teiknari.setposition(self.lengd/2*-1, self.breidd/2*-1)
        teiknari.pendown()


    def border(self):
        teiknari.penup()
        teiknari.pendown()
        teiknari.setheading(90)
        for x in range(2):
            teiknari.forward(self.lengd)
            teiknari.right(90)
            teiknari.forward(self.breidd)
            teiknari.right(90)
        teiknari.penup()

    def pixlar(self):
        bp()
        teiknari.penup()
        teiknari.pendown()


b1 = level(100, 100, 20)
b1.border()
b1.pixlar()
input()

