#Gudmundur Brimir Bjornsson 
#Uppsetning hafinn 2019-03-21
import random
import collections

def greinaskil(): 
    print('==========')

class Setning():
    def __init__(self):
        self.string = ""

    def fall1(self, strengur):
        self.string = strengur

    def fall2(self):
        print(self.string)

class Medlimir():
    def __init__(self, nafn, gsm, heimasimi, email):
        self.n                  afn = nafn
        self.gsm = gsm
        self.heimasimi = heimasimi
        self.email = email

    def breytaNafn(self, nafn):
        self.nafn = nafn

    def breytaGsm(self, gsm):
        self.gsm = gsm

    def breytaHeimasimi(self, heimasimi):
        self.heimasimi = heimasimi

    def breytaEmail(self, email):
        self.email = email

    def prentaUt(self):
        print("Nafn :", self.nafn)
        print("Gemsi : ", self.gsm)
        print("Heimasími", self.heimasimi)
        print("Netfang : ", self.email)

class Nemandi():
    def __init__(self, nafn, aldur, braut):
        self.nafn = nafn
        self.aldur = aldur
        self.braut = braut

    def __str__(self):
        return("Nafn : "+self.nafn+"Aldur : "+str(self.aldur)+"Braut : "+self.braut)

    def elsti(listinem):
        elsti_aldur = 0
        elsti_nafn = "enginn"
        for x in listinem:
            if x.aldur > elsti_aldur:
                elsti_aldur = x.aldur
                elsti_nafn = x.nafn
        print("Sá elsti var", elsti_nafn+". Hann var", elsti_aldur, "ára.")

    def rada(listinem):
        listi = []
        for x in listinem:
            listi.append(x.nafn)
        listi.sort()
        for x in listi:
            print(x)

    def fjoldiBraut(listinem):
        listi = []
        for x in listinem:
            listi.append(x.braut)

        brauta_talning = collections.Counter(listi)
        for brautin, fjoldi in brauta_talning.items():
            print(brautin,":", fjoldi)

class Bankareikningur():
    def __init__(self, nafn, inneign):
        self.vextir = 0.04
        self.nafn = nafn
        self.inneign = inneign

    def __str__(self):
        return(self.nafn+":"+str(self.inneign)+" kr.")

    def reikningarVextir(self):
        self.inneign += self.inneign*self.vextir
        print(str(x+1), "mánuðinn :", self.inneign)

    def breytaVoxtum(self, nyirVextir):
        self.vextir = nyirVextir


verkefni = ['Klasinn Setning', 'Klasinn Medlimir', 'Klasinn Nemandi', 'Klasinn Bankareikningur', 'Hætta'] 
while(True): 
    for x, y in enumerate(verkefni): 
        print(str(x+1)+'.', y) 
    val = input('Hvaða dæmi viltu skoða? : ') 
    greinaskil() 
 
    if(val == '1'): 
        setning = Setning()
        setning.fall1(input("Skrifaðu inn streng í klasann. : "))
        setning.fall2()
 
    elif(val == '2'):
        listiAfMedlimum = []
        listiAfMedlimum.append(Medlimir("Einsr Geir Gabríelsson", 9822832, 2925378, "EinarGG@yahoo.com"))
        listiAfMedlimum.append(Medlimir("Guðmundur Heimir Halldórsson", 2761562, 1236725, "GuðmundurHeimis@outlok.com"))
        listiAfMedlimum.append(Medlimir("Dagný Ragna Kristínssdóttir", 2341782, 2872561, "DaggaRagga@gmail.com"))

        print("Áður en að breytingar eiga sér stað:")
        for x in listiAfMedlimum:
            x.prentaUt()
            greinaskil()

        # Nafnið hans Einars var ekki skrifað rétt
        listiAfMedlimum[0].breytaNafn("Einar Geir Gabríelsson")

        # Email-ið hans Guðmunds var ekki skrifað rétt
        listiAfMedlimum[1].breytaEmail("GuðmundurHeimir@outlook.com")

        # Dagný breytti gemsa símanúmerinu sínu
        listiAfMedlimum[2].breytaGsm(9837234)

        print("Eftir að breytingar eiga sér stað:")
        for x in listiAfMedlimum:
            x.prentaUt()
            greinaskil()


 
    elif(val == '3'):
        nofn = ["Heimir", "Ragnar", "Dagný", "Kristín", "Geir", "Hallgerður", "Halldór", "Krystian", "Gerður", "Björn"]
        brautir = ["Upplýsingatækni", "Hárgreiðsla", "Rafmagnsfræði", "Hagfræði"]
        nemendur = []
        for x in range(10):
            nafn = nofn[x]
            aldur = random.randint(16, 50)
            braut = brautir[random.randint(0, 3)]
            nemendur.append(Nemandi(nafn, aldur, braut))
        Nemandi.elsti(nemendur)
        greinaskil()
        Nemandi.rada(nemendur)
        greinaskil()
        Nemandi.fjoldiBraut(nemendur)
        greinaskil()

    elif(val == '4'): 
        jon = Bankareikningur("Jón", 2000)
        gunna = Bankareikningur("Gunna", 3000)

        print(jon)
        for x in range(12):
            jon.reikningarVextir()
        print(jon)

        greinaskil()
        print(gunna)
        for x in range(12):
            gunna.reikningarVextir()
        print(gunna)

    elif(val == '5'): 
        break

    greinaskil()
