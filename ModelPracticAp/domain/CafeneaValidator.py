from dataclasses import dataclass

from domain.Cafenea import Cafenea
from exceptii.CafeneaError import CafeneaError


@dataclass
class CafeneaValidator:

    @staticmethod
    def valideaza(cafenea: Cafenea):
        if cafenea.pret < 0:
            raise CafeneaError("Pretul nu poate fi < 0")
