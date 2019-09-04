class Verkalydsfelag():
    def __init__(self, nafn, nr, laun, kt):
        self.nafn = nafn
        self.nr = nr
        self.laun = int(laun)
        self.kt = kt

    def __str__(self):
        return(f'{self.nafn}\n{self.nr}\n{self.laun}\n{self.kt}\n')

    def skatt(self):
        return self.laun * 0.36

    def writeIntoFile(self):
        return list(map(str, [self.nafn, self.nr, self.laun, self.kt]))



