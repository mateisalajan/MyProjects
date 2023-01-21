from domain.Cafea import Cafea
from domain.CafeaValidator import CafeaValidator
from repository.Repo import Repo
from service.Service import Service


def test_service():
    repo = Repo()
    valid = CafeaValidator()
    service = Service(repo, valid)
    service.add('borsec', 'spania', 23)
    service.add('nescafe', 'grecia', 12)

    assert (len(service.get_all()) == 2)


def test_sortare():
    repo = Repo()
    valid = CafeaValidator()
    service = Service(repo, valid)
    service.add('borsec', 'spania', 54.3)
    service.add('nescafe', 'grecia', 12)
    service.add('bucegi', 'spania', 15.8)
    service.add('dorna', 'albania', 37)
    service.add('eco', 'spania', 45)
    service.add('alfi', 'spania', 23)
    lst = service.sortare()
    cafea1 = Cafea('dorna', 'albania', 37)
    cafea2 = Cafea('borsec', 'spania', 54.3)
    assert (lst[0] == cafea1)
    assert (lst[5] == cafea2)


def test_filtrare():
    repo = Repo()
    valid = CafeaValidator()
    service = Service(repo, valid)
    service.add('borsec', 'spania', 54.3)
    service.add('nescafe', 'grecia', 12)
    service.add('bucegi', 'spania', 15.8)
    service.add('dorna', 'albania', 37)
    service.add('eco', 'spania', 45)
    service.add('alfi', 'spania', 23)
    lst = service.filtrare('spania', 30)
    cafea1 = Cafea('alfi', 'spania', 23)
    cafea2 = Cafea('bucegi', 'spania', 15.8)
    assert (lst[0] == cafea2)
    assert (lst[1] == cafea1)


def test_all():
   test_service()
   test_sortare()
   test_filtrare()