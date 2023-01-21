
from typing import Type, Union, Optional, List

import jsonpickle

from Domain.Client import Client
from Exceptions.Id_Error import DuplicateIdError, NoSuchIdError
from Repository.Client_Repo import ClientRepo


class RepositoryJsonC:
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.elems = {}

    def __readFile(self):
        try:
            with open(self.filename, "r") as f:
                file = f.read()
                return jsonpickle.loads(file)
        except Exception:
            return {}

    def __writeFile(self):
        with open(self.filename, "a") as f:
            f.write(jsonpickle.dumps(self.elems, indent=2))

    def read(self, id_client=None) -> Type[Union[Optional[Client], List[Client]]]:
        self.elems = self.__readFile()
        if id_client is None:
            return list(self.elems.values())

        if id_client in self.elems:
            return self.elems[id_client]
        else:
            return None

    def adauga(self, client: Client) -> None:
        self.elems = self.__readFile()
        if self.read(client.id_client) is not None:
            raise DuplicateIdError("Exista deja o entitate cu id-ul dat!")
        self.elems[client.id_client] = client
        self.__writeFile()

    def sterge(self, id_client: str) -> None:
        self.elems = self.__readFile()
        if self.read(id_client) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        del self.elems[id_client]
        self.__writeFile()

    def modifica(self, client: Client) -> None:
        self.elems = self.__readFile()
        if self.read(client.id_client) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        self.elems[client.id_client] = client
        self.__writeFile()
