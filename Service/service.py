from Characters.character import Character
from Characters.mage import MageCharacter
from Characters.melee import MeleeCharacter
from Repository.repository import RepositoryJsonC
from Characters.character_validator import CharacterValidator
from typing import List


class Service:
    def __init__(self, character_repo: RepositoryJsonC, character_val: CharacterValidator):
        self.character_repo = character_repo
        self.character_val = character_val

    def add_character(self, name: str, option: str) -> None:
        if option == "melee":
            character1 = MeleeCharacter(name)
            self.character_val.validate(character1)
            self.character_repo.add(character1)
        if option == "mage":
            character2 = MageCharacter(name)
            self.character_val.validate(character2)
            self.character_repo.add(character2)

    def update_character(self, name: str) -> None:
        character = Character(name)
        self.character_val.validate(character)
        self.character_repo.update(character)

    def delete_character(self, name: str) -> None:
        self.character_repo.delete(name)

    def get_all(self) -> List[Character]:
        return self.character_repo.read()

    def select_character(self, character_name=None) -> [Character]:
        return self.character_repo.read(character_name)
