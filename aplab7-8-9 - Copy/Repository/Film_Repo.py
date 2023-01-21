
from Domain.Film import Film
from Exceptions.Id_Error import DuplicateIdError, NoSuchIdError
from typing import Type, Union, Optional, List


class FilmRepo:
    def __init__(self):
        self.filme = {}

    def read(self, id_film=None) -> Type[Union[Optional[Film], List[Film]]]:
        if id_film is None:
            return list(self.filme.values())

        if id_film in self.filme:
            return self.filme[id_film]
        else:
            return None

    def adauga(self, film: Film) -> None:
        if self.read(film.id_film) is not None:
            raise DuplicateIdError("Exista deja o entitate cu id-ul dat!")
        self.filme[film.id_film] = film

    def sterge(self, id_film: str) -> None:
        if self.read(id_film) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        del self.filme[id_film]

    def modifica(self, film: Film) -> None:
        if self.read(film.id_film) is None:
            raise NoSuchIdError("Nu exista nicio entitate cu id-ul dat!")
        self.filme[film.id_film] = film
