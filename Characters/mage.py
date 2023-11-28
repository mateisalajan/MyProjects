from dataclasses import dataclass, field
from typing import Dict

from Characters.character import Character


@dataclass
class MageCharacter(Character):
    extra_base_dm: int = 80
    extra_inventory: Dict[str, int] = field(default_factory=lambda: {"staff": 1, "special_spell": 3}, compare=False)

    def __post_init__(self):
        self.damage += self.extra_base_dm
        for item, quantity in self.extra_inventory.items():
            if item not in self.inventory:
                self.inventory[item] = quantity

    def __str__(self):
        return f"MageCharacter(name='{self.name}', hp={self.hp}, damage={self.damage}, " \
               f"inventory={self.inventory})"
