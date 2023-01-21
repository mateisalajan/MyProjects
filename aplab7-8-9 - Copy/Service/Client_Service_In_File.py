import operator
from collections import Counter
from typing import List
from Domain.Client import Client
from Domain.Client_Validator import ClientValidator
from Exceptions.Id_Error import NoSuchIdError
from Repository.Client_Repo_In_File import RepositoryJsonC
from Repository.Film_Repo_In_File import RepositoryJsonF
import numpy


class ClientServiceInFile:

    def __init__(self, client_repository: RepositoryJsonC, film_repository: RepositoryJsonF,
                 client_validator: ClientValidator):
        self.client_repository = client_repository
        self.film_repository = film_repository
        self.client_validator = client_validator

    def adauga_client(self, id_client: str, nume_client: str, CNP: str, lista_filme: list) -> None:
        """
        Adauga un client
        :param id_client: id-ul clientului
        :param nume_client: numele clientului
        :param CNP: CNP-ul clientului
        :return: None
        """
        client = Client(id_client, nume_client, CNP, lista_filme)
        self.client_validator.valideaza(client)
        self.client_repository.adauga(client)

    def modifica_client(self, id_client: str, nume_client: str, CNP: str, lista_filme: list) -> None:
        """
        Modifica un client
        :param id_client: id-ul clientului
        :param nume_client: numele clientului
        :param CNP: CNP-ul clientului
        :return: None
        """
        client = Client(id_client, nume_client, CNP, lista_filme)
        self.client_validator.valideaza(client)
        self.client_repository.modifica(client)

    def sterge_client(self, id_client: str) -> None:
        """
        Sterge un client dupa id
        :param id_client: id-ul clientului pe care dorim sa-l stergem
        :return: None
        """
        self.client_repository.sterge(id_client)

    def get_all(self) -> List[Client]:
        """
        Returneaza o lista cu toti clientii
        :return: o lista cu toti clientii
        """
        return self.client_repository.read()

    def get_by_id(self, id_client=None) -> [Client]:
        """
        Returneaza clientul cu id-ul specificat
        :return: clientul cu id-ul specificat
        """
        return self.client_repository.read(id_client)

    def inchiriere(self, id_client: str, id_film: str) -> None:
        """
        adauga un film in lista de filme inchiriate
        :param id_client:id-ul clientului
        :param id_film:id-ul filmului de inchiriat
        :return:
        """
        if self.client_repository.read(id_client) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        if self.film_repository.read(id_film) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        client = self.client_repository.read(id_client)
        a = len(client.lista_filme)
        film = self.film_repository.read(id_film)
        client.lista_filme.append(film)
        client2 = self.client_repository.read(id_client)
        b = len(client2.lista_filme)
        if a < b:
            print("Film inchiriat!")

    def returnare(self, id_client: str, id_film: str) -> None:
        """
        sterge un film in lista de filme inchiriate
        :param id_client:id-ul clientului
        :param id_film: id-ul filmului de returnat
        :return:
        """
        if self.client_repository.read(id_client) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        if self.film_repository.read(id_film) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        client = self.client_repository.read(id_client)
        a = len(client.lista_filme)
        film = self.film_repository.read(id_film)
        client.lista_filme.remove(film)
        client2 = self.client_repository.read(id_client)
        b = len(client2.lista_filme)
        if a > b:
            print("Film returnat!")

    def ordonare_dupa_nume(self) -> List:
        """
        Ordoneaza clientii crescator dupa nume
        :return:lista cu clientii ordonati crescator dupa nume
        """
        lst = []
        for x in self.client_repository.read():
            if len(x.lista_filme) > 0:
                lst.append(x)
        return sorted(lst, key=lambda client: client.nume_client, reverse=False)

    def ordonare_dupa_nr_filme(self) -> List:
        """
        Ordoneaza clientii crescator dupa nr de filme inchiriate
        :return:lista cu clientii ordonati crescator dupa nr de filme inchiriate
        """
        lst = []
        for x in self.client_repository.read():
            if len(x.lista_filme) > 0:
                lst.append(x)
        return sorted(lst, key=lambda client: len(client.lista_filme), reverse=False)

    def cele_mai_inchiriate_filme(self):
        """
        Calculeaza cele mai inchiriate filme
        :return: un dictionar cu nr de aparitii al tuturor filmelor inchiriate
        """
        lst = []
        for x in self.client_repository.read():
            for y in x.lista_filme:
                lst.append(y.id_film)
        occurence_count = Counter(lst)
        return occurence_count

    def clientii_cu_cele_mai_inchiriate_filme(self):
        dict_nou = {}
        dict_nou2 = {}
        for x in self.client_repository.read():
            dict_nou[x.id_client] = len(x.lista_filme)
        sorted_dict = sorted(dict_nou.items(), key=operator.itemgetter(1),  reverse=True)
        lst1 = numpy.array(sorted_dict)
        lst2 = lst1[lst1 > numpy.percentile(lst1, 30)]
        for x in lst2:
            nume = self.get_by_id(x).nume_client
            nr_filme = len(self.get_by_id(x).lista_filme)
            dict_nou2[nume] = nr_filme
        return dict_nou2

    def check(self):
        return
