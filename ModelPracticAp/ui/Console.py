
from service import Service


class Console:

    def __init__(self, cafeneaService: Service):
        self.cafeneaService = cafeneaService

    def run_menu(self):
        while True:
            print("1. Adauga cafenea")
            print("2. Afisare toate cafenelele")
            print("3. Sortare")
            print("4. Filtrare")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.ui_adauga()
            elif optiune == "2":
                self.ui_showall()
            elif optiune == "3":
                self.ui_soratare()
            elif optiune == "4":
                self.ui_filtarare()
            elif optiune.lower() == "x":
                break
            else:
                print("Optiune gresita! Reincercati :)")

    def ui_adauga(self):
        try:
            nume = input("Dati numele cafenelei: ")
            tara_de_origine = input("Dati tara_de_origine a cafenelei: ")
            pret = float(input("Dati pretul cafenelei: "))
            self.cafeneaService.adauga_cafenea(nume, tara_de_origine, pret)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_showall(self):
        for cafenea in self.cafeneaService.showAll():
            print(cafenea)

    def ui_soratare(self):
        for cafenea in self.cafeneaService.sortare():
            print(cafenea)

    def ui_filtarare(self):
        tara_de_origine = input("Dati tara_de_origine a cafenelei: ")
        pret = float(input("Dati pretul cafenelei: "))
        for cafenea in self.cafeneaService.filtrare(tara_de_origine,pret):
            print(cafenea)
