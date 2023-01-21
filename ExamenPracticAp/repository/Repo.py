import jsonpickle

from domain.Cafea import Cafea
from errors.IdError import DuplicateIdError


class Repo:
    def __init__(self, filename):
        self.filename = filename
        self.cafele = {}

    def __readFile(self):
        try:
            with open(self.filename, "r") as f:
                file = f.read()
                return jsonpickle.loads(file)
        except Exception:
            return {}

    def __writeFile(self):
        with open(self.filename, "w") as f:
            f.write(jsonpickle.dumps(self.cafele, indent=2))

    def read(self, id_cafea=None):
        """
        citeste o entitate
        :param id_cafea: id-ul entitatii
        :return:
        """
        self.cafele = self.__readFile()
        if id_cafea is None:
            return list(self.cafele.values())
        if id_cafea in self.cafele:
            return self.cafele[id_cafea]
        else:
            return None

    def adauga(self, cafea: Cafea):
        """
        adauga o entitate in repository
        :param cafea:cafeaua de adaugat
        :return:
        """
        self.cafele = self.__readFile()
        self.cafele[cafea.id_cafea] = cafea
        self.__writeFile()
