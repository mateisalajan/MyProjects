from dataclasses import dataclass


@dataclass
class CafeneaError(Exception):
    mesaj: str

    def __str__(self):
        return f'CafeneaError: {self.mesaj}'