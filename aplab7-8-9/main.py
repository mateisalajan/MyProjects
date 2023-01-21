from Domain.Client_Validator import ClientValidator
from Domain.Film_Validator import FilmValidator
from Repository.Repository_In_Memory import Repository
from Service.Client_Service import ClientService
from Service.Film_Service import FilmService
from UI.Console import Console


def main():

    film_repository = Repository()
    film_validator = FilmValidator()
    film_service = FilmService(film_repository, film_validator)

    client_repository = Repository()
    client_validator = ClientValidator()
    client_service = ClientService(client_repository, client_validator)

    consola = Console(film_service, client_service)
    consola.run_menu()


if __name__ == "__main__":
    main()
