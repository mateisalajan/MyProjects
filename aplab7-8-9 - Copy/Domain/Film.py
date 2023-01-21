from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Film:
    id_film: str
    titlu: str
    gen: str
    pret: float
