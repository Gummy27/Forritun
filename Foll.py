import turtle
import math

a = 1
b = -2
c = 1

class Fall():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def reiknaYHnit(self, x):
        return(self.a*x*x+self.b*x+c)

    def gildistafla(self, fra, til):
        print(" y | x ")
        for x in range(self, til):
            print(self.a*x*x+self.b*x+c, x)

p1 = Fall(a, b, c)
print(p1.reiknaYHnit(2))
p1

