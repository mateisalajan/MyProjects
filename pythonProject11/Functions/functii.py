def suma_n_numere(n: int):
    """
    Calculeaza suma a n numere
    :param n: numraul de numere(citit de la tastatura)
    :return: suma numerelor
    """
    s = 0
    for x in range(n+1):
        s = s + x
    return s


def verif_nr_prim(x: int):
    """
    Verifica daca un numar este prim
    :param x: un nr intreg
    :return: 1,daca un nr este prim, 0 in caz contrar
    """
    nrdiv = 0
    for d in range(1, x+1):
        if x % d == 0:
            nrdiv += 1

    if nrdiv == 2:
        return 1
    else:
        return 0


def cmmdc(x: int, y: int):
    """
    Calculeaza cmmdc ul a dpua numere
    :param x: un nr intreg
    :param y: un nr intreg
    :return: cmmdc ul lui x si y
    """
    while x != y:
        if x > y:
            x = x-y
        else:
            y = y-x
    return x
