from typing import List

from Domain.Inchiriere import Inchiriere
from Exceptions.Film_Error import FilmError
from Repository.Repository_In_Memory import Repository


class InchiriereService:

    def __init__(self, inchiriere_repository: Repository, client_repository: Repository, film_repository: Repository):
        self.inchiriere_repository = inchiriere_repository
        self.client_repository = client_repository
        self.film_repository = film_repository

    def adauga_inchiriere(self, id_inchiriere: int, id_client: int, id_film: int) -> None:
        """
        Adauga o inchiriere
        :param id_inchiriere: id-ul inchirierii
        :param id_film: id-ul filmului
        :param id_client: id-ul clientului
        :return: None
        """
        film = self.film_repository.read(id_film)
        if self.film_repository.read(film.idEntitate) is None:
            raise FilmError("Nu exista un film cu id-ul dat !")
        client = self.client_repository.read(id_client)
        inchiriere = Inchiriere(id_inchiriere, id_client, id_film)
        self.inchiriere_repository.adauga(inchiriere)

    def modifica_inchiriere(self, id_inchiriere: int, id_client: int, id_film: int) -> None:
        """
        Modifica un client
        :param id_client: id-ul clientului
        :param nume_client: numele clientului
        :param CNP: CNP-ul clientului
        :param lista_filme: lista cu filmele inchiriate de catre client
        :return: None
        """
        inchiriere = Inchiriere(id_inchiriere, id_client, id_film)
        self.client_repository.modifica(inchiriere)

    def sterge_inchiriere(self, id_inchiriere: int) -> None:
        """
        Sterge un client dupa id
        :param id_inchiriere: id-ul inchirierii pe care dorim sa o stergem
        :return: None
        """
        self.client_repository.sterge(id_inchiriere)

    def get_all(self) -> List[Inchiriere]:
        """
        Returneaza o lista cu toate inchirierile
        :return: o lista cu toate inchirierile
        """
        return self.client_repository.read()
