
from domain.Entitate import Entitate


class User(Entitate):
    def __init__(self, nume: str, varsta: int):
        super().__init__()
        self.id_user = self.id_entitate
        self.nume = nume
        self.varsta = varsta

    @property
    def user_nume(self):
        return self.nume

    @user_nume.setter
    def user_nume(self, n: str):
        if len(n) == 0:
            raise ValueError("Numele nu poate fi un string gol!")
        self.nume = n

    @property
    def user_varsta(self):
        return self.varsta

    @user_varsta.setter
    def user_varsta(self, v: int):
        if v < 0:
            raise ValueError("Varsta nu poate fi mai mica sau egala cu 0!")
        self.varsta = v

    def __repr__(self):
        return "{}(id={}, nume={}, varsta={})".format(self.__class__.__name__,
                                                      self.id_entitate, self.nume, self.varsta)
