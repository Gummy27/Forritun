#Gudmundur Brimir Bjornsson 
#Uppsetning hafinn 2019-04-02
import math

def greinaskil(): 
    print('==========')

# Klasinn Hringur er með einn eiginleika sem heitir r og táknar radíus hrings.
class Hringur():
    # Smiðurinn setur input frá notanda í eiginleikann self.radius
    def __init__(self, r):
        self.radius = r

    # Þetta fall tekur inn eiginleika klasans og reiknar ummál hringsins.
    def ummal(self):
        return(2*self.radius*math.pi)

    # Þetta fall tekur inn eiginleika klasans og reiknar flatarmál hringsins.
    def flatarmal(self):
        return(2*math.pow(self.radius, 2)*math.pi)

    # Þetta fall tekur inn einginleika klasans og reiknari rúmmál kúlunnar.
    def rummal(self):
        return((3*(math.pow(self.radius,3)*math.pi))/4)

# Klasinn Jofnur hefur 2 eiginleika sem heita x og z. Þeir tákna algebru breytu.
class Jofnur():
    # Smiðurinn býr til x og z útfrá input notanda.
    def __init__(self, x, z):
        self.x = x
        self.z = z

    # fallið daemi1 tekur inn eiginleika klasans og setur þá upp í algebru stæðu. Það síðan skilar svarinu.
    def daemi1(self):
        x = self.x
        return(3*x+4+2*math.pow(x, 3))

    # fallið daemi2 tekur inn eiginleika klasans og setur þá upp í algebru stæðu. Það síðan skilar svarinu.
    def daemi2(self):
        x, z = self.x, self.z
        return((math.pow(z,2)+math.pow(x,2))*4)

# Klasinn Hnit hefur 2 eiginleika sem heita x og y. Þeir tákna hnít á hvorum ásunum  fyrir sig.
class Hnit():
    # Smiðurinn býr til tvo eiginleika frá inputi notanda.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Ef klasinn er prentaður út þá eru hnitin skiluð á stærðflæðilega réttum hætti.
    def __str__(self):
        return(f"({self.x},{self.y})")

    # Fallið hvar tekur inn eiginleika klasans og notar hann til að finna á hvaða svæði hnitin eru.
    def hvar(self):
        # Skrifað er út svæðisskipan svo léttara er fyrir notanda að sjá hvar punkturinn er.
        print("1 | 2")
        print("-----")
        print("3 | 4")
        # Gáð er hvort að y sé minna en 0. Ef svo er þá er hann fyrir neðan x ásinn.
        if self.y < 0:
            # Gáð er hvort að x sé minna en 0. Ef svo er þá er hann vinstra megin við y ásinn.
            if self.x < 0:
                stadsetning = 3
            # Annars er punkturinn hægra megin við y ásinn.
            else:
                stadsetning = 4
        # Annars er punkturinnn fyrir ofan x ásinn
        else:
            # Gáð er hvort að x sé minna en 0. Ef svo er þá er hann vinstra megin við y ásinn.
            if self.x < 0:
                stadsetning = 1
            # Annars er punkturinn hægra megin við y ásinn.
            else:
                stadsetning = 2

        return(f"Punkturinn er á svæði {stadsetning}")

    # Fallið lengd tekur inn eiginleika klasans og annað tilvik klasans. Þetta verður notað til að finna fjarlægð milli tveggja punkta.
    def lengd(self, p2):
        return(math.sqrt(math.pow(abs(self.x - p2.x), 2) + math.pow(abs(self.y - p2.y), 2)))

verkefni = ['Klasarnir hringur og jofnur', 'Klasinn hnit', 'Hætta'] 
while(True): 
    for teljari, nafn in enumerate(verkefni):
        print(str(teljari+1)+'.', nafn)
    val = input('Hvaða dæmi viltu skoða? : ') 
    greinaskil() 

    # Dæmi 1 - Klasarnir Hringur og Jofnur
    if(val == '1'):
        # Fyrsta tilvik klasans Hringur er skilgreint undir nafninu h1. Hann mun sitja inn input frá notanda.
        h1 = Hringur(int(input("Hver er radíus hringsins? : ")))
        print(f"Ummál = {h1.ummal()}")              # Ummál tilviksins er prentað út.
        print(f"Flatarmál = {h1.flatarmal()}")      # Flatarmál tilviksins er prentað út.
        print(f"Rúmmál = {h1.rummal()}")            # Rúmmál tilviksins er prentað út.
        greinaskil()

        # x, z taka á sig gildi frá inputi sem er splittað.
        x, z = map(int, input("Skrifaðu inn x og z með bil á milli : ").split(" "))
        # x og z eru settar inn í jafna1 tilvik klasans Jofnur.
        jafna1 = Jofnur(x, z)
        print(f"Y = 3X+4+2X^3 = {jafna1.daemi1()}")        # Y = 3X+4+2X^3
        print(f"Y = (Z^2+X^2)*4 = {jafna1.daemi2()}")      # Y = (Z^2+X^2)*4

    elif(val == '2'):
        # X og y taka á sig gildi frá splittuðu inputi notandans.
        x, y = map(int, input("Skrifaðu inn x og y með bil á milli : ").split(" "))
        # Tilvik klasans Hnit er skilgreint sem p1(punktur) og mun hafa gildin x og y.
        p1 = Hnit(x, y)

        x, y = map(int, input("Skrifaðu inn x og y með bil á milli : ").split(" "))
        p2 = Hnit(x, y)

        print("Punktarnir:")
        print(p1)
        print(p2)
        greinaskil()

        print("Punktur 1:")
        print(p1.hvar()) # Hnit punktsins p1 er skrifað út.
        greinaskil()
        print("Punktur 2:")
        print(p2.hvar()) # Hnit punktsins p2 er skrifað út.

        greinaskil()

        print(f"Systa leiðin á milli tveggja punkta er {p1.lengd(p2)}")

    elif(val == '3'): 
        break 
    greinaskil()