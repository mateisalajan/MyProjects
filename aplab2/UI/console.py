from Functii.functii import prob_2, prob_7, prob_14


def print_menu():
    print("1.Problema 2")
    print("2.Problema 7")
    print("3.Problema 14")
    print("x.Iesire")


def run_ui():
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == '1':
            zi = int(input("Dati ziua: "))
            luna = int(input("Dati luna: "))
            an = int(input("Dati anul: "))
            print(prob_2(zi, luna, an))
        elif optiune == '2':
            nr = int(input("Dati numarul: "))
            print(prob_7(nr))
        elif optiune == '3':
            nr = int(input("Dati numarul: "))
            print(prob_14(nr))
        elif optiune == 'x':
            break
        else:
            print("Optiune gresita! Reincercati")
