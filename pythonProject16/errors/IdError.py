from dataclasses import dataclass


@dataclass
class NoSuchIdError(Exception):
    mesaj: str

    def __str__(self):
        return f'NoSuchIdError: {self.mesaj}'


@dataclass
class DuplicateIdError(Exception):
    mesaj: str

    def __str__(self):
        return f'DuplicateIdError: {self.mesaj}'