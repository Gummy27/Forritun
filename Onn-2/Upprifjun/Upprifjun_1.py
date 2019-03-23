#Guðmundur Brimir Björnsson
#Breytan val er skilgreind svo að forritið geti byrjað val slaufuna.
val = ""
def greinaskil(): #Þetta á aðeins að létta lífið fyrir mig með því að binda þessari skiptingu við eina skipun svo að út kemur jafnt bil á hverjum hluta forritsins. 
    print("===========")
    
while(val != "7"): #While slaufa er hafinn og mun keyra þangað til að notandi velur 7 sem merkir stopp.
    greinaskil() #Greinaskil eru gerð til að gera forritið flottar og nettara.
    for x in range(7): #For slaufa er notuð til að prenta út valmyndina. 
        if(x != 6): #Þetta skilyrði er þarna svo að hætta valmöguleikinn kemur í endann.
            print(str(x+1)+". Dæmi", (x+1)) #Gert er x+1 því að talvan telur frá 0
        else:
            print(str(x+1)+". Hætta")
    val = input("Hvað viltu gera? : ") #Notandinn er spurður
    greinaskil() #Greinaskil eru búinn til.

    #Dæmi 1
    if(val == "1"):
        #Notandinnn er spurður um tölur sem verða geymdar í breytunum  tala1 og tala2 og mun verða að gagni seinna.
        tala1 = int(input("Tala 1 : "))
        tala2 = int(input("Tala 2 : "))

        print("Summa talnanna er", tala1+tala2) #Summa talnanna er prentað út
        print("Margföldun talnanna er", tala1*tala2) #Margföldun talnanna er prentað út

    #Dæmi 2
    elif(val == "2"):
        fornafn = input("Fornafn : ") #Notandi er spurður um Fornafn
        eftirnafn = input("Eftirnafn : ") #Notandi er spurður um Eftirnafn
        fulltnafn = fornafn + " " + eftirnafn

        print("Halló", fulltnafn.title())

    #Dæmi 3
    elif(val == "3"):
        lengd = float(input("Lengd í kílómetrum? : ")) #Notandi er spurður um lengd
        print(lengd, "kílómetrar eru", lengd*1000, "metrar") #Útkoman er prentuð út og lengd er margfölduð með 1000 til að fá út lengdina í km

    #Dæmi 4
    elif(val == "4"):
        laun = int(input("Laun á klukkutíma? : ")) #Notandi er spurður um launin á tímann.
        timar = int(input("Fjöldi klukkutíma sem unnið er? : ")) #Notandi er spurður um hve langan tíma hann vinnur

        print("Hviæeildarlaun verða þá :", laun*timar) #Útkoman er prentuð út. 

    #Dæmi 5
    elif(val == "5"):
        skattur = 0 #Breytan skattur er skilgreind sem 0 svo hægt
        laun = int(input("Laun á klukkutíma? : "))
        timar = int(input("Fjöldi klukkutíma sem unnið er? : "))
        if(laun*timar >= 30000):
            skattur = round(((laun*timar-30000)*0.2),0)
        print("Heildarlaun verða þá :", laun*timar)
        print("Skattur", skattur, "krónur.")

    elif(val == "6"):
        gradur = int(input("Hversu margar gráður? : "))
        hringir = gradur // 360
        gradur = gradur-hringir*360

        print("Það eru", hringir, "hringir og", gradur, "gráður.")
                
        

greinaskil()
