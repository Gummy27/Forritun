import math

class Vigur:
    # Smiður frumstillir x og y hnit vigurs eftir parametrum
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Fall sem skrifar hnit vigurs á skjá
    def prenta(self):
        print(f"[{self.x} {self.y}]")
    
    # Fall sem skilar lengd
    def lengd(self):
        return round((self.x**2+self.y**2)**0.5, 2)
    
    # Fall sem skilar hallatölu
    def halli(self):
        return round((self.y / self.x), 2)
    
    # Fall sem skilar þvervigri
    def þvervigur(self):
        return Vigur(self.y*-1, self.x)
    
    def innfelldi(self, annarVigur):
        return self.x * annarVigur.x + self.y * annarVigur.y

    # Fall sem skilar stefnuhorni
    def stefnuhorn(self):
        return round(math.degrees(math.atan(self.y/self.x)), 1)
    
    # Fall sem tekur vigur sem parameter og skilar horni milli vigra
    def horn(self,v):
        return round(v.stefnuhorn() - self.stefnuhorn(), 2)
    
    # Fall sem tekur vigur sem parameter og skilar summu vigri
    def summa(self,v):
        return Vigur(self.x + v.x, self.y + v.y)  

# Keyrsluforrit
v1 = Vigur(1, 3)
v1.prenta()
print("Lengd: ", v1.lengd())
print("Halli: ", v1.halli())
vþ = v1.þvervigur()
print("Þvervigur: " , end=" ")
vþ.prenta()
print("Stefnuhorn: ", v1.stefnuhorn())    
v2 = Vigur(-3,1)
print("Horn milli vigra: " , v2.horn(v1))
v3 = v1.summa(v2)
print("Summa: " , end=" ")
v3.prenta()

