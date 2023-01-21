def creeaza_cheltuiala(nr_apartament, ziua, suma, tip):
    """
    creeaza o cheltuiala
    :param ziua: ziua cheltuielii
    :param nr_apartament: numarul apartamentului
    :param suma: suma cheltuielii
    :param tip: tipul cheltuielii
    :return: un dictionar ce retine o cheltuiala
    """
    return {
        'nr_apartament': nr_apartament,
        'ziua': ziua,
        'suma': suma,
        'tip': tip
    }


def get_ziua(cheltuiala):
    """
    ia ziua cheltuielii
    :param cheltuiala: un dictionar de tip cheltuiala
    :return: ziua cheltuielii
    """
    return cheltuiala['ziua']


def get_nr_apartament(cheltuiala):
    """
    ia nr apartamentului
    :param cheltuiala: un dictionar de tip cheltuiala
    :return: nr apartamentului
    """
    return cheltuiala['nr_apartament']


def get_suma(cheltuiala):
    """
    ia suma cheltuielii
    :param cheltuiala: un dictionar de tip cheltuiala
    :return: suma cheltuielii
    """
    return int(cheltuiala['suma'])


def get_tip(cheltuiala):
    """
    ia tipul cheltuielii
    :param cheltuiala: un dictionar de tip cheltuiala
    :return: tipul cheltuielii
    """
    return cheltuiala['tip']


def to_string(cheltuiala):
    return "nr_apartament: {}, ziua: {}, suma: {}, tip: {}".format(
        get_nr_apartament(cheltuiala),
        get_ziua(cheltuiala),
        get_suma(cheltuiala),
        get_tip(cheltuiala)
    )
