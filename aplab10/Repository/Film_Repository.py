from typing import Type, Union, Optional, List

import jsonpickle

from Domain.Film import Film
from Exceptions.Id_Error import DuplicateIdError, NoSuchIdError


class RepositoryJsonF:
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.filme = {}

    def __readFile(self):
        try:
            with open(self.filename, "r") as f:
                file = f.read()
                return jsonpickle.loads(file)
        except Exception:
            return {}

    def __writeFile(self):
        with open(self.filename, "w") as f:
            f.write(jsonpickle.dumps(self.filme, indent=2))

    def read(self, id_film=None) -> Type[Union[Optional[Film], List[Film]]]:
        self.filme = self.__readFile()
        if id_film is None:
            return list(self.filme.values())

        if id_film in self.filme:
            return self.filme[id_film]
        else:
            return None

    def adauga(self, film: Film) -> None:
        self.filme = self.__readFile()
        if self.read(film.id_film) is not None:
            raise DuplicateIdError("Exista deja o entitate cu id-ul dat!")
        self.filme[film.id_film] = film
        self.__writeFile()

    def sterge(self, id_film: str) -> None:
        self.filme = self.__readFile()
        if self.read(id_film) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        del self.filme[id_film]
        self.__writeFile()

    def modifica(self, film: Film) -> None:
        self.filme = self.__readFile()
        if self.read(film.id_film) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        self.filme[film.id_film] = film
        self.__writeFile()
