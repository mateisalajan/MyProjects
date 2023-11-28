from dataclasses import dataclass


@dataclass
class CharacterError(Exception):
    mesaj: str

    def __str__(self) -> str:
        return f'CharacterError: {self.mesaj}'
