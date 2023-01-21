from dataclasses import dataclass


@dataclass
class UserError(Exception):
    mesaj: any

    def __str__(self) -> str:
        return f'UserError: {self.mesaj}'
