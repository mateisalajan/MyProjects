from dataclasses import dataclass

from domain.Cafea import Cafea
from errors.CafeaError import CafeaError


@dataclass
class CafeaValidator:
    """
    Valideaza o cafea
    """
    @staticmethod
    def valideaza(cafea: Cafea):
        if cafea.pret < 0:
            raise CafeaError("Pretul nu poate fi mai mic decat 0!")
        if len(cafea.nume) < 3:
            raise CafeaError("Numele trebuie sa aiba cel putin 3 caractere!")
        if cafea.nume[0].isupper() is False:
            raise CafeaError("Numele trebuie sa inceapa cu litera mare!")
