from Characters.character import Character
from Exceptions.character_error import CharacterError
from dataclasses import dataclass


@dataclass
class CharacterValidator:

    @staticmethod
    def validate(character: Character):
        if character.name is None:
            raise CharacterError("Character name can not be empty!!")
