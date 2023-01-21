import itertools


class Entitate:
    newid = itertools.count()

    def __init__(self):
        self.id_entitate = next(self.newid)

    @property
    def entitate_id_entitate(self):
        return self.id_entitate

    @entitate_id_entitate.setter
    def entitate_id_entitate(self, i: int):
        if i < 0:
            raise ValueError("Id-ul nu poate fi mai mic decat 0")
        self.id_entitate = i
