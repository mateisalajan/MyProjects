
from service.DisciplinaService import DisciplinaService
from service.StudentService import StudentService


class Console:

    def __init__(self, student_service: StudentService, disciplina_service: DisciplinaService):
        self.student_service = student_service
        self.disciplina_service = disciplina_service

    def show_menu(self):
        print("1.CRUD student")
        print("2.CRUD disciplina")
        print("x.Iesire")

    def show_menu_student(self):
        print("1.Adauga student")
        print("2.Sterge student")
        print("3.Modifica student")
        print("4.Cauta student")
        print("5.Show all studenti")

    def show_menu_disciplina(self):
        print("1.Adauga disciplina")
        print("2.Sterge disciplina")
        print("3.Modifica disciplina")
        print("4.Cauta disciplina")
        print("5.Show all discipline")

    def run_menu(self):
        while True:
            self.show_menu()
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.run_menu_student()
            elif optiune == "2":
                self.run_menu_disciplina()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita!")


    def run_menu_student(self):
        while True:
            self.show_menu_student()
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.ui_adauga_student()
            elif optiune == "2":
                self.ui_sterge_student()
            elif optiune == "3":
                self.ui_modifica_student()
            elif optiune == "4":
                self.ui_cauta_student()
            elif optiune == "5":
                self.ui_show_all_student()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita!")

    def ui_adauga_student(self):
        try:
            id_student = input("Dati id-ul studentului: ")
            nume = input("Dati numele studentului: ")
            self.student_service.add(id_student, nume)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_sterge_student(self):
        try:
            id_student = input("Dati id-ul studentului pe care doriti sa il stergeti: ")
            self.student_service.delete(id_student)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_modifica_student(self):
        try:
            id_student = input("Dati id-ul studentului pe care doriti sa il modificati: ")
            nume = input("Dati noul nume al studentului: ")
            self.student_service.update(id_student, nume)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_cauta_student(self):
        try:
            id_student = input("Dati id-ul studentului pe care il cautati: ")
            self.student_service.get_by_id(id_student)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_show_all_student(self):
        for student in self.student_service.get_all():
            print(student)

    def run_menu_disciplina(self):
        while True:
            self.show_menu_disciplina()
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.ui_adauga_disciplina()
            elif optiune == "2":
                self.ui_sterge_disciplina()
            elif optiune == "3":
                self.ui_modifica_disciplina()
            elif optiune == "4":
                self.ui_cauta_disciplina()
            elif optiune == "5":
                self.ui_show_all_disciplina()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita!")

    def ui_adauga_disciplina(self):
        try:
            id_disciplina = input("Dati id-ul disciplinei: ")
            nume = input("Dati numele disciplinei: ")
            profesor = input("Dati profesorul disciplinei: ")
            self.disciplina_service.add(id_disciplina, nume, profesor)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_sterge_disciplina(self):
        try:
            id_disciplina = input("Dati id-ul disciplinei pe care doriti sa o stergeti: ")
            self.disciplina_service.delete(id_disciplina)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_modifica_disciplina(self):
        try:
            id_disciplina = input("Dati id-ul disciplinei pe care doriti sa o modificati: ")
            nume = input("Dati noul nume al disciplinei: ")
            profesor = input("Dati noul profesor al disciplinei: ")
            self.disciplina_service.update(id_disciplina, nume, profesor)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_cauta_disciplina(self):
        try:
            id_disciplina = input("Dati id-ul disciplinei pe care o cautati: ")
            self.disciplina_service.get_by_id(id_disciplina)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_show_all_disciplina(self):
        for disciplina in self.disciplina_service.get_all():
            print(disciplina)
