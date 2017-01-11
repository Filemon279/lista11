from animal import Animal

class Dog(Animal):
    def __init__(self,rasa="",ulubionaKarma=""):
        super().__init__()
        self.rasa = rasa
        self.ulubionaKarma = ulubionaKarma
