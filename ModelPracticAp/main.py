from domain.CafeneaValidator import CafeneaValidator
from repository.Repository import Repository
from service.Service import CafeneaService
from tests.Tests import testAll
from ui.Console import Console


def main():
    testAll()
    crepo = Repository()
    cvalidator = CafeneaValidator()
    cservice = CafeneaService(crepo, cvalidator)
    console = Console(cservice)
    console.run_menu()


if __name__ == '__main__':
    main()
