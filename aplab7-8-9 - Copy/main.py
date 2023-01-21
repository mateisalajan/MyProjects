from Domain.Client_Validator import ClientValidator
from Domain.Film_Validator import FilmValidator
from Repository.Client_Repo import ClientRepo
from Repository.Film_Repo import FilmRepo
from Repository.Client_Repo_In_File import RepositoryJsonC
from Repository.Film_Repo_In_File import RepositoryJsonF
from Service.Client_Service import ClientService
from Service.Film_Service_In_File import FilmServiceInFile
from Service.Client_Service_In_File import ClientServiceInFile
from Service.Film_Service import FilmService
from Tests.Test_All import test_all
from UI.Console import Console
from UI.Console_In_File import ConsoleInFile


def main():

    test_all()
    while True:
        print("1. Repository in memory")
        print("2. Repository in file")
        print("x. Iesire")
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            film_repository = FilmRepo()
            film_validator = FilmValidator()
            film_service = FilmService(film_repository, film_validator)

            client_repository = ClientRepo()
            client_validator = ClientValidator()
            client_service = ClientService(client_repository, film_repository, client_validator)

            consola = Console(film_service, client_service)
            consola.run_menu()
        elif optiune == "2":
            filmrepository = RepositoryJsonF("filme.json")
            filmvalidator = FilmValidator()
            filmservice = FilmServiceInFile(filmrepository, filmvalidator)

            clientrepository = RepositoryJsonC("clienti.json")
            clientvalidator = ClientValidator()
            clientservice = ClientServiceInFile(clientrepository, filmrepository, clientvalidator)

            consola = ConsoleInFile(filmservice, clientservice)
            consola.run_menu()
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati")


if __name__ == "__main__":
    main()
