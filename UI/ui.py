from Service.service import Service


class Console:
    def __init__(self, character_service: Service):
        self.character_service = character_service

    def ui_run_menu(self):
        while True:
            print("1. Add character")
            print("2. Delete character")
            print("3. Select character")
            print("a. Show characters")
            print("x. Exit")
            option = input("Give option: ")
            if option == "1":
                self.ui_add_character()
            elif option == "2":
                self.ui_delete_character()
            elif option == "3":
                self.ui_search_characters()
            elif option == "a":
                self.ui_showall_characters()
            elif option.lower() == "x":
                break
            else:
                print("Optiune gresita! Reincercati")

    def ui_add_character(self):
        try:
            name = input("Name your character: ")
            option = input("Choose a class melee / mage: ")
            self.character_service.add_character(name, option)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_delete_character(self):
        try:
            name = input("Name the character you want to delete: ")
            self.character_service.delete_character(name)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_update_character(self):
        try:
            name = input("Name the character you want to update: ")
            self.character_service.update_character(name)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def ui_showall_characters(self):
        for character in self.character_service.get_all():
            print(character)

    def ui_search_characters(self):
        try:
            name = input("Select your character: ")
            print(self.character_service.select_character(name))
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)