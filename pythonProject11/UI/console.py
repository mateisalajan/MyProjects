from Functions.functii import suma_n_numere, verif_nr_prim, cmmdc


def print_menu():
    print("1.Suma a n numere")
    print("2.Verificare nr prim")
    print("3.Cmmdc a doua numere")
    print("x.Iesire")


def run_ui():
    while True:
        print_menu()
        optiune = input("Dati optiune: ")
        if optiune == '1':
            n = int(input("Dati numarul de numere: "))
            print(suma_n_numere(n))
        elif optiune == '2':
            x = int(input("Dati numarul de verificat: "))
            print(verif_nr_prim(x))
        elif optiune == '3':
            x = int(input("Dati primul numar: "))
            y = int(input("Dati al doilea numar: "))
            print(cmmdc(x, y))
        elif optiune == 'x':
            break
        else:
            print("Optiune gresita! Reincercati")
