import random


class Cafea:
    def __init__(self, nume: str, tara_de_origine: str, pret: float):
        self.id_cafe = random.randint(1, 100)
        self.nume = nume
        self.tara_de_origine = tara_de_origine
        self.pret = pret

    def __str__(self):
        return f'[Cafea: {self.id_cafe}, {self.nume}, {self.tara_de_origine}, {self.pret}]'

    def __eq__(self, other):
        if not isinstance(other, Cafea):
            return False
        return self.nume == other.nume and self.tara_de_origine == other.tara_de_origine and self.pret == other.pret
