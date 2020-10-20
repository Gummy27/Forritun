import math
'''
Heildunin er skipt niður í þrjú föll.

Fyrsta fallið er marglitha_i_lista. Það fall tekur inn jöfnu sem streng og bútar niður alla liðina.
Annað fallið er skilja_ath_fasta_og_veldi. Það fall fer í gegnum liðinna og skilur að fasta og veldi.
Þriðja fallið er heildun þar sem veldin og fastar eru breyttir í samræmi við heildun.
Síðasta fallið er plug_in_heildath_fall sem setur inn gildi og reiknar það út.

Ástæðan fyrir því að þetta sé skipt svona niður er að léttara er að finna út hvaða fall fór úrskeiðis.
Einnig er mun léttara að kommenta þannig kóða finnst mér.
'''

# Þetta fall tekur inn jöfnu sem streng og skilur að alla liðina.
def marglitha_i_lista(marglitha):
    part = ""             # Part er skilgreind og verður notuð til að hýsa einn lið í einu.
    listuth_margliða = [] # plug_in_heildath_fall er skilgreind og verður notuð til að hýsa listaða margliðu
    # Þessi lykkja mun fara í gegnum jöfnuna og setja liðina í lista.
    for index, x in enumerate(marglitha):
        # Gáð er hvort að lykkja sé í byrjun strengsins.
        if index != 0:
            # Þetta er í raun þar sem strengurinn splittar. Ef að lykkjan er á einhverjum formerkjum þá
            # Er hann kominn í einhvern annan lið. Þess vegna er part tæmdur.
            if x == '+' or x == '-' :
                listuth_margliða.append(part) # Kláraði liðurinn er settur í lista.
                # Forritið þarf að vita hvort að tala sé mínus eða plús. Þess vegna þarf part að hafa - 
                # formerkið.
                if x == '-':
                    part = x
                else:
                    part = ""
            else:
                part += x # Stakið er bætt við liðinn
        else: 
            part += x     # Stakið er bætt við liðinn
    # Síðasti liðurinn er bættur við.
    listuth_margliða.append(part)

    # Listinn er kláraður og skilaður.
    return listuth_margliða

# Þetta fall tekur inn listann með alla liðina og skilur að fasta og veldi.
def skilja_ath_fasta_og_veldi(listuth_margliða):
    listuth_margliða = marglitha_i_lista(listuth_margliða)

    til_heildunar = [] # Þessi listi mun halda utan um kláraðan lista.

    # Þessi for lykkja mun fara í gegnum listaða margliðuna og skilja að veldi og fasta.
    for x in listuth_margliða:
        # Liðurinn er splittaður. Í flestum tilvikum munu koma tvær breytur t.d. þegar x er '2x2' en
        # Stundum hefur liður bara veldi eða bara fasta. Því myndi aðeins koma ein breyta t.d. þegar
        # x er '2x' eða 'x2'. 
        lithur = x.split('x') 
        for x in range(len(lithur)):
            # Hér er gáð hvort að annað hvort stakið sé tómt eða aðeins með formerki. Bætt er við
            # 1 til að einfalda aðgerðina sem tölvan þarf að gera.
            if lithur[x] == '' or lithur[x] == '-':
                # Lithurinn er endurskilgreindur með 1 bætt við. t.d. '' yrði 1 og '-' yrði -1.
                # Tölunum er breytt í float því stór partur af reikningnum inniheldur brotatölur.
                lithur[x] = float(lithur[x]+'1')
            else:
                # En í flestum tilvikum koma alvöru tölur sem er siðan breytt í float og bætt við í listann.
                lithur[x] = float(lithur[x])
        til_heildunar.append(lithur)
    
    # Listinn er skilaður.
    return til_heildunar

# Þetta fall mun taka inn lista sem er búinn að skilja að fasta og veldi. Jafnan er loksins heilduð.
def heildun(til_heildunar):
    til_heildunar = skilja_ath_fasta_og_veldi(til_heildunar)

    # Þessi lykkja mun fara í gegnum listann og taka inn indexið. Þetta er gert til þess að auðvelda
    # það að breyta listanum.
    for x in range(len(til_heildunar)):
        # Gáð er hvort að stak er einsamallt. Þetta er alltaf þegar það er einn stakur fasti. Það sem er
        # gert er að veldi er sett í 1. Ástæða fyrir því kemur í ljós síðar þegar jafnan er reiknuð.
        if len(til_heildunar[x]) == 1:
            til_heildunar[x] = [til_heildunar[x][0], 1]
        else:
            til_heildunar[x][1] += 1 # Þegar veldi x er heildað er það hækkað um einn. 
            # Síðan er x-ið margfaldað með 1/nýja veldið svo hér sinnuma ég fastann við það.
            til_heildunar[x][0] *= (1/til_heildunar[x][1])
    return til_heildunar

# Þetta fall tekur inn heildath, listað, aðskilið fall og x ása og reiknar flatarmál.
def plug_in_heildath_fall(heildath_fall, efri, nedri):
    flatarmal_efri = 0 # Þessi breyta mun halda utan um flatarmál efri part jöfnunar.
    for x in fallith_heildath:
        '''
        Hérna mun allt útskýrast. Ég ákvað að einfaldast væri að skilja að fasta og veldi
        Í hverjum lið fyrir sig, heilda þá og síðar reikna. Þetta virkaði gífurlega vel og
        er líka einfalt. 
        Dæmi um virkni:
            liðurinn er geymdur sem [fasti, veldi]
            x er síðar sett í þett veldi og margfaldað með fasta.
        Liðir eins og 2 er líka með veldisvísi til að einfalda kóðan. Þess vegna væri liðurinn hjá 2
            [2, 1]
        
        '''
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

'''
Aðeins með föllinn:
Ég skipti aðgerðunum niður í þrjú föll sem kalla síðan á hvorn annan. Ástæðan fyrir því er 
readability. Ef að öll föllinn væru saman í einni steypu þá væri villuleit erfið og einnig 
mat á kóðanum sjálfum. Það er mun léttara að skilja forrit þegar þau eru brotin niður.
'''
fallith_heildath = heildun(fall)

print("Flatarmálið er :", plug_in_heildath_fall(fallith_heildath, efriX, nedriX))

