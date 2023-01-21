
from Service.Client_Service import ClientService
from Service.Film_Service import FilmService


class Console:

    def __init__(self, film_service: FilmService, client_service: ClientService):
        self.film_service = film_service
        self.client_service = client_service

    def run_menu(self):
        while True:
            print("1. CRUD film")
            print("2. CRUD client")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.ui_run_crud_film_menu()
            elif optiune == "2":
                self.ui_run_crud_client_menu()
            elif optiune.lower() == "x":
                break
            else:
                print("Optiune gresita! Reincercati :)")

    def ui_run_crud_film_menu(self):
        while True:
            print("1. Adauga film")
            print("2. Sterge film")
            print("3. Modifica film")
            print("a. Afiseaza filme")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.ui_adauga_film()
            elif optiune == "2":
                self.ui_sterge_film()
            elif optiune == "3":
                self.ui_modifica_film()
            elif optiune.lower() == "a":
                self.ui_showall_filme()
            elif optiune.lower() == "x":
                break
            else:
                print("Optiune gresita! Reincercati")

    def ui_adauga_film(self):
        try:
            id_entitate = int(input("Dati id-ul filmului: "))
            titlu = input("Dati titlul filmului: ")
            gen = input("Dati genul filmului: ")
            pret = float(input("Dati pretul filmului: "))
            self.film_service.adauga_film(id_entitate, titlu, gen, pret)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_sterge_film(self):
        try:
            id_entitate = int(input("Dati id-ul filmului pe care doriti sa-l stergeti: "))
            self.film_service.sterge_film(id_entitate)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_modifica_film(self):
        try:
            id_entitate = int(input("Dati id-ul filmului pe care doriti sa-l modificati: "))
            titlu = input("Dati noul titlu al filmului: ")
            gen = input("Dati noul gen al filmului: ")
            pret = float(input("Dati noul pret al filmului: "))
            self.film_service.modifica_film(id_entitate, titlu, gen, pret)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def ui_showall_filme(self):
        for film in self.film_service.get_all():
            print(film)

    def ui_run_crud_client_menu(self):
        while True:
            print("1. Adauga client")
            print("2. Sterge client")
            print("3. Modifica client")
            print("a. Afiseaza clienti")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.ui_adauga_client()
            elif optiune == "2":
                self.ui_sterge_client()
            elif optiune == "3":
                self.ui_modifica_client()
            elif optiune.lower() == "a":
                self.ui_showall_clienti()
            elif optiune.lower() == "x":
                break
            else:
                print("Optiune gresita! Reincercati")

    def ui_adauga_client(self):
        try:
            id_entitate = int(input("Dati id-ul clientului: "))
            nume = input("Dati numele clientului: ")
            CNP = input("Dati CNP-ul: ")
            self.client_service.adauga_client(id_entitate, nume, CNP)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def ui_sterge_client(self):
        try:
            id_entitate = int(input("Dati id-ul clientului pe care doriti sa-l stergeti: "))
            self.client_service.sterge_client(id_entitate)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_modifica_client(self):
        try:
            id_entitate = int(input("Dati id-ul clientului pe care doriti sa-l modificati: "))
            nume = input("Dati noul nume al clientului: ")
            CNP = input("Dati noul CNP: ")
            self.client_service.modifica_client(id_entitate, nume, CNP)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def ui_showall_clienti(self):
        for client in self.client_service.get_all():
            print(client)
