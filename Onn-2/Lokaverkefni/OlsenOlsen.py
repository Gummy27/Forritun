from random import shuffle

class Spil():
    def __init__(self, takn, tala):
        royal = {
            11:"J",
            12:"D",
            13:"K"
        }
        self.takn = takn
        if tala > 10:
            self.tala = royal[tala]
        else:
            self.tala = tala

    def __str__(self):
        lengd = len(str(self.tala))
        return "| "+self.takn+" "*(2-lengd)+str(self.tala)+" |"

def greinaskil(strengur=""):
    if strengur == "":
        print("="*56)
    else:
        try:
            int(strengur)
            sym = {
                "/":"\\"
            }
            key = "/"
        except:
            sym = {">":"<"}
            key = ">"

        strengur = " "+str(strengur)+" "
        print(key*(28-(int(len(strengur)/2))), end="")
        print(strengur, end="")
        print(sym[key]*(28-int((len(strengur)/2))))

def buaTilBunka():
    takn = ["♥", "♦", "♣", "♠"]
    bunki = []
    for t in takn:
        for nr in range(13):
            spil = Spil(t, nr+1)
            bunki.append(spil)
    shuffle(bunki)
    return bunki

def flippabunka(bunki):
    if len(bunki) == 0:


def gefa(bunki):
    notandi, talva = [], []
    for x in range(5):
        for spilari in [notandi, talva]:
            spilari.append(bunki.pop(0))

    return [notandi, talva]

def skrifaUtStodu(h1, h2, bunki):
    lengd = lambda l, t : int((8*t-len(l))*7/2)
    print(" "*24, "Talva")
    print(" "*lengd(h2, 1), end="")
    for t, spil in enumerate(h2):
        print("|  x  |", end="")
        if (t+1) % 8 == 0:
            print("\n"+" "*lengd(h2, t/8+1), end="")

    print("\n")
    print(" "*24+str(bunki[0]), "\n")

    print(" "*lengd(h1, 1), end="")
    for t, spil in enumerate(h1):
        print(spil, end="")
        if (t+1) % 8 == 0:
            print("\n"+" "*lengd(h1, t/8+1), end="")

    print("\n"," "*22, "Spilari")

def spilanlegSpil(nhendi, spilastokkur1, spilanleg=[]):
    for spil in nhendi:
        if spil.tala == spilastokkur1[0].tala or spil.takn == spilastokkur1[0].tala:
            spilanleg.append(spil)
    return spilanleg

spilastokkur = buaTilBunka() # Spilastokkurinn er búinn til og stokkaður
nhendi, thendi = gefa(spilastokkur) # Notand(nhendi) og Talvan(thendi) fá spil
spilastokkur1 = [] # Spilastokkurinn er búinn til
spilastokkur1.insert(0, spilastokkur.pop(0)) # Fyrsta spilið er hvolft á leikborðið
print("Skipanir: ")
print("Draga = draga | Pass = pass | Olsen = olsen | Olsen Olsen | olsen olsen")
print("Til þess að draga spil þá skrifaru sæti þess sem það er í. D.")
print("| ♥ 1 || ♦ 4 || ♦13 |")
print("Skrifaðu 1 til að fá hjarta ás, 2 til að fá 4 tígull og svo framvegis")
print("Ef að fleirri en 10 spil eru á hendi þá byrjar forritið að prenta spilin niður")
print("Sama regla gildir og talið er frá toppnum")
input("Ýttu á Enter til að byrja leikinn")
print("\n"*4)
greinaskil("1")

turn = 1
while True:
    turn += 1
    skrifaUtStodu(nhendi, thendi, spilastokkur1)
    teljari = 0
    spil = ""
    skilabod = "Hvað viltu gera? : "

    # ============== Notandi ===============
    while True:
        spilanleg = spilanlegSpil(nhendi, spilastokkur1)
        action = input(skilabod)
        if action.lower() == "draga" and teljari != 3:
            if len(spilanleg) > 0:
                nhendi.append(spilastokkur.pop(0))
                skrifaUtStodu(nhendi, thendi, spilastokkur1)
                greinaskil()
                teljari += 1
            else:
                print("Þú mátt ekki draga þegar þú getur gert eitthvað.")

        elif action.lower() == "pass" and teljari == 3:
            print("Pass")
            break

        elif action.lower() == "olsen" and len(nhendi) == 1:
            print("Olsen!")
            break

        elif action.lower() == "olsen olsen" and len(nhendi) == 0:
            print("Olsen Olsen!")
            break

        elif teljari != 3:
            try:
                if int(action)-1 <= len(nhendi):
                    spil = nhendi[int(action) - 1]
                    if spil.takn == spilastokkur1[0].takn or spil.tala == spilastokkur1[0].tala:
                        spilastokkur1.insert(0, nhendi.pop(nhendi.index(spil)))
                        greinaskil()
                        skrifaUtStodu(nhendi, thendi, spilastokkur1)
                        tala = spil.tala
                        skilabod = "Viltu gera eitthvað meira? Skrifaðu pass ef þú vilt enda umferð. : "
                        teljari = 3
                    else:
                        print("Því miður eru þessi spil ekki lík. Dragðu ef að þú getur ekki gert neitt.")
            except:
                print("Fyrirgefðu. Ég veit ekki hvað þú ert að reyna að gera. Til að draga skrifaðu draga")
        else:
            try:
                if int(action)-1 <= len(nhendi):
                    spil = nhendi[int(action) - 1]
                    if spil.tala == tala:
                        spilastokkur1.insert(0, nhendi.pop(nhendi.index(spil)))
                        skrifaUtStodu(nhendi, thendi, spilastokkur1)
                    else:
                        print("Þessi spil hafa ekki eins tölur.")
                else:
                    print("Þetta spil er ekki til að svo stöddu.")
            except:
                print("Ég hef enga hugmynd hvað þú ert að reyna að gera. Skipanirnar eru pass, draga og olsen")


    if len(nhendi) == 1 and action.lower() != "olsen":
        print("Haha! gleymdir að segja olsen. Þú þarft að draga 3 spil.")
        for x in range(3):
            nhendi.append(spilastokkur.pop(0))
    elif action.lower() == "olsen olsen":
        print("Spilari vann leikinn!")
        break

    greinaskil("Talva")
    print()
    teljari = 0

    # ================== Talva ==================
    while teljari < 3:
        card = "None"
        for spil in thendi:
            if spil.takn == spilastokkur1[0].takn:
                spilastokkur1.insert(0, thendi.pop(thendi.index(spil)))
                teljari = 4
                card = spil
                break
            elif spil.tala == spilastokkur1[0].takn:
                spilastokkur1.insert(0, thendi.pop(thendi.index(spil)))
                teljari = 4
                card = spil
                break

        if card == "None":
            thendi.append(spilastokkur.pop(0))
            print("Draga")
            teljari += 1

    if card == "None":
        print("Pass!")
    else:
        print("Ég set út", spil)

    if len(thendi) == 1:
        print("Olsen!")

    elif len(thendi) == 0:
        print("Olsen Olsen!")
        print("Talvan vinnur!")
        break

    print()
    greinaskil(turn)
    if teljari == 3:
        print("Pass")








