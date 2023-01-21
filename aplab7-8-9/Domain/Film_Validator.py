from Domain.Film import Film
from Exceptions.Film_Error import FilmError


class FilmValidator:
    """
    Clasa care valideaza un film
    """

    @staticmethod
    def valideaza(film: Film):
        if film.pret < 0:
            raise FilmError("Pretul nu poate fi negativ !")