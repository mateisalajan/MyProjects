from Domain.Client import Client
from Exceptions.Client_Error import ClientError

from dataclasses import dataclass


@dataclass
class ClientValidator:
    """
    Clasa care valideaza un client
    """

    @staticmethod
    def valideaza(client: Client):
        if len(client.CNP) == 0:
            raise ClientError("CNP-ul nu poate avea 0 caractere !")
