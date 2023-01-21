from dataclasses import dataclass


@dataclass
class DisciplinaError(Exception):
    mesaj: str

    def __str__(self) -> str:
        return f'DisciplinaError: {self.mesaj}'
