from dataclasses import dataclass


@dataclass
class CafeaError(Exception):
    mesaj: str

    def __str__(self):
        return f'CafeaError: {self.mesaj}'
