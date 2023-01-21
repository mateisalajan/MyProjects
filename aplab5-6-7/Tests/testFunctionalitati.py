from Logic.CRUD import adaugare_cheltuiala, get_by_nr_apartament
from Logic.Functionalitati import stergere_cheltuieli, sterge_cheltuieli_consecutive, sterge_cheltuieli_dupa_tip, \
    tipareste_apartamente_dupa_suma, tipareste_cheltuieli_dupa_tip, tipareste_cheltuieli_dupa_zi_si_suma, \
    suma_totala_dupa_tip, sortare_dupa_tip, total_cheltuieli, elimina_dupa_tip, elimina_dupa_suma


def test_stergere_cheltuieli():
    lista = []
    lista = adaugare_cheltuiala(1, 2, 125, "gaz", lista)
    lista = adaugare_cheltuiala(2, 3, 600, "canal", lista)
    lista = stergere_cheltuieli(1, lista)
    assert len(lista) == 1
    assert get_by_nr_apartament(1, lista) is None


def test_stergere_cheltuieli_consecutive():
    lista = []
    lista = adaugare_cheltuiala(1, 2, 125, "gaz", lista)
    lista = adaugare_cheltuiala(2, 3, 600, "canal", lista)
    lista = adaugare_cheltuiala(3, 1, 245, "apa", lista)
    lista = adaugare_cheltuiala(12, 5, 78, "canal", lista)
    lista = sterge_cheltuieli_consecutive(1, 3, lista)
    assert len(lista) == 1


def test_sterge_cheltuieli_dupa_tip():
    lista = []
    lista = adaugare_cheltuiala(1, 2, 350, "apa", lista)
    lista = sterge_cheltuieli_dupa_tip("apa", lista)
    assert len(lista) == 0
    assert get_by_nr_apartament("1", lista) is None


def test_tipareste_apartamente_dupa_suma():
    lista = []
    lista = adaugare_cheltuiala(1, 2, 200, "inclazire", lista)
    lista = adaugare_cheltuiala(2, 4, 400, "canal", lista)
    lista = tipareste_apartamente_dupa_suma(300, lista)
    assert len(lista) == 1


def test_tipareste_cheltuieli_dupa_tip():
    lista = []
    lista = adaugare_cheltuiala(1, 2, 350, "gaz", lista)
    lista = adaugare_cheltuiala(2, 4, 400, "gaz", lista)
    lista = tipareste_cheltuieli_dupa_tip("gaz", lista)
    assert len(lista) == 2


def test_tipareste_cheltuieli_dupa_zi_si_suma():
    lista = []
    lista = adaugare_cheltuiala(1, 2, 350, "lumina", lista)
    lista = adaugare_cheltuiala(2, 4, 400, "gaz", lista)
    lista = adaugare_cheltuiala(3, 12, 266, "apa", lista)
    lista = adaugare_cheltuiala(4, 7, 200, "apa", lista)
    lista = tipareste_cheltuieli_dupa_zi_si_suma(10, 300, lista)
    assert len(lista) == 2


def test_suma_totala_dupa_tip():
    lista = []
    lista = adaugare_cheltuiala(1, 2, 350, "gaz", lista)
    lista = adaugare_cheltuiala(2, 4, 400, "lumina", lista)
    lista = adaugare_cheltuiala(3, 2, 450, "gaz", lista)
    lista = adaugare_cheltuiala(4, 4, 400, "apa", lista)
    rez = suma_totala_dupa_tip("gaz", lista)
    assert rez == 800


def test_sortare_dupa_tip():
    lista = []
    lista = adaugare_cheltuiala(1, 2, 125, "apa", lista)
    lista = adaugare_cheltuiala(2, 4, 400, "canal", lista)
    lista = adaugare_cheltuiala(3, 20, 600, "apa", lista)
    lista = sortare_dupa_tip("apa", lista)
    assert len(lista) == 3


def test_total_cheltuieli():
    lista = []
    lista = adaugare_cheltuiala(14, 2, 125, "lumina", lista)
    lista = adaugare_cheltuiala(2, 4, 400, "gaz", lista)
    lista = adaugare_cheltuiala(3, 2, 350, "electrica", lista)
    lista = adaugare_cheltuiala(14, 4, 400, "gaz", lista)
    rez = total_cheltuieli(14, lista)
    assert rez == 525


def test_elimina_dupa_tip():
    lista = []
    lista = adaugare_cheltuiala(1, 2, 30, "apa", lista)
    lista = adaugare_cheltuiala(2, 4, 167, "gaz", lista)
    lista = adaugare_cheltuiala(3, 2, 350, "apa", lista)
    lista = adaugare_cheltuiala(4, 4, 289, "lumina", lista)
    lista = elimina_dupa_tip("apa", lista)
    assert len(lista) == 2


def test_elimina_dupa_suma():
    lista = []
    lista = adaugare_cheltuiala(1, 2, 30, "apa", lista)
    lista = adaugare_cheltuiala(2, 4, 167, "gaz", lista)
    lista = adaugare_cheltuiala(3, 2, 350, "apa", lista)
    lista = adaugare_cheltuiala(4, 4, 289, "lumina", lista)
    lista = elimina_dupa_suma(300, lista)
    assert len(lista) == 1
