from domain.CafeaValidator import CafeaValidator
from repository.Repo import Repo
from service.Service import Service
from ui.Console import Console


def main():
    repo = Repo()
    valid = CafeaValidator()
    service = Service(repo, valid)
    service.add('borsec', 'spania', 54.3)
    service.add('nescafe', 'grecia', 12)
    service.add('bucegi', 'spania', 15.8)
    service.add('dorna', 'albania', 37)
    service.add('eco', 'spania', 45)
    service.add('alfi', 'spania', 23)
    console = Console(service)
    console.run_menu()


if __name__ == '__main__':
    main()