from domain.Cafea import Cafea
from domain.CafeaValidator import CafeaValidator
from repository.Repository import Repo
from service.Service import Service


def test_service():
    repo = Repo()
    validator = CafeaValidator()
    service = Service(repo, validator)

    service.add("borsec", "spania", 23)
    service.add("nescafe", "albania", 12.5)

    assert (len(service.getAll()) == 2)

def test_sortare():
    repo = Repo()
    validator = CafeaValidator()
    service = Service(repo, validator)

    service.add("borsec", "spania", 23)
    service.add("nescafe", "albania", 12.5)
    service.add("poiana", "spania", 10)
    service.add("dorna", "spania", 45)
    service.add("gusto", "grecia", 36)
    service.add("bucegi", "spania", 52.9)
    cafea1 = Cafea("nescafe", "albania", 12.5)
    cafea2 = Cafea("bucegi", "spania", 52.9)

    lst = service.sortare()
    assert (lst[0] == cafea1)
    assert (lst[5] == cafea2)

def test_filtrare():
    repo = Repo()
    validator = CafeaValidator()
    service = Service(repo, validator)

    service.add("borsec", "spania", 23)
    service.add("nescafe", "albania", 12.5)
    service.add("poiana", "spania", 10)
    service.add("dorna", "spania", 45)
    service.add("gusto", "grecia", 36)
    service.add("bucegi", "spania", 52.9)
    cafea1 = Cafea("poiana", "spania", 10)
    cafea2 = Cafea("borsec", "spania", 23)

    lst = service.filtrarea("spania", 30)
    assert (lst[0] == cafea2)
    assert (lst[1] == cafea1)

def test_all():
    test_service()
    test_sortare()
    test_filtrare()


