from dataclasses import dataclass

from domain.Cafea import Cafea


@dataclass
class CafeaError(Exception):
    """
    Afiseaza mesaj de eroare pt clasa cafea
    """
    mesaj: str

    def __str__(self):
        return f'CafeaError: {self.mesaj}'