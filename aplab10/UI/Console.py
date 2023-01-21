
from Service.Client_Service import ClientService
from Service.Film_Service import FilmService


class Console:

    def __init__(self, film_service: FilmService, client_service: ClientService):
        self.film_service = film_service
        self.client_service = client_service

    def run_menu(self):
        while True:
            print("1. CRUD client")
            print("2. CRUD film")
            print("3.Inchiriere film")
            print("4.Returnare film")
            print("5.Clientii ordonati crescator dupa nume")
            print("6.Clientii ordonati crescator dupa nr de filem inchiriate")
            print("7.Cele mai inchiriat filme")
            print("8.Primi 30% clienti cu cele mai multe filme")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.ui_run_crud_client_menu()
            elif optiune == "2":
                self.ui_run_crud_film_menu()
            elif optiune == "3":
                self.ui_ichiriaza_film()
            elif optiune == "4":
                self.ui_returneaza_film()
            elif optiune == "5":
                self.ui_ordonare_dupa_nume()
            elif optiune == "6":
                self.ui_ordonare_dupa_nr_filme()
            elif optiune == "7":
                self.ui_cele_mai_inchiriate_filme()
            elif optiune == "8":
                self.ui_clientii_cu_cele_mai_inchiriate_filme()
            elif optiune.lower() == "x":
                break
            else:
                print("Optiune gresita! Reincercati :)")

    def ui_run_crud_film_menu(self):
        while True:
            print("1. Adauga film")
            print("2. Sterge film")
            print("3. Modifica film")
            print("4. Cautare film")
            print("a. Afiseaza filme")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.ui_adauga_film()
            elif optiune == "2":
                self.ui_sterge_film()
            elif optiune == "3":
                self.ui_modifica_film()
            elif optiune == "4":
                self.ui_cauta_film()
            elif optiune.lower() == "a":
                self.ui_showall_filme()
            elif optiune.lower() == "x":
                break
            else:
                print("Optiune gresita! Reincercati")

    def ui_adauga_film(self):
        try:
            id_film = input("Dati id-ul filmului: ")
            titlu = input("Dati titlul filmului: ")
            gen = input("Dati genul filmului: ")
            pret = float(input("Dati pretul filmului: "))
            self.film_service.adauga_film(id_film, titlu, gen, pret)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_sterge_film(self):
        try:
            id_film = input("Dati id-ul filmului pe care doriti sa-l stergeti: ")
            self.film_service.sterge_film(id_film)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_modifica_film(self):
        try:
            id_film = input("Dati id-ul filmului pe care doriti sa-l modificati: ")
            titlu = input("Dati noul titlu al filmului: ")
            gen = input("Dati noul gen al filmului: ")
            pret = float(input("Dati noul pret al filmului: "))
            self.film_service.modifica_film(id_film, titlu, gen, pret)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def ui_showall_filme(self):
        for film in self.film_service.get_all():
            print(film)

    def ui_cauta_film(self):
        try:
            id_film = input("Dati id-ul filmului pe care doriti sa-l cautati: ")
            print(self.film_service.get_by_id(id_film))
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_run_crud_client_menu(self):
        while True:
            print("1. Adauga client")
            print("2. Sterge client")
            print("3. Modifica client")
            print("4. Cautare client")
            print("a. Afiseaza clienti")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.ui_adauga_client()
            elif optiune == "2":
                self.ui_sterge_client()
            elif optiune == "3":
                self.ui_modifica_client()
            elif optiune == "4":
                self.ui_cauta_client()
            elif optiune.lower() == "a":
                self.ui_showall_clienti()
            elif optiune.lower() == "x":
                break
            else:
                print("Optiune gresita! Reincercati")

    def ui_adauga_client(self):
        try:
            id_client = input("Dati id-ul clientului: ")
            nume = input("Dati numele clientului: ")
            CNP = input("Dati CNP-ul: ")
            lista_filme = []
            self.client_service.adauga_client(id_client, nume, CNP, lista_filme)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def ui_sterge_client(self):
        try:
            id_client = input("Dati id-ul clientului pe care doriti sa-l stergeti: ")
            self.client_service.sterge_client(id_client)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_modifica_client(self):
        try:
            id_client = input("Dati id-ul clientului pe care doriti sa-l modificati: ")
            nume = input("Dati noul nume al clientului: ")
            CNP = input("Dati noul CNP: ")
            lista_filme = []
            self.client_service.modifica_client(id_client, nume, CNP, lista_filme)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def ui_showall_clienti(self):
        for client in self.client_service.get_all():
            print(client)

    def ui_cauta_client(self):
        try:
            id_client = input("Dati id-ul clientului pe care doriti sa-l cautati: ")
            print(self.client_service.get_by_id(id_client))
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_ichiriaza_film(self):
        id_client = input("Dati id-ul clientului care doriti sa inchirieze filmul: ")
        id_film = input("Dati id-ul filmului pe care doriti sa il inchiriati: ")
        print(self.client_service.inchiriere(id_client, id_film))

    def ui_returneaza_film(self):
        id_client = input("Dati id-ul clientului care doriti sa returneze un film: ")
        id_film = input("Dati id-ul filmului pe care doriti sa il returnati: ")
        print(self.client_service.returnare(id_client, id_film))

    def ui_ordonare_dupa_nume(self):
        for x in self.client_service.ordonare_dupa_nume():
            print(x)

    def ui_ordonare_dupa_nr_filme(self):
        for x in self.client_service.ordonare_dupa_nr_filme():
            print(x)

    def ui_cele_mai_inchiriate_filme(self):
        print(self.client_service.cele_mai_inchiriate_filme())

    def ui_clientii_cu_cele_mai_inchiriate_filme(self):
        print(self.client_service.clientii_cu_cele_mai_inchiriate_filme())
