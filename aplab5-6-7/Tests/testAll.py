from Tests.testCRUD import test_get_by_nr_apartament, test_adauga_cheltuiala, \
    test_modifica_cheltuiala
from Tests.testFunctionalitati import test_total_cheltuieli, \
    test_stergere_cheltuieli, test_sterge_cheltuieli_dupa_tip, test_tipareste_apartamente_dupa_suma, \
    test_tipareste_cheltuieli_dupa_tip, \
    test_suma_totala_dupa_tip, test_sortare_dupa_tip, test_elimina_dupa_tip, test_elimina_dupa_suma, \
    test_stergere_cheltuieli_consecutive, test_tipareste_cheltuieli_dupa_zi_si_suma \


def run_all_tests():
    test_get_by_nr_apartament()
    test_adauga_cheltuiala()
    test_modifica_cheltuiala()
    test_stergere_cheltuieli()
    test_stergere_cheltuieli_consecutive()
    test_sterge_cheltuieli_dupa_tip()
    test_tipareste_apartamente_dupa_suma()
    test_tipareste_cheltuieli_dupa_tip()
    test_tipareste_cheltuieli_dupa_zi_si_suma()
    test_elimina_dupa_suma()
    test_elimina_dupa_tip()
    test_total_cheltuieli()
    test_suma_totala_dupa_tip()
    test_sortare_dupa_tip()
