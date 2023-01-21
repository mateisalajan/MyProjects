import random


class Cafea:
    def __init__(self, nume: str, tara_de_origine: str, pret: float):
        self.id_cafea = random.randint(1, 150)
        self.nume = nume
        self.tara_de_origine = tara_de_origine
        self.pret = pret

    def __str__(self):
        return f'[Cafea: {self.id_cafea}, {self.nume}, {self.tara_de_origine}, {self.pret}]'

    def __eq__(self, other):
        if isinstance(other, Cafea):
            return False
        return self.nume == other.nume and self.tara_de_origine == other.tara_de_origine and self.pret == other.pret
