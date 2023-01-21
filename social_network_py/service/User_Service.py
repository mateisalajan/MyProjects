from typing import List

from domain.User import User
from domain.User_Validator import UserValidator
from repository.User_Repo import UserRepo


class UserService:

    def __init__(self, user_repo: UserRepo, user_validator: UserValidator):
        self.user_repo = user_repo
        self.user_validator = user_validator

    def adauga_user(self, nume: str, varsta: int) -> None:
        user = User(nume, varsta)
        self.user_validator.valideaza(user)
        self.user_repo.adauga(user)

    def modifica_user(self, id_user: int, nume: str, varsta: int) -> None:
        user = User(nume, varsta)
        self.user_validator.valideaza(user)
        self.user_repo.modifica(id_user, nume, varsta)

    def sterge_user(self, id_user: int) -> None:
        self.user_repo.sterge(id_user)

    def get_all(self) -> List[User]:
        return self.user_repo.read()

    def get_by_id(self, id_user=None) -> [User]:
        return self.user_repo.read(id_user)
