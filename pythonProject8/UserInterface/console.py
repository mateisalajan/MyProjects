
from Service.localitateService import LocalitateService
from Service.rutaService import RutaService


class Console:
    def __init__(self, localitateService: LocalitateService, rutaService: RutaService):
        self.localitateService = localitateService
        self.rutaService = rutaService

    def runMenu(self):
        while True:
            print("1. Adauga localitate")
            print("2. Adauga ruta")
            print("3. Ordoneaza localitatile dupa nr. de rute dus-intors")
            print("4. Determina rutele ce se opresc intr-un municipiu")
            print("5. Exporta Json")
            print("a1. Afiseaza toate localitatile")
            print("a2. Afiseaza toate rutele")
            print("x. Iesire")

            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.adaugaLocalitate()
            elif optiune == "2":
                self.adaugaRuta()
            elif optiune == "3":
                self.afiseaza(self.rutaService.ordonareLocalitatiNrRute())
            elif optiune == "4":
                self.afiseaza(self.rutaService.getRuteMunicipiu())
            elif optiune == "5":
                self.exportaJson()
            elif optiune == "a1":
                self.afiseaza(self.localitateService.getAll())
            elif optiune == "a2":
                self.afiseaza(self.rutaService.getAll())
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati")

    def afiseaza(self, listaEntitai):
        for entitate in listaEntitai:
            print(entitate)

    def adaugaLocalitate(self):
        try:
            idEntitate = input("Dati id-ul localitatii: ")
            nume = input("Dati numele localitatii: ")
            tip = input("Dati tipul localitatii(sat,oras,municipiu): ")

            self.localitateService.adauga(idEntitate, nume, tip)
        except Exception as e:
            print(e)

    def adaugaRuta(self):
        try:
            idRuta = input("Dati id-ul rutei: ")
            idOrasPornire = input("Dati id-ul orasului de pornire: ")
            idOrasOprire = input("Dati id-ul orasului de oprire: ")
            pret = float(input("Dati pretul rutei: "))
            dusIntors = input("Dati proprietatea de dus-intors a rutei (da/nu): ")
            if dusIntors == "da":
                dusIntors = True
            elif dusIntors == "nu":
                dusIntors = False
            else:
                raise ValueError("'Dus-intors' poate fi doar da sau nu!")

            self.rutaService.adauga(idRuta, idOrasPornire, idOrasOprire, pret, dusIntors)
        except Exception as e:
            print(e)

    def exportaJson(self):
        try:
            filename = input("Dati numele fisierului in care se va face exportul: ")

            self.rutaService.exportJson(filename)
        except Exception as e:
            print(e)

