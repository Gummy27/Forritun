#Guðmundur Brimir Björnsson
#Uppsetning hafinn 19. febrúar 2019
def greinaskil():
    print("=========")

while(True):
    for x in range(4):
        print(str(x+1)+". Dæmi", str(x+1)+".")
    print("5. Hætta")
    val = input("Hvaða dæmi viltu skoða? : ")
    greinaskil()

    if(val == "1"):
        MyTuple = ("Einn", 2, "Þrír", 4, "Fimm", 6)
        print(MyTuple[3])
        for x in MyTuple:
            print(x, end=":")
        print()

    elif(val == "2"):
        MyTuple = (["Einn", "Tveir"], ["Þrír", "Fjórir"], ["Fimm", "Sex"], ["Sjö", "Átta"])
        print(MyTuple)
        print(MyTuple[1][1])

    elif(val == "3"):
        MyTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
        print(MyTuple[4])
        print(MyTuple[-4])
        print(MyTuple[1:8])

    elif(val == "4"):
        MyTuple = (1, 2, 3, 4, 5)
        sinnum = int(input("Hvert á margfeldið að vera? : "))
        ThisTuple = tuple((MyTuple[0]*sinnum, MyTuple[1]*sinnum, MyTuple[2]*sinnum, MyTuple[3]*sinnum, MyTuple[4]*sinnum))
        print(MyTuple)
        print(ThisTuple)

    elif(val == "5"):
        print("Eigðu góðan dag.")
        break

    else:
        print("Þarna skrifaðir þú eitthvað vitlaust. Reyndu aftur.")
    greinaskil()