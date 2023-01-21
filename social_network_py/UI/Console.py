from service.Prietenie_Srevice import PrietenieService
from service.User_Service import UserService


class Console:

    def __init__(self, user_service: UserService, prietenie_service: PrietenieService):
        self.user_service = user_service
        self.prietenie_service = prietenie_service

    def run_menu(self):
        while True:
            print("1. CRUD user")
            print("2. CRUD prietenie")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.ui_run_crud_user_menu()
            elif optiune == "2":
                self.ui_run_crud_prietenie_menu()
            elif optiune.lower() == "x":
                break
            else:
                print("Optiune gresita! Reincercati :)")

    def ui_run_crud_user_menu(self):
        while True:
            print("1. Adauga user")
            print("2. Sterge user")
            print("3. Modifica user")
            print("4. Cautare user")
            print("a. Afiseaza users")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.ui_adauga_user()
            elif optiune == "2":
                self.ui_sterge_user()
            elif optiune == "3":
                self.ui_modifica_user()
            elif optiune == "4":
                self.ui_cauta_user()
            elif optiune.lower() == "a":
                self.ui_showall_useri()
            elif optiune.lower() == "x":
                break
            else:
                print("Optiune gresita! Reincercati")

    def ui_adauga_user(self):
        try:
            nume = input("Dati numele user-ului: ")
            varsta = int(input("Dati varsta user-ului: "))
            self.user_service.adauga_user(nume, varsta)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_sterge_user(self):
        try:
            id_user = int(input("Dati id-ul user-ului pe care doriti sa-l stergeti: "))
            self.user_service.sterge_user(id_user)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_modifica_user(self):
        try:
            id_user = int(input("Dati id-ul user-ului pe care doriti sa-l modificati: "))
            nume = input("Dati noul nume al user-ului: ")
            varsta = int(input("Dati noua varsta a user-ului: "))
            self.user_service.modifica_user(id_user, nume, varsta)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def ui_showall_useri(self):
        for user in self.user_service.get_all():
            print(user)

    def ui_cauta_user(self):
        try:
            id_user = int(input("Dati id-ul user-ului pe care doriti sa-l cautati: "))
            print(self.user_service.get_by_id(id_user))
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_run_crud_prietenie_menu(self):
        while True:
            print("1. Adauga prietenie")
            print("2. Sterge prietenie")
            print("3. Cautare prietenie")
            print("a. Afiseaza prietenii")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.ui_adauga_prietenie()
            elif optiune == "2":
                self.ui_sterge_prietenie()
            elif optiune == "3":
                self.ui_cauta_prietenie()
            elif optiune.lower() == "a":
                self.ui_showall_prietenii()
            elif optiune.lower() == "x":
                break
            else:
                print("Optiune gresita! Reincercati")

    def ui_adauga_prietenie(self):
        try:
            id_user1 = int(input("Dati id-ul primului user: "))
            id_user2 = int(input("Dati id-ul celui de al doilea user: "))
            self.prietenie_service.adauga_prietenie(id_user1, id_user2)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_sterge_prietenie(self):
        try:
            id_prietenie = int(input("Dati id-ul prieteniei pe care doriti sa o stergeti: "))
            self.prietenie_service.sterge_prietenie(id_prietenie)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_showall_prietenii(self):
        for prietenie in self.prietenie_service.get_all():
            print(prietenie)

    def ui_cauta_prietenie(self):
        try:
            id_prietenie = int(input("Dati id-ul prieteniei pe care doriti sa o cautati: "))
            print(self.prietenie_service.get_by_id(id_prietenie))
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)
