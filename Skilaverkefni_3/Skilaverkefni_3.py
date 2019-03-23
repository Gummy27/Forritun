#Guðmundur Brimir Björnsson
#Uppsetning hafinn 21. febrúar 2019
import random

# Þetta fall gerir greinaskil á milli dæma.
def greinaskil():
    print("==========")

# Þetta fall prentar út lista á fallegan hátt.
def listaPrentari(listi):
    for x in listi:
        print(x)

# Þetta fall mun prenta út tuple á fallegan hátt.
def prentaTuple(tupl1, tupl2):  # Fallið tekur inn 2 tuple lista og skýrir þá tupl1 og tupl2
    for x in tupl1:  # Fyrst er farið í gegnum tupl1. Þar mun x taka á sig gildi í tuple1
        print(x, end=" ")  # Prentað er út x en ekki með newline heldur bara autt bil þar sem næsta x kemur.
    print() # Prentað er ekkert út svo að næsta for slaufa prenti ekki í sömu línu og hin.
    for x in tupl2: # Farið er í gegnum tupl2 þar sem x tekur á sig gildi úr tupl2
        print(x, end=" ") # X er prentað út með ekkert endline.
    print() # Hér er ekkert prentað út svo að ný lína verðu búin til.

# Þetta fall parar saman tvo einstaklinga úr báðum listunum.
def paraRod(tupl1, tupl2): #Fallið tekur inn tvo tuple lista sem munu heita tupl1 og tupl2
    for x in range(len(tupl1)): #Þessi slaufa mun loopa jafn mörgum sinnum og það eru hlutir í tupl1.
        print(tupl1[x], "og", tupl2[x]) #Hér eru sérstök stök úr listunum prentuð út og þau pöruð saman: Einar og Jósefína

# Þetta fall velur einstaklinga af handahófi og parar þeim saman.
def paraRandom(tupl1, tupl2): #Fallið tekur inn tvo tuple lista sem munu heita tupl1 og tupl2
    for x in range(len(tupl1)): #Þessi slaufa mun loopa jafn mörgum sinnum og það eru hlutir í tupl1.
        y = random.randint(0, 4) #y fær á sig handahófskennda tölu sem mun vera notuð til að velja einhvern úr hópnum.
        i = random.randint(0, 4) #i fær á sig handahófskennda tölu sem mun vera notuð til að velja einhvern úr hópnum.
        print(tupl1[i], "og", tupl2[y]) #Hér eru sérstök stök úr listunum prentuð út og þau pöruð saman: Einar og Jósefína

# Þetta fall velur einstakling af handahófi og parar þeim saman. Hérna þá getur aðeins einn einstaklingur verið paraður í einu.
def paraRandomStakur(tupl1, tupl2): #Fallið tekur inn tvo tuple lista sem munu heita tupl1 og tupl2
    #Tuple listarnir eru breyttir í venjulega lista og síðan settir í tupl_random svo hægt sé að breyta röðinni í þeim.
    tupl1_random = list(tupl1) #List er notað til að breyta tuple í lista.
    tupl2_random = list(tupl2)
    #Listarnir eru síðan shufflaðir með .shuffle fallið sem breytir röðinni þeirra í einhverja handahófskennda röð.
    random.shuffle(tupl1_random)
    random.shuffle(tupl2_random)
    for x in range(len(tupl1)): #Þessi slaufa mun loopa jafn mörgum sinnum og það eru hlutir í tupl1.
        print(tupl1_random[x], "og", tupl2_random[x]) #Hér eru sérstök stök úr listunum prentuð út og þau pöruð saman: Einar og Jósefína

# Þetta fall reynir að finna nafn eftir aðeins einum staf.
def finnaNafn(stafur, tupl1, tupl2): #Fallið tekur inn tvo tuple lista sem munu heita tupl1 og tupl2
    listi = []
    # Þessar for slaufur munu fara í gegnum báða tuple listana og taka á sig gildi úr þeim.
    for x in tupl1:
        # Í þessari for slaufu fer i í gegnum alla stafina í x til að gá hvort að stafurinn sé í orðinu.
        for i in x:
            # Gáð er hvort að i sé sá stafur sem leitað er að.
            if(i.lower() == stafur.lower()): # Stafirnir eru settir í lágstafi svo að hann finni stafinn þó að hann sé í hástöfum.
                listi.append(x)
                break #Ekki er þörf á að leita meira því við fundum stafinn í orðinu svo for slaufan er brotinn. 
    for x in tupl2:
        for i in x:
            if(i.lower() == stafur.lower()):
                listi.append(x)
                break
    return(listi)

# Gáð er hvort að orð hefur fleiri en eitt n
def morgN(tupl1, tupl2): #Fallið tekur inn tvo tuple lista sem munu heita tupl1 og tupl2
    listi = []
    # Þessi for slaufa mun fara í gegnum listann tupl1.
    for x in tupl1: 
        # Flag er bráðabirgðarbreyta sem verður notuð til að sýna fram á það að fleiri en 1 n sé orðinu.
        flag = 0
        #for slaufa fer gegnum x til að skoða alla stafina í orðinu í leit að n.
        for i in x:
            if(i.lower() == 'n'): #Gáð er hvort að i í lágstöfum sé n
                flag += 1 #Flag er plúsað við einn.
                continue #Continue er notað til að fara í gegnum hina if setninguna.
            elif(flag == 2): #Gáð er hvort að flag sé 2 sem bendir til þess að orðið hafi meiri eða nákvæmlega 2 n.
                listi.append(x)
                break
    for x in tupl2:
        flag = 0
        for i in x:
            if(i.lower() == 'n'):
                flag += 1
                continue
            elif(flag == 2):
                listi.append(x)
                break
    return(listi)

# Þetta fall reynir að finna það nafn sem er með fyrsta staf sem er það sama og notandi skrifaði inn.
def finnaFyrstaStaf(tupl1, tupl2): #Fallið tekur inn tvo tuple lista sem munu heita tupl1 og tupl2
    # Notadni skrifar inn þann staf sem á að leita að.
    stafur = input("Skrifaðu inn staf sem tilheyrir fyrsta staf nafns. : ")
    # Farið er í gegnum tuple listann tupl1. X mun taka gildi úr honum.
    for x in tupl1:
        # Gáð er hvort að fyrsti stafur orðsins sem x er með sé sá stafur sem notandi er að leita að.
        if(x[0].lower() == stafur.lower()):
            # Ef stafurinn reynist vera stafurinn sem notandi er að leita að þá er orðið prentað út.
            print(x)
    # Hérna gildir það nákvæmlega sama og í fyrstu for lykkjuni.
    for x in tupl2:
        if(x[0].lower() == stafur.lower()):
            print(x)

# Þetta fall leitar að færslu í dictionary með nafni og prentar út símanúmerið ef hann er sá sem notandi er að leita að.
def finnaSimanumer(nafn, simskra): # Þetta fall tekur inn inntak frá notanda og kallar það nafn. Einnig tekur hann inn dictionary sem hann nefnir símaskrá.
    flag = 0
    for key, value in simaskra.items(): # Símaskrá dictionary er itemað svo bæði lykillinn og gildið er tekið inn og sett inn í breyturnar key og value.
        if(key.lower() == nafn.lower()): # Gáð er hvort að lykillinn(nafnið á tengilið) sé það sama og notandi er að leita að.
            # Ef if setningin er sönn þá er símanúmerið prentað út og for slaufan brotinn.
            print("Símanúmerið hans", key, "er", value)
            flag = 1 # Flag er sett í 1 sem þýðir að talvan hafi fundið nafn og því þarf ekki að prenta út villu skilaboðinn niðri.
            break
    # Villuskilaboð: Gáir hvort að flag sé ennþá 0.
    if(flag == 0):
        # Ef svo er þá er villuskilaboðið prentað út.
        print("Þetta nafn er ekki til í skránni.")

# Þetta fall prentar út dictionary á fallegan hátt.
def prentaDict(dict): # Fallið tekur inn dictionary lista og geymir hann í breytu sem nefnist dict.
    # For slaufa fer í gegnum dict sem er itemað svo hægt sé að geyma gildið og lykilinn í samnefndum breytum
    for key, value in dict.items():
        # Reikningsdæmin sem koma á milli breytana er notað til að gera nægt bil á milli orða.
        # t.d. ef að orð er 4 stafa langt þá mínusar forritið lengdina með 10 og skrifar út það mörg bil til að láta
        # þetta líta jafnt út.
        print(key, "-"*(10-len(key))+">", " "*(2-len(str(value))) + str(value), "ára")

# Þetta fall fer í gegnum dictionary og leitar að einstaklingum sem eru 18 ára eða eldri.
def yfir18(dict): # Fallið tekur inn dictionary og skýrir það dict.
    teljari = 0 # Breytan teljari mun vera notaður til að telja hve oft einhver 18 ára eða eldri kom fram.
    # For slaufa fer í gegnum dict sem er itemað svo hægt sé að geyma gildið og lykilinn í samnefndum breytum
    for key, value in dict.items():
        if(value <= 18): # Gáð er hvort að value(aldur) sé hærri eða jafngildir 18.
            # Ef svo er þá fer teljarinn upp um einn og prentar út nafn einstaklingsins sem er 18 ára eða eldri.
            teljari += 1
            print(key)
    print("Þarna voru", teljari, "sem voru 18 ára eða eldri") # Og á endanum er skrifað út hversu margir voru 18 ára eða eldri.

# Þetta fall finnur meðaltal allra sem eru í dictionary.
def medalaldur(dict): # Fallið tekur inn dictionary og geymir það í breytuni dict.
    samanlagt = 0 # Samanlagt breytan er skilgreind með 0 og mun vera notuð til að geyma heildaraldur einstaklinganna.
    # For slaufa fer í gegnum dict sem er itemað svo hægt sé að geyma gildið og lykilinn í samnefndum breytum
    for key, value in dict.items():
        samanlagt += value # Samanlagt breytan plúsar sjálfa sig við gildið.
    print("Meðalaldur bekkjarins er", round((samanlagt/15), 2)) # Meðalaldurinn er reiknaður og skrifaður út.

# Þetta fall finnu heildaraldur allra einstaklinga i dictionary.
def heildaraldur(dict): # Fallið tekur inn dictionary og geymir það í breytuni dict.
    samanlagt = 0 # Samanlagt breytan er skilgreind með 0 og mun vera notuð til að geyma heildaraldur einstaklinganna.
    # For slaufa fer í gegnum dict sem er itemað svo hægt sé að geyma gildið og lykilinn í samnefndum breytum
    for key, value in dict.items():
        samanlagt += value # Samanlagt breytan plúsar sjálfa sig við gildið(aldur).
    print("Samanlagður aldur bekkjarins er", samanlagt) # Heildaraldur allra einstaklinganna er prentað út.

# Þetta fall leitar að einstakling með fyrsta staf hans.
def finnaStafDict(dict): # Fallið tekur inn dictionary og geymir það í breytuni dict.
    listi = [] # Listi er skilgreindur sem verður notaðut til að halda utan um undir lista af aldri.
    stafur = input("Skrifaðu inn staf. : ") # Spurt er um staf sem á að leita að.
    # For slaufa fer í gegnum dict sem er itemað svo hægt sé að geyma gildið og lykilinn í samnefndum breytum
    for key, value in dict.items():
        if(stafur.lower() == key[0].lower()): # Gáð er hvort að fyrsti stafur nafns sé sá sami og notandi eru að leita að.
            # Nafnið og aldur einstaklings er prentað út.
            print(key, "-" * (10 - len(key)) + ">", " " * (2 - len(str(value))) + str(value), "ára")
            listi.append(key) # Listinn fær á sig annan lykil.
    return(listi) # Listanum er skilað.

# Þetta fall finnu meðalaldur nokkura einstaklinga.
def medalaldurDict_2(listi, dict): # Fallið tekur inn bæði dictionary og lista.
    samanlagt = 0 # Samanlagt breytan er stofnuð og verður notuð til að finna heildaraldur listans.
    for x in listi: # For slaufa fer í gegnum lista og geymir breyturnar í x.
        # For slaufa fer í gegnum dict sem er itemað svo hægt sé að geyma gildið og lykilinn í samnefndum breytum
        for key, value in dict.items():
            # Gáð er hvort að x sé sama og key.
            if(x == key):
                # Ef svo er þá plúsar samanlagt sig við value.
                samanlagt += value
                break
    print("Meðalaldur þeirra er", round((samanlagt/len(listi)),2)) # Meðalaldurinn er reiknaður og prentaður út.

verkefni = ["Danspörin", "Símaskrá", "Skráning í bekk", "Hætta"]
while(True):
    for x, y in enumerate(verkefni):
        print(str(x+1)+".", y)
    val = input("Hvaða dæmi viltu skoða? : ")
    greinaskil()

    # Dæmi 1 - Danspörin
    if(val == "1"):
        strakar = ("Einar", "Geir", "Angantínus", "Halldór", "Heimir", "Kristófer") # Stráka dansarar.
        stelpur = ("Rósa", "Kristín", "Guðmunda", "Halldóra", "Gerður", "Anna") # Stelpu dansarar.

        # Listi af nöfnum af dæmum fyrir valmyndina.
        daemi_1 = ["Nafnalisti prentaður út", "Parað er saman eftir röð", "Pör valin af handahófi",
                   "Pör valin af handahófi en aðeins 1 getur komið í einu", "Finna nafn eftir einum staf",
                   "Finna fyrsta staf", "Fleiri en 1 n", "Hætta"]
        while(True):
            for x, y in enumerate(daemi_1):
                print(str(x+1)+".", y)
            val = input("Hvaða fall viltu skoða? : ")
            greinaskil()

            # Nafnalistarnir prentaðir út.
            if(val == "1"):
                prentaTuple(strakar, stelpur)

            # Einstaklingarnir eru paraðir saman eftir röð.
            elif(val == "2"):
                paraRod(strakar, stelpur)

            # Einstaklingarnir eru paraðir saman eftir handahófskenndri röð.
            elif(val == "3"):
                paraRandom(strakar, stelpur)

            # Einstaklingar eru paraðir saman eftir handahófskenndri röð en eitt nafn getur aðeins komið fyri einu sinni.
            elif(val == "4"):
                paraRandomStakur(strakar, stelpur)

            # Reynt er að finna einstakling eftir aðeins einum staf.
            elif(val == "5"):
                listaPrentari(finnaNafn(input("Skrifaðu inn staf sem á að leita að. : "), strakar, stelpur))

            # Reynt er að finna einstakling eftir fyrsta staf hans.
            elif (val == "6"):
                finnaFyrstaStaf(strakar, stelpur)

            # Reynt er að finna einstaklinga sem eru með fleiri en eitt n
            elif(val == "7"):
                listaPrentari(morgN(strakar, stelpur))

            # Hætta: Hættir dæmi 1.
            elif(val == "8"):
                break
            greinaskil()

    # Dæmi 2 - Símaskrá
    elif(val == "2"):
        # Dictionary fullur af nöfnum(key) og símanúmerum(value).
        simaskra = {"Einar":8121234, "Þórgerður":9202138, "Heimir":2302317, "Ragnar":2312309, "Halldór":9218321,
                    "Kristófer":6723214, "Anna":5622364, "Sigurður":2782387, "Pedró":7682347, "Dagný":2312787}
        # Spurt er um þann sem notandi er að leita að.
        nafn = input("Hvern viltu finna? : ")
        finnaSimanumer(nafn, simaskra) # Inntak notandans og dictionary er sett inn í fall.

    elif(val == "3"):
        # Dictionary bekkur er skilgreint og er stútfullt af nöfnum(key) og aldri þeirra(value).
        bekkur = {"Einar":16, "Guðmundur":17, "Árni":4, "Gabríel":20, "Halldór":22, "Heimir":30, "Kristófer":42,
                  "Magnús":15, "Hreiðar":14, "Guðmunda":18, "Þógerður":21, "Sólveig":13, "Guðrún":19, "Geir":6,
                  "Kormákur":78}
        # Þessi listi verður aðeins notaður fyrir valmyndina.
        daemi_2 = ["Bekkurinn er prentaður út", "18 ára eða eldri", "Meðalaldur bekkjarins", "Heildaraldur bekkjarins",
                   "Fyrsti stafur og meðalaldur þeirra", "Hætta"]
        while (True):
            for x, y in enumerate(daemi_2):
                print(str(x + 1) + ".", y)
            val = input("Hvaða fall viltu skoða? : ")
            greinaskil()

            # Prentar út bekkinn.
            if(val == "1"):
                prentaDict(bekkur)

            # Prentar út alla sem eru 18 ára eða eldri.
            elif(val == "2"):
                yfir18(bekkur)

            # Prentar út meðalaldur bekkjarins.
            elif(val == "3"):
                medalaldur(bekkur)

            # Heildar aldur bekkjarins er prentaður út.
            elif(val == "4"):
                heildaraldur(bekkur)

            # Einstaklingar eru fundnir með sama staf og notandi gefur upp og meðalaldur þeirra er reiknaður.
            elif(val == "5"):
                nafnalisti = finnaStafDict(bekkur) # Breytan nafnalisti fær á sig listann sem fallið skilar.
                if(len(nafnalisti) != 0):
                    medalaldurDict_2(nafnalisti, bekkur) # Fallið tekur inn nafnalistann og bekkinn.
            # Hætta: Hætta í dæmi 3
            elif(val == "6"):
                break

            greinaskil()


    elif(val == "4"):
        print("Eigðu góðan dag.")
        break
    else:
        print("Þarna skrifaðir þú eitthvað vitlaust. Reyndu aftur.")

    greinaskil()
