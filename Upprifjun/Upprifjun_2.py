#Guðmundur Brimir Björnsson
def greinaskil():
    print("=============")
val = ""
while(val != "6"):
    greinaskil()
    for x in range(6):
        if(x != 5):
            print(str(x+1)+". Dæmi", x+1)
        else:
            print(str(x+1)+". Hætta")
    val = input("Hvað viltu skoða? : ")
    greinaskil()

    if(val == "1"):
        nafn_1 = input("Fyrra nafn: ")
        haed_1 = input("Hæð í sentimetrum: ")
        nafn_2 = input("Seinna nafn: ")
        haed_2 = input("Hæð í sentimetrum: ")

        if(haed_1 == haed_2):
            print(nafn_1, "og", nafn_2, "eru jafnhá.")
        elif(haed_1 > haed_2):
            print(nafn_1, "er stærri en", nafn_2)
        elif(haed_1 < haed_2):
            print(nafn_2, "er stærri en", nafn_1)

    elif(val == "2"):
        lengd = int(input("Lengd í metrum: "))
        breidd = int(input("Breidd í metrum: "))
        print("Þessi reitur er", round(lengd*breidd/4046, 3), "ekrur")

    elif(val == "3"):
        breidd = int(input("Breidd reits í metrum: "))

        print("Stærð     Lengd í ekrum")
        for x in range(10):
            print(" ", x+1*10, "           ", round(x+1*10*breidd/4046,6))
            

    elif(val == "4"):
        nafn = input("Hver er skammstöfun áfangans? : "
        
        if(nafn[0:3] == nafn[0:3].upper()):
            if(len(nafn) == 7):
                print("Þetta er rétt skammstöfun á áfanga.")
            else:
                print("Það vantar einn tölustaf í skammstöfunina.")
        else:
            print("Stafirnir eru ekki í hástöfum.")

    elif(val == "5"):
        heild = int(input("Hver er heildin? : "))
        prosenta = int(input("Hver er %? : "))
        print("Niðurstaðan:", heild*(prosenta/100)) 
            
    
            
