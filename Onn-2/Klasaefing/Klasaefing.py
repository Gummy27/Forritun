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
        self.nafn = nafn
        self.gsm = gsm
        self.heimasimi = heimasimi
        self.email = email

    def __str__(self):
        return "Nafn : "+self.nafn+"\n"+"Gemsi : "+self.gsm+"\n"+"Heimasími : "+self.heimasimi+"\n"+"Netfang : "+self.email

    def breytaNafn(self, nafn):
        self.nafn = nafn

    def breytaGsm(self, gsm):
        self.gsm = gsm

    def breytaHeimasimi(self, heimasimi):
        self.heimasimi = heimasimi

    def breytaEmail(self, email):
        self.email = email

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
        return(self.nafn+": "+str(round(self.inneign, 1))+" kr.")

    def reikningarVextir(self):
        self.inneign += self.inneign*self.vextir
        print(str(x+1), "mánuðinn"+" "*(3-len(str(x+1)))+":", round(self.inneign, 1))

    def breytaVoxtum(self, vextir=0.04):
        self.vextir = vextir


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

        for x in range(int(input("Hve marga notendur viltu búa til? : "))):
            nafn = input("Hvað heitir notandinn? : ")
            simanumer = input("Hvað er símanúmerið hans? : ")
            heimasimi = input("Hvað er heimasímanúmerið hans? : ")
            mail = input("Hvað er netfangið hans? : ")
            listiAfMedlimum.append(Medlimir(nafn, simanumer, heimasimi, mail))
            greinaskil()

        while val != 0:
            for teljari, x in enumerate(listiAfMedlimum):
                print(x.nafn+":", teljari+1)
            print("Hætta: 0")
            val = int(input("Hverjum viltu breyta? : "))
            greinaskil()
            val1 = ""
            while val1 != "0" and val != 0:
                print("Nafn: 1")
                print("Gemsi: 2")
                print("Heimasími: 3")
                print("Netfang: 4")
                print("Hætta: 0")
                val1 = input("Hverju viltu breyta? : ")
                greinaskil()

                if val1 == "1":
                    listiAfMedlimum[val-1].breytaNafn(input("Nýja nafnið : "))

                elif val1 == "2":
                    listiAfMedlimum[val-1].breytaGsm(input("Nýji gemsinn : "))

                elif val1 == "3":
                    listiAfMedlimum[val-1].breytaHeimasimi(input("Nýji heimasíminn : "))

                elif val1 == "4":
                    listiAfMedlimum[val-1].breytaEmail(input("Nýja netfangið : "))

                else:
                    break
                greinaskil()

        for x in listiAfMedlimum:
            print(x)
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
        vextir = 0.01
        while vextir != 0:
            print(jon)
            for x in range(12):
                jon.reikningarVextir()
            print(jon)
            greinaskil()

            print(gunna)
            for x in range(12):
                gunna.reikningarVextir()
            print(gunna)
            greinaskil()

            print("Sláðu inn 0 ef að þú vilt hætta.")
            vextir = float(input("Hve háir eiga vextirnir nú að vera? : "))
            jon = Bankareikningur("Jón", 2000)
            gunna = Bankareikningur("Gunna", 3000)
            jon.breytaVoxtum(vextir)
            gunna.breytaVoxtum(vextir)

    elif(val == '5'): 
        break

    greinaskil()
