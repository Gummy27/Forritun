#Guðmundur Brimir Björnsson
#Uppsetning hafinn: 22. janúar 2019 - Uppsetning kláruð: 24. janúar 2019.
'''Kommenta leiðbeiningar'''
# ' ' = breyta/listi    " " = skipun/jafna.
val = ""
teljari_for = 0
import random

#Fallið 'greinaskil' er búið til og verður notað til að gera.... greinaskil hvað annað?
def greinaskil():
    print("==========")

#Falli' "ListaPrentari" er búinn til og hún tekur inn lista og breytir honum í listann 'listi'. Hann verður notaður til að prenta út lista á snyrtilegan hátt.
def ListaPrentari(listi):
    #"for" lykkja er byrjuð og hún mun keyra eins oft og það eru tölur í listanum 'listi'.
    for x in range(len(listi)):
        #Hér er gáð hvort að "for" lykkjan sé kominn á síðustu töluna á listanum. Ef svo er þá mun hún fara í gegnum "else" kóðann.
        if(x != len(listi)-1):
            print(listi[x], end=", ")
        #Hér mun kóðinn prentast út án "end" svo að listinn muni ekki prentar út svona: 0, 0, 0, heldur: 0, 0, 0
        else:
           print(listi[x])
           
#Dæmigerð "while" lykkja er prentuð út.
while(val != "6"):
    for x in range(6):
        if(x != 5):
            print(str(x+1)+". Dæmi", x+1)
        else:
            print(str(x+1), "Hætta")
    val = input("Hvaða dæmi viltu skoða? : ")
    greinaskil()

    #Dæmi 1 - Listi fyrir tölur
    if(val == "1"):
        talnalisti = []
        undir_50 = []
        #Í þessar "for" lykkju er bætt við 'talnalisti' listann og tékkað hvaða tölur eru undir 50,5
        for x in range(7):
            tala = float(input("Skrifaðu inn tölu. : ")) #Float er notað svo að hægt sé að sitja inn kommutölur. s.s. 50.5
            talnalisti.append(tala)
            #Gáð er hvort að talan sé minni eða jafnt og 50.5
            if(tala <= 50.5):
                undir_50.append(tala)
        talnalisti.sort()
        greinaskil()

        #Hér er listinn 'talnalisti' prentaður fallega út.
        print("Tölurnar prentaðar eftir stærð:", end=" ")
        ListaPrentari(talnalisti)

        #Hér er listinn 'undir_50' prentað fallega út.
        print("Tölur minni en 50.5:", end=" ")
        ListaPrentari(undir_50)
        print("Tölurnar sem voru undir 50,5 voru", len(undir_50), "að þessu sinni.")

    #Dæmi 2 - Random tölur
    elif(val == "2"):
        print("===Upprunalega===")
        #Breytur
        talnalisti = []
        undir_250 = 0
        yfir_250  = 0
        teljari = 0

        #Þessi "for" lykkja telur þær tölur sem eru minni og stærri en 250. Hún prentar líka tölurnar út.
        for x in range(70):
            teljari += 1 
            tala = random.randint(1, 500)
            talnalisti.append(tala)
            if(tala >= 0 and tala <= 250):
                undir_250 += 1
            elif(tala >= 251 and tala <= 500):
                yfir_250 += 1
            if(teljari == 4 or x == 69): #Gáð er hvort að búið sé að skrifa eina línu með því að gá hvort að slaufann hafi gengið 4*eitthvað. Ef svo er þá mun talan prentast út með ekkert "end".
                print(tala)
                teljari = 0
            else: #Hér er talan prentuð út með "end". "4-len(str(tala))" er jafna sem tryggir það að bilið á milli dálka sé alltaf jafn langt.
                print(tala, end=" "*(4-len(str(tala))))
                
        talnalisti.reverse() #Hér mun listinn 'talnalisti' verða öfugur.
        print("\n===Öfuga===")

        #Þessi lykkja er í grundvallaatriðum alveg eins og sú fyrri. Hennar verk er að prenta tölurnar í 6 dálka. Eina breytinginn er einföldun og teljarinn telur upp í 6 núna.
        for x in range(70):
            teljari += 1
            if(teljari == 6 or x == 69):
                print(talnalisti[x])
                teljari = 0
            else:
                print(talnalisti[x], end=" "*(4-len(str(talnalisti[x]))))
        print("Það voru", undir_250, "tölur á bilinu 1-250 og",  yfir_250, "tölur á bilinu 251-500")

    #Dæmi 3 - Strengjalisti
    elif(val == "3"):
        nafnalisti = []
        #Hér verðu notandi spurður 5 sinnum um nafn í gegnum "for" lykkju.
        for x in range(5):
            nafnalisti.append(input("Skrifaðu inn nafn. : "))
        greinaskil()

        #Hér mun önnur valmynd vera prentuð út og while lykkja er sett utan um hana svo að notandi getur valið eins oft og hann vill.
        while(val != "5"):
            nafnalisti_2 = [] #'nafnalisti_2' er skilgreindur og mun hýsa ýmsar breytingar á 'nafnalisti' svo að hann breytist ekki sjálfur.
            for x in nafnalisti:
                nafnalisti_2.append(x)
            print("1. Birta nöfnin óröðuð.")
            print("2. Raða nöfnunum í stafrófsröð og birta.")
            print("3. Raða nöfnunum í öfuga stafrófsröð og birta.")
            print("4. Birta eitt nafn eftir því hvaða númer 1-5 var valið.")
            print("5. Hætta í verkefni 3.")
            val = input("Hvaða verkefni viltu skoða? : ")
            greinaskil()

            #Nafnalistinn er prentaður óbreyttur út.
            if(val == "1"):
                ListaPrentari(nafnalisti)

            #Nafnalistinn er prentaður út í stafrófsröð.
            elif(val == "2"):
                nafnalisti_2.sort()
                ListaPrentari(nafnalisti_2)

            #Nafnalisti er prentaður út í öfugri stafrófsröð.
            elif(val == "3"):
                nafnalisti_2.sort()
                nafnalisti_2.reverse()
                ListaPrentari(nafnalisti_2)

            #Notandi velur númer hvaða nafn hann vilju prenta út.
            elif(val == "4"):
                val = input("Hvaða nafn viltu skrifað út. 1-5. : ")
                print(nafnalisti[int(val)-1])

            #Forritið kveður.
            elif(val == "5"):
                print("Bæ, bæ")
                break
            greinaskil()

    #Dæmi 4 - Teningakast
    elif(val == "4"):
        teljari = int(input("Hve oft viltu kasa teningnum? : "))
        teljara_listi = [0, 0, 0, 0, 0, 0] #'teljara_listi' geymir í fyrstu 6 núll sem hver um sig á að tákna einn af 6 tölunum sem hægt er að fá á teningnum. 
        #Í þessari for lykkju fær 'tala' á sig tölu sem valinn er af handahófi af fallinu "random". Talan er síðan prentuð út.
        for x in range(teljari):
            tala = random.randint(1, 6)
            #Gáð er hvort að lykkja sé kominn á síðasta snúning. Þetta er gert svo að síðasta talan sé prentuð verði ekki með , á endanum.
            if(x != teljari-1):
                print(tala, end=", ")
            else:
                print(tala)
            teljara_listi[tala-1] += 1 #Eitt af tölunum á listanum 'teljara_listi' hækkar. Tilgangur þess er að telja hve oft þessar tölur koma fyrir.
        greinaskil()
         
        haesta = []
        minnsta = []
        
        for x in range(6):
            print(str(x+1)+":", teljara_listi[x], end="   ") #Talan og hve oft hún kom fyrir er prentað út í einni línu.

            #Gáð er hvort að "for" lykkjan sé á fyrstu lykkjunni. Ef svo er þá mun lykkjan keyra í gegnum "else" kóðann.
            if(x != 0):
                #Hér er gáð hvort að tíðni tölunar er hærri en tíðni síðustu tölunnar. Ef svo er þá fær 'heasta' listinn á sig þessa tölu.
                if(teljara_listi[x] > teljara_listi[haesta[0]-1]):
                    haesta = [x+1]

                #Hér er gáð hvort að tíðni tölunnar er jafn og tíðni síðustu tölunnar. Ef svo er þá er talan bætt við 'heasta' listann.
                elif(teljara_listi[x] == teljara_listi[haesta[0]-1]):
                    haesta.append(x+1)

                #Hér er gáð hvort að tíðni tölunnar er minni en tíðni síðustu tölunnar. Ef svo er þá fær 'minnsta' listinn á sig þessa tölu.
                if(teljara_listi[x] < teljara_listi[minnsta[0]-1]):
                    minnsta = [x+1]

                #Hér er gáð hvort að tíðni tölunnar er jafn og tíðni síðustu tölunnar. Ef svo er þá er talan bætt við 'minnsta' listann.
                elif(teljara_listi[x] == teljara_listi[minnsta[0]-1]):
                    minnsta.append(x+1)
                    
            #Hér mun 'heasta' listinn og 'minnsta' listinn fá á sig sína fyrstu tölu. 
            else:
                haesta.append(x+1)
                minnsta.append(x+1)
        print("\n"+str(minnsta)+" kom sjaldnast við en", haesta, "kom mest við.")
                
    #Dæmi 5 - Skráning í áfanga.       
    elif(val == "5"):
        nafnalisti = []
        #Notandi er spurður hve margir eru í áfanganum.
        teljari = int(input("Hve margir eru skráðir í hópinn FOR1TÖ05BU. : "))
        #Notandi er spurður um nöfn nemendana í áfanganum.
        for x in range(teljari):
            nafnalisti.append(input("Hvað heitir nemandi "+str(x+1)+"? : "))
        nafnalisti.sort()
        greinaskil()
        #Nafnalistinn er prentaður út.
        for x in nafnalisti:
            print(x)

    #Hætta.
    elif(val == "6"):
        #Forritið prentar bæ eins mörgum sinnum og forritið var keyrt.
        print("Bæ, "*teljari_for, end="")
        print("Bæ")
        break

    #Notandi skrifar eitthvað vitlaust inn.
    else:
        print("Þarna skrifaðirðu eitthvað vitlaus. Reyndu aftur.")

    teljari_for += 1
    greinaskil()

    
