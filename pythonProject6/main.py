#proprietatea 14 lab-3
def allHavePfEqualToPi(l: list[float]):
    '''
    verifica daca toate elementele dintr-o lista au partea intreaga egala cu partea fractionara
    :param l: lista de numere float
    :return: True daca toate elementele din l au partea intreaga egala cu partea fractionara,sau False in caz contrar
    '''
    for x in l:
        lStr = str(x)
        pi = lStr.split(".")[0]
        pf = lStr.split(".")[1]
        if pi != pf:
            return False
    return True


def testAllHavePfEqualToPi():
    assert allHavePfEqualToPi([17.23, 7.0, 34.98, 2.0]) is False
    assert allHavePfEqualToPi([12.12, 6.6, 18.18, 27.27]) is True

def get_longest_equal_int_real(l: list[float]):
    '''
    detrmina cea mai lunga subsecventa de numere care au partea intreaga egala cu partea fractionara
    :param l: lista de numere float
    :return: cea mai lunga subsecventa de numere care au partea intreaga egala cu partea fractionara
    '''
    subsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if allHavePfEqualToPi(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventaMax):
                subsecventaMax = l[i:j + 1]
    return subsecventaMax

def test_get_longest_equal_int_real():
    assert get_longest_equal_int_real([2.0, 13.13, 9.9, 77.77, 12.12, 8.5, 4.2, 7.2]) == [13.13, 9.9, 77.77, 12.12]
    assert get_longest_equal_int_real([3.14, 8.7, 9.62, 4.66, 8.0, 9.77]) == []