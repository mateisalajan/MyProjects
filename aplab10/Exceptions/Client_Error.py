from dataclasses import dataclass


@dataclass
class ClientError(Exception):
    mesaj: any

    def __str__(self) -> str:
        return f'ClientError: {self.mesaj}'
