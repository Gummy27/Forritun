#Guðmundur Brimir Björnsson
#Uppsetning hafinn 29. janúar, 2019 - 
def greinaskil():
    print("=================")
    
def skrifaUt(listi):
    print("Þú skrifaðir inn þessar tölur:", end=" ")
    for x in range(len(listi)):
        if(x != len(listi)-1):
            print(listi[x], end=", ")
        else:
            print(listi[x])

def staersta(listi):
    staerst = listi[0]
    for x in listi:
        if(x > staerst):
            staerst = x
    return(staerst)

def minnsta(listi):
    minnsta = listi[0]
    for x in listi:
        if(x < minnsta):
            minnsta = x
    return(minnsta)

def summa(listi):
    utk = 0
    for x in listi:
        utk += x
    return(utk)

def medaltala(listi):
    summa = 0
    teljari = 0
    for x in listi:
        summa += x
        teljari += 1
    return(summa/teljari)

def setning(ord1 = "Jón", ord2="er", ord3="ekki", ord4="latur"):
    print(ord1, ord2, ord3, ord4)

def medaltal_margra_talna(*listi):
    summa = 0
    teljari = 0
    for x in listi:
        summa += x
        teljari += 1
    return(summa/teljari)

def texta_tjekkari(texti, word):
    ordabreyta = ""
    texti = texti+" "
    for x in texti:
        flag = 0
        if(x != " "):
            ordabreyta = ordabreyta + x
        else:
            if(word == ordabreyta):
                print("Já, þetta orð er í textanum.")
                flag = 1
                break
            else:
                ordabreyta = ""
    return(flag)
    
verkefni = ["Unnið með 5 tölur", "4 færibreytur", "Meðaltal talna", "Finna orðið", "Hætta"] 
while(True):
    for x in range(len(verkefni)):
        print(str(x+1)+".", verkefni[x])
    val = input("Hvaða verkefni viltu skoða? : ")
    greinaskil()
    
    if(val == "1"):
        tolur = []
        for x in range(5):
            tolur.append(int(input("Skrifaðu inn tölu. : ")))
            
        skrifaUt(tolur)
        print("Stærsta talan er", staersta(tolur))
        print("Minnsta talan er", minnsta(tolur))
        print("Summa talnanna er", summa(tolur))
        print("Meðaltal talnanna er", medaltala(tolur))
        
    elif(val == "2"):
        setning()
        setning("Palli")
        setning("Stína", "er")
        setning("Halli", "er", "mjög")
        setning("Einar", "er", "mjög", "latur")
        
    elif(val == "3"):
        tala = medaltal_margra_talna(4, 23, 213, 321, 4214, 3)
        
        teljari = 0
        enda_tala = ""
        flag = 0
        for x in str(tala):
            if(teljari == 4):
                break
            elif(x == "."  or flag == 1):
                flag = 1
                teljari += 1
                enda_tala = enda_tala + str(x)
            else:
                enda_tala = enda_tala + str(x)
        print(enda_tala) 

    elif(val == "4"):
        text = input("Skrifaðu inn texta. : ")
        word = input("Skrifaðu inn orð. : ")
        flag = texta_tjekkari(text, word)
        if(flag == 0):
            print("Nei, þetta orð er ekki í textanum.")
            
    elif(val == "5"):
        print("Eigðu góðan dag.")
        break
    
    else:
        print("Þarna skrifaðir þú eitthvað vitlaust. Reyndu aftur.")

    greinaskil()
    
