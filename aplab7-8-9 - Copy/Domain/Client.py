from dataclasses import dataclass, field

from Domain.Film import Film


@dataclass(frozen=True, order=True)
class Client:
    id_client: str
    nume_client: str
    CNP: str
    lista_filme: list[Film] = field(default_factory=list, compare=False)
