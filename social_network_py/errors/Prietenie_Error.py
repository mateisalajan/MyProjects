from dataclasses import dataclass


@dataclass
class PrietenieError(Exception):
    mesaj: any

    def __str__(self) -> str:
        return f'PrietenieError: {self.mesaj}'
