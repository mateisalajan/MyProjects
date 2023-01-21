from domain.Cafenea import Cafenea
from domain.CafeneaValidator import CafeneaValidator
from repository.Repository import Repository


class CafeneaService:

    def __init__(self, cafenea_repository: Repository, cafenea_validator: CafeneaValidator):
        self.cafenea_repository = cafenea_repository
        self.cafenea_validator = cafenea_validator

    def adauga_cafenea(self, nume: str, tara_de_origine: str, pret: float) -> None:
        """
        adauga o cafenea
        :param nume: numele cafenelei
        :param tara_de_origine: tara de origine a cafenelei
        :param pret: pretul cafenelei
        :return:
        """
        cafenea = Cafenea(nume,tara_de_origine,pret)
        self.cafenea_validator.valideaza(cafenea)
        self.cafenea_repository.adauga(cafenea)

    def showAll(self):
        return self.cafenea_repository.read()

    def sortare(self):
        cafenele = self.cafenea_repository.read()
        return sorted(cafenele, key=lambda cafenea: (cafenea.tara_de_origine,cafenea.pret), reverse=False)

    def filtrare(self, tara: str, pret: float):
        cafenele = self.cafenea_repository.read()
        if tara == '':
            return [cafenea for cafenea in cafenele if cafenea.pret <= pret]
        elif pret == 0:
            return [cafenea for cafenea in cafenele if cafenea.tara_de_origine == tara]
        elif tara == '' and pret == 0:
            print("NU exisat nici o astfel de cafenea")
        else:
            return [cafenea for cafenea in cafenele if cafenea.tara_de_origine == tara and cafenea.pret <= pret]
