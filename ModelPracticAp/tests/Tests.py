from domain.Cafenea import Cafenea
from domain.CafeneaValidator import CafeneaValidator
from repository.Repository import Repository
from service.Service import CafeneaService


def testService():
    repo = Repository()
    validator = CafeneaValidator()
    service = CafeneaService(repo, validator)
    service.adauga_cafenea('nescafe', 'spania', 23)
    assert(len(service.showAll())) == 1

def testSortare():
    repo = Repository()
    validator = CafeneaValidator()
    service = CafeneaService(repo, validator)
    service.adauga_cafenea('nescafe', 'spania', 23)
    service.adauga_cafenea('dorna', 'grecia', 26)
    service.adauga_cafenea('bucegi', 'spania', 13)
    lista = service.sortare()
    cafenea1 = Cafenea('nescafe', 'spania', 23)
    cafenea2 = Cafenea('dorna', 'grecia', 26)
    cafenea3 = Cafenea('bucegi', 'spania', 13)

    assert (lista[0] == cafenea2)
    assert (lista[1] == cafenea3)
    assert (lista[2] == cafenea1)

def testFiltrare():
    repo = Repository()
    validator = CafeneaValidator()
    service = CafeneaService(repo, validator)
    service.adauga_cafenea('nescafe', 'spania', 23)
    service.adauga_cafenea('dorna', 'grecia', 26)
    service.adauga_cafenea('bucegi', 'spania', 13)
    service.adauga_cafenea('carpati', 'spania', 45)
    lista = service.filtrare('spania', 30)
    cafenea1 = Cafenea('nescafe', 'spania', 23)
    cafenea2 = Cafenea('bucegi', 'spania', 13)

    assert (lista[0] == cafenea1)
    assert (lista[1] == cafenea2)

def testAll():
    testSortare()
    testService()
    testFiltrare()
