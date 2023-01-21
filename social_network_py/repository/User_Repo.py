from typing import Type, Union, Optional, List

from domain.Entitate import Entitate
from domain.User import User
from errors.Duplicate_Id import DuplicateIdError
from errors.No_Such_Id import NoSuchIdError


class UserRepo:
    def __init__(self):
        self.useri = {}

    def read(self, id_user=None) -> Type[Union[Optional[Entitate], List[Entitate]]]:
        if id_user is None:
            return list(self.useri.values())

        if id_user in self.useri:
            return self.useri[id_user]
        else:
            return None

    def adauga(self, user: User) -> None:
        if self.read(user.id_entitate) is not None:
            raise DuplicateIdError("Exista deja o entitate cu id-ul dat")
        self.useri[user.id_entitate] = user

    def sterge(self, id_user: int) -> None:
        if self.read(id_user) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        del self.useri[id_user]

    def modifica(self, id_user: int, n: str, v: int) -> None:
        if self.read(id_user) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        user = self.read(id_user)
        user.user_nume = n
        user.user_varsta = v
