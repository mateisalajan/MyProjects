
from Domain.Client import Client
from Exceptions.Id_Error import DuplicateIdError, NoSuchIdError
from typing import Type, Union, Optional, List


class ClientRepo:
    def __init__(self):
        self.clienti = {}

    def read(self, id_client=None) -> Type[Union[Optional[Client], List[Client]]]:
        if id_client is None:
            return list(self.clienti.values())

        if id_client in self.clienti:
            return self.clienti[id_client]
        else:
            return None

    def adauga(self, client: Client) -> None:
        if self.read(client.id_client) is not None:
            raise DuplicateIdError("Exista deja o entitate cu id-ul dat!")
        self.clienti[client.id_client] = client

    def sterge(self, id_client: str) -> None:
        if self.read(id_client) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        del self.clienti[id_client]

    def modifica(self, client: Client) -> None:
        if self.read(client.id_client) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        self.clienti[client.id_client] = client
