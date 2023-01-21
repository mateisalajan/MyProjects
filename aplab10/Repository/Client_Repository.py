from typing import Type, Union, Optional, List

import jsonpickle

from Domain.Client import Client
from Exceptions.Id_Error import DuplicateIdError, NoSuchIdError


class RepositoryJsonC:
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.clienti = {}

    def __readFile(self):
        try:
            with open(self.filename, "r") as f:
                file = f.read()
                return jsonpickle.loads(file)
        except Exception:
            return {}

    def __writeFile(self):
        with open(self.filename, "w") as f:
            f.write(jsonpickle.dumps(self.clienti, indent=2))

    def read(self, id_client=None) -> Type[Union[Optional[Client], List[Client]]]:
        self.clienti = self.__readFile()
        if id_client is None:
            return list(self.clienti.values())

        if id_client in self.clienti:
            return self.clienti[id_client]
        else:
            return None

    def adauga(self, client: Client) -> None:
        self.clienti = self.__readFile()
        if self.read(client.id_client) is not None:
            raise DuplicateIdError("Exista deja o entitate cu id-ul dat!")
        self.clienti[client.id_client] = client
        self.__writeFile()

    def sterge(self, id_client: str) -> None:
        self.clienti = self.__readFile()
        if self.read(id_client) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        del self.clienti[id_client]
        self.__writeFile()

    def modifica(self, client: Client) -> None:
        self.clienti = self.__readFile()
        if self.read(client.id_client) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        self.clienti[client.id_client] = client
        self.__writeFile()
