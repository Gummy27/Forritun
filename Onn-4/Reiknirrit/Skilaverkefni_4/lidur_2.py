import math

def marglitha_i_lista(marglitha):
    part = ""
    listuth_margliða = []
    for index, x in enumerate(fall):
        if index != 0:
            if x == '+' or x == '-' :
                listuth_margliða.append(part)
                if x == '-':
                    part = x
                else:
                    part = ""
            else:
                part += x
        else:
            part += x
    listuth_margliða.append(part)
    
    print(listuth_margliða)
    return listuth_margliða

def skilja_ath_fasta_og_veldi(listuth_margliða):
    til_heildunar = []
    for x in listuth_margliða:
        lithur = x.split('x')
        for x in range(len(lithur)):
            if lithur[x] == '' or lithur[x] == '-':
                lithur[x] = float(lithur[x]+'1')
            else:
                lithur[x] = float(lithur[x])
        til_heildunar.append(lithur)
    
    return til_heildunar

def heildun(til_heildunar):
    for x in range(len(til_heildunar)):
        if len(til_heildunar[x]) == 1:
            til_heildunar[x] = [til_heildunar[x][0], 1]
        else:
            til_heildunar[x][1] += 1
            til_heildunar[x][0] *= (1/til_heildunar[x][1])
    return til_heildunar

def plug_in_heildath_fall(heildath_fall, efri, nedri):
    flatarmal_efri = 0
    for x in fallith_heildath:
        flatarmal_efri += x[0] * (efri ** x[1])

    flatarmal_nedri = 0
    for x in fallith_heildath:
        flatarmal_nedri += x[0] * (nedri ** x[1])

    return flatarmal_efri - flatarmal_nedri

#fall = input("Sláðu inn fallið: f(x)=")
#efriX = input("Sláðu inn x fyrir efri mörk:")
#nedriX = input("Sláðu inn x fyrir neðri mörk:")

fall = "-x2+2"
efriX = 1
nedriX = -1

fallith_heildath = heildun(skilja_ath_fasta_og_veldi(marglitha_i_lista(fall)))

print(plug_in_heildath_fall(fallith_heildath, efriX, nedriX))

