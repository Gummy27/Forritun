#Guðmundur Brimir Björnsson
#Uppsetning hafinn 29. janúar, 2019 - kláruð 29. janúar, 2019
def greinaskil():
    print("=================")
    
def brandari():
    input("Hvað sagði eplið við bananan?")
    print("Ekkert því epli kunna ekki að tala.")
    
def brandarar(tala):
    if(tala == "1"):
        input("Af hverju tók hafnfirðingurinn með sér stiga í skólann?")
        print("Til að komast í háskólann.")
    
    elif(tala == "2"):
        input("Af hverju eru ljósku brandarar svona stuttir?")
        print("svo karlmenn geti munað þá")
    
    elif(tala == "3"):
        input("Hvað er blátt og hvítt og felur sig á bakvið ísskáp?")
        print("Feimin mjólkurferna.")
    
    elif(tala == "4"):
        print("Fyrirgefðu það eru aðeins 3 brandarar.")

def kyn(kyn=""):
    if(kyn == "kk"):
        print("Þú ert karlmaður.")
    elif(kyn == "kvk"):
        print("Þú ert kvenmaður.")
    else:
        print("Þetta kyn þekki ég ekki.")
          
verkefni = ["Brandari", "Brandarar", "Kyn", "Hætta"]
val = ""
while(True):
    for x in range(len(verkefni)):
        print(str(x+1)+".", verkefni[x])
    val = input("Hvaða fall viltu keyra? : ")
    greinaskil()

    if(val == "1"):
        brandari()

    elif(val == "2"):
          brandarar(input("Veldu brandara 1-3: "))

    elif(val == "3"):
        val = input("Hvaða kyn ertu? : ")
        kyn(val)

    elif(val == "4"):
          print("Eigðu góðan dag.")
          break
    else:
          print("Þarna skrifaðirðu eitthvað vitlaust. Reyndu aftur.")
    greinaskil()
          
