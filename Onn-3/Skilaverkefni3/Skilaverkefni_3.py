class SkraningNema():
    def nemalisti(nemar):
        print('Nýskráning nema:')
        print("====================")
        for nemi in nemar:
            print(nemi)
            print('')

class Nemi:
    def __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang):
        self.kt = kt
        self.nafn = nafn
        self.kyn = kyn
        self.heimilisfang = heimilisfang
        self.simanumer = simanumer
        self.netfang = netfang

    def __str__(self):
        return f"nafn: {self.nafn}\nKennitala: {self.kt}\nKyn: {self.kyn}\nHeimilisfang: {self.heimilisfang}\nSímanúmer: {self.simanumer}\nNetfang: {self.netfang}"

class Grunnskolanemi(Nemi):
    def __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang, fm, nafnSkola):
        super().__init__(kt, nafn, kyn, heimilisfang, simanumer, netfang)
        self.fm = fm
        self.nafnSkola = nafnSkola

    def __str__(self):
        return f"{super().__str__()}\nForráðamaður: {self.fm}\nSkóli: {self.nafnSkola}"

class Framhaldskolanemi(Nemi):
    def __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang, brautarheiti, busetustyrk):
        super().__init__(kt, nafn, kyn, heimilisfang, simanumer, netfang)
        self.brautarheiti = brautarheiti
        self.busetustyrk = busetustyrk

    def __str__(self):
        return f"{super().__str__()}\nBrautarheiti: {self.brautarheiti}\nSkóli: {self.busetustyrk}"

class Haskolanemi(Nemi):
    def __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang, stig, namslan):
        super().__init__(kt, nafn, kyn, heimilisfang, simanumer, netfang)
        self.stig = stig
        self.namslan = namslan

    def __str__(self):
        return f"{super().__str__()}\nStig: {self.stig}\nNámslán: {self.namslan}"



# Tilvik klasanna.
grskn = Grunnskolanemi('2405052960', 'Guðmundur Brimir Björnsson', 'S', 'Bjarnhólastígur 20', '841-1650', 'brimir27@outlook.com', 'Davíð', 'Álfhólsskóla')
frskn = Framhaldskolanemi('2405052960', 'Guðmundur Brimir Björnsson', 'S', 'Bjarnhólastígur 20', '841-1650', 'brimir27@outlook.com', 'Tölvubraut', 'Tækniskólinn')
haskn = Haskolanemi('2405052960', 'Guðmundur Brimir Björnsson', 'S', 'Bjarnhólastígur 20', '841-1650', 'brimir27@outlook.com', 'Bsc.', 'Já')

print(grskn)
print("=====================")
print(frskn)
print("=====================")
print(haskn)
print("=====================")

SkraningNema.nemalisti([grskn, frskn, haskn])