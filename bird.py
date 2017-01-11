from animal import Animal

class Bird(Animal):
    def __init__(self,czyLata=0,gatunek=""):
        self.czyLata = czyLata
        self.gatunek = gatunek



uno = Animal(10,10,10)
uno.waga = 45
print(uno.waga)





#  def setWiek(self,wiek):
#      self.wiek = wiek
#  def setKolor(self,kolor):
#      self.kolor = kolor        
#  def setWzrost(self,wzrost):
#      self.wzrost = wzrost
#  def setWaga(self,waga):
#      self.waga = waga
