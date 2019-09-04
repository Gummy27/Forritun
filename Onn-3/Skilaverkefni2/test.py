import csv
from klasi import Verkalydsfelag

csvFile = 'Verkalydsfelag.csv' # Geymi nafn skjalsins í breytu því það lítur fallegra út.

members = []

def greinaskil():
    print('='*36)

# Fallið opna skrá mun vera notað til að opna skrá og nota upplýsingar þaðan til að búa til hluti.
def opnaSkra():
    # Skjalið er opnað á read stillinguni og vistað í breytuna file.
    with open(csvFile, 'r', newline='', encoding='utf-8') as file:
        # Reader breytan mun taka á sig lista af breytum sem að csv.reader skilaði þegar hann braut niður textan.
        reader = csv.reader(file, delimiter=';')
        # Farið er í gegnum alla listana sem reader hefur að geyma.
        for member in reader:
            # Býr til hlut úr breytunum og bætir hlutnum við listann members.
            members.append(Verkalydsfelag(member[0], member[1], member[2], member[3]))

# Fallið skrifa skrá mun vera notað til að skrifa inn í skránna frá listanum.
def skrifaSkra():
    # Skjalið er opnað með write stillinguni svo að hann eyði öllu úr skjalinu áður en við skrifum inn í það.
    with open(csvFile, 'w', newline='', encoding='utf-8') as writer:
        # Farið er í gegnum listann members.
        for member in members:
            # Hér nota ég join fallið til að forðast óþarfa for slaufur eða harðkóðun.
            writer.write(';'.join(member.writeIntoFile())+'\n') # Join mun blanda str saman og hafa ; á milli þeirra.

# Fallið nyrMedlimur er notað til að bæta við nýjum meðlimum.
def nyrMedlimur():
    nafn = input("Hvað heitir nýji meðlimurinn? : ")
    nr = input("Hvað á númerið hans að vera? : ")
    laun = input("Hvað á hann að fá borgað á mánuði? : ")
    kt = input("Hver er kennitalan hans? : ")
    members.append(Verkalydsfelag(nafn, nr, laun, kt))

# Fallið eyðdaMedlimum er notað til að eyða meðlimum.
def eydaMedlim():
    nr = input("Hvaða númer er hann? : ")
    # Farið er í gegnum listann members. index tekur á sig output af enumerate og member tekur hlutinn.
    for index, member in enumerate(members):
        # Gáð er hvort að við séum kominn á meðlimin sem við ætlum að eyða.
        if member.nr == nr:
            del members[index]
            break

# Fallið breytaMedlim er notað til að breyta meðlim.
def breytaMedlim():
    nr = input("Hvaða númer er hann? : ")
    for member in members:
        if member.nr == nr:
            member.nafn = input("Hvað heitir nýji meðlimurinn? : ")
            member.nr = input("Hvað á númerið hans að vera? : ")
            member.laun = input("Hvað á hann að fá borgað á mánuði? : ")
            member.kt = input("Hver er kennitalan hans? : ")
            break

# Fallið prentaVerkalydsfelag er notað til að prenta allar upplýsingarnar um meðlimi verkalýðsfélagsins.
def prentaVerkalydsfelag():
    for member in members:
        print('-'*36)
        print(member)

# Fallið nafnLaun prentar út nafn meðlims og launin hans fyrir skatt.
def nafnLaun():
    for member in members:
        print(f'{member.nafn}: {member.laun} kr.')

# Fallið utborgudLaun prentar út nafn meðlims og launin hans eftir skatt.
def utborgudLaun():
    for member in members:
        print(f'{member.nafn}: {int(member.laun)-member.skatt()} kr.')


opnaSkra()

verkefni = ['Nýr meðlimur', 'Eyða meðlim', 'Breyta meðlim', 'Prenta verkalýðsfélag', 'Nafn laun', 'Útborguð laun', 'Hætta']
val = ''
while val != '7':
    for index, nafn in enumerate(verkefni):
        print(f'{index+1}. {nafn}')
    val = input("Hvaða dæmi viltu skoða? : ")
    greinaskil()

    if val == '1':
        nyrMedlimur()

    elif val == '2':
        eydaMedlim()

    elif val == '3':
        breytaMedlim()

    elif val == '4':
        prentaVerkalydsfelag()

    elif val == '5':
        nafnLaun()

    elif val == '6':
        utborgudLaun()
    greinaskil()

skrifaSkra()


