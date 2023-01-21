from Domain.Client_Validator import ClientValidator
from Domain.Film_Validator import FilmValidator
from Repository.Client_Repo import ClientRepo
from Repository.Film_Repo import FilmRepo
from Service.Client_Service import ClientService
from Service.Film_Service import FilmService


def test_film_service():
    film_validator = FilmValidator()
    film_repository = FilmRepo()
    film_service = FilmService(film_repository, film_validator)
    film_service.adauga_film("1", "Titanic", "drama", 30)
    assert len(film_service.get_all()) == 1
    film_service.adauga_film("2", "Dune", "actiune", 35)
    assert len(film_service.get_all()) == 2
    film_service.modifica_film("1", "Mask", "thriller", 19.99)
    assert len(film_service.get_all()) == 2
    film_service.sterge_film("1")
    assert len(film_service.get_all()) == 1


def test_client_service():
    client_validator = ClientValidator()
    client_repository = ClientRepo()
    film_repository = FilmRepo()
    client_service = ClientService(client_repository, film_repository, client_validator)
    client_service.adauga_client("1", "Mihai", "31234", [])
    assert len(client_service.get_all()) == 1
    client_service.adauga_client("2", "Andrei", "90261", [])
    assert len(client_service.get_all()) == 2
    client_service.modifica_client("1", "Ion", "55555", [])
    assert len(client_service.get_all()) == 2
    client_service.sterge_client("1")
    assert len(client_service.get_all()) == 1


def test_all_service():
    test_client_service()
    test_film_service()
