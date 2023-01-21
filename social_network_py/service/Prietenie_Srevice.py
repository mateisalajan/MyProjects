from typing import List

from domain.Prietenie import Prietenie
from domain.Prietenie_Validator import PrietenieValidator
from repository.Prietenie_Repo import PrietenieRepo
from repository.User_Repo import UserRepo
from errors.No_Such_Id import NoSuchIdError


class PrietenieService:

    def __init__(self, prietenie_repo: PrietenieRepo, user_repo: UserRepo, prietenie_validator: PrietenieValidator):
        self.prietenie_repo = prietenie_repo
        self.user_repo = user_repo
        self.prietenie_validator = prietenie_validator

    def adauga_prietenie(self, id1: int, id2: int) -> None:
        if self.user_repo.read(id1) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        if self.user_repo.read(id2) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        prietenie = Prietenie(id1, id2)
        self.prietenie_validator.valideaza(prietenie)
        self.prietenie_repo.adauga(prietenie)

    def sterge_prietenie(self, id_prietenie: int) -> None:
        self.prietenie_repo.sterge(id_prietenie)

    def get_all(self) -> List[Prietenie]:
        return self.prietenie_repo.read()

    def get_by_id(self, id_prietenie=None) -> [Prietenie]:
        return self.prietenie_repo.read(id_prietenie)
