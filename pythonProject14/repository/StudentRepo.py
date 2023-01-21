import jsonpickle

from domain.Student import Student
from exceptions.IdError import DuplicateError, NoSuchIdError


class StudentRepo:
    def __init__(self, filename: str):
        self.filename = filename
        self.studenti = {}

    def __readfile(self):
        try:
            with open(self.filename, "r") as f:
                file = f.read()
                return jsonpickle.loads(file)
        except Exception:
            return {}

    def __writefile(self):
        with open(self.filename, "w") as f:
            f.write(jsonpickle.dumps(self.studenti, indent=2))

    def read(self, id_student=None):
        self.studenti = self.__readfile()
        if id_student is None:
            return list(self.studenti.values())

        if id_student in self.studenti:
            return self.studenti[id_student]
        else:
            return None

    def adauga(self, student: Student):
        self.studenti = self.__readfile()
        if self.read(student.id_student) is not None:
            raise DuplicateError("Exista deja un student cu acel id!")
        self.studenti[student.id_student] = student
        self.__writefile()

    def sterge(self, id_student=None):
        self.studenti = self.__readfile()
        if self.read(id_student) is None:
            raise NoSuchIdError("Nu exista nici un student cu acel id!")
        del self.studenti[id_student]
        self.__writefile()

    def modifica(self, student: Student):
        self.studenti = self.__readfile()
        if self.read(student.id_student) is None:
            raise NoSuchIdError("Nu exista nici un student cu acel id!")
        self.studenti[student.id_student] = student
        self.__writefile()
