from domain.CafeaValidator import CafeaValidator
from repository.Repository import Repo
from service.Service import Service
from tests.Tests import test_all
from ui.Console import Console


def main():

    test_all()
    repo = Repo()
    validator = CafeaValidator()
    service = Service(repo, validator)

    service.add("borsec", "spania", 23)
    service.add("nescafe", "albania", 12.5)
    service.add("poiana", "spania", 10)
    service.add("dorna", "spania", 45)
    service.add("gusto", "grecia", 36)
    service.add("bucegi", "spania", 52.9)

    console = Console(service)
    console.run_menu()


if __name__ == '__main__':
    main()
