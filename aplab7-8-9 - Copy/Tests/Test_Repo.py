from Domain.Client import Client
from Domain.Film import Film
from Repository.Client_Repo import ClientRepo
from Repository.Film_Repo import FilmRepo


def test_film_repo():
    repo = FilmRepo()
    repo.adauga(Film("1", "Titanic", "drama", 30))
    repo.adauga(Film("2", "Dune", "actiune", 35))
    assert len(repo.read()) == 2
    assert repo.read("1").titlu == "Titanic"
    assert repo.read("1").gen == "drama"
    assert repo.read("1").pret == 30
    repo.modifica(Film("1", "Mask", "thriller", 19.99))
    assert len(repo.read()) == 2
    assert repo.read("1").titlu == "Mask"
    assert repo.read("1").gen == "thriller"
    assert repo.read("1").pret == 19.99
    repo.sterge("1")
    assert len(repo.read()) == 1
    repo.sterge("2")
    assert len(repo.read()) == 0


def test_client_repo():
    repo = ClientRepo()
    repo.adauga(Client("1", "Mihai", "31234", []))
    repo.adauga(Client("2", "Andrei", "90261", []))
    assert len(repo.read()) == 2
    assert repo.read("1").nume_client == "Mihai"
    assert repo.read("1").CNP == "31234"
    repo.modifica(Client("1", "Ion", "55555", []))
    assert len(repo.read()) == 2
    assert repo.read("1").nume_client == "Ion"
    assert repo.read("1").CNP == "55555"
    repo.sterge("1")
    assert len(repo.read()) == 1
    repo.sterge("2")
    assert len(repo.read()) == 0


def test_all_repo():
    test_client_repo()
    test_film_repo()
