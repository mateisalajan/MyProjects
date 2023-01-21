from Functions.functii import suma_n_numere, verif_nr_prim, cmmdc


def tests():
    assert suma_n_numere(18) == 171
    assert verif_nr_prim(17) == 1
    assert verif_nr_prim(12) == 0
    assert cmmdc(18, 12) == 6
