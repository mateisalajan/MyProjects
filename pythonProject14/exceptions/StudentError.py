from dataclasses import dataclass


@dataclass
class StudentError(Exception):
    mesaj: str

    def __str__(self) -> str:
        return f'StudentError: {self.mesaj}'
