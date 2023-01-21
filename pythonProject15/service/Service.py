from domain.Cafea import Cafea
from domain.CafeaValidator import CafeaValidator
from repository.Repository import Repo


class Service:
    def __init__(self, repo: Repo, validator: CafeaValidator):
        self.repo =repo
        self.validator = validator

    def add(self, nume: str, tara_de_origine: str, pret: float):
        cafea = Cafea(nume, tara_de_origine, pret)
        self.validator.valideaza(cafea)
        self.repo.adauga(cafea)

    def sortare(self):
        cafele = self.getAll()
        return sorted(cafele, key=lambda cafea: (cafea.tara_de_origine, cafea.pret), reverse=False)

    def filtrarea(self, tara: str, pret: float):
        cafele = self.getAll()
        if tara == '':
            return [cafea for cafea in cafele if cafea.pret <= pret]
        elif pret == 0:
            return [cafea for cafea in cafele if cafea.tara_de_origine == tara]
        elif tara == '' and pret == 0:
            print("Nu exista nici o astfel de cafea!")
        else:
            return [cafea for cafea in cafele if cafea.tara_de_origine == tara and cafea.pret <= pret]

    def getAll(self):
        return self.repo.read()
