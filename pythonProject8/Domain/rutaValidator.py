from Domain.ruta import Ruta


class RutaValidator:
    def valideaza(self, ruta: Ruta):
        erori = []
        if ruta.idOrasPornire == ruta.idOrasOprire:
            erori.append("Id-urile oraselor de pornire & oprire trebuie sa fie distincte!")
        if ruta.dusIntors != True and ruta.dusIntors != False:
            erori.append("'dus-intors' poate fi doar True sau False!")
        if erori:
            raise ValueError(erori)
