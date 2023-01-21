from Functii.functii import citire_lista, prop_5, prop_12


def print_menu():
    print("1.Citirea si afisarea listei")
    print("2.Proprietatea 5")
    print("3.Proprietatea 12")
    print("x.Iesire")


def run_ui():
    lst = []
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == '1':
            lst = citire_lista()
            print(lst)
        elif optiune == '2':
            print(prop_5(lst))
        elif optiune == '3':
            print(prop_12(lst))
        elif optiune == 'x':
            break
        else:
            print("Optiune gresita! Reincercati")
