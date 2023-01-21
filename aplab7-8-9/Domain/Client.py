from dataclasses import dataclass
from Domain.entitate import Entitate


@dataclass
class Client(Entitate):
    nume_client: str
    CNP: str

    def get_text_format(self):
        return f'{self.id_entitate} {self.nume_client} {self.CNP}'
