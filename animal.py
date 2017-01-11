class Animal:
    def __init__(self,waga=0,wzrost=0,kolor="",wiek=0):
        self.waga = waga
        self.wzrost = wzrost
        self.kolor = kolor
        self.wiek = wiek

    def __str__(self): # zwraca string
        return "Zwierze: Waga: {}, Wzrost: {}, Kolor: {}, Wiek: {}"\
                .format(self.waga, self.wzrost, self.kolor, self.wiek)


