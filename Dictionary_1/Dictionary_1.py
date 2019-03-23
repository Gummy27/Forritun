#Guðmundur Brimir Björnsson
#Uppsetning hafinn 19. febrúar 2019.
def greinaskil():
    print("=========")

def prentaDict(dict):
    for key, value in dict.items():
        print("Númer", key, "er", value)

def LitirDict():
    MyDict = {1:"Gulur", 2:"Rauður", 3:"Svartur", 4:"Appelsínugulur", 5:"Blár", 6:"Grænn", 7:"Fjólublár", 8:"Hvítur", 9:"Brúnn", 10:"Bleikur"}
    return(MyDict)

def eydaLit(nr, dict):
    dict.pop(nr)
    return(dict)

def prentaLit(nr, dict):
    print(dict[nr])

def NyttDict():
    MyDict = {}
    for x in range(int(input("Hvað viltu hafa dictionary stórt? : "))):
        MyDict[input("Skráðu inn lykil. : ")] = input("Sláðu inn breytu. : ")
    return(MyDict)

LitaDict = {}
verkefni = ["Búa til dictionary", "Prenta dictionary", "Eyða lit", "Prenta ákveðin lit", "Gera afrit af dict - eyða dict og prenta síðan bæði", "Sýna notkun falla", "Nýtt dictionary fall", "Hætta"]
while(True):
    for x, y in enumerate(verkefni):
        print(str(x+1)+".", y)
    val = input("Hvaða verkefni viltu skoða? : ")
    greinaskil()

    if(val == "1"):
        LitaDict = LitirDict()
        print(LitaDict)

    elif(val == "2"):
        prentaDict(LitaDict)

    elif(val == "3"):
        LitaDict = eydaLit(int(input("Nr hvaða lit viltu eyða? : ")), LitaDict)

    elif(val == "4"):
        prentaLit(int(input("Nr hvaða lit viltu prenta út? : ")), LitaDict)

    elif(val == "5"):
        afrit = LitaDict.copy()
        LitaDict.clear()
        prentaDict(afrit)
        print(LitaDict)

    elif(val == "6"):
        print(".items() skrifar út bæði lyklana og breyturnar sem eru í dictionary:")
        print(LitaDict.items())
        greinaskil()
        print(".keyes() sýnir þá lykla sem eru í dictionary:")
        print(LitaDict.keys())
        greinaskil()
        print(".values() sýnir alla breyturnar sem eru í dictionary:")
        print(LitaDict.values())
        greinaskil()
        print(".clear() eyðir öllu gögnunum af dictionary:")
        print(LitaDict.clear())

    elif(val == "7"):
        print(NyttDict())

    elif(val == "8"):
        print("Eigðu góðan dag.")
        break
    else:
        print("Þarna skrifaðir þú eitthvað vitlaust. Reyndu aftur.")

    greinaskil()