#Guðmundur Brimir Björnsson
#Uppsetning hafinn 14. febrúar 2019
import random

#Fallið greinaskil mun taka á sig það verk að búa til greinaskil með "=".
def greinaskil(lengd=1):
    print("=============="*lengd)

#Þetta fall mun prenta út lista. Hann var því miður aðeins notaður einu sinni en hann virkaði vel.
def ListaPrentar(listi): #Hann tekur inn þann lista sem hann á að prenta fallega út.
    for x, y in enumerate(listi): #enumerate er notað svo að ég fái bæði gildið og teljara.
        if(x != len(listi)-1): #Gáð er hvort að for slaufan sé kominn á endaveg til að forðast eina loka kommu.
            print(y, end=", ") #end er komið fyrir með kommu til að skrifa listann fallega út.
        else:
            print(y) #Hér er enginn komma því það lítur bjánalega. Dæmi: 2, 2, 2,

#Þetta fall mun gera heilan lista af tölum sem valdar voru af handahófi.
def randomListi(byrjun, endir, fjoldi):  #Fallið fær breyturnar byrjun og endir sem á að vera það millibil sem tölurnar eru valdar frá. Fjöldinn er fjöldi talnanna,
    listi = []
    for x in range(fjoldi): #For slaufu er komið fyrir og mun fara fjöldi sinnum og í hvert sinn bæta við einni handahófskenndri tölu við listann.
        listi.append(random.randint(byrjun, endir)) #Handahófskennd tala er bætt við listann.
    return(listi) #Listinn er skilaður til forritsins.

#Eins tölur mun finna hvort að einhverja tölur séu sameiginlegar hjá tveimur listum.
def einsTolur(l1, l2): #EinstTölur fallið fær á sig 2 lista sem munu heita l1 og l2.
    listi = []
    for x in l1: #For slaufa er hafinn og mun fara í gegnum allan l1 listann og taka á sig gildið sem það er á.
        for y in l2:#For slaufa er afinn og mun fara í gegnum allan l2 listann og taka á sig gildið sem það er á.
            if(x == y): #Gáð er hvort að gildin úr listunum er það sama.
                listi.append(y)#Sameiginlega gildinu er bætt við lista.
                break#Slaufan er brotinn til að fara að næsta l1 gildi.
    return(listi)#Listinn er skilaður.

#Öfugur fallið mun taka streng og gera hann öfugan.
def ofugur(strengur):#Fallið tekur á sig streng og mun kalla það strengur.
    ofugur_strengur = ""
    for x in range(len(strengur)-1, -1, -1): #For slaufa er hafinn og mun keyra öfugt frá lengd textans og til fyrsta stafsins.
        ofugur_strengur += strengur[x] #Gildinu er bætt við strenginn
    return(ofugur_strengur)#Öfugur strengurinn er skilaður.

#Reikna gróða fallið mun reikna hve mikinn gróða verslun fær af tiltekni vöru.
def reiknaGroda(soluv, innkv, vsk): #Fallið tekur á sig gildið söluverð, innkaupverð og virðisaukaskattur.
    return(soluv-(innkv+vsk))#Dæmið er reiknað og síðan skilað.

#Fallið prenta er notað til að prenta út skilaboð sem er í samræmi við ágóða vörunnar.
def prenta(agodi):#Fallið tekur inn ágóða vöru og breytir því í gildið agodi.
    if(agodi < 0): #Gáð er hvort að ágóðinn sé minni en 0 kr
        print("Hér hefur eitthvað farið úrskeiðis.")
    if(agodi == 0): #Gáð er hvort að ágóðinn sé nákvæmlega 0 kr
        print("Hækkaðu álagninguna á vörunni þinni.")
    elif(agodi > 0): #Gáð er hvort að ágóðinn sé meiri en 0 kr
        print("Ágóðinn er", agodi, "kr")

verkefni = ["Listi", "Strengur", "Föll", "Hætta"]
while(True):
    for x in range(len(verkefni)):
        print(str(x+1)+".", verkefni[x])
    val = input("Hvaða verkefni viltu skoða? : ")
    greinaskil()

    #Dæmi 1 - Random Listar og Eins tölur.
    if(val == "1"):
        print("Dæmi 1 - Random Listar og Eins Tölur.")
        listiA = randomListi(50, 100, 100) #Byrjun = 50 | Endir = 100 | Fjöldi = 100
        listiB = randomListi(75, 200, 150) #Byrjun = 75 | Endir = 200 | Fjöldi = 150
        listiC = einsTolur(listiA, listiB) #l1 = listiA | l2 = listiB
        greinaskil(5)
        print("Listi A :", end="")
        ListaPrentar(listiA) #Listi = listiA
        greinaskil(5)
        print("Listi B :", end="")
        ListaPrentar(listiB) #Listi = listiB
        greinaskil(5)
        print("Listi C :", end="")
        ListaPrentar(listiC) #Listi = listiC

    #DÆmi 2 - Strengjavinnsla
    elif(val == "2"):
        print("Dæmi 2 - Strengjavinnsla")
        greinaskil()
        texti = input("Skrifaðu inn texta: ") #Spurt er um texta.
        print("Það eru", len(texti.split(' ')), "orð í þessum texta") #Orða fjöldi
        print("Þessi texti er", len(texti), "stafa langur.") #Stafa fjöldi
        print("Þessi texti hefur", texti.lower().count("b"), "b/B í textanum.") #Fjöldi b/B í texta
        teljari = 0
        #Þessi slaufa virkar þannig að forritið prófar að breyta gildinu í int og ef það virkar þá fer teljarinn upp en annars þá gerist ekkert.
        for x in texti:
            try:
                int(x)
                teljari += 1
            except ValueError:
                pass
        print("Þessi texti hefur", teljari, "tölustafi.") #Fjöldi tölustafa í texta.
        print("Textinn öfugur er", ofugur(texti)) #Textinn skrifaður út öfugt.

    #Dæmi 3 - Ágóði vöru
    elif(val == "3"):
        print("Dæmi 3 - Ágóði vöru")
        greinaskil()
        soluverd = int(input("Hvað er söluverðið á vörunni? : ")) #Spurt er um söluverð.
        innkaupsverd = int(input("Hvað er innkaupsverðið? : ")) #Spurt er um innkaupsverð
        vaskur = int(input("Hver er virðisaukarskattur vörunnar? : ")) #Spurt er um virðisaukarskatt.
        prenta(reiknaGroda(soluverd, innkaupsverd, vaskur)) #reiknagróða fallið er sett strax inn í prenta fallið.

    elif(val == "4"):
        print("Eigðu góðan dag.")

    else:
        print("Þarna skrifaðir þú eitthvað vitlaust. Reyndu aftur.")
    greinaskil()
