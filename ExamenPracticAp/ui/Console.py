from service.Service import Service


class Console:
    def __init__(self, service: Service):
        self.service = service

    def run_menu(self):
        while(True):
            print("1.Adaugare cafea")
            print("2.Afisare cafele")
            print("3.Filtrare dupa tara")
            print("x.Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == '1':
                self.ui_add()
            elif optiune == '2':
                self.ui_get_all()
            elif optiune == '3':
                self.ui_get_tara()
            elif optiune == 'x':
                break
            else:
                print("Optiune gresita!")

    def ui_add(self):
        try:
            id_cafea = int(input("Dati id-ul cafelei: "))
            nume = input("Dati numele cafelei: ")
            tara = input("Dati tara de origine a cafelei: ")
            pret = float(input("Dati pretul cafelei: "))
            self.service.add(id_cafea, nume, tara, pret)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)


    def ui_get_all(self):
        cafele = self.service.get_all()
        for cafea in cafele:
            print(cafea)

    def ui_get_tara(self):
        tara = input("Dati tara de origine a cafelei: ")
        cafele = self.service.get_cafea_tara(tara)
        for cafea in cafele:
            print(cafea)
