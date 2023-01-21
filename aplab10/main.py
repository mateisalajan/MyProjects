from Domain.Client_Validator import ClientValidator
from Domain.Film_Validator import FilmValidator
from Repository.Client_Repository import RepositoryJsonC
from Repository.Film_Repository import RepositoryJsonF
from Service.Client_Service import ClientService
from Service.Film_Service import FilmService
from UI.Console import Console


def main():

    filmrepository = RepositoryJsonF("filme.json")
    filmvalidator = FilmValidator()
    filmservice = FilmService(filmrepository, filmvalidator)

    clientrepository = RepositoryJsonC("clienti.json")
    clientvalidator = ClientValidator()
    clientservice = ClientService(clientrepository, filmrepository, clientvalidator)

    consola = Console(filmservice, clientservice)
    consola.run_menu()


if __name__ == "__main__":
    main()
