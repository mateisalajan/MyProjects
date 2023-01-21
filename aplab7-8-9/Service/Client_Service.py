from typing import List
from Domain.Client import Client
from Domain.Client_Validator import ClientValidator
from Domain.entitate import Entitate
from Repository.Repository_In_Memory import Repository


class ClientService:

    def __init__(self, client_repository: Repository, client_validator: ClientValidator):
        self.client_repository = client_repository
        self.client_validator = client_validator

    def adauga_client(self, id_client: int, nume_client: str, CNP: str) -> None:
        """
        Adauga un client
        :param id_client: id-ul clientului
        :param nume_client: numele clientului
        :param CNP: CNP-ul clientului
        :return: None
        """
        client = Client(id_client, nume_client, CNP)
        self.client_validator.valideaza(client)
        self.client_repository.adauga(client)

    def modifica_client(self, id_client: int, nume_client: str, CNP: str) -> None:
        """
        Modifica un client
        :param id_client: id-ul clientului
        :param nume_client: numele clientului
        :param CNP: CNP-ul clientului
        :return: None
        """
        client = Client(id_client, nume_client, CNP)
        self.client_validator.valideaza(client)
        self.client_repository.modifica(client)

    def sterge_client(self, id_client: int) -> None:
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

    def cautare_nume_client(self, string_nume: str) -> List:
        """
        Returneaza o lista cu clientii in care se regaseste stringul citit
        :param string_nume: stringul dupa care cautam
        :return: o lista cu clientii in care se regaseste stringul citit
        """
        return list(filter(lambda x: x if string_nume in
                           x.getTextFomat() else None,
                           self.client_repository.read()))

    def get_by_id(self, id_client=None) -> [Entitate]:
        """
        Returneaza clientul cu id-ul specificat
        :return: clientul cu id-ul specificat
        """
        return self.client_repository.read(id_client)

    def add_film(self, film):
        self.lista_filme.append(film)

        return self.lista_filme
