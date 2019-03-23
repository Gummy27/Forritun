#Guðmundur Brimir Björnsson
#15. janúar, 2019
val = ""
import datetime
import math
nuna = datetime.datetime.now()
def greinaskil():
    print("===========")
while(val != "8"):
    greinaskil()
    for x in range(8):
        if(x != 7):
            print(str(x+1)+". Dæmi", x+1)
        else:
            print(str(x+1)+". Hætta")

    val = input("Hvað viltu skoða? : ")
    greinaskil()

    if(val == "1"):
        tala = []
        for x in range(3):
            tala.append(input("Skrifaðu inn tölu : "))
        tala.sort()
        for x in range(len(tala)):
            if(x != len(tala)-1):
                print(tala[x], end=" ")
            else:
                print("og", tala[x])
        
        if(tala[0] == tala[1] == tala[2]):
            print("Allar tölurnar eru eins.")
            
    elif(val == "2"):
        nafn = input("Hvað heitir þú? : ")
        aldur = int(input("Hve gamall ertu? : "))
        
        print(nafn, ", um næstu aldamót verður þú", 2100-nuna.year+aldur+1)

    elif(val == "3"):
        listi = []
        tala = 2
        while(tala != 0):
            tala = int(input("Sláðu inn tölu: "))
            listi.append(tala)
        listi= listi[0:-1]
        print("Summa talnanna er:", sum(listi))
        print("Fjöldi talnanna er:", len(listi))
        print("Meðaltal talnanna er:", sum(listi)/len(listi))

    elif(val == "4"):
        radius = int(input("Radíus kúlunnar? : "))
        print("Yfirborðsflatarmál kúlunnar er:", round(4*math.pi*radius*radius,7))
        print("Rúmmál kúlunar er:", round((3*radius*radius*radius*math.pi)/3,7))

    elif(val == "5"):
        tjekkari = 0
        password = input("Sláðu inn lykilorð og forritið mun athuga hvort það er löglegt eða ekki. : ")
        if(len(password) == 6):
            for x in range(10):
                for i in password:
                    if(str(i) == str(x)):
                        tjekkari += 1
            if(tjekkari > 0 and tjekkari != 6):
                print("Þetta lykilorð er í lagi.")
            elif(tjekkari == 0):
                print("Lykilorð ættu að hafa stafi og tölustafi svo að lykilorðinn séu öruggari og flóknari.")
            elif(tjekkari == 6):
                print("Lykilorð ættu að hafa tölustafi og stafi svo að lykilorðinn séu öruggari og flóknari.")
        elif(len(password) > 6):
            print("Þetta lykilorð er alltof langt. Það er", len(password), "þegar það ætti að vera 6 stafir/tölustafir.")
        elif(len(password) < 6):
            print("Þetta lykilorð er alltof stutt. Það er", len(password), "þegar það ætti að vera 6 stafir/tölustafir.")
        
    elif(val == "6"):
        hastafir = 0
        lagstafir = 0
        strengur = input("Skrifaðu inn texta: ")
        for x in strengur:
            if(x == " "):
                pass
            elif(x == x.upper()):
                hastafir += 1
            elif(x == x.lower()):
                lagstafir += 1
        print("Í þessum texta eru", hastafir, "hástafir,", lagstafir, "lágstafir.")

    elif(val == "7"):
        deilingar = []
        tala = []
        samnefnari = 0
        for x in range(2):
            tala.append(int(input("Skrifaðu inn tölu sem er stærri en 0. : ")))
        tala.sort()
        
        for i in range(1, tala[0]+1):
            if(tala[0] % i == 0):
                deilingar.append(i)

        for x in deilingar:
            if(tala[1] % x == 0):
                samnefnari = x

        print("Stærsti samnefnari talnanna er", samnefnari)

    elif(val == "8"):
        print("Eigðu góðan dag.")

    else:
        print("Þarna skrifaðirðu eitthvað vitlaust inn. Reyndu aftur.")
