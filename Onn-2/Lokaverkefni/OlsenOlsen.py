from random import shuffle


# Klasinn Spil er búinn til og er notaður til að hýsa eiginleika spila og nokkur föll.
class Spil():
    def __init__(self, takn, tala): # Klasinn tekur inn takn og tölu.
        # Ég bjó til dictionary fyrir konungsfjölskylduna svo hægt sé að nota for loopuna fyrir þau líka.
        royal = {
            11:"J",
            12:"D",
            13:"K"
        }
        self.takn = takn # Tákn spilsins er sett i eiginleikan takn.
        # Gáð er hvort að talan sé hærri 10 svo ekki er reynt að breyta venjulegri tölu í konungsspjald.
        if tala > 10:
            self.tala = royal[tala] # talan er notaður sem lykill til að fá rétta karakterinn.
        else:
            self.tala = tala

    # Hér kemur string fall sem er notað til að prenta út spilið stílað.
    def __str__(self):
        lengd = len(str(self.tala)) # Lengdi spilsins er reiknað út.
        # Síðan er skilað streng sem inniheldur allar þær upplýsingar stílaðar: | ♥ 1 |
        return "| "+self.takn+" "*(2-lengd)+str(self.tala)+" |"

    # Fallið spil8 er aðeins keyrt þegar að spil er nr 8. Það er notað til að breyta tákn spilsins.
    def spil8(self):
        takn = ["♥", "♦", "♣", "♠"] # Tákn listi er búinn til til að auðvelda að assigna nýtt tákn.
        nytt_takn = takn[int(input("1:♥ 2:♦ 3:♣ 4:♠ \nHvað viltu gera? : "))-1] # Nýja táknið er sett í breytu.
        self.takn = nytt_takn # Spilið uppfærir eiginleikann tákn.


# Fallið greinaskil er notað til að gera... greinaskil.
def greinaskil(strengur=""):
    # Gáð er hvort að strengurinn sé sett á default. Ef svo er þá eru greinaskilinn prentuð venjulega.
    if strengur == "":
        print("="*56)
    else:
        # Ég nota try til að gá hvort að strengurinn sé tala.
        try:
            # Þessi partur kóðans er ætlaður að sýna á hvaða umferð þeir eru.
            int(strengur)
            # Hér er táknið sem á að vera notað sem og andstæða þess.
            sym = {
                "/":"\\"
            }
            key = "/"
        except:
            # Þessi partur kóðans er ætlaður að sýna hvort að notandi sé að spila eða talva.
            sym = {">":"<"}
            key = ">"

        strengur = " "+str(strengur)+" " # Bætt er við bilum við byrjun og enda strengsins.
        print(key*(28-(int(len(strengur)/2))), end="") # Fyrri helmingurinn er prentaður.
        print(strengur, end="")                        # Strengurinn sjálfur er prentaður á milli.
        print(sym[key]*(28-int((len(strengur)/2))))    # Seinni helmingurinn er prentaður.


# Fallið leibeiningar prentar allar leiðbeiningarnar fyrir skipanir og hvernig hann virkar í þessu forriti.
def leidbeiningar():
    print("Skipanir: ")
    print("Draga = draga | Pass = pass | Olsen = olsen | Olsen Olsen | olsen olsen")
    print("Til þess að draga spil þá skrifaru sæti þess sem það er í. D.")
    print("| ♥ 1 || ♦ 4 || ♦13 |")
    print("Skrifaðu 1 til að fá hjarta ás, 2 til að fá 4 tígull og svo framvegis")
    print("Ef að fleirri en 10 spil eru á hendi þá byrjar forritið að prenta spilin niður")
    print("Sama regla gildir og talið er frá toppnum")
    input("Ýttu á Enter til að byrja leikinn")
    print("\n" * 4)
    greinaskil("1")


# Fallið buaTilBunka er búið til og verður notað til að búa til bunka.
def buaTilBunka():
    # Tákninn er sett í lista svo hægt er að keyra í gegnum þau með for slaufu.
    takn = ["♥", "♦", "♣", "♠"]
    bunki = []
    # For lykkjan fer í gegnum listann takn.
    for t in takn:
        # For lykkjan keyrir 13 sinnum. Nr verður notað sem tala spilsins.
        for nr in range(13):
            spil = Spil(t, nr+1) # nr er hækkað um einn því for slaufa byrjar á 0.
            bunki.append(spil)   # Spilinu er bætt við bunkann.
    shuffle(bunki)               # Bunkinn er stokkaður.
    return bunki                 # Bunkinn er skilaður.


# Fallið gefa er notað til að gefa tölvuni og notanda spil.
def gefa(bunki):
    notandi, talva = [], []
    # For lykkja er hafinn og mun keyra 1 sinni fyrir hvert spil sem á að vera á hendi(5).
    for x in range(5):
        # Farið er í gegnum listana báða til skiptis eins og er oft gefið í raunveruleikanum.
        for spilari in [notandi, talva]:
            # Listinn sem spilari er á mun fá á sig nýtt spil.
            spilari.append(bunki.pop(0))

    # Báðir listarnir eru skilaðir sem tvöfaldur listi. Hann verður síðan unpackaður á áfangastaðnum.
    return [notandi, talva]


# Fallið skrifaUtStodu er notað til að skrifa út leikborðið.
def skrifaUtStodu(h1, h2, bunki): # Fallið tekur inn h1(hönd 1), h2(hönd 2) og bunki(spilastokkur).
    # Hér nota ég lambda til að reikna út bilið sem á að vera prentað út. Ástæða fyrir því að ég nota lambda í staðinn
    # fyrir fall er því það er alveg eins bara fallegra.
    lengd = lambda l, t : int((8*t-len(l))*7/2)
    print(" "*24, "Talva")                              # Hér er prentað út hver er að gera.
    print(" "*lengd(h2, 1), end="")                     # Bilið sem miðjar úttakið út er prentað út
    for t, spil in enumerate(h2):                       # Spilinn eru prentuð út með for lykkju.
        print("|  x  |", end="")                        # Af því að þetta er talvan þá má notandi ekki sjá spilinn hans.
        if (t+1) % 8 == 0:                              # Gáð er hvort að spilinn eru búinn að fylla línuna.
            print("\n"+" "*lengd(h2, t/8+1), end="")    # Annað bil er prentað út með lambda fallið sem viðmið.

    # Hérna er toppspilið prentað út.
    print("\n")
    print(" "*24+str(bunki[0]), "\n")

    print(" "*lengd(h1, 1), end="")
    for t, spil in enumerate(h1):                       # Bilið sem miðjar úttakið út er prentað út
        print(spil, end="")                             # Spilið er prentað út með string fallinu.
        if (t+1) % 8 == 0:                              # Gáð er hvort að spilinn eru búinn að fylla línuna.
            print("\n"+" "*lengd(h1, t/8+1), end="")    # Annað bil er prentað út með lambda fallið sem viðmið.
    print("\n"," "*22, "Spilari")                       # Hér er prentað út hver er að gera.


# Fallið spilanlegSpil er notað til að leita að spilum spilanlegum spilum
def spilanlegSpil(h, bunki): # Fallið tekur inn n(hönd) spilastokkur1(bunkinn á borðinu).
    spilanleg = 0
    for spil in h: # Farið er í gegnum öll spilinn í hendi notandans.
        if spil.tala == bunki[0].tala or spil.takn == bunki[0].takn: # Gáð er hvort að þetta spil sé spilanlegt.
            spilanleg += 1 # Breytan spilanleg er hækkuð um einn
    return spilanleg # Breytan skilanleg er skiluð.


spilastokkur = buaTilBunka()                    # Spilastokkurinn er búinn til og stokkaður
nhendi, thendi = gefa(spilastokkur)             # Notand(nhendi) og Talvan(thendi) fá spil
spilastokkur1 = []                              # Spilastokkurinn er búinn til
spilastokkur1.insert(0, spilastokkur.pop(0))    # Fyrsta spilið er hvolft á leikborðið
leidbeiningar()                                 # Leiðbeiningarnar eru prentaðar út.

# Turn breytan verður notuð til að sýna hve margar umferðir hafa liðið frá byrjun.
turn = 1
while True:
    turn += 1
    skrifaUtStodu(nhendi, thendi, spilastokkur1)   # Skrifað er út leikborðið.
    teljari = 0 # Teljarinn er núllstilltur.
    spil = ""   # breytan spil er núllstillt.

    # ============== Notandi ===============
    # Þessi while slaufa mun ganga þar til að teljari er 4. Það annaðhvort þýðir að notandi hafi dregið 3 sinnum eða
    # að hann hafi gert.
    while teljari != 4:
        # Breytan spilanleg mun taka á sig hve mörg spilanleg spil eru tiltæk.
        spilanleg = spilanlegSpil(nhendi, spilastokkur1)
        action = input("Hvað viltu gera? : ") # action breytan tekur inn hvað notandi vilji gera.

        # Gáð er hvort að notandi hafi viljað draga.
        if action.lower() == "draga":
            # Gáð er hvort að það séu enginn spilanleg spil á hendi notanda og að teljari sé minna en 4.
            if spilanleg == 0 and teljari < 4:
                nhendi.append(spilastokkur.pop(0))            # Notandi dregur spil úr bunka
                skrifaUtStodu(nhendi, thendi, spilastokkur1)  # Leikborðið er skrifað út.
                greinaskil()                                  # Venjuleg greinaskil eru prentuð út.
                teljari += 1                                  # Teljarinn er hækkaður um einn.

                if len(spilastokkur) == 0: # Gáð er hvort að spilastokkurinn sé tómur.
                    # breytan spilastokkur tekur á sig stokkaðan spilastokk1 án fyrsta spilsins
                    spilastokkur = shuffle(spilastokkur1[1:])
                    spilastokkur1 = [spilastokkur1[0]] # Spilastokkur1 er minnkaður í aðeins 1 spilið.

            elif spilanleg == 0 and teljari == 4: # Gáð er hvort að notandi hafi enginn spilanleg spil og hafi dregið 3 sinnum.
                print("Þú getur ekki dregið í fjórða sinn.")

            else:
                print("Þú mátt ekki draga þegar þú getur gert eitthvað.")

        else:
            try: # Gert er til try skipun svo ef hún mistekst þá veit forritið að það sé út af því að notandi hafi gert eitthvað vitlaust.
                if int(action)-1 <= len(nhendi): # Gáð er hvort að notandi hafi skrifað inn spil sem er í hendi notanda.
                    spil = nhendi[int(action) - 1] # Breytan spil er búinn til til að hýsa spilið sem notandi vill spila.

                    # Gáð er hvort að spilið sé átta.
                    if spil.tala == 8:
                        spil.spil8()                                             # Fallið spil 8 er ræst.
                        spilastokkur1.insert(0, nhendi.pop(nhendi.index(spil)))  # Spilastokkurinn er uppfærður
                        skrifaUtStodu(nhendi, thendi, spilastokkur1)             # Leikborðið er prentað út.
                        teljari = 4

                    # Gáð er hvort hægt sé að spila spilið sem notandi vill setja út.
                    elif spil.takn == spilastokkur1[0].takn or spil.tala == spilastokkur1[0].tala:
                        spilastokkur1.insert(0, nhendi.pop(nhendi.index(spil)))  # Spilastokkurinn er uppfærður.
                        greinaskil()                                             # Greinaskil eru prentuð út.
                        skrifaUtStodu(nhendi, thendi, spilastokkur1)             # Leikborðið er prentað út.
                        tala = spil.tala                                         # Tala spilsins er geymt.
                        teljari = 4
                    else:
                        print("Því miður eru þessi spil ekki lík. Dragðu ef að þú getur ekki gert neitt.")
            except:
                print("Fyrirgefðu. Ég veit ekki hvað þú ert að reyna að gera. Til að draga skrifaðu draga")


    # Þessi while lykkja mun ganga þar til hann er breakaður.
    while True:
        action = input("Viltu gera eitthvað meira? Skrifaðu pass ef þú vilt enda umferð. : ")

        # Gáð er hvort að notandi hafi skrifað inn pass. Ef svo er þá er while lykkjan brotinn.
        if action.lower() == "pass":
            break

        # Gáð er hvort að notandi hafi skrifað inn olsen og að hann hafi aðeins eitt spil á hendi.
        elif action.lower() == "olsen" and len(nhendi) == 1:
            break

        # Gáð er hvort að notandi hafi skrifað inn olsen olsen og að hafnn hafi enginn spil á hendi.
        elif action.lower() == "olsen olsen" and len(nhendi) == 0:
            break

        else:
            try:
                # Gáð er hvort að tala spilsins sem notandi vill spila sé sú sama og síðasta spilið.
                if nhendi[int(action)-1].tala == tala:
                    spil = nhendi[int(action) - 1] # Spilið sem notandi vill spila er geymt í breytu.
                    spilastokkur1.insert(0, nhendi.pop(nhendi.index(spil))) # Spilastokkurinn er uppfærður.
                    greinaskil() # Greinaskil eru prentuð út.
                    skrifaUtStodu(nhendi, thendi, spilastokkur1) # Leikborðið er prentað út.

                else:
                    print("Þessi tvö spil hafa ekki eins tölur.")
            except:
                print("Fyrirgefðu. Ég veit ekki hvað þú ert að reyna að gera. Til að enda umferð skrifaðu pass")

    # Hér er gáð hvort að notandi hafi gleymt að skrifa olsen
    if len(nhendi) == 1 and action.lower() != "olsen":
        print("Haha! gleymdir að segja olsen. Þú þarft að draga 3 spil.")
        for x in range(3):
            nhendi.append(spilastokkur.pop(0))

    # Hér er gáð hvort að notandi hafi gleymt að skrifa olsen olsen.
    elif len(nhendi) == 0 and action.lower() != "olsen olsen":
        print("Haha! gleymdir að segja olsen olsen. Þú þarft að draga 3 spil.")
        for x in range(3):
            nhendi.append(spilastokkur.pop(0))

    # Hér er gáð hvort að notandi hafi munað eftir því að skrifa olsen olsen.
    elif action.lower() == "olsen olsen" and nhendi == 0:
        print("Spilari vann leikinn!")
        break

    greinaskil("Talva")
    print()
    teljari = 0

    # ================== Talva ==================
    # While lykkja er hafinn og mun keyra þangað til að teljarinn er orðinn 3 sem annaðhvort þýðir að talvan hafi gert
    # eða að hann hafi dregið 3 sinnum.
    while teljari < 3:
        # Þessi card breyta er notuð til að gá hvort að talva hafi gert.
        card = "None"
        for spil in thendi: # Farið er í gegnum hendina hjá tölvunni.
            # Gáð er hvort að spilið sé spilanlegt.
            if spil.takn == spilastokkur1[0].takn or spil.tala == spilastokkur1[0].takn:
                spilastokkur1.insert(0, thendi.pop(thendi.index(spil))) # Spilið er sett á bunkann
                teljari = 4
                card = spil # Card breytan fær á sig spilið svo hægt sé að láta vita að talva hafi gert.
                break

        # Gáð er hvort að talva hafi gert svo hægt sé að draga ef hann hefur ekki getað gert neitt.
        if card == "None":
            thendi.append(spilastokkur.pop(0)) # Talvan fær eitt annað spil.
            if len(spilastokkur) == 0: # Gáð er hvort að spilastokkurinn sé tómur.
                spilastokkur = shuffle(spilastokkur1[1:])
                spilastokkur1 = [spilastokkur1[0]]
            print("Draga")
            teljari += 1

    # Gáð er hvort að notandi hafi ekki gert svo hægt sé að segja pass.
    if card == "None":
        print("Pass!")
    else:
        print("Ég set út", spil)

    # Gáð er hvort að talvan hafi 1 spil svo hún geti sagt olsen
    if len(thendi) == 1:
        print("Olsen!")

    # Gáð er hvort að talvan hafi unnið.
    elif len(thendi) == 0:
        print("Olsen Olsen!")
        print("Talvan vinnur!")
        break

    print()
    greinaskil(turn)
    if teljari == 3:
        print("Pass")






