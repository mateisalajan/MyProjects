from domain.DisciplinaValidator import DisciplinaValidator
from domain.StudentValidator import StudentValidator
from repository.DisciplinaRepo import DisciplinaRepo
from repository.StudentRepo import StudentRepo
from service.DisciplinaService import DisciplinaService
from service.StudentService import StudentService
from ui.Console import Console


def main():
    studentrepo = StudentRepo("studenti")
    studentvalidator = StudentValidator()
    disciplinarepo = DisciplinaRepo("discipline")
    disciplinavalidator = DisciplinaValidator()

    student_service = StudentService(studentrepo, studentvalidator)
    disciplina_service = DisciplinaService(disciplinarepo, disciplinavalidator)

    console = Console(student_service, disciplina_service)
    console.run_menu()


if __name__ == '__main__':
    main()
