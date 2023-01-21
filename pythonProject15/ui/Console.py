from service.Service import Service


class Console:
    def __init__(self, service: Service):
        self.service = service

    def run_menu(self):
        while(True):
            print("1.Adaugare cafea")
            print("2.Afisare toate cafelele")
            print("3.Sortare")
            print("4.Filtrare")
            print("x.Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == '1':
                self.ui_add()
            elif optiune == '2':
                self.get_all_ui()
            elif optiune == '3':
                self.ui_sortare()
            elif optiune == '4':
                self.ui_filtrare()
            elif optiune == 'x':
                break
            else:
                print("Optiune gresita!")

    def ui_add(self):
        try:
            nume = input("Dati numele cafelei: ")
            tara = input("Dati tara de orgine: ")
            pret = float(input("Dati pretul: "))
            self.service.add(nume, tara, pret)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def get_all_ui(self):
        for cafea in self.service.getAll():
            print(cafea)

    def ui_sortare(self):
        for cafea in self.service.sortare():
            print(cafea)

    def ui_filtrare(self):
        tara = input("Dati tara de orgine: ")
        pret = float(input("Dati pretul: "))
        cafele = self.service.filtrarea(tara, pret)
        for cafea in cafele:
            print(cafea)
