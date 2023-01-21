from dataclasses import dataclass


@dataclass
class NoSuchIdError(Exception):
    mesaj: str

    def __str__(self):
        return f'NoSuchIdError: {self.mesaj}'


@dataclass
class DuplicateError(Exception):
    mesaj: str

    def __str__(self):
        return f'DuplicateError: {self.mesaj}'
