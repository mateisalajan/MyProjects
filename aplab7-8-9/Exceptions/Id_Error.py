from dataclasses import dataclass


@dataclass
class NoSuchIdError(Exception):
    mesaj: any

    def __str__(self) -> str:
        return f'NoSuchIdError: {self.mesaj}'


@dataclass
class DuplicateIdError(Exception):
    mesaj: any

    def __str__(self) -> str:
        return f'DuplicateIdError: {self.mesaj}'
