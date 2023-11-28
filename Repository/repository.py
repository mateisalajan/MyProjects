from typing import Type, Union, Optional, List

import jsonpickle

from Characters.character import Character
from Exceptions.name_error import NoSuchNameError, DuplicateNameError


class RepositoryJsonC:
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.characters = {}

    def __readFile(self):
        try:
            with open(self.filename, "r") as f:
                file = f.read()
                return jsonpickle.loads(file)
        except Exception:
            return {}

    def __writeFile(self):
        with open(self.filename, "w") as f:
            f.write(jsonpickle.dumps(self.characters, indent=2))

    def read(self, character_name=None) -> Type[Union[Optional[Character], List[Character]]]:
        self.characters = self.__readFile()
        if character_name is None:
            return list(self.characters.values())

        if character_name in self.characters:
            return self.characters[character_name]
        else:
            return None

    def add(self, character: Character) -> None:
        self.characters = self.__readFile()
        if self.read(character.name) is not None:
            raise DuplicateNameError("There is already a character with the same name!")
        self.characters[character.name] = character
        self.__writeFile()

    def delete(self, character_name: str) -> None:
        self.characters = self.__readFile()
        if self.read(character_name) is None:
            raise NoSuchNameError("There is no character with that name!")
        del self.characters[character_name]
        self.__writeFile()

    def update(self, character: Character) -> None:
        self.characters = self.__readFile()
        if self.read(character.name) is None:
            raise NoSuchNameError("There is no character with that name!")
        self.characters[character.name] = character
        self.__writeFile()
