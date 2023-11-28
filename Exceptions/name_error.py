from dataclasses import dataclass


@dataclass
class NoSuchNameError(Exception):
    mesaj: any

    def __str__(self) -> str:
        return f'NoSuchNameError: {self.mesaj}'


@dataclass
class DuplicateNameError(Exception):
    mesaj: any

    def __str__(self) -> str:
        return f'DuplicateNameError: {self.mesaj}'
