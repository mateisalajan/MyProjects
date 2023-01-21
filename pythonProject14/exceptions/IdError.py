from dataclasses import dataclass


@dataclass
class NoSuchIdError(Exception):
    mesaj: str

    def __str__(self) -> str:
        return f'NoSuchIdError: {self.mesaj}'


@dataclass
class DuplicateError(Exception):
    mesaj: str

    def __str__(self) -> str:
        return f'DuplicateError: {self.mesaj}'
