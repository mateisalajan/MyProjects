from Domain.cheltuiala import creeaza_cheltuiala, get_nr_apartament, get_ziua


def read(lista_cheltuieli, nr_apartament):
    """
    Citeste o cheltuiala din lista de cheltuieli.
    :param lista_cheltuieli: lista de cheltuieli
    :param nr_apartament: nr apartamentului cheltuielii
    :return: cheltuiala daca aceasta exista in lista de cheltuieli sau lista de cheltuieli daca aceasta nu exista
    """
    if not nr_apartament:
        return lista_cheltuieli

    cheltuiala_nr_apartament = None
    for cheltuiala in lista_cheltuieli:
        if get_nr_apartament(cheltuiala) == nr_apartament:
            cheltuiala_nr_apartament = cheltuiala

    if cheltuiala_nr_apartament:
        return cheltuiala_nr_apartament


def adaugare_cheltuiala(nr_apartament, ziua, suma, tip, lst: list):
    """
    adauga o cheltuiala in lista de cheltuieli
    :param ziua: ziua cheltuielii
    :param nr_apartament: nr apartamentului cheltuielii
    :param suma: suma cheltuielii
    :param tip: tipul cheltuielii
    :param lst: lista de cheltuieli
    :return: o lista continand atat elementele vechi, cat si noua cheltuiala
    """

    cheltuiala = creeaza_cheltuiala(nr_apartament, ziua, suma, tip)
    return lst + [cheltuiala]


def modifica_cheltuiala(nr_apartament, ziua, suma, tip, lst):
    """
    modifica o cheltuiala cu nr_apartament dat
    :param ziua: ziua cheltuielii
    :param nr_apartament: nr apartamentului cheltuielii
    :param suma: suma cheltuielii
    :param tip: tipul cheltuielii
    :param lst: lista de cheltuieli
    :return: lista modificata
    """
    lista_noua = []
    for cheltuiala in lst:
        if get_nr_apartament(cheltuiala) == nr_apartament:
            cheltuiala_noua = creeaza_cheltuiala(nr_apartament, ziua, suma, tip)
            lista_noua.append(cheltuiala_noua)
        else:
            lista_noua.append(cheltuiala)

    return lista_noua


def stergere_cheltuiala(ziua, lst):
    """
    sterge cheltuielile dupa zi din lista
    :param ziua: ziua cheltuielii
    :param lst: lista de cheltuieli
    :return: lista modificata
    """
    return [cheltuiala for cheltuiala in lst if get_ziua(cheltuiala) != ziua]


def get_by_nr_apartament(nr_apartament, lst):
    """
    gaseste o cheltuiala cu nr_apartament dat din lista
    :param nr_apartament: int
    :param lst: lista de cheltuieli
    :return: cheltuiala cu nr_apartament dat din lista sau None, daca aceasta nu exista
    """
    for cheltuiala in lst:
        if get_nr_apartament(cheltuiala) == nr_apartament:
            return cheltuiala
    return None
