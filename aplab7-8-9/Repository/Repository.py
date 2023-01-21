from typing import Protocol, Type, Union, Optional, List
from Domain.entitate import Entitate


class Repository1(Protocol):
    def read(self, id_entitate=None) -> Type[Union[Optional[Entitate], List[Entitate]]]:
        ...

    def adauga(self, entitate: Entitate) -> None:
        ...

    def sterge(self, id_entitate: int) -> None:
        ...

    def modifica(self, entitate: Entitate) -> None:
        ...
