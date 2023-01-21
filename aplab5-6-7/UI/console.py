from Domain.cheltuiala import to_string
from Logic.CRUD import adaugare_cheltuiala, modifica_cheltuiala
from Logic.Functionalitati import stergere_cheltuieli, sterge_cheltuieli_consecutive, sterge_cheltuieli_dupa_tip, \
    tipareste_apartamente_dupa_suma, tipareste_cheltuieli_dupa_tip, tipareste_cheltuieli_dupa_zi_si_suma, \
    elimina_dupa_tip, elimina_dupa_suma, suma_totala_dupa_tip, total_cheltuieli, sortare_dupa_tip, get_undo_list


def print_menu():
    print("1.Adauga cheltuiala")
    print("2.Modifica cheltuiala")
    print("3.Șterge toate cheltuielile de la un apartament")
    print("4.Șterge cheltuielile de la apartamente consecutive")
    print("5.Șterge cheltuielile de un anumit tip de la toate apartamentele")
    print("6.Tipărește apartamentele cu cheltuieli mai mari decât o sumă")
    print("7.Tipărește cheltuielile de un anumit tip de la toate apartamentele")
    print("8.Tipărește cheltuielile efectuate înainte de o zi și mai mari decât o sumă")
    print("9.Tipărește suma totală pentru un tip de cheltuială")
    print("10.Tipărește apartamentele sortate după tip")
    print("11.Tipărește totalul de cheltuieli pentru un apartament dat")
    print("12.Elimină toate cheltuielile de un anumit tip")
    print("13.Elimină cheltuielile mai mici decât o sumă dată")
    print("u.Undo")
    print("r.Redo")
    print("a.Afisare toate cheltuielile")
    print("x.Iesire\n")


def ui_adaugare_cheltuiala(lst):
    try:
        nr_apartament = int(input("Dati nr apartamentului: "))
        ziua = int(input("Dati ziua cheltuielii: "))
        suma = int(input("Dati suma cheltuielii: "))
        tip = input("Dati tipul cheltuielii: ")
        if not tip.isalpha():
            print("Eroare:tipul trebuie sa fie apa, canal, încălzire, gaz, altele!")
        rezultat = adaugare_cheltuiala(nr_apartament, ziua, suma, tip, lst)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))


def ui_modificare_cheltuiala(lst):
    try:
        nr_apartament = int(input("Dati nr apartamentului: "))
        ziua = int(input("Dati noua zi cheltuielii: "))
        suma = int(input("Dati noua suma a cheltuielii: "))
        tip = input("Dati noul tip al cheltuielii: ")
        if not tip.isalpha():
            print("Eroare:tipul trebuie sa fie apa, canal, încălzire, gaz, altele!")
        rezultat = modifica_cheltuiala(nr_apartament, ziua, suma, tip, lst)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))


def ui_sterge_cheltuieli_nr_ap(lst):
    try:
        nr_apartament = int(input("Dati nr apartamentului: "))
        rez = stergere_cheltuieli(nr_apartament, lst)
        return rez
    except ValueError as ve:
        print("Eroare : {}".format(ve))


def ui_sterge_cheltuieli_nr_ap_consecutive(lst):
    try:
        nr_ap1 = int(input("Dati nr primului apartamentului: "))
        nr_ap2 = int(input("Dati nr celui de al doilea apartamentului: "))
        rez = sterge_cheltuieli_consecutive(nr_ap1, nr_ap2, lst)
        return rez
    except ValueError as ve:
        print("Eroare : {}".format(ve))


def ui_sterge_cheltuieli_tip(lst):
    try:
        tip = input("Dati tipul cheltuielii: ")
        rez = sterge_cheltuieli_dupa_tip(tip, lst)
        return rez
    except ValueError as ve:
        print("Eroare : {}".format(ve))


def ui_tipareste_cheltuieli_mai_mari_decat_suma(lst):
    try:
        suma = int(input("Dati suma cheltuielii: "))
        rez = tipareste_apartamente_dupa_suma(suma, lst)
        for x in rez:
            print(x)
    except ValueError as ve:
        print("Eroare : {}".format(ve))


def ui_tipareste_cheltuieli_dupa_tip(lst):
    try:
        tip = input("Dati tipul cheltuielii: ")
        rez = tipareste_cheltuieli_dupa_tip(tip, lst)
        for x in rez:
            print(x)
    except ValueError as ve:
        print("Eroare : {}".format(ve))


def ui_tipareste_cheltuieli_dupa_zi_si_suma(lst):
    try:
        ziua = int(input("Dati ziua cheltuielii: "))
        suma = int(input("Dati suma cheltuielii: "))
        rez = tipareste_cheltuieli_dupa_zi_si_suma(ziua, suma, lst)
        for x in rez:
            print(x)
    except ValueError as ve:
        print("Eroare : {}".format(ve))


def ui_suma_totala_cheltuieli_tip(lst):
        tip = input("Dati tipul cheltuielii: ")
        rez = suma_totala_dupa_tip(tip, lst)
        print(rez)


def ui_tipareste_cheltuieli_sortate_dupa_tip(lst):
    try:
        tip = input("Dati tipul cheltuielii: ")
        rez = sortare_dupa_tip(tip, lst)
        for x in rez:
            print(x)
    except ValueError as ve:
        print("Eroare : {}".format(ve))


def ui_suma_totala_cheltuieli_nr_ap(lst):
    try:
        nr_apartament = int(input("Dati nr apartamentului: "))
        rez = total_cheltuieli(nr_apartament, lst)
        print(rez)
    except ValueError as ve:
        print("Eroare : {}".format(ve))


def ui_elimina_cheltuieli_dupa_tip(lst):
    try:
        tip = input("Dati tipul cheltuielii: ")
        rez = elimina_dupa_tip(tip, lst)
        for x in rez:
            print(x)
    except ValueError as ve:
        print("Eroare : {}".format(ve))


def ui_elimina_cheltuieli_mai_mici_suma(lst):
    try:
        suma = int(input("Dati suma cheltuielii: "))
        rez = elimina_dupa_suma(suma, lst)
        for x in rez:
            print(x)
    except ValueError as ve:
        print("Eroare : {}".format(ve))


def ui_undo(lst, undo_list, redo_list):
    if len(undo_list) > 0:
        redo_list.append(lst)
        return undo_list.pop()
    return lst


def ui_redo(lst, undo_list, redo_list):
    if len(redo_list) > 0:
        undo_list.append(lst)
        return redo_list.pop()
    return lst


def show_all(lst):
    for cheltuiala in lst:
        print(to_string(cheltuiala))


def run_menu(lst):
    undo_list = []
    redo_list = []
    while True:
        print_menu()
        optiune = input("Alegeti optiunea: ")
        if optiune == '1':
            undo_list = get_undo_list(lst, undo_list)
            redo_list.clear()
            lst = ui_adaugare_cheltuiala(lst)
        elif optiune == '2':
            undo_list = get_undo_list(lst, undo_list)
            redo_list.clear()
            lst = ui_modificare_cheltuiala(lst)
        elif optiune == "3":
            undo_list = get_undo_list(lst, undo_list)
            redo_list.clear()
            lst = ui_sterge_cheltuieli_nr_ap(lst)
        elif optiune == "4":
            undo_list = get_undo_list(lst, undo_list)
            redo_list.clear()
            lst = ui_sterge_cheltuieli_nr_ap_consecutive(lst)
        elif optiune == "5":
            undo_list = get_undo_list(lst, undo_list)
            redo_list.clear()
            lst = ui_sterge_cheltuieli_tip(lst)
        elif optiune == "6":
            ui_tipareste_cheltuieli_mai_mari_decat_suma(lst)
        elif optiune == "7":
            ui_tipareste_cheltuieli_dupa_tip(lst)
        elif optiune == "8":
            ui_tipareste_cheltuieli_dupa_zi_si_suma(lst)
        elif optiune == "9":
            ui_suma_totala_cheltuieli_tip(lst)
        elif optiune == "10":
            ui_tipareste_cheltuieli_sortate_dupa_tip(lst)
        elif optiune == "11":
            ui_suma_totala_cheltuieli_nr_ap(lst)
        elif optiune == "12":
            undo_list = get_undo_list(lst, undo_list)
            redo_list.clear()
            ui_elimina_cheltuieli_dupa_tip(lst)
        elif optiune == "13":
            undo_list = get_undo_list(lst, undo_list)
            redo_list.clear()
            ui_elimina_cheltuieli_mai_mici_suma(lst)
        elif optiune == 'u':
            if len(undo_list) > 0:
               lst = ui_undo(lst, undo_list, redo_list)
            else:
                print("Nu se mai poate face undo!")
        elif optiune == 'r':
            if len(redo_list) > 0:
                lst = ui_redo(lst, undo_list, redo_list)
            else:
                print("Nu se mai poate face redo!")
        elif optiune == 'a':
            show_all(lst)
        elif optiune == 'x':
            break
