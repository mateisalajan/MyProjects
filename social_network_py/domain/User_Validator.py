from domain.User import User
from errors.User_Error import UserError


class UserValidator:

    @staticmethod
    def valideaza(user: User):
        if len(user.nume) == 0:
            raise UserError("Numele nu poate fi un string gol!")
        if user.varsta < 0:
            raise UserError("Varsta nu poate fi mai mica sau egala cu 0!")
