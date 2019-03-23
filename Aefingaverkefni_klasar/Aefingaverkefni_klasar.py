#Gudmundur Brimir Bjornsson 
#Uppsetning hafinn 2019-03-19
def greinaskil(): 
    print('==========')

class FyrstiKlasi():
    def prentaUt(self, nafn, aldur):
        print("Halló", nafn, "þú ert", aldur, "gamall.")

    def tolur(self, tala1, tala2):
        if(tala1 < tala2):
            utkoma = tala2-tala1
        else:
            utkoma = tala1-tala2
        print("Það er", utkoma, "tölur á milli þessara talna.")

class AnnarKlasi():
    def prentaUt(self, nafn):
        print(nafn)

    def sidustuTveirStafir(self, nafn):
        print(nafn[-2:])

    def bilAMilli(self, nafn):
        for x in nafn:
            print(x, end=" ")
        print()

class ThridjiKlasi():
    def __init__(self, t1, t2):
        self.tala1 = t1
        self.tala2 = t2

    def samlagning(self):
        return(self.tala1+self.tala2)

    def margfoldun(self):
        return(self.tala1*self.tala2)

    def deiling(self):
        return(self.tala1/self.tala2)


verkefni = ['FyrstiKlasi', 'AnnarKlasi', 'ThridjiKlasi', 'Hætta'] 
while(True):
    for x, y in enumerate(verkefni): 
        print(str(x+1)+'.', y) 
    val = input('Hvaða dæmi viltu skoða? : ') 
    greinaskil() 

    if(val == '1'): 
        klasi1 = FyrstiKlasi()
        klasi1.prentaUt("Guðmundur", 16)
        klasi1.tolur(54, 23)
 
    elif(val == '2'): 
        h1 = AnnarKlasi()
        h2 = AnnarKlasi()
        h3 = AnnarKlasi()

        h1.prentaUt("Geir")
        h1.sidustuTveirStafir("Geir")
        h2.sidustuTveirStafir("Guðmundur")
        h3.bilAMilli("Ragnar")
 
    elif(val == '3'): 
        reikningsDaemi1 = ThridjiKlasi(65, 2)
        reikningsDaemi2 = ThridjiKlasi(102, 2)

        print(reikningsDaemi1.samlagning())
        print(reikningsDaemi1.margfoldun())
        print(reikningsDaemi1.deiling())
        greinaskil()
        print(reikningsDaemi2.samlagning())
        print(reikningsDaemi2.margfoldun())
        print(reikningsDaemi2.deiling())
 
    elif(val == '4'): 
        break

    greinaskil()
 
