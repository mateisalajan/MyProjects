from UI.Console import Console
from domain.Prietenie_Validator import PrietenieValidator
from domain.User_Validator import UserValidator
from repository.Prietenie_Repo import PrietenieRepo
from repository.User_Repo import UserRepo
from service.Prietenie_Srevice import PrietenieService
from service.User_Service import UserService


def main():
    user_repo = UserRepo()
    user_validator = UserValidator()
    user_service = UserService(user_repo, user_validator)

    prietenie_repo = PrietenieRepo()
    prietenie_validator = PrietenieValidator()
    prietenie_service = PrietenieService(prietenie_repo, user_repo, prietenie_validator)

    console = Console(user_service, prietenie_service)
    console.run_menu()


if __name__ == '__main__':
    main()
