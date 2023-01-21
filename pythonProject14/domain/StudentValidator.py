from dataclasses import dataclass

from domain.Student import Student
from exceptions.StudentError import StudentError


@dataclass
class StudentValidator:

    @staticmethod
    def valideaza(student: Student):
        if len(student.id_student) == 0:
            raise StudentError("Id-ul nu poate fi null")

