import jsonpickle

from Domain.ruta import Ruta
from Domain.rutaValidator import RutaValidator
from Repository.json_repository import JsonRepository


class RutaService:
    def __init__(self, rutaRepository: JsonRepository, localitateRepository: JsonRepository,
                 rutaValidator: RutaValidator):
        self.rutaRepository = rutaRepository
        self.rutaValidator = rutaValidator
        self.localitateRepository = localitateRepository

    def adauga(self, idRuta: str, idOrasPornire: str, idOrasOprire: str, pret: float, dusIntors: bool):
        '''
        adauga o ruta in multimea de rute
        :param idRuta: id-ul rutei
        :param idOrasPornire: id-ul orasului de pornire
        :param idOrasOprire:id-ul orasului de oprire
        :param pret: pretul rutei
        :param dusIntors: daca ruta este dus-intors sau nu
        :return:
        '''

        if self.localitateRepository.read(idOrasPornire) is None:
            raise KeyError("Nu exista un oras cu id-ul orasului de pornire dat!")
        if self.localitateRepository.read(idOrasOprire) is None:
            raise KeyError("Nu exista un oras cu id-ul orasului de oprire dat!")

        ruta = Ruta(idRuta, idOrasPornire, idOrasOprire, pret, dusIntors)
        self.rutaValidator.valideaza(ruta)
        self.rutaRepository.create(ruta)

    def getAll(self):
        return self.rutaRepository.read()

    def ordonareLocalitatiNrRute(self):
        '''
        ordoneaza localitatile dupa nr de rute dus-intors care pornesc din ele
        :return: o lista de dictionare {"localitate": Localitate, "numarRute": int}
        '''
        idLocalitatiNrRute = {}
        for localitate in self.localitateRepository.read():
            idLocalitatiNrRute[localitate.id_entity] = 0
        for ruta in self.rutaRepository.read():
            if ruta.dusIntors:
                idLocalitatiNrRute[ruta.idOrasPornire] += 1

        idLocalitatiOrdonate = sorted(idLocalitatiNrRute.keys(), key= lambda idLocalitate: idLocalitatiNrRute[idLocalitate])

        rezultat = []
        for idLocalitate in idLocalitatiOrdonate:
            rezultat.append({
                "localitate": self.localitateRepository.read(idLocalitate),
                "numarRute": idLocalitatiNrRute[idLocalitate]
            })
        return rezultat

    def getRuteMunicipiu(self):
        '''
        determina rutele municipiu si numele localitatilor de pornire/oprire
        :return: o lista de dictionare {"ruta": Ruta, "numeOrasPornire": str, "numeOrasOprire": str}
        '''

        rezultat = []
        for ruta in self.rutaRepository.read():
            localitateOprire = self.localitateRepository.read(ruta.idOrasOprire)
            if localitateOprire.tip == "municipiu":
                localitatePornire = self.localitateRepository.read(ruta.idOrasPornire)
                rezultat.append({
                    "ruta": ruta,
                    "numeOrasPornire": localitatePornire.nume,
                    "numeOrasOprire": localitateOprire.nume
                })
        return rezultat

    def exportJson(self, filename: str):
        '''
        exporta intr-un fisier Json numele de localitati, impreuna cu numele loclaiattilr inspre care exista rute
        pornind de la acestea
        :param filename: numele fisierului in care se face exportul
        :return:
        '''

        rezultat = {}
        for localitate in self.localitateRepository.read():
            rezultat[localitate.id_entity] = []
        for ruta in self.rutaRepository.read():
            localitatePornire = self.localitateRepository.read(ruta.idOrasPornire)
            localitateOprire = self.localitateRepository.read(ruta.idOrasOprire)

            if localitateOprire.nume not in rezultat[localitatePornire.nume]:
                rezultat[localitatePornire.nume].append(localitateOprire.nume)

        with open(filename, 'w') as f:
            f.write(jsonpickle.dumps(rezultat))
