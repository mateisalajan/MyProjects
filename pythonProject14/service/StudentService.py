from domain.Student import Student
from domain.StudentValidator import StudentValidator
from repository.StudentRepo import StudentRepo


class StudentService:
    def __init__(self, studentrepo: StudentRepo, studentvalidator: StudentValidator):
        self.studentrepo = studentrepo
        self.studentvalidator = studentvalidator

    def add(self, id_student: str, nume: str):
        student = Student(id_student, nume)
        self.studentvalidator.valideaza(student)
        self.studentrepo.adauga(student)

    def delete(self, id_student: str):
        self.studentrepo.sterge(id_student)

    def update(self, id_student: str, nume: str):
        student = Student(id_student, nume)
        self.studentvalidator.valideaza(student)
        self.studentrepo.modifica(student)

    def get_all(self):
        return self.studentrepo.read()

    def get_by_id(self, id_student: str):
        return self.studentrepo.read(id_student)
