from datetime import datetime
import datetime


def prob_2(zi: int, luna: int, an: int):
    """
    Calculeaza varsta unei persoane, in zile
    :param zi:zi nasterii
    :param luna:luna nasterii
    :param an:anul nasterii
    :return:varsta unei persoane, in zile
    """
    current_time = datetime.datetime.now()
    birth_date = datetime.date(an, luna, zi)
    end_date = datetime.date(current_time.year, current_time.month, current_time.day)
    time_difference = end_date - birth_date
    age = time_difference.days

    return age


def prob_7(n: int):
    """
    Calculeaza produsul factorilor primi ai lui n
    :param n: un numar intreg
    :return: produsul factorilor primi ai lui n
    """
    prod = 1
    f = 2
    while n > 1:
        p = 0
        while n % f == 0:
            p += 1
            n = n/f
        if p != 0:
            prod = prod * f
        f += 1
    return prod


def verif_nr_perfect(n: int):
    s = 0
    for d in range(1, n):
        if n % d == 0:
            s = s + d
    if s == n:
        return 1
    else:
        return 0


def prob_14(n: int):
    """
    Genereaza cel mai mic număr perfect mai mare decât n
    :param n:un nr intreg
    :return:cel mai mic număr perfect mai mare decât n
    """
    y = n + 1
    ok = 0
    while ok == 0:
        if verif_nr_perfect(y) == 1:
            ok = 1
        else:
            y += 1
    return y
