from service.Service import Service


class Console:
    def __init__(self, service: Service):
        self.service = service

    def run_menu(self):
        while(True):
            print("1.Adauga cafea")
            print("2.Afisare cafele")
            print("3.Sortare")
            print("4.Filtrare")
            print("x.Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == '1':
                self.ui_add()
            elif optiune == '2':
                self.ui_afisare()
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
            tara = input("Dati tara de origine a cafelei: ")
            pret = float(input("Dati pretul cafelei: "))
            self.service.add(nume, tara, pret)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_afisare(self):
        cafele = self.service.get_all()
        for cafea in cafele:
            print(cafea)

    def ui_sortare(self):
        cafele = self.service.sortare()
        for cafea in cafele:
            print(cafea)

    def ui_filtrare(self):
        tara = input("Dati tara de origine a cafelei: ")
        pret = float(input("Dati pretul cafelei: "))
        cafele = self.service.filtrare(tara, pret)
        for cafea in cafele:
            print(cafea)
