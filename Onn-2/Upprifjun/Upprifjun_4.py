#Guðmundur Brimir Björnsson
#15. janúar, 2019
import random
def greinaskil():
    print("===========")
val = ""

print("Höfundur: Guðmundur Brimir Björnsson")
print("Þróun hafinn: 15. janúar, 2019")
while(val != "6"):
    greinaskil()
    for x in range(5):
        if(x != 5):
            print(str(x+1)+". Dæmi", x+1)
        else:
            print(str(x+1)+". Hætta")
    print("6. Hætta")
    val = input("Hvað viltu skoða? : ")
    greinaskil()

    if(val == "1"):
        teljari = 0
        setning = input("Skrifaðu inn setningu. : ")

        for x in setning:
            if(x.lower() == "n"):
                teljari += 1

        print("Það voru", teljari, "n í þessari setningu. ")

    elif(val == "2"):
        nafn = []
        for x in range(2):
            nafn.append(input("Skrifaðu inn nafn. : ").capitalize())

        if(len(nafn[0]) == len(nafn[1])):
            print("Nöfnin eru jafn löng.")
        else:
            print("Nöfnin eru ekki jafn löng.")
        if(len(nafn[1]) < len(nafn[0])):
            teljari = nafn[1]
        elif(len(nafn[1]) < len(nafn[0])):
            teljari = nafn[0]
        else:
            teljari = nafn[0]
        
        for x in range(len(teljari)):
            if(nafn[0][x] == nafn[1][x]):
                print("Bókstafur númer", x+1, nafn[0][x], "er eins í báðum nöfnum.")

    elif(val == "3"):
        nafn = input("Skrifaðu inn nafn. : ").lower()

        if(nafn == nafn[::-1]):
            print("Þetta nafn er samhverft sjálfu sér. ")
        else:
            print("Þetta nafn er ekki samhverft sjálfu sér.")
    
    elif(val == "4"):
        val = ""
        texti = input("Gefðu mér texta. : ")
        while(val != "0"):
            print("1. Finnur og skrifar út hversu mörg orð eru í textanum")
            print("2. Athugaðu hvort ákveðið orð eða orðhluti er í strengnum og skrifaðu út svarið.")
            print("3. Segir hvað strengurinn er langur sem notandinn sló inn.")
            print("4. Snýr strengnum sem sleginn var inn við og prentar hann út.")
            print("5. Setur allan strenginn sem notandinn sló inn í stóra stafi og prentar út.")
            print("6. Biður um staf og athugar hvort hann komi fyrir í strengnum.")
            print("7. Setur stórt A i staðinn fyrir öll lítil a sem koma fyrir í strengnum.")
            print("0. Hættir í forritinu.")
            val = input("Hvað viltu skoða? : ")
            greinaskil()

            if(val == "1"):
                teljari = 0
                for x in texti:
                    if(x == " "):
                        teljari += 1
                print("Það eru", teljari+1, "orð í þessum texta.")

            elif(val == "2"):
                teljari = 0
                teljari_1 = 0
                for x in texti:
                    if(x.lower() == "o"):
                        if(texti[teljari_1+1].lower() == "g"):
                            if(teljari_1+2 == len(texti)):
                                teljari += 1
                            elif(texti[teljari_1+2].lower() == " "):
                                teljari += 1
                    teljari_1 += 1
                print("og kemur", teljari, "sinnum fram.")
            
            elif(val == "3"):
                print("Þessi texti er", len(texti), "stafa langur.")
            
            elif(val == "4"):
                print(texti[::-1])
            
            elif(val == "5"):
                print(texti.upper())
            
            elif(val == "6"):
                teljari = 0
                stafur = input("Komdu með staf.")
                for x in texti:
                    if(x.lower() == stafur.lower()):
                        teljari += 1
                print(stafur, "kom", teljari, "sinnum fram.")
                
            elif(val == "7"):
                print(texti.replace("a", "A"))

            elif(val == "0"):
                pass

            else:
                print("Þarnar skrifaðirðu eitthvað vitlaust inn. Reyndu aftur.")
            
    
    elif(val == "5"):
        talnalisti = []
        stadur = []
        minnsta = 500
        for x in range(100):
            i = random.randint(250, 400)
            talnalisti.append(i)
            if(i < minnsta):
                minnsta = i
            

        print("Meðaltal talnanna er", round(sum(talnalisti)/100,2))
        teljari = 0
        for x in talnalisti:
            if(x < 267):
                teljari += 1
        print("Það voru", teljari, "tölur sem voru minni en 267.")
        
        teljari = 0
        for x in range(0, 100):
            if(talnalisti[x] == minnsta):
                stadur.append(x)
                teljari += 1

        print("Minnsta talan er", minnsta, "og kemur", teljari, "sinnum fram")
        print("Sætistala talnanna sem er þær minnstu er:", end=" ")
        for x in stadur:
            if(x != stadur[-1]):
                print(x + 1, end=", ")
            else:
                print(x+1)
    
    elif(val == "6"):
        print("Eigðu góðan dag ;)")

    else:
        print("Þarna skrifaðirðu eitthvað vitlaust inn. Reyndu aftur.")
