from domain.Disciplina import Disciplina
from domain.DisciplinaValidator import DisciplinaValidator
from repository.DisciplinaRepo import DisciplinaRepo


class DisciplinaService:
    def __init__(self, disciplinarepo: DisciplinaRepo, disciplinavalidator: DisciplinaValidator):
        self.disciplinarepo = disciplinarepo
        self.disciplinavalidator = disciplinavalidator

    def add(self, id_disciplina: str, nume: str, profesor: str):
        disciplina = Disciplina(id_disciplina, nume, profesor)
        self.disciplinavalidator.valideaza(disciplina)
        self.disciplinarepo.adauga(disciplina)

    def delete(self, id_disciplina: str):
        self.disciplinarepo.sterge(id_disciplina)

    def update(self, id_disciplina: str, nume: str, profesor: str):
        disciplina = Disciplina(id_disciplina, nume, profesor)
        self.disciplinavalidator.valideaza(disciplina)
        self.disciplinarepo.modifica(disciplina)

    def get_all(self):
        return self.disciplinarepo.read()

    def get_by_id(self, id_disciplina: str):
        return self.disciplinarepo.read(id_disciplina)
