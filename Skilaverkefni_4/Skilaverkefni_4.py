#Gudmundur Brimir Bjornsson 
#Uppsetning hafinn 2019-03-05
# Föll
# Gömul föll
def greinaskil(): 
   print('==========')

# Fall fyrir valmynd var búið til svo ég þyrfti ekki að búa til valmynd aftur og aftur fyrir hvert dæmi
# Þetta var áður en ég lærði að ég þyrfti ekki að gera valmynd fyrir öll dæmin.
def Valmynd(verkefna_listi): # Fallið tekur inn lista af nöfnum á verkefni svo hann geti prenta það út.
    for x, y in enumerate(verkefna_listi): # x tekur á sig teljara og y tekur á sig nafn á verkefni.
        print(str(x+1)+'.', y) # Prentað er út teljarann + 1 sem segir númer hvað verkefnið er. Nafnið er líka prentað út.
    return(input('Hvaða dæmi viltu skoða? : ')) # Fallið skilar inputi notanda um hvaða verkefni hann ætlar að skoða.


# Föll sem notuð er aftur og aftur
# Fallið skrifaskra tekur inn lista og nafn á skrá og setur allt innihald listanns í skrá..
def skrifaSkra(listi, nafntxt):  # Fallið tekur inn lista(listi) og skrárheiti(nafntxt).
    f = open(nafntxt+".txt", "a+", encoding="utf-8") # f opnar skrá í a+ ham svo hægt sé að umbreyta skránni.
    # Þessi slaufa fer í gegnum listann listi.
    f.write(str(listi)+"\n") # Hár listi er skrifaður inn í skránna ásamt nýrri línu.
    f.close() # Skránni er lokað.

def lesaSkra(nafnTxtSkra):
    f = open(nafnTxtSkra+".txt", "r", encoding="utf-8") # f opnar skrá í les ham.
    try:
        listi = list(map(int, f.read().split(" "))) # Reynt er að setja línuna í lista sem integers.
    except: # Hérna er listi bara hrár því aðeins strengir eru í honum.
        f.seek(0)
        listi = f.read()
    return(listi) # Listanum er skilað.
    f.close()

# Fallið tekur inn lista og prentar hann fallega út.
def prenta(listi): # Fallið tekur inn lista og endurnefnir hann listi.
    for x, y in enumerate(listi): # x tekur á sig teljara og y tekur á sig gildi úr listanum.
        if(x != len(listi)-1): # Gáð er hvort að slaufan sé kominn á síðasta gildi.
            print(y, end=", ")
        else:
            print(y)

# Föll sem eru notuð í dæmi 1
# Þetta fall finnur allar heiltölur á bilinu 1 til 1001 og skilar þeim sem lista.
def slettarTolurListi(): # Fallið tekur ekki inn færibreytur.
    listi = [] # Listi er skilgreindur og mun vera notaður til að geyma heiltölurnar sem fallið finnur.
    # For lykkja er hafinn og mun keyra frá 1 til 1001.
    for x in range(1, 1001): # X mun taka gildi og lykkjan gáir að því hvort að hún sé heiltala eða ekki.
        if x % 2 == 0: # Gáð er hvort að x sé heiltala með því að gá hvort að x deilt með 2 gefur engan afgang. Ef svo er þá er hún heiltala.
            listi.append(x) # Heiltölunni er síðan bætt við í lista.
    return(listi) # Listinn sem inniheldur allar heiltölurnar eru skilaðar.


# Þetta fall tekur inn lista og finnur meðaltal allra talnanna sem eru í honum.
def medaltal(listi): # Fallið tekur inn lista sem verður nefndur listi innan fallsins.
    medaltalid = sum(listi)/len(listi) # Meðaltalið er reiknað og er geymt í breytu sem heitir medaltalid.
    return(round(medaltalid, 2))  # breytan medaltalid er skilað með aðeins tveimur aukastöfum.

# Þetta fall finnur allar tölur í lista sem 8 gengur upp í.
def uppI8(listi): # Fallið tekur inn lista og nefnir listann listi.
    listi_2 = [] # Listi_2 er skilgreindur og mun vera notaður til að geyma allar tölurnar sem 8 gengur upp í.
    for x in listi: # For lykkja er hafinn og mun fara í gegnum allar tölur listanns og gefa x þær.
        if x % 8 == 0: # Gáð er hvort að 8 gengur upp í x. 
            listi_2.append(x) # X er bætt við í lista_2 ef 8 gengur upp í hann.
    return(listi_2) # listi_2 er skilaður.

# Þetta fall prentar út hlutina úr listanum með einu bili og aðeins 10 hlutir í hverri línu.
def prenta_10(listi): # Fallið tekur inn lista og endurnefnir hann listi.
     # for slaufa er hafinn með enumerate falli sem mun láta eins og teljari.
    for x, y in enumerate(listi, 1): # x tekur inn teljarann sem enumerate gefur og y mun taka hlut úr listanum.
        if x % 10 == 0: # Gáð er hvort að x sé deilanlegt með 10 til þess að gá hvort 10 hlutir hafa verið skrifaðir út.
            print(y) # Y er prentað eitt og sér út svo að ný lína er búin til. 
        else:
            print(y, end=(" "*(4-len(str(y))))) # Y er prentað út með millibili sem er í samræmi við lengd tölustafsins.
    print() # Þessi print lætur aðra línu byrjar til öryggis um að lykkjan hafi lent á end=""

# Föll sem eru notuð í dæmi 2

# Þetta fall finnur allar prímtölurnar frá 0 til 100.
def primtolur_100():
    listi =  [] # Listi er skilgreindur og mun geyma allar prímtölurnar sem eru fundnar.
    for x in range(100): # Þessi for lykkja mun keyra 100 sinnum og gefur x númerið sem lykkjan er á.
        flag = 0 # Bráðabirgðarbreytan flag er búinn til og mun vera notaður sem bool breyta.
        if x % 2 != 0: # Gáð er hvort að x sé deilanleg með 2.
            # Önnur for lukkja er hafinn og mun fara frá 2 upp í x. 
            for i in range(2, x): # Hún er notuð til að deila allar þær tölur sem geta mögulega verið deildar með x til að vera viss um að x sé prímtala.
                if x % i == 0: # Gáð er hvort að x sé deilanleg með i.
                    flag = 1 # flag er gefið gildið 1 sem segir að talan x sé ekki prímtala.
                    break # For lykkjan er brotinn því við vitum núna að x sé prímtala.
            if flag == 0: # Gáð er hvort að flag sé 0. Ef svo er þá er x prímtala.
                listi.append(x) # Prímtölunni er bætt við í lista.
    return(listi) # Listanum er skilað.

# Þetta fall gáir hvort að tölustafur innihaldi tölustafinn 7
def tolur7(listi): # Fallið tekur inn lista sem verður endurnefndur í listi.
    for x in listi: # Farið er í gegnum listann með breytuni x. 
        if(str(x).count("7") >= 1): # Þessi if skipun gáir hvort að fallið count hafi talið eina eða fleiri sjöur.
            print(x) # X er prentað út.

# Þetta fall fer í gegnum lista og setur fjórða hverja tölu í lista.
def fjorda_hver_tala(listi): # Fallið tekur inn lista sem verður endurnefndur í listi.
    nyr_listi = [] # Listinn nyr_listi er skilgreindur og verður notaður til að geyma allar tölurnar.
    # For lykkja fer í gegnum listann listi.
    for x, y in enumerate(listi): # x tekur á sig teljarann sem enumerate gefur og y tekur gildi úr listanum listi.
        if x % 4 == 0: # Gáð er hvort að x sé deilanlegt með 4.
            nyr_listi.append(y) # y er bætt við í lista.
    return(nyr_listi) # Listanum er skilað.

# Föll sem notuð er í dæmi 3

# Þetta fall tekur inn tuple og skrifar hana inn í skránna tuple.txt
def skrifa_i_tuple(tupla): # Fallið tekur inn tuple og endurnefnir hana tupla.
    f = open("tuple.txt", "a+", encoding="utf-8") # f er notað til að opna tuple.txt í umbreytinga fasanum a+ og encoding utf-8
    f.write(str(tupla)+"\n")
    f.close() # Skjalinu er lokað svo að engar villur komi upp með að vista gögnin.

# Þetta fall á að lesa úr texta skjalinu og prenta út innihaldið.
def lesaTupleSkra(): 
    f = open("tuple.txt", "r", encoding="utf-8") # f opnar tuple.txt í lesa fasanum r, encoding er utf-8.
    listi = f.read().split("\n") # Listi fær á sig lista af línunum úr skjalinu.
    for x in listi: # For lykkja þessi fer í gegnum listi og gefur x gildin.
        print(x) # x sem inniheldur eina línu úr skjalinu er prentað út.
    f.close() # Skjalinu er lokað svo að engar villur komi upp með að vista gögnin.

# Þetta fall leyfir notandanum að búa til tuple. 
def bua_til_tuple():
    listi = [] # Listinn listi er skilgreindur og mun vera notaður til að geyma tupluna sem notandi vill búa til.
    lengd = int(input("Hve margir hlutir eiga að fara í tuple? : ")) # Lengd breytan tekur inn tölu sem á að tákna hve marga hluti notandi vill hafa í tuple.
    for x in range(lengd): # For lykkja er hafinn og mun keyra eins oft og framtíðar lengd tuplunar.
        listi.append(input("Sláðu inn hlut sem á að fara í tuple. : ")) # Notandi er spurður um hvað hann vilji geyma í tupluni.
    tupla = tuple(listi) # listinn er breyttur í tuple og er gefinn tupla tuplunni. 
    return(tupla) # Tuple er skilað.
 
# Þetta fall finnur summu fyrstu tuplunar.
def summa_fyrstu_tupplunar():
    f = open("tuple.txt", "r", encoding="utf-8") # f opnar skránna tuple.txt í fasanum r. Encoding = utf-8
    f.seek(0) # f er sett á byrjun skjalsins svo að finnur fyrstu færsluna.
    gut) # Listinn listi tekur inn línu af tölum. Allir svigar teknir út = [1:-2].
    return(sum(listi)) # Summa listans er skilað.
    f.close()
# Föll sem eru notuð í dæmi 4

# Þetta fall lætur notanda búa til dictionary.
def buaTilDict(): 
    dict = {} # Fallið dict er skilgreint og mun vera notað til að geyma dictionary.
    for x in range(int(input('Hve mikið af hlutum á að vera í dictionary? : '))): # For lykkja er hafinn og fer eins oft og notandi gefur upp.
        dict[input("Nafn : ")] = int(input("Tala : ")) # Notandi er spurður um lykil og gildi fyrir dictionary.
    return(dict) # Dictionary er skilað til baka.

# Þetta fall tekur inn dict og skrifar það í skránna.
def skrifaDictISkra(dict):
    f = open('dict.txt', 'a+', encoding='utf-8') # f opnar dict.txt í umbreytingar fasanum a+. Encoding = utf-8.
    f.write(str(dict)+"\n")
    f.close()

# Þetta fall les úr skrá sem inniheldur dictionary og prentar það út.
def lesaDictSkra():
    f = open('dict.txt', 'r', encoding='utf-8') # f opnar dict.txt og opnar það í read ham.
    for x in f:
        print(x)
    f.close()

# Fallið skrifar út lykil og gildi úr skránni.
def skrifaUtItems():
    f = open('dict.txt', 'r', encoding='utf-8') # f opnar dict.txt og opnar hana í read ham.
    print("lykill     gildi")
    for teljari, line in enumerate(f):
        listi = line[1:-2].split(", ")
        for i in listi:
            key, value = i.split(": ")
            print(key.replace("'", ""), " "*(13-len(key)), value)
    f.close()

# Valmynd
verkefni = ['Sléttar tölur', 'Prímtölur', 'Tuple skrá', 'Dictionary', 'Hætta'] 
while(True):
    val = Valmynd(verkefni)
    greinaskil()

    if val == '1':
        slettar_tolur = slettarTolurListi() #a
        skra = input("Hvað á skráin að heita? : ")
        skrifaSkra(slettar_tolur, skra) #b
        innihald = lesaSkra(skra) #c
        prenta(innihald) #d
        medaltal(innihald) #e
        gengurI8 = uppI8(innihald) #f
        skrifaSkra(gengurI8, "sumarslettartolur") #g
        prenta_10(innihald) #h

    elif val == '2':
        primtolur_100() #a
        skrifaSkra(primtolur_100(), "primtolur") #b
        primtolur = lesaSkra("primtolur") #c
        print("Hérna eru allar prímtölurnar frá 0 til 100.")
        prenta(primtolur) #d
        print("Hérna eru allar tölurnar sem hafa 7 í þeim.")
        tolur7(primtolur) #e
        fjordaHver = fjorda_hver_tala(primtolur) #f
        skrifaSkra(fjordaHver, "fjorda") #g
 
    elif val == '3':
        tuple_1 = (1,2,3,4,5,6,7,8,9)
        tuple_2 = ('a','b','c','d','e','f','g','h')
        tuple_3 = ("konni", 123, "sponni", 234)
        skrifa_i_tuple(tuple_1)
        skrifa_i_tuple(tuple_2)
        skrifa_i_tuple(tuple_3)
        print("Tuple skráinn er prentuð út:")
        lesaTupleSkra()
        greinaskil()
        print("Notandi fær að búa til tuple:")
        tuple_listi = bua_til_tuple() #d
        skrifa_i_tuple(tuple_listi)
        greinaskil()
        lesaTupleSkra()
        greinaskil()
        print("Summa fyrstu tuplunar er:", end=" ")
        print(summa_fyrstu_tupplunar())
        f = open('tuple.txt', 'a+', encoding="utf-8")
        f.seek(0)
        f.truncate()
        f.close()

    elif val == '4':
        print("Búa til skrá.")
        skrifaDictISkra(buaTilDict())
        print("Lesa skrá.")
        print(lesaSkra("dict"))
        print("Lesa skrá með dict falli.")
        lesaDictSkra()
        greinaskil()
        skrifaDictISkra(buaTilDict())
        greinaskil()
        skrifaDictISkra(buaTilDict())
        greinaskil()
        skrifaUtItems()
        f = open("dict.txt", "a+", encoding="utf-8")
        f.seek(0)
        f.truncate()
        f.close()


    elif(val == '5'):
        break
    greinaskil()
