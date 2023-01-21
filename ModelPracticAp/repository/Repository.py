from domain.Cafenea import Cafenea
from exceptii.IdError import DuplicateError


class Repository:
    def __init__(self):
        self.cafenele = {}

    def read(self, id_cafenea=None):
        if id_cafenea is None:
            return list(self.cafenele.values())

        if id_cafenea in self.cafenele:
            return self.cafenele[id_cafenea]
        else:
            return None

    def adauga(self, cafenea: Cafenea) -> None:
        if self.read(cafenea.id_cafenea) is not None:
            raise DuplicateError("Exista deja o entitate cu id-ul dat!")
        self.cafenele[cafenea.id_cafenea] = cafenea
