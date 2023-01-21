from typing import List
from Domain.Film import Film
from Domain.Film_Validator import FilmValidator
from Repository.Repository_In_Memory import Repository


class FilmService:

    def __init__(self, film_repository: Repository, film_validator: FilmValidator):
        self.film_repository = film_repository
        self.film_validator = film_validator

    def adauga_film(self, id_film: int, titlu: str, gen: str, pret: float) -> None:
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

    def modifica_film(self, id_film: int, titlu: str, gen: str, pret: float) -> None:
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

    def sterge_film(self, id_film: int) -> None:
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

    def cautare_text_film(self, string_film: str) -> List:
        """
        Returneaza o lista cu filmele in care se regaseste stringul citit
        :param string_film: stringul dupa care cautam
        :return: o lista cu filmele in care se regaseste stringul citit
        """
        return list(filter(lambda x: x if string_film in
                           x.getTextFomat() else None,
                           self.film_repository.read()))
