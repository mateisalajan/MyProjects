from dataclasses import dataclass, field
from typing import Dict

from Characters.character import Character


@dataclass
class MeleeCharacter(Character):
    extra_base_hp: int = 50
    extra_base_dm: int = 50
    extra_inventory: Dict[str, int] = field(default_factory=lambda: {"sword": 1, "rage_potions": 3}, compare=False)

    def __post_init__(self):
        self.hp += self.extra_base_hp
        self.damage += self.extra_base_dm
        for item, quantity in self.extra_inventory.items():
            if item not in self.inventory:
                self.inventory[item] = quantity

    def __str__(self):
        return f"MeleeCharacter(name='{self.name}', hp={self.hp}, damage={self.damage}, " \
               f"inventory={self.inventory})"
