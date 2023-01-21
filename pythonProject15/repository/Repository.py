from domain.Cafea import Cafea
from errors.CafeaError import CafeaError


class Repo:
    def __init__(self):
        self.cafele = {}

    def read(self, id_cafea=None):
        if id_cafea is None:
            return list(self.cafele.values())
        if id_cafea in self.cafele:
            return self.cafele[id_cafea]
        else:
            return None

    def adauga(self, cafea: Cafea):
        if self.read(cafea.id_cafe) is not None:
            raise CafeaError("Idul trebuie sa fie unic!")
        self.cafele[cafea.id_cafe] = cafea
