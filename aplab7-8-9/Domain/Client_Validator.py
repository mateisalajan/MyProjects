from Domain.Client import Client
from Exceptions.Client_Error import ClientError


class ClientValidator:
    """
    Clasa care valideaza un card client
    """

    @staticmethod
    def valideaza(client: Client):
        if len(client.CNP) != 13:
            raise ClientError("CNP-ul trebuie sa aiba exact 13 caractere !")
