
from Domain.entitate import Entitate
from Exceptions.Id_Error import DuplicateIdError, NoSuchIdError


class Repository:
    def __init__(self):
        self.entitati = {}

    def read(self, id_entitate=None):
        if id_entitate is None:
            return list(self.entitati.values())

        if id_entitate in self.entitati:
            return self.entitati[id_entitate]
        else:
            return None

    def adauga(self, entitate: Entitate) -> None:
        if self.read(entitate.id_entitate) is not None:
            raise DuplicateIdError("Exista deja o entitate cu id-ul dat!")
        self.entitati[entitate.id_entitate] = entitate

    def sterge(self, id_entitate: int) -> None:
        if self.read(id_entitate) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        del self.entitati[id_entitate]

    def modifica(self, entitate: Entitate) -> None:
        if self.read(entitate.id_entitate) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        self.entitati[entitate.id_entitate] = entitate
