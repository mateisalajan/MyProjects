from domain.Prietenie import Prietenie
from errors.Prietenie_Error import PrietenieError


class PrietenieValidator:

    @staticmethod
    def valideaza(prietenie: Prietenie):
        if prietenie.id_user1 < 0:
            raise PrietenieError("Id-ul primului user nu poate fi mai mic decat 0!")
        if prietenie.id_user2 < 0:
            raise PrietenieError("Id-ul celui de al doilea user nu poate fi mai mic decat 0!")
