from Functii.functii import prop_5, prop_12


def tests():
    lst = [1, 4, 4, 4, 5, 6, 6, 7]
    assert prop_5(lst) == [4, 4, 4]
    lst2 = [1, 1, -2, 3, -4, -6, 5, 7]
    assert prop_12(lst2) == [1, -2, 3, -4]
