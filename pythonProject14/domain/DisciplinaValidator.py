from dataclasses import dataclass

from domain.Disciplina import Disciplina
from exceptions.DisciplinaError import DisciplinaError


@dataclass
class DisciplinaValidator(Exception):

    @staticmethod
    def valideaza(disciplina: Disciplina):
        if len(disciplina.id_disciplina) == 0:
            raise DisciplinaError("Id-ul nu poate fi null")
