from Logic.CRUD import adaugare_cheltuiala, modifica_cheltuiala, get_by_nr_apartament
from Domain.cheltuiala import get_nr_apartament, get_tip, get_suma, get_ziua


def test_adauga_cheltuiala():
    lista = adaugare_cheltuiala(1, 2, 500, "gaz", [])
    assert len(lista) == 1
    assert get_nr_apartament(lista[0]) == 1
    assert get_ziua(lista[0]) == 2
    assert get_suma(lista[0]) == 500
    assert get_tip(lista[0]) == "gaz"


def test_modifica_cheltuiala():
    lista = []
    lista = adaugare_cheltuiala(1, 2, 500, "gaz", lista)
    lista = adaugare_cheltuiala(2, 3, 256, "canal", lista)
    lista = modifica_cheltuiala(1, 3, 300, "apa", lista)

    cheltuiala_noua = get_by_nr_apartament(1, lista)
    assert get_nr_apartament(cheltuiala_noua) == 1
    assert get_suma(cheltuiala_noua) == 300
    assert get_tip(cheltuiala_noua) == "apa"


def test_get_by_nr_apartament():
    lista = []
    lista = adaugare_cheltuiala(1, 2, 500, "apa", lista)
    lista = adaugare_cheltuiala(2, 3, 360, "incalzire", lista)
    assert get_suma(get_by_nr_apartament(1, lista)) == 500
    assert get_tip(get_by_nr_apartament(2, lista)) == "incalzire"
