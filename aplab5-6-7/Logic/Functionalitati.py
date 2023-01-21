from Domain.cheltuiala import get_nr_apartament, get_tip, get_suma, get_ziua


def stergere_cheltuieli(nr_apartament, lst):
    """
    sterge cheltuielile dupa nr_apartament din lista
    :param nr_apartament: nr apartamentului cheltuielii
    :param lst: lista de cheltuieli
    :return: lista modificata
    """
    return [cheltuiala for cheltuiala in lst if get_nr_apartament(cheltuiala) != nr_apartament]


def sterge_cheltuieli_consecutive(nr_ap1, nr_ap2, lst):
    """
    sterge cheltuielile dupa nr_apartament din lista
    :param nr_ap1: nr primului apartament
    :param nr_ap2: nr celui de al doilea apartament
    :param lst: lista de cheltuieli
    :return: lista modificata
    """
    return [cheltuiala for cheltuiala in lst if get_nr_apartament(cheltuiala) < nr_ap1 or
            get_nr_apartament(cheltuiala) > nr_ap2]


def sterge_cheltuieli_dupa_tip(tip, lst):
    """
    sterge cheltuielile dupa tip din lista
    :param tip: tipul cheltuielii
    :param lst: lista de cheltuieli
    :return: lista modificata
    """
    return [cheltuiala for cheltuiala in lst if get_tip(cheltuiala) != tip]


def tipareste_apartamente_dupa_suma(suma: int, lst):
    """
    tipărește toate apartamentele care au cheltuieli mai mari decât o sumă data
    :param suma: suma cheltuielii
    :param lst: lista de cheltuieli
    :return: lista modificata
    """
    lista_noua = []
    for cheltuiala in lst:
        if get_suma(cheltuiala) > suma:
            lista_noua.append(cheltuiala)

    return lista_noua


def tipareste_cheltuieli_dupa_tip(tip, lst):
    """
    tipărește cheltuielile de un anumit tip de la toate apartamentele
    :param tip: tipul cheltuielii
    :param lst: lista de cheltuieli
    :return: lista modificata
    """
    lista_noua = []
    for cheltuiala in lst:
        if get_tip(cheltuiala) == tip:
            lista_noua.append(cheltuiala)

    return lista_noua


def tipareste_cheltuieli_dupa_zi_si_suma(ziua, suma, lst):
    """
    tipărește toate cheltuielile efectuate înainte de o zi și mai mari decât o suma
    :param ziua: ziua cheltuielii
    :param suma: suma cheltuielii
    :param lst: lista de cheltuieli
    :return: lista modificata
    """
    lista_noua = []
    for cheltuiala in lst:
        if get_ziua(cheltuiala) < ziua and get_suma(cheltuiala) > suma:
            lista_noua.append(cheltuiala)

    return lista_noua


def suma_totala_dupa_tip(tip, lst):
    """
    tipărește suma totală pentru un tip de cheltuială
    :param tip: tipul cheltuielii
    :param lst: lista de cheltuieli
    :return: suma totala dupa tip
    """
    suma = 0
    for cheltuiala in lst:
        if get_tip(cheltuiala) == tip:
            suma = suma + get_suma(cheltuiala)

    return suma


def sortare_dupa_tip(tip, lst):
    """
    tipărește toate apartamentele sortate după un tip de cheltuială
    :param tip: tipul cheltuielii
    :param lst: lista de cheltuieli
    :return: lista sortata
    """
    lista_noua = []
    for cheltuiala in lst:
        if get_tip(cheltuiala) == tip:
            lista_noua.append(cheltuiala)

    return sorted(lst, reverse=False, key=get_tip)


def total_cheltuieli(nr_apartament, lst):
    """
    tipărește totalul de cheltuieli pentru un apartament dat
    :param nr_apartament: nr apartamentului cheltuielii
    :param lst: lista de cheltuieli
    :return: suma totala
    """

    suma_total = 0
    for cheltuiala in lst:
        if get_nr_apartament(cheltuiala) == nr_apartament:
            suma_total = suma_total + get_suma(cheltuiala)
    return suma_total


def elimina_dupa_tip(tip, lst):
    """
    elimină toate cheltuielile de un anumit tip
    :param tip: tipul cheltuielii
    :param lst: lista de cheltuieli
    :return: lista dupa eliminare
    """
    lista_noua = []
    for cheltuiala in lst:
        if get_tip(cheltuiala) != tip:
            lista_noua.append(cheltuiala)

    return lista_noua


def elimina_dupa_suma(suma, lst):
    """
    elimină toate cheltuielile mai mici decât o sumă dată
    :param suma: suma cheltuielii
    :param lst: lista de cheltuieli
    :return: lista dupa eliminare
    """

    # lista_noua = []
    # for cheltuiala in lst:
    #     if get_suma(cheltuiala) > suma:
    #         lista_noua.append(cheltuiala)
    #
    # return lista_noua
    return [cheltuiala for cheltuiala in lst if get_suma(cheltuiala) > suma]


def get_undo_list(lst, undo_list):
    """
    reface ultima operație
    :param lst: lista de cheltuieli
    :param undo_list: lista operatiilor efectuate
    :return: lista operatiilor efectuate
    """
    undo_list.append(lst)
    return undo_list
