def citire_lista():
    lst = []
    given_string = input("Dati lista de nr intregi ,separate prin virgula: ")
    numbers_as_strings = given_string.split(",")
    for x in numbers_as_strings:
        lst.append(int(x))
    return lst


def prop_5(lst: list[int]):
    """
    Calculeaza cea mai lunga secventa de numere egale
    :param lst: o lista de numere intregi
    :return: o lista ce contine cea mai lunga secventa de numere egale
    """
    subsecventa_max = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] == lst[j] and len(lst[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = lst[i:j + 1]
    return subsecventa_max


def verif(x: int, y: int):
    if (x < 0 and y < 0) or (x > 0 and y > 0):
        return False
    else:
        return True


def verifica_lista(lst: list[int]):
    i = 0
    while i < len(lst) - 1:
        if verif(lst[i], lst[i + 1]) is False:
            return False
        i += 1
    return True


def prop_12(lst: list[int]):
    """
    Calculeaza cea mai lunga secventa in care oricare doua elemente consecutive sunt de semne contrare
    :param lst: o lista de numere intregi
    :return: o lista ce contine cea mai lunga secventa cu proprietatea mentionata
    """
    subsecventa_max = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if verifica_lista(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = lst[i:j + 1]
    return subsecventa_max
