#Gudmundur Brimir Bjornsson 
#Uppsetning hafinn 2019-04-11
import random

# Klasinn Jofnur mun aðeins halda utan undir eitt fall og hefur enga eiginleika.
class Jofnur:
    # Fallið jafna mun finna stærstu töluna af þremur tölum.
    def jafna(tala1, tala2, tala3): # Fallið tekur inn 3 tölur.
        listi = [tala1, tala2, tala3] # Öllum tölunum er bætt við í lista.
        return max(listi) # Hæsta tala lista er fundinn með max fallinu og stærsta talan er skiluð.

# Klasinn Paskaegg hef smið og strengjarfall.
class Paskaegg:
    # Smiðurinn tekur inn tegund eggs og stærð eggs og situr það í samsvarandi klasa eiginleika.
    def __init__(self, tegund_eggs, staerd):
        self.tegund = tegund_eggs
        self.staerd = staerd

    # Strengjar fallið skilar setningu sem segir til um hvernig páskaegg tilvikið hefur og stærð þess.
    def __str__(self):
        return "Ég er páskaegg af tegundinni "+str(self.tegund)+" og er af stærð "+str(self.staerd)

def greinaskil(): 
    print('==========')

# Fallið bua_til_lista verður notaður til að búa til lista af random tölum á bili og fjölda sem notandi velur.
def bua_til_lista(byrjun, endir, fjoldi=100): # Fallið tekur inn færibreyturnar byrjun og endir sem lýsa millibilinu og síðan fjölda
    listi = []
    # For lykkja er hafinn og mun keyra eins oft og notandi vill tölur.
    for x in range(fjoldi):
        # Handahófskenndri tölu á millibilinu byrjun og endir er sett í listann listi
        listi.append(random.randint(byrjun, endir))
    return listi # Listinn er skilaður.

# Fallið syna_lista verður notaður til að prenta út lista með : á milli talnanna.
def syna_lista(tolulisti): # Fallið tekur inn lista af tölum.
    # For lykkja er hafinn og mun fara í gegnum tölulistann. Teljari er búinn til með enumerate fallinu.
    for teljari, tala in enumerate(tolulisti):
        # Gáð er hvort að for lykkjan sé kominn á enda listans svo að : komi ekki á síðustu tölu.
        if teljari != len(tolulisti)-1:
            print(tala, end=":")
        else:
            print(tala)

# Fallið medaltal mun finna meðaltal runu af tölum.
def medaltal(tolulisti): # Fallið tekur inn lista af tölum.
    # Meðaltali tölurununar er skilað. Formúlan er: Summa allra talnanna / fjöldi talna.
    return round(sum(tolulisti)/len(tolulisti), 3)

# Fallið deilanlegt mun finna þær tölur sem eru deilanlegar.
def deilanlegt(tolulisti):
    deilanlegir = []
    # For lykkja er hafinn og mun fara í gegnum allar tölur listans.
    for tala in tolulisti:
        # for lykkja er hafinn og mun fara frá 2 og upp í tala-1 til að finna hvort einhver tala sé deilanleg með henni.
        for deilir in range(2, tala):
            # Gáð er hvort að ef að tölurnar séu deildar að einhver afgangur verði eftir.
            if tala % deilir == 0:
                # Talan sem reyndist vera deilanleg er bætt við í lista af deilanlegum tölum
                deilanlegir.append(tala)
                break
    # Listinn af deilanlegum tölum er skilað.
    return deilanlegir

# Fallið skila_bili mun finna þær tölur á bili sem notandi velur.
def skila_bili(tolulisti, fra, til):
    bil = []
    # For lykkja er hafinn og mun fara í gegnum tölulistann.
    for tala in tolulisti:
        # Gáð er hvort að talan sé bæði stærri eða jafnstór og minnsta talan sem notandi vill hafa og að hún sé minni eða jafnstórt og stærsta tala sem notandi vill hafa.
        if tala >= fra and tala <= til:
            bil.append(tala)
    # Lista af tölum sem eru á millibili notanda er skilað.
    return bil

verkefni = ['Föll með listum.', 'jöfnur og páskaegg', 'Hætta']
while(True):
    for x, y in enumerate(verkefni): 
        print(str(x+1)+'.', y) 
    val = input('Hvaða dæmi viltu skoða? : ') 
    greinaskil() 
 
    if(val == '1'): 

        listi1 = bua_til_lista(100, 200) # Listi1 tekur á sig lista frá bua_til_lista fallinu.
        print("Allar tölur lista 1 með : á milli:")
        syna_lista(listi1) # Listinn er prentaður út með syna_lista fallinu.
        print("Meðaltal lista 1:", medaltal(listi1)) # Meðaltal listans er prentaður út með medalta fallinu.

        listi2 = bua_til_lista(1, 50, 50) # listi1 tekur á sig lista frá bua_til_lista fallinu.
        print("Deilanlegar tölur lista 2:", deilanlegt(listi2)) # Allar deilanlegar tölur listans eru fundnar með deilanlegt fallinu.
        print("Bil á milli lista 2:", skila_bili(listi2, 21, 30)) # Tölur sem samsvara millibili sem notandi vill er prentað út.

    elif(val == '2'): 
        tolur = Jofnur # Tilvik klasans Jofnur er búið til og skýrt tolur
        print("Hæsta talan af þessum þrem er ", tolur.jafna(5, 212, 34)) # Prentað er út stærsta tala af 3 með jafna fallinu.

        egg = Paskaegg("Súkkulaði egg", 12) # Tilvik klasans Paskaegg er búið til og skýrt egg
        print(egg) # StrengjaFall tilviksins egg er prentað út.
 
    elif(val == '3'): 
        break

    greinaskil()
 
