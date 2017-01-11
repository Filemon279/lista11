from animal import Animal
from bird import Bird
from alpaka import Alpaka
from dog import Dog

baza = []

b1=Dog()
b2=Dog()

def addToZoo(zwierze):
    baza.append(zwierze)

addToZoo(b1)
addToZoo(b2)




def printAnimals():
    for x in baza:
        print(x)
        
printAnimals()

u1 = Animal(10,10,12,13)
print(u1)
