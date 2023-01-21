from dataclasses import dataclass

from domain.Cafea import Cafea


@dataclass
class DuplicateIdError(Exception):
    mesaj: str

    def __str__(self):
        return f'DuplicateIdError: {self.mesaj}'