from dataclasses import dataclass
from Domain.entitate import Entitate


@dataclass
class Film(Entitate):
    titlu: str
    gen: str
    pret: float

    def get_text_format(self):
        return f'{self.id_entitate} {self.titlu} {self.gen} {self.pret}'
