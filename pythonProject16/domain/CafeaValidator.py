from dataclasses import dataclass

from domain.Cafea import Cafea
from errors.CafeaError import CafeaError


@dataclass
class CafeaValidator:

    @staticmethod
    def valideaza(cafea: Cafea):
        if cafea.pret < 0:
            raise CafeaError("Pretul nu poate fi < 0!")
