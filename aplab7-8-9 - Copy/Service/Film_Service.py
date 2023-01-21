from typing import List
from Domain.Film import Film
from Domain.Film_Validator import FilmValidator
from Repository.Film_Repo import FilmRepo


class FilmService:

    def __init__(self, film_repository: FilmRepo, film_validator: FilmValidator):
        self.film_repository = film_repository
        self.film_validator = film_validator

    def adauga_film(self, id_film: str, titlu: str, gen: str, pret: float) -> None:
        """
        Adauga un film
        :param id_film: id-ul filmului
        :param titlu: titlul filmului
        :param gen: genul filmului
        :param pret: pretul biletului
        :return: None
        """
        film = Film(id_film, titlu, gen, pret)
        self.film_validator.valideaza(film)
        self.film_repository.adauga(film)

    def modifica_film(self, id_film: str, titlu: str, gen: str, pret: float) -> None:
        """
        Modifica un film existent
        :param id_film: id-ul filmului
        :param titlu: titlul filmului
        :param gen: genul filmului
        :param pret: pretul biletului
        :return: None
        """
        film = Film(id_film, titlu, gen, pret)
        self.film_validator.valideaza(film)
        self.film_repository.modifica(film)

    def sterge_film(self, id_film: str) -> None:
        """
        Sterge un film dupa id
        :param id_film: id-ul filmului pe care dorim sa-l stergem
        :return: None
        """
        self.film_repository.sterge(id_film)

    def get_all(self) -> List[Film]:
        """
        Returneaza o lista cu toate filmele
        :return: o lista cu toate filmele
        """
        return self.film_repository.read()

    def get_by_id(self, id_film=None) -> [Film]:
        """
        Returneaza filmul cu id-ul specificat
        :return: filmul cu id-ul specificat
        """
        return self.film_repository.read(id_film)
