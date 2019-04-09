# Guðmundur Brimir Björnsson
# Uppsetning hafinn 4. apríl, 2019
import random
import time
import itertools

'''
Þú getur valið um hve margar sekúndur er stoppað á milli atburða. Þetta á að bæta hve raunverulegur eikurinn er.
Ef þú vilt þetta ekki þá skrifaru bara núll fyrir ekkert delay. Ég mæli persónulega með 2 sekúndum.
'''

timi = int(input("Hve margar sekúndur á talvan að stoppa? : "))
print("\n")

def greinaskil():
    print("==========")

# Klasinn Hermenn mun vera notaður til að búa til hermenn.
class Hermenn: # Klasinn tekur inn nafn, líf, vopn og styrk.
    # Smiður er skilgreindur og mun búa til eiginleikana nafn(nafn), hp(líf), wp(vopn) og st(styrkur)
    def __init__(self, nafn, lif, vopn, styrkur):
        self.nafn = nafn
        self.hp = lif
        self.wp = vopn
        self.st = styrkur

    # Þessi klasi er aðeins fyrir að debugga til að gá hvort að hermennirnir eru rétt settir upp.
    def __str__(self):
        return "Nafn : "+str(self.nafn)+" Líf : "+str(self.hp)+" Vopn : "+str(self.wp)+" Styrkur : "+str(self.st)

# Klasinn mun vera notaður til að geyma herdeildirnar og hermennina sem eiga að berjast.
class Leikurinn(): # Klasinn tekur inn herdeildirnar lid1 og lid2 og líka hermennina hermadur1 og hermadur2
    # Smiðurinn býr til eiginleikana l1(lid1), l2(lid2), h1(hermadur1), h2(hermadur2) og turn(0)
    def __init__(self, lid1, lid2, hermadur1, hermadur2):
        self.l1 = lid1 # Eiginleikinn l1 heldur utan um einn af herdeildunum sem munu keppa.
        self.l2 = lid2 # Eiginleikinn l2 heldur utan um einn af herdeildunum sem munu keppa.
        self.h1 = hermadur1 # Eiginleikinn h1 heldur utan um eitt af þeim hermönnum sem á að berjast.
        self.h2 = hermadur2 # Eiginleikinn h2 heldur utan um eitt af þeim hermönnum sem á að berjast.
        self.turn = 1 # Eiginleikinn turn mun halda utan um hve mörg turn forritið hefur spilað.

    # Fallið lidskipan prentar út alla sem eru ennþá lifandi frá báðu liðunum.
    def lidskipan(self): # Fallið tekur aðeins inn eiginleika klasans.
        # Ég skrifa sumar breytur svona því ég nenni ekki að taka frá 2 línur fyrir eitthvað sem tæki aðeins 1.
        l1, l2 = self.l1, self.l2 # l1 fær á sig self.l1 og l2 fær á sig self.l2

        # Haus prentaðgerarinnar er prentað út.
        print("---------------------------------------------------")
        print("           lið 1         |        lið 2")
        print("---------------------------------------------------")


        # zip_longest unpackar bæði breyturnar í einu alveg eins og zip. Eini munurinn er að hann heldur
        # áfram þó að fallið sé búið að fara yfir allar breytur í listanum
        for x, y in itertools.zip_longest(l1, l2): # For slaufa er hafinnn og mun fara í gegnum bæði herdeild 1 og líka herdeild 2 með zip_longest fallinu.
            # Try skilyrði er skilgreint svo að forritið lendi ekki í villu þegar hann reynir að fá .nafn frá lista sem er búinn.
            try:
                # Strengirnir eru búnir til frá nafni og hp hlutsins.
                strengur1 = x.nafn+" "*(25-len(x.nafn)-4)+str(x.hp)+"hp" # Dæmi: Jón Bubbi      10hp
                strengur2 = y.nafn+" "*(25-len(y.nafn)-4)+str(y.hp)+"hp" # Dæmi: Jón Bubbi      10hp
                #Strengurinn er síðan prentaður með | á milli til að skilja nöfnin að.
                print(strengur1+" | "+strengur2)
            # Except skilyrði er skilgreint og er notað þegar eitt af listunum er kláraður.
            except:
                # Hér er gáð hvor listinn er búinn með einfaldri if setningu sem spyr hvort að l1 sé með fleirri hluti en l2.
                if len(l1) > len(l2):
                    # Prentað er út streng1 ásamt annari hlið sem inniheldur ekki neitt.
                    print(strengur1+" "*(25-len(strengur1))+"| ") # Dæmi: Einar  10hp | _______
                else:
                    # Prentað er út streng2 þar sem fyrsta hliðin er alveg tóm
                    strengur2 = y.nafn+" "*(25-len(y.nafn)-4)+str(y.hp)+"hp"
                    print(" "*25+"| "+strengur2+" "*(18-len(strengur2))) # Dæmi: _______ | Einar  10hp
        print("---------------------------------------------------")


    # Fallið bardagi setur upp if setingar sem ræður hver vinnur í bardaganum á milli.
    def bardagi(self): # Fallið tekur aðeins inn eiginleika klasans
        # h1 og h2 taka hvor um sig eiginleikana self.h1 og self.h2 á sig.
        h1, h2 = self.h1, self.h2

        # Gáð er hvort að styrkur hermanns 2 er meiri en hjá hermanni 1
        if h1.st < h2.st:
            print(f"{h1.nafn} tapaði með {h1.st} styrk á móti {h2.nafn} með {h2.st}") # Prentar út styrk h1 á móti styrk h2
            print(f"{h1.nafn} missti {h2.st} líf á hendi {h2.nafn}") # Prentar út hve mörg líf hermaður 1 tapaði
            h1.hp -= h2.st # Hermaður 1 missir h2.st líf
        # Gáð er hvort að styrkur hermanns 1 er meiri en hjá hermanni 2
        elif h1.st > h2.st:
            print(f"{h2.nafn} tapaði með {h2.st} styrk á móti {h1.nafn} með {h1.st}") # Prentar út styrk h2 á móti styrk h2
            print(f"{h2.nafn} missti {h1.st} líf á hendi {h1.nafn}") # Prentar út hve mörg líf hermapur 2 tapaði
            h2.hp -= h1.st # Hermaður 2 missir h1.st líf
        # Annars þegar hermennirnir er jafn sterkir.
        else:
            # Ég setti upp svona skæri, blað, steinn reglu upp þegar kemur að vopnunum til að ráða úr jafntefli.
            wpDict = {
                "Sverð":"Spjót", # Sverð tapar á móti spjóti
                "Spjót":"Exi",   # Spjót tapar á móti exi
                "Exi":"Sverð"    # Exi tapar á móti sverði
            }
            # Prentað er út skilaboð sem segir notanda að hermennirnir eru jafn sterkir.
            print(f"{h1.nafn} og {h2.nafn} eru jafn sterkir.")

            # Gáð er hvort að hermaður h2 sé með það vopn sem er sterkt á móti vopni h1
            if wpDict[h1.wp] == h2.wp: # Hermaður 1 tapar
                h1.hp -= h2.st # Hermaður 1 missti h2.st líf
                # Prentað er út skilaboð sem segir notanda að vopnið hjá hermanni 1 tapaði á móti vopni hermanns 2
                print(f"{h1.wp} er veikt á móti {h2.wp} svo {h2.nafn} vinnur.")
                # Prentað er út hve mörg líf hermaður 1 missti
                print(f"{h1.nafn} missti {h2.st} líf á hendi {h2.nafn}")

            # Gáð er hvort að hermaður h1 sé með það vopn sem er sterkt á móti vopni h2
            elif wpDict[h2.wp] == h1.wp: # Hermaður 2 tapar.
                h2.hp -= h2.st
                # Prentað er út skilaboð sem segir notanda að vopnið hjá hermanni 2 tapaði á móti vopni hermanns 1
                print(f"{h2.wp} er veikt á móti {h1.wp} svo {h1.nafn} vinnur.")
                # Prentað er út hve mörg líf hermaður 2 missti.
                print(f"{h2.nafn} missti {h1.st} líf á hendi {h1.nafn}")

            # Ef báðir hermenn eru alveg eins á báða vegu þá missa þeir báðir jafn mörg líf.
            else: # Báðir eru jafnir.
                print(f"Þeir sköðuðu hvorn annan fyrir {h2.st} skaða")
                h1.hp -= h2.st
                h2.hp -= h1.st
        self.turn += 1 # Turn er hækkað um 1 til að sýna hve margar umferðir hafa liðið.

    # Fallið killed gáir hvort að eitthver af hermönnunum hafa dáið í bardaga.
    def killed(self): # Fallið tekur aðeins inn eiginleika klasans.
        # Breyturnar h1 og h2 taka hvor um sig eiginleikana self.h1 og self.h2
        h1, h2 = self.h1, self.h2

        # Gáð er hvort að hermaður 1 sé með fleiri líf en 0.
        if h1.hp > 0:
            lidA.append(h1) # Ef svo er þá er hermaðurinn bættur aftur við listann.
        else:
            print(f"{h1.nafn} er dáinn") # Annars er hann lýstur látinn

        if h2.hp > 0:
            lidB.append(h2)
        else:
            print(f"{h2.nafn} er dáinn")

    # Fallið bardagaUmferd skilar hve mikið af umferðum hafa liðið síðan byrjun leiks.
    def bardagaUmferd(self): # Fallið tekur aðeins inn eiginleika klasans.
        strengur = "Umferð "+str(self.turn) # Strengur tekur á sig orðið umferð plús hve margar umferðir hafa liðið.
        strengur = "="*(25-(len(strengur)//2))+strengur # Síðan er bætt við "=" sem situr orðið út í miðju.
        strengur = strengur + "="*(51-len(strengur)) # Síðan er bætt við "=" eftir orðinu til að loka því fallega.
        return strengur # Strengnum er skilað.

lid = [[], []] # Listinn lid er skilgreindur sem tvöfaldur listi svo hægt sé að halda utan um bæði liðinn í for slaufuni.
tiltaekVopn = ["Sverð", "Spjót", "Exi"] # Þau vopn sem eru leyfð í bardaganum eru skilgreind.
ListiAfNofnum = [
    "Bob",
    "Rambo",
    "Riddley",
    "Schwarzenegger",
    "John Wick",
    "Billy Bob",
    "Brad Pitt",
    "Sylvester Stallone",
    "Private Ryan",
    "Egill Skallagrímsson",
    "Bill"] # Listi af nöfnum sem að hermennirnir eru skírðir.

random.shuffle(ListiAfNofnum) # Listinn af nöfnunum er shufflaður svo allir hermenn er einstakir á milli hvers leiks.

teljari = 0 # Teljari er skilgreindur sem mun fara frá 0 til 9 og þannig velja nöfn í shufflaða listanum.
for x in range(2): # For slaufa er hafinn sem mun aðeins keyra 2 sinnum. 1 sinni fyrir hvern lista inn í lid.
    for i in range(5): # For slaufa er hafinn sem mun keyra 5 sinnum. 1 sinni fyrir hvern hermann sem á að vera í listanum.
        teljari += 1 # Teljari er hækkaður um einn.
        nafn = ListiAfNofnum[teljari] # Nafn hermannsins er tekinn úr shufflaða listanum.
        lif = random.randint(5, 9) # Líf hermanns er randomly ákveðið á milli 5 og 9. Ástæða þessara talna er svo að hermenn myndu lifa oftar af eftir einn bardaga
        vopn = tiltaekVopn[random.randint(0, 2)] # Vopn hermanns er randomly ákveðið,
        styrkur = random.randint(3, 5) # Styrkur hermanns er randomly ákveðið á milli 3 og 5
        hermadur = Hermenn(nafn, lif, vopn, styrkur) # tilvikið hermadur er skilgreindur sem tilvik af klasanum Hermenn
        lid[x].append(hermadur) # Hermaður er bættur við í lið.

lidA, lidB = lid[0], lid[1] # LiðA tekur á sig fyrsta listann í listanum lid og lidB tekur á sig seinni listann í listanum lid.

# Tilvik klasans Leikurinn er skilgreindur með lidA og lidB og síðan tóma strengi því við erum ekki búnir að ákveða hverjir munu berjast.
umferd = Leikurinn(lidA, lidB, "", "")
umferd.lidskipan() # Liðinn eru prentuð út.

# While slaufa er hafinn og mun keyra þangað til að annaðhvor liðinn eru tóm.
while len(lidA) != 0 and len(lidB) != 0:
    print("\n"+umferd.bardagaUmferd()) # Prentað er út á hvaða umferð þú ert á.

    # Hermenn eru valdir af handahófi úr liðunum og teknir úr þeim(poppaðir).
    soldier1 = lidA.pop(random.randint(0, len(lidA)-1))
    soldier2 = lidB.pop(random.randint(0, len(lidB)-1))

    # Klasaeiginleikarnir h1 og h2 eru breyttir í soldier 1 og soldier 2.
    umferd.h1, umferd.h2 = soldier1, soldier2

    # Gáð er hvort að tími sé hærri en 0.
    if timi > 0:
        # Þessi skilaboð eru prentuð til að líkja eftir tölvuleik.
        print("Bardagi er hafinn")

    time.sleep(timi)        # Forritið hvílir sig í þann tíma sem notandi valdi.
    umferd.bardagi()        # Kallað er á fallið bardagi til að byrja bardagann á milli hermannanna.
    time.sleep(timi)        # Forritið hvílir sig í þann tíma sem notandi valdi.
    umferd.killed()         # Kallað er á fallið killed til að gá hvort ð eitthvað af hermönnunum voru drepnir.
    umferd.lidskipan()      # Prentað er út þá sem lifðu af.

# Gáð er hvor vinni með því að sjá hvaða listi er stærstur.
if len(lidA) > len(lidB):
    print("Lið 1 vinnur!")

elif len(lidA) < len(lidB):
    print("Lið 2 vinnur!")

else:
    print("Eins og alltaf þá vinnur enginn í stríði.")






