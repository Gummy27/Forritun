import datetime
import os

nafn = input("Hvað viltu að verkefnið heiti?: ")
os.mkdir(nafn)
daemi = []
for x in range(int(input("Hve mikið af dæmum? : "))):
    daemi.append(input("Hvað heitir dæmið? : "))
daemi.append("Hætta")

f = open(str(nafn)+"/"+str(nafn)+".py", 'a+', encoding='utf8')
f.write("#Gudmundur Brimir Bjornsson \n")
f.write("#Uppsetning hafinn "+str(datetime.date.today())+"\n")
f.write("def greinaskil(): \n")
f.write("    print('==========') \n")
f.write("verkefni = [")
for x, gildi in enumerate(daemi):
    if(x != len(daemi)-1):
        f.write("'"+gildi+"', ")
    else:
        f.write("'"+gildi+"'")
f.write("] \n")
f.write("while(True): \n")
f.write("    for x, y in enumerate(verkefni): \n")
f.write("        print(str(x+1)+'.', y) \n")
f.write("    val = input('Hvaða dæmi viltu skoða? : ') \n")
f.write("    greinaskil() \n \n")
for x in range(len(daemi)):
    if(x == 0):
        f.write("    if(val == "+"'"+str(x+1)+"'"+"): \n")
        f.write("        pass \n \n")
    elif(x == len(daemi)-1):
        f.write("    elif(val == "+"'"+str(x+1)+"'"+"): \n")
        f.write("        break \n \n")
    else:
        f.write("    elif(val == "+"'"+str(x+1)+"'"+"): \n")
        f.write("        pass \n \n")
f.close()