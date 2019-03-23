#Guðmundur Brimir Björnsson
#Uppsetning hafinn 29. janúar, 2019 - kláruð 29, janúar, 2019
import math
def greinaskil():
    print("============")
def reiknaRummalKulu(radius):
    return((4*(math.pi)*(math.pow(radius, 3))/3))

def reiknaRummalKassa(lengd, breidd, haed):
    return(lengd*breidd*haed)

def reiknaFlatarmalThrihyrnings(breidd, haed):
    return((breidd*haed)/2)

while(True):
    print("1. Kúla")
    print("2. Kassi")
    print("3. Þríhyrning")
    print("4. Hætta")
    val = input("Rúmmál hvers viltu reikna? : ")
    greinaskil()

    if(val == "1"):
        print(reiknaRummalKulu(int(input("Hver er radíus kúlunnar? : "))))

    elif(val == "2"):
        lengd = int(input("Hvað er lengd kassans? : "))
        breidd = int(input("Hvað er breidd kassans? : "))
        haed = int(input("Hvað er hæð kassans? : "))
        print(reiknaRummalKassa(lengd, breidd, haed))

    elif(val == "3"):
        breidd = int(input("Hver er breidd þríhyrningsins? : "))
        haed = int(input("Hver er hæð þríhyrningsins? : "))
        print(reiknaFlatarmalThrihyrnings(breidd, haed))

    elif(val == "4"):
        print("Eigðu góðan dag.")
        break

    else:
        print("Þarna skrifaðir þú eitthvað vitlaust. Reyndu aftur.")

    greinaskil()
        
    
           
