from domain.Cafea import Cafea
from domain.CafeaValidator import CafeaValidator
from repository.Repo import Repo


class Service:
    def __init__(self, repo: Repo, valid: CafeaValidator):
        self.repo = repo
        self.valid = valid

    def add(self, id_cafea: int, nume: str, tara: str, pret: float):
        """
        adauga o entitate in service
        :param id_cafea: id-ul cafelei
        :param nume: numele cafelei
        :param tara: tara de origine a cafelei
        :param pret: pretul cafelei
        :return:
        """
        cafele = self.get_all()
        if any(cafea for cafea in cafele if cafea.nume == nume):
            raise ValueError("Numele trebuie sa fie unic")
        if any(cafea for cafea in cafele if cafea.id_cafea == id_cafea):
            raise ValueError("Id-ul trebuie sa fie unic")
        cafea = Cafea(id_cafea, nume, tara, pret)
        self.valid.valideaza(cafea)
        self.repo.adauga(cafea)

    def get_all(self):
        """
        returneaza toate cafelele
        :return: o lista cu toate cafelele
        """
        return self.repo.read()

    def get_cafea_tara(self, tara: str):
        """
        face o lista cu cafelele dintr-o anumita tara
        :param tara:
        :return: o lista filtrata dupa tara de origine
        """
        cafele = self.get_all()
        return [cafea for cafea in cafele if cafea.tara_de_origine == tara]



