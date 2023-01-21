from domain.CafeaValidator import CafeaValidator
from repository.Repo import Repo
from service.Service import Service
from ui.Console import Console
from tests.Tests import test_all


def main():
    test_all()
    repo = Repo("coffees")
    valid = CafeaValidator()
    service = Service(repo, valid)
    console = Console(service)
    console.run_menu()


if __name__ == '__main__':
    main()