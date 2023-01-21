from dataclasses import dataclass
from Domain.entitate import Entitate


@dataclass
class Inchiriere(Entitate):
    id_client: int
    id_film: int

    def get_text_format(self):
        return f'{self.id_client} {self.id_film}'
