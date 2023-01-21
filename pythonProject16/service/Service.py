from domain.Cafea import Cafea
from domain.CafeaValidator import CafeaValidator
from repository.Repo import Repo


class Service:
    def __init__(self, repo: Repo, validator: CafeaValidator):
        self.repo = repo
        self.validator = validator

    def add(self, nume: str, tara: str, pret: float):
        cafele = self.get_all()
        if any(cafea.nume == nume for cafea in cafele):
            raise ValueError("Exista deja o cafenea cu acel nume!")
        cafea1 = Cafea(nume, tara, pret)
        self.validator.valideaza(cafea1)
        self.repo.adauga(cafea1)

    def get_all(self):
        return self.repo.read()

    def sortare(self):
        cafele = self.get_all()
        return sorted(cafele, key=lambda cafea: (cafea.tara_de_origine, cafea.pret), reverse=False)

    def filtrare(self, tara: str, pret: float):
        cafele = self.get_all()
        if tara == '' and pret == 0:
            print("Nu exista nici o astfel de cafea!")
        elif tara == '':
            return [cafea for cafea in cafele if cafea.pret <= pret]
        elif pret == 0:
            return [cafea for cafea in cafele if cafea.tara_de_origine == tara]
        else:
            return [cafea for cafea in cafele if cafea.tara_de_origine == tara and cafea.pret <= pret]
