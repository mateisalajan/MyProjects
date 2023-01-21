from dataclasses import dataclass


@dataclass
class Cafea:
    id_cafea: int
    nume: str
    tara_de_origine: str
    pret: float
