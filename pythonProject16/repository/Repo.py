from domain.Cafea import Cafea
from errors.IdError import DuplicateIdError
import jsonpickle


class Repo:
    def __init__(self):
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
            f.write(jsonpickle.dumps(self.filme, indent=2))

    def read(self, id_cafea=None):
        if id_cafea is None:
            return list(self.cafele.values())
        if id_cafea in self.cafele:
            return self.cafele[id_cafea]
        else:
            return None

    def adauga(self, cafea: Cafea):
        if self.read(cafea.id_cafea) is not None:
            raise DuplicateIdError("Exista deja o entitate cu id-ul dat!")
        self.cafele[cafea.id_cafea] = cafea
