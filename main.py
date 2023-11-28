from Characters.character_validator import CharacterValidator
from Repository.repository import RepositoryJsonC
from Service.service import Service
from UI.ui import Console


def main():
    c_repo = RepositoryJsonC("characters.json")
    c_val = CharacterValidator()
    c_service = Service(c_repo, c_val)
    console = Console(c_service)
    console.ui_run_menu()


if __name__ == '__main__':
    main()
