from typing import Type, Union, Optional, List
from domain.Entitate import Entitate
from domain.Prietenie import Prietenie
from errors.Duplicate_Id import DuplicateIdError
from errors.No_Such_Id import NoSuchIdError


class PrietenieRepo:
    def __init__(self):
        self.prietenii = {}

    def read(self, id_prietenie=None) -> Type[Union[Optional[Entitate], List[Entitate]]]:
        if id_prietenie is None:
            return list(self.prietenii.values())

        if id_prietenie in self.prietenii:
            return self.prietenii[id_prietenie]
        else:
            return None

    def adauga(self, prietenie: Prietenie) -> None:
        if self.read(prietenie.id_entitate) is not None:
            raise DuplicateIdError("Exista deja o entitate cu id-ul dat")
        self.prietenii[prietenie.id_entitate] = prietenie

    def sterge(self, id_prietenie: int) -> None:
        if self.read(id_prietenie) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        del self.prietenii[id_prietenie]
