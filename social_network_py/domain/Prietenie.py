
from domain.Entitate import Entitate


class Prietenie(Entitate):
    def __init__(self, id_user1: int, id_user2: int):
        super().__init__()
        self.id_user1 = id_user1
        self.id_user2 = id_user2

    @property
    def prietenie_id_user1(self):
        return self.id_user1

    @prietenie_id_user1.setter
    def prietenie_id_user1(self, id1: int):
        self.id_user1 = id1

    @property
    def prietenie_id_user2(self):
        return self.id_user2

    @prietenie_id_user2.setter
    def prietenie_id_user2(self, id2: int):
        self.id_user2 = id2

    def __repr__(self):
        return "{}(id={}, id_user1={}, id_user2={})".format(self.__class__.__name__, self.id_entitate,
                                                            self.id_user1, self.id_user2)
