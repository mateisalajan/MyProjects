import jsonpickle
from domain.Disciplina import Disciplina
from exceptions.IdError import NoSuchIdError,DuplicateError

class DisciplinaRepo:
    def __init__(self, filename: str):
        self.filename = filename
        self.discipline = {}

    def __readfile(self):
        try:
            with open(self.filename, "r") as f:
                file = f.read()
                return jsonpickle.loads(file)
        except Exception:
            return {}

    def __writefile(self):
        with open(self.filename, "w") as f:
            f.write(jsonpickle.dumps(self.discipline, indent=2))

    def read(self, id_disciplina=None):
        self.discipline = self.__readfile()
        if id_disciplina is None:
            return list(self.discipline.values())
        if id_disciplina in self.discipline:
            return self.discipline[id_disciplina]
        else:
            return None

    def adauga(self, disciplina: Disciplina):
        self.discipline = self.__readfile()
        if self.read(disciplina.id_disciplina) is not None:
            raise DuplicateError("Exista deja o discplina cu acel id!")
        self.discipline[disciplina.id_disciplina] = disciplina
        self.__writefile()

    def sterge(self, id_disciplina=None):
        self.discipline = self.__readfile()
        if self.read(id_disciplina) is None:
            raise NoSuchIdError("Nu exista nici o discplina cu acel id!")
        del self.discipline[id_disciplina]
        self.__writefile()

    def modifica(self, disciplina: Disciplina):
        self.discipline = self.__readfile()
        if self.read(disciplina.id_disciplina) is None:
            raise NoSuchIdError("Nu exista nici o discplina cu acel id!")
        self.discipline[disciplina.id_disciplina] = disciplina
        self.__writefile()
