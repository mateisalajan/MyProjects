import random


class Cafenea:
    def __init__(self, nume: str, tara_de_origine: str, pret: float):
        self.id_cafenea = random.randint(1, 100)
        self.nume = nume
        self.tara_de_origine = tara_de_origine
        self.pret = pret

    def __str__(self):
        return f'Cafenea[id:{self.id_cafenea},nume:{self.nume},tara_de_origine:{self.tara_de_origine},pret:{self.pret}]'

    def __eq__(self, other):
        if not isinstance(other, Cafenea):
            return False
        return self.nume == other.nume and self.tara_de_origine == other.tara_de_origine and self.pret == other.pret
