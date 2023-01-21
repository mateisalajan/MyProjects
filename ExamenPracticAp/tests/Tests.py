from domain.Cafea import Cafea
from domain.CafeaValidator import CafeaValidator
from repository.Repo import Repo
from service.Service import Service


def test_service():
    repo = Repo("coffees")
    valid = CafeaValidator()
    service = Service(repo, valid)
    assert (len(service.get_all()) == 6)


def test_filtrare():
    repo = Repo("coffees")
    valid = CafeaValidator()
    service = Service(repo, valid)
    lst = service.get_cafea_tara('Spania')
    cafea1 = Cafea(2, 'Eco', 'Spania', 40.6)
    cafea2 = Cafea(3, 'Nescafe', 'Spania', 23)

    assert (lst[0] == cafea1)
    assert (lst[1] == cafea2)


def test_all():
    test_service()
    test_filtrare()
